---
title: Calendar - Extending
description: Reminder configuration, the holiday variables and the subscription table.
product: mod
page_type: extending
doc_id: DOC-M13
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Calendar - Extending

## Reminder Configuration { #reminder-configuration }

There is currently no UI for reminder settings. Both can be set from a script.

### Global Offset { #global-offset }

The number of days before a deadline that a reminder event appears. Default is 3 days. Use `scMaintenance.setReminderOffset` and pass the value in milliseconds:

```javascript
var days = 5;
scMaintenance.setReminderOffset(days * 24 * 60 * 60 * 1000);
```

### Per-Template Toggle { #per-template-toggle }

Controls whether reminders are generated for tasks created from a specific template. Default is off. There is no helper function for this. Update the `maintenanceLog_templates` table directly and call `updateTemplates()` to refresh the in-memory cache so the calendar picks up the change immediately:

```javascript
var templateType = "Filterbyte";
var current = scMaintenance.getAllTemplatesMap()[templateType];
var newVal = (current && current.reminder_enabled === 1) ? 0 : 1;
DatabaseConnections["maintenance"].exec(
    "UPDATE maintenanceLog_templates SET reminder_enabled = " + newVal + " WHERE type = '" + templateType + "'"
);
scMaintenance.updateTemplates();
```

Tasks created without a template always generate reminders regardless of this setting.

## Holiday Variables { #holiday-variables }

The `scHoliday` script classifies the current day and publishes the result to two boolean variables in the Data Store.

| Variable | Set when |
|---|---|
| `isHoliday` | A calendar event carrying the **HOLIDAY** colour covers today. |
| `isHolidayEve` | A calendar event carrying the **HOLIDAYEVE** colour covers today. |

A holiday event is stored with `Holiday` in the `object` column of `CalendarEvents`, and a holiday eve with `HolidayEve`. That marker is what the classification matches on, and it is set by the colour chosen on the event.

The test is an overlap test rather than a start-date test, so a multi-day holiday sets the flag on every day it covers rather than only on the first.

`refreshHolidayStateVariables()` writes both. It runs at startup and on every poll.

!!! warning "The flag turns over on the poll, not at midnight"
    Both variables are refreshed by the hourly poll, which starts counting from application start rather than from midnight. The change of day therefore lands up to an hour into the new day.

    A schedule that has to act exactly at midnight should not read the flag as its only trigger. Where the exact moment matters, call `refreshHolidayStateVariables()` from a schedule of the project's own at the time required.

!!! note "Server only"
    The poll is guarded with `if (System.remote) return`, so it runs on the server rather than on every connected client. The variables themselves are readable everywhere.

## Subscription Storage { #subscription-storage }

Imported calendars are stored in the `ics_subscriptions` table in the maintenance database. The table is created on first use, and columns added in later versions are added on start, so an existing project upgrades itself.

| Column | Purpose |
|---|---|
| `id` | Primary key. Every imported event is tagged with it, so an import can be recoloured and deleted independently. |
| `name` | Display name shown in **Edit calendars** and **Calendar filter**. |
| `url` | The file path the calendar was imported from. |
| `etag`, `lastModified` | Cached response validators. Unused in this build. |
| `isBuiltin` | Marked an authoritative holiday source. No import sets it in this build. |
| `type` | `file` for an imported `.ics` file. |
| `visibleInCalendar` | Whether the import is drawn in the calendar. Set from **Calendar filter**. |
| `color`, `colorOverridden` | A colour chosen in **Edit calendars**. `colorOverridden` is the actual signal. When it is `0`, `color` is stale and the type-based default still applies. |

!!! info "Rows of a retired type"
    A database carried over from a build that included the REST plugin can still hold `url` and `nager` rows. A sync skips them and writes a note to the log rather than failing. Their events stay in the calendar until the subscription is removed in **Edit calendars**.

## Script Reference { #script-reference }

| Function | Purpose |
|---|---|
| `importFileSubscription(path)` | Adds an import for a local `.ics` path and reads it immediately. The name defaults to the filename without its extension. |
| `addSubscription(name, url, isBuiltin, type)` | Adds a subscription row. Returns `duplicate_name` or `duplicate_url` if one already matches. |
| `listSubscriptions()` | Returns every subscription. |
| `getSubscription(id)` | Returns one subscription. |
| `syncSubscription(id)` | Re-reads one import. |
| `syncAllSubscriptions()` | Re-reads every import. |
| `renameSubscription(id, newName)` | Renames an import. |
| `setSubscriptionColor(id, color)` | Overrides an import's event colour. |
| `setSubscriptionVisibility(id, visible)` | Sets whether the import is drawn in the calendar. |
| `countSubscriptionEvents(id)` | Returns how many events an import currently contributes. |
| `removeSubscription(id)` | Removes an import and its events. |
| `holidayExists(startMs)` | True when a holiday event covers the given day. |
| `holidayEveExists(startMs)` | True when a holiday eve event covers the given day. |
| `refreshHolidayStateVariables()` | Writes `isHoliday` and `isHolidayEve` for the current day. |
| `snapToWholeDays(startMs, endMs)` | Widens a span to cover whole days. Applied when a holiday event is saved. |
| `exportCalendarToIcs(path, subscriptionIds, includeNative)` | Writes selected imports, and optionally locally created events, to an `.ics` file. |
| `parseICS(icsText)` | Parses ICS text into events. Shared by import and by any future feed source. |

<!-- --8<-- [end:body] -->
