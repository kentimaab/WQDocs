---
title: Trace Log (Audit Trail)
description: Track and review changes to selected DataStore variables.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-05-27
---
<!-- --8<-- [start:body] -->
# Trace Log (Audit Trail)

The Trace Log records changes to selected DataStore variables. Each entry captures the old value, the new value, the variable path, the user who was logged in when the change occurred, and a timestamp. This makes it possible to review what changed, when, and who made the change.

The Trace Log is available under **History → Logs → Trace log**.

!!! note "Requirements"
    The `scAuditTrail` script must be running for the Trace Log to work.

## Configuring Variables to Track { #configuring-variables-to-track }

Navigate to **History → Logs → Trace log → Audit Trail - Settings**.

![Audit Trail - Settings view](/Images/Audit_Trail/audit-trail-settings.png){align=center}

The view has two panels. The left panel shows all available DataStore variables. The right panel shows the variables currently being tracked.

To start tracking a variable, select it in the left panel and click the **>** button. To stop tracking a variable, select it in the right panel and click the **<** button. Variables can also be added/removed by double-clicking.

Variables can be added at any level of the DataStore tree. Selecting a parent node and clicking **>** adds all variables under that node at once.

!!! warning
    Avoid tracking variables that change continuously, such as measured values and sensor readings. This will generate a very large number of log entries and make the log difficult to use. The Trace Log is intended for variables that change infrequently and deliberately — setpoints, control signals, and configuration values.

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

!!! warning
    **Clear audit log** removes all entries permanently. This cannot be undone.

## Maintenance Change Log { #maintenance-change-log }

Navigate to **History → Logs → Trace log → Audit Trail - Maintenance**.

![Audit Trail - Maintenance view](/Images/Audit_Trail/audit-trail-maintenance.png){align=center}

This view shows a full history of changes to maintenance tasks. Every status change, deadline update, priority change, assignee change and description edit is recorded automatically — no configuration is needed.

Each row shows:

* **Task** — the maintenance type.
* **Object** — the object the task belongs to.
* **Changed by** — the user who made the change, or **System** for automatic changes such as missed deadline transitions.
* **Change Time** — when the change occurred.
* **Previous Status** — the status before the change.
* **Current Status** — the status after the change.

Select a row and click **Open** to see the full before/after detail for that change, including assignee, priority, deadline and description.
<!-- --8<-- [end:body] -->
