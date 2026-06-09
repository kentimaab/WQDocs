---
title: Themes — Extending
description: Create a custom theme that follows a graphical profile using Material Theme Builder.
product: mod
page_type: extending
status: draft
last_reviewed: 2026-05-29
---
<!-- --8<-- [start:body] -->

# Themes — Extending

## Creating a custom theme { #creating-a-custom-theme }

WideQuick MOD themes are built on Material Design 3 (M3). This means a full theme, including all color roles, light and dark variants, elevation surfaces, and contrast levels, can be generated from a single source color. The result is a theme that is immediately coherent, visually distinct, and standards-compliant without manually defining every role.

This makes it straightforward to create themes that closely follow a customer's or organization's graphical profile. Feed in the brand's primary color and the M3 system derives all supporting colors in a way that works well together across both light and dark modes.

### Step 1 — Generate the theme { #step-1-generate-the-theme }

Open the [Theme Builder](../../../../Tools/theme-builder.md). The embedded **Material Theme Builder** allows setting a source color (or uploading a logo to extract one) and previewing the resulting theme in light and dark mode. Export the finished theme as a `Colors.xml` file.

### Step 2 — Import into WideQuick { #step-2-import-into-widequick }

On the same [Theme Builder](../../../../Tools/theme-builder.md) page, scroll down to **Parse Theme into WideQuick format**:

1. Select the project's `Themes.kdat` file. This file is located in the project folder (`WideQuick_MOD/`).
2. Select the `Colors.xml` file exported from the Theme Builder.
3. Click **Merge new theme into existing themes file**.
4. Download the updated `Themes.kdat`.

Replace the existing `Themes.kdat` in the project folder with the downloaded file. If **WideQuick Designer®** was open, restart it. The new theme appears under the **Themes** branch in the project tree and can be set as the start theme.

## What M3 generates automatically { #what-m3-generates-automatically }

When a theme is generated through M3, the following are derived automatically:

* **Light and dark variants** — both are produced from the same source color.
* **Surface tonal hierarchy** — a set of surface levels (`surfaceContainerLowest` through `surfaceContainerHighest`) that convey elevation without shadows.
* **Contrast variants** — medium and high contrast versions of each role for accessibility compliance.
* **Color relationships** — all `on*` colors (e.g., `onPrimary`, `onSurface`) are calculated to meet contrast requirements against their background color.

This means that even a heavily customized theme remains legible and visually balanced across all its states.

## Built-in themes { #built-in-themes }

The following themes ship with WideQuick MOD and are available in the project's `Themes.kdat`:

| Theme | Variant |
|---|---|
| WQ_Material_BMS_Light | Light |
| WQ_Material_BMS_Dark | Dark |
| WQ_Material_VA_Light | Light |
| WQ_Material_VA_Dark | Dark |
| WQ_Material_MF_Light | Light |
| WQ_Material_MF_Dark | Dark |

These can be used as-is or as a starting point when building a custom theme. The BMS, VA and MF variants differ in their primary and secondary brand colors but share the same M3 structure.
<!-- --8<-- [end:body] -->
