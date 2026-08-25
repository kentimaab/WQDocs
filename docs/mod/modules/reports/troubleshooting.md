---
title: Reports
description: Common issues and solutions for the Reports module.
product: mod
page_type: troubleshooting
doc_id: DOC-M16
status: draft
last_reviewed: 2026-08-25
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Reports - Troubleshooting

## Common issues { #common-issues }

| Problem | Solution |
|---|---|
| Dates are out of range | If no data is available for the selected time period the report will fail. Ensure the values are actually being stored in the database. If not, verify that the logger is correctly set up. See [Loggers](../../guides/Loggers.md) for more information. |
| The report is empty | If no data appears in the report the macro command is most likely failing. This only happens when a custom template is used. Review the macro command configuration in [Creating templates](extending.md#creating-templates) |
| Report is not being sent | Either the SMTP server is not configured correctly — try sending a test email from the **Reports - Schedule** view to verify. If that works, verify that the email addresses are correctly entered. See [Alarms — Extending](../Core/alarms/extending.md#email-notifications) for SMTP configuration. |
| **Create Report** does nothing | A report cannot be created until at least one signal is selected in the **LoggerList**. Select a signal and try again. Alarm Reports are exempt, since they include all signals automatically. |
| Values are off by a factor of a thousand | Check the **Unit** and **Prefix** pickers on the report controller. Each selected signal is scaled from its own native prefix to the chosen display unit, so a signal logged in `Wh` and one logged in `kWh` in the same report are both converted before reaching the template. See [Units and prefixes](get-started.md#units-and-prefixes). |
| Scheduled reports never run | Confirm that the five-minute schedule in `Schedules.kdat` calls `scReportScheduler.control_trigger()`. A call naming any other script object is skipped silently, with no error. |

## Known bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->

