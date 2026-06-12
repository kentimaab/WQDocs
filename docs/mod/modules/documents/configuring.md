---
title: Documents — Configuring
description: Configure the Documents module — link documents to objects and sync with the filesystem.
product: mod
page_type: howto
doc_id: DOC-M16
status: draft
last_reviewed: 2026-05-27
---
<!-- --8<-- [start:body] -->

# Documents — Configuring

## Linking documents to objects { #linking-documents-to-objects }

Documents can be connected to specific objects in the project. When a document is linked to an object, it becomes accessible in the [**Documents**](../../reference/Popup/Documents.md) tab of that object's popup.

Navigate to **Documents → Object Refs** to manage links.

![Object references view](/Images/Documents/documents-objects-references.png){align=center}

To link documents to an object:

1. Find the object in the list.
2. Click **Edit document links**.
3. Double-click a file to add it. A **+** indicator shows it will be linked.
4. Click **Update document links** to save.

A document can be linked to multiple objects. The same object can have multiple documents linked to it.

## Object popup { #object-popup }

Every object in the project has a [**Documents**](../../reference/Popup/Documents.md) tab available through its popup. Open the popup by clicking on an object and selecting the **Documents** tab. This shows all documents linked to that specific object. Selecting a document and clicking **Open** opens a preview directly in the popup.

![Documents tab in the object popup](/Images/Documents/documents-object-popup.png){align=center}

## Syncing with the filesystem { #syncing-with-the-filesystem }

Local files are stored in the `HTML/documents/` folder on the server. The document list reflects what is registered in the database, not what is physically on disk. If files are added to or removed from the folder directly — for example by copying files over a network share — they will not appear in the list until a sync is performed.

Click **Sync with local files on server** to scan the folder and update the database:

* Files found on disk but not in the database are added to the list.
* Database entries for files no longer on disk are removed.
* Online resources are never removed by the sync.

The sync runs automatically when `scDoc` starts.
<!-- --8<-- [end:body] -->
