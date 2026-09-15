---
title: maintenance.db
description: Table reference for maintenance.db — stores maintenance tasks, calendar events, and remote system state.
product: mod
page_type: reference
doc_id: DOC-D4
size: M
priority: p1
status: draft
last_reviewed: 2026-09-15
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Maintenance database

The Maintenance database stores everything related to the Maintenance and Calendar modules, including task configurations, the task log, change history, calendar events, and the registry of known remote systems.

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
| `CalendarEvents` | Custom calendar events — title, object, color, creator, description, and start/end timestamps in milliseconds. Imported events are tagged with the subscription they came from. |
| `calendar_config` | Key-value configuration for the calendar, such as the reminder offset. |
| `ics_subscriptions` | Calendars imported into the project. One row per import, holding its name, the file path it came from, its type, visibility in the calendar, and any colour override. A database carried over from a build with the REST plugin can also hold rows of the retired `url` and `nager` types. See [Calendar — Extending](../../modules/calendar/extending.md#subscription-storage). |

## Remote Systems { #remote-systems }

| Table | Description |
|---|---|
| `known_systems` | Registry of remote WideQuick nodes — system name, hostname, and last-seen timestamp. Used to track which remote systems are connected. |

<!-- --8<-- [end:body] -->
