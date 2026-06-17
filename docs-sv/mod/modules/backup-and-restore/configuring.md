---
title: Säkerhetskopiering och återställning — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Säkerhetskopiering och återställning — Konfigurering

## Återställa en säkerhetskopia { #restoring-a-backup }

Navigera till **Inställningar → Säkerhetskopiering → Återställ**.

![Återställ variabler från säkerhetskopia](/Images/Backup_And_Restore/backup-restore.png){align=center}

Vyn har tre paneler. Den vänstra panelen listar alla sparade säkerhetskopior med deras skapandedatum. Om du väljer en säkerhetskopia visas dess metadata under panelerna, och den mellersta panelen fylls med de variabler som finns lagrade i den säkerhetskopian.

![Metadata för säkerhetskopia visas under panelerna](/Images/Backup_And_Restore/backup-metadata.png){align=center}

* **Skapad den** — datum och tid då säkerhetskopian skapades.
* **Skapad av** — den användare som skapade säkerhetskopian.
* **Beskrivning** — den beskrivning som angavs vid skapandet.

Den mellersta panelen stöder samma filter som vyn för att skapa säkerhetskopior. Skriv i filterfältet för att begränsa variabellistan.

1. Välj en säkerhetskopia i den vänstra panelen.
2. Bläddra eller filtrera den mellersta panelen för att hitta de variabler som ska återställas.
3. Dubbelklicka på en variabel, eller markera den och klicka på **>**, för att flytta den till den högra panelen. Klicka på **Lägg till alla variabler** för att lägga till alla variabler på en gång.
4. Klicka på **Återställ från säkerhetskopia**. De lagrade värdena tillämpas omedelbart.

## Ta bort en säkerhetskopia { #deleting-a-backup }

1. Navigera till **Inställningar → Säkerhetskopiering → Återställ**.
2. Välj den säkerhetskopia som ska tas bort i den vänstra panelen.
3. Klicka på **Ta bort säkerhetskopia** och bekräfta. Säkerhetskopian och alla dess lagrade värden tas bort permanent.
<!-- --8<-- [end:body] -->
