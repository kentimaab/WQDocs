---
title: Logbook — Extending
description: Add logbook support to custom views and buttons.
product: mod
page_type: extending
doc_id: DOC-M15
status: draft
last_reviewed: 2026-05-26
---
<!-- --8<-- [start:body] -->

# Logbook — Extending

## Privileges { #privileges }

Three privileges control access to logbook operations:

| Privilege | Description |
|---|---|
| `Logbook_Add` | Required to create new entries |
| `Logbook_Edit` | Required to edit existing entries |
| `Logbook_Delete` | Required to delete entries |

Users without `Logbook_Add` will not see the **Add** button. The buttons are hidden automatically based on the current user's privileges. No extra script logic is needed.

<!-- --8<-- [end:body] -->
