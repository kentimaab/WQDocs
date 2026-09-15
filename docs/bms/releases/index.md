---
title: Releases - BMS
description: Release notes for WideQuick BMS.
product: bms
page_type: release
status: draft
last_reviewed: 2026-09-15
tags: 
 - BMS
---

# Releases - BMS

Release notes for WideQuick BMS. The newest release is listed first and expanded;
older releases are collapsed, click a release to expand it. Each release is built on
a specific WideQuick Modular Framework version, linked under its heading. For the full
framework changelog see the [MOD releases](../../mod/releases/index.md).


## WideQuick BMS 2026.1.2 { #bms-2026-1-2 }

__Released 2026-08-20__
Modular Framework Version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0)
<details class="release" markdown="1" open>
<summary>Release notes</summary>

### New features

| Feature | Description |
|---|---|
| **Calendar import and export** | Events can be imported into the calendar from a local `.ics` file and exported back out to one. Each import is kept as its own subscription in a new `ics_subscriptions` table, so it can be renamed, recoloured, hidden or removed as a unit without touching events created directly in the calendar. An import is read once at import time. Adds the **ImportCalendar**, **ExportCalendar**, **EditCalendars** and **CalendarFilter** views. |
| **Holidays and holiday eves** | A day is marked as a holiday by creating a calendar event on it with the **HOLIDAY** colour, and as a holiday eve with **HOLIDAYEVE**. Such an event is snapped to whole days when saved. The daily classification is published to two internal Data Store variables, `isHoliday` and `isHolidayEve`, which can be connected to an output so a PLC or DUC runs its own schedules against the day type. The classification is a property of the day rather than a value written into each time channel's own registers, so one pair of variables serves every schedule. The match is an overlap test, so a multi-day holiday marks every day it covers. |
| **Logbook archive** | Logbook entries can be archived instead of deleted. The `logbook` table gains an `archived` column, the filter gains a **Visa arkiverade** toggle, and a new `Logbook_Archive` privilege controls who may archive an entry. The privilege defaults to denied, so it must be granted to a role before anyone can archive. The settings view gains an action that permanently deletes every archived note. |
| **Report units and prefixes** | Reports carry a display unit. The report controllers gained **Unit** and **Prefix** pickers, and every selected signal gets its own scale factor, calculated from that signal's own prefix and the chosen unit. The values are queried in the unit they were logged in, and the factors travel to the template alongside the data, landing on its **Meta** sheet as `Factor1` to `Factor15`, where the template applies the scaling. One signal logged in `Wh` and another already in `kWh` therefore report on the same scale. The **Unit** list is not a fixed set. It is built from the units of the signals on the report's logger, reduced to their SI base, so only units the data actually contains are offered. Selecting a unit filters the signal tree to signals of that dimension, and the tree stays disabled until a unit is chosen. Filtering is opt-in per controller: a report view without the `Unit` object leaves the tree unfiltered and sends values in their native units. Prefixes on `m³` apply to the metre, so `dm³` is a thousandth of `m³` rather than a tenth. `ReportQueue`, `reportStats` and `reportSchedules` gain `unit` and `factorArray` columns, added automatically on first start so existing databases migrate themselves. |
| **Delta reports** | Two new report controllers, **Delta_Week** and **Delta_Year**, report the change over a period rather than the logged values themselves. They are intended for meters that report a continuously increasing total. **Delta_Week** presents a daily delta per column, one column per weekday, and accepts logging intervals from hourly to daily. **Delta_Year** presents a monthly delta per column, one column per month, using the `DeltaYear_H.xlsx` template that accepts intervals from monthly down to hourly. Both accept up to 15 signals. They ship with new Excel templates (`DeltaWeek.xlsx`, `DeltaYear_H.xlsx`) alongside reworked `EnergyReport.xlsx` and `WeeklyEnergyReport.xlsx`. |
| **Remote client list** | A new `scRemoteClients` script counts the remote clients connected to the application. A remote client can request the connected-client detail list, which the server returns over RPC to the requesting client only. The list is never stored. Adds the `RemoteClients.kvie` pop-out. |
| **Alarm notification criteria** | Outbound alarm notifications can be filtered by alarm state. The `mail_schedules` table gains a `criteria` column accepting `all`, `active`, `acknowledged`, `unacknowledged` and `inactive`, added automatically on first start and defaulting to `active` so existing schedules keep sending on the same alarm state as before. The alarm schedule treeview shows which alarm classes and which criteria each schedule monitors. |
| **Map lines and pipes** | Lines and pipes can be drawn on a map alongside pins. Line geometry is defined on the `MainLine1`, `MediumLine1` and `SmallLine1` objects, and the `scMap` script was reworked to position them from geographic coordinates. |
| **Dashboard gauges** | Two gauge widgets, `Gauge_1x1` and `Gauge_2x2`, were added to `Dashboard Widgets.klib`. They present a single value as a dial, in a one-cell and a two-by-two dashboard size. |
| **Unused suffix view** | An **Inte kopplade variabler** button in the debug view opens the new `UnboundDebug.kvie`, listing every suffix that is not connected to a popup or a view. |
| **Logbook topic tree** | The logbook files an entry against a workview, an object, or a topic path of its own, and presents all three in a single tree. A toggle switches that tree between **workview** order, which follows the folder structure of the process views, and **signal** order, which follows the tag path. The two are linked through the object index, so a note on an object also appears under every view that object is drawn in, and a note on a view also appears under the objects drawn in it. Where two objects in the same view share a name, the leaf label is extended with as much of the tag as is needed to tell them apart. The `logbook` table gains `topic_kind` and `topic_ref`, derived from `topic` and re-derived on every start, and the entry list gains a **Placerad på** column naming what each entry is anchored to. The logbooks opened from an object popup and from a process view preselect their subject while leaving the rest of the tree reachable. |

