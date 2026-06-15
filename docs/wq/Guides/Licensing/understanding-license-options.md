---
title: Understanding WideQuick License Options
description: Guide to WideQuick license types, levels, and optional features to help you choose the right license for your application.
product: wq
page_type: concept
tags:
 - WQ
---
# Understanding WideQuick License Options

## Introduction

Picking the right license for your WideQuick application is vital to ensuring the right features are available in your HMI/SCADA solution. This guide explains the license types, license levels, system size, and the optional features you can include when choosing a WideQuick license.

---

## License Types

Kentima offers two main license types: **WideQuick General License** and **WideQuick Universal License**. Both provide flexibility and reliability, enabling you to choose based on infrastructure, connectivity, and lifecycle requirements.

### WideQuick General License

The WideQuick General License is tied to the specific Runtime System on which WideQuick runs. It is a proven model suitable for fixed environments, from local HMIs to complex SCADA systems in secured networks.

Variants include:

- **Version-specific licenses** – locked to a specific main version.  
- **Licenses with five years of free version upgrades** – recommended when periodic upgrades are planned.

This license type is well suited for non-connected or highly secured systems, such as installations behind a DMZ or fully air‑gapped networks.

### WideQuick Universal License

The WideQuick Universal License is a subscription-based, cloud-managed licensing model designed for modern and dynamic environments.

Key characteristics:

- Run multiple WideQuick Runtime applications on the same host, including container-based deployments.  
- Dynamically adjust license level, optional features, and external variables on a monthly basis.  
- Access to the latest WideQuick version and security updates throughout the subscription period.

This license type is ideal for organizations with diverse infrastructures, high scalability requirements, and a need for flexible license strategy.

---

## Selecting the right license


### License Levels

Each WideQuick license, regardless of license type, is associated with a **license level** that defines the functional scope available to the application. 

From WideQuick 14.0 and onward, the runtime offers three main levels (for example: Extended, Advanced, and Premium).  

The levels include different features and allows for a different range of external variables


| License Level | Description |
|:---|:---|
| **Extended** | Basic HMI functionality for simple visualization and control |
| **Advanced** | Enhanced SCADA features including advanced drivers and database connectivity |
| **Premium** | Full enterprise features including all drivers, advanced HMI, database, and user management |

### System Size (External Variables)

After choosing a license level, select the **system size** by specifying the maximum number of **external tags/variables**. External variables are those coming from communication drivers such as MODBUS, MQTT, OPC UA, or BACnet.  

The number of **internal variables** (for example alarms and internal tags created directly in WideQuick) scales with the chosen number of external variables, typically at least double and within the ranges defined in the license table.

---

## Selecting Optional Features

| Feature | Included in License Level | Description |
|:---|:---|:---|
|<span style = "font-size:16px"> **WideQuick Connections**</span> |||
| Able to connect to other WideQuick Runtime | Advanced | Enables a WideQuick application to connect to other WideQuick applications. Useful when multiple applications form a larger, distributed system. |
| Remote Client/Runtime Connections | Advanced | Defines how many concurrent Remote Client or Runtime‑to‑Runtime connections are allowed. **Important:** This feature limits the number of concurrent connections. |
| Web Client Connections | Advanced | Defines how many concurrent web client connections are allowed. **Important:** This feature limits the number of concurrent connections. |
| OPC DA Server Connections | Premium | Maximum number of clients that can connect to a WideQuick OPC DA Server. |
| OPC UA Server Connections | Premium | Maximum number of clients that can connect to a WideQuick OPC UA Server. |
|<span style = "font-size:16px"> **Communication Drivers**</span> |||
| Modbus Serial and TCP Driver | Extended | Allows WideQuick to communicate with devices over Modbus (serial and TCP) via the DataStore. |
| OPC DA Driver | Advanced | Allows WideQuick to communicate with devices over OPC DA via the DataStore. |
| OPC UA Driver | Advanced | Allows WideQuick to communicate with devices over OPC UA via the DataStore. |
| MQTT Driver | Advanced | Allows WideQuick to communicate with devices over MQTT via the DataStore. |
| BACnet Driver | Premium | Allows WideQuick to communicate with devices over BACnet via the DataStore. |
| BACnet+ Driver | Premium | Allows WideQuick to communicate with devices over BACnet via the DataStore and enables an extended script interface for deeper integration. |
|<span style = "font-size:16px">**HMI/SCADA Features**</span> |||
| Number of Workviews | Extended | Maximum number of Workviews that can be used in the application. |
| Themes | Extended | Enables the application to define and switch between color schemes. |
| Language and Unit Conversions | Advanced | Enables translation between defined languages and automatic unit conversions. |
| Embedded Maps | Advanced | Enables use of map objects inside the application. |
| Window Manager | Extended | Enables a window manager to handle application windows (minimize, maximize, resize, move). |
| Pan and Zoom | Extended | Enables panning and zooming in Workviews. |
| Treeview | Advanced | Enables use of a treeview object to display structured data. |
| Reports | Premium | Enables creation of reports based on Excel templates, populated with logged and current data from the application. |
| <span style = "font-size:16px">**Database Features**</span> |||
| Number of Database Connections | Advanced | Maximum number of configured database connections in the application. |
| Access to Custom Queries | Premium | Enables creation and execution of custom database queries. |
| <span style = "font-size:16px">**Ethiris/PSIM Features**</span> |||
| Parallel Ethiris Server Connections | Premium | Allows the application to connect to multiple Ethiris servers in parallel. |
| Ethiris Extended Functionality | Premium | Enables extended Ethiris functions such as playback of recorded material, Pan‑To‑Zoom, and cluster connections. |
| <span style = "font-size:16px">**Other Features**</span> |||
| Project File Encryption | Advanced | Allows encrypted project files to be executed in the application. |
| Remote Procedure Calls (RPC) | Premium | Allows WideQuick to communicate with other WideQuick systems using RPC. |
| TCP Listener | Advanced | Allows WideQuick to open TCP sockets for reading and writing data. |
| Microsoft Windows Service | Extended | Allows WideQuick to run as a Windows service. |
| Microsoft .NET Plug‑in Support | Premium | Enables the use of .NET plug‑ins in the application. |
| WideQuick C API | Premium | Enables the application to use custom plug‑ins and drivers developed with the C API. |
| <span style = "font-size:16px">**User Features**</span> |||
| Number of Users and Privileges | Advanced | Maximum number of defined users and privilege sets that can log in and control access. |
| Microsoft Active Directory | Premium | Enables WideQuick to use Microsoft Active Directory for domain logins and privilege management. |

