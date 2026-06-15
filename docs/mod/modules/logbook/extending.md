---
title: Logbook — Extending
description: Add logbook support to custom views and buttons.
product: mod
page_type: extending
doc_id: DOC-M15
status: draft
last_reviewed: 2026-05-26
tags: 
 - MOD
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

Users without `Logbook_Add` will see the **Add** button area disabled and grayed out, with a red box overlay displaying a message indicating the required privilege. The `Enabled` property on the button is bound to `scUsers.hasPriv("Logbook_Add")`. The same pattern applies to `Logbook_Edit` and `Logbook_Delete`.

<!-- --8<-- [end:body] -->
