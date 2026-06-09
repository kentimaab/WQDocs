---
title: Architecture Overview Modular Framework
description: The foundation of Modular Framework as a platform for HMI and SCADA Applications
product: mod
status: draft
last_reviewed: 2026-05-19
---

<!-- --8<-- [start:body] -->

# Architecture Overview Modular Framework

Every HMI and SCADA project asks the same questions:

- how do you handle alarms?
- How does navigation work? Where does history live?
- How do operators log actions?

The answers rarely change, but most integrators rebuild them from scratch, project after project.

**WideQuick Modular Framework** is Kentima's answer to that problem.

Since the early 2000s Kentima has built the motor behind powerful HMI and SCADA systems across industries: building management, water and wastewater treatment, process and batch. In Modular Framework, Kentima extracted what is universal and made it reusable.
The result is a structured project foundation that ships with production-ready modules for the features every system needs, while staying fully open for system integrators to configure, extend, and tailor to any customer requirement.

The framework does not constrain what you build. It eliminates the work you should never have had to do twice.

The architecture that makes this possible is straightforward and worth understanding before you build your first project.

## A modular architecture

The Modular Framework is built on a single idea: every feature is an independent module that you include only if you need it. The core application provides the runtime, navigation, user management, and data layer. Everything else is optional and additive.

The diagram below shows how the full stack fits together: from the WideQuick HMI/SCADA platform at the base, through the Modular Framework and its module library, up to the concept applications built on top.

<div class="arch-wrap" style="margin: 1.5rem 0;">

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--concepts">
      <span>Concepts &amp; Applications</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Concepts</span></div>
        <div class="arch-indent arch-indent--lg"></div>
        <a href="../bms/" class="arch-concept arch-concept--bms">
          <small>WideQuick</small>
          <strong>BMS</strong>
          <span>Building Management System</span>
        </a>
        <a href="../wwt/" class="arch-concept arch-concept--wwt">
          <small>WideQuick</small>
          <strong>WWT</strong>
          <span>Water &amp; Wastewater Treatment</span>
        </a>
      </div>
    </div>
  </div>

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--framework">
      <span>Framework &amp; Solutions</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Framework</span></div>
        <div class="arch-indent arch-indent--sm"></div>
        <a href="./" class="arch-concept arch-concept--mod">
          <small>WideQuick</small>
          <strong>MOD</strong>
          <span>Modular Framework</span>
        </a>
      </div>
      <div class="arch-row">
        <div class="arch-sublabel-col"><span>Modules</span></div>
        <div class="arch-indent arch-indent--sm"></div>
        <div class="arch-content arch-content--solutions">
          <div class="arch-mini-chips">
            <span>Alarms</span><span>Maintenance</span><span>Alarm Sending</span><span>Navigation</span><span>Popups</span><span>Reports</span><span>Dashboards</span><span>History</span><span>Calendar</span><span>Maps</span><span>Documents</span><span>Logbook</span><span>Graphical Symbols</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="arch-tier">
    <div class="arch-tier__label arch-tier__label--software">
      <strong>WideQuick</strong>
      <span>HMI / SCADA</span>
    </div>
    <div class="arch-tier__rows">
      <div class="arch-row">
        <div class="arch-sublabel-col arch-sublabel-col--light"><span>Core</span></div>
        <div class="arch-content arch-content--core">
          <div class="arch-mini-chips">
            <span>Workviews</span><span>Graphical Objects</span><span>Interactive Objects</span><span>Dynamics</span><span>Alarms</span><span>History</span><span>Events</span><span>Users</span><span>Themes</span><span>Language</span><span>Data Store</span>
          </div>
        </div>
      </div>
      <div class="arch-row">
        <div class="arch-sublabel-col arch-sublabel-col--light"><span>Communication</span></div>
        <div class="arch-content arch-content--comms">
          <div class="arch-mini-chips">
            <span>OPC UA</span><span>OPC DA</span><span>Modbus</span><span>BACnet</span><span>MQTT</span><span>Database connectors</span><span>C API</span><span>.NET Plugin</span>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>