---

### Improvements

| Area | Description |
|---|---|
| **Alarm Sender — acknowledging user** | Notifications now report which user acknowledged an alarm. Alarm state and the acknowledging user name are resolved from `wqlogg_larmlogg_alarm_data` rather than inferred from the live alarm object. |
| **Alarm details in description** | Each alarm's details are copied into its `description` property, making the text reachable outside alarm objects. |
| **Alarm schedule status** | **Larm - Schema** updates the number of schedules and their active state live instead of only on load. |
| **Maintenance log** | A **Rensa underhållsloggen** button clears every entry in the maintenance log. The action sits behind a confirmation dialog and the `Config` privilege. |
| **Alarm frequency** | **Larm - Frekvens** gained a **Filtrera** button that opens the alarm filter pop-out, so the frequency view can be narrowed the same way the alarm list is. |
| **Bar chart date order** | A new property renders the date axis right-to-left instead of left-to-right. |
| **Calendar import colours** | Imported calendars are created with the **DEFAULT** colour and can be recoloured in **EditCalendars**. The **HOLIDAY** and **HOLIDAYEVE** colours are what mark a day, so changing a calendar to or from either shows a warning first. |
| **Holidays on remote clients** | The `scHoliday` script is registered for remote clients. |
| **Theme-aware filters** | The alarm filter and the maintenance filter follow the active theme. |
| **Report scheduler follows the report system** | A scheduled report stores the same display unit and per-signal factors as a manually created one, selected in `ReportSchedule2.kvie`. |
| **Report signal check** | Creating a report is blocked until at least one signal is selected, the same check MOD and WWT already had. |
| **Calendar — overflow badge opens the day** | The month view's **Visa fler (N)** badge opens the Day view for that date, where every event of the day is visible. Overflowing events are never drawn in the month cell itself. |
| **Calendar — week and day event names** | Events sharing an identical span were drawn as stacked bars with their names on top of each other. A column holding more than one event now collapses to a single bar labelled **Visa händelser (X)**, which opens a picker listing everything it stands for. |
| **Alarm overview text length** | Long alarm texts are held to the width of the alarm overview widget instead of stretching it. |
| **Settings icons** | Settings icons ship in gray and white variants so they follow the active theme. |
| **Speed dial** | The `SpeedDialRight` object was drawn out of proportion. Its element widths and offsets were corrected. |
| **Object property descriptions** | Property descriptions appear as help text in **WideQuick® Designer**. The descriptions left empty on the valve objects were filled in, and the `ObjectName` example in `DynTouch` was missing its closing quotation mark, reading `"FS61` instead of `"FS61"`. |
| **`scPrototypes`** | Gained a `toUpperCase()` helper for use in project scripts. |
| **Alarm Sender — compact SMS** | An alarm schedule can send a compact message instead of the full per-alarm listing. A compact message carries the subject line, the event type and a comma-separated list of the alarms matching it, which keeps a notification covering many alarms within a sensible length. |
| **Prompt accepts Enter** | The prompt pop-out treats **Enter** as a confirmation, so a value can be typed and committed without reaching for the button. |
| **Quieter logs** | The application and error logs were cleaned up. Schema migrations in `scCalendar`, `scHoliday`, `scMaintenance` and `scSuffix` now check whether a column exists before adding it, rather than attempting the change and letting the SQLite driver report the failure into `Errors.log`. `scUsers.hasPriv()` denies instead of throwing when it is called without a privilege. Several hundred lines of recurring startup noise are gone. |

