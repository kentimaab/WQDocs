---
title: History
description: Common issues and solutions for the History module.
product: mod
page_type: troubleshooting
doc_id: DOC-M18
status: draft
last_reviewed: 2026-06-08
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# History

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| Signal tree is empty | The signal tree is populated by scanning the project's loggers. If no loggers are configured, the tree will be empty. Verify that at least one logger is active in the project configuration. |
| A signal is missing from the tree | Only signals with an active logger appear in the tree. Use **Show variables not being logged** in the project-wide view to confirm whether the signal is present but unlogged. |
| Chart is blank after clicking Apply | Confirm that the selected time interval contains logged data for those signals. If the signals were only recently added, there may not yet be enough data to display. |
| Saved signal groups are missing | Project-wide saved groups are stored in the `History_SavedSignals_Project` table. View-specific groups are stored in `History_SavedSignals_View`. If groups are missing after a project update, check whether the relevant table was overwritten during the update. |
| Y-axis ranges are unexpected | When **Scale Y-axes** is off, the Y-axis range uses the default limits for each signal unit. Enable **Scale Y-axes** in the **Settings** panel to fit the chart to actual data. |

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
