---
title: Speed Dial
description: Add a floating action menu to a workview with icon options that run project functions.
product: mod
page_type: howto
status: draft
last_reviewed: 2026-09-04
scripts:
  - scLogBook
  - scAlert
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Speed Dial

The Speed Dial is a floating action button placed in a workview. It sits collapsed as a single button and expands into a set of icon options when clicked, so a view can offer several actions without giving up permanent screen space to a toolbar.

At rest it shows a single **+** button.

![Speed Dial collapsed](/docs/Images/SpeedDial/speeddial-collapsed.png){align=center}

Clicking it expands the options and rotates the button to a **×**, which collapses it again.

![Speed Dial expanded, showing the five standard options](/docs/Images/SpeedDial/speeddial-expanded.png){align=center}

Each option is an icon paired with a function. Because the function is written in the view itself, the same component can drive very different actions from one view to the next: toggling a display setting, opening a popup scoped to the current view, or running any other project script.

The objects live in `Speed Dial.klib`. A Speed Dial holds a maximum of seven options.

???+ info "Requirements"
    The Speed Dial itself has no script dependencies. The standard options described in
    [The five standard options](#the-five-standard-options) rely on:

    * `scObjectFinder` — populates the `ObjectList` table that scopes both the alarm and the history option
    * `scAlarmFinder` — populates the `AlarmObjects` table that the alarm option joins against
    * `scLogBook` — for the logbook option
    * `scAlert` — for error logging in the logbook option
    * The `dynTouchVisible` and `showNamplates` variables in Data Store
    * The `VySpecifikAlarm.kvie` and `VySpecifikHistorik.kvie` views

## Adding a Speed Dial to a view { #adding-a-speed-dial-to-a-view }

Drag one of the Speed Dial objects from `Speed Dial.klib` into the workview and position it where the button should sit. Nothing else is configured through properties. The options are defined in a script on the instance, described in [Configuring the options](#configuring-the-options).

### Choosing a variant { #choosing-a-variant }

The library provides several variants. They differ only in which direction the options expand and whether each option carries a caption.

| Object | Options expand | Captions |
|---|---|---|
| `SpeedDial` | Vertically, above the button | No |
| `SpeedDialBottom` | Vertically, above the button, slots in reverse order | No |
| `SpeedDialVerticalRight` | Horizontally, beside the button | No |
| `SpeedDialVerticalLeft` | Horizontally, beside the button, slots in reverse order | No |
| `SpeedDialCaption` | Vertically | Below each icon |
| `SpeedDialCaptionBottom` | Vertically, slots in reverse order | Below each icon |
| `SpeedDialCaptionsRight` | Vertically | To the right of each icon |
| `SpeedDialCaptionsRightBottom` | Vertically, slots in reverse order | To the right of each icon |

Use a plain variant where the button sits along the top or bottom of a view, and a `Vertical` variant where it sits along a side.

## Configuring the options { #configuring-the-options }

A Speed Dial is configured entirely from the instance's **Load** event. Two arrays are assigned there:

* `ImageArray` — the image path for each option, in order.
* `Functions` — the function to run when that option is clicked, in the same order.

The object's own Load handler reads both arrays and wires them to the option slots, which are named `Op0` through `Op6`:

```javascript title="Speed Dial.klib — SpeedDial onLoad()"
for (var img = 0; img < 7; img++) {
    if (img < this.ImageArray.length) {
        this.SpeedDialOptions["Op" + img].imgPath = this.ImageArray[img]
        this.SpeedDialOptions["Op" + img].onClick = this.Functions[img]
    } else {
        this.SpeedDialOptions["Op" + img].visible = false
    }
}
```

Slots beyond the length of `ImageArray` are hidden, so a Speed Dial with three options shows three icons and nothing else. There is no way to add an eighth option without extending the library object.

!!! warning "Both arrays are required, and must be the same length"
    The loop is driven by the length of `ImageArray` and indexes `Functions` with the same counter. An entry present in `ImageArray` but missing from `Functions` produces an option whose `onClick` is `undefined`, so the icon appears but does nothing.

    
### Adding captions { #adding-captions }

The caption variants take a third array, `Captions`, holding the label for each option in the same order:

```javascript title="Workview — SpeedDialCaption onLoad()"
this.ImageArray = new Array("Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/logs-white.svg");

this.Captions = new Array("Alarms",
                          "Logbook");

this.Functions = new Array(function () { /* ... */ },
                           function () { /* ... */ });
```

The caption variants run the same loop as the plain ones with one extra assignment, setting `Op{n}.Caption.Caption` from the array. Pass caption text through `Language.translate` if the project is translated.

### Image paths { #image-paths }

An image path is given relative to the project root, and the file must exist in the project's resources. The icons used by the standard options live in `Images/Material_Icons/`.

Icons are drawn on the Speed Dial's own background, so a white icon variant is normally the right choice. The library ships light icon files for this reason, for example `Alarm_white.svg` and `logs-white.svg`.

## The five standard options { #the-five-standard-options }

Five options recur across process views in the project. Together they form the standard Speed Dial: two display toggles and three view-scoped popups. The system views in the demo project use exactly this set on a `SpeedDialVerticalLeft`, and it is the set shown expanded above.

They are listed here in array order. On a `SpeedDialVerticalLeft` that puts the first entry closest to the button and the last one furthest from it, so the icons read right to left on screen.

| # | Icon | Action |
|---|---|---|
| 1 | `dynTouch-white.svg` | Toggle DynTouch fields |
| 2 | `Alarm_white.svg` | View-specific alarms |
| 3 | `chart-line-variant.svg` | View-specific history |
| 4 | `showNamePlate.svg` | Toggle nameplates |
| 5 | `logs-white.svg` | View-scoped logbook |

### 1. Toggle DynTouch fields { #toggle-dyntouch-fields }

```javascript
function () { dynTouchVisible = !dynTouchVisible }
```

Flips the `dynTouchVisible` variable in Data Store. When it is `true` the clickable DynTouch fields over process objects are always visible. The variable is persisted, so the choice survives a restart.

This gives an operator a way to see which objects in a view are clickable without hovering over each one.

### 2. View-specific alarms { #view-specific-alarms }

```javascript
function () {
    this.view.link("Common_Popup/VySpecifikAlarm/VySpecifikAlarm.kvie", true, { linkName: this.view.name })
}
```

Opens the alarm list filtered to the current view. The view's own name is passed as `linkName`, which is what scopes the list, so the same function works unchanged in every view it is pasted into.

The filtering is done in the database rather than by the popup. `linkName` is matched against the `View` column of `ObjectList`, and the objects found there are joined to `AlarmObjects` to arrive at the alarms belonging to the view:

```sql
SELECT ao.AlarmName FROM AlarmObjects ao
JOIN ObjectList ol ON ao.DeviceKey = ol.Object
WHERE ol.View = '<linkName>'
```

!!! note "This option depends on both finder scripts"
    `ObjectList` is built by `scObjectFinder` and `AlarmObjects` by `scAlarmFinder`. Both must have run for the alarm option to return anything. If either table is empty, or the view has not been indexed, the popup opens with no alarms rather than reporting an error.

### 3. View-specific history { #view-specific-history }

```javascript
function () {
    app.popOut.newData = { linkName: this.view.name };
    app.popOutVisible = true;
    app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie")
}
```

Opens history for the signals belonging to the current view. Unlike the alarm option this uses the pop-out mechanism rather than a link: the data is set first, the pop-out is made visible, and the view is loaded into it.

Scoping works the same way as for alarms, from a single lookup:

```sql
Select `Object` from ObjectList Where View = '<linkName>'
```

!!! note "This option depends on `scObjectFinder`"
    Only `ObjectList` is consulted here, so the history option needs `scObjectFinder` but not `scAlarmFinder`. A view missing from `ObjectList` opens an empty history rather than an error.

### 4. Toggle nameplates { #toggle-nameplates }

```javascript
function () { showNamplates = !showNamplates; }
```

Flips the `showNamplates` variable in Data Store, which controls whether nameplates are drawn on process objects. It defaults to on and is persisted.

Turning nameplates off is useful on dense views where the labels obscure the process picture.

!!! note "The variable name is spelled `showNamplates`"
    The variable is spelled without the second `e`. It is the name defined in Data Store, so it has to be written that way in scripts.

### 5. View-scoped logbook { #view-scoped-logbook }

```javascript
function () {
    try {
        app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
        app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
        app.popOutVisible = true;
    } catch (e) { scAlert.toFile("SpeedDial logbook: " + e.message); }
}
```

Opens the logbook filtered to the current view's topic, and new entries created from it are assigned that topic automatically. The topic is taken from the view's own path through `scLogBook.normalizeTopic()`, so entries written from a Speed Dial group under the view they came from. See [Logbook — Configuring](../modules/logbook/configuring.md#topics) for how topics are structured.

This is the one standard option that guards itself. The logbook depends on a database connection and on `scLogBook` being loaded, so a failure is written to the alert log through `scAlert.toFile()` instead of interrupting the operator. See [Logbook — Configuring](../modules/logbook/configuring.md#view-scoped) for how view-scoped logbooks behave.

### The complete example { #the-complete-example }

The five options as they appear in a system view in the demo project:

```javascript title="System view — SpeedDialVerticalLeft onLoad()"
try {

this.ImageArray = new Array("Images/Material_Icons/dynTouch-white.svg",
                            "Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/chart-line-variant.svg",
                            "Images/Material_Icons/showNamePlate.svg",
                            "Images/Material_Icons/logs-white.svg");

this.Functions = new Array(function () { dynTouchVisible = !dynTouchVisible },
                           function () {
    this.view.link("Common_Popup/VySpecifikAlarm/VySpecifikAlarm.kvie", true, { linkName: this.view.name })
},
                           function () {
    app.popOut.newData = { linkName: this.view.name };
    app.popOutVisible = true;
    app.popOut.setView("Pop_Outs/VySpecifikHistorik.kvie")
},
                           function () { showNamplates = !showNamplates; },
                           function () {
    try {
        app.logbookSelectedTopic = scLogBook.normalizeTopic(this.view.name);
        app.popOut.setView("Pop_Outs/LogBookControls/GetLogBookEntryByTopic.kvie");
        app.popOutVisible = true;
    } catch (e) { scAlert.toFile("SpeedDial logbook: " + e.message); }
})

} catch (e) { alert(e.message) }
```

Every function refers to the view through `this.view` rather than naming a view, so the block can be copied into a new process view without editing. Adding the standard Speed Dial to a view is a matter of placing the object and pasting this script into its Load event.

## Adding a custom option { #adding-a-custom-option }

A custom option is added by extending both arrays with a matching pair. To add a documents option to the standard set:

```javascript title="Workview — SpeedDial onLoad() — after"
this.ImageArray = new Array("Images/Material_Icons/dynTouch-white.svg",
                            "Images/Material_Icons/Alarm_white.svg",
                            "Images/Material_Icons/chart-line-variant.svg",
                            "Images/Material_Icons/showNamePlate.svg",
                            "Images/Material_Icons/logs-white.svg",
                            "Images/Material_Icons/file-document-edit-outline-white.svg");

this.Functions = new Array(function () { dynTouchVisible = !dynTouchVisible },
                           /* ... the four standard functions ... */
                           function () {
    app.popOut.setView("Common_Popup/Documents.kvie");
    app.popOutVisible = true;
});
```

Keep the two arrays aligned. An entry added to one and not the other is the most common configuration mistake, and it fails quietly rather than raising an error.

!!! tip "Scripts run in the object's context"
    Inside these functions `this` is the option object, so the current view is reached through `this.view`. A function that needs the Speed Dial itself can use `this.parent`.
<!-- --8<-- [end:body] -->
