---
title: Calendar
description: Common issues and solutions for the Calendar module.
product: mod
page_type: troubleshooting
doc_id: DOC-M13
status: draft
last_reviewed: 2026-08-25
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
| An imported calendar shows no events | Check that the subscription is enabled in **CalendarFilter**. A subscription that is not visible is still synced but is not drawn. Then confirm the source itself still returns events, and check the `scAlert` log for `scHoliday` errors. |
| A subscription cannot be added | Adding is rejected when the name or the address already belongs to another subscription. The comparison ignores surrounding whitespace and a trailing slash, so a feed added twice with and without a trailing slash counts as a duplicate. |
| A feed URL is rejected | The REST plugin accepts HTTP and HTTPS only. A `file://` address is rejected by design. Import a local file with the **Local file** option, which creates a `file` subscription instead. |
| A feed stops updating after moving host | Redirects are followed only to HTTPS and only up to five hops. A feed that redirects to plain HTTP, or through a longer chain, is not followed. Update the subscription to the final address in **EditCalendars**. |
| A large feed never imports | A response body above 16 MB is rejected, both from `Content-Length` and while streaming. Narrow the feed's date range at the source, or export it to a file and import that instead. |
| Holidays are missing for next year | The holiday import fetches the current year and the next two. A year that the source has not published yet is skipped without failing the sync. Re-sync once the source publishes it. |
| Holidays import for the wrong country | The country list is derived from the locales in `Languages.kdat`. Confirm the language entry's `LocaleUnix` value ends in the intended country code. |
| The time channel holiday flag is not set | Only a subscription marked as an authoritative holiday source feeds the classification. Confirm the calendar carries the **HOLIDAY** colour, and see [Holiday-aware Time Channels](extending.md#holiday-aware-time-channels). |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
