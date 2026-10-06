---
title: Migration Guide - BMS
description: Step-by-step migration guides for upgrading between WideQuick BMS versions.
product: bms
page_type: release
status: draft
last_reviewed: 2026-10-06
tags:
 - BMS
---

# Migration Guide - BMS

Step-by-step guides for upgrading between WideQuick BMS versions. The newest migration is listed first and expanded; older migrations are collapsed.

## WideQuick BMS 2026.1.1 → 2026.1.1.2 { #bms-migration-2026-1-1-2 }
__Released 2026-10-06__
<details class="release" markdown="1" open>
<summary>Migration steps</summary>

## Prerequisites

* WideQuick BMS 2026.1.1 (Template or Demo project)
* WideQuick V14 or later installed

## Migration steps

1. Download the resource package that matches your project:

    * **RemoteFixBMS.1.1_Template.wqrc** for the Template project
    * **RemoteFixBMS.1.1_Demo.wqrc** for the Demo project

2. Open your `WideQuick_BMS_Template_2026_1_1` or `WideQuick_BMS_Demo_2026_1_1`
project in **WideQuick® Designer** and import the resource package.

3. In **WideQuick® Designer**, click the **Resources** button to open the resource
panel.

    ![Resources_Button](/docs/Images/Resources/Resources%20.png)

    In the resource panel, navigate to **Files → Import from...** and select the
    resource package from the downloaded files.

    Once the resource is loaded, set all files to **Replace** so that the existing
    files in the project are overwritten with the updated versions. The gif below
    shows how to do this:

    ![Import resource](/docs/Images/Resources/RemoteFixImport.gif)

    When all files are set to **Replace** including the ones in the Data Store, click **Import** to start the process.

    !!! warning
        Once **Import** is clicked, do not interact with the application until it
        has finished. If it crashes, simply run the import again.

4. Start the project in **WideQuick® Runtime**.

5. If the project connects to remote systems, open **Remote Systems** in
**WideQuick® Designer** and enable **Auto connect** for each remote system whose
alarms should be included in the alarm counters. Without it, the connection to a
remote system is only open while a view uses it, such as the alarm list.

!!! note
    **Replace** overwrites the project's versions of the files in the package. If
    you have made your own changes to any of them, merge those changes back after
    the import. The changed files are listed in the
    [release notes](index.md#bms-2026-1-1).

!!! note
    Script functions are now called through their script library. Your own scripts
    and views that call the framework's functions by their old global names must use
    the library-qualified name instead, for example `scSmartPopup.smartPopup`,
    `scAlarmFinder.goToAlarm(...)` and `scWorkviewAnimation.AnimationHandler`.

</details>

## WideQuick BMS 2026.1.0 → 2026.1.1 { #bms-migration-2026-1-1 }
__Released 2026-06-26__
<details class="release" markdown="1">
<summary>Migration steps</summary>

## Prerequisites

* WideQuick BMS 2026.1.0 (Template or Demo project)
* WideQuick V14 or later installed

## Migration steps

1. Download the resource package **Migration BMS.2026.1.1**.

2. Open your `WideQuick_BMS_Template_2026_1_0` or `WideQuick_BMS_Demo_2026_1_0`
project in **WideQuick® Designer** and import the resource package.

3. In **WideQuick® Designer**, click the **Resources** button to open the resource
panel.

    ![Resources_Button](/docs/Images/Resources/Resources%20.png)

    In the resource panel, navigate to **Files → Import from...** and select
    **Migration BMS.2026.1.1** from the downloaded package.

    Once the resource is loaded, set all files to **Replace** so that the existing
    files in the project are overwritten with the updated versions. The gif below
    shows how to do this:

    ![Import resource](/docs/Images/Resources/MigrationImport.gif)

    When all files are set to **Replace** including the ones in the Data Store, click **Import** to start the process.

    !!! warning
        Once **Import** is clicked, do not interact with the application until it
        has finished. The process takes approximately 1 minute. If it crashes,
        simply run the import again.

4. Start the project in **WideQuick® Runtime**.

5. Close the application and start it again.

6. After the second restart all changes are applied. The `scCheck.js` script can
now safely be deleted from the project. This script is a one-time migration script
that runs on startup to add missing suffix aliases, update user privileges, and
correct database connection settings from the 2026.1.0 release. It is no longer
needed once the migration is complete.

!!! note
    The 2026.1.0 Template and Demo projects shipped with a bug where the **Larm**,
    **Maintenance**, and **History** database connections were missing their database
    name. `scCheck.js` corrects this automatically, but only if the connections are
    still in their original bugged state. Any database connections that have already
    been configured by the integrator will not be touched.

</details>
