---
title: BackUpAndRestore.db
description: Table reference for BackUpAndRestore.db — stores tracked variables and saved snapshots for the Backup and Restore feature.
product: mod
page_type: reference
doc_id: DOC-D6
size: M
priority: p1
status: draft
last_reviewed: 2026-07-01
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# BackUpAndRestore database

The BackUpAndRestore database stores the state of the Backup and Restore feature, which lets a user save the current value of selected Data Store variables and restore them later.

## Tables { #tables }

| Table | Description |
|---|---|
| `currentVariablesForBackUp` | The variables currently staged for the next backup — added and removed via the Backup and Restore view before a backup is taken. |
| `existingBackUps` | One row per saved backup — the backup's table name, description, original name, the user who created it, and the creation date. |

## Backup tables { #backup-tables }

Each time a backup is created, a new table is generated, named after the backup (lowercased), with two columns:

| Column | Description |
|---|---|
| `variable` | The Data Store path of the variable. |
| `value` | The variable's value at the time the backup was taken, stored as text. |

These tables are created and dropped by `scBackUpAndRestore` and are listed in `existingBackUps` by their `tableName`.

<!-- --8<-- [end:body] -->