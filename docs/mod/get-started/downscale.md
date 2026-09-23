---
title: Downscale Version
description: The minimal WideQuick MOD template and how to add optional modules back in as resource packages.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-09-22
tags: 
 - MOD
---

# Downscale Version

Alongside the full [template project](download.md#template-project), WideQuick MOD is also available as a **downscale version**: a minimal project containing only the Core module. Every optional module is left out entirely, giving integrators a smaller starting point than the standard template.

## What the downscale version includes { #what-the-downscale-version-includes }

The downscale project ships with [Core](../modules/Core/index.md) only: navigation, alarms, themes, graphical symbols, project-wide settings, and user & privilege management. This is the same foundation every WideQuick MOD project builds on, without any of the optional modules layered on top.

## What is left out { #what-is-left-out }

None of the optional modules are included in the downscale version:

* [Audit Trail](../modules/audit-trail/index.md) — tracks changes to Data Store variables and maintenance tasks.
* [Backup and Restore](../modules/backup-and-restore/index.md) — saves and restores Data Store variable values by name.
* [Calendar](../modules/calendar/index.md) — month, week and day views of events and maintenance deadlines.
* [Dashboards](../modules/dashboards/index.md) — configurable views for monitoring signals, values and status.
* [Documents](../modules/documents/index.md) — manages files and links them to objects.
* [History](../modules/history/index.md) — graphical views of logged signal data.
* [Logbook](../modules/logbook/index.md) — records and organises free-text notes tied to parts of the system.
* [Maintenance](../modules/maintenance/index.md) — schedules, tracks and automates maintenance tasks.
* [Maps & Indicators](../modules/maps/index.md) — floorplan views and map indicators.
* [Reports](../modules/reports/index.md) — generates, schedules and customizes reports.

A project built from the downscale version therefore starts with nothing but Core, and grows by adding only the modules the project actually needs.

## Adding a module { #adding-a-module }

Each optional module is distributed as a resource package, a `.wqrc` file bundling everything the module needs: scripts, views, objects, and database schema. To add a module to a downscale project, download its resource package and import it through the built-in Resources interface. See [Resources and Resource package](../reference/Resources-and-Resource-package.md) for the full import procedure.

Because [every module is independent](../concepts/index.md#module-independence), packages can be imported in any combination and in any order. Adding Maintenance does not require also adding Calendar, even though the two integrate when both are present.

## Choosing a starting point { #choosing-a-starting-point }

* Start from the **downscale version** when the project's module needs are narrow, or not yet fully known, and modules should be added deliberately as requirements are confirmed.
* Start from the full **template project** (see [Download](download.md)) when most or all modules are expected to be used from the outset.

Whichever starting point is used, the modules themselves are identical: importing a module into a downscale project produces the same result as it already being present in the full template project. The only difference is what is in place when the project is opened for the first time: nothing but Core, or every module ready to use.