---

### Changes

| Area | Change |
|---|---|
| **Removed views and scripts** | The unused `CreateEnergyReport.kvie` was deleted and `scMapObjects.js` was removed from the project — a copy is kept in the resource pack should it be needed. |
| **Calendar feeds** | Events can now be imported into the calendar from a local `.ics` file. |

---

### Bugs

| # | Area | Description |
|---|---|---|
| 1 | Maintenance | A missed recurring deadline was dropped when no user was logged in, because the insert required a current user and threw instead. The creator now falls back to `System`. |
| 2 | Alarm Sender | The alarm description could be sent as the literal text `Undefined`. A guard now suppresses the field when no description is available. |
| 3 | Alarm list | `dslAlarms.onDataChanged()` could push the same alarm twice. The list is now scanned before a push, so duplicates are rejected. |
| 4 | Calendar | Events did not cover a whole day. A full-day event is now written at index 0 and index 48, so it spans the day. |
| 5 | Dashboard | Daylight saving transitions misaligned the bar chart. Fixed, together with grid and description rendering. |
| 6 | Map | `StatusPin` applied its dynamic status without checking the alarm objects, so a pin could show a state its object did not have. It now verifies against both the object list and the alarm objects. |
| 7 | Map | Lines and pipes were never drawn on a map. The `scMap` update calls were left disabled, and the geometry properties sat on the info popup instead of the line objects. The calls are now active, and the properties live on the `MainLine1`, `MediumLine1` and `SmallLine1` objects. Any values previously entered on the info popup need to be set again on the line objects. |
| 8 | Map | A pipe spanning a large geographic area computed its pixel offsets from a fixed `Line0` that could fall outside the visible frame, placing the pipe incorrectly. Offsets are now anchored to the corner of the visible frame. |
| 9 | Object library | The `CustomLabel` property had no effect on the nameplate of some objects. Fixed across the sensor, valve, speed dial and map indicator libraries, including their legacy variants. |
| 10 | Object library | Dampers reported NO and NC inverted, in both the current and the legacy damper libraries. Fixed. |
| 11 | Navigation | Menu buttons did not change colour when the theme was toggled, and a sub-navigation item that outlived its view broke the registration loop. A guard and an unregister step were added. |
| 12 | Navigation | In the full menu, **Back** on a paginated sub-navigation page only undid the last forward step, because paging was driven by a single previous-index value rather than a page history. The `scSubNavPopup` script now records the start index of every page, so **Back** steps back through the whole sequence. |
| 13 | Script libraries | `scAlarmFinder` was registered twice in `ScriptLibraries.kdat`, and error messages in `scAuditTrail` and `scMaintenance` still carried the old `scMaintenanceLog` prefix, pointing at the wrong script when something failed. The duplicate registration was removed and the prefixes corrected. |
| 14 | Alarm overview | The **error** layer could not cover the view because other objects sat above it. The object order was corrected. |
| 15 | Maintenance | `MaintenanceInfoPanel` was registered under a name that did not match its view file, and a stale `folder` entry was left in `SuffixConfig.db`. Both corrected. |
| 16 | Suffix settings | **Suffixalias - Popuper** keys its categories by their Swedish names while the tree shows them translated, so in any other language the settings fields resolved to nothing. The controls displayed but silently refused input, and selecting an item no longer filled in the combo boxes and text fields. The displayed label is now resolved back to its canonical key before use. Adding a category also rejects a name matching an existing category's translated label, which would otherwise create two entries that cannot be told apart. |
| 17 | Suffix settings | Creating a category reported an error and left the new category unselected, because the tree was searched using the raw typed name and a criterion the translated model can never match. The lookup now uses the label the node actually renders under, and skips the selection rather than throwing if the node cannot be found. |

---

### Translations

