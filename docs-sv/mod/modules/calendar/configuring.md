---
title: Kalender — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Kalender — Konfigurering

## Händelser { #events }

Anpassade kalenderhändelser skapas, redigeras och tas bort direkt i kalendern. De lagras i underhållsdatabasen tillsammans med underhållsdata.

När du skapar eller redigerar en händelse kan du välja en färg från en fast uppsättning alternativ: **ENERGY**, **POWER**, **SYSTEM**, **SAFETY**, **SECURITY**, **HVAC**, **WATER**, **DEFAULT**. Dessa färger definieras i temat **CalendarColors** i `Themes.kdat`.

**Redigera en händelse:**

Klicka på en befintlig händelse för att öppna popup-fönstret **Lägg till/redigera kalenderhändelse**. Alla fält kan uppdateras. Klicka på **Spara** för att tillämpa ändringarna.

**Ta bort en händelse:**

Öppna händelsen och klicka på **Ta bort**. Detta tar bort händelsen permanent.

![Popup-fönstret Lägg till/redigera kalenderhändelse](/docs/sv/Images/Calendar/edit-event-popup.png){align=center}

## Underhållshändelser { #maintenance-events }

Underhållsdeadlines från [underhållsmodulen](../maintenance/index.md) visas automatiskt i kalendern. De är skrivskyddade och kan inte redigeras eller tas bort från kalendern. Ändringar måste göras i **Underhåll - Lista**.

Varje underhållshändelse visas på dagen för sin deadline. Färgen ställs in automatiskt baserat på uppgiftens aktuella status — den kan inte väljas manuellt. Dessa färger definieras i temat **MaintenanceColors** i `Themes.kdat` och är separata från de färger som används för anpassade kalenderhändelser.

Om du klickar på en underhållshändelse öppnas ett popup-fönster som visar objekt, status, deadline och underhållstyp. Klicka på **Öppna redigering** för att navigera direkt till den uppgiften i **Underhåll - Lista**.

| Status | Färg |
|---|---|
| Planerad | Gul |
| Missad | Mörkröd |
| Stoppad | Grå |
| Påminnelse | Dämpad olivgrön |

![Underhållshändelser med olika statusfärger i månadsvy](/docs/sv/Images/Calendar/maintenance-event-colors.png){align=center}

## Påminnelser { #reminders }

En påminnelsehändelse kan visas i kalendern ett angivet antal dagar före en underhållsdeadline. Påminnelsen visas som en separat post med färgen **Påminnelse**, skild från själva deadlinehändelsen.

Påminnelser är aktiverade som standard för uppgifter som skapas utan en mall. Uppgifter som skapas från en mall använder mallens påminnelseinställning, som är avstängd som standard. Standard påminnelseförskjutningen är 3 dagar. Se [Utöka](extending.md#reminder-configuration) för hur du ändrar dessa inställningar.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — konfiguration av påminnelseförskjutning
<!-- --8<-- [end:body] -->
