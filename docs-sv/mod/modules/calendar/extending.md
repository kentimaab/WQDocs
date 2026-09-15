---
title: Kalender — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Kalender — Utöka

## Påminnelsekonfiguration { #reminder-configuration }

Det finns för närvarande inget gränssnitt för påminnelseinställningar. Båda kan ställas in via ett skript.

### Globalt förskjutningsvärde { #global-offset }

Antalet dagar före en deadline som en påminnelsehändelse visas. Standard är 3 dagar. Använd `scMaintenance.setReminderOffset` och ange värdet i millisekunder:

```javascript
var days = 5;
scMaintenance.setReminderOffset(days * 24 * 60 * 60 * 1000);
```

### Aktivering per mall { #per-template-toggle }

Styr om påminnelser genereras för uppgifter som skapas från en specifik mall. Standard är av. Det finns ingen hjälpfunktion för detta. Uppdatera tabellen `maintenanceLog_templates` direkt och anropa `updateTemplates()` för att uppdatera minnescachen så att kalendern fångar upp ändringen omedelbart:

```javascript
var templateType = "Filterbyte";
var current = scMaintenance.getAllTemplatesMap()[templateType];
var newVal = (current && current.reminder_enabled === 1) ? 0 : 1;
DatabaseConnections["maintenance"].exec(
    "UPDATE maintenanceLog_templates SET reminder_enabled = " + newVal + " WHERE type = '" + templateType + "'"
);
scMaintenance.updateTemplates();
```

Uppgifter som skapas utan en mall genererar alltid påminnelser oavsett denna inställning.

## Helgdagsvariabler { #holiday-variables }

Skriptet `scHoliday` klassificerar den aktuella dagen och publicerar resultatet till två booleska variabler i Datalagret.

| Variabel | Sätts när |
|---|---|
| `isHoliday` | En kalenderhändelse med färgen **HOLIDAY** täcker dagens datum. |
| `isHolidayEve` | En kalenderhändelse med färgen **HOLIDAYEVE** täcker dagens datum. |

En helgdagshändelse lagras med `Holiday` i kolumnen `object` i `CalendarEvents`, och en helgdagsafton med `HolidayEve`. Den markeringen är vad klassificeringen matchar mot, och den sätts av färgen som valts på händelsen.

Testet är ett överlappningstest snarare än ett test på startdatum, så en flerdagshelg sätter flaggan varje dag den täcker i stället för enbart den första.

`refreshHolidayStateVariables()` skriver båda. Den körs vid uppstart och vid varje pollning.

!!! warning "Flaggan slår om vid pollningen, inte vid midnatt"
    Båda variablerna uppdateras av den timvisa pollningen, som räknar från applikationens start snarare än från midnatt. Dagbytet landar därför upp till en timme in på den nya dagen.

    Ett schema som måste agera exakt vid midnatt bör inte enbart läsa flaggan som utlösare. Där tidpunkten är avgörande anropas `refreshHolidayStateVariables()` från ett eget schema i projektet vid den tidpunkt som krävs.

!!! note "Endast på servern"
    Pollningen är skyddad med `if (System.remote) return`, så den körs på servern i stället för på varje ansluten klient. Variablerna är läsbara överallt.

## Lagring av prenumerationer { #subscription-storage }

Importerade kalendrar lagras i tabellen `ics_subscriptions` i underhållsdatabasen. Tabellen skapas vid första användning, och kolumner som tillkommit i senare versioner läggs till vid start, så ett befintligt projekt uppgraderar sig självt.

| Kolumn | Syfte |
|---|---|
| `id` | Primärnyckel. Varje importerad händelse märks med den, så en import kan byta färg och tas bort separat. |
| `name` | Visningsnamn som visas i **Ändra kalendrar** och **Kalenderfilter**. |
| `url` | Filsökvägen kalendern importerades från. |
| `etag`, `lastModified` | Cachade svarsvalidatorer. Används inte i den här versionen. |
| `isBuiltin` | Markerade en auktoritativ helgdagskälla. Ingen import sätter den i den här versionen. |
| `type` | `file` för en importerad `.ics`-fil. |
| `visibleInCalendar` | Om importen ritas i kalendern. Ställs in från **Kalenderfilter**. |
| `color`, `colorOverridden` | En färg vald i **Ändra kalendrar**. `colorOverridden` är den avgörande uppgiften. När den är `0` är `color` inaktuell och standardfärgen för typen gäller fortfarande. |

!!! info "Rader av en utgången typ"
    En databas som förts över från en version som innehöll REST-insticksmodulen kan fortfarande innehålla rader av typerna `url` och `nager`. En synkronisering hoppar över dem och skriver en notering till loggen i stället för att misslyckas. Deras händelser ligger kvar i kalendern tills prenumerationen tas bort i **Ändra kalendrar**.

## Skriptreferens { #script-reference }

| Funktion | Syfte |
|---|---|
| `importFileSubscription(path)` | Lägger till en import för en lokal `.ics`-sökväg och läser den omedelbart. Namnet sätts som standard till filnamnet utan filändelse. |
| `addSubscription(name, url, isBuiltin, type)` | Lägger till en prenumerationsrad. Returnerar `duplicate_name` eller `duplicate_url` om en redan matchar. |
| `listSubscriptions()` | Returnerar samtliga prenumerationer. |
| `getSubscription(id)` | Returnerar en prenumeration. |
| `syncSubscription(id)` | Läser om en import. |
| `syncAllSubscriptions()` | Läser om samtliga importer. |
| `renameSubscription(id, newName)` | Byter namn på en import. |
| `setSubscriptionColor(id, color)` | Åsidosätter färgen på en imports händelser. |
| `setSubscriptionVisibility(id, visible)` | Anger om importen ritas i kalendern. |
| `countSubscriptionEvents(id)` | Returnerar hur många händelser en import för närvarande bidrar med. |
| `removeSubscription(id)` | Tar bort en import och dess händelser. |
| `holidayExists(startMs)` | Sann när en helgdagshändelse täcker angiven dag. |
| `holidayEveExists(startMs)` | Sann när en helgdagsaftonshändelse täcker angiven dag. |
| `refreshHolidayStateVariables()` | Skriver `isHoliday` och `isHolidayEve` för den aktuella dagen. |
| `snapToWholeDays(startMs, endMs)` | Vidgar ett tidsspann till hela dygn. Tillämpas när en helgdagshändelse sparas. |
| `exportCalendarToIcs(path, subscriptionIds, includeNative)` | Skriver valda importer, och valfritt lokalt skapade händelser, till en `.ics`-fil. |
| `parseICS(icsText)` | Tolkar ICS-text till händelser. Delas av import och av framtida flödeskällor. |

<!-- --8<-- [end:body] -->
