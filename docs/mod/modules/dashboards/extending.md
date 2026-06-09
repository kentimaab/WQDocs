---
title: Dashboards — Extending
description: Extend and customise the Dashboards module beyond the defaults.
product: mod
page_type: extending
doc_id: DOC-M14
status: draft
last_reviewed: 2026-05-26
---
<!-- --8<-- [start:body] -->

# Dashboards — Extending

## Custom Widgets — Building New Widgets from Existing Templates { #custom-widgets-building-new-widgets-from-existing-templates }

To base a new widget on an existing one, drag it from the `Dashboard Widgets` library onto a workview in **WideQuick Designer®**. Right-click the placed widget and select **Disconnect from template**. The widget can now be edited freely. Adjust the layout, add or remove objects, and modify the script logic.

Once the changes are done, drag the widget from the workview back into the library list. It is stored there as a new object. To rename it, right-click it in the library list and set a new name.

The same last step applies when building a widget from scratch: once complete, drag it into the library and rename it there.

It is also possible to edit already existing widgets by double clicking one in the library. This opens up a new workview, containing only an editable version of the widget.  

### Grid Dimensions { #grid-dimensions }

Use these dimensions to ensure new widgets align with the dashboard grid. Combine the width and height for the desired span — a 2×1 widget uses width 2 and height 1.

| Units | Width   | Height  |
|-------|---------|---------|
| 1     | 385 px  | 240 px  |
| 2     | 780 px  | 490 px  |
| 3     | 1175 px | 740 px  |
| 4     | 1570 px | 990 px  |

### Inspecting Existing Widgets { #inspecting-existing-widgets }

To understand how a widget handles signals, properties or layout, double-click it in the library list. This opens an editable version of the widget where the script and dynamics for each part can be inspected and used as a reference.

!!! tip
    Right-clicking a placed widget in a workview and selecting **Show template** opens the library and highlights the source object — useful for finding which template a widget on the dashboard came from.

---

## Role-Based Dashboards — Controlling Access and Default Views { #role-based-dashboards-controlling-access-and-default-views }

### Setting View Privileges { #setting-view-privileges }

View privileges restrict which users can access a given dashboard. Set them at runtime by navigating to **Main Menu → Settings → Workview Privileges**. Select the workview from the tree on the left, then set the required privilege level in the **Privilege** dropdown on the right.

![Workview privileges](/Images/Dashboard/WVPriv.png){align=center}

### Setting Default View per Role { #setting-default-view-per-role }

To set a different default dashboard per role, add the logic to the `onLoad` script of the `Workspace.kvie` workview in **WideQuick Designer®**. Use `_sys_user_name` to match a specific user or `System.currentUser().hasPrivilege()` to match a privilege level.

```javascript title="Workspace.kvie — onLoad"
app.MultiViewer = this.MultiviewerPage;
if (_sys_user_name == "Admin"){
    app.MultiViewer.setView("Main_Menu/Dashboards & Kartor/Dashboard/Dashboard Larm.kvie");
}
if (System.currentUser().hasPrivilege("Config")){
    app.MultiViewer.setView("Main_Menu/Dashboards & Kartor/Dashboard/Dashboard Ventilation.kvie");
}
```

---

## Troubleshooting — Common Issues and How to Fix Them { #troubleshooting-common-issues-and-how-to-fix-them }

### Widget header shows "undefined" { #widget-header-shows-undefined }

The `Header` property was left empty on a widget that does not have a default fallback value. Either set the `Header` property on the widget instance or add a fallback in the widget `onLoad` script.

> **Note:** A plain string set as `Header` will not be picked up by the translation system. The string needs to be added to `Translations.klib` and then the translation has to be entered under **Translations → Project Translation** in the project tree.

### Signal value shows -- or is blank { #signal-value-shows-or-is-blank }

The signal path passed to the widget does not match any entry in DataStore. Check for typos, confirm the signal exists in DataStore and verify that the driver is connected and writing values.

### Alarm widgets show no alarms despite active alarms existing { #alarm-widgets-show-no-alarms-despite-active-alarms-existing }

The `Grupp` or `Grupper` parameter is set to a group name that does not match any alarm group in the project. Leave the parameter empty to show all alarms, or check the exact group name in the alarm configuration.

### Maintenance widget always shows zero for active tasks { #maintenance-widget-always-shows-zero-for-active-tasks }

Confirm that the maintenance database connection is active and that the maintenance table contains records with the expected status values.
<!-- --8<-- [end:body] -->
