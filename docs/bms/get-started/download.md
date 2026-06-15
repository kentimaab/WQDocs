---
title: Download WideQuick BMS
description: Download WideQuick BMS
product: bms
page_type: getstarted
status: draft
last_reviewed: 2026-06-02
tags: 
 - BMS
---

# Download WideQuick BMS

WideQuick BMS is available free of charge to Kentima partners. If you are not yet a partner, visit [kentima.com](https://www.kentima.com){target="_blank"} to learn more and get in touch.

The download includes everything needed to get started: 
- a complete template project with all scripts
- object libraries
- system logic pre-configured
- a fully implemented demo project for reference. 

The project can be opened and explored freely in WideQuick Designer, but commissioning a live system requires a **WideQuick Advanced** license or higher. 

If you are in need of a WideQuick License please get in contact with the Kentima [sales team](https://www.kentima.com/en-GB/Kontakt)

## Template vs Demo application

WideQuick BMS 2026.1.0 is available in two versions for download on the Kentima website:

!!! note "Requirements"
    **WideQuick version 14.0** or later must be installed before downloading and opening the project files. See [Installing WideQuick](/wq/get-started/Installing-WideQuick) for more information.

[**Download WideQuick BMS 2026.1.0**](https://www.kentima.com/en-GB/Download/HMI-SCADA%20CONCEPTS/Fastighetsautomation/Download%20application){target="_blank"}

### Template project
The template project is a fresh, ready-to-implement project containing the full
functionality of WideQuick BMS 2026.1.0. All scripts, object libraries, and system
logic are pre-configured and in place — the integrator simply starts building their
system views. There are no implemented systems or external connections such as
**OPC UA** or **Modbus**. It is the recommended starting point for integrators who
want to build a new project from scratch.

![Template project](/Images/BMS_Intro/Template.png)

### Demo project
The demo project is a fully implemented example showing all functionality of
WideQuick BMS 2026.1.0 in use. It is useful both for understanding how the system
works and for drawing inspiration for implementation.

The demo project contains three implemented systems:

* **Heating** — views `VS11`, `VV10`, `VS10`, and `VS20`
* **Air Handling** — views `LB01`, `LB02`, and `LB03`
* **Cabinet** — views `AS01` and `AS02`

![Demo project](/Images/BMS_Intro/Demo.png)

!!! note
    The Air Handling system also includes copies of the views using legacy icons,
    which can be used as a reference for projects that have not yet migrated to the
    current icon set.

### Start the application

Once downloaded, extract the zip file to your desired folder. The extracted folder
contains:

* A project folder — containing all project files
* `WideQuick_Mod.kpro` — double-click this file to launch the project in WideQuick Designer.
* To run the preview press ++f5++ on your keyboard.
