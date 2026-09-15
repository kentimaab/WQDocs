---
title: Logbook - Configuring
description: Configure what entries are filed against, how the topic trees are built, contexts and access patterns.
product: mod
page_type: howto
doc_id: DOC-M15
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook - Configuring

## What an Entry Is Filed Against { #what-an-entry-is-filed-against }

Every entry is anchored to one of three things. The anchor is what decides where the entry appears in the topic tree, and it is chosen by where the entry was created rather than by typing a path.

| Anchor | Created from | Example |
|---|---|---|
| A workview | The **SpeedDial** logbook button on a process view, or a view node in the tree | `System/Heating/VS11` |
| An object | The **Logbook** tab of an object popup, or an object node in the tree | `MB.AS01.VS11_SV21` |
| A topic of its own | Typing a path that matches neither | `Optimisation/2026-03/Night operation` |

The third kind covers notes that belong to no single piece of equipment. A commissioning thread, a seasonal optimisation discussion or a project log is filed under a path of the operator's own choosing and appears in the tree exactly as written, in both tree modes.

An entry anchored to a view or an object can still carry a path of its own below it. A note filed on `MB.AS02.LB02_GT44` with the sub-path `Trend` is anchored to the sensor and grouped under a **Trend** node beneath it, so several notes about the same object can be kept apart.

!!! info "Topics are not registered in advance"
    A topic exists because an entry uses it. There is no list of topics to maintain, and removing the last entry under a node removes the node.

## How the Two Trees Are Built { #how-the-two-trees-are-built }

The same entries are arranged two ways, and the toggle above the tree switches between them. Neither arrangement filters anything out.

### Workview mode { #workview-mode }

The tree follows the folder structure of the process views, so it reads like the navigation menu.

```text
System
  Heating
    VS11
      SV21
  Air handling
    LB01
```

A note filed on a view sits on that view's node. A note filed on an object sits under every view the object is drawn in, as a leaf named after the object.

### Signal mode { #signal-mode }

The tree follows the tag path, so it reads like the Data Store.

```text
MB
  AS01
    VS11
      SV21
  AS02
    LB01
```

A note filed on an object sits on its tag. A note filed on a view sits under the tags drawn in that view, because a view is only meaningful in this arrangement through the equipment it shows.

### Why a note appears in more than one place { #why-a-note-appears-in-more-than-one-place }

The two arrangements are linked through the object index, which records which objects are drawn in which views. That link is followed in both directions:

* A note on an object appears under **every** view that object is drawn in. A pump shown in both an overview and a detail view carries its notes in both.
* A note on a view appears under the objects drawn in that view.
* A note on a piece of equipment, rather than a single tag, appears wherever anything belonging to that equipment is drawn.

This is deliberate. A note about a pump is relevant in every view an operator might meet that pump in, and a note about a view is relevant to the equipment it covers.

!!! warning "A note on a cabinet or a device reaches a long way"
    The same rule applies at every level of the tag path. A note filed on a device such as `MB.AS01` belongs to every view that shows anything from that device, which can be most of the plant. Filing a note about a physical cabinet on the **view** that represents it keeps it where it belongs. Filing it on the device tag spreads it across every view fed by that cabinet.

### Objects that share a name { #objects-that-share-a-name }

Two objects drawn in the same view can carry the same name, for example a `GT11` belonging to `VS10` and another belonging to `VS11`. In workview mode both would otherwise claim the same leaf.

When that happens, the leaf label is extended with as much of the tag as is needed to tell them apart, giving `VS10_GT11` and `VS11_GT11`. Objects whose names are already unique in their view keep their plain name.

## Contexts { #contexts }

Contexts are named groupings that can be used to categorise entries across topics. Examples: `Operations`, `Commissioning`, `Alarms`. The default context `General` is always available.

Contexts are managed from the **Change logbook context** popup, opened by clicking **...** next to the Context field when creating or editing an entry. From there, contexts can be added, renamed and deleted. Deleting a context does not delete the entries assigned to it. Those entries remain in the logbook with no context assigned.

When filtering the logbook, selecting a context shows only entries assigned to that context, regardless of topic.

![Context management view](/docs/Images/Logbook/context-management.png){align=center}

## Access Patterns { #access-patterns }

### Global { #global }

The full logbook under **Documents & Logbook → Logbook** shows all entries. The topic tree on the left narrows down to a specific area of the system, in whichever arrangement is selected. This is the primary view for operators who need to review or add notes across the whole project.

### Object Popup { #object-popup }

Every object in the project has a [**Logbook**](../../reference/Popup/Logbook.md) tab in its popup. Opening this tab selects that object in the tree and lists its entries. New entries created from here are filed against the object automatically.

The rest of the tree stays reachable, so a note on a neighbouring object or on the surrounding view can be read without leaving the popup. Entries can be added and edited from here. Archiving is offered in the global logbook only, since that is where archived entries can be shown again and restored. Archived entries are never listed in an object popup.

![Logbook tab in the object popup](/docs/Images/Logbook/object-popup-logbook.png){align=center}

### View-Scoped { #view-scoped }

The **SpeedDial** menu on process views includes a button that opens the logbook with the current view selected in the tree. Its entries are listed straight away, together with those of the objects drawn in the view. New entries created from here are filed against the view.

As in the object popup, the rest of the tree stays reachable from a view-scoped logbook, so a note filed elsewhere can be read without going back to the main view.

## Next Steps { #next-steps }

* [Extending](extending.md) — privileges, topic storage and archiving
<!-- --8<-- [end:body] -->
