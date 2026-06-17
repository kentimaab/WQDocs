---
title: Suffix System
description: How suffix objects are structured, their attributes, and how they associate tags with popups at runtime.
product: mod
page_type: reference
doc_id: DOC-M22
status: draft
last_reviewed: 2026-06-11
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Suffix System

The suffix system is how WideQuick MOD connects a clickable object in a Workview to the correct popup controls and Data Store tags. When an operator clicks a pump, valve, or sensor, the suffix system looks up which parameters exist for that object and renders only the controls that apply.

The link between object and parameter is a naming convention: a short string (the suffix) appended to the base tag name. For an object named `MB.AS01.SYS_PUMP1`, a suffix `_BV` resolves to the Data Store tag `MB.AS01.SYS_PUMP1_BV`. If that tag exists, the corresponding control is shown.

Configuration lives in `SuffixConfig.db` as a JSON structure called `SuffixObj`. The structure is loaded by `scSuffix` at startup and read by `scSmartPopup` whenever a popup opens.

## SuffixObj structure { #suffixobj-structure }

`SuffixObj` has two active top-level sections.

| Section | Purpose |
|---|---|
| `Popups` | Defines popup groups — each group maps to a view file and declares which suffix controls it contains. |
| `Views` | Defines tag categories used for alarm, warning, service, and active status indicators. |

## Popups { #popups }

Each entry in `Popups` represents one popup group — a tab or panel that appears when an object is clicked.

```json
"Kontroll": {
  "name": "Kontroll",
  "viewPath": "Control.kvie",
  "Always visible": false,
  "privilage": "",
  "suffixes": {
    "analogOutputValue": {
      "suffix": "_R",
      "desc": "Analog signal ut",
      "decimals": 1,
      "writeable": 1,
      "write_priv": "",
      "unit": ""
    }
  }
}
```

### Popup group attributes { #popup-group-attributes }

| Attribute | Type | Description |
|---|---|---|
| `name` | string | Display name shown as the tab label. |
| `viewPath` | string | The `.kvie` Workview file to load for this popup group. |
| `Always visible` | boolean | If `true`, the tab is shown even if no suffixes exist for the clicked object. If `false`, the tab is hidden unless at least one suffix tag is found in the Data Store. |
| `privilage` | string | Privilege key required to see this tab. Empty string means all users. |
| `suffixes` | object | Map of suffix alias names to suffix definitions (see below). |

### Suffix definition attributes { #suffix-definition-attributes }

| Attribute | Type | Description |
|---|---|---|
| `suffix` | string | The string appended to the object's base tag name to form the Data Store key. |
| `desc` | string | Human-readable label shown in the popup control. |
| `decimals` | number | Number of decimal places for numeric display. |
| `writeable` | number | `1` if the control allows operator input, `0` for read-only display. |
| `write_priv` | string | Privilege key required to write. Empty string falls back to the object's own privilege. |
| `unit` | string | Unit label. Can be left empty if the unit is defined on the Data Store tag description. |

## Views { #views }

Each entry in `Views` defines a tag category used by the status indicator system.

```json
"1 - Alarms": {
  "vector": "alarmTags",
  "blink": "true",
  "suffixes": {
    "Givarfel": {
      "suffix": "_LG",
      "desc": "Givarfel"
    }
  }
}
```

| Attribute | Type | Description |
|---|---|---|
| `vector` | string | The name of the runtime array that will hold matching tag names for this category. |
| `blink` | string | Whether the indicator blinks when tags in this category are active. `"true"` or `"false"`. |
| `suffixes` | object | Suffix definitions scanned to build the category's tag list. Only `suffix` and `desc` are used here. |

## Tag resolution at runtime { #tag-resolution }

When a DynTouch object is clicked, the base tag name is assembled from the object's properties:

```
tagName = Connection + Device + Sys + "_" + ObjectName
```

For example: `MB` + `.AS01.` + `SYS` + `_` + `PUMP1` → `MB.AS01.SYS_PUMP1`

`scSmartPopup` then iterates over every popup group in `SuffixObj.Popups` and checks whether the group should be shown:

1. If `Always visible` is `true`, the tab is included unconditionally.
2. Otherwise, it checks each suffix in the group. If `DataStore[tagName + suffix.suffix]` exists, the tab is included.

Only tabs that pass this check are rendered. This means the popup automatically adapts to the signals that actually exist for the clicked object — no manual configuration per object is needed.

## Component binding { #component-binding }

Popup UI components use the `SuffixAlias` property to declare which suffix they bind to. When a popup opens, `scSmartPopup` calls `activate(suffixObj)` on each registered component, passing the resolved suffix definition. The component then binds its display and input to `DataStore[tagName + suffixObj.suffix]`.

Components that have `always_visible` set to `true` remain visible even if the suffix tag does not exist for the current object.

## CustomPopupFirstOpen { #custompopupfirstopen }

When a popup is opened directly via a DynTouch link (not routed through the tab container), components fire their Load events before the parent view has finished initialising. This means `registerObject()` calls from components happen before `view.popup` exists, and suffix binding is missed.

`scSmartPopup.bootstrapDirect()` solves this. It reconstructs the popup context from the clicked object and re-fires the Load events for all child components, ensuring they register and receive `activate()` after the view is fully ready.

This bootstrap runs automatically. No manual handling is needed in popup Workviews.

## Editing the configuration { #editing }

The suffix configuration is stored as JSON in `SuffixConfig.db` and loaded into memory by `scSuffix` on startup. Changes take effect after restarting the runtime or reloading the script.

`scSuffix` handles migration automatically: if it finds the legacy single-column `JSON` format in `SuffixObj`, it splits the content into the three separate columns (`Popups`, `ProcessViews`, `Views`) on first read.

<!-- --8<-- [end:body] -->
