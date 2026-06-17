---
title: Dokument — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Dokument — Konfigurering

## Koppla dokument till objekt { #linking-documents-to-objects }

Dokument kan kopplas till specifika objekt i projektet. När ett dokument är kopplat till ett objekt blir det tillgängligt på fliken [**Dokument**](../../reference/Popup/Documents.md) i objektets popup.

Navigera till **Dokument → Objektreferenser** för att hantera kopplingar.

![Vy för objektreferenser](/Images/Documents/documents-objects-references.png){align=center}

Så här kopplar du dokument till ett objekt:

1. Hitta objektet i listan.
2. Klicka på **Redigera dokumentkopplingar**.
3. Dubbelklicka på en fil för att lägga till den. En **+**-indikator visar att den kommer att kopplas.
4. Klicka på **Uppdatera dokumentkopplingar** för att spara.

Ett dokument kan kopplas till flera objekt. Samma objekt kan ha flera dokument kopplade till sig.

## Objektpopup { #object-popup }

Varje objekt i projektet har en flik [**Dokument**](../../reference/Popup/Documents.md) tillgänglig via sin popup. Öppna popupen genom att klicka på ett objekt och välja fliken **Dokument**. Här visas alla dokument som är kopplade till det specifika objektet. Välj ett dokument och klicka på **Öppna** för att öppna en förhandsgranskning direkt i popupen.

![Dokumentfliken i objektpopupen](/Images/Documents/documents-object-popup.png){align=center}

## Synkronisering med filsystemet { #syncing-with-the-filesystem }

Lokala filer lagras i mappen `HTML/documents/` på servern. Dokumentlistan återspeglar vad som är registrerat i databasen, inte vad som faktiskt finns på disk. Om filer läggs till eller tas bort från mappen direkt — till exempel genom att kopiera filer via en nätverksresurs — visas de inte i listan förrän en synkronisering utförs.

Klicka på **Synkronisera med lokala filer på servern** för att skanna mappen och uppdatera databasen:

* Filer som finns på disk men inte i databasen läggs till i listan.
* Databasposter för filer som inte längre finns på disk tas bort.
* Onlineresurser tas aldrig bort vid synkronisering.

Synkroniseringen körs automatiskt när `scDoc` startar.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — behörighetsreferens
<!-- --8<-- [end:body] -->
