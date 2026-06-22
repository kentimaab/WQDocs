---
title: Databasscheman
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Databasscheman

WideQuick MOD använder flera SQLite-databaser som lagras i mappen `Data/` i projektet. Varje databas ägs av en specifik uppsättning moduler och ska bara nås via de skript som hanterar den.

## Innehåll { #contents }

### [Config.db](config-db.md) { #config-db }

* [**Config.db**](config-db.md) — Den centrala konfigurationsdatabasen. Lagrar navigationsstrukturer, objektregistreringar, schemalagda jobb, rapportköer, loggboksposter, dokumentreferenser och sparade användarinställningar för de flesta MOD-moduler.

---

### [History.db](history-db.md) { #history-db }

* [**History.db**](history-db.md) — Lagrar loggad signaldata. Tabeller genereras dynamiskt av loggenheter — varje loggenhet skapar en datatabell och en metatabell identifierad med en hash av loggenhetens namn.

---

### [maintenance.db](maintenance-db.md) { #maintenance-db }

* [**maintenance.db**](maintenance-db.md) — Lagrar konfigurationer för underhållsuppgifter, uppgiftsloggen, ändringshistorik, kalenderhändelser och registret över kända fjärrsystem.

---

### [SuffixConfig.db](suffixconfig-db.md) { #suffixconfig-db }

* [**SuffixConfig.db**](suffixconfig-db.md) — Lagrar suffixobjektets konfiguration som JSON. Används av suffixsystemet för att lösa upp taggstrukturer vid körning.
<!-- --8<-- [end:body] -->
