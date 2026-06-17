---
title: Audit Trail - Configuring
description: Configure which DataStore variables are tracked by the Audit Trail.
product: mod
page_type: howto
doc_id: DOC-M19
status: draft
last_reviewed: 2026-06-08
tags: 
 - MOD
---
<!-- --8<-- [start:body] -->

# Audit Trail - Configuring

## Configuring Variables to Track { #configuring-variables-to-track }

Navigate to **History → Logs → Audit trail → Audit Trail - Settings**.

![Audit Trail - Settings view](/Images/Audit_Trail/audit-trail-settings.png){align=center}

The view has two panels. The left panel shows all available DataStore variables. The right panel shows the variables currently being tracked.

To start tracking a variable, select it in the left panel and click the **>** button. To stop tracking a variable, select it in the right panel and click the **<** button. Variables can also be added/removed by double-clicking.

Variables can be added at any level of the DataStore tree. Selecting a parent node and clicking **>** adds all variables under that node at once.

!!! warning
    Avoid tracking variables that change continuously, such as measured values and sensor readings. This will generate a very large number of log entries and make the log difficult to use. The Audit Trail is intended for variables that change infrequently and deliberately, such as setpoints, control signals, and configuration values.
<!-- --8<-- [end:body] -->
