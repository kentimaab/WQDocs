---
title: Larmlista.db
description: Table reference for Larmlista.db — the alarm log written by Alarm-type loggers.
product: mod
page_type: reference
doc_id: DOC-D8
size: S
priority: p1
status: draft
last_reviewed: 2026-07-01
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Larmlista database

The Larmlista database does not have a fixed set of tables. It is written to by Alarm-type loggers configured in **WideQuick Designer®** — see [Configuring a Logger](../../guides/Loggers.md) for how logger type and version affect the tables that are created.

## Table naming { #table-naming }

Table names and layout depend on the Logger Version selected for the alarm logger:

| Version | Tables |
|---|---|
| Version 1 | Two tables named after the logger. |
| Version 2 | Multiple auto-generated tables, depending on the number of alarms logged. |

## Querying { #querying }

Alarm history is read through the `Loggers` global object rather than by querying the tables directly — for example `Loggers["Larmlogg"].data(...)`. This keeps queries independent of the underlying table names, which change if the logger is renamed or its version is changed.

<!-- --8<-- [end:body] -->