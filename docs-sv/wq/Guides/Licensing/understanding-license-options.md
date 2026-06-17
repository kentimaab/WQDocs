---
title: Förstå WideQuick-licensalternativ
product: wq
page_type: overview
status: draft
last_reviewed: 2026-06-16
tags:
 - WQ
---

# Förstå WideQuick-licensalternativ

## Introduktion

Att välja rätt licens för din WideQuick-applikation är avgörande för att säkerställa att rätt funktioner finns tillgängliga i din HMI/SCADA-lösning. Den här guiden förklarar licenstyper, licensnivåer, systemstorlek och de tillvalsfunktioner du kan inkludera när du väljer en WideQuick-licens.

---

## Licenstyper

Kentima erbjuder två huvudsakliga licenstyper: **WideQuick General License** och **WideQuick Universal License**. Båda ger flexibilitet och tillförlitlighet och gör det möjligt att välja utifrån infrastruktur, anslutningsbehov och livscykelkrav.

### WideQuick General License

WideQuick General License är knuten till det specifika Runtime System som WideQuick körs på. Det är en beprövad modell som lämpar sig för fasta miljöer, från lokala HMI:er till komplexa SCADA-system i säkrade nätverk.

Varianter inkluderar:

- **Versionsspecifika licenser** – låsta till en specifik huvudversion.  
- **Licenser med fem års kostnadsfria versionsuppgraderingar** – rekommenderas när periodiska uppgraderingar planeras.

Den här licenstypen passar väl för ej anslutna eller starkt säkrade system, exempelvis installationer bakom en DMZ eller helt luftgapade nätverk.

