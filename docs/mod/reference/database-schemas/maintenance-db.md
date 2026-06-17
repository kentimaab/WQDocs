---
title: maintenance.db
description: Table reference for maintenance.db — stores maintenance tasks, calendar events, and remote system state.
product: mod
page_type: reference
doc_id: DOC-D4
size: M
priority: p1
status: draft
last_reviewed: 2026-06-11
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# maintenance.db

maintenance.db stores everything related to the Maintenance and Calendar modules, including task configurations, the task log, change history, calendar events, and the registry of known remote systems.

## Maintenance { #maintenance }

| Table | Description |
|---|---|
| `maintenance_configs` | Recurring maintenance configurations — defines the object, type, interval, priority, assignee, and whether missed deadlines auto-generate a follow-up task. |
| `maintenanceLog` | The task log — one row per maintenance task instance, with status, creator, assignee, entry date, deadline, and a reference back to its configuration. |
| `maintenanceLog_templates` | Templates for maintenance task types — defines default priority, deadline type and value, and whether reminders are enabled. |
| `maintenance_events` | Changelog for maintenance tasks — records every status change, reassignment, description edit, and priority change on a log entry. |

## Calendar { #calendar }

| Table | Description |
|---|---|
| `CalendarEvents` | Custom calendar events — title, object, color, creator, description, and start/end timestamps in milliseconds. |
| `calendar_config` | Key-value configuration for the calendar, such as the reminder offset. |

## Remote Systems { #remote-systems }

| Table | Description |
|---|---|
| `known_systems` | Registry of remote WideQuick nodes — system name, hostname, and last-seen timestamp. Used to track which remote systems are connected. |

<!-- --8<-- [end:body] -->
