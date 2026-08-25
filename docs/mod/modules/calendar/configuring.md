---
title: Calendar - Configuring
description: Configure events, maintenance colors and reminder settings in the Calendar module.
product: mod
page_type: howto
doc_id: DOC-M13
status: draft
last_reviewed: 2026-08-25
---
<!-- --8<-- [start:body] -->

# Calendar - Configuring

## Events { #events }

Custom calendar events are created, edited and deleted directly in the calendar. They are stored in the maintenance database alongside maintenance data.

When creating or editing an event, a color can be selected from a fixed set of options: **ENERGY**, **POWER**, **SYSTEM**, **SAFETY**, **SECURITY**, **HVAC**, **WATER**, **DEFAULT**. These colors are defined in the **CalendarColors** theme in `Themes.kdat`.

**Editing an event:**

Click an existing event to open the **Add/Edit Calendar Event** popup. All fields can be updated. Click **Save** to apply the changes.

**Deleting an event:**

Open the event and click **Remove**. This removes the event permanently.

![Add/Edit Calendar Event popup](/docs/Images/Calendar/edit-event-popup.png){align=center}

## Maintenance Events { #maintenance-events }

Maintenance deadlines from the [Maintenance module](../maintenance/index.md) are automatically shown in the calendar. They are read-only and cannot be edited or deleted from the calendar. Changes must be made in **Maint. - List**.

Each maintenance event is displayed on the day of its deadline. The color is set automatically based on the task's current status — it cannot be chosen manually. These colors are defined in the **MaintenanceColors** theme in `Themes.kdat` and are separate from the colors used for custom calendar events.

Clicking a maintenance event opens a popup showing the object, status, deadline and maintenance type. Click **Open editing** to navigate directly to that task in **Maint. - List**.

| Status | Color |
|---|---|
| Planned | Yellow |
| Missed | Dark red |
| Stopped | Gray |
| Reminder | Muted olive |

![Maintenance events with different status colors in month view](/docs/Images/Calendar/maintenance-event-colors.png){align=center}

## Reminders { #reminders }

A reminder event can appear in the calendar a set number of days before a maintenance deadline. The reminder appears as a separate entry with the color **Reminder**, distinct from the deadline event itself.

Reminders are enabled by default for tasks created without a template. Tasks created from a template use that template's reminder setting, which defaults to off. The default reminder offset is 3 days. See [Extending](extending.md#reminder-configuration) for how to change these settings.

## Calendar Subscriptions { #calendar-subscriptions }

Alongside events created in the calendar itself, the calendar can show events from external ICS sources. Each source is a subscription. Every imported event is tagged with the subscription it came from, so subscriptions can be synced, recoloured and removed independently without affecting each other or the events created locally.

Subscriptions are managed from three pop-outs reached from the calendar: **ImportCalendar** to add one, **EditCalendars** to change or remove one, and **CalendarFilter** to choose which ones are shown.

### Importing a Calendar { #importing-a-calendar }

**ImportCalendar** offers three ways to add a subscription:

* **Feed URL** — subscribes to a live ICS feed, for example an Outlook or Google calendar published as `.ics`. The feed is re-fetched on a schedule.
* **Local file** — picks an `.ics` file from disk. The file is re-read from that path on every sync, so replacing the file on disk updates the calendar.
* **Public holidays** — imports a country's public holidays. The country is chosen from a combo box listing the languages configured in the project.

A subscription is rejected if its name or its address matches one that already exists. The comparison ignores surrounding whitespace and a trailing slash, so `https://example.com/basic.ics` and `https://example.com/basic.ics/` count as the same feed.

!!! info "Where the holiday data comes from"
    Public holidays are read from the Nager.Date JSON API. The current year and the next two are fetched, so a time channel's daily classification keeps working past New Year without a rollover step.

    The country list is derived from `Languages.kdat`, so it follows whichever languages the project has configured. Arabic is deliberately excluded. See [Extending](extending.md#public-holiday-import) for the details.

### Managing Imported Calendars { #managing-imported-calendars }

**EditCalendars** lists every subscription and allows it to be renamed, recoloured or removed. It also shows how many events each subscription currently contributes. Removing a subscription deletes its events from the calendar. Events created directly in the calendar are not affected.

Imported calendars are created with the **DEFAULT** colour. A public-holiday import keeps the **HOLIDAY** colour instead.

!!! warning "Changing a calendar to or from Holiday"
    The **HOLIDAY** colour is what marks a subscription as a holiday source. Changing a calendar to Holiday connects it to the time channel hand-off, and changing it away disconnects it. A warning is shown before the change is applied. See [Holiday-aware Time Channels](extending.md#holiday-aware-time-channels).

### Choosing Which Calendars Are Shown { #choosing-which-calendars-are-shown }

**CalendarFilter** controls which subscriptions are drawn in the calendar. The setting is global rather than per-user, so it applies to every client. Events created directly in the calendar are always shown and are not affected by the filter.

### Exporting a Calendar { #exporting-a-calendar }

**ExportCalendar** writes events out to an `.ics` file. Select which subscriptions to include, and whether to include the events created directly in the calendar.

## Next Steps { #next-steps }

* [Extending](extending.md) — reminder offset configuration and calendar subscriptions
<!-- --8<-- [end:body] -->
