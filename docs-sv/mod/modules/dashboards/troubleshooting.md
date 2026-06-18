---
title: dashboards
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# dashboards

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Widget-rubrik visar "undefined" | Bindningen för egenskapen `Header` på widget-instansen är trasig. Kontrollera att bindningen är korrekt inställd på widgeten. |
| Widget-rubrik visar en rå svensk sträng | Värdet i `Header` är inte registrerat i `Translations.klib`. Lägg till strängen i `Translations.klib` och ange översättningen under **Translations → Project Translation** i projektträdet. |
| Signalvärdet visar -- eller är tomt | Signalvägen som skickas till widgeten matchar inte någon post i DataStore. Kontrollera stavningen, bekräfta att signalen finns i DataStore och verifiera att drivrutinen är ansluten och skriver värden. |
| Larmwidgetar visar inga larm trots att aktiva larm finns | Parametern `Grupp` eller `Grupper` är inställd på ett gruppnamn som inte matchar någon larmgrupp i projektet. Lämna parametern tom för att visa alla larm, eller kontrollera det exakta gruppnamnet i larmkonfigurationen. |
| Underhållswidgeten visar alltid noll för aktiva uppgifter | Bekräfta att anslutningen till underhållsdatabasen är aktiv och att underhållstabellen innehåller poster med de förväntade statusvärdena. |

## Kända fel { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
