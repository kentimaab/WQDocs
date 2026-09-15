---
title: Loggbok
product: mod
page_type: module
status: draft
last_reviewed: 2026-09-15
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok

Loggboksmodulen ger ett sätt att registrera fritextanteckningar kopplade till specifika delar av systemet. En post placeras på det den handlar om: en arbetsvy, ett objekt, eller en egen ämnessökväg.

Posterna nås genom ett gemensamt ämnesträd som kan ordnas på två sätt. I **arbetsvyläge** ordnas anteckningarna efter processvyernas mappstruktur, och i **signalläge** efter taggsökvägen. En anteckning går att nå i båda lägena, eftersom en anteckning på ett objekt även hör till varje vy där objektet är ritat, och en anteckning på en vy även hör till de objekt som är ritade i den.

Loggboken är tillgänglig på tre ställen: globalt under **Dokument & Loggbok → Loggbok**, i fliken [**Loggbok**](../../reference/Popup/Logbook.md) i valfritt objektpopup, samt via menyn **SpeedDial** i processvyer.

## Innehåll { #contents }

### [Kom igång](get-started.md) { #get-started }
* [**Loggboksvyn**](get-started.md#the-logbook-view) — Layout, ämnesträd, postlista och arkivering.
* [**Byta hur trädet ordnas**](get-started.md#switching-how-the-tree-is-keyed) — Arbetsvyläge och signalläge.
* [**Skapa en post**](get-started.md#creating-an-entry) — Fält och hur man sparar.
* [**Filtrering**](get-started.md#filtering) — Sökning och filtrering av poster, inklusive arkiverade.

---

### [Konfigurera](configuring.md) { #configuring }
* [**Vad en post placeras på**](configuring.md#what-an-entry-is-filed-against) — Vyer, objekt och egna ämnen.
* [**Hur de två träden byggs**](configuring.md#how-the-two-trees-are-built) — Arbetsvyläge, signalläge och hur en anteckning syns i båda.
* [**Kontexter**](configuring.md#contexts) — Hantering av namngivna kontextgrupper.
* [**Åtkomstmönster**](configuring.md#access-patterns) — Global användning, objektpopup och vybegränsad användning.

---

### [Utöka](extending.md) { #extending }
* [**Behörigheter**](extending.md#privileges) — Nödvändiga behörigheter för att lägga till, redigera och arkivera poster.
* [**Lagring av ämnet**](extending.md#topic-storage) — Kolumnerna `topic`, `topic_kind` och `topic_ref`.
* [**Arkivering**](extending.md#archiving) — Kolumnen `archived`, arkivfunktionerna och permanent radering.
* [**Skriptreferens**](extending.md#script-reference) — Funktionerna i `scLogBook` bakom trädet och de begränsade vyerna.

---

### [Felsökning](troubleshooting.md) { #troubleshooting }
* [**Vanliga problem**](troubleshooting.md) — Vanliga problem och hur man löser dem.
<!-- --8<-- [end:body] -->
