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

---

### [Popups](Popup/index.md) { #popups }

* [**Tab**](Popup/Tab.md) — Entry point for all popups: object overview, alarm and maintenance summary.
* [**History**](Popup/History.md) — Trend graph of logged signals for the selected object.
* [**Trend**](Popup/Trend.md) — Live signal values in a real-time graph.
* [**Object Info**](Popup/ObjectInfo.md) — Raw list of all signals connected to the object, with current values, units, and types.
* [**Maintenance**](Popup/Maintenance.md) — Scheduled maintenance tasks for the object.
* [**Logbook**](Popup/Logbook.md) — Logbook entries for the object.
* [**Documents**](Popup/Documents.md) — Documents linked to the object.
* [**Process**](Popup/Process.md) — Process values and status signals (suffix-dependent).
* [**Manover**](Popup/Manover.md) — Operating mode switching and manual setpoint control (suffix-dependent).
* [**TimeChannel**](Popup/Timechannel.md) — Time-based schedule configuration (suffix-dependent).
* [**Control Curve**](Popup/Control curve.md) — Non-linear control curve editor (suffix-dependent).

<!-- --8<-- [end:body] -->
