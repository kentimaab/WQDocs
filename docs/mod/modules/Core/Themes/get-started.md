---
title: Themes — Get Started
description: Get up and running with the Themes module.
product: mod
page_type: getstarted
status: draft
last_reviewed: 2026-05-29
---
<!-- --8<-- [start:body] -->

# Themes — Get Started

!!! note "Requirements"
    The `scThemes` script must be running for the Themes module to work.

## Light and dark mode { #light-and-dark-mode }

WideQuick MOD ships with both a light and a dark theme. The two variants share the same color structure but invert the surface hierarchy — backgrounds that are light in one become dark in the other, and text colors adjust accordingly.

![Light and dark theme comparison](/Images/Themes/theme-light-dark.png){align=center}

## Switching themes { #switching-themes }

### In WideQuick Designer® { #in-widequick-designer }

The start theme is the theme the application uses when it first loads. It is set in **WideQuick Designer®**. Open the **Themes** branch in the project tree to see all installed themes. Right-click the desired theme and select **Set as start theme**.

![Selecting a theme in WideQuick Designer®](/Images/Themes/Select_theme.gif){align=center}

### At runtime { #at-runtime }

The theme can be switched between light and dark at runtime without restarting the application. Navigate to **Settings** and use the theme toggle. The preference is saved and persists across restarts.

## How objects follow themes { #how-objects-follow-themes }

All objects in the project use theme color roles rather than fixed colors. When the theme changes, every background, text color, border, and surface updates automatically — no manual adjustment is needed per object.

This includes alarm state colors. Objects with active alarms display colors such as the alarm and warning indicators defined in the theme, ensuring visual consistency across themes. See [Workview Animations](../../../guides/workview-animations.md) for how alarm state animations are configured.

## Next Steps { #next-steps }

* [Configuring](configuring.md) — changing individual colors and assigning color roles to objects
* [Extending](extending.md) — creating a custom theme that follows a graphical profile
<!-- --8<-- [end:body] -->
