---
title: Themes
description: Apply, configure, and create themes for WideQuick MOD applications.
product: mod
page_type: concept
status: draft
last_reviewed: 2026-05-29
---
<!-- --8<-- [start:body] -->

# Themes

WideQuick MOD uses a theme system built on Material Design 3 (M3). Every color in the application, including backgrounds, text, borders, surfaces, and status indicators, is drawn from the active theme rather than set as a fixed value. Switching the theme updates the entire application at once.

Themes ship in light and dark variants. Both can be selected in **WideQuick Designer®** and toggled at runtime. The active preference persists across restarts.

Because themes follow the M3 standard, a complete theme with all color roles, elevation surfaces, and dark/light variants can be generated from a single brand color. This makes it practical to build themes that match a customer's graphical profile and the result is coherent, visually distinct, and standards-compliant without manually defining every role.

!!! note "Requirements"
    The `scThemes` script must be running for the Themes module to work.

## Contents { #contents }

### [Get started](get-started.md) { #get-started }
* [**Light and dark mode**](get-started.md#light-and-dark-mode) — The two theme variants and what they look like.
* [**Switching themes**](get-started.md#switching-themes) — Setting the start theme in **WideQuick Designer®** and toggling at runtime.
* [**How objects follow themes**](get-started.md#how-objects-follow-themes) — How colors, text, and alarm states update automatically with the theme.

---

### [Configuring](configuring.md) { #configuring }
* [**Changing a specific color**](configuring.md#changing-a-specific-color) — Editing individual color roles in the theme editor.
* [**Color roles**](configuring.md#color-roles) — Overview of the M3 color role system.
* [**Assigning color roles to objects**](configuring.md#assigning-color-roles-to-objects) — Connecting objects to theme roles in **WideQuick Designer®**.
* [**Custom colors**](configuring.md#custom-colors) — Adding project-specific colors to a theme.

---

### [Extending](extending.md) { #extending }
* [**Creating a custom theme**](extending.md#creating-a-custom-theme) — Generating a theme from a brand color using Material Theme Builder.
* [**Built-in themes**](extending.md#built-in-themes) — The themes that ship with WideQuick MOD.
<!-- --8<-- [end:body] -->
