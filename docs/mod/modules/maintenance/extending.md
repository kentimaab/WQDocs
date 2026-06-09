---
title: Maintenance — Extending
description: Extend the Maintenance module — calendar integration and troubleshooting.
product: mod
page_type: extending
doc_id: DOC-M6
status: draft
last_reviewed: 2026-05-26
---
<!-- --8<-- [start:body] -->

# Maintenance — Extending

## Calendar Integration { #calendar-integration }

Maintenance tasks with upcoming deadlines automatically appear as events in the Calendar module. This gives a time-based overview of scheduled maintenance across the project without needing to open the maintenance list.

The calendar reads tasks from the maintenance database and displays them based on their deadline date. Tasks with the status **Done**, **Done - Delayed** or **Removed** are excluded.

A reminder event appears in the calendar a set number of days before each task's deadline. The default reminder offset is 3 days. The offset and per-template reminder toggle can both be configured from a script — see [Calendar — Extending](../calendar/extending.md#reminder-configuration).

![Maintenance tasks visible as events in the Calendar view](/Images/Maintenance/maintenance-in-calendar.png){align=center}

## Change History { #change-history }

Every change to a maintenance task — status, deadline, assignee, priority and description — is automatically recorded and viewable under **History → Logs → Trace log → Audit Trail - Maintenance**. No configuration is needed. See [Trace Log](/mod/guides/audit-trail/#maintenance-change-log) for details.

## Troubleshooting { #troubleshooting }

### Maintenance widget on the dashboard always shows zero for active tasks { #maintenance-widget-on-the-dashboard-always-shows-zero-for-active-tasks }

Confirm that the maintenance database connection is active and that the maintenance table contains records with the expected status values.

### A recurring task was not created after completing the previous one { #a-recurring-task-was-not-created-after-completing-the-previous-one }

Check that the configuration is still set to active. If the object was removed from the configuration's object list between completions, no new task is generated for that object.

### Tasks show the status Ongoing { #tasks-show-the-status-ongoing }

**Ongoing** is a legacy status from an earlier version of the module. The `scMaintenance` script includes a migration that automatically converts these to **Planned** on startup. If tasks still show **Ongoing** after the system has been restarted, check that the `scMaintenance` script is running and that the migration completed without errors.

### A missed task did not generate a follow-up { #a-missed-task-did-not-generate-a-follow-up }

Check that **Auto-create next maintenance on missed deadline** is enabled on the recurring configuration. If it is disabled, the schedule does not continue automatically when a task is missed.
<!-- --8<-- [end:body] -->
