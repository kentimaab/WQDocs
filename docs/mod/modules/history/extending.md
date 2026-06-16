---
title: History - Extending
description: Script setup for view-specific history, unlogged signals, and troubleshooting.
product: mod
page_type: extending
doc_id: DOC-M18
status: draft
last_reviewed: 2026-05-27
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# History - Extending

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

In the object popup [**History**](../../reference/Popup/History.md) tab, unlogged signals are always visible on the right side under **Tags that are not logged**, without needing to open any extra window.

<!-- --8<-- [end:body] -->
