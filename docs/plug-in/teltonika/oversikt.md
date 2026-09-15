# Send SMS with Teltonika – Overview

!!! info "License requirement"
    Using the plugin requires an Advance license with the .NET plugin option or a Premium license.

!!! warning "Linux" 
    The Teltonika pluging only works for Windows OS 
    
Using a .NET plugin, WideQuick can send SMS messages directly from the system, without intermediate services or external SMS gateways. The plugin communicates with a Teltonika router via its built-in REST API and sends SMS through the mobile network the router is connected to.

## Why send SMS from WideQuick?

Email and alarm clients work well as long as someone is actively monitoring them, but an SMS reaches a phone directly even when no one is sitting in front of an HMI or logged in to the system. That makes SMS particularly valuable for SCADA and HMI applications, where a fast response to a process upset can prevent downtime, damage, or a compliance breach, for example:

- **A critical process alarm becomes active** – operators, maintenance staff, or on-call engineers get an immediate notification of a high/low level, pressure, temperature, or other critical process alarm, wherever they are.
- **An unmanned or remote site needs attention outside office hours** – an SMS is sent immediately if a critical alarm occurs during evenings, nights, or weekends, when no operator is watching the HMI.
- **Escalation of unresolved alarms** – if an alarm remains active longer than expected, a follow-up SMS can be sent to a secondary contact or on-call engineer.
- **Equipment or communication issues** – SMS for things like a pump or motor fault, lost communication with a PLC or RTU, full storage, or other technical deviations that require prompt attention.

Since SMS is sent via the router's own mobile subscription, the solution is also independent of the site's internet connection, making it robust against network outages where email-based notifications would otherwise fail to arrive – particularly valuable for remote pumping stations, treatment plants, and other unmanned installations.

## Which Teltonika routers are supported?

The plugin works with Teltonika routers running RutOS that expose the Web API / REST API. Using the API requires the following minimum firmware version:

| Router family | Minimum firmware version |
|--------------|-------------------------|
| RUT2, RUT9, RUTM, RUTC, TRB, and other families | 7.15 or later |
| RUTX family | 7.12 or later |

The SMS-sending functionality is part of **Mobile Utilities**, a built-in RutOS feature included on all of Teltonika's mobile routers (the RUT, RUTX, and TRB series) – it is not a separate package that needs to be installed via Package Manager, but a standard feature as long as the firmware requirement above is met.
