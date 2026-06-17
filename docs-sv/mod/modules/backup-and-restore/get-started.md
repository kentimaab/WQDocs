---
title: Säkerhetskopiering och återställning — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Säkerhetskopiering och återställning — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Säkerhetskopiering och återställning samt all
    relaterad funktionalitet som beskrivs i guiderna för Säkerhetskopiering och återställning:
    
    * `scBackUpAndRestore`

Funktionen Säkerhetskopiering och återställning sparar de aktuella värdena för valda DataStore-variabler som en namngiven säkerhetskopia. Den finns tillgänglig under **Inställningar → Säkerhetskopiering**.

## Vad kan säkerhetskopieras { #what-can-be-backed-up }

Variabelträdet visar DataStore-variabler som är tillgängliga för säkerhetskopiering — interna variabler och loggade signaler från processvyer. Systemvariabler med prefixet `_sys_` är undantagna. Alla variabler med ett värde av typen sträng, tal eller boolesk kan säkerhetskopieras.

En säkerhetskopia fångar värdena för de valda variablerna vid det tillfälle **Skapa säkerhetskopia** klickas. Det är en ögonblicksbild. Värden som ändras efter att säkerhetskopian skapats spåras inte.

## Skapa en säkerhetskopia { #creating-a-backup }

Navigera till **Inställningar → Säkerhetskopiering → Skapa**.

![Variable backup view](/Images/Backup_And_Restore/backup-create.png){align=center}

Vyn har två paneler. Den vänstra panelen listar alla tillgängliga DataStore-variabler med deras aktuella värden. Den högra panelen visar de variabler som kommer att ingå i säkerhetskopian.

Skriv i filterfältet längst upp i den vänstra panelen för att begränsa variabelträdet. Klicka på **X** för att rensa filtret.

![Filtering the variable tree](/Images/Backup_And_Restore/backup-filter.png){align=center}

1. Bläddra eller filtrera den vänstra panelen för att hitta de variabler som ska inkluderas.
2. Dubbelklicka på en variabel, eller markera den och klicka på **>**, för att flytta den till den högra panelen.
3. Ange ett namn i fältet **Säkerhetskopians namn**. Namnet måste vara unikt.
4. Ange eventuellt en beskrivning i fältet **Beskrivning av säkerhetskopia**.
5. Klicka på **Skapa säkerhetskopia**.
!!! tip
    Vyn kommer ihåg vilka variabler som ingick i den föregående säkerhetskopian, vilket gör det enkelt att skapa flera säkerhetskopior med samma variabelurval.

Om du vill rensa den högra panelen utan att skapa en säkerhetskopia klickar du på **Rensa tillagda variabler**.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — återställa och ta bort säkerhetskopior
<!-- --8<-- [end:body] -->
