---
title: Referens
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Referens

Tekniskt referensmaterial för WideQuick MOD. Dessa sidor beskriver hur systemet är uppbyggt — taggkonventioner, skriptberoenden, databasscheman och grundläggande körningskoncept.

## Innehåll { #contents }

### [Databasscheman](database-schemas/index.md) { #database-schemas }

* [**Config**](database-schemas/config-db.md) — Navigation, rapporter, loggbok, objekt, dokument och modulkonfiguration.
* [**History**](database-schemas/history-db.md) — Dynamiskt genererade loggartabeller för signalhistorik.
* [**Maintenance**](database-schemas/maintenance-db.md) — Underhållsuppgifter, kalenderhändelser och register för fjärrsystem.
* [**SuffixConfig**](database-schemas/suffixconfig-db.md) — Konfiguration av suffixobjekt.
* [**BackUpAndRestore**](database-schemas/backupandrestore-db.md) — Variabler valda för säkerhetskopiering, sparade säkerhetskopior och deras värden.
* [**EventList**](database-schemas/eventlist-db.md) — Systemets händelselogg och lista över variabler som bevakas av Spårningslogg.
* [**Larmlista**](database-schemas/larmlista-db.md) — Loggade statusändringar för larm.

---

### Multiview

* [**Multiview**](multiview.md) — Hur man konfigurerar länkning av Arbetsvyer så att systemet kan navigera mellan vyer baserat på objektåtgärder.

---

### [Popup-fönster](Popup/index.md) { #popups }

* [**Flik**](Popup/Tab.md) — Startpunkt för alla popup-fönster: objektöversikt, larm- och underhållssammanfattning.
* [**Historik**](Popup/History.md) — Trendgraf över loggade signaler för det valda objektet.
* [**Trend**](Popup/Trend.md) — Livevärdessignaler i en realtidsgraf.
* [**Objektinfo**](Popup/ObjectInfo.md) — Rålista över alla signaler kopplade till objektet, med aktuella värden, enheter och typer.
* [**Underhåll**](Popup/Maintenance.md) — Schemalagda underhållsuppgifter för objektet.
* [**Loggbok**](Popup/Logbook.md) — Loggboksposter för objektet.
* [**Dokument**](Popup/Documents.md) — Dokument kopplade till objektet.
* [**Process**](Popup/Process.md) — Processvärden och statussignaler (suffixberoende).
* [**Manöver**](Popup/Maneuver.md) — Byte av driftläge och manuell börvärdesstyrning (suffixberoende).
* [**Tidskanal**](Popup/Time-channel.md) — Konfiguration av tidsbaserat schema (suffixberoende).
* [**Styrkurva**](Popup/Control%20curve.md) — Icke-linjär styrkurveeditor (suffixberoende).
* [**Styrkurva Tid**](Popup/Control%20curveTime.md) — Tidsbaserad styrkurveeditor (suffixberoende).
---

### Resurser och Resurspaket

* [**Resurser och Resurspaket**](Resources-and-Resource-package.md) — Export och import av resurser mellan projekt.

---

### Skripthierarki

* [**Skripthierarki**](ScriptHierarchy.md) — Beroendestruktur för alla skript i WideQuick MOD.

---

### Suffixsystem

* [**Suffixsystem**](suffix-system.md) — Hur suffixobjekt är strukturerade, deras attribut och hur de associeras med popup-fönster.

---

### Taggstruktur

* [**Taggstruktur**](tag-structure.md) — Taggnamnskonventioner och konfiguration för WideQuick MOD.

<!-- --8<-- [end:body] -->
