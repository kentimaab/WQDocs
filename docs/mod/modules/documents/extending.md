---
title: Documents - Extending
description: Extend the Documents module — privilege reference.
product: mod
page_type: extending
doc_id: DOC-M16
status: draft
last_reviewed: 2026-05-27
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Documents - Extending

## Privileges { #privileges }

Access to document actions is controlled by privileges. Buttons that require a privilege the current user does not have are visible but disabled. The required privilege is displayed below each disabled button.

![Documents view with privilege notices shown on restricted buttons](/Images/Documents/documents-privileges.png){align=center}

| Privilege | Controls |
|---|---|
| `Documents_Upload` | **Add document** — upload local files and add online resources |
| `Documents_Edit` | **Edit selected document** — rename documents |
| `Documents_Delete` | **Delete document** — permanently remove a document |
| `Documents_Sync` | **Sync with local files on server** — sync the document list with the server filesystem |
| `Documents_Link` | Linking and unlinking documents from within the object popup |
<!-- --8<-- [end:body] -->
