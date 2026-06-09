---
title: Releases — BMS
description: Release notes for WideQuick BMS.
product: bms
page_type: release
last_reviewed: 2026-06-03
---

# Releases — BMS

Release notes for WideQuick BMS. The newest release is listed first and expanded;
older releases are collapsed, click a release to expand it. Each release is built on
a specific WideQuick Modular Framework version, linked under its heading. For the full
framework changelog see the [MOD releases](../../mod/releases/index.md).


## WideQuick BMS 2026.1.0 { #bms-2026-1-0 }
__Released 2026-05-21__
Modular Framework Version: [WideQuick MOD 2026.1.0](../../mod/releases/index.md#mod-2026-1-0) 
<details class="release" markdown="1" open>
<summary>Release notes</summary>

This is the first release of WideQuick BMS in the Modular Framework family — the building-management concept rebuilt on the Modular Framework foundation. It brings the full  Framework feature set (multi-language support, an in-system logbook, a maintenance calendar, document handling, and broad web and remote client support) together with the building-management tooling that defines the BMS concept, such as time channels, reasonable suffixes, control curves and ready-made building dashboards.

### New features

| Feature | Description |
| --- | --- |
| **Multi-language support** | Views, scripts, the object library, dynamics and datastore are now fully translatable, with a built-in language selector and flag icons for switching language at runtime. |
| **Tooltip system** | A new tooltip mechanism (`scToolTip`) adds contextual help boxes throughout the system, including history and map objects. |
| **Rewritten workview animation** | The animation system has been rebuilt from the ground up to be more versatile and easier to configure, with a matching settings view and helpers for reading user-defined theme colours. |
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
| **Control curves** | Control curve (styrkurva) objects with configurable X/Y setpoints, value clamping and axis locking, plus a time-based control curve (styrkurvatid). Curve signals have their own privileges and the views scale correctly across resolutions. |
| **Manual operation (Manöver)** | A manual-operation popup for commanding objects, including changing the hand icon and the shutdown option, with captioned special buttons. |
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
| **Process value object** | Value updates are now driven by a datastore listener instead of dynamics, giving lighter rendering for stale or slow-changing variables since the object only redraws when the value actually changes. |
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
