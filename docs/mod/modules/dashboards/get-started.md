---
title: Dashboards — Get started
description: Get up and running with the Dashboards module.
product: mod
page_type: getstarted
doc_id: DOC-M14
status: draft
last_reviewed: 2026-05-26
scripts:
  - scDashboard
  - scAlarm
object_libraries: 
    - Dashboard Widgets
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Dashboards — Get started
???+ info "Requirements"
    The following scripts are required to use Dashboards and all
    related functionality covered in the Dashboards guides:
    
    * `scDashboard`
    * `scAlarm`
    * `scHistory`
    * `scPrototypes`
    * `scThemes`
    * `scAlert`
    * `scQuickSort`
    
    And the following Object Libraries:
    
    * `Dashboard Widgets`

WideQuick MOD comes with three example dashboards that can be used as a starting point or modified to fit a project.
New Dashboards can be created either from the template or from scratch depending on what the user wants.
<figure markdown="span">
    ![Dashboard](/Images/Dashboard/Dashboard.png)  <figcaption>The Energy Dashboard in WideQuick Runtime</figcaption>
</figure>

## Setting Up a New Dashboard { #setting-up-a-new-dashboard }

Duplicate the dashboard template in **WideQuick Designer®** by right clicking the template in the project tree and move it to the correct folder in the project structure.

![Setting up a dashboard](/Images/Dashboard/SetupDashboard.gif){align=center}
## Widgets — Pre-built Components for the Dashboard { #widgets-pre-built-components-for-the-dashboard }

Dashboards are built using pre-built widgets from the `Dashboard Widgets` library.
Each widget is designed for a specific type of data and can be placed and
configured directly without any custom development. Most widgets also exist in different sizes. 

![Widget](/Images/Dashboard/Widget.png){align=center}

## Grid Layout — Positioning Widgets in the Editor { #grid-layout-positioning-widgets-in-the-editor }

The dashboards in **WideQuick Designer®** uses a 4×4 grid to help with widget placement. Each grid
position is marked by an ellipse that acts as a placement guide. These ellipses
are not visible at runtime.

![Grid](/Images/Dashboard/Grid.png){align=center}

## Adding a Widget { #adding-a-widget }

Add a widget by dragging it from the `Dashboard Widgets` library onto the dashboard, then fill in the relevant parameters in the properties panel. For a full list of available widgets and their parameters, see [Configuring](configuring.md).

![Adding a widget](/Images/Dashboard/UseWidget.gif){align=center}

## Next Steps { #next-steps }

* [Configuring](configuring.md) — widget reference and parameter details
* [Extending](extending.md) — custom widgets, design patterns and troubleshooting
<!-- --8<-- [end:body] -->
