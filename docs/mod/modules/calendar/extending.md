---
title: Calendar - Extending
description: Extend the Calendar module and troubleshoot common issues.
product: mod
page_type: extending
doc_id: DOC-M13
status: draft
last_reviewed: 2026-08-25
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

Controls whether reminders are generated for tasks created from a specific template. Default is off. There is no helper function for this — update the `maintenanceLog_templates` table directly and call `updateTemplates()` to refresh the in-memory cache so the calendar picks up the change immediately:

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

## Calendar Subscriptions { #calendar-subscriptions }

Calendar subscriptions are handled by the `scHoliday` script. All three import paths share one parser and one write path, so a feed, a local file and a public-holiday import produce events in the same shape.

### Subscription Storage { #subscription-storage }

Subscriptions are stored in the `ics_subscriptions` table in the maintenance database. The table is created on first use, and columns added in later versions are added on start, so an existing project upgrades itself.

| Column | Purpose |
|---|---|
| `id` | Primary key. Every imported event is tagged with it, so subscriptions can be synced and deleted independently. |
| `name` | Display name shown in **EditCalendars** and **CalendarFilter**. |
| `url` | The feed URL for `url`, the file path for `file`, and the ISO 3166-1 alpha-2 country code for `nager`. |
| `etag`, `lastModified` | Cached response validators for conditional requests. Unused for `file` and `nager`. |
| `isBuiltin` | Marks an authoritative holiday source. |
| `type` | `url`, `file` or `nager`. |
| `visibleInCalendar` | Whether the subscription is drawn in the calendar. Set from **CalendarFilter**. |
| `color`, `colorOverridden` | A colour chosen in **EditCalendars**. `colorOverridden` is the actual signal. When it is `0`, `color` is stale and the type-based default still applies. |

### Subscription Types { #subscription-types }

| Type | Source | Sync behaviour |
|---|---|---|
| `url` | A live ICS feed fetched over HTTP or HTTPS. | Conditional request using the cached `ETag` and `Last-Modified`. An unchanged feed answers `304` and is not re-parsed. |
| `file` | A local `.ics` file. | Re-read from disk on every sync. There are no HTTP semantics to cache, so the file is always re-parsed. |
| `nager` | A country's public holidays. | Re-fetched on every sync. |

Subscriptions are polled once an hour. The interval is held in `scHoliday.pollIntervalMs`.

### Fetching { #fetching }

Feeds are fetched through the `WideQuickRestPlugin` CAPI plugin, registered in **WideQuick® Designer** as `REST` in `ScriptPlugins.kdat`.

!!! warning "Transport restrictions"
    The REST plugin accepts HTTP and HTTPS only. A `file://` URL is rejected, so a subscription address cannot be used to read local files back into the script. Local files are imported through the `file` subscription type instead.

    Redirects are followed only to HTTPS and are capped at five hops. A response body larger than 16 MB is rejected, both from `Content-Length` up front and while streaming. The connect timeout is 10 seconds, so a single unreachable feed does not stall the whole sync.

Names, URLs and paths are stripped of embedded carriage returns and line feeds before they are stored or sent. An embedded newline is how a pasted value turns into a request-line or header injection, which typically surfaces as a hard-to-diagnose `400 Bad Request`.

### Public Holiday Import { #public-holiday-import }

The `nager` type reads public holidays from the Nager.Date JSON API:

```text
https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}
```

The current year and the next two are fetched. Fetching three years ahead means a time channel's daily classification keeps working well past New Year without an exact rollover-day fix. A year that is not published yet is not treated as fatal, as long as the current year succeeded.

The JSON API is used deliberately rather than Nager.Date's own ICS endpoint, because that endpoint redirects to a different domain that is commonly blocked.

Each holiday's title takes the native name, falling back to the English name when no native name is given. The English name is written to the description only when it adds something beyond the title.

The country list comes from `scHoliday.getLanguageCountries()`, which reads `Languages.kdat` and takes the country code from each language's `LocaleUnix` value, so `sv_SE` yields `SE`. This avoids maintaining a second hardcoded list alongside the project's languages.

!!! note "Arabic is excluded"
    Arabic is the one entry whose locale (`ar_AR`) is not a real per-country locale. Deriving a code from it the same way as every other entry would produce `AR`, which is Argentina's actual code, so it would silently import the wrong country's holidays. It is skipped rather than mapped.

### Holiday-aware Time Channels { #holiday-aware-time-channels }

`scHoliday` classifies each day and hands the result to the `TimeChannel` objects that have opted in, through the `Tidkanal` suffix category.

The hand-off only reports which day-type bucket applies today. The PLC's own time-channel firmware still owns the actual on and off schedule evaluation. Only a subscription marked as an authoritative holiday source takes part, which is what a public-holiday import creates.

### Script Reference { #script-reference }

| Function | Purpose |
|---|---|
| `addSubscription(name, url, isBuiltin, type)` | Adds a subscription. Returns `duplicate_name` or `duplicate_url` if one already matches. |
| `importFileSubscription(path)` | Adds a `file` subscription for a local `.ics` path and syncs it immediately. The name defaults to the filename without its extension. |
| `importHolidays(countryCode, name)` | Find-or-create plus sync for a country's public holidays. |
| `getLanguageCountries()` | Returns `{name, countryCode}` pairs derived from `Languages.kdat`, for populating the country picker. |
| `listSubscriptions()` | Returns every subscription. |
| `syncSubscription(id)` | Syncs one subscription. |
| `syncAllSubscriptions()` | Syncs every subscription. |
| `renameSubscription(id, newName)` | Renames a subscription. |
| `setSubscriptionColor(id, color)` | Overrides a subscription's event colour. |
| `setSubscriptionVisibility(id, visible)` | Sets whether the subscription is drawn in the calendar. |
| `countSubscriptionEvents(id)` | Returns how many events a subscription currently contributes. |
| `removeSubscription(id)` | Removes a subscription and its events. |
| `exportCalendarToIcs(path, subscriptionIds, includeNative)` | Writes selected subscriptions, and optionally locally created events, to an `.ics` file. |

<!-- --8<-- [end:body] -->