| Area | Change |
|---|---|
| **New project translation strings** | Logbook archive labels and the view controller popup, report schedule views, calendar import, export and edit views, the maintenance info panel and maintenance filter, alarm criteria labels, document and file picker labels, the login view, and report and damper library strings. |
| **Removed** | Dead source strings were pruned ahead of the new translation pass. |
| **Verified** | Translated strings were compared against the Swedish baseline to catch entries that had drifted from their source. |
| **Alarm criteria** | Criteria are displayed translated but stored as canonical keys. The `scAlarmSender` script untranslates the selected value before writing it to the database. |
| **Report strings** | The unit, prefix and delta report labels were added, and the misspelt "Excell" is now "Excel" throughout. |
| **Calendar collapse strings** | **Visa fler (N)** and **Visa händelser (X)** were added for the collapsed month, week and day events. |
| **Languages updated** | Arabic, Bulgarian, Croatian, Czech, Danish, English, Finnish, French, German, Hungarian, Italian, Mandarin, Norwegian, Polish, Portuguese (PT and BR), Romanian, Slovenian, Spanish, Swedish. |

---

### Library and view changes

| File | Change |
|---|---|
| `scHoliday.js` | Calendar import and export, shared ICS parser, holiday and holiday eve classification published to `isHoliday` and `isHolidayEve` |
| `scAlarmSender.js` | Criteria filtering, acknowledging user reporting, alarm state resolved from the alarm log, description guard, criteria untranslation |
| `scLogBook.js` | `archived` column, `deleteMark` retirement and cleanup, permanent delete of archived entries |
| `scRemoteClients.js` | New script — connected client count and RPC-served client list |
| `scMap.js` | Line and pipe handling, offsets anchored to the visible frame |
| `scMaintenance.js` | `System` fallback for unattended recurring inserts |
| `scDashboard.js` | Bar chart date order property, daylight saving correction, grid and description fixes |
| `scSubNavPopup.js`, `scThemes.js` | Theme recolouring of menu buttons, guard and unregister for stale sub-navigation items |
| `scAlarm.js` | Duplicate push guard in `dslAlarms.onDataChanged()` |
| `Privileges.kdat` | New `Logbook_Archive` privilege |
| `DataStore.kdat` | Alarm details copied into `description` |
| `ImportCalendar.kvie`, `ExportCalendar.kvie`, `EditCalendars.kvie`, `CalendarFilter.kvie` | Calendar import, export, edit and filter views |
| `UnboundDebug.kvie` | New view listing suffixes not connected to a popup or view |
| `RemoteClients.kvie` | New pop-out listing connected remote clients |
| `Logbook.kvie`, `LogBookFilter.kvie`, `LogbookViewControllerPopup.kvie` | Archive column, **Visa arkiverade** toggle, translated labels |
| `Larm - Schema.kvie`, `AlarmSchedule_1.kvie`, `AlarmSchedule_2.kvie` | Criteria selection, live schedule count and active status |
| `Spårningslogg - Underhåll.kvie` | **Rensa underhållsloggen** button |
| `Map Indicators.klib` | Line and pipe objects, `StatusPin` alarm object verification, `CustomLabel` fixes |
| `Dashboard Widgets.klib` | Gauge widgets, bar chart date order |
| `COMPONENTS.klib`, `COMPONENTS_Legacy.klib`, `DAMPERS_Legacy.klib` | Damper NO and NC corrections |
| `Valves.klib`, `Speed Dial.klib`, `DynTouch.klib` | Property descriptions filled in, `SpeedDialRight` proportions, `ObjectName` example corrected |
| `scReports.js`, `scReportScheduler.js` | Unit and SI prefix resolution, per-signal scale factors, `unit` and `factorArray` columns with their schema migrations, logger guard |
| `Report.klib` | Unit and prefix pickers, delta report support |
| `Delta_Week.kvie`, `Delta_Year.kvie` | New delta report controllers, with a signal-selected check before a report can be created |
| `ReportSchedule2.kvie` | Unit and prefix selection for scheduled reports |
| `Reports/Templates/*.xlsx` | New `DeltaWeek` and `DeltaYear_H` templates, reworked energy report templates |
| `Schedules.kdat` | Report schedule trigger corrected to `scReportScheduler` |
| `scCalendar.js` | Month view overflow badge opens the Day view for that date |
| `scWeekViewManager.js`, `scDayViewManager.js`, `Calendar.klib` | Week and day event collapse with **Visa händelser (X)** |
| `Loggers.kdat` | `*_Effekt` and `*_RPM` log values removed |
| `Larm - Översikt.kvie` | Object order so the error layer covers the view |
| `Translations.klib` | String additions, dead string removal, Swedish baseline verification |

