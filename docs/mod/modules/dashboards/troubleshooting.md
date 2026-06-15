---
title: Dashboards
description: Common issues and solutions for the Dashboards module.
product: mod
page_type: troubleshooting
doc_id: DOC-M14
status: draft
last_reviewed: 2026-06-08
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Dashboards

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| Widget header shows "undefined" | The `Header` property binding on the widget instance is broken. Check that the binding is correctly set on the widget. |
| Widget header shows a raw Swedish string | The `Header` value is not registered in `Translations.klib`. Add the string to `Translations.klib` and enter the translation under **Translations → Project Translation** in the project tree. |
| Signal value shows -- or is blank | The signal path passed to the widget does not match any entry in DataStore. Check for typos, confirm the signal exists in DataStore and verify that the driver is connected and writing values. |
| Alarm widgets show no alarms despite active alarms existing | The `Grupp` or `Grupper` parameter is set to a group name that does not match any alarm group in the project. Leave the parameter empty to show all alarms, or check the exact group name in the alarm configuration. |
| Maintenance widget always shows zero for active tasks | Confirm that the maintenance database connection is active and that the maintenance table contains records with the expected status values. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
