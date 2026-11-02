---
title: Loggbok
description: Översikt över popupen Loggbok i WideQuick.
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Loggbok

Loggbokspopupen visar de aktiva loggboksposter som är kopplade till det valda objektet.
Anteckningar kan skapas och redigeras direkt från denna popup. Den visas i flikmenyn för
alla objekt oavsett vilka suffix de har, men bara för användare med `Logbook_View`. För mer
information om hur loggbokssystemet fungerar, se [Loggbok](../../modules/logbook/index.md).

!!! note "Arkiverade poster visas inte här"
    Arkivering, återställning och permanent radering hanteras i den globala loggboken under
    **Dokument & Loggbok → Loggbok**, som också är det enda stället där arkiverade poster kan
    listas. Den här popupen visar alltid bara aktiva poster. Se
    [Loggbok — Utöka](../../modules/logbook/extending.md#archiving).
<!-- --8<-- [end:body-1] -->

![Logbook popup](/docs/sv/Images/Popups/Logbook.png)

<!-- --8<-- [start:body-2] -->
## Poster { #entries }

Postlistan visar alla loggboksanteckningar som är kopplade till objektet med följande
kolumner:

* **Titel** — anteckningens rubrik
* **Meddelande** — anteckningens innehåll
* **Kontext** — det ämne eller den kontext som anteckningen tillhör
* **Användare** — den användare som skapade anteckningen
* **Skapad** — datum och tid när anteckningen skapades
* **Senast ändrad** — datum och tid när anteckningen senast redigerades

## Filtrering { #filtering }

Den vänstra panelen möjliggör filtrering av poster efter kontext via rullgardinsmenyn. Välj
**Alla ämnen** för att visa alla poster, eller välj en specifik kontext för att filtrera listan.
Klicka på bockmarkeringsknappen för att tillämpa filtret. Klicka på **Visa inlägg** för att visa
de filtrerade resultaten.

## Åtgärder { #actions }

Följande åtgärder är tillgängliga längst ned i popupen:

* **Lägg till anteckning** — skapar en ny loggbokspost för detta objekt. Kräver `Logbook_Add`.
* **Redigera anteckning** — redigerar den valda posten. Kräver `Logbook_Edit`. Att
dubbelklicka på en post gör detsamma.
* **Visa inlägg** — läser in posterna för det valda ämnet i listan.

En åtgärd som den aktuella användaren saknar behörighet för är inaktiverad och täckt av en röd
ruta som anger vilken behörighet som krävs.
<!-- --8<-- [end:body-2] -->