En fullständig funktionsöversikt per licensnivå och tillgängliga tillvalspaket finns i [WideQuick 14 License Overview](https://widequick.com/license/14/Licens%20WideQuick%2014%20-%20English.html){target="_blank"} på Kentimas webbplats.

### WideQuick Universal License

WideQuick Universal License är en prenumerationsbaserad, molnhanterad licensmodell utformad för moderna och dynamiska miljöer.

Viktiga egenskaper:

- Kör flera WideQuick Runtime-applikationer på samma värd, inklusive containerbaserade driftsättningar.  
- Justera licensnivå, tillvalsfunktioner och externa variabler dynamiskt på månadsbasis.  
- Tillgång till den senaste versionen av WideQuick och säkerhetsuppdateringar under hela prenumerationsperioden.

Den här licenstypen är idealisk för organisationer med varierad infrastruktur, höga skalbarhetskrav och behov av en flexibel licensstrategi.

---

## Välja rätt licens


### Licensnivåer

Varje WideQuick-licens, oavsett licenstyp, är kopplad till en **licensnivå** som definierar det funktionella omfång som är tillgängligt för applikationen.

Från och med WideQuick 14.0 erbjuder runtimemiljön tre huvudnivåer (exempelvis: Extended, Advanced och Premium).  

Nivåerna inkluderar olika funktioner och tillåter olika antal externa variabler.


| Licensnivå | Beskrivning |
|:---|:---|
| **Extended** | Grundläggande HMI-funktionalitet för enkel visualisering och styrning |
| **Advanced** | Utökade SCADA-funktioner inklusive avancerade drivrutiner och databasanslutning |
| **Premium** | Fullständiga enterprise-funktioner inklusive alla drivrutiner, avancerat HMI, databas och användarhantering |

### Systemstorlek (externa variabler)

När du valt en licensnivå väljer du **systemstorlek** genom att ange maximalt antal **externa taggar/variabler**. Externa variabler är sådana som kommer från kommunikationsdrivrutiner som MODBUS, MQTT, OPC UA eller BACnet.  

Antalet **interna variabler** (exempelvis larm och interna taggar skapade direkt i WideQuick) skalas med det valda antalet externa variabler, typiskt minst dubbelt så många och inom de intervall som definieras i licensöversikten.

---

## Välja tillvalsfunktioner

| Funktion | Ingår i licensnivå | Beskrivning |
|:---|:---|:---|
|<span style = "font-size:16px"> **WideQuick-anslutningar**</span> |||
| Möjlighet att ansluta till andra WideQuick Runtime | Advanced | Gör det möjligt för en WideQuick-applikation att ansluta till andra WideQuick-applikationer. Användbart när flera applikationer bildar ett större, distribuerat system. |
| Fjärrklient-/Runtime-anslutningar | Advanced | Definierar hur många samtidiga fjärrklient- eller Runtime-till-Runtime-anslutningar som tillåts. **Viktigt:** Den här funktionen begränsar antalet samtidiga anslutningar. |
| Webbklientanslutningar | Advanced | Definierar hur många samtidiga webbklientanslutningar som tillåts. **Viktigt:** Den här funktionen begränsar antalet samtidiga anslutningar. |
| OPC DA-serveranslutningar | Premium | Maximalt antal klienter som kan ansluta till en WideQuick OPC DA-server. |
| OPC UA-serveranslutningar | Premium | Maximalt antal klienter som kan ansluta till en WideQuick OPC UA-server. |
|<span style = "font-size:16px"> **Kommunikationsdrivrutiner**</span> |||
| Modbus seriell och TCP-drivrutin | Extended | Gör det möjligt för WideQuick att kommunicera med enheter via Modbus (seriellt och TCP) via DataStore. |
| OPC DA-drivrutin | Advanced | Gör det möjligt för WideQuick att kommunicera med enheter via OPC DA via DataStore. |
| OPC UA-drivrutin | Advanced | Gör det möjligt för WideQuick att kommunicera med enheter via OPC UA via DataStore. |
| MQTT-drivrutin | Advanced | Gör det möjligt för WideQuick att kommunicera med enheter via MQTT via DataStore. |
| BACnet-drivrutin | Premium | Gör det möjligt för WideQuick att kommunicera med enheter via BACnet via DataStore. |
| BACnet+-drivrutin | Premium | Gör det möjligt för WideQuick att kommunicera med enheter via BACnet via DataStore och möjliggör ett utökat skriptgränssnitt för djupare integrering. |
|<span style = "font-size:16px">**HMI/SCADA-funktioner**</span> |||
| Antal arbetsbilder | Extended | Maximalt antal arbetsbilder som kan användas i applikationen. |
| Teman | Extended | Gör det möjligt för applikationen att definiera och växla mellan färgscheman. |
| Språk- och enhetsomvandlingar | Advanced | Möjliggör översättning mellan definierade språk och automatisk enhetsomvandling. |
| Inbyggda kartor | Advanced | Möjliggör användning av kartobjekt inuti applikationen. |
| Fönsterhanterare | Extended | Möjliggör en fönsterhanterare för att hantera applikationsfönster (minimera, maximera, ändra storlek, flytta). |
| Panorering och zoomning | Extended | Möjliggör panorering och zoomning i arbetsbilder. |
| Trädvy | Advanced | Möjliggör användning av ett trädvyobjekt för att visa strukturerad data. |
| Rapporter | Premium | Möjliggör skapande av rapporter baserade på Excel-mallar, fyllda med loggad och aktuell data från applikationen. |
| <span style = "font-size:16px">**Databasfunktioner**</span> |||
| Antal databasanslutningar | Advanced | Maximalt antal konfigurerade databasanslutningar i applikationen. |
| Åtkomst till anpassade frågor | Premium | Möjliggör skapande och körning av anpassade databasfrågor. |
| <span style = "font-size:16px">**Ethiris/PSIM-funktioner**</span> |||
| Parallella Ethiris-serveranslutningar | Premium | Gör det möjligt för applikationen att ansluta till flera Ethiris-servrar parallellt. |
| Utökad Ethiris-funktionalitet | Premium | Möjliggör utökade Ethiris-funktioner såsom uppspelning av inspelat material, panorering-till-zoomning och klusteranslutningar. |
| <span style = "font-size:16px">**Övriga funktioner**</span> |||
| Kryptering av projektfiler | Advanced | Tillåter att krypterade projektfiler körs i applikationen. |
| Fjärrproceduranrop (RPC) | Premium | Tillåter WideQuick att kommunicera med andra WideQuick-system via RPC. |
| TCP-lyssnare | Advanced | Tillåter WideQuick att öppna TCP-socketar för läsning och skrivning av data. |
| Microsoft Windows-tjänst | Extended | Tillåter WideQuick att köras som en Windows-tjänst. |
| Microsoft .NET-pluginstöd | Premium | Möjliggör användning av .NET-plugin-program i applikationen. |
| WideQuick C API | Premium | Gör det möjligt för applikationen att använda anpassade plugin-program och drivrutiner utvecklade med C API. |
| <span style = "font-size:16px">**Användarfunktioner**</span> |||
| Antal användare och behörigheter | Advanced | Maximalt antal definierade användare och behörighetsuppsättningar som kan logga in och styra åtkomst. |
| Microsoft Active Directory | Premium | Gör det möjligt för WideQuick att använda Microsoft Active Directory för domäninloggningar och behörighetshantering. |
