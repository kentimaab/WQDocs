---
title: Popups
description: Overview of all popups available in WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-05-29
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Popups

WideQuick includes a set of built-in popups that provide detailed information and
control for individual objects in the process view. Popups are accessed by clicking
a `DynTouch` object, which opens the **Tab** popup as the entry point. From there
the user can navigate to the other available popups using the tab menu at the top.

Which popups are available for a given object depends on which signals the object
has. Some popups are always visible regardless of the object's signals, while others
only appear when the object has signals matching the configured suffix aliases. For
more information on how suffix aliases work, see
[Tag Structure — Suffix Alias](../tag-structure.md#suffix-alias).

To create a custom popup, see [Create Popup](../../guides/create-a-popup.md).

---

### Always visible

* [**Tab**](Tab.md) — the entry point for all popups. Displays a navigation menu,
an object overview, and a summary of active alarms and maintenance tasks.
* [**History**](History.md) — displays a trend graph of logged signals for the
selected object.
* [**Trend**](Trend.md) — displays live signal values for the selected object in a
real-time graph.
* [**Object Info**](ObjectInfo.md) — displays a raw list of all signals connected
to the object, including their current values, units, and types.
* [**Maintenance**](Maintenance.md) — displays scheduled maintenance tasks for the
object and allows new tasks to be created.
* [**Logbook**](Logbook.md) — displays logbook entries for the object and allows
notes to be created, edited, and deleted.
* [**Documents**](Documents.md) — displays documents linked to the object and
allows new documents to be linked.

---

### Suffix-dependent

These popups only appear when the object has signals matching the configured suffix
aliases:

* [**Process**](Process.md) — displays process values and status signals for the
object.
* [**Maneuver**](Maneuver.md) — provides control actions such as switching between
operating modes or setting manual values.
* [**Time Channel**](Time-channelmd) — allows time-based schedules to be configured
for the object.
* [**Control Curve**](Control curve.md) — a control curve editor for configuring
non-linear control relationships.
<!-- --8<-- [end:body] -->
