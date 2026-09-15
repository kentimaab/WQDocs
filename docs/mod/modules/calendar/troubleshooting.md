---
title: Calendar
description: Common issues and solutions for the Calendar module.
product: mod
page_type: troubleshooting
doc_id: DOC-M13
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Calendar

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| No events appear in the calendar | Confirm that the maintenance database connection is active. Both custom calendar events and maintenance deadlines are read from the same database. If the connection is down, the calendar will load but show no events. |
| Maintenance events do not appear | Check that the `scMaintenance` script is running. The calendar reads maintenance deadlines by calling `scMaintenance` functions at load time. If `scMaintenance` is not available, maintenance events are skipped. |
| Events from a previous period still show after navigating | The calendar clears and re-renders all events when navigating to a new period. If stale events appear, reload the view. If the issue persists, check whether multiple `CalendarManager` instances have been created for the same view, as this can cause duplicate rendering. |
| The calendar is blank after opening | The `CalendarManager` initializes on view load. If the view loads before the maintenance database connection is ready, the event loading step may fail silently. Check the `scAlert` log for errors from `CalendarService` or `CalendarManager`. |
| There is no option to subscribe to an ICS link | Live feeds require the REST plugin, which is not part of this build. Import a local `.ics` file instead, and mark holidays in the calendar itself. |
| There is no option to import public holidays | Public holiday import required the same plugin. Mark holidays by creating events with the **HOLIDAY** colour. See [Holidays and Holiday Eves](configuring.md#holidays-and-holiday-eves). |
| An imported calendar shows no events | Check that the import is enabled in **Calendar filter**. An import that is not visible is still stored but is not drawn. Then check the `scAlert` log for `scHoliday` errors. |
| An edited local `.ics` file does not show its changes | A file is read at import and is not re-checked afterwards. Import the file again to pick up the new content. |
| An import cannot be added | Adding is rejected when the name or the path already belongs to another import. The comparison ignores surrounding whitespace and a trailing slash. |
| A subscription is skipped during sync with a note in the log | The database holds a `url` or `nager` row from a build that included the REST plugin. Those types cannot be fetched in this build. Remove the subscription in **Edit calendars** if its events are no longer wanted. |
| `isHoliday` is not set on a day marked as a holiday | Confirm the event carries the **HOLIDAY** colour rather than another colour, since the colour is what marks the day. Then check that the day falls inside the event's span. |
| `isHoliday` changes an hour or so into the day | Expected. Both holiday variables are refreshed by the hourly poll, which counts from application start rather than from midnight. See [Holiday Variables](extending.md#holiday-variables). |
| A holiday eve does not set `isHoliday` | The two are separate by design, because a holiday eve is usually a shortened working day rather than a closed one. Read `isHolidayEve` for it, or read both where the same behaviour is wanted. |
| A multi-day holiday only marks its first day | The classification uses an overlap test, so every covered day is marked. If only the first day is marked, check that the event's end date is set as intended. A holiday event is snapped to whole days when saved. |
| A holiday does not reach the PLC | The variables carry the classification but do not send it. Connect `isHoliday` and `isHolidayEve` to outputs the same way as any other value. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
