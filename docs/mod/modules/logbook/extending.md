---
title: Logbook - Extending
description: Privileges, topic storage and archiving in the Logbook module.
product: mod
page_type: extending
doc_id: DOC-M15
status: draft
last_reviewed: 2026-09-15
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

## Topic Storage { #topic-storage }

An entry's placement is held in three columns on the `logbook` table. `topic_kind` and `topic_ref` are added on start if the table predates them, so an existing project upgrades itself.

| Column | Purpose |
|---|---|
| `topic` | The display path the entry was filed under. This is the source of truth. |
| `topic_kind` | What the entry is anchored to: `view`, `signal`, `signal-node` or `free`. |
| `topic_ref` | The raw identifier of that anchor: a view path including `.kvie`, or a tag. Empty for `free`. |

!!! warning "Only `topic` should be edited directly"
    `topic_kind` and `topic_ref` are derived values. `reconcileTopicRefs()` re-derives both from `topic` at every start, so a change written to either one alone is overwritten on the next restart. To move an entry, change its `topic`.

The derivation takes the longest part of the path that resolves to a known view or tag, and keeps whatever follows as the entry's own sub-path. `MB/AS02/Station2/GT44/Trend` therefore anchors to the sensor `MB.AS02.Station2_GT44` and keeps `Trend` as a node beneath it.

### Self-healing on start { #self-healing-on-start }

`reconcileTopicRefs()` runs once on start and re-derives the anchor of every distinct topic. This keeps placements correct after views are renamed or moved, and after the object index is rebuilt.

!!! note "The object index fills in as views are opened"
    Anchors are resolved against the index of which objects are drawn in which views, and that index grows as views are visited. A tag that has not been indexed yet resolves to the equipment above it instead, and settles on the exact tag after the view has been opened once and the application is restarted. The entry is reachable either way. Only the node it sits on differs.

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
| `getLogBookTopics(contextFilter, showArchived, mode)` | Builds the topic tree in the given mode. Topics of archived entries are included only when `showArchived` is `true`. |

A handler exposes `showArchived`, which defaults to `false`. Setting it to `true` before calling `load()` includes archived entries in the list.

!!! warning "Deleting archived entries cannot be undone"
    `deleteAllArchived()` removes every archived entry from the database outright. It backs the delete action in the settings view and is the only operation in the module that destroys archived content.

### Retired soft-delete { #retired-soft-delete }

An earlier `deleteMark` column implemented a separate soft-delete lifecycle. It has been retired in favour of `archived`. On start, any rows still marked `deleteMark=1` are deleted and the column is dropped. No manual migration is needed.

## Script Reference { #script-reference }

The `scLogBook` script resolves placements and builds the tree. A view holds a handler instance, created with `new logBookHandler(topic, view)`, which owns the entry list and the tree for that view.

### Tree keying { #tree-keying }

| Member | Purpose |
|---|---|
| `scLogBook.MODE_DIR` | Tree keyed by workview directory. |
| `scLogBook.MODE_SIGNAL` | Tree keyed by signal path. |
| `handler.treeMode` | The mode this handler builds in. Set before `setTreeView()`, or the first tree is built unkeyed. |
| `handler.setTreeMode(mode)` | Switches mode and rebuilds. Clears the cross-reference cache, because the object index grows as views are opened. |

The operator's choice is held in the `LogBookTreeDirMode` Data Store point, which every logbook view watches with a `DataStoreListener`. The point is not persisted, so the tree returns to workview mode when the application restarts.

### Resolution { #resolution }

| Function | Purpose |
|---|---|
| `resolveTopic(topic)` | Resolves a display path to `{kind, ref, tail}`, taking the longest matching prefix. |
| `displayPathsFor(kind, ref, tail, topic, mode, preferView)` | The paths an entry appears under in the given mode. Returns more than one when an object is drawn in several views. |
| `viewsForRef(ref)` | The views a tag appears in, climbing the tag path until something matches. |
| `topicsUnderPath(displayPath, mode, withDescendants)` | The stored topics filed under a selected tree node. |
| `placementLabel(kind, ref, topic)` | The text shown in the **Placed on** column. |
| `leafLabelFor(view, signal)` | The leaf label for an object in a view, extended with as much of the tag as is needed when two objects share a name. |

### Opening a logbook scoped to something { #opening-a-logbook-scoped-to-something }

A view or a button opens a scoped logbook by naming the topic to select, then linking to the logbook pop-out. The topic is handed over in `app.logbookSelectedTopic` and consumed by the pop-out:

```javascript title="Opening the logbook on the current view"
app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
app.popOutVisible = true;
```

The pop-out resolves that path back to its anchor with `resolveTopic()`, records it with `setScope(kind, ref)`, and calls `applyScope()` to translate the anchor into a path for whichever mode is active. Holding the scope as an anchor rather than as a path is what lets the selection survive a mode switch.

!!! note "The hand-off is cleared when it is consumed"
    The main logbook view clears `app.logbookSelectedTopic` when it reads it. A value left behind would otherwise still be applied the next time the logbook is opened from the menu, filtering the list to a topic the operator did not ask for.

<!-- --8<-- [end:body] -->
