---
title: Releases - BMS
description: Release notes for WideQuick BMS.
product: bms
page_type: release
status: draft
last_reviewed: 2026-06-03
tags: 
 - BMS
---

# Releases - BMS

Release notes for WideQuick BMS. The newest release is listed first and expanded;
older releases are collapsed, click a release to expand it. Each release is built on
a specific WideQuick Modular Framework version, linked under its heading. For the full
framework changelog see the [MOD releases](../../mod/releases/index.md).


## WideQuick BMS 2026.1.1 { #bms-2026-1-1 }
__Released 2026-06-30__
Modular Framework Version: <!-- MOD VERSION LINK -->
<details class="release" markdown="1" open>
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
