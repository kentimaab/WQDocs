---
title: EventList.db
description: Table reference for EventList.db — the system event log and the Audit Trail tracked-variable list.
product: mod
page_type: reference
doc_id: DOC-D7
size: M
priority: p1
status: draft
last_reviewed: 2026-07-01
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# EventList database

The EventList database stores system events and the configuration for the Audit Trail feature.

## Tables { #tables }

| Table | Description |
|---|---|
| `events` | The system event log. One row per event — group name, event text, UTC timestamp, user, system name, user data, and context. Populated by `System.logEvent()`, including the value changes logged by the Audit Trail feature. |
| `auditTrail` | The list of Data Store variables currently tracked by the Audit Trail feature. Managed by `scAuditTrail` — stores only which variables are watched, not their historical values. |

## Audit Trail { #audit-trail }

The Audit Trail feature watches the variables listed in `auditTrail`. When a watched variable's value changes, `scAuditTrail` writes a row to `events` with group name `"Audit trail"`, recording the variable name and its old and new value. Historical Audit Trail entries are read back from `events`, not from `auditTrail`.

<!-- --8<-- [end:body] -->