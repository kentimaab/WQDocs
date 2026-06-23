---
title: MultiView
description: How to link Workviews in WideQuick MOD using MultiView to trigger navigation between views based on object actions.
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# MultiView

In WideQuick Modular Framework it is possible to have objects which contains linking to other Workviews. This makes it possible to have the system change to another Workview based on a certain action. This guide will go through how to set this up.  Firstly go to a Workview where this will be implemented, and select the object. From here press the tab ++"Action"++, which will bring up the following. 

![Action menu](../../docs/Images/MultiView/Action_menu.png)

In this window, next to event the user can decide what action will change the Workview. In this example "Click" will be used. Next change from "No action" to "Script" and click the text icon to the right. This will open up the script window

![Script menu](../../docs/Images/MultiView/Script_window.png)

In this window the user can create their script for what action will happen when the event happens. The script for switching to another Workview is shown below.

``` 
app.MultiViewer.setView("/Path/to/workView/myworkview.kvie")
```
The path in the parentheses is set to the Workview that is being switched to. In order to illustrate how this should be set, a image of a project tree is provided below with the script with correct path after

![Project Tree](../../docs/Images/MultiView/Project_tree.png)

```
app.MultiViewer.setView("/System/Test/Link.kvie")
```