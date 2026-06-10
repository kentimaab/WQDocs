---
title: Backup and Restore — Configuring
description: Restore and delete saved backups in the Backup and Restore feature.
product: mod
page_type: howto
doc_id: DOC-M20
status: draft
last_reviewed: 2026-06-08
---
<!-- --8<-- [start:body] -->

# Backup and Restore — Configuring

## Restoring a Backup { #restoring-a-backup }

Navigate to **Settings → Backup → Restore**.

![Restore variables from backup view](/Images/Backup_And_Restore/backup-restore.png){align=center}

The view has three panels. The left panel lists all saved backups with their creation date. Selecting a backup shows its metadata below the panels and populates the middle panel with the variables stored in that backup.

![Backup metadata shown below the panels](/Images/Backup_And_Restore/backup-metadata.png){align=center}

* **Created on** — the date and time the backup was created.
* **Created By** — the user who created the backup.
* **Description** — the description entered at the time of creation.

The middle panel supports the same filter as the create view. Type in the filter field to narrow the variable list.

1. Select a backup from the left panel.
2. Browse or filter the middle panel to find the variables to restore.
3. Double-click a variable, or select it and click **>**, to move it to the right panel. To add all variables at once, click **Add all variables**.
4. Click **Restore from backup**. The stored values are applied immediately.

## Deleting a Backup { #deleting-a-backup }

1. Navigate to **Settings → Backup → Restore**.
2. Select the backup to delete from the left panel.
3. Click **Delete backup** and confirm. The backup and all its stored values are permanently removed.
<!-- --8<-- [end:body] -->
