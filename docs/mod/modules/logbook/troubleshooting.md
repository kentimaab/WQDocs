---
title: Logbook
description: Common issues and solutions for the Logbook module.
product: mod
page_type: troubleshooting
doc_id: DOC-M15
status: draft
last_reviewed: 2026-06-08
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

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
