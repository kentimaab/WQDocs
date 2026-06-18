---
title: Loggbok — Utöka
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Loggbok — Utöka

## Behörigheter { #privileges }

Tre behörigheter styr åtkomsten till loggboksoperationer:

| Behörighet | Beskrivning |
|---|---|
| `Logbook_Add` | Krävs för att skapa nya poster |
| `Logbook_Edit` | Krävs för att redigera befintliga poster |
| `Logbook_Delete` | Krävs för att ta bort poster |

Användare utan `Logbook_Add` ser knappområdet **Lägg till** inaktiverat och nedtonat, med ett rött överlager som visar ett meddelande om vilken behörighet som krävs. Egenskapen `Enabled` på knappen är bunden till `scUsers.hasPriv("Logbook_Add")`. Samma mönster gäller för `Logbook_Edit` och `Logbook_Delete`.

<!-- --8<-- [end:body] -->
