---
title: Documents — Get Started
description: Get up and running with the Documents module.
product: mod
page_type: getstarted
doc_id: DOC-M16
status: draft
last_reviewed: 2026-05-27
---
<!-- --8<-- [start:body] -->

# Documents — Get Started

The Documents module is available under **Documents & Logbook -> Documents** in the main menu. The **Documents - List** view is the main entry point — it lists all documents available in the system and lets you add, preview and manage them.

!!! note "Requirements"
    The `scDoc` script must be running for the Documents module to work.

## Files view { #files-view }

The view is split into two panels. The left panel shows a file tree with two categories: **Local files** and **Online files**. Local files are stored on the server; online files are links to external URLs. The right panel shows the preview for the selected file. On **WideQuick Web®**, a third category appears for files that cannot be opened in the browser.

![Documents Files view](/Images/Documents/documents-list.png){align=center}

The following actions are available at the bottom of the view:

* **Preview** — opens the selected file in the preview panel.
* **Add document** — opens the upload dialog to add a new document.
* **Delete document** — permanently removes the selected document.
* **Edit selected document** — rename the selected document.
* **Sync with local files on server** — scans the documents folder on the server and updates the list to match. See [Syncing with the filesystem](configuring.md#syncing-with-the-filesystem).

## Uploading a local file { #uploading-a-local-file }

1. Click **Add document**.
2. Select the **Upload file** tab.
3. Click the drop zone or drag files into it to add them to the queue.
4. Optionally click a file name in the queue to rename it before uploading.
5. Click **Upload files**.

![Upload file tab](/Images/Documents/documents-upload.png){align=center}

The files are copied to the server and added to the document list under **Local files**.

## Adding an online resource { #adding-an-online-resource }

1. Click **Add document**.
2. Select the **Online resource** tab.
3. Enter the URL in the **Document URL** field.
4. Enter a display name in the **Document name** field.
5. Select the file type using the icon selector.
6. Click **Add**.
7. Click **Upload files**.

![Online resource tab](/Images/Documents/documents-upload-online.png){align=center}

The resource is added to the document list under **Online files**. The URL is stored — no file is downloaded to the server.

## Previewing a document { #previewing-a-document }

Select a file in the left panel and click **Preview** to load it in the preview panel.

Most file types can be previewed inline — images, PDFs and web pages render directly. On **WideQuick Web®**, Office files (Word, Excel, PowerPoint) are not previewable in the browser and are grouped separately in the file tree.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — linking documents to objects and keeping files in sync
* [Extending](extending.md) — privilege reference
<!-- --8<-- [end:body] -->
