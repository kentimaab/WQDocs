---
title: Database schemas
description: Overview of the SQLite databases used by WideQuick MOD and what each one stores.
product: mod
page_type: reference
doc_id: DOC-D1
size: S
priority: p1
status: draft
last_reviewed: 2026-06-11
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Database schemas

WideQuick MOD uses several SQLite databases stored in the `Data/` folder of the project. Each database is owned by a specific set of modules and should only be accessed through the scripts that manage it.

## Contents { #contents }

### [Config.db](config-db.md) { #config-db }

* [**Config.db**](config-db.md) — The central configuration database. Stores navigation structures, object registrations, scheduled jobs, report queues, logbook entries, document references, and saved user settings across most MOD modules.

---

### [maintenance.db](maintenance-db.md) { #maintenance-db }

* [**maintenance.db**](maintenance-db.md) — Stores maintenance task configurations, the task log, change history, calendar events, and the registry of known remote systems.

---

### [History.db](history-db.md) { #history-db }

* [**History.db**](history-db.md) — Stores logged signal data. Tables are generated dynamically by loggers — each logger produces a data table and a meta table identified by a hash of the logger name.

---

### [SuffixConfig.db](suffixconfig-db.md) { #suffixconfig-db }

* [**SuffixConfig.db**](suffixconfig-db.md) — Stores the suffix object configuration as JSON. Used by the suffix system to resolve tag structures at runtime.

<!-- --8<-- [end:body] -->
