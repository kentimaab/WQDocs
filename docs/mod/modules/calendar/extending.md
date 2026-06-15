---
title: Calendar — Extending
description: Extend the Calendar module and troubleshoot common issues.
product: mod
page_type: extending
doc_id: DOC-M13
status: draft
last_reviewed: 2026-05-26
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Calendar — Extending

## Reminder Configuration { #reminder-configuration }

There is currently no UI for reminder settings. Both can be set from a script.

### Global Offset { #global-offset }

The number of days before a deadline that a reminder event appears. Default is 3 days. Use `scMaintenance.setReminderOffset` and pass the value in milliseconds:

```javascript
var days = 5;
scMaintenance.setReminderOffset(days * 24 * 60 * 60 * 1000);
```

### Per-Template Toggle { #per-template-toggle }

Controls whether reminders are generated for tasks created from a specific template. Default is off. There is no helper function for this — update the `maintenanceLog_templates` table directly and call `updateTemplates()` to refresh the in-memory cache so the calendar picks up the change immediately:

```javascript
var templateType = "Filterbyte";
var current = scMaintenance.getAllTemplatesMap()[templateType];
var newVal = (current && current.reminder_enabled === 1) ? 0 : 1;
DatabaseConnections["maintenance"].exec(
    "UPDATE maintenanceLog_templates SET reminder_enabled = " + newVal + " WHERE type = '" + templateType + "'"
);
scMaintenance.updateTemplates();
```

Tasks created without a template always generate reminders regardless of this setting.

<!-- --8<-- [end:body] -->
