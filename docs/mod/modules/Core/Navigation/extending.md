---
title: Navigation - Extending
description: Extend the Navigation module with scripts and hooks.
product: mod
page_type: howto
doc_id: DOC-M14
status: draft
last_reviewed: 2026-05-21
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Navigation - Extending

This section covers how to extend the Navigation module with custom functionality.
This includes creating shortcuts to specific objects using GoTo and adding custom
icons to the navigation menu.

Before getting started, make sure you are familiar with the basics of the Navigation
module. If not, see [Navigation — Get started](get-started.md).

## GoTo { #goto }
The GoTo function allows linking directly to a specific object, making it possible to
create shortcuts that bring the user to the view where that object is located. When
reached via GoTo, the object is highlighted, making it easy to find even in a complex
view. If the object exists in multiple views, a popup will appear showing all available
locations.

To use GoTo, apply the following script to a button's **onClick** action, replacing
`YOUR_OBJECT.NAME` with the name of the target object:

```javascript title="goTo() function in scLinking script"
scLinking.goTo("YOUR_OBJECT.NAME");
```

In the example below, the `goTo()` function is applied to a button's **onClick** action
with the target object `MB.AS01.LB02_GT43`:

![goTo](/docs/Images/Navigation/goTO.gif)

### GoTo in Alarm Groups { #goto-in-alarm-groups }
GoTo can also be integrated into **Alarm Group** and the **AlarmList**, allowing users to
immediately navigate to the object that triggered an alarm and take action.

To enable GoTo for alarms, follow these steps:

1. In **WideQuick Designer®**, open the **Alarm Group** properties and navigate to
**Measures**.
2. Click the circle next to **Script** to enable the script action and enter the
following:

```javascript title="goToAlarm() function in Alarm Group Measures"
goToAlarm(app.alarmView.Alarm1.nameForCurrentAlarm, app.alarmView.name)
```

3. Add a **Measure** state by clicking **Add** on the same page. Enter the desired
display text and select a colour.
4. In the **Alarm** object, navigate to **Alarm Columns** and enable
**Use Custom Alarm Columns**.
5. Select the **Measure** category — pressing this column for a specific alarm will
trigger GoTo and navigate to the **Workview** where that alarm originated.

![Alarm_Goto](/docs/Images/Navigation/Alarm_goTo.png)

!!! note 
    In order to use the Goto function on Alarms, the script `scAlarmFinder` is needed


## Custom navigation icons { #custom-navigation-icons }
This section covers how to implement custom navigation icons connected to specific
views. The implementation process consists of two steps:

1. Importing and setting up the SVG
2. Connecting the SVG to a **Workview** identifier

### Importing and configuring the SVG { #importing-and-configuring-the-svg }
First, import your SVG icon. It is recommended to have two versions — one for dark mode
and one for light mode. This ensures the icon remains visible regardless of the user's
theme preference. Name and place the files as follows:

* `YourSvg-gray.svg` — for the light theme
* `YourSvg-white.svg` — for the dark theme

Both files should be placed in `Images/Material_Icons/`.

If the application is intended to run through the web client, the SVG must have a
`width` and `height` definition. Without these, the icon will not render in the web
client. Verify this by opening the SVG in a text editor and confirming they are defined.
If not, add them to the XML structure:

```xml title="SVG width and height definition"
<svg
    width="24"
    height="24"
/>
```

With the SVG files placed in the correct folder and their dimensions verified, proceed
to the next step.

### Connecting the SVG { #connecting-the-svg }
To connect an SVG to a folder or **Workview**, add an additional `else if` block to the
`selectImage()` function in the `scSubNav` script, which can be found under
**Scripts → scSubNav** in the project tree. Locate the `selectImage()` function and add
the new `else if` block before the final `else` block, which handles the default icon
fallback. The example below shows how to match the identifier `solarcell` to a solar
panel icon:

```javascript title="selectImage() function in scSubNav script"
else if (type === 'solarcell' || type === 'solar' || type === 'solarpanel' || type === 'solar park') {
    return base + 'solar-power' + s;
}
```

Any **Workview** whose name contains `solarcell`, `solar`, `solarpanel`, or
`solar park` will be assigned the corresponding icon. The `scSubNav` script
automatically converts **Workview** names to lowercase before comparing, so
capitalisation is not an issue as long as the identifier words in the
`selectImage()` function are lowercase. The `base` variable holds the path to the
icon folder and `s` holds the theme suffix, which together form the full path to
the correct SVG file. If no identifier matches, the final `else` block assigns a
default icon.
