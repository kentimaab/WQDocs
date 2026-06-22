---
title: Teman — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Teman — Utöka

## Skapa ett anpassat tema { #creating-a-custom-theme }

Ett komplett tema kan genereras från en enda varumärkesfärg. Mata in den färgen i temabyggaren så härleds alla stödfärger, ljusa och mörka varianter, ytskikt för elevation samt kontrastnivåer automatiskt — resultatet är ett tema som passar kundens eller organisationens grafiska profil och fungerar väl i alla tillstånd.

### Steg 1 — Generera temat { #step-1-generate-the-theme }

Öppna [Temabyggaren](../../../../Tools/theme-builder.md). Den inbäddade **Material Theme Builder** låter dig ange en källfärg (eller ladda upp en logotyp för att extrahera en) och förhandsgranska det resulterande temat i ljust och mörkt läge. Exportera det färdiga temat som en `Colors.xml`-fil.

### Steg 2 — Importera till WideQuick { #step-2-import-into-widequick }

På samma sida för [Temabyggaren](../../../../Tools/theme-builder.md), scrolla ned till **Parse Theme into WideQuick format**:

1. Välj projektets `Themes.kdat`-fil. Den här filen finns i projektmappen (`WideQuick_MOD/`).
2. Välj den `Colors.xml`-fil som exporterades från Temabyggaren.
3. Klicka på **Merge new theme into existing themes file**.
4. Ladda ned den uppdaterade `Themes.kdat`.

Ersätt den befintliga `Themes.kdat` i projektmappen med den nedladdade filen. Om **WideQuick Designer®** var öppet, starta om det. Det nya temat visas under grenen **Themes** i projektträdet och kan anges som starttema.

## Vad M3 genererar automatiskt { #what-m3-generates-automatically }

När ett tema genereras via M3 härleds följande automatiskt:

* **Ljusa och mörka varianter** — båda produceras från samma källfärg.
* **Yttonalhierarki** — en uppsättning ytnivåer (`surfaceContainerLowest` till `surfaceContainerHighest`) som förmedlar elevation utan skuggor.
* **Kontrastvarianter** — medium och hög kontrastversion av varje roll för tillgänglighetsanpassning.
* **Färgrelationer** — alla `on*`-färger (t.ex. `onPrimary`, `onSurface`) beräknas för att uppfylla kontrastkraven mot sin bakgrundsfärg.

Det innebär att även ett kraftigt anpassat tema förblir läsbart och visuellt balanserat i alla sina tillstånd.

## Inbyggda teman { #built-in-themes }

Följande teman levereras med WideQuick MOD och är tillgängliga i projektets `Themes.kdat`:

| Tema | Variant |
|---|---|
| WQ_Material_BMS_Light | Light |
| WQ_Material_BMS_Dark | Dark |
| WQ_Material_VA_Light | Light |
| WQ_Material_VA_Dark | Dark |
| WQ_Material_MF_Light | Light |
| WQ_Material_MF_Dark | Dark |

Dessa kan användas som de är eller som utgångspunkt när ett anpassat tema byggs. BMS-, VA- och MF-varianterna skiljer sig åt i sina primära och sekundära varumärkesfärger men delar samma M3-struktur.
<!-- --8<-- [end:body] -->
