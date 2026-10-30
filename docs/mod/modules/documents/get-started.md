---
title: Documents - Get Started
description: Get up and running with the Documents module.
product: mod
page_type: getstarted
doc_id: DOC-M16
status: draft
last_reviewed: 2026-10-12
scripts:
  - scDoc
  - scUsers
  - scFilePicker
  - scWM
  - scButtons
  - scNav
  - scToolTip
  - scSmartPopup
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->

# Documents - Get Started
???+ info "Requirements"
    The following scripts are required to use Documents and all
    related functionality covered in the Documents guides:
    
    * `scDoc`
    * `scUsers`
    * `scFilePicker`
    * `scWM`
    * `scButtons`
    * `scNav`
    * `scToolTip`
    * `scSmartPopup`
    * `scSubNav`
    * `scLinking`
    * `scPrototypes`
    * `scSuffix`
    * `scThemes`
    * `scAlert`
    * `scQuickSort`

The Documents module is available under **Documents & Logbook → Documents** in the main menu. The **Documents - List** view is the main entry point. It lists all documents in the system, where they can be added, previewed and managed.



## Files view { #files-view }

The view is split into two panels. The left panel shows a file tree with two categories: **Local files** and **Online files**. Local files are stored on the server; online files are links to external URLs. The right panel shows the preview for the selected file. On **WideQuick® Web**, a third category appears for files that cannot be opened in the browser.
<!-- --8<-- [end:body-1] -->

![Documents Files view](/docs/Images/Documents/documents-list.png){align=center}

<!-- --8<-- [start:body-2] -->
The following actions are available at the bottom of the view:

* **Preview** — opens the selected file in the preview panel.
* **Add document** — opens the upload dialog to add a new document.
* **Delete document** — permanently removes the selected document.
* **Edit selected document** — rename the selected document, or change the URL of an online resource. The path of a local file cannot be edited.
* **Sync with local files on server** — scans the documents folder on the server and updates the list to match. See [Syncing with the filesystem](configuring.md#syncing-with-the-filesystem).

## Uploading a local file { #uploading-a-local-file }

Local files can only be uploaded on the server. On remote and web clients the **Upload file** tab is disabled and shows "File upload is not possible on remote systems".

1. Click **Add document**.
2. Select the **Upload file** tab.
3. Click **Click to browse local files** and double-click files in the file browser to add them to the queue.
4. Optionally click a file name in the queue to rename it before uploading.
5. Click **Upload files**.
<!-- --8<-- [end:body-2] -->

![Upload file tab](/docs/Images/Documents/documents-upload.png){align=center}

<!-- --8<-- [start:body-3] -->
The files are copied to the server and added to the document list under **Local files**.

## Adding an online resource { #adding-an-online-resource }

1. Click **Add document**.
2. Select the **Online resource** tab.
3. Enter the URL in the **Document URL** field.
4. Enter a display name in the **Document name** field.
5. Select the file type using the icon selector.
6. Click **Add**.
7. Click **Upload files**.
<!-- --8<-- [end:body-3] -->

![Online resource tab](/docs/Images/Documents/documents-upload-online.png){align=center}

<!-- --8<-- [start:body-4] -->
The resource is added to the document list under **Online files**. Only the URL is stored. No file is downloaded to the server.

## Previewing a document { #previewing-a-document }

Select a file in the left panel and click **Preview** to load it in the preview panel.

Images, PDFs and web pages render directly in the preview panel. Office and OpenDocument files (Word, Excel, PowerPoint, `.odt`, `.ods`, `.odp`) are never previewed inline. On desktop clients they open in the external application associated with the file type. On **WideQuick® Web** they are grouped separately in the file tree, and an alert explains that they cannot be shown in the browser.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — linking documents to objects and keeping files in sync
* [Extending](extending.md) — privilege reference
<!-- --8<-- [end:body-4] -->