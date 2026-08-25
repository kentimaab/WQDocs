---
title: Logbook
description: Common issues and solutions for the Logbook module.
product: mod
page_type: troubleshooting
doc_id: DOC-M15
status: draft
last_reviewed: 2026-08-25
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| Entries do not appear after saving | Check that `loggWildCardReload` is set to `true` in Data Store. When `true`, the handler reloads all entries under the topic using a wildcard match after each save, so newly created sub-topic entries appear immediately. When `false`, only exact-topic entries reload. |
| The topic tree is empty | The topic tree is populated from entries in the database. If no entries exist for the handler's topic, the tree will be empty. Create at least one entry to verify the connection is working, then check the `Config` database connection if nothing appears. |
| Entries from other topics appear in a view-scoped handler | Verify that `load()` is called with `false` if only exact-topic matches are wanted. Calling `load(true)` includes all sub-topics via a wildcard query. |
| An entry has disappeared from the list | It was most likely archived rather than deleted. Enable **Visa arkiverade** in the filter to show archived entries, then restore it. |
| A topic has vanished from the topic tree | The tree is built from non-archived entries. A topic whose entries are all archived is not listed until archived entries are included. |
| A user is missing from the filter's user list | The user list is built from non-archived entries only, so a user whose entries are all archived does not appear. |
| Archived entries came back after an upgrade | Entries previously soft-deleted through the retired `deleteMark` column are removed on start, not archived. Anything still present was archived rather than soft-deleted. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
