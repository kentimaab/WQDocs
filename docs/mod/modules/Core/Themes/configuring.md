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

## Changing a specific color { #changing-a-specific-color }

Individual colors in a theme can be adjusted directly in **WideQuick Designer®** without regenerating the full theme.

In the project tree, open the **Themes** branch and double-click the theme to edit. This opens the theme editor.

![Theme editor](/Images/Themes/Theme_menu.png){align=center}

Select the color role to change and set a new value. Changes apply immediately when the theme is active.

For larger changes, such as replacing the primary brand color across all derived roles, use the [Theme Builder](../../../../Tools/theme-builder.md) to regenerate the theme from a new source color instead of updating individual roles manually.

## Color roles { #color-roles }

Themes use the Material Design 3 color role system. Each role has a defined purpose:

* **primary / onPrimary** — main brand color and the text color used on top of it.
* **secondary / onSecondary** — supporting accent color.
* **tertiary / onTertiary** — additional accent for differentiation.
* **surface / onSurface** — the default background for most content areas and the text/icon color used on them.
* **surfaceContainer** and variants — surfaces at different elevation levels, from `surfaceContainerLowest` to `surfaceContainerHighest`.
* **primaryContainer / onPrimaryContainer** — a softer tint of the primary color, used for contained elements such as cards or chips.
* **error / onError** — color used for error and destructive states.
* **outline / outlineVariant** — border and divider colors.

Using the correct role for each element ensures the design adapts correctly across both light and dark themes.

## Assigning color roles to objects { #assigning-color-roles-to-objects }

Color roles are assigned to objects in **WideQuick Designer®** through the object's color properties. Instead of setting a fixed color, select a theme color role — the object then updates automatically whenever the theme changes.

To change which role an object uses, for example switching from `onSurface` to `onPrimaryContainer`, open the object's properties in Designer and update the relevant color property to the desired role.

## Custom colors { #custom-colors }

The **Custom colors** tab in the theme editor allows adding project-specific colors that sit alongside the standard M3 roles. These are useful for colors that have no standard M3 equivalent, such as pipe state colors or process-specific indicators.

Custom colors can be accessed from scripts using:

```javascript title="scThemes — accessing a custom color"
System.themes.color("myCustomColor")
```

Custom colors defined in the active theme are automatically available by name. If a color is used across multiple themes, define it with the same name in each theme so it resolves correctly when switching.
<!-- --8<-- [end:body] -->
