---
title: Config.db
description: Table reference for Config.db — the central configuration database in WideQuick MOD.
product: mod
page_type: reference
doc_id: DOC-D2
size: M
priority: p1
status: draft
last_reviewed: 2026-06-11
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Config.db

Config.db is the central configuration database. It stores persistent application state that needs to survive restarts — navigation structures, object registrations, scheduled jobs, saved user settings, and module-specific configuration across most MOD modules.

## Alarms { #alarms }

| Table | Description |
|---|---|
| `AlarmObjects` | Maps alarm names to their device keys. Used by `scAlarmFinder` to resolve which device an alarm belongs to. |
| `mail_schedules` | Notification schedules for alarm emails and SMS. Each row defines a time window, active days, severity filter, and alarm group filter. |
| `mailStats` | Log of every outgoing email and SMS attempt — timestamp, recipient, success flag, and any error message. |

## Navigation { #navigation }

| Table | Description |
|---|---|
| `navMenu` | The main navigation menu structure, stored as JSON. Built and updated by `scNav` at runtime. |
| `subNavs` | Sub-navigation structures for individual views, stored as JSON. Managed by `scSubNav`. |
| `viewPrivilegies` | Privilege requirements per Workview name. Controls which users can access a given view. |

## History { #history }

| Table | Description |
|---|---|
| `History_SavedSignals_Project` | Project-wide saved signal groups in the History module. Available to all users. |
| `History_SavedSignals_View` | View-specific saved signal groups in the History module. Scoped to a particular Workview. |

## Logbook { #logbook }

| Table | Description |
|---|---|
| `logbook` | Logbook entries — text, topic, author, and timestamp. |
| `logbook_contexts` | Topic and context definitions used to categorise logbook entries. |

## Reports { #reports }

| Table | Description |
|---|---|
| `ReportQueue` | Pending report generation jobs waiting to be processed by `scReports`. |
| `reportSchedules` | Scheduled automatic report configurations — frequency, time window, logger, recipients, and output format. |
| `reportStats` | History of completed and failed report jobs, including failure counts and timestamps. |

## Documents { #documents }

| Table | Description |
|---|---|
| `documents` | Document metadata records. |
| `document_files` | File references for documents — either a local file path or an online URL. |
| `document_file_objects_mapping` | Maps document files to process objects by connection, device, system, and object name. |

## Objects { #objects }

| Table | Description |
|---|---|
| `ObjectList` | Maps process objects to the Workviews they appear in and their Data Store names. Used by `scObjectFinder` and `scLinking` to resolve object locations at runtime. |

## Control Curves { #control-curves }

| Table | Description |
|---|---|
| `StyrkurvaProfile` | Saved control curve profiles per tag. Stores the profile name, description, and a JSON representation of the curve. |

## Time Channels { #time-channels }

| Table | Description |
|---|---|
| `TimeChannelProfile` | Saved time channel profiles per tag. Stores the profile name, description, and a JSON representation of the schedule. |

<!-- --8<-- [end:body] -->
