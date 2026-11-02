---
title: Maintenance - Extending
description: Extend the Maintenance module — calendar integration and troubleshooting.
product: mod
page_type: extending
doc_id: DOC-M6
status: draft
last_reviewed: 2026-10-12
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->

# Maintenance - Extending

## Calendar Integration { #calendar-integration }

Maintenance tasks with upcoming deadlines automatically appear as events in the Calendar module. This gives a time-based overview of scheduled maintenance across the project without needing to open the maintenance list.

The calendar reads tasks from the maintenance database and displays them based on their deadline date. Tasks with the status **Done**, **Done - Delayed** or **Removed** are excluded.

A reminder event appears in the calendar a set number of days before each task's deadline. The default reminder offset is 3 days, and the offset can be configured from a script. Reminders are switched on per template with the **Create a reminder 3 days before** checkbox in **Maint. - Templates**. A task whose template has it unchecked gets no reminder, and new templates start with it unchecked. See [Reminder Configuration](../calendar/extending.md#reminder-configuration) in the Calendar module.
<!-- --8<-- [end:body-1] -->

![Maintenance tasks visible as events in the Calendar view](/docs/Images/Maintenance/maintenance-in-calendar.png){align=center}

<!-- --8<-- [start:body-2] -->
## Change History { #change-history }

Every change to a maintenance task's status, deadline, assignee, priority or description is recorded automatically and can be viewed under **History → Logs → Audit Trail → Audit Trail - Maintenance**. No configuration is needed. See [Audit Trail](/mod/modules/audit-trail/get-started/#maintenance-change-log) for details.

<!-- --8<-- [end:body-2] -->
