---
title: Distributionsalternativ för WideQuick
product: wq
page_type: overview
status: draft
last_reviewed: 2026-06-16
tags:
 - WQ
---

# Distributionsalternativ för WideQuick

WideQuick kan köras på ett brett spektrum av hårdvara och miljöer, från kompakta inbyggda enheter till distribuerade kluster i molnet.

Distributionsflexibiliteten bygger på en plattformsoberoende körningsmiljö som stöder Windows, GNU/Linux och containerisering, vilket möjliggör skalbarhet från enpanelssystem för enskilda operatörer till flernodsystem med centraliserad databehandling.


## Inbyggda HMI-paneler

Distributioner använder Kentimas H-serie operatörspaneler som integrerar WideQuick Runtime direkt i fläktfri industrihårdvara.

- **H300–H500**: Kompakta väggmonterade paneler för byggnadsautomation och lätt industri, med 10,1"–15,6" skärmar och grundläggande CPU-alternativ.
- **H600–H800**: Större, robusta paneler upp till 21,5" för tuffare miljöer, med galvanisk isolation, höljen i rostfritt stål och avancerad övervakning.

Alla modeller inkluderar WideQuick Control Center för lokal hantering, OPC UA-server, SQL-databas och drivrutinsanslutning (ModBus, OPC, MQTT och BACnet), idealiskt för fristående eller edge-HMI.

## Panel-PC och Box-PC

För anpassade eller högpresterande behov installeras WideQuick på Kentimas H-serie Panel-PC och headless Box-PC.

- Fläktfria konstruktioner med utbyggbart I/O, stöd för större skärmar eller DIN-skenmontage.
- Kör full WideQuick Runtime med valfria Kepware OPC-servrar för protokollbryggor.

Lämpliga för mellannivå-SCADA där dedikerad processorkraft överstiger de mer grundläggande H-panelerna.

## Virtualiserade och serverdistributioner

WideQuick skalar till virtuella maskiner eller fysiska servrar för centraliserad HMI/SCADA.

- **Virtuella maskiner/Hypervisorer**: Distribuera på VMware, Hyper-V eller Proxmox med flera virtuella WideQuick-instanser som delar hårdvara.
- **Windows/Linux-servrar**: Rackmonterade eller lokala servrar som hanterar stora projekt, larm, trender och historikerfunktioner för dussintals klienter.

Projekt överförs sömlöst mellan inbyggda körningsmiljöer och serverkörningsmiljöer.

## Containeriserade distributioner

Med Docker/Podman containeriseras WideQuick Runtime för portabla och orkestrerade konfigurationer.

- Enkelbehållarläge för edge-enheter eller utveckling.
- Flerbehållarstackar med databaser (MariaDB), MQTT-mäklare och Grafana-instrumentpaneler, driftsättningsbara via Docker Compose.

Stämmer överens med din containeriseringskompetens på Kentima för reproducerbara industriella stackar.

## Moln- och klusterdistributioner

Den största skalan involverar Kubernetes-kluster eller molnplattformar för SCADA med hög tillgänglighet.

- **Molnleverantörer**: AWS, Azure eller GCP-virtuella maskiner som kör containeriserat WideQuick, med autoskalning för global operatörsåtkomst.
- **Hybridkluster**: Lokala K8s (t.ex. med minikube eller fullständigt Kubernetes) som federerar edge-H-paneler med molnhistorik och analys.
- Stöder redundans, lastbalansering och integration med molnbaserade IoT-tjänster som AWS IoT Core eller Azure IoT Hub för massiva sensornätverk.

Möjliggör "stora applikationskluster" där flera WideQuick-noder bearbetar data från tusentals fältenheter.

## Distributionsjämförelse

| Skala | Plattformar | Viktiga användningsområden | Hanteringsverktyg |
|-------|-------------|---------------------------|-------------------|
| Liten (inbyggd) | H300–H800-paneler | Lokalt HMI, edge-styrning | Panel Control Center |
| Medel (servrar) | Panel-/Box-PC, virtuella maskiner | Platsövergripande SCADA | RDP/SSH, WideQuick Designer |
| Stor (moln/kluster) | Docker/K8s, AWS/Azure | Företag, distribuerad övervakning | Kubernetes Dashboard, Prometheus/Grafana |

Välj baserat på projektets storlek, redundansbehov och integrationskrav. WideQuick:s enhetliga Designer säkerställer konsekvent utveckling för alla målmiljöer.
