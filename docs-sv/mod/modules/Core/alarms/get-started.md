---
title: Larm — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Larm — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Larm och all
    relaterad funktionalitet som beskrivs i larmguiderna:
    
    * `scAlarm`
    * `scPrototypes`
    * `scAlert`

Larmmodulen tillhandahåller realtidsövervakning av larm i hela WideQuick MOD-installationen. Larm definieras i **WideQuick® Designer** och övervakas vid körning via en uppsättning dedikerade vyer som är tillgängliga från huvudnavigeringen.
## Larmvyer { #alarm-views }

Larmvyerna nås från avsnittet **Larm** i huvudnavigeringen.

### Larm - Lista { #alarm-list }

**Larm - Lista** är den primära vyn för att övervaka aktiva larm. Varje rad visar larmklass, larmtext, aktiveringstid, larmnamn och vilket system larmet härstammar från. Om ett **Mätvärde** är konfigurerat på larmet visas en länk i den sista kolumnen — till exempel en **Gå till larm**-länk som navigerar direkt till objektet i processvyn.

Om `scRemoteAlarms` körs och fjärrsystem är anslutna visas även larm från dessa system i listan tillsammans med lokala larm.

![Alarm - List view](/docs/sv/Images/Alarms/alarm-list.png){align=center}

### Larm - Översikt { #alarm-overview }

**Larm - Översikt** ger en bredare bild av larmaktiviteten. Ett stapeldiagram visar antalet larm per dag under de senaste sju dagarna, uppdelat efter larmklass. Ett cirkeldiagram visar fördelningen av larmklasser bland aktuellt aktiva larm, med en topp-fem-lista över de vanligaste larmen. En statistikpanel till höger visar aktuellt antal aktiva larm samt historiska totaler för de senaste 30 dagarna, hittills i år och föregående år.

![Alarm - Overview](/docs/sv/Images/Alarms/alarm-overview.png){align=center}

Cirkeldiagrammet kan konfigureras genom att klicka på **kugghjulsikonen**. Välj vilka larmgrupper som ska inkluderas, ange antalet dagar som ska visas, välj om grupperingen ska ske efter larmklass eller grupp, och växla enheten mellan procent och antal.

![Alarm - Overview graph settings](/docs/sv/Images/Alarms/alarm-overview-settings.png){align=center}

### Larm - Logg { #alarm-log }

**Larm - Logg** är ett historiskt register över alla larmhändelser och visar larmklass, larmtext, tid, larmnamn, detaljer och fjärrsystem. Aktiva larm markeras i rött.

![Alarm - Log](/docs/sv/Images/Alarms/alarm-log.png){align=center}

Larmhistorik kan också exporteras som en rapport. Se [Rapporter](../../reports/configuring.md#alarm-report).

### Larm - Frekvens { #alarms-frequency }

**Larm - Frekvens** listar alla larm rangordnade efter hur ofta de har utlösts under en vald tidsperiod. Varje rad visar den totala aktiva tiden och frekvensantalet tillsammans med larmnamn, larmtext och larmklass. Detta hjälper till att identifiera beständiga eller ofta återkommande larm som kan behöva åtgärdas.

![Alarms - Frequency](/docs/sv/Images/Alarms/alarm-frequency.png){align=center}

## Kvittera larm { #acknowledging-alarms }

Larm kvitteras från **Larm - Lista**. Välj ett larm och klicka på **Kvittera**, eller använd kvitteringsåtgärden direkt på raden.

Varje larm har en kvitteringsregel som styr när det kan kvitteras:

* **Normal** — kan kvitteras när som helst, oavsett om larmet är aktivt eller inaktivt.
* **Strikt** — kan bara kvitteras efter att larmet har blivit inaktivt.
* **Auto** — kvitteras automatiskt när larmet blir inaktivt. Kan också kvitteras manuellt medan det fortfarande är aktivt.

För larm från fjärrsystem skickas kvitteringen till det ursprungliga systemet — ingen separat inloggning på det systemet krävs.

## Processvyns larmlista { #process-view-alarm-list }

En dedikerad larmlista kan öppnas från en specifik processvy och visar bara de larm som är relevanta för den vyn. Den öppnas som ett separat fönster ovanpå processvyn, vilket ger operatörerna en fokuserad larmöversikt för den utrustning som visas på skärmen utan att behöva navigera bort.

## Dashboardwidgetar { #dashboard-widgets }

Larmdata kan också visas på en dashboard med larmwidgetar — Larmstatus, Larmrad, Larmlista, Larmlogg, Larmfrekvens och Larmgraf. Detta är användbart för att bygga anpassade översiktsskärmar som kombinerar larminformation med live-värden, historik eller underhållsstatus. Se [Dashboards — Konfigurering](../../dashboards/configuring.md#widgets-all-available-widgets-and-their-parameters).

## Objektanimationer { #object-animations }

Objekt med aktiva larm kan konfigureras att visa visuell återkoppling — till exempel blinkande rött när ett larm utlöses. Detta hanteras av animationssystemet och beskrivs i [arbetsvy Animations](/mod/guides/arbetsvy-animations/).

## Nästa steg { #next-steps }

* [Konfigurering](configuring.md) — skapa larmgrupper, definiera larm och konfigurera notifieringsscheman
* [Utöka](extending.md) — konfigurera e-post och SMS för larmnotifieringar
<!-- --8<-- [end:body] -->
