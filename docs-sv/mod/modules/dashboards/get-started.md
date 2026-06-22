---
title: Dashboards — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Dashboards — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda dashboards och all
    relaterad funktionalitet som täcks i guiderna för dashboards:
    
    * `scDashboard`
    * `scAlarm`
    * `scHistory`
    * `scPrototypes`
    * `scThemes`
    * `scAlert`
    * `scQuickSort`
    
    Samt följande objektbibliotek:
    
    * `Dashboard Widgets`

WideQuick MOD levereras med tre exempeldashboards som kan användas som startpunkt eller anpassas för att passa ett projekt.
Nya dashboards kan skapas antingen från mallen eller från grunden beroende på vad användaren vill.
<figure markdown="span">
    ![Dashboard](/Images/Dashboard/Dashboard.png)  <figcaption>Energidashboarden i WideQuick Runtime</figcaption>
</figure>

## Konfigurera en ny dashboard { #setting-up-a-new-dashboard }

Duplicera dashboardmallen i **WideQuick Designer®** genom att högerklicka på mallen i projektträdet och flytta den till rätt mapp i projektstrukturen.

![Setting up a dashboard](/Images/Dashboard/SetupDashboard.gif){align=center}
## Widgets — färdiga komponenter för dashboarden { #widgets-pre-built-components-for-the-dashboard }

dashboards byggs med färdiga widgets från biblioteket `Dashboard Widgets`.
Varje widget är utformad för en specifik typ av data och kan placeras och
konfigureras direkt utan någon egen utveckling. De flesta widgets finns även i olika storlekar.

![Widget](/Images/Dashboard/Widget.png){align=center}

## Rutnätslayout — placera widgets i redigeraren { #grid-layout-positioning-widgets-in-the-editor }

dashboarderna i **WideQuick Designer®** använder ett 4×4-rutnät som hjälp vid widgetplacering. Varje rutnätsposition markeras med en ellips som fungerar som placeringsguide. Dessa ellipser
visas inte vid körning.

![Grid](/Images/Dashboard/Grid.png){align=center}

## Lägga till en widget { #adding-a-widget }

Lägg till en widget genom att dra den från biblioteket `Dashboard Widgets` till dashboarden och fyll sedan i relevanta parametrar i egenskapspanelen. En fullständig lista över tillgängliga widgets och deras parametrar finns i [Konfigurera](configuring.md).

![Adding a widget](/Images/Dashboard/UseWidget.gif){align=center}

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — widgetreferens och parameterdetaljer
* [Utöka](extending.md) — egna widgets, designmönster och felsökning
<!-- --8<-- [end:body] -->
