---
title: Alarms - Configuring
description: Create alarm groups, define alarms, and set up notification schedules.
product: mod
page_type: howto
doc_id: DOC-M9
status: draft
last_reviewed: 2026-05-29
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Alarms - Configuring

## Creating alarm groups { #creating-alarm-groups }

Alarms are organised into groups in **WideQuick Designer®**. Each group defines shared defaults — colors, icons, and measures — that its alarms inherit unless overridden individually.

1. In the project tree, right-click **Alarms** under **Data Store** and select **Add Group...**.
2. Enter a **Name** for the group.
3. Set the **Monitor variable** — a boolean variable that will be `true` whenever any alarm in the group is active.
4. Optionally configure default **Colors** for each alarm state, default **Icons**, and a default **Measure** for the group.
5. Click **OK**.

![Add alarm group dialog](/docs/Images/Create_Alarm/AddAlarm.png){align=center}

## Adding alarms { #adding-alarms }

Once a group exists, open it (double-click or right-click → **Open**) and click **Add** to create a new alarm.

![New alarm dialog](/docs/Images/Create_Alarm/NewAlarm.png){align=center}

| Field | Description |
|---|---|
| **Name** | Unique name for the alarm within the group |
| **Alarm class** | Label used to rank or categorise alarms — for example `1`, `A`, or `High` |
| **Ack rule** | When the alarm can be acknowledged — see below |
| **Text** | Short label shown in the alarm list, e.g. *Motor overheating* |
| **Details** | Longer description shown when the alarm is expanded in the log |
| **Activation** | Trigger condition and optional delay before the alarm fires |
| **Block type** | Whether the alarm can be suppressed: **None**, **Manually** (by operator), or **Automatic** (by a variable) |
| **Block variable** | Variable used when **Block type** is **Automatic** — alarm is suppressed while this variable is true |
| **Colors** | Per-alarm color overrides. If left blank, the group defaults are used |
| **Activation monitor** | Boolean variable set to `true` while the alarm is active |
| **Acknowledge monitor** | Boolean variable set to `true` while the alarm is acknowledged |
| **Measure** | Action available in the alarm list — used to add a GoTo link. See [GoTo in Alarm Groups](../Navigation/extending.md#goto-in-alarm-groups) |
| **Description** | Internal note about the alarm. Not shown at runtime |

### Activation { #activation }

Double-click the **Activation** field to configure the trigger. Set the variable the alarm monitors and optionally add a delay — the alarm will only fire if the condition has been true for the full delay period.

![Activation settings](/docs/Images/Create_Alarm/Activation.png){align=center}

### Acknowledgement rules { #acknowledgement-rules }

* **Normal** — can be acknowledged at any time.
* **Strict** — can only be acknowledged after the alarm has gone inactive.
* **Auto** — acknowledged automatically when the alarm goes inactive. Can also be acknowledged manually while still active.

### Measure { #measure }

The **Measure** field on an alarm enables an action column in the alarm list. Configuring a GoTo measure lets operators navigate directly to the object that triggered the alarm by pressing the measure in the list. See [GoTo in Alarm Groups](../Navigation/extending.md#goto-in-alarm-groups) for setup instructions.

![Measure settings](/docs/Images/Create_Alarm/Measure.png){align=center}

## Alarm notification schedules { #alarm-notification-schedules }

The **Alarm - Schedule** view controls when and to whom alarm notifications are sent by email or SMS. It shows a bar chart of emails and SMS messages sent and failed over the last month, a list of all configured schedules, and a status panel with schedule counts, current alarm counts, and SMTP status.

!!! note "Requirements"
    Notification schedules require `scAlarmSender` to be running and a configured email or SMS channel. See [Extending](extending.md).

![Alarm - Schedule view](/docs/Images/Alarms/alarm-schedule-view.png){align=center}

### Creating a schedule { #creating-a-schedule }

Click **New schedule** to open the creation wizard. It steps through three pages.

**Step 1 — When**

![New schedule step 1](/docs/Images/Alarms/alarm-schedule-step-1.png){align=center}

* **Name** — name for the schedule.
* **System** — which system this schedule applies to: the local system or a connected
remote system.
* **Active schedule** — toggle to enable or disable the schedule without deleting it.
* **Weekdays** — select which days of the week the schedule is active. Only the
selected days will appear in the **Time interval** section below.
* **Time interval** — configure the active time windows for each selected day. Each
day shows a primary **From/To** time slot. Click the **+** button to add a secondary
time slot for that day, allowing two separate notification windows on the same day.
Setting both **From** and **To** to `00:00` disables notifications for that time
slot. To receive notifications for the entire day, set **From** to `00:00` and
**To** to `23:59`.

!!! note
    Setting **To** to `23:59` covers the full day including the final minute.
**Step 2 — What**

![New schedule step 2](/docs/Images/Alarms/alarm-schedule-step-2.png){align=center}

* **Severity level** — which alarm classes trigger this schedule. Leave empty to include all classes.
* **Alarm groups** — which alarm groups are monitored. Use **Select all** to include all groups.

**Step 3 — Who**

![New schedule step 3](/docs/Images/Alarms/alarm-schedule-step-3.png){align=center}

* **Subject line** — subject used for outgoing email notifications.
* **Recipient** — add individual email addresses or phone numbers directly.
* **Alias** — select from configured aliases to add a group of recipients at once.
* **Collect alarm dispatches** — delay in seconds before sending. Alarms that trigger within this window are collected and sent together in a single notification.

### Editing and deleting schedules { #editing-and-deleting-schedules }

Select a schedule in the list and click **Edit schedule** to modify it. Active and inactive status can be toggled from within the edit dialog.

Click **Delete schedule** to remove the selected schedule.

## Next Steps { #next-steps }

* [Extending](extending.md) — configuring email and SMS for alarm notifications
<!-- --8<-- [end:body] -->
