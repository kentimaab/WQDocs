---
title: Reference
description: Technical reference for WideQuick MOD — tag structure, scripts, databases, and system concepts.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-11
---
<!-- --8<-- [start:body] -->

# Reference

Technical reference material for WideQuick MOD. These pages describe how the system is built — tag conventions, script dependencies, database schemas, and core runtime concepts.

## Contents { #contents }

### [Tag Structure](tag-structure.md) { #tag-structure }

* [**Tag Structure**](tag-structure.md) — Tag naming conventions and configuration for WideQuick MOD.

---

### [Suffix System](suffix-system.md) { #suffix-system }

* [**Suffix System**](suffix-system.md) — How suffix objects are structured, their attributes, and how they associate with popups.

---

### [Script Hierarchy](ScriptHierarchy.md) { #script-hierarchy }

* [**Script Hierarchy**](ScriptHierarchy.md) — Dependency map for all scripts in WideQuick MOD.

---

### [Multiview](multiview.md) { #multiview }

* [**Multiview**](multiview.md) — How to configure workview linking so the system can navigate between views based on object actions.

---

### [Resources and Resurspaket](resources-and-resurspaket.md) { #resources-and-resurspaket }

* [**Resources and Resurspaket**](resources-and-resurspaket.md) — Exporting and importing resources between projects.

---

### [Database Schemas](database-schemas/index.md) { #database-schemas }

* [**Config.db**](database-schemas/config-db.md) — Navigation, reports, logbook, objects, documents, and module configuration.
* [**maintenance.db**](database-schemas/maintenance-db.md) — Maintenance tasks, calendar events, and remote system registry.
* [**History.db**](database-schemas/history-db.md) — Dynamically generated logger tables for signal history.
* [**SuffixConfig.db**](database-schemas/suffixconfig-db.md) — Suffix object configuration.

<!-- --8<-- [end:body] -->
