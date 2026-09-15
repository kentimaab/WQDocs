---
title: Logbook
description: Common issues and solutions for the Logbook module.
product: mod
page_type: troubleshooting
doc_id: DOC-M15
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| The same note appears under several nodes | This is intended. A note on an object belongs to every view that object is drawn in, and a note on a view belongs to the objects drawn in it. The **Placed on** column names the entry's real anchor. See [How the Two Trees Are Built](configuring.md#how-the-two-trees-are-built). |
| A note appears in views it has nothing to do with | It is filed higher up the tag path than intended, on a device or a cabinet rather than on a single object or a view. Everything below that point belongs to it, which can reach most of the plant. Change the entry's `topic` to the view or the object it actually concerns. |
| A node is in the tree in one mode but not the other | The two modes key the same entries differently, so a node in one has no counterpart in the other. Nothing is filtered out. Switch the toggle and look under the corresponding view or tag. |
| An entry cannot be found after switching tree mode | The entry moved node rather than disappearing. Read its anchor in the **Placed on** column, then look for that view or tag in the current mode. |
| A note on a view does not appear under any tag in signal mode | Signal mode places a view's notes under the tags drawn in that view. If no object in the view has been indexed yet, there is nowhere to place it. Open the view once so its objects are indexed, then restart. |
| Two objects in the same view share a leaf name | The leaf label is extended with as much of the tag as is needed to tell them apart, giving names such as `VS10_GT11` and `VS11_GT11`. An object whose name is already unique in its view keeps its plain name. |
| An entry sits on a piece of equipment instead of the exact object | The object had not been indexed when the anchor was last derived, so the resolution fell back to the equipment above it. Open the view the object is drawn in, then restart. The anchor is re-derived on every start. |
| `topic_kind` or `topic_ref` reverts after a restart | Both are derived from `topic` on start. Editing either one alone is undone. Change the entry's `topic` instead. See [Topic Storage](extending.md#topic-storage). |
| The topic tree is empty | The tree is built from entries in the database. If none exist, the tree is empty. Create one entry to verify the connection, then check the `Config` database connection if nothing appears. |
| Opening the logbook from the menu shows only one topic's entries | A scoped logbook left its hand-off behind. Reopen the logbook from **Documents & Logbook → Logbook**, which clears the value as it reads it. |
| An entry has disappeared from the list | It was most likely archived rather than deleted. Enable **Show archived** in the filter to show archived entries, then restore it. |
| A topic has vanished from the topic tree | The tree is built from non-archived entries. A topic whose entries are all archived is not listed until archived entries are included. |
| A user is missing from the filter's user list | The user list is built from non-archived entries only, so a user whose entries are all archived does not appear. |
| Archived entries came back after an upgrade | Entries previously soft-deleted through the retired `deleteMark` column are removed on start, not archived. Anything still present was archived rather than soft-deleted. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
