---
title: Releases - WWT
description: Release notes for WideQuick WWT.
product: wwt
page_type: release
status: draft
last_reviewed: 2026-06-02
tags: 
 - WWT
---

# Releases - WWT

Release notes for WideQuick WWT. The newest release is listed first. Each release
is built on a specific WideQuick Modular Framework version, linked under its
heading. For the full framework changelog see the
[MOD releases](../../mod/releases/index.md).



## WideQuick WWT 2024.1.0 { #wwt-2024-1-0 }

Released 2024-09-03

**Modular Framework Version**: [WideQuick MOD 2024.1.0](../../mod/releases/index.md#mod-2024-1-0)

<details class="release" markdown="1" open>
<summary>Release notes</summary>

The first official release of WideQuick WWT — the water and wastewater concept built on the Modular Framework. Its feature set is identical to [WideQuick MOD 2024.1.0](../../mod/releases/index.md#mod-2024-1-0); WWT differs only in its dedicated theming and a set of WWT-specific views. It provides a themed, privilege-controlled operator environment with a complete PID/process-graphics library, alarm handling, trends, reports, maintenance, backup and audit tooling, so a new project starts from a working system rather than a blank canvas.

### New features

| Feature | Description |
| --- | --- |
| Modular architecture | The framework is built from self-contained modules (alarms, trends, reports, maintenance, backup, etc.) that can be reused and combined independently, so a project only includes what it needs. |
| Theme system | Built-in light and dark themes with a shared colour palette named by the Google Material convention. Themes switch consistently across all views, objects and the navigation bar. |
| Login & privilege system | Role-based login with view locking, so users only see and reach the views and actions their privilege level allows. Unauthorised actions are met with clear error messages instead of silent failures. |
| Navigation system | A main menu plus an auto-generated sub-navigation that builds itself from the project's views, keeping menus in sync as views are added. |
| Suffix system | A central suffix/alias mechanism that lets the same object graphics be reused across many process objects without rebuilding views. |
| Dynamic workview objects (DynTouch) | Interactive process objects that come alive with live values and click-to-open popups. |
| Backup & restore | Operators can select variables (with search), save their values, and restore them later, with the original variable names preserved. |

### New & updated modules

| Module | Description |
| --- | --- |
| Process object library | A full set of P&ID symbols: pumps, valves, actuators, pipes, vessels/tanks, heat exchangers, compressors, instruments and PID control objects, all consistently scaled and styled. |
| Alarm module | Live alarm lists with filtering, alarm counters in the navigation bar, alarm grouping and severity, auto-acknowledge support, and external notification via email and GSM modem. |
| Trends & history | Trend views with consistent legend naming and theme-aware colours for readable multi-curve graphs. |
| Reports module | Manual and scheduled report generation sharing a common template, with a report queue and email delivery for automatic reports. |
| Maintenance module | Maintenance scheduling and machine cards for planning and tracking service work. |
| Audit trail | Tracks variable and struct changes (including initial values), with filtering, sorting and a dedicated database. |
| Popup & object-info system | Standardised object popups with value displays, decimals, privileges and per-object settings. |
| Remote & multi-system support | A remote-system handler with launcher and aggregated alarm counts across connected systems. |

</details>