</details>


## WideQuick BMS 2026.1.1 { #bms-2026-1-1 }

__Released 2026-07-08__ — Patch version BMS 2026.1.1.1
<details class="release" markdown="1">
<summary>Release notes</summary>

### Bugs

| # | Area | Description |
|---|---|---|
| 1 | Audit trail | The audit trail filter couldn't combine object, user, and time at the same time (it was capped at two conditions), and the row-count limit didn't reliably return the newest rows. Fixed with a single predicate-based filter. |
| 2 | Maintenance | Recurring tasks stored the interval unit in the active interface language, so the recurring offset could be skipped or misapplied when the language differed from when the task was created. Fixed by normalising units to a canonical form. |

---

### Library and view changes

| File | Change |
|---|---|
| `Spårningslogg.kvie` | Audit trail filter rewritten — predicate-based object/user/time filtering with a newest-N row limit |
| `scMaintenance.js` | Recurring interval units normalised to a canonical form for language-independent scheduling |

</details>


__Released 2026-07-02__
Modular Framework Version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0)
<details class="release" markdown="1">
<summary>Release notes</summary>

### New features

| Feature | Description |
|---|---|
| **Time Channel Profiles** (`scTimeChannel.js`) | A new script library that lets users save and load named time channel schedules. A profile captures the on/off values for all day types — weekdays, weekends, holidays, and up to three special days — for a given tag and stores them in the Config database for later reuse. |
| **History — Import from All** | New workview popup `ImportFromAll.kvie` under `Common_Popup/HistorikPopups/` for importing history signal groups from any part of the project. |
| **History — Import Saved Signals** | New workview popup `ImportSavedSignals.kvie` for importing from previously saved signal selections. |

---

### Improvements

| Area | Change |
|---|---|
| **Report Scheduler** | Reports can now be triggered at a specific time of day (±5 min accuracy). Three new database columns added to `reportSchedules`: `trigger_time`, `trigger_day`, and `trigger_month`. The `checkTrigger` logic was fully rewritten and `ReportSchedule1.kvie` updated with new UI controls. |
| **Map pins** | Map pins no longer use tooltip objects. They are now created with `createObject`, giving more display control and making them more stable in the web client. |
| **Map — folder navigation depth** | Navigation from map pins to folders was limited to 1 level deep. It can now navigate to any depth. |
| **Map — alarm text translation** | Alarm texts shown on map pin popups are now run through `Language.translate` so they respect the active language. |
| **Map — `mapView` property** | All internal `mapViews` references corrected to `mapView`. The map (`Karta.kvie`) no longer renders above the navigation bar in the web client. |
| **Dashboard — bar chart** | Bar chart now supports Days, Weeks, and Year grouping views. |
| **Dashboard — expanded view** | History set-time now applies to the expanded popup view. Pie, Bar, and History widgets now initialise on load via `scDashboard`. Expanded legend shows the current value at the ruler position and percentage where applicable. Fixed expanded list column widths being stretched by long content. |
| **Calendar** | Month names and day-of-week labels are now passed through `Language.translate` and match the selected interface language. |
| **Alarm Sender — slot 2** | Added `slot2_active` column to `mail_schedules` so each weekday can independently enable or disable its second time slot. |
| **Alarm Sender — day-of-week** | Fixed an off-by-one bug where `getDay()` misaligned all alarm days by one. A Monday-first index map is now used correctly. |
| **Alarm Sender — midnight send** | `00:00 – 00:00` time slots are now treated as disabled rather than triggering a midnight send. |
| **Alarm Sender — timer guard** | Timer delay now guards against a zero or negative `timeToSend` value, defaulting to a 2 second minimum. |
| **Alarm Schedule** | Editing an existing schedule no longer silently resets `emailActive` to 0. `00:00 to 00:00` is the default disabled state for new schedules. Buttons now follow the active theme. |
| **Alarm email and SMS** | All hardcoded Swedish labels are now passed through `Language.translate` so they appear in the user's active language. |
| **History / VySpecifikHistorik** | Can now load signal groups from other parts of the project. Signal list switched from a flat list to a TreeView. Maximum signal count lowered to improve performance. Tags that are not logged are now clearly indicated. |
| **Maintenance** | Added `reminder_enabled` field to maintenance templates. The UI now shows a reminder checkbox in the template editor. |
| **Documents and Maintenance** | Both modules now handle the tag structure format `C_c.D_d.S_o_s` in addition to previously supported formats. |
| **Documents — UI labels** | Document list group labels are now passed through `Language.translate`. |
| **Control Curve (Styrkurva)** | The popup now displays the current value on the curve. It can also be placed directly inside a workview screen rather than only as a popup. |
| **Control Curve Time (StyrkurvaTid)** | Brought to feature-parity with the standard Control Curve and visually overhauled. A vertical line tracks the current wall-clock time on the graph in real time; a horizontal line tracks the live Y0 process value. The X-axis label now appends the current HH:MM time. Data point boxes are arranged in two columns (previously a single column), supporting up to 24 visible points. The preview curve now also updates when Y-axis min/max changes, not only when data points are edited. |
| **Control Curve — independent clamp save/load** | Both Styrkurva and StyrkurvaTid now save and load the upper and lower clamp values independently. Previously, both clamp handles had to be visible for either value to be included in a saved profile. |
| **Control Curve — duplicate profile name prevention** | Renaming a profile to a name already used by another profile is now blocked. |
| **Control Curve — audit trail** | `Spårningslogg.kvie` updated with control curve audit trail support. |
| **Process popup** | Visual update with corrected element placement and spacing. |
| **Pop-out close** | Pop-outs opened via a link now use the correct close action instead of `app.popup.visible`. |
| **SubNav popup** | Now lazily initialises the subnav route tree on demand for correct behaviour on web clients. Default fallback view corrected to `Dashboard Energi.kvie`. |
| **Settings** | The Settings view now respects user privilege levels. |
| **`scPlatform`** | All timers now call `setSingleShot(true)` to prevent repeated firing after initial detection. |
| **Weather** | A data-change trigger was added so the weather widget refreshes automatically when the underlying data changes. |
| **"Email" label** | All places previously showing "Epost" now consistently use "Email". Text boxes resized to accommodate translated strings. |
| **Language icon** | Language icon is now square for consistent display in the settings. |

