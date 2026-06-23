---
title: Time Channel
description: Overview of the Time Channel popup in WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-05-29
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Time Channel

The Time Channel popup allows users to configure time-based schedules for the selected
object. Each day of the week can have up to two active time periods defined by Turn on
and Turn off times. It only appears in the Tab menu when the object has a signal
matching the `_TK` suffix.

![Time Channel popup](/docs/Images/Popups/Time-channel.png)

## Channel status

The top right panel displays the current status of the time channel — whether it is
active or inactive — alongside a clock showing the current time.

## Weekdays

The **Weekdays** section displays a schedule for each day of the week. Each day
supports two independent active periods, each defined by a **Turn on** and
**Turn off** time in `hhmm` format. The **Run time** column shows the total active
time for that day. A **Total runtime** row at the bottom shows the combined runtime
across all weekdays.

## Special days

The **Special days** section allows different schedules to be defined for specific
dates. The following special day types are available:

* **Holiday Eve** — the day before a public holiday
* **Holiday** — public holidays
* **Special Day 1**, **Special Day 2**, **Special Day 3** — custom dates that can
be defined by entering a date in `MM-DD` format

Each special day supports the same two-period schedule as weekdays.

## Hand ctrl

The **Hand ctrl** panel allows the time channel to be overridden manually:

* **Auto** — the time channel follows the configured schedule
* **Hand** — the time channel is controlled manually, ignoring the schedule

The current output status of the time channel is also shown:

* **From** — the time channel output is currently off
* **Till** — the time channel output is currently on

## Save and fetch

The **Save** and **Fetch** buttons allow the current schedule configuration to be
saved to the database or retrieved from a previously saved configuration.

## Default suffix aliases

The Time Channel popup uses a large number of suffixes to map each time slot to a
specific signal. The key suffixes are:

| Suffix alias | Suffix | Description |
|---|---|---|
| `timechannelIsActive` | `_TK` | Indicates whether the time channel is active |
| `timechannelManualControl` | `_TK1_0` | Switches between Auto and Hand mode |
| `timechannelManualCommand` | `_TK4_5` | Sets the output state in Hand mode |

Each day and time slot is mapped to a dedicated suffix following the pattern
`_TK[register]_[index]`. All time slot suffixes are writable.