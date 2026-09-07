---
title: Script Dependencies
description: Dependency map for all scripts in WideQuick Modular Framework.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-08-27
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Script Dependencies

This page lists all scripts in WideQuick Modular Framework and their dependencies.
A script listed under **Requires** must be present and running for the script to
function correctly. Optional, guarded references are not listed: `scCalendar` reads
`scHoliday` only when that script happens to be loaded and works without it, so only
the hard direction, `scHoliday` requiring `scCalendar`, appears below.

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

* `b64`
* `scAlert`
* `scKeybindings`
* `scModem`
* `scOSK`
* `scQuickSort`

### Single dependency

| Script | Requires |
|---|---|
| `scAlarm` | `scAlert` |
| `scAuditTrail` | `scAlert` |
| `scBackUpAndRestore` | `scAlert` |
| `scButtons` | `scAlert` |
| `scDatabase` | `scAlert` |
| `scInit` | `scAlert` |
| `scLinking` | `scAlert` |
| `scLogBook` | `scPrototypes` |
| `scMail` | `scAlert` |
| `scMap` | `scAlert` |
| `scObjectFinder` | `scAlert` |
| `scPlatform` | `scAlert` |
| `scPrototypes` | `scAlert` |
| `scRemoteClients` | `scAlert` |
| `scRemoteSystems` | `scAlert` |
| `scReports` | `scAlert` |
| `scSuffix` | `scAlert` |
| `scThemes` | `scAlert` |
| `scTimeChannel` | `scAlert` |
| `scToolTip` | `scAlert` |
| `scTrend` | `scAlert` |
| `scUsers` | `scAlert` |
| `scWM` | `scAlert` |
| `scWeather` | `scAlert` |

### Multiple dependencies

| Script | Requires |
|---|---|
| `scAlarmFinder` | `scAlert`, `scLinking`, `scMap` |
| `scAlarmSender` | `scAlert`, `scAlarm`, `scPrototypes` |
| `scCalendar` | `scAlert`, `scMaintenance`, `scThemes` |
| `scDashboard` | `scAlert`, `scHistory` |
| `scDayViewManager` | `scAlert`, `scCalendar`, `scThemes` |
| `scDoc` | `scAlert`, `scLinking`, `scPrototypes`, `scThemes` |
| `scFilePicker` | `scAlert`, `scPrototypes`, `scThemes` |
| `scHistory` | `scAlert`, `scPrototypes`, `scQuickSort` |
| `scHoliday` | `scAlert`, `scCalendar` |
| `scMaintenance` | `scAlert`, `scDatabase`, `scLinking`, `scNav`, `scPlatform` |
| `scNav` | `scAlert`, `scQuickSort`, `scSubNav`, `scUsers` |
| `scRemoteAlarms` | `scAlert`, `scAlarm`, `scAlarmSender` |
| `scReportScheduler` | `scAlert`, `scReports` |
| `scSmartPopup` | `scAlert`, `scPrototypes`, `scQuickSort`, `scSuffix`, `scUsers` |
| `scStyrkurva` | `scAlert`, `scQuickSort` |
| `scStyrkurvaTid` | `scAlert`, `scQuickSort`, `scWM` |
| `scSubNav` | `scAlert`, `scPrototypes`, `scUsers` |
| `scSubNavPopup` | `scAlert`, `scSubNav`, `scThemes`, `scUsers` |
| `scWeekViewManager` | `scAlert`, `scCalendar`, `scThemes` |
| `scWorkviewAnimation` | `scAlert`, `scSuffix` |
<!-- --8<-- [end:body] -->
