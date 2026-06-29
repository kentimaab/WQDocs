---
title: Migration Guide - BMS
description: Step-by-step migration guides for upgrading between WideQuick BMS versions.
product: bms
page_type: release
status: draft
last_reviewed: 2026-06-26
tags:
 - BMS
---

# Migration Guide - BMS

Step-by-step guides for upgrading between WideQuick BMS versions. The newest migration is listed first and expanded; older migrations are collapsed.

## WideQuick BMS 2026.1.0 → 2026.1.1 { #bms-migration-2026-1-1 }
__Released 2026-06-26__
<details class="release" markdown="1" open>
<summary>Migration steps</summary>

## Prerequisites

* WideQuick BMS 2026.1.0 (Template or Demo project)
* WideQuick V14 or later installed

## Migration steps

1. Download the resource package **Migration BMS.2026.1.1**.

2. Open your `WideQuick_BMS_Template_2026_1_0` or `WideQuick_BMS_Demo_2026_1_0`
project in **WideQuick Designer®** and import the resource package.

3. In **WideQuick Designer®**, click the **Resources** button to open the resource
panel.

    ![Resources_Button](/docs/Images/Resources/Resources%20.png)

    In the resource panel, navigate to **Files → Import from...** and select
    **Migration BMS.2026.1.1** from the downloaded package.

    Once the resource is loaded, set all files to **Replace** so that the existing
    files in the project are overwritten with the updated versions. The gif below
    shows how to do this:

    ![Import resource](/docs/Images/Resources/MigrationImport.gif)

    When all files are set to **Replace**, click **Import** to start the process.

    !!! warning
        Once **Import** is clicked, do not interact with the application until it
        has finished. The process takes approximately 1 minute. If it crashes,
        simply run the import again.

4. Start the project in **WideQuick Runtime®**.

5. Close the application and start it again.

6. After the second restart all changes are applied. The `scCheck.js` script can
now safely be deleted from the project.

</details>
