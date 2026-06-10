---
title: Script Dependencies
description: Dependency map for all scripts in WideQuick Modular Framework.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-08
---

# Script Dependencies

This page lists all scripts in WideQuick Modular Framework and their dependencies.
A script listed under **Requires** must be present and running for the script to
function correctly.

## Dependency graph

The graph below shows all scripts grouped by dependency layer — from standalone
scripts at the top to the most complex chains at the bottom. Click a node to
highlight its direct dependencies and dependents. Use the layer buttons to focus
on a specific level.

<div markdown>

--8<-- "mod/reference/Script_Widget.html"

</div>

## Reference tables

### No dependencies

The following scripts have no dependencies and can run standalone:

* `scAlert`
* `scQuickSort`
* `scKeybindings`
* `scModem`
* `scOSK`

### Single dependency

| Script | Requires |
|---|---|
| `scDatabase` | `scAlert` |
| `scObjectFinder` | `scAlert` |
| `scUsers` | `scAlert` |
| `scPrototypes` | `scAlert` |
| `scPlatform` | `scAlert` |
| `scThemes` | `scAlert` |
| `scSuffix` | `scAlert` |
| `scLogBook` | `scAlert` |
| `scAuditTrail` | `scAlert` |
| `scRemoteClients` | `scAlert` |
| `scRemoteSystems` | `scAlert` |
| `scTimeChannel` | `scAlert` |
| `scToolTip` | `scAlert` |
| `scTrend` | `scAlert` |
| `scWM` | `scAlert` |
| `scWeather` | `scAlert` |
| `scMapObjects` | `scAlert` |
| `scButtons` | `scAlert` |
| `scInit` | `scAlert` |
| `scSimMB` | `scAlert` |
| `scMail` | `scAlert` |
| `scReports` | `scAlert` |

### Multiple dependencies

| Script | Requires |
|---|---|
| `scMaintenance` | `scAlert`, `scDatabase` |
| `scSubNav` | `scAlert`, `scUsers`, `scSuffix` |
| `scHistory` | `scAlert`, `scPrototypes`, `scQuickSort`, `scThemes` |
| `scNav` | `scAlert`, `scThemes` |
| `scFilePicker` | `scAlert`, `scThemes` |
| `scAlarm` | `scAlert`, `scPrototypes` |
| `scMap` | `scAlert`, `scThemes`, `scMaintenance` |
| `scSubNavPopup` | `scAlert`, `scUsers`, `scSubNav` |
| `scLinking` | `scAlert`, `scPrototypes`, `scSubNav`, `scObjectFinder` |
| `scSmartPopup` | `scAlert`, `scPrototypes`, `scUsers`, `scSuffix` |
| `scStyrkurva` | `scAlert`, `scSuffix` |
| `scStyrkurvaTid` | `scAlert`, `scSuffix` |
| `scWorkviewAnimation` | `scAlert`, `scSuffix` |
| `scRemoteAlarms` | `scAlert`, `scAlarm` |
| `scReportScheduler` | `scAlert`, `scReports` |
| `scAlarmSender` | `scAlert`, `scMail` |
| `scCalendar` | `scAlert`, `scThemes`, `scMaintenance` |
| `scDashboard` | `scAlert`, `scHistory` |
| `scDoc` | `scAlert`, `scThemes`, `scLinking` |
| `scAlarmFinder` | `scAlert`, `scObjectFinder`, `scLinking`, `scMap` |
| `scDayViewManager` | `scAlert`, `scThemes`, `scCalendar` |
| `scWeekViewManager` | `scAlert`, `scThemes`, `scCalendar` |