---
title: Maintenance - Extending
description: Extend the Maintenance module — calendar integration and troubleshooting.
product: mod
page_type: extending
doc_id: DOC-M6
status: draft
last_reviewed: 2026-05-26
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Maintenance - Extending

## Calendar Integration { #calendar-integration }

Maintenance tasks with upcoming deadlines automatically appear as events in the Calendar module. This gives a time-based overview of scheduled maintenance across the project without needing to open the maintenance list.

The calendar reads tasks from the maintenance database and displays them based on their deadline date. Tasks with the status **Done**, **Done - Delayed** or **Removed** are excluded.

A reminder event appears in the calendar a set number of days before each task's deadline. The default reminder offset is 3 days. The offset and per-template reminder toggle can both be configured from a script — see [Calendar — Extending](../calendar/extending.md#reminder-configuration).

![Maintenance tasks visible as events in the Calendar view](/Images/Maintenance/maintenance-in-calendar.png){align=center}

## Change History { #change-history }

Every change to a maintenance task — status, deadline, assignee, priority and description — is automatically recorded and viewable under **History → Logs → Trace log → Audit Trail - Maintenance**. No configuration is needed. See [Trace Log](/mod/modules/audit-trail/get-started/#maintenance-change-log) for details.

<!-- --8<-- [end:body] -->
