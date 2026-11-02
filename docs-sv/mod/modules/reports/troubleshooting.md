---
title: Rapporter — Felsökning
description: Vanliga problem och lösningar för modulen Rapporter.
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Rapporter — Felsökning

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Rapporten misslyckas | Felet som visas i **Rapportstatus** är generellt och anger inte orsaken. Den vanligaste orsaken är att inga data finns lagrade för den valda tidsperioden. Kontrollera att värdena faktiskt lagras i databasen. Om inte, verifiera att loggern är korrekt konfigurerad. Se [Loggrar](../../guides/Loggers.md) för mer information. |
| Rapporten är tom | Om inga data visas i rapporten misslyckas troligen makrokommandot. Detta sker bara när en anpassad mall används. Granska makrokommandots konfiguration under [Skapa mallar](extending.md#creating-templates) |
| Rapporten skickas inte | SMTP-servern kan vara felkonfigurerad. Skicka ett testmejl från vyn **Rapporter - Schemalägg** för att kontrollera. Om det fungerar, kontrollera att e-postadresserna är korrekt angivna. Se [E-postnotifieringar](../Core/alarms/extending.md#email-notifications) i modulen Larm för SMTP-konfiguration. |
| **Skapa rapport** gör ingenting | En rapport kan inte skapas förrän minst en signal har valts i **LoggerList**. Välj en signal och försök igen. **Larmrapport** är undantagen, eftersom den inkluderar alla signaler automatiskt. **Larmrapport ett larm** kräver att exakt ett larm är valt. |
| Värdena är fel med en faktor tusen | Kontrollera väljarna **Enhet** och **Prefix** på rapportkontrollen. Varje vald signal skalas från sitt eget ursprungliga prefix till den valda visningsenheten, så en signal loggad i `Wh` och en loggad i `kWh` i samma rapport får var sin faktor. Faktorerna skickas otillämpade till mallen, och mallen gör skalningen. Se [Enheter och prefix](get-started.md#units-and-prefixes). |
| Schemalagda rapporter körs aldrig | Kontrollera att femminutersschemat i `Schedules.kdat` anropar `scReportScheduler.control_trigger()`. Ett anrop som namnger något annat skriptobjekt hoppas över tyst, utan fel. |

## Kända buggar { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
