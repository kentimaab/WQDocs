---
title: Logbook
description: Overview of the Logbook popup in WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-08-25
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->

# Logbook

The Logbook popup displays the active logbook entries associated with the selected
object. Notes can be created and edited directly from this popup. It is always
visible in the Tab menu regardless of which suffixes the object has. For more
information on how the logbook system works, see [Logbook](../../modules/logbook/index.md).

!!! note "Archived entries are not shown here"
    Archiving, restoring and permanent deletion are handled in the global logbook under
    **Documents & Logbook → Logbook**, which is also the only place archived entries can
    be listed. This popup always shows active entries only. See
    [Logbook — Extending](../../modules/logbook/extending.md#archiving).
<!-- --8<-- [end:body-1] -->

![Logbook popup](/docs/Images/Popups/Logbook.png)

<!-- --8<-- [start:body-2] -->
## Entries { #entries }

The entries list displays all logbook notes associated with the object with the
following columns:

* **Title** — the title of the note
* **Message** — the content of the note
* **Context** — the topic or context the note belongs to
* **User** — the user who created the note
* **Created** — the date and time the note was created
* **Last modified** — the date and time the note was last edited

## Filtering { #filtering }

The left panel allows filtering entries by context using the dropdown. Select
**All topics** to show all entries, or choose a specific context to filter the list.
Click the checkmark button to apply the filter. Click **Show entries** to display
the filtered results.

## Actions { #actions }

The following actions are available at the bottom of the popup:

* **Add note** — creates a new logbook entry for this object. Requires `Logbook_Add`.
* **Edit note** — edits the selected entry. Requires `Logbook_Edit`.
* **Show entries** — loads the entries for the selected topic into the list.

An action the current user lacks the privilege for is disabled and covered by a red
overlay naming the privilege required.
<!-- --8<-- [end:body-2] -->