---
title: Fjärrsystem
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Fjärrsystem
???+ info "Krav"
    Följande skript krävs för att använda Fjärrsystem och all
    relaterad funktionalitet som täcks av guiderna för Fjärrsystem:
    
    * `scRemoteAlarms`
    * `scRemoteSystems`
    * `scAlarm`
    * `scPrototypes`
    * `scAlert`

Fjärrsystem låter en WideQuick-applikation ansluta till en eller flera andra WideQuick Runtime-instanser. När anslutning är upprättad visas varje fjärrsystem i navigationsmenyn och kan öppnas direkt. Larm från alla anslutna system aggregeras i den lokala larmlistan, vilket ger operatörer en samlad vy över hela installationen.


## Ta emot anslutningar { #receiving-connections }

För att en WideQuick-applikation ska kunna acceptera inkommande anslutningar från andra applikationer måste en anslutningsport konfigureras i projektinställningarna. I **WideQuick Designer®**, öppna **Project Properties** (genom att högerklicka på toppnoden i projektträdet) och ange **View access** under **Connection Port**. Standardporten är **2122**.

![Connection Port i Project Properties](/Images/Remote_System/remote-connection-port.png){align=center}

Båda applikationerna måste vara nåbara via nätverket på den konfigurerade porten.

## Konfigurera ett fjärrsystem { #configuring-a-remote-system }

Ett fjärrsystem kan läggas till under utveckling i **WideQuick Designer®** eller vid körning i **WideQuick Runtime®**.

### Via WideQuick Designer® { #via-widequick-designer }

Fjärrsystem hanteras under noden **Remote Systems** i projektträdet. Högerklicka på noden och välj **Add Remote Systems...**. Fyll i följande fält:

* **Name** — visningsnamn för fjärrsystemet. Visas i menyn för Fjärrsystem.
* **Description** — valfri beskrivning. Visas under namnet i menyn för Fjärrsystem.
* **Host/IP** — IP-adress till fjärrsystemet.
* **Port** — måste matcha den anslutningsport som konfigurerats på fjärrsystemet. Standard är **2122**.
* **Refreshrate** — hur ofta variabeluppdateringar hämtas från detta system, i millisekunder. Lägre värden ger snabbare respons men ökar nätverksbelastningen.
* **Auto connect on startup** — när aktiverat ansluter applikationen automatiskt till detta system vid uppstart.

![Dialogrutan Add Remote System](/Images/Remote_System/remote-designer-add.png){align=center}

### Via WideQuick Runtime® { #via-widequick-runtime }

Navigera till **Inställningar → Inställningar** i huvudmenyn och klicka på **Manage remote systems**.

Dialogrutan för Fjärrsystem visar alla konfigurerade system. Klicka på **Add** för att lägga till ett nytt, **Edit** för att ändra ett befintligt eller **Remove** för att ta bort det.

![Dialogrutan Remote Systems](/Images/Remote_System/remote-runtime-list.png){align=center}

Avsnittet **Defaults** längst upp anger globala standardvärden för alla system:

* **Refreshrate** — standarduppdateringsfrekvens som används när ett nytt system läggs till.
* **Max reconnect attempts** — hur många gånger som återanslutning ska försökas efter en förlorad anslutning. **-1** innebär att försök görs i det oändliga.
* **Reconnect delay** — sekunder mellan återanslutningsförsök.

Om du klickar på **Add** öppnas samma fält som i **WideQuick Designer®**.

![Dialogrutan för att lägga till fjärrsystem](/Images/Remote_System/remote-runtime-add.png){align=center}

## Navigation { #navigation }

Konfigurerade fjärrsystem visas i avsnittet **Remote Systems** längst ned i huvudnavigeringen. Klicka på **Remote Systems** för att öppna listan.

![Menyn Remote Systems med anslutna och frånkopplade system](/Images/Remote_System/remote-menu.png){align=center}

Varje post visar systemnamn, beskrivning och en ikon för anslutningsstatus. Statusikonen uppdateras i realtid — grön betyder ansluten, röd betyder inte ansluten. Om **Auto connect on startup** är aktiverat återansluter applikationen automatiskt vid frånkoppling enligt inställningarna för **Max reconnect attempts** och **Reconnect delay**.

Att öppna ett fjärrsystem startar det i ett separat klientfönster. Den lokala applikationen förblir fullt tillgänglig medan fjärrsystemet är öppet.

## Öppna ett fjärrsystem { #accessing-a-remote-system }

Varje system i menyn för Fjärrsystem kan öppnas på två sätt:

* **Klicka på systemnamnet** — öppnar fjärrapplikationen i **WideQuick Remote®**, en nativ klient med full vyåtkomst och interaktiva kontroller.
* **Klicka på globikonen** — öppnar fjärrapplikationen i webbklienten, ett webbläsarbaserat gränssnitt som inte kräver någon separat installation.

**WideQuick Remote®** är det rekommenderade alternativet för operatörsanvändning. Webbklienten lämpar sig för situationer där det inte är praktiskt att installera Remote®-klienten — till exempel vid åtkomst från en privat enhet eller ett externt nätverk.

## Fjärrlarm { #remote-alarms }

När `scRemoteAlarms` körs visas larm från alla anslutna fjärrsystem i den lokala larmlistan tillsammans med lokala larm. Varje larmpost visar vilket system larmet härstammar från. Larmlistan kan filtreras per system för att fokusera på en specifik fjärrinstallation. Att kvittera ett larm skickar kvitteringen direkt till det ursprungliga systemet — ingen separat inloggning krävs.

Om ett fjärrsystem kopplas från tas dess larm automatiskt bort från listan och återkommer när anslutningen är återupprättad.

### Integrera en icke-MOD-applikation { #integrating-a-non-mod-application }

Larmaggregering fungerar med vilken WideQuick-applikation som helst — inte bara MOD — så länge fjärrapplikationen exponerar följande variabler i sin Datalager:

* `activeAckAlarms` — aktuellt antal aktiva kvitterade larm.
* `activeNoAckAlarms` — aktuellt antal aktiva okvitterade larm.
* `alarmNames` — en kommaseparerad lista med larmgruppsnamn. Varje namn i listan måste också finnas som ett `AlarmGroup`-objekt i Datalager.

Det är dessa variabler som `scAlarm` underhåller i MOD. En icke-MOD-applikation som håller dessa uppdaterade kommer automatiskt att kännas igen av `scRemoteAlarms` när fjärrsystemanslutningen är upprättad.

<!-- --8<-- [end:body] -->
