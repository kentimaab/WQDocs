---
title: Backup and Restore
description: Save and restore DataStore variable values by name.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-05-27
---
<!-- --8<-- [start:body] -->
# Backup and Restore

The Backup and Restore feature lets you save the current values of selected DataStore variables as a named backup and restore them at a later time. This can be used to preserve known-good states, commissioning baselines, or setpoint configurations.

The feature is available under **Settings → Backup** with two views: **Create** for creating backups and **Restore** for restoring and managing them.

!!! note "Requirements"
    The `scBackUpAndRestore` script must be running for Backup and Restore to work.

## What Can Be Backed Up { #what-can-be-backed-up }

The variable tree shows DataStore variables available for backup — internal variables and logged signals from process views. System variables prefixed with `_sys_` are excluded. Any variable with a value of type string, number, or boolean can be backed up.

A backup captures the values of the selected variables at the moment **Create backup** is clicked. It is a point-in-time snapshot — values that change after the backup is created are not tracked.

## Creating a Backup { #creating-a-backup }

Navigate to **Settings → Backup → Create**.

![Variable backup view](/Images/Backup_And_Restore/backup-create.png){align=center}

The view has two panels. The left panel lists all available DataStore variables with their current values. The right panel shows the variables that will be included in the backup.

1. Browse or filter the left panel to find the variables to include. Type in the filter field at the top to narrow the tree — click **X** to clear it.
2. Double-click a variable, or select it and click **>**, to move it to the right panel.
3. Enter a name in the **Backup name** field. The name must be unique.
4. Optionally enter a description in the **Backup description** field.
5. Click **Create backup**.

!!! note
    If a backup with the same name already exists, you will be warned before it is overwritten.

!!! tip
    The view remembers which variables were included in the previous backup, making it easy to create multiple backups with the same variable selection.

To clear the right panel without creating a backup, click **Clear added variables**.

## Restoring a Backup { #restoring-a-backup }

Navigate to **Settings → Backup → Restore**.

![Restore variables from backup view](/Images/Backup_And_Restore/backup-restore.png){align=center}

The view has three panels. The left panel lists all saved backups with their creation date. Selecting a backup shows its metadata below the panels and populates the middle panel with the variables stored in that backup.

![Backup metadata shown below the panels](/Images/Backup_And_Restore/backup-metadata.png){align=center}

* **Created on** — the date and time the backup was created.
* **Created By** — the user who created the backup.
* **Description** — the description entered at the time of creation.

To restore:

1. Select a backup from the left panel.
2. Browse or filter the middle panel to find the variables to restore.
3. Double-click a variable, or select it and click **>**, to move it to the right panel. To add all variables at once, click **Add all variables**.
4. Click **Restore from backup**. The stored values are applied immediately.

## Deleting a Backup { #deleting-a-backup }

1. Navigate to **Settings → Backup → Restore**.
2. Select the backup to delete from the left panel.
3. Click **Delete backup** and confirm. The backup and all its stored values are permanently removed.

<!-- --8<-- [end:body] -->
