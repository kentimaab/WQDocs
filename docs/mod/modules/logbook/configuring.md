---
title: Logbook - Configuring
description: Configure topics, contexts and access patterns for the Logbook module.
product: mod
page_type: howto
doc_id: DOC-M15
status: draft
last_reviewed: 2026-05-26
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook - Configuring

## Topics { #topics }

A topic is a string that identifies where in the system an entry belongs. Topics are hierarchical: levels are separated by `/`. An entry with the topic `Building/Floor2/AHU01` is visible when selecting `Building`, `Building/Floor2`, or `Building/Floor2/AHU01` in the topic tree.

Topics do not need to be registered in advance. They are created automatically the first time an entry is saved under that topic string.

**Convention:** Follow the same structure as the tag system: `Connection/Device/System/Object`. This makes it easy to find entries that belong to a specific piece of equipment.

```text
MB/AS01/VS10/GT11
MB/AS01/VS10/PT01
MB/AS02
```

When the logbook is opened from an object popup, the topic is set automatically from the object's tag path. When opened from a view button, the topic can be set from the view name or passed explicitly. See [Extending](extending.md) for how to do this in a script.

![Topic tree showing a nested hierarchy](/docs/Images/Logbook/topic-tree.png){align=center}

## Contexts { #contexts }

Contexts are named groupings that can be used to categorise entries across topics. Examples: `Operations`, `Commissioning`, `Alarms`. The default context `General` is always available.

Contexts are managed from the **Change logbook context** popup, opened by clicking **...** next to the Context field when creating or editing an entry. From there, contexts can be added, renamed and deleted. Deleting a context does not delete the entries assigned to it. Those entries remain in the logbook with no context assigned.

When filtering the logbook, selecting a context shows only entries assigned to that context, regardless of topic.

![Context management view](/docs/Images/Logbook/context-management.png){align=center}

## Access Patterns { #access-patterns }

### Global { #global }

The full logbook under **Documents & Logbook → Logbook** shows all entries from all topics. The topic tree on the left can be used to narrow down to a specific area of the system. This is the primary view for operators who need to review or add notes across the whole project.

### Object Popup { #object-popup }

Every object in the project has a [**Logbook**](../../reference/Popup/Logbook.md) tab in its popup. Opening this tab shows only entries whose topic matches the object's tag path. New entries created from here are automatically assigned the correct topic.

![Logbook tab in the object popup](/docs/Images/Logbook/object-popup-logbook.png){align=center}

### View-Scoped { #view-scoped }

The **SpeedDial** menu on process views includes a button that opens a logbook scoped to the current view. Only entries matching that view's topic are shown, and new entries created from here are automatically assigned the correct topic. See [Extending](extending.md) for setup details.

## Next Steps { #next-steps }

* [Extending](extending.md) — adding a logbook to a custom view or button
<!-- --8<-- [end:body] -->
