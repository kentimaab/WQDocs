---
title: Spårningslogg — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Spårningslogg — Konfigurering

## Konfigurera variabler att spåra { #configuring-variables-to-track }

Navigera till **Historik → Loggar → Spårningslogg → Spårningslogg - Inställningar**.

![Spårningslogg - Inställningsvy](/docs/sv/Images/Audit_Trail/audit-trail-settings.png){align=center}

Vyn har två paneler. Den vänstra panelen visar alla tillgängliga Datalager-variabler. Den högra panelen visar de variabler som för närvarande spåras.

För att börja spåra en variabel, markera den i den vänstra panelen och klicka på knappen **>**. För att sluta spåra en variabel, markera den i den högra panelen och klicka på knappen **<**. Variabler kan också läggas till eller tas bort genom att dubbelklicka.

Variabler kan läggas till på valfri nivå i Datalager-trädet. Genom att markera en överordnad nod och klicka på **>** läggs alla variabler under den noden till på en gång.

!!! warning
    Undvik att spåra variabler som ändras kontinuerligt, såsom mätvärden och sensoravläsningar. Det genererar ett mycket stort antal loggposter och gör loggen svår att använda. Spårningsloggen är avsedd för variabler som ändras sällan och avsiktligt, exempelvis börvärden, styrsignaler och konfigurationsvärden.
<!-- --8<-- [end:body] -->