---
### Bugs 

| # | Area | Description |
|---|---|---|
| 1 | Alarm Schedule | Editing a schedule silently set `emailActive` to 0. Fixed. |
| 2 | Alarm Sender | Day-of-week index off-by-one caused all scheduled alarm windows to fall on the wrong day. Fixed. |
| 3 | Map | Folder navigation from map pins was limited to one directory level. Fixed to support unlimited depth. |
| 4 | Date Config | Translation string handling caused date configuration to fail when the locale format produced a non-numeric string. Date comparison now uses numeric values directly. |
| 5 | Dashboard | Expanded list column widths were stretched by long content. Fixed. |
| 6 | Reports | Logger list column ordering was incorrect. Fixed. |
| 7 | Calendar | Month and day names were rendered using the system locale instead of the active WideQuick language. Fixed. |
| 8 | Documents | Tag structure `C_c.D_d.S_o_s` was incorrectly split, causing object tree build failures. Fixed with proper parsing. |
| 9 | Calendar | Maintenance reminders were appearing on two calendar days instead of one. Fixed by snapping the reminder block to the start of the day. |

---

### Translations

| Area | Change |
|---|---|
| **New project translation strings** | Alarm acknowledgement, history import labels, settings and privilege labels, dashboard widget labels, report scheduler time controls, calendar month and day names, document group labels, map indicator tooltips, mail status strings ("Sending…", "Sent!", "Send failed"), and report status strings ("Creating report…", "Report done!"). |
| **Removed** | Orphaned Swedish source strings. |
| **Verified** | All Swedish source strings now have a corresponding translation entry. |
| **Languages updated** | Arabic, Bulgarian, Croatian, Czech, Danish, English, Finnish, French, German, Hungarian, Italian, Mandarin, Norwegian, Polish, Portuguese (PT + BR), Romanian, Slovenian, Spanish, Swedish. |

---

### Library and view changes

