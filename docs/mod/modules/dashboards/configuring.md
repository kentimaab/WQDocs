---
title: Dashboards - Configuring
description: Configure and customise the Dashboards module.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-05-26
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Dashboards - Configuring

## Parameters - Common Settings Shared by All Widgets { #parameters-common-settings-shared-by-all-widgets }

All widgets share a `Header` parameter, a string, that sets the title displayed on the widget. If left empty the widgets has a standard header.


Parameters that accept multiple signals or groups accept either a single string or an array of strings.

```javascript title="Single signal"
"MB.AS01.VS10_VMM1_E"
```

```javascript title="Multiple signals"
["MB.AS01.VS10_VMM1_E", "MB.AS01.VS10_VMM1_P"]
```

Some widgets include an expand button in the top-right corner. Clicking it opens a fullscreen version of the widget for a more detailed view.

Widgets that display a signal legend automatically handle overflow. When there are more signals than fit in the legend, a button shows how many are hidden. Clicking it opens the fullscreen view with all signals listed.

## Widgets - All Available Widgets and Their Parameters { #widgets-all-available-widgets-and-their-parameters }

### Alarm Status { #alarm-status }

Displays alarm counts — total, acknowledged and unacknowledged.

![Alarm Status](/Images/Dashboard/AlarmStatus.png){align=center}

**Parameters**

* `Grupp` — Filter alarms by group name. Leave empty to show all alarms.

---

### Alarm Row { #alarm-row }

A compact single-row alarm indicator. Intended to sit at the top or bottom of a dashboard as a thin status band.

![Alarm Row](/Images/Dashboard/AlarmRow.png){align=center}

**Parameters**

* `Grupper` — Filter alarms by group name. Leave empty to show all alarms.

---

### Alarm List { #alarm-list }

Displays currently active alarms in a scrollable list.

![Alarm List](/Images/Dashboard/AlarmList.png){align=center}

**Parameters**

* `Grupper` — Filter alarms by group name. Leave empty to show all alarms.

---

### Alarm Log { #alarm-log }

Displays historical alarms in a scrollable list.

![Alarm Log](/Images/Dashboard/AlarmLog.png){align=center}

**Parameters**

* `Grupper` — Filter alarms by group name. Leave empty to show all alarms.

---

### Alarm Frequency { #alarm-frequency }

Displays how often alarms have been triggered.

![Alarm Frequency](/Images/Dashboard/AlarmFrequency.png){align=center}

**Parameters**

* `Grupper` — Filter alarms by group name. Leave empty to show all alarms.

---

### Alarm Graph { #alarm-graph }

A larger alarm trend and distribution graph. Suited for dashboards where alarm analysis is a primary focus.

![Alarm Graph](/Images/Dashboard/AlarmGraph.png){align=center}

---

### History { #history }

Displays historical signal values as a trend graph. The legend shows current values with units and decimal precision.

![History](/Images/Dashboard/History.png){align=center}

The **From** and **To** fields at the top of the dashboard set the time range. How that range is applied depends on which button is used:

* **Apply** — applies the From/To range to all History widget instances on the dashboard.
* **Calendar icon** (on an individual widget) — applies the From/To range to that widget instance only, without affecting the others.
* **Reset** — sets all History widget instances back to the default 5-minute window.

**Parameters**

* `Signaler` — Signal path or array of signal paths to display.

---

### Key Value { #key-value }

Displays a single live value with its configured unit and decimal precision. Accepts any value in DataStore — internal variables, driver signals and System variables.

![Key Value](/Images/Dashboard/KeyValue.png){align=center}

**Parameters**

* `KeyValue` — Direct variable reference (not a string). Enter the variable path without quotes: `MB.AS01.LB01_P`, not `"MB.AS01.LB01_P"`.

---

### Signal Value Display { #signal-value-display }

Displays current live values for one or more signals. Automatically resolves units and decimal precision from DataStore.

![Signal Value Display](/Images/Dashboard/SignalValueDisplay.png){align=center}

**Parameters**

* `Signaler` — Signal path or array of signal paths to display.

---

### Pie Chart { #pie-chart }

Displays real-time signal distribution as a pie chart. Includes an expand button that opens a fullscreen view.

![Pie Chart](/Images/Dashboard/PieChart.png){align=center}

**Parameters**

* `Signaler` — Array of signal paths to display.

---

### Bar Chart { #bar-chart }

Displays signal value comparisons as a bar chart across configurable time periods. Suited for energy comparisons over time. Includes an expand button that opens a fullscreen view.

![Bar Chart](/Images/Dashboard/Widget.png){align=center}

**Parameters**

* `Signaler` — Array of signal paths to display.
* `Typ` — Aggregation mode. Determines how each period's bar value is calculated. Defaults to `Add`.
* `TimePeriod` — The time unit for each bar: `"Day"`, `"Week"`, `"Month"` or `"Year"`. Defaults to `"Month"`.
* `TimeSpan` — Number of periods to display. Defaults to `12`.

| `Typ` | Description |
|---|---|
| `Add` | Sums all logged values within each period. Use for instantaneous signals such as power, where the sum represents total energy consumed. |
| `Average` | Calculates the average of all logged values within each period. Use for continuous signals such as temperature. |
| `Trend` | Shows the difference between the last value in the current period and the last value in the previous period. Use for signals where the change from one period to the next is what matters. |
| `Result` | Shows the last logged value within each period. Use for signals where the end-of-period state is what matters. |

---

### Maintenance { #maintenance }

Displays maintenance task status — active, planned and missed tasks. Connects directly to the maintenance module. No signal input required.

![Maintenance](/Images/Dashboard/Maintenance.png){align=center}

## Next Steps { #next-steps }

* [Extending](extending.md) — custom widgets, design patterns and troubleshooting
<!-- --8<-- [end:body] -->
