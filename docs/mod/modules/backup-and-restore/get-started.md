---
title: Backup and Restore - Get Started
description: Get up and running with the Backup and Restore feature.
product: mod
page_type: getstarted
doc_id: DOC-M20
status: draft
last_reviewed: 2026-06-08
scripts:
  - scBackUpAndRestore
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Backup and Restore - Get Started
???+ info "Requirements"
    The following scripts are required to use Backup and Restore and all
    related functionality covered in the Backup and Restore guides:
    
    * `scBackUpAndRestore`

The Backup and Restore feature saves the current values of selected DataStore variables as a named backup. It is available under **Settings → Backup**.

## What Can Be Backed Up { #what-can-be-backed-up }

The variable tree shows DataStore variables available for backup — internal variables and logged signals from process views. System variables prefixed with `_sys_` are excluded. Any variable with a value of type string, number, or boolean can be backed up.

A backup captures the values of the selected variables at the moment **Create backup** is clicked. It is a point-in-time snapshot. Values that change after the backup is created are not tracked.

## Creating a Backup { #creating-a-backup }

Navigate to **Settings → Backup → Create**.

![Variable backup view](/Images/Backup_And_Restore/backup-create.png){align=center}

The view has two panels. The left panel lists all available DataStore variables with their current values. The right panel shows the variables that will be included in the backup.

Type in the filter field at the top of the left panel to narrow the variable tree. Click **X** to clear the filter.

![Filtering the variable tree](/Images/Backup_And_Restore/backup-filter.png){align=center}

1. Browse or filter the left panel to find the variables to include.
2. Double-click a variable, or select it and click **>**, to move it to the right panel.
3. Enter a name in the **Backup name** field. The name must be unique.
4. Optionally enter a description in the **Backup description** field.
5. Click **Create backup**.
!!! tip
    The view remembers which variables were included in the previous backup, making it easy to create multiple backups with the same variable selection.

To clear the right panel without creating a backup, click **Clear added variables**.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — restoring and deleting backups
<!-- --8<-- [end:body] -->