| File | Change |
|---|---|
| `Translations.klib` | Major string additions and cleanup across all languages |
| `Dashboard Widgets.klib` | Widget and language updates |
| `Map Indicators.klib` | Map pin, indicator, and tooltip updates |
| `Report.klib` | Report template and layout changes |
| `COMPONENTS.klib` | Component updates |
| `COMPONENTS_Legacy.klib` | Legacy component updates |
| `Dampers_Legacy.klib` | Legacy component updates |
| `COMMON_STATIC.klib` | Static component updates |
| `Calendar.klib` | Calendar display updates |
| `CustomPopupObjects.klib` | Popup object updates |
| `WorkviewNameDisplay.klib` | Workview name display updates |
| `Buttons.klib` | New button definitions |
| `Styrkurva.klib` | Control Curve component updates |
| `AlarmSchedule_1.kvie` | Full UI rework for slot 2 time windows and theme |
| `ReportSchedule1.kvie` | New send-time controls |
| `VySpecifikHistorik.kvie` | Cross-system group loading |
| `Historik.kvie` | Cross-system groups, TreeView for signal list, max count lowered |
| `Dashboard *.kvie` | Bar chart, legend, and load improvements |
| `Karta.kvie` | Map nav-bar z-order fix for web |
| `StyrkurvaTid.kvie` | Visual overhaul, two-column data point layout, live time and Y0 indicator lines |
| `WORKSPACE.kvie` | Workspace layout updates |
| `LB01/LB02/LB03.kvie` | HVAC standard and legacy view updates |
| `VS11 / VV10–VS20.kvie` | Heating system view updates |
| `Larm - Logg.kvie` | Alarm log view updates |
| `Inställningar.kvie` | Settings view with privilege support |


</details>


## WideQuick BMS 2026.1.0 { #bms-2026-1-0 }
__Released 2026-05-21__
Modular Framework Version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0)
<details class="release" markdown="1">
<summary>Release notes</summary>

This is the first release of WideQuick BMS in the Modular Framework family — the building-management concept rebuilt on the Modular Framework foundation. It brings the full  Framework feature set (multi-language support, an in-system logbook, a maintenance calendar, document handling, and broad web and remote client support) together with the building-management tooling that defines the BMS concept, such as time channels, reasonable suffixes, control curves and ready-made building dashboards.

### New features

| Feature | Description |
| --- | --- |
| **Multi-language support** | Views, scripts, the object library, dynamics and Data Store are now fully translatable, with a built-in language selector and flag icons for switching language at runtime. |
| **Tooltip system** | A new tooltip mechanism (`scToolTip`) adds contextual help boxes throughout the system, including history and map objects. |
| **Rewritten Workview animation** | The animation system has been rebuilt from the ground up to be more versatile and easier to configure, with a matching settings view and helpers for reading user-defined theme colours. |
| **ObjectFinder & goTo** | Every object is automatically indexed with its view path and name, and the new `goTo` function lets you jump straight to any object from anywhere in the project. |
| **Configurable runtime behaviour** | Value-display refresh rate is now adjustable at runtime, and the chosen theme (light/dark) is remembered and restored on the next startup. |
| **Automatic data retention** | Loggers and history now prune data older than a set age (e.g. two years) automatically, keeping databases from growing unbounded over time. |
| **Web & remote client support** | Major expansion of client support: report creation, alarm-schedule editing and the log viewer all work on WideQuick Web and remote clients, and suffixes, view privileges and maintenance state are synchronised between all clients. |
| **Legacy view import** | Views built in WideQuick BMS 8.0 or earlier can be lifted directly into the framework, where their symbols instantly repaint to the new, redesigned objects while keeping the same connections. |

### New & updated modules

