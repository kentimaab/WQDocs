---
title: Logbook - Extending
description: Add logbook support to custom views and buttons.
product: mod
page_type: extending
doc_id: DOC-M15
status: draft
last_reviewed: 2026-08-25
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook - Extending

## Privileges { #privileges }

These privileges control access to logbook operations:

| Privilege | Description |
|---|---|
| `Logbook_Add` | Required to create new entries |
| `Logbook_Edit` | Required to edit existing entries |
| `Logbook_Archive` | Required to archive and restore entries |
| `Logbook_Delete` | Required for **delete all archived notes** in the settings view |
| `Logbook_Context` | Required to add, remove or edit contexts |
| `Logbook_View` | Required to view entries |

Users without `Logbook_Add` will see the **Add** button area disabled and grayed out, with a red box overlay displaying a message indicating the required privilege. The `Enabled` property on the button is bound to `scUsers.hasPriv("Logbook_Add")`. The same pattern applies to the other logbook privileges.

!!! warning "Every logbook privilege defaults to denied"
    All logbook privileges are defined with `Default="denied"` in `Privileges.kdat`. After an upgrade, `Logbook_Archive` must be granted to a role before anyone can archive an entry. See [Users and Privileges](../Core/users-privileges.md).

## Archiving { #archiving }

Archiving has replaced per-entry deletion. There is no function that deletes a single entry, and no view offers one. An entry is archived instead, which hides it from the list while keeping it in the database. It is stored in the `archived` column on the `logbook` table, which is added on start if the table predates it.

!!! note "Archiving is available in the global logbook only"
    Archiving and restoring are offered in the full logbook view under **Documents & Logbook → Logbook**. The object popup and view-scoped logbooks offer adding and editing only.

    This keeps the action where it can be undone. Showing archived entries and restoring them both rely on the **Show archived** filter, which exists only in the global view. Archiving from a scoped logbook would hide the entry with no way to bring it back from there.

| State | `archived` | Behaviour |
|---|---|---|
| Active | `0` | Listed normally. |
| Archived | `1` | Hidden unless the view opts in. |

Archived entries are excluded from the topic tree and from the user list in the filter, so a topic whose entries are all archived disappears from the tree until archived entries are shown.

| Function | Purpose |
|---|---|
| `markEntryAsArchived(entryObj)` | Sets the entry's `archived` flag to `1` and reloads the view. |
| `unarchiveEntry(entryObj)` | Clears the flag and reloads the view. |
| `deleteAllArchived()` | Permanently deletes every archived entry and returns how many were removed. |
| `getLogBookTopics(contextFilter, showArchived)` | Builds the topic tree. Topics of archived entries are included only when `showArchived` is `true`. |

A handler exposes `showArchived`, which defaults to `false`. Setting it to `true` before calling `load()` includes archived entries in the list.

!!! warning "Deleting archived entries cannot be undone"
    `deleteAllArchived()` removes every archived entry from the database outright. It backs the delete action in the settings view and is the only operation in the module that destroys archived content.

### Retired soft-delete { #retired-soft-delete }

An earlier `deleteMark` column implemented a separate soft-delete lifecycle. It has been retired in favour of `archived`. On start, any rows still marked `deleteMark=1` are deleted and the column is dropped. No manual migration is needed.

<!-- --8<-- [end:body] -->
