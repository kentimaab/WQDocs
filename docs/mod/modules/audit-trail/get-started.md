---
title: Trace Log — Get Started
description: Get up and running with the Trace Log (Audit Trail) module.
product: mod
page_type: getstarted
doc_id: DOC-M19
status: draft
last_reviewed: 2026-06-08
scripts:
  - scAuditTrail
---
<!-- --8<-- [start:body] -->

# Trace Log — Get Started
???+ info "Requirements"
    The following scripts are required to use Trace Log and all
    related functionality covered in the Trace Log guides:
    
    * `scAuditTrail`
    * `scAlert`

The Trace Log records changes to selected DataStore variables and maintenance tasks. It is available under **History → Logs → Trace log**.

## Viewing the Log { #viewing-the-log }

Navigate to **History → Logs → Trace log → Trace log**.

![Trace log view](/Images/Audit_Trail/audit-trail-log.png){align=center}

The log shows all recorded changes with the following columns:

* **Time** — when the change occurred.
* **Event** — the old value and new value, shown as `old → new`.
* **Context** — the full variable path in the DataStore.
* **User** — the user logged in when the change was made.

Use the **Filter** panel on the left to narrow down the log:

* **Object** — filter by a specific object or variable path.
* **Time** — show all events, events within a selected time span, or the most recent events only.
* **User** — filter by a specific user.
* **Number of rows** — limit how many entries are shown.

Click **Filter** to apply. Click **Clear audit log** to permanently delete all log entries.
## Maintenance Change Log { #maintenance-change-log }

Navigate to **History → Logs → Trace log → Audit Trail - Maintenance**.

![Audit Trail - Maintenance view](/Images/Audit_Trail/audit-trail-maintenance.png){align=center}

This view shows a full history of changes to maintenance tasks. Every status change, deadline update, priority change, assignee change and description edit is recorded automatically. No configuration is needed.

Each row shows:

* **Task** — the maintenance type.
* **Object** — the object the task belongs to.
* **Changed by** — the user who made the change, or **System** for automatic changes such as missed deadline transitions.
* **Change Time** — when the change occurred.
* **Previous Status** — the status before the change.
* **Current Status** — the status after the change.

Select a row and click **Open** to see the full before/after detail for that change, including assignee, priority, deadline and description.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — choosing which variables to track
<!-- --8<-- [end:body] -->
