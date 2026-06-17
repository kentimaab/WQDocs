---
title: Modular Framework Releases
description: Release notes for the WideQuick Modular Framework.
product: mod
page_type: release
status: draft
last_reviewed: 2026-06-02
tags: 
 - MOD
---

# Modular Framework Releases

Release notes for the WideQuick Modular Framework. The newest release is listed
first. Each concept built on the framework (BMS, WWT) pins a specific MOD release
and links back to its entry here.

## WideQuick MOD 2026.1.0 { #mod-2026-1-0 }

<details class="release" markdown="1" open>
<summary>Released 2026-05-20</summary>

The second major release of the WideQuick Modular Framework builds on the 2024.1.0 foundation with several new modules and a large number of usability improvements. The headline additions are full multi-language support, an in-system logbook, a maintenance calendar, document handling, and far broader support for web and remote clients — making the framework easier to deploy, configure and operate across teams and sites.

### New features

| Feature                        | Description                                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-language support         | Views, scripts, the object library, dynamics and Data Store are now fully translatable, with a built-in language selector and flag icons for switching language at runtime.                                                                                                                                                                |
| Tooltip system                 | A new tooltip mechanism (`scToolTip`) adds contextual help boxes throughout the system, including history and map objects.                                                                                                                                                                                                                |
| Rewritten Workview animation   | The animation system has been rebuilt from the ground up to be more versatile and easier to configure, with a matching settings view and helpers for reading user-defined theme colours.                                                                                                                                                  |
| ObjectFinder & goTo            | Every object is automatically indexed with its view path and name, and the new `goTo` function lets you jump straight to any object from anywhere in the project.                                                                                                                                                                         |
| Project-wide history           | History can now be shown for the entire project, not just a single object, with automatic decimal scaling and a wider colour spread for readable multi-curve trends.                                                                                                                                                                      |
| Configurable runtime behaviour | Value-display refresh rate is now adjustable at runtime, and the chosen theme (light/dark) is remembered and restored on the next startup.                                                                                                                                                                                                |
| Automatic data retention       | Loggers and history now prune data older than a set age (e.g. two years) automatically, keeping databases from growing unbounded over time.                                                                                                                                                                                               |
| Legacy view import             | Views built in WideQuick BMS 8.0 or earlier can be lifted directly into the Modular Framework, where their symbols instantly repaint to the new, redesigned objects while keeping the same connections. Useful even outside a BMS context, since some projects were built on BMS 8.0 without intending to use it for building management. |

### New & updated modules

| Module               | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object library       | A redesigned set of process symbols (valves, sensors, dampers and more) with a cleaner, modernised look. Objects were standardised across font size, decimals, captions and descriptions, and digital value displays were added. These are the symbols that legacy BMS 8.0 views repaint to on import.                                                                                                                             |
| Dashboard            | A new configurable dashboard built from a library of reusable widget objects (`Dashboard Widgets.klib`). Widgets work on desktop, web and remote, the start dashboard shown after login is configurable, and example dashboards are included to build from.                                                                                                                                                                        |
| Logbook              | A new module for creating, browsing and filtering timestamped log entries across the project. Filter by topic, date range and user; open it pre-filtered to a specific topic; and embed the `LogBookEntryButton` template in any view.                                                                                                                                                                                             |
| Calendar             | A new calendar module with month navigation, mini calendar and an upcoming-events sidebar. Maintenance tasks appear as calendar events with status-based colours and automatic reminders ahead of scheduled work.                                                                                                                                                                                                                  |
| Documents            | A new document-management module with a file picker for uploading documents and a handler (`scDoc`) for linking documents to objects, validated across desktop, remote and web.                                                                                                                                                                                                                                                    |
| Map handler          | A new map module with an example view and web-compatible map support, plus a new set of map navigation indicator objects for placing and linking objects on a map.                                                                                                                                                                                                                                                                 |
| Maintenance          | Significantly expanded: recurring maintenance tasks with a treeview object selector, real-time sync across all connected clients, refresh buttons, a per-user maintenance counter on the dashboard, and status/priority colours throughout. A new **system-identity** mechanism registers each system, tags tasks by system, and adds a System column and filter so a single maintenance database can serve several installations. |
| Reports              | The report scheduler now supports two time spans per day and scheduling by alias, shows clear status messages, and can be created and run from remote clients. Reports from an existing WideQuick installation can also be migrated into a Modular Framework project.                                                                                                                                                              |
| Alarms               | A new alarm frequency view shows how often alarms occur, remote alarms can be scheduled in alarm schedules with their severity and group, alarm schedules gained select-all / deselect-all buttons for alarm groups, the "Visa information" button supports show scripts, and alarm log events are no longer recorded twice.                                                                                                       |
| Web & remote clients | Major expansion of client support: report creation, alarm-schedule editing and the log viewer all work on WideQuick Web and remote clients, and suffixes, view privileges and maintenance state are synchronised between all clients.                                                                                                                                                                                              |

### Changes

| Area                 | Description                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Navigation           | "Loggar" moved into "Rapporter & loggar", "Underhåll & loggar" renamed to "Underhåll", individual menu items can be hidden at runtime, and a re-show button was added for hidden sub-navigation.                                                                                                                                                                                          |
| Login & users        | Login is now possible via a combo box instead of typing a username, and the login requirement can be disabled from the settings view.                                                                                                                                                                                                                                                     |
| Users & permissions  | New demo users were added, each with a sensible role-based privilege level, and the privilege system was reworked: privileges were renamed from the old scheme to a new one, dedicated privileges were added for maintenance and logbook actions, and users now get a clear notification when they lack the privilege for an action. The `Servicetekniker` role was renamed to `service`. |
| Process value object | Value updates are now driven by a Data Store listener instead of dynamics, giving lighter rendering for stale or slow-changing variables since the object only redraws when the value actually changes.                                                                                                                                                                                    |
| Alarm terminology    | Alarm wording was standardised: "Allvarlighetsgrad" is now "Larmklass" and "Bekräfta/Bekräftbara" is now "Kvittera/Kvitterbara" throughout the views and translations.                                                                                                                                                                                                                    |
| Settings             | Settings unavailable on remote/web clients are now clearly disabled.                                                                                                                                                                                                                                                                                                                      |
| Map indicators       | A new set of map navigation indicator objects has been introduced and is now used by default. The previous map indicators are no longer used in the framework views but remain fully functional and behave exactly as before, so existing projects that use them are unaffected.                                                                                                          |
| **Licensing**        | The project now ships under the BSD 3-Clause license, together with third-party license texts and attributions.                                                                                                                                                                                                                                                                           |

### Breaking changes & migration

| Change                      | Migration notes                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objects now use SuffixAlias | All framework objects have been converted to reference values through a `SuffixAlias` instead of the suffix directly, and the property was added to popup objects to make this explicit. Projects upgrading from 2024.1.0 must define a suffix alias for each object; objects with an unconfigured alias are flagged visually in the views. This is the main migration step for this release. |
| Privilege rename            | Privileges were renamed from the old scheme to a new one. Projects upgrading from 2024.1.0 should re-check their privilege assignments after upgrading, since custom assignments tied to the old privilege names need to be re-mapped to the new ones.                                                                                                                                        |
| Suffix storage              | `scSuffix.suffixObj` is now split into three columns. Existing projects are upgraded automatically the first time the project is opened; no manual action is required.                                                                                                                                                                                                                        |
| Maintenance system identity | On first start, existing maintenance tasks are migrated to the current system by hostname, and a migration dialog is shown if an application name change is detected. Review the assignment afterwards to confirm tasks are attributed to the correct system.                                                                                                                                 |

</details>

## WideQuick MOD 2024.1.0 { #mod-2024-1-0 }

<details class="release" markdown="1">
<summary>Released 2024-09-03</summary>

The first official release of the WideQuick Modular Framework — a ready-to-use HMI/SCADA template assembled from
independent, reusable modules. It provides a themed, privilege-controlled operator environment with a complete
process-graphics library, alarm handling, trends, reports, maintenance, backup and audit tooling, so a new project
starts from a working system rather than a blank canvas.

### New features

| Feature                             | Description                                                                                                                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Modular architecture                | The framework is built from self-contained modules (alarms, trends, reports, maintenance, backup, etc.) that can be reused and combined independently, so a project only includes what it needs.       |
| Theme system                        | Built-in light and dark themes with a shared colour palette named by the Google Material convention. Themes switch consistently across all views, objects and the navigation bar.                      |
| Login & privilege system            | Role-based login with view locking, so users only see and reach the views and actions their privilege level allows. Unauthorised actions are met with clear error messages instead of silent failures. |
| Navigation system                   | A main menu plus an auto-generated sub-navigation that builds itself from the project's views, keeping menus in sync as views are added.                                                               |
| Suffix system                       | A central suffix/alias mechanism that lets the same object graphics be reused across many process objects without rebuilding views.                                                                    |
| Dynamic Workview objects (DynTouch) | Interactive process objects that come alive with live values and click-to-open popups.                                                                                                                 |
| Backup & restore                    | Operators can select variables (with search), save their values, and restore them later, with the original variable names preserved.                                                                   |

### New & updated modules

| Module                        | Description                                                                                                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Process object library        | A full set of P&ID symbols: pumps, valves, actuators, pipes, vessels/tanks, heat exchangers, compressors, instruments and PID control objects, all consistently scaled and styled. |
| Alarm module                  | Live alarm lists with filtering, alarm counters in the navigation bar, alarm grouping and severity, auto-acknowledge support, and external notification via email and GSM modem.   |
| Trends & history              | Trend views with consistent legend naming and theme-aware colours for readable multi-curve graphs.                                                                                 |
| Reports module                | Manual and scheduled report generation sharing a common template, with a report queue and email delivery for automatic reports.                                                    |
| Maintenance module            | Maintenance scheduling and machine cards for planning and tracking service work.                                                                                                   |
| Audit trail                   | Tracks variable and struct changes (including initial values), with filtering, sorting and a dedicated database.                                                                   |
| Popup & object-info system    | Standardised object popups with value displays, decimals, privileges and per-object settings.                                                                                      |
| Remote & multi-system support | A remote-system handler with launcher and aggregated alarm counts across connected systems.                                                                                        |

</details>
