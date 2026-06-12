---
title: History.db
description: Table reference for History.db — dynamically generated tables created by WideQuick loggers.
product: mod
page_type: reference
doc_id: DOC-D5
size: M
priority: p1
status: draft
last_reviewed: 2026-06-11
---
<!-- --8<-- [start:body] -->

# History.db

History.db does not have a fixed set of tables. Tables are created automatically when loggers are configured in **WideQuick Designer®**. Each logger produces a pair of tables identified by a hash derived from the logger name.

## Table naming { #table-naming }

Each logger creates two tables:

| Table | Description |
|---|---|
| `wq_<hash>_data0` | The logged signal values — one row per sample, with a timestamp and the recorded value for each signal in the logger. |
| `wq_<hash>_meta` | Metadata for the logger — maps column names in the data table to their signal names and units. |

The hash is generated from the logger name and stays stable as long as the logger name does not change. Renaming a logger produces a new hash and a new pair of tables — the old tables are not removed automatically.

## Querying { #querying }

The `scHistory` script resolves the correct table names at runtime by reading the meta table. Direct queries against History.db should use the meta table to look up column names rather than hardcoding them, as column layout varies between loggers.

<!-- --8<-- [end:body] -->
