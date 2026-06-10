---
title: Themes — Configuring
description: Change individual theme colors and assign color roles to objects.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-05-29
---
<!-- --8<-- [start:body] -->

# Themes — Configuring

## Changing a color { #changing-a-color }

In **WideQuick Designer®**, open the **Themes** branch in the project tree and double-click the theme to edit. The **Edit theme** dialog opens with three tabs: **Components**, **Custom colors**, and **Keyboard**.

![Theme editor](/Images/Themes/theme-edit-dialog.png){align=center}

Navigate to the **Custom colors** tab and double-click a color code to change its value.

## How colors are applied to objects { #how-colors-are-applied-to-objects }

Colors from the active theme are applied to objects through scripts. An `onLoad` script or a dynamics expression calls `System.themes.color()` with the name of the color role:

```javascript title="Applying a theme color in onLoad"
this.brush.color1 = System.themes.color("surface")
this.pen.color = System.themes.color("onSurface")
```

To see which color role a specific object uses, check its `onLoad` script or dynamics. The name passed to `System.themes.color()` corresponds directly to an entry in the **Edit theme** settings.

## Custom colors { #custom-colors }

The **Custom colors** tab contains project-specific colors alongside the standard roles — for example `Symbol_Alarm`, `Symbol_Warning`, and `Alarm_Severity_0` through `Alarm_Severity_5`. These follow the same naming convention as standard roles and are used the same way in scripts:

```javascript title="Using a custom color"
System.themes.color("Symbol_Alarm")
```

 To add a new custom color, click **+** at the bottom of the **Custom colors** tab (It will be added as ColorX), assign a name, and set a value. Use the same name across all themes so the color resolves correctly when switching between themes.
<!-- --8<-- [end:body] -->