| Module | Description |
| --- | --- |
| **Object library** | A redesigned set of process symbols (valves, sensors, dampers and more) with a cleaner, modernised look, plus the legacy BMS symbols (including air-handling/"luftbehandling") integrated to work in the framework while keeping their familiar appearance. Objects were standardised across font size, decimals, captions and descriptions, and digital value displays were added. These are the symbols that legacy BMS 8.0 views repaint to on import. |
| **Time channels** | Time-channel functionality ported from the legacy BMS and integrated into the common popup system. Time-channel configurations can be saved and applied, with a user-assigned name and description, and a privilege check on the time-channel popout. |
| **Control curves** | Control curve objects with configurable X/Y setpoints, value clamping and axis locking, plus a time-based control curve. Curve signals have their own privileges and the views scale correctly across resolutions. |
| **Manual operation** | A manual-operation popup for commanding objects, including changing the hand icon and the shutdown option, with captioned special buttons. |
| **Dashboard** | A new configurable dashboard built from a library of reusable widget objects (`Dashboard Widgets.klib`), with ready-made BMS dashboards and a dynamic alarm graph. Widgets work on desktop, web and remote, the start dashboard shown after login is configurable, and example dashboards are included to build from. |
| **Logbook** | A new module for creating, browsing and filtering timestamped log entries across the project. Filter by topic, date range and user; open it pre-filtered to a specific topic; and embed the `LogBookEntryButton` template in any view. |
| **Calendar** | A new calendar module with month navigation, mini calendar and an upcoming-events sidebar. Maintenance tasks appear as calendar events with status-based colours and automatic reminders ahead of scheduled work. |
| **Documents** | A new document-management module with a file picker for uploading documents and a handler (`scDoc`) for linking documents to objects, validated across desktop, remote and web. |
| **Map handler** | A new map module with an example view and web-compatible map support, plus a new set of map navigation indicator objects for placing and linking objects on a map. |
| **History** | History can now be shown for the entire project, not just a single object, with automatic decimal scaling and a wider colour spread for readable multi-curve trends. |
| **Maintenance** | Significantly expanded: recurring maintenance tasks with a treeview object selector, real-time sync across all connected clients, refresh buttons, a per-user maintenance counter on the dashboard, and status/priority colours throughout. A new **system-identity** mechanism registers each system, tags tasks by system, and adds a System column and filter so a single maintenance database can serve several installations. |
| **Reports** | The report scheduler now supports two time spans per day and scheduling by alias, shows clear status messages, and can be created and run from remote clients. Reports from an existing WideQuick installation can also be migrated into a Modular Framework project. |
| **Alarms** | A new alarm frequency view shows how often alarms occur, remote alarms can be scheduled in alarm schedules with their severity and group, alarm schedules gained select-all / deselect-all buttons for alarm groups, the "Visa information" button supports show scripts, and alarm log events are no longer recorded twice. Alarm list status colours follow the standard BMS alarm colour configuration. |

### Changes

| Area | Change |
| --- | --- |
| **Navigation** | "Loggar" moved into "Rapporter & loggar", "Underhåll & loggar" renamed to "Underhåll", individual menu items can be hidden at runtime, and a re-show button was added for hidden sub-navigation. |
| **Login & users** | Login is now possible via a combo box instead of typing a username, and the login requirement can be disabled from the settings view. |
| **Users & permissions** | New demo users were added, each with a sensible role-based privilege level, and the privilege system was reworked: privileges were renamed from the old scheme to a new one, dedicated privileges were added for maintenance and logbook actions, and users now get a clear notification when they lack the privilege for an action. The `Servicetekniker` role was renamed to `service`. |
| **Process value object** | Value updates are now driven by a Data Store listener instead of dynamics, giving lighter rendering for stale or slow-changing variables since the object only redraws when the value actually changes. |
| **Alarm terminology** | Alarm wording was standardised: "Allvarlighetsgrad" is now "Larmklass" and "Bekräfta/Bekräftbara" is now "Kvittera/Kvitterbara" throughout the views and translations. |
| **Signal simulation** | Demo Modbus signals were converted to OPC UA, with a simulator (`scSimMB`) generating realistic values for the new OPC UA signals. |
| **Settings** | Settings unavailable on remote/web clients are now clearly disabled. |
| **Map indicators** | A new set of map navigation indicator objects has been introduced and is now used by default. The previous map indicators are no longer used in the framework views but remain fully functional and behave exactly as before, so existing projects that use them are unaffected. |
| **Licensing** | The project now ships under the BSD 3-Clause license, together with third-party license texts and attributions. |

### Migrating from a legacy WideQuick BMS

As the first BMS release in the Modular Framework family, there is no earlier version in this family to upgrade from. When bringing an existing, legacy WideQuick BMS project across, note the following:

| Topic | Note |
| --- | --- |
| **Legacy view import** | Views built in WideQuick BMS 8.0 or earlier can be lifted directly into this project, where their symbols repaint to the new, redesigned objects while keeping the same connections. |
| **Objects use SuffixAlias** | Framework objects reference their values through a `SuffixAlias` rather than the suffix directly. A suffix alias must be defined for each object; objects with an unconfigured alias are flagged visually in the views. |
| **Maintenance system identity** | On first start, maintenance tasks are attributed to the current system by hostname, and a migration dialog is shown if an application name change is detected. Review the assignment afterwards to confirm tasks belong to the correct system. |

</details>
