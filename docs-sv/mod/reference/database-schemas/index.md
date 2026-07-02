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

!!! note
    WideQuick stöder flera olika typer av databaser. Att byta från en till en annan är enkelt, men anpassade frågor kan behöva justeras eftersom motorerna använder olika SQL-dialekter. Se [Distinctive Features Of SQLite](https://www.sqlite.org/different.html) för mer information om detta.

## Innehåll { #contents }

### Config

* [**Config**](config-db.md) — Den centrala konfigurationsdatabasen. Lagrar navigationsstrukturer, objektregistreringar, schemalagda jobb, rapportköer, loggboksposter, dokumentreferenser och sparade användarinställningar för de flesta MOD-moduler.

---

### History

* [**History**](history-db.md) — Lagrar loggad signaldata. Tabeller genereras dynamiskt av loggenheter — varje loggenhet skapar en datatabell och en metatabell identifierad med en hash av loggenhetens namn.

---

### Maintenance

* [**Maintenance**](maintenance-db.md) — Lagrar konfigurationer för underhållsuppgifter, uppgiftsloggen, ändringshistorik, kalenderhändelser och registret över kända fjärrsystem.

---

### SuffixConfig

* [**SuffixConfig**](suffixconfig-db.md) — Lagrar suffixobjektets konfiguration som JSON. Används av suffixsystemet för att lösa upp taggstrukturer vid körning.

---

### BackUpAndRestore

* [**BackUpAndRestore**](backupandrestore-db.md) — Lagrar variablerna som är valda för säkerhetskopiering och listan över sparade säkerhetskopior, tillsammans med de sparade variabelvärdena för varje kopia.

---

### EventList

* [**EventList**](eventlist-db.md) — Lagrar systemets händelselogg och listan över variabler som bevakas av Spårningslogg.

---

### Larmlista

* [**Larmlista**](larmlista-db.md) — Lagrar loggade statusändringar för larm. Tabeller genereras av larmloggenheten, på samma sätt som för History-databasen.
<!-- --8<-- [end:body] -->
