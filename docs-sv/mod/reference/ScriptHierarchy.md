---
title: Skriptberoenden
product: mod
page_type: reference
status: draft
last_reviewed: 2026-08-27
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Skriptberoenden

Den här sidan listar alla skript i WideQuick Modular Framework och deras beroenden.
Ett skript som anges under **Kräver** måste finnas och köras för att skriptet ska
fungera korrekt. Valfria, skyddade referenser listas inte: `scCalendar` läser
`scHoliday` endast när det skriptet råkar vara laddat och fungerar utan det, så bara
den hårda riktningen, att `scHoliday` kräver `scCalendar`, visas nedan.

## Beroendegraf

Grafen nedan visar alla skript grupperade efter beroendeskikt — från fristående
skript högst upp till de mest komplexa kedjorna längst ned. Klicka på en nod för att
markera dess direkta beroenden och beroende skript. Använd skiktknapparna för att
fokusera på en specifik nivå.

<div markdown>

--8<-- "mod/reference/Script_Widget.html"

</div>

## Referenstabeller

### Inga beroenden

Följande skript har inga beroenden och kan köras fristående:

* `b64`
* `scAlert`
* `scKeybindings`
* `scModem`
* `scOSK`
* `scQuickSort`

### Ett beroende

| Skript | Kräver |
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

### Flera beroenden

| Skript | Kräver |
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
