---
title: Calendar
description: Common issues and solutions for the Calendar module.
product: mod
page_type: troubleshooting
doc_id: DOC-M13
status: draft
last_reviewed: 2026-06-08
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

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
