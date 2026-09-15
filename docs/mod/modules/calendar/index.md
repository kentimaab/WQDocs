---
title: Calendar
description: Visual overview of events and maintenance deadlines in month, week and day views.
product: mod
page_type: concept
doc_id: DOC-M13
size: M
priority: p0
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Calendar

The Calendar module provides a visual overview of events and upcoming maintenance deadlines. It supports three view modes (month, week and day) and can be navigated forward and backward through time.

Events come from three sources: events created directly in the calendar, maintenance deadlines pulled automatically from the [Maintenance module](../maintenance/index.md), and events imported from a local `.ics` file. A configurable reminder is shown a set number of days before each maintenance deadline.

Days can be marked as holidays and holiday eves. The calendar publishes that classification to two internal variables, which can be handed on to a PLC or DUC so its own schedules react to the day type.

!!! info "Live calendar feeds are not part of this release"
    Subscribing to an ICS link and importing a country's public holidays both require the REST plugin, which is not included. Importing from a local `.ics` file is available, and holidays are marked in the calendar itself. See [Importing a Calendar](configuring.md#importing-a-calendar).

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
* [**Holidays and Holiday Eves**](configuring.md#holidays-and-holiday-eves) — Marking a day and handing the classification to a PLC.
* [**Importing a Calendar**](configuring.md#importing-a-calendar) — Adding events from a local `.ics` file.
* [**Managing Imported Calendars**](configuring.md#managing-imported-calendars) — Renaming, recolouring, filtering and removing.
* [**Exporting a Calendar**](configuring.md#exporting-a-calendar) — Writing events to a file or sending them by email.

---

### [Extending](extending.md) { #extending }
* [**Reminder Configuration**](extending.md#reminder-configuration) — Changing the reminder offset and the per-template toggle.
* [**Holiday Variables**](extending.md#holiday-variables) — `isHoliday`, `isHolidayEve` and how they are refreshed.
* [**Subscription Storage**](extending.md#subscription-storage) — The `ics_subscriptions` table and what each column holds.
* [**Script Reference**](extending.md#script-reference) — The `scHoliday` functions behind import, export and the holiday classification.

---

### [Troubleshooting](troubleshooting.md) { #troubleshooting }
* [**Common Issues**](troubleshooting.md) — Common issues and how to fix them.
<!-- --8<-- [end:body] -->
