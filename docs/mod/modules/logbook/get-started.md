---
title: Logbook - Get Started
description: Get up and running with the Logbook module.
product: mod
page_type: getstarted
doc_id: DOC-M15
status: draft
last_reviewed: 2026-08-25
scripts:
  - scDoc
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Logbook - Get Started
???+ info "Requirements"
    The following scripts are required to use Logbook and all
    related functionality covered in the Logbook guides:
    
    * `scDoc`
    * `scLinking`
    * `scSubNav`
    * `scObjectFinder`
    * `scPrototypes`
    * `scSuffix`
    * `scThemes`
    * `scUsers`
    * `scAlert`

The Logbook is available in the main menu under **Documents & Logbook → Logbook**.

## The Logbook View { #the-logbook-view }

The logbook view has two panels. The left panel shows the topic tree — a hierarchical list of all topics that have at least one entry. Selecting a node and clicking **Show entries** loads all entries under that topic into the entry list on the right. Selecting **All topics** at the top of the tree shows all entries across all topics.

The entry list shows the following columns: **Title**, **Message**, **Context**, **User**, **Created** and **Last modified**.

Select an entry and click **Edit note** to open it for editing, or **Archive note** to move it out of the active list. An archived entry is kept in the database and hidden from the list rather than removed, and the same button restores it once archived entries are shown.

!!! note "Entries are archived, not deleted"
    There is no per-entry delete. The only action that removes logbook content permanently is **delete all archived notes** in the settings view, which clears every archived entry at once. See [Archiving](extending.md#archiving).

![Logbook view with topic tree and entry list](/docs/Images/Logbook/logbook-overview.png){align=center}

## Creating an Entry { #creating-an-entry }

Click **Add note** to open the **Create new logbook entry** popup. Fill in the following fields:

* **Topic** — the path this entry belongs to. Use `/` to create levels, for example `MB/AS01/VS10/GT11`. The entry is then findable by selecting any parent node in the topic tree.
* **Context** — an optional grouping label. Click **...** to manage available contexts.
* **Title** — a short headline for the entry.
* **Message** — the full text of the note.

Click **Save** to save and continue, or **Save & Close** to save and close the popup. The entry appears immediately at the top of the entry list.

![Create entry popup with fields labeled](/docs/Images/Logbook/create-entry-popup.png){align=center}

## Filtering { #filtering }

Click the filter icon to open the **Filter logbook** panel. Available filters:

* **Time period** — filter by creation date range (Created from / Created to)
* **User** — show entries from a specific user only
* **Search** — search by text in the title, the message, or both
* **Sorting** — newest first or oldest first
* **Show archived** — include archived entries in the list. Archived entries are hidden until this is enabled.

Click **Apply** to apply the filters, **Clear filter** to reset, or **Cancel** to close without changes.

![Filter panel](/docs/Images/Logbook/logbook-filter.png){align=center}

## Next Steps { #next-steps }

* [Configuring](configuring.md) — topics, contexts and access patterns
* [Extending](extending.md) — adding a logbook to a custom view or button
<!-- --8<-- [end:body] -->