Start at the bottom. **WideQuick HMI/SCADA** is the platform layer: the runtime, graphical engine, communication protocols, and core capabilities like alarms, history, and user management. This is what every WideQuick project runs on.

One layer up sits the **Modular Framework**. It adds a structured project model on top of WideQuick and a library of pre-built modules: alarms, maintenance, dashboards, history, navigation, and more. Integrators pick what the project needs and leave out the rest.

At the top are the **concept applications**, BMS and WWT. These are not separate products. They are pre-configured implementations of the Modular Framework, built for a specific industry, with an opinionated module selection and project structure already in place.

**The top tier is optional.** Many projects run directly on MOD without ever touching BMS or WWT. If your industry, customer, or project scope does not fit a concept application, build straight on MOD and assemble exactly the modules you need.

**You only ship what the project needs.** A simple process overview carries none of the weight of reporting engines, maintenance schedulers, or alarm-sender configuration. A complex multi-site installation can pull in every available module without any structural changes to the project.

**Scope is a deliberate choice.** Not an accident of what happened to be included in a starting template.

## Many industries, one framework

The same framework runs across fundamentally different application domains. Building management systems track HVAC, access control, and energy. Water and wastewater installations monitor treatment processes, pump stations, and alarms. Batch and process industry applications manage recipes, production logging, and operator workflows.

What these have in common is that they are all built from the same WideQuick Modular Framework foundation, with the same Designer toolchain, the same module library, and the same deployment model. The domain-specific logic lives in configuration and module selection, not in a different product.

This matters for integrators who work across industries: the knowledge, tooling, and project structure transfer directly from one vertical to the next.

## Concept applications

Building Management System (BMS) and Water & Wastewater Treatment (WWT) are concept applications: complete, pre-structured implementations of the Modular Framework targeted at specific industries. They ship with an opinionated module selection, navigation structure, and system views that reflect the typical requirements of that domain.

They are starting points, not constraints. An integrator can adopt a concept application as-is, extend it with additional modules, or use it as a reference when building a custom project from the base framework.

Many successful deployments never use a concept application at all. Batch production, food and beverage, and general process industry projects routinely run directly on WideQuick Modular Framework with a custom module selection that fits the project exactly.

## Keep what you like, discard anything else

Every module in the framework is independent. There are no hidden dependencies between, for example, the Calendar module and the Alarm module. Each can be included or excluded without affecting the others.

For a system integrator this means the delivered application can be scoped precisely to what the end customer needs. A smaller installation might run with Alarms, History, and a Dashboard. A larger one adds Maintenance scheduling, Reports, and Maps. Neither project requires workarounds or stub implementations for the features that were left out.

The practical workflow is to start from the template application, include the modules that are relevant, and remove the rest. What remains is a clean, purposeful application with no dead views or unused configuration.

## Template vs Demo Application

Two starting points are available for download.

**Demo Application**

The demo is designed to be running within minutes of download. It ships with a set of simulated signal tags, pre-configured alarms, and a bundled SQLite database for history, **no external infrastructure required**. Open it in WideQuick, start the runtime, and the application is immediately interactive with live-looking data.

Use the demo to evaluate the framework, explore module behaviour, or walk a customer through what a finished application looks like.

**Template Application**

The template is the production starting point. The simulated tags, demo alarms, and example system views have been removed. The history database connection is configured for MariaDB rather than SQLite, reflecting a real production deployment.
What remains is the structural skeleton of a Modular Framework project:

- navigation
- user management
- module placeholders

**ready to be built on.**

Use the template when starting a real project. It avoids the cleanup step of removing demo content and starts the integrator from a known, production-appropriate baseline.

<!-- --8<-- [end:body] -->
