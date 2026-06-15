---
title: WideQuick Deployment Options
description: Overview of WideQuick deployment options across embedded panels, Windows, Linux, and containerized environments.
product: wq
page_type: concept
tags:
 - WQ
---
# WideQuick Deployment Options

WideQuick can run on a broad spectrum of hardware and environments, from compact embedded devices to distributed cloud clusters. 

Deployment flexibility stems from its cross-platform runtime supporting Windows, GNU/Linux, and containerization, enabling scalability from single-operator panels to multi-node systems with centralized data processing.


## Embedded HMI Panels

Deployments use Kentima's H-series operator panels integrate WideQuick Runtime directly into fanless industrial hardware.

- **H300–H500**: Compact wall-mount panels for building automation and light industrial tasks, with 10.1"–15.6" displays and basic CPU options.
- **H600–H800**: Larger, robust panels up to 21.5" for harsher environments, featuring galvanic isolation, stainless steel enclosures, and advanced monitoring.

All models include WideQuick Control Center for local management, OPC UA server, SQL database, and Driver connectivity (ModBus, OPC, MQTT and BACnet), ideal for standalone or edge HMI.

## Panel PCs and Box PCs

For custom or higher-performance needs, WideQuick installs on Kentima's H-series Panel PCs and headless Box PCs.

- Fanless designs with expandable I/O, supporting larger screens or DIN-rail mounting.
- Runs full WideQuick Runtime with optional Kepware OPC servers for protocol bridging.

Suitable for mid-tier SCADA where dedicated processing power exceeds the more basic H-panels.

## Virtualized and Server Deployments

WideQuick scales to virtual machines or physical servers for centralized HMI/SCADA.

- **VMs/Hypervisors**: Deploy on VMware, Hyper-V, or Proxmox with multiple virtual WideQuick instances sharing hardware.
- **Windows/Linux Servers**: Rack-mounted or on-premise servers handling large projects, alarms, trends, and historian functions for dozens of clients.

Projects transfer seamlessly between embedded and server runtimes.

## Containerized Deployments

Leveraging Docker/Podman, WideQuick Runtime containerizes for portable, orchestrated setups.

- Single-container mode for edge devices or development.
- Multi-container stacks with databases (MariaDB), MQTT brokers, and Grafana dashboards, deployable via Docker Compose.

Aligns with your containerization expertise at Kentima for reproducible industrial stacks.

## Cloud and Cluster Deployments

Largest scale involves Kubernetes clusters or cloud platforms for high-availability SCADA.

- **Cloud Providers**: AWS, Azure, or GCP VMs running containerized WideQuick, with auto-scaling for global operator access.
- **Hybrid Clusters**: On-premise K8s (e.g., using minikube or full Kubernetes) federating edge H-panels with cloud historian and analytics.
- Supports redundancy, load balancing, and integration with cloud IoT services like AWS IoT Core or Azure IoT Hub for massive sensor fleets.

Enables "large cluster of applications" where multiple WideQuick nodes process data from thousands of field devices.

## Deployment Comparison

| Scale | Platforms | Key Use Cases | Management Tools |
|-------|-----------|---------------|------------------|
| Small (Embedded) | H300–H800 panels | Local HMI, edge control | Panel Control Center  |
| Medium (Servers) | Panel/Box PCs, VMs | Site-wide SCADA | RDP/SSH, WideQuick Designer |
| Large (Cloud/Cluster) | Docker/K8s, AWS/Azure | Enterprise, distributed monitoring | Kubernetes Dashboard, Prometheus/Grafana  |

Select based on project size, redundancy needs, and integration requirements. WideQuick's unified Designer ensures consistent development across all targets.
