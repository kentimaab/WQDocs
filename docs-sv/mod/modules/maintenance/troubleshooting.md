---
title: Underhåll — Felsökning
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
| Underhållswidgeten på instrumentpanelen visar alltid noll för aktiva uppgifter | Kontrollera att underhållsdatabasens anslutning är aktiv och att underhållstabellen innehåller poster med de förväntade statusvärdena. |
| En återkommande uppgift skapades inte efter att den föregående slutfördes | Kontrollera att konfigurationen fortfarande är inställd på aktiv. Om objektet togs bort från konfigurationens objektlista mellan slutföranden genereras ingen ny uppgift för det objektet. |
| Uppgifter visar statusen Pågående | **Pågående** är en äldre status från en tidigare version av modulen. Skriptet `scMaintenance` innehåller en migrering som automatiskt konverterar dessa till **Planerad** vid uppstart. Om uppgifter fortfarande visar **Pågående** efter att systemet har startats om, kontrollera att skriptet `scMaintenance` körs och att migreringen slutfördes utan fel. |
| En missad uppgift genererade ingen uppföljning | Kontrollera att **Skapa nästa underhåll automatiskt vid missat deadline** är aktiverat i den återkommande konfigurationen. |

## Kända buggar { #known-bugs }

| Problem | Lösning | Version |
|---|---|---|

<!-- --8<-- [end:body] -->
