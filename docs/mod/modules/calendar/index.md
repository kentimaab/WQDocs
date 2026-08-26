---
title: Calendar
description: Visual overview of events and maintenance deadlines in month, week and day views.
product: mod
page_type: concept
doc_id: DOC-M13
size: M
priority: p0
status: draft
last_reviewed: 2026-08-25
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Calendar

The Calendar module provides a visual overview of events and upcoming maintenance deadlines. It supports three view modes (month, week and day) and can be navigated forward and backward through time.

Events come from three sources: custom events created directly in the calendar, maintenance deadlines pulled automatically from the [Maintenance module](../maintenance/index.md), and external calendars added as subscriptions. A configurable reminder is shown a set number of days before each maintenance deadline.

A subscription can be a live ICS feed, a local `.ics` file, or a country's public holidays. Holiday subscriptions also feed a daily classification to time channels, so PLC-side schedules can react to which days are holidays.

## Contents { #contents }

### [Get started](get-started.md) { #get-started }
* [**Views**](get-started.md#views) — Month, week and day view modes.
* [**Sidebar**](get-started.md#sidebar) — Mini calendar and upcoming events list.
* [**Creating an Event**](get-started.md#creating-an-event) — How to add a new calendar event.

---

### [Configuring](configuring.md) { #configuring }
* [**Events**](configuring.md#events) — Creating, editing and deleting events.
* [**Maintenance Events**](configuring.md#maintenance-events) — How maintenance deadlines appear and what the colors mean.
* [**Reminders**](configuring.md#reminders) — Configuring the reminder offset for maintenance deadlines.
* [**Calendar Subscriptions**](configuring.md#calendar-subscriptions) — Importing, exporting, filtering and editing external calendars.
* [**Importing a Calendar**](configuring.md#importing-a-calendar) — Adding a feed, a local file or a country's public holidays.
* [**Exporting a Calendar**](configuring.md#exporting-a-calendar) — Writing events to a file or sending them by email.

---

### [Extending](extending.md) { #extending }
* [**Reminder Offset**](extending.md#global-offset) — Changing the reminder offset in the database.
* [**Subscription Storage**](extending.md#subscription-storage) — The `ics_subscriptions` table and what each column holds.
* [**Fetching**](extending.md#fetching) — The REST plugin, conditional requests and the transport restrictions.
* [**Public Holiday Import**](extending.md#public-holiday-import) — Where holiday data comes from and how the country list is built.
* [**Holiday-aware Time Channels**](extending.md#holiday-aware-time-channels) — Handing the daily holiday classification to time channels.
* [**Script Reference**](extending.md#script-reference) — The `scHoliday` functions behind the subscription views.

---

### [Troubleshooting](troubleshooting.md) { #troubleshooting }
* [**Common Issues**](troubleshooting.md) — Common issues and how to fix them.
<!-- --8<-- [end:body] -->
