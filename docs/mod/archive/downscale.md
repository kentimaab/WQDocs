---
title: Downscale Version
description: The minimal WideQuick MOD template, and how to add the optional modules back in as resource packages.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-11-03
tags: 
 - MOD
---

# Downscale Version

Alongside the full [template project](../get-started/download.md#template-project), WideQuick MOD is also available as a **downscale version**: the template project with every optional module taken out. Each of those modules is available as a package of its own, so a project can start small and add only the modules it needs.

## What the downscale version includes { #what-the-downscale-version-includes }

The downscale project contains:

* [Core](../modules/Core/index.md): navigation, alarms, themes, graphical symbols, project-wide settings, and user & privilege management. This is the foundation every WideQuick MOD project builds on.
* [History](../modules/history/index.md): the history view, and the History and Trend tabs in the object popup.

The object popup keeps the tabs that belong to Core and History. The tabs of the modules below appear once their module is imported.

## What is left out { #what-is-left-out }

Eleven modules are left out, and each one is available as a separate package:

* [Audit Trail](../modules/audit-trail/index.md): logs changes to variables, what changed, who changed it and when.
* [Backup and Restore](../modules/backup-and-restore/index.md): saves the values of chosen variables under a name and restores them when needed.
* [Calendar](../modules/calendar/index.md): month, week and day views of events, with holiday import. Shows maintenance deadlines when Maintenance is installed too.
* [Control Curve](../reference/Popup/Control curve.md): the Control Curve and [Control Curve Time](../reference/Popup/Control curveTime.md) popups, for adjusting control curves and switching between their profiles.
* [Dashboards](../modules/dashboards/index.md): widgets and a view template for building dashboards with signals, key figures, history and alarms.
* [Documents](../modules/documents/index.md): stores files in the project and links them to objects.
* [Logbook](../modules/logbook/index.md): free-text notes tied to objects, views and other parts of the system.
* [Maintenance](../modules/maintenance/index.md): plans, tracks and automates maintenance of objects, with templates and recurring tasks.
* [Maps & Weather](../modules/maps/index.md): map indicators linked to alarms, and a weather widget with forecasts from SMHI.
* [Reports](../modules/reports/index.md): alarm, energy and delta reports in Excel, on demand or on a schedule, sent by email.
* [Time Channel](../reference/Popup/Time-channel.md): the popup for viewing and changing an object's time channel and saving it as a profile.

## Adding a module { #adding-a-module }

Each module is downloaded as a zip file from the same page as the template project, see [Download](../get-started/download.md). The zip file holds:

* `<Module>.wqrc`: the resource package, with the module's scripts, views, object libraries, variables, privileges and, for a module that has one, its database.
* `README.md`: what the module contains, how to import it, the privileges it brings and anything that needs extra care.

The Reports package also holds `Reports.kdat`, see [Reports](#reports).

To add a module:

1. Unzip the package.
2. In **WideQuick® Designer**, import the `.wqrc` file through the Resources interface and select **Replace all**. See [Resources and Resource package](../reference/Resources-and-Resource-package.md#importing-resources) for the import window.
3. Assign the module's privileges. The package adds them but grants them to no one, so give them to the users who need them. The packages contain no user accounts, so the project's existing users and their privileges are left as they are.

Modules can be imported in any combination and in any order, since [every module is independent](../concepts/index.md#module-independence). Calendar works without Maintenance, and starts showing maintenance deadlines once Maintenance is added.

The object popup needs no setup. The popups of Documents, Logbook, Maintenance, Control Curve and Time Channel appear in it, and in the **Suffixalias - Popuper** settings view, as soon as their module is in the project.

### Calendar and Maintenance { #calendar-and-maintenance }

Calendar and Maintenance store their data in the same database, `Data/maintenance.db`, through the `maintenance` database connection. Both packages include the file and the connection, so either module can be imported on its own.

!!! warning "Importing the second of the two"
    If one of the two modules is already in the project, set `maintenance.db` and the `maintenance` connection to **Skip** instead of **Replace** before pressing ++"Import"++. Replacing the file deletes every maintenance task, template, calendar event and subscription already in the project.

Each module creates the tables it needs when the Runtime starts.

### Reports { #reports }

The report definitions are in `Reports.kdat`, which a resource package can't carry. It comes in the zip file next to `Reports.wqrc`. After importing the package:

1. Close the project in **WideQuick® Designer**.
2. Copy `Reports.kdat` into the project folder, next to the project's other `.kdat` files, and replace the existing one.
3. Open the project again.

### Maps & Weather { #maps-and-weather }

No ready-made maps are included. Build a map view with the map indicators, as described in [Maps & Indicators](../modules/maps/index.md).

The SMHI weather connection is imported inactive. The weather widget turns it on when it fetches a forecast, so leave it as it is.

## Choosing a starting point { #choosing-a-starting-point }

* Start from the **downscale version** when the project's module needs are narrow, or not yet fully known, and modules should be added deliberately as requirements are confirmed.
* Start from the full **template project** (see [Download](../get-started/download.md)) when most or all modules are expected to be used from the outset.

Whichever starting point is used, the modules themselves are identical: a module imported into a downscale project is the same as the one already in the full template project. What differs is what is in place when the project is opened for the first time, and the privileges. In the full template the preconfigured users already hold the module privileges, while an imported module's privileges are granted to no one until you assign them.
