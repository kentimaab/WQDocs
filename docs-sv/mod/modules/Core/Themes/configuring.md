---
title: Teman — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Teman — Konfigurering

## Ändra en färg { #changing-a-color }

I **WideQuick® Designer**, öppna grenen **Themes** i projektträdet och dubbelklicka på det tema du vill redigera. Dialogrutan **Edit theme** öppnas med tre flikar: **Components**, **Custom colors** och **Keyboard**.

![Theme editor](/docs/sv/Images/Themes/theme-edit-dialog.png){align=center}

Navigera till fliken **Custom colors** och dubbelklicka på en färgkod för att ändra dess värde.

## Hur färger appliceras på objekt { #how-colors-are-applied-to-objects }

Färger från det aktiva temat appliceras på objekt via skript. Ett `onLoad`-skript eller ett dynamikuttryck anropar `System.themes.color()` med namnet på färgrollen:

```javascript title="Applying a theme color in onLoad"
this.brush.color1 = System.themes.color("surface")
this.pen.color = System.themes.color("onSurface")
```

För att se vilken färgroll ett specifikt objekt använder, kontrollera dess `onLoad`-skript eller dynamik. Namnet som skickas till `System.themes.color()` motsvarar direkt en post i inställningarna för **Edit theme**.

## Anpassade färger { #custom-colors }

Fliken **Custom colors** innehåller projektspecifika färger tillsammans med standardrollerna — till exempel `Symbol_Alarm`, `Symbol_Warning` och `Alarm_Severity_0` till `Alarm_Severity_5`. Dessa följer samma namnkonvention som standardroller och används på samma sätt i skript:

```javascript title="Using a custom color"
System.themes.color("Symbol_Alarm")
```

För att lägga till en ny anpassad färg, klicka på **+** längst ned på fliken **Custom colors** (den läggs till som ColorX), tilldela ett namn och ange ett värde. Använd samma namn i alla teman så att färgen löses korrekt vid byte mellan teman.

## Modulspecifika färgpaletter { #module-specific-color-palettes }

Utöver de M3-roller som utgör huvudtemat innehåller WideQuick MOD ett antal separata färgpaletter som används av specifika moduler. Dessa paletter visas under temavarianten i **WideQuick® Designer** och kan redigeras på samma sätt som övriga temafärger, men de påverkas inte av ljust/mörkt-växlingen — de gäller oavsett vilket tema som är aktivt.

| Palett | Modul | Vad den styr |
|---|---|---|
| CalendarColors | Kalender | Färger per händelsekategori (ENERGY, SAFETY, HVAC m.fl.) i kalendervy |
| HistoryGraphColors | Historia | 13 färger som tilldelas mätvärdeskurvor automatiskt i trenddiagram |
| MaintenanceColors | Underhåll | Status- och prioritetsfärger för underhållsordrar |
| mapIndicators | Kartor | Indikatorfärger för linjer och statussymboler på systemkartor |
| pipeColors | Rör | Rörmediefärger (t.ex. Rinse\_Water, Sewage, Chemical) |
| ValueDisplay\_dark | Värdevisning | BV-, MV- och mätarspårsfärger i mörkt tema |
| ValueDisplay\_light | Värdevisning | BV-, MV- och mätarspårsfärger i ljust tema |

`ValueDisplay_dark` och `ValueDisplay_light` är undantaget — de växlas automatiskt av komponenten baserat på om det aktiva temats namn innehåller `_Dark`. Övriga paletter är statiska oavsett aktivt tema.

För att redigera en palett, öppna grenen **Themes** i projektträdet, välj önskad palett och dubbelklicka på en färgkod.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — skapa ett anpassat tema som följer en grafisk profil

!!! tip
    Om du vill läsa mer om M3: [Material Design 3](https://m3.material.io/){target="_blank"}
<!-- --8<-- [end:body] -->
