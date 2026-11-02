---
title: Underhåll — Felsökning
description: Vanliga problem och lösningar för modulen Underhåll.
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Underhåll

## Vanliga problem { #common-issues }

| Problem | Lösning |
|---|---|
| Underhållswidgeten på dashboarden visar alltid noll för aktiva uppgifter | Kontrollera att underhållsdatabasens anslutning är aktiv och att underhållstabellen innehåller poster med de förväntade statusvärdena. **Mina pågående** och **Mina missade** räknar bara uppgifter som är tilldelade den inloggade användaren, och **Mina pågående** bara de med en deadline inom `maintenanceDaysAhead` dagar (60 som standard). Se [Dashboards — Konfigurering](../dashboards/configuring.md#maintenance). |
| En uppgift ligger kvar som Planerat efter sin deadline | Missade uppgifter upptäcks en gång i timmen av schemat `maintenance_tracker`. Vänta på nästa kontroll och kontrollera att schemat anropar `scMaintenance.findOverdue()`. |
| En återkommande uppgift skapades inte efter att den föregående slutfördes | Kontrollera att konfigurationen fortfarande är inställd på aktiv. Om objektet togs bort från konfigurationens objektlista mellan slutföranden genereras ingen ny uppgift för det objektet. |
| Uppgifter visar statusen Pågående | **Pågående** är en äldre status från en tidigare version av modulen. Skriptet `scMaintenance` innehåller en migrering som automatiskt konverterar dessa till **Planerat** vid uppstart. Om uppgifter fortfarande visar **Pågående** efter att systemet har startats om, kontrollera att skriptet `scMaintenance` körs och att migreringen slutfördes utan fel. |
| En missad uppgift genererade ingen uppföljning | Kontrollera att **Skapa nästa underhåll automatiskt vid missat deadline** är aktiverat i den återkommande konfigurationen. |

## Kända buggar { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
