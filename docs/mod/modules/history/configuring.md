---
title: History — Configuring
description: Configure signal selection, chart settings and saved signal groups in the History module.
product: mod
page_type: howto
doc_id: DOC-M18
status: draft
last_reviewed: 2026-05-27
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# History — Configuring

## Tracking a Signal { #tracking-a-signal }

The **Track signal** panel keeps the chart centred on a specific signal as its value changes over time.

**To track a signal:**

1. Select a signal from the dropdown.
2. Click **Track**. The tracked signal has a wider line and the other lines are muted in color. 

**To stop tracking:**

1. Click **Unfollow**. The chart returns to its normal display.

## Saved Signal Groups { #saved-signal-groups }

Signal groups can be saved and reloaded to avoid re-selecting the same signals each time. Saved groups are managed from the **Saved groups** section in the **Track signal** panel.

![Saved groups panel showing the group name field, dropdown, and import button](/Images/History/history-saved-signals.png){align=center}

**To save a signal group:**

1. Select the signals and click **Apply** so they are visible in the chart.
2. Type a name in the **Enter group name** field.
3. Click **Save group**. The group is saved and appears in the **Select saved group** dropdown.

**To load a saved group:**

1. Select the group from the **Select saved group** dropdown.
2. Click **Use group**. The signals from the group are selected and applied to the chart.

**To delete a saved group:**

1. Select the group from the **Select saved group** dropdown.
2. Click **Remove group**. The group is removed. This does not affect the logged signal data.

### Importing Groups from Other Views { #importing-groups-from-other-views }

Both the project-wide History and the view-specific History let you import saved groups that were created in other views. This lets you reuse a group saved in one view without having to recreate it.

![Saved groups dialog with All saved on the left and Selected on the right](/Images/History/history-import-groups.png){align=center}

**To import groups from other views:**

1. Click **Import groups from views** in the **Saved groups** section. A dialog opens.
2. The left panel (**All saved**) lists every saved group in the project — both project-wide groups and groups saved in other views, organised by their source.
3. Select a group and click **→** to move it to the right panel (**Selected**).
4. Repeat for each group you want to import.
5. Click **Import and close**. The groups are added to the current saved group list.

To remove a group from your selection before importing, select it in the right panel and click **←**. Click **Clear added** to empty the right panel entirely.

!!! note
    Importing a group copies it into the current context. Changes to the original group after importing are not reflected.

## Next Steps { #next-steps }

* [Extending](extending.md) — opening the view-specific popup from a script and troubleshooting
<!-- --8<-- [end:body] -->
