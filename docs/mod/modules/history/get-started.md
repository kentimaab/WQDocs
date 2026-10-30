---
title: History - Get started
description: Get up and running with the History module.
product: mod
page_type: getstarted
doc_id: DOC-M18
status: draft
last_reviewed: 2026-10-12
scripts:
  - scHistory
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->

# History - Get started
???+ info "Requirements"
    The following scripts are required to use History and all
    related functionality covered in the History guides:
    
    * `scHistory`
    * `scPrototypes`
    * `scAlert`
    * `scQuickSort`

The History module displays logged signal data as interactive line charts. There are three ways to access it: the project-wide **History** view from the main menu, a view-specific **History** popup opened from a workview, and the [**History**](../../reference/Popup/History.md) tab in any object popup.

## The History View { #the-history-view }

The project-wide **History** view is available from the main menu. It shows signals from across the entire project.
<!-- --8<-- [end:body-1] -->

![History view with a signal plotted](/docs/Images/History/history-view.png){align=center}

<!-- --8<-- [start:body-2] -->
The view has a chart at the top and three panels at the bottom:

* **Signals** — a tree of all logged signals in the project, grouped by system. Signals are selected here and applied to the chart.
* **Track signal** — options for tracking a live signal on the chart. Also contains the **Saved groups** section for saving and loading named signal groups.
* **Settings** — toggles for legend, ruler and Y-axis scaling, plus time interval and update interval controls.

The **Show variables not being logged** button in the top-right corner opens a separate window that shows all signals not connected to a logger. 

## Selecting Signals { #selecting-signals }

1. Expand the **Signals** tree to find the signal. Click **Expand all** to open all nodes at once.
2. Click the signal to select it. Multiple signals can be selected at once. The **Apply** button shows how many signals are currently selected.
3. Click **Apply** to plot the selected signals on the chart.
4. To clear all signals from the chart, click **Clear sel.**

The second column of the tree shows the line type for each selected signal. Clicking the line type symbol cycles through the available styles (Full or dashed).

## Settings { #settings }

The **Settings** panel controls how the chart looks and how often it updates.
<!-- --8<-- [end:body-2] -->

![Settings panel showing toggles and interval controls](/docs/Images/History/history-panels.png){align=center}

<!-- --8<-- [start:body-3] -->
| Setting | Description |
|---|---|
| Show legend | Toggles the signal legend in the chart area. |
| Show ruler | Toggles a vertical ruler line that follows the cursor. |
| Scale Y-axes | Enables auto-scaling of all Y-axes to fit the visible data. |

**Time interval** sets how much history is shown. When the ruler is shown, the interval is centred on the ruler. Otherwise it ends at the current time.

| Button | Description |
|---|---|
| 30 s | Shows 30 seconds |
| 5 min | Shows 5 minutes |
| 1 h | Shows 1 hour |
| 6 h | Shows 6 hours |
| 1 day | Shows 1 day |
| 7 days | Shows 7 days |
| 14 days | Shows 14 days |
| 30 days | Shows 30 days |

**Update interval** sets how often the chart refreshes with new data:

| Button | Description |
|---|---|
| 0 s | No automatic update |
| 1 s | Update every second |
| 5 s | Update every 5 seconds |
| 10 s | Update every 10 seconds |

## View-Specific History { #view-specific-history }

The **SpeedDial** menu on process views includes a button that opens a view-specific history popup. It works exactly like the project-wide view but shows only signals from objects that belong to that view.
<!-- --8<-- [end:body-3] -->

![View-specific history popup](/docs/Images/History/history-view-specific.png){align=center}

<!-- --8<-- [start:body-4] -->
Signal selection, time controls, settings and saved signal groups work the same way. Saved signal groups in this popup are stored per view and are separate from project-wide saved groups. The signals of project-wide groups and of groups saved in other views can also be fetched with **Get signals from other groups**. See [Importing Groups from Other Views](configuring.md#importing-groups-from-other-views).

Since the view-specific History only shows signals belonging to the current view, signals from other views can be brought in with **Import signals**.
<!-- --8<-- [end:body-4] -->

![Import signals dialog with Available on the left and Selected on the right](/docs/Images/History/history-import-signals.png){align=center}

<!-- --8<-- [start:body-5] -->
**To import signals from other views:**

1. Click **Import signals**. A dialog opens showing all signals from all other views, organised by system and object.
2. Expand the tree in the **Available** panel to find the signal to add.
3. Select a signal and click **→** to move it to the **Selected** panel.
4. Repeat for each signal to add.
5. Click **Import and close**. The signals are added to the signal list already selected. Click **Apply** to plot them.

To remove a signal from the selection before importing, select it in the **Selected** panel and click **←**. Click **Clear added** to empty the right panel entirely.


## Object Popup (History Tab) { #object-popup-history-tab }

Every object in the project has a [**History**](../../reference/Popup/History.md) tab in its popup. Opening the tab shows the logged signals for that object in a chart.
<!-- --8<-- [end:body-5] -->

![History tab in an object popup](/docs/Images/History/history-object-popup.png){align=center}

<!-- --8<-- [start:body-6] -->
Signals that belong to the object but have no logger configured are listed on the right side under **Tags that are not logged**.

The signal list supports keyboard navigation using the **▲** and **▼** buttons. Click **Pick** to select the highlighted signal.

Signals with the suffix `_MV` (measured value) are selected automatically when the popup opens.

Click **Apply** to plot the selected signals. Click **Close** to close the popup.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — signal selection, track signal, saved groups and chart settings in detail
* [Extending](extending.md) — opening the view-specific popup from a script and troubleshooting
<!-- --8<-- [end:body-6] -->