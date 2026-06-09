---
title: Logbook — Extending
description: Add logbook support to custom views and buttons.
product: mod
page_type: extending
doc_id: DOC-M15
status: draft
last_reviewed: 2026-05-26
---
<!-- --8<-- [start:body] -->

# Logbook — Extending

## Privileges { #privileges }

Three privileges control access to logbook operations:

| Privilege | Description |
|---|---|
| `Logbook_Add` | Required to create new entries |
| `Logbook_Edit` | Required to edit existing entries |
| `Logbook_Delete` | Required to delete entries |

Users without `Logbook_Add` will not see the **Add** button. The buttons are hidden automatically based on the current user's privileges. No extra script logic is needed.

## Troubleshooting { #troubleshooting }

### Entries do not appear after saving { #entries-do-not-appear-after-saving }

Check that `loggWildCardReload` is set to `true` in DataStore. When `true`, the handler reloads all entries under the topic using a wildcard match after each save, so newly created sub-topic entries appear immediately. When `false`, only exact-topic entries reload.

### The topic tree is empty { #the-topic-tree-is-empty }

The topic tree is populated from entries in the database. If no entries exist for the handler's topic, the tree will be empty. Create at least one entry to verify the connection is working, then check the `Config` database connection if nothing appears.

### Entries from other topics appear in a view-scoped handler { #entries-from-other-topics-appear-in-a-view-scoped-handler }

Verify that `load()` is called with `false` if only exact-topic matches are wanted. Calling `load(true)` includes all sub-topics via a wildcard query.
<!-- --8<-- [end:body] -->
