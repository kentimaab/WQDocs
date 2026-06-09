---
title: History — Extending
description: Script setup for view-specific history, unlogged signals, and troubleshooting.
product: mod
page_type: extending
doc_id: DOC-M18
status: draft
last_reviewed: 2026-05-27
---
<!-- --8<-- [start:body] -->

# History — Extending

## Opening View-Specific History { #opening-view-specific-history }

The view-specific history popup is opened from a workview using a script. The view passes its own link name so the popup knows which objects to include:

```javascript
app.popOut.newData = { linkName: view.linkName };
app.popOutVisible = true;
app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie");
```

The popup reads the `ObjectList` table in the configuration database and filters to rows where `View` matches the provided `linkName`. The resulting set of objects determines which signals appear in the signal tree.

Saved signal groups in the view-specific popup are stored per view in the `History_SavedSignals_View` table. Groups saved here are not visible in the project-wide **History** view, and vice versa.

## Signals Not Logged { #signals-not-logged }

The **Show variables not being logged** button in the project-wide view opens a separate window with a tree of all signals that exist in the system but have no active logger. The window is read-only — it is only for identifying missing loggers.

In the object popup **History** tab, unlogged signals are always visible on the right side under **Tags that are not logged**, without needing to open any extra window.

## Troubleshooting { #troubleshooting }

**Signal tree is empty**

The signal tree is populated by scanning the project's loggers. If no loggers are configured, the tree will be empty. Verify that at least one logger is active in the project configuration.

**A signal is missing from the tree**

Only signals with an active logger appear in the tree. Use **Show variables not being logged** in the project-wide view to confirm whether the signal is present but unlogged.

**Chart is blank after clicking Apply**

Confirm that the selected time interval contains logged data for those signals. If the signals were only recently added, there may not yet be enough data to display.

**Saved signal groups are missing**

Project-wide saved groups are stored in the `History_SavedSignals_Project` table. View-specific groups are stored in `History_SavedSignals_View`. If groups are missing after a project update, check whether the relevant table was overwritten during the update.

**Y-axis ranges are unexpected**

When **Scale Y-axes** is off, the Y-axis range uses the default limits for each signal unit. Enable **Scale Y-axes** in the **Settings** panel to fit the chart to actual data.
<!-- --8<-- [end:body] -->
