---
title: Loggbok — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Loggbok — Konfigurering

## Ämnen { #topics }

Ett ämne är en sträng som identifierar var i systemet en post hör hemma. Ämnen är hierarkiska: nivåerna separeras med `/`. En post med ämnet `Building/Floor2/AHU01` visas när man väljer `Building`, `Building/Floor2` eller `Building/Floor2/AHU01` i ämnesträdet.

Ämnen behöver inte registreras i förväg. De skapas automatiskt första gången en post sparas under den ämnessträngen.

**Konvention:** Följ samma struktur som taggsystemet: `Connection/Device/System/Object`. Det gör det enkelt att hitta poster som hör till en specifik utrustning.

```text
MB/AS01/VS10/GT11
MB/AS01/VS10/PT01
MB/AS02
```

När loggboken öppnas från ett objektpopup sätts ämnet automatiskt utifrån objektets taggsökväg. När den öppnas från en vyknapp kan ämnet sättas från vyns namn eller skickas in explicit. Se [Utökning](extending.md) för hur man gör detta i ett skript.

![Ämnesträd som visar en nästlad hierarki](/Images/Logbook/topic-tree.png){align=center}

## Kontexter { #contexts }

Kontexter är namngivna grupperingar som kan användas för att kategorisera poster över ämnesgränserna. Exempel: `Operations`, `Commissioning`, `Alarms`. Standardkontexten `General` finns alltid tillgänglig.

Kontexter hanteras från popup-fönstret **Ändra loggbokskontext**, som öppnas genom att klicka på **...** bredvid fältet Kontext när en post skapas eller redigeras. Därifrån kan kontexter läggas till, byta namn och tas bort. Om en kontext tas bort raderas inte de poster som tillhör den. Dessa poster finns kvar i loggboken utan tilldelad kontext.

Vid filtrering i loggboken visas, när en kontext väljs, enbart poster tilldelade den kontexten oavsett ämne.

![Vy för kontexthantering](/Images/Logbook/context-management.png){align=center}

## Åtkomstmönster { #access-patterns }

### Globalt { #global }

Den fullständiga loggboken under **Dokument & Loggbok → Loggbok** visar alla poster från alla ämnen. Ämnesträdet till vänster kan användas för att begränsa visningen till ett specifikt område i systemet. Detta är den primära vyn för operatörer som behöver granska eller lägga till anteckningar för hela projektet.

### Objektpopup { #object-popup }

Varje objekt i projektet har en flik [**Loggbok**](../../reference/Popup/Logbook.md) i sitt popup-fönster. Öppnas den fliken visas enbart poster vars ämne matchar objektets taggsökväg. Nya poster som skapas härifrån tilldelas automatiskt rätt ämne.

![Loggboksfliken i objektets popup-fönster](/Images/Logbook/object-popup-logbook.png){align=center}

### Vybegränsad { #view-scoped }

Menyn **SpeedDial** i processvyer innehåller en knapp som öppnar en loggbok begränsad till den aktuella vyn. Endast poster som matchar vyns ämne visas, och nya poster som skapas härifrån tilldelas automatiskt rätt ämne. Se [Utökning](extending.md) för installationsdetaljer.

## Nästa steg { #next-steps }

* [Utökning](extending.md) — lägga till en loggbok i en anpassad vy eller knapp
<!-- --8<-- [end:body] -->
