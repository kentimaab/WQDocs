---
title: Logbook
description: Record and organise free-text notes tied to specific parts of the system.
product: mod
page_type: concept
doc_id: DOC-M15
size: S
priority: p1
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook

The Logbook module provides a way to record free-text notes tied to specific parts of the system. An entry is filed against the thing it concerns: a workview, an object, or a topic path of the operator's own choosing.

Entries are reached through a single topic tree that can be keyed two ways. **Workview** mode arranges notes by the folder structure of the process views, and **signal** mode arranges them by tag path. A note is reachable in both, because a note on an object also belongs to every view that object is drawn in, and a note on a view also belongs to the objects drawn in it.

The logbook is available in three places: globally under **Documents & Logbook → Logbook**, in the [**Logbook**](../../reference/Popup/Logbook.md) tab of any object popup, and through the **SpeedDial** menu on process views.

## Contents { #contents }

### [Get started](get-started.md) { #get-started }
* [**The Logbook View**](get-started.md#the-logbook-view) — Layout, topic tree, entry list and archiving.
* [**Switching How the Tree Is Keyed**](get-started.md#switching-how-the-tree-is-keyed) — Workview mode and signal mode.
* [**Creating an Entry**](get-started.md#creating-an-entry) — Fields and how to save.
* [**Filtering**](get-started.md#filtering) — Searching and filtering entries, including archived ones.

---

### [Configuring](configuring.md) { #configuring }
* [**What an Entry Is Filed Against**](configuring.md#what-an-entry-is-filed-against) — Views, objects and free topics.
* [**How the Two Trees Are Built**](configuring.md#how-the-two-trees-are-built) — Workview mode, signal mode and how a note appears in both.
* [**Contexts**](configuring.md#contexts) — Managing named context groups.
* [**Access Patterns**](configuring.md#access-patterns) — Global, object popup and view-scoped usage.

---

### [Extending](extending.md) { #extending }
* [**Privileges**](extending.md#privileges) — Required privileges for adding, editing and archiving entries.
* [**Topic Storage**](extending.md#topic-storage) — The `topic`, `topic_kind` and `topic_ref` columns.
* [**Archiving**](extending.md#archiving) — The `archived` column, the archive functions and permanent deletion.
* [**Script Reference**](extending.md#script-reference) — The `scLogBook` functions behind the tree and the scoped views.

---

### [Troubleshooting](troubleshooting.md) { #troubleshooting }
* [**Common Issues**](troubleshooting.md) — Common issues and how to fix them.
<!-- --8<-- [end:body] -->
