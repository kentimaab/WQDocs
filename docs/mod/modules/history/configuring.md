---
title: History - Configuring
description: Configure signal selection, chart settings and saved signal groups in the History module.
product: mod
page_type: howto
doc_id: DOC-M18
status: draft
last_reviewed: 2026-10-12
tags: 
 - MOD
---
<!-- --8<-- [start:body-1] -->

# History - Configuring

## Tracking a Signal { #tracking-a-signal }

The **Track signal** panel highlights a specific signal in the chart.

**To track a signal:**

1. Select a signal from the dropdown.
2. Click **Track**. The tracked signal has a wider line and the other lines are muted in color. 

**To stop tracking:**

1. Click **Unfollow**. The chart returns to its normal display.

## Saved Signal Groups { #saved-signal-groups }

Signal groups can be saved and reloaded to avoid re-selecting the same signals each time. Saved groups are managed from the **Saved groups** section in the **Track signal** panel.
<!-- --8<-- [end:body-1] -->

![Saved groups panel showing the group name field, dropdown, and import button](/docs/Images/History/history-saved-signals.png){align=center}

<!-- --8<-- [start:body-2] -->
**To save a signal group:**

1. Select the signals and click **Apply** so they are visible in the chart.
2. Type a name in the **Enter group name** field.
3. Click **Save group**. The group is saved and appears in the **Select saved group** dropdown.

**To load a saved group:**

1. Select the group from the **Select saved group** dropdown.
2. Click **Use group**. The signals from the group are selected and applied to the chart. In the project-wide History they are added to the signals already selected. In the view-specific History they replace the current selection.

**To delete a saved group:**

1. Select the group from the **Select saved group** dropdown.
2. Click **Remove group**. The group is removed. This does not affect the logged signal data.

### Importing Groups from Other Views { #importing-groups-from-other-views }

Both the project-wide History and the view-specific History can fetch the signals of saved groups created in other views, so a group saved in one view can be reused without recreating it.
<!-- --8<-- [end:body-2] -->

![Saved groups dialog with All saved on the left and Selected on the right](/docs/Images/History/history-import-groups.png){align=center}

<!-- --8<-- [start:body-3] -->
**To import groups from other views:**

1. Click **Get signals from groups in views** (project-wide History) or **Get signals from other groups** (view-specific History) in the **Saved groups** section. A dialog opens.
2. The left panel (**All saved**) lists saved groups organised by their source. In the project-wide History it lists the groups saved in views. In the view-specific History it lists the project-wide groups under **Project** and the groups saved in other views.
3. Select a group and click **→** to move it to the right panel (**Selected**).
4. Repeat for each group to import.
5. Click **Get and close**. The signals of the selected groups are selected in the **Signals** tree, and the **Apply** button shows the new count. A message shows how many signals were fetched, and the dialog closes when it is acknowledged.
6. Click **Apply** to plot the signals.

To remove a group from the selection before importing, select it in the right panel and click **←**. Click **Clear added** to empty the right panel entirely.

!!! note
    Importing fetches only the signals. The groups are not added to the **Select saved group** dropdown. To keep the selection as a group here, save it with **Save group**.

## Next Steps { #next-steps }

* [Extending](extending.md) — opening the view-specific popup from a script and troubleshooting
<!-- --8<-- [end:body-3] -->
