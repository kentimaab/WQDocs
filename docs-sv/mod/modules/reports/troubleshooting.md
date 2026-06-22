---
title: Rapporter — Felsökning
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Rapporter — Felsökning

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Datum är utanför intervallet | Om inga data finns tillgängliga för den valda tidsperioden misslyckas rapporten. Kontrollera att värdena faktiskt lagras i databasen. Om inte, verifiera att loggern är korrekt konfigurerad. Se [Loggrar](../../guides/Loggers.md) för mer information. |
| Rapporten är tom | Om inga data visas i rapporten misslyckas troligen makrokommandot. Detta sker bara när en anpassad mall används. Granska makrokommandots konfiguration under [Skapa mallar](extending.md#creating-templates) |
| Rapporten skickas inte | Antingen är SMTP-servern inte korrekt konfigurerad — försök skicka ett testmejl från vyn **Rapporter — Schema** för att verifiera. Om det fungerar, kontrollera att e-postadresserna är korrekt angivna. Se [Larm — Utöka](../Core/alarms/extending.md#email-notifications) för SMTP-konfiguration. |

## Kända buggar { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
