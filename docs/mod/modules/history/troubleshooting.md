---
title: History
description: Common issues and solutions for the History module.
product: mod
page_type: troubleshooting
doc_id: DOC-M18
status: draft
last_reviewed: 2026-10-28
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# History

## Common Issues { #common-issues }

| Problem | Solution |
|---|---|
| Signal tree is empty | The signal tree is populated by scanning the project's loggers. If no loggers are configured, the tree will be empty. Verify that at least one logger is active in the project configuration. |
| A signal is missing from the tree | Only signals with an active logger appear in the tree, and only cyclic, change and trigger loggers count. The process view that holds the object must also have been opened at least once, since the tree only lists objects found in opened views. Use **Show variables not being logged** in the project-wide view to confirm whether the signal is present but unlogged. |
| Chart is blank after clicking Apply | Confirm that the selected time interval contains logged data for those signals. If the signals were only recently added, there may not yet be enough data to display. |
| Saved signal groups are missing | Project-wide saved groups are stored in the `History_SavedSignals_Project` table. View-specific groups are stored in `History_SavedSignals_View`. If groups are missing after a project update, check whether the relevant table was overwritten during the update. |
| Y-axis ranges are unexpected | When **Scale Y-axes** is off, the Y-axis range uses the default limits for each signal unit. Enable **Scale Y-axes** in the **Settings** panel to fit the chart to actual data. |
| A signal logged in more than one logger is read from the wrong one | History uses the first logger in alphabetical order. See [Signals Logged in More Than One Logger](#signals-in-several-loggers). |

## Signals Logged in More Than One Logger { #signals-in-several-loggers }

Each curve in the chart reads from one logger. When a signal is logged in more than one, History goes through the loggers in alphabetical order and uses the first one that logs the signal.

This applies in the History view, the view-specific History popup and the History tab in object popups. Each signal is picked on its own, so the curves in one chart can come from different loggers.

### Switching Logger in Runtime { #switching-logger-in-runtime }

In the History view and the view-specific History popup, a curve can be moved to another logger from the chart's built-in settings:

1. Click the settings button in the bottom-left corner of the chart.
2. Under **Graphs**, select the curve.
3. Choose another logger in **Logger**.

The switch is temporary. History picks the logger again whenever it re-adds a curve: **Apply** does that for every curve, and **Track** and **Unfollow** for the tracked signal. The switch is also lost when the view is closed, and saved signal groups do not keep it.

The History tab in object popups has no settings button, so the logger cannot be switched there.

### Renaming a Logger { #renaming-a-logger }

To make History prefer a logger permanently, rename it in the Designer so that it comes first alphabetically among the loggers that log the signal. The rename affects every signal the logger shares with another logger, not only the one in question.

The logged data is kept. A database logger stores its data in tables named after its ID (`wq_<ID>_data0` and so on), and the ID does not change with the name.

Before renaming, search the project for the old name and update whatever refers to it. Reports, report schedules and scripts can name a logger directly, for example `Loggers["EnergyLogg"]`, and saved report schedules store the logger name in the database.

!!! note "Dashboards use the same rule"
    Dashboard history and bar chart widgets also read a signal from the first logger in alphabetical order, so a rename changes which logger they use as well.

## Known Bugs { #known-bugs }

| Problem | Solution | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
