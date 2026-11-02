---
title: Spårningslogg — Konfigurering
description: Konfigurera vilka Datalager-variabler som spåras av Spårningsloggen.
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Spårningslogg — Konfigurering

## Konfigurera variabler att spåra { #configuring-variables-to-track }

Navigera till **Historik → Loggar → Spårningslogg → Spårningslogg - Inställningar**.
<!-- --8<-- [end:body-1] -->

![Spårningslogg - Inställningsvy](/docs/sv/Images/Audit_Trail/audit-trail-settings.png){align=center}

<!-- --8<-- [start:body-2] -->
Vyn har två paneler. Den vänstra panelen, **Variabler att spåra**, visar alla tillgängliga Datalager-variabler. Den högra panelen, **Variabler som spåras**, visar de variabler som för närvarande spåras.

För att börja spåra en variabel, markera den i den vänstra panelen och klicka på knappen **>**. För att sluta spåra en variabel, markera den i den högra panelen och klicka på knappen **<**. Variabler kan också läggas till eller tas bort genom att dubbelklicka.

Variabler kan läggas till på valfri nivå i Datalager-trädet. Genom att markera en överordnad nod och klicka på **>** läggs alla variabler under den noden till på en gång.

Ett filterfält ovanför varje panel begränsar dess träd till matchande variabler. Filtret begränsar också vad **>**, **<** och dubbelklick gör: att lägga till eller ta bort en överordnad nod omfattar bara de variabler under den vars sökväg innehåller filtertexten.

### Variabler som inte längre finns { #variables-that-no-longer-exist }

En spårad variabel som inte längre finns i Datalager, till exempel efter att en tagg bytt namn eller tagits bort, ligger kvar i listan och markeras med en ikon i den högra panelen. Noderna ovanför den markeras med ett grått utropstecken, så att den går att hitta i ett hopfällt träd. En saknad variabel loggas inte.

Så länge minst en spårad variabel saknas visas knappen **Ta bort alla saknade signaler** under den högra panelen. Den ber om en bekräftelse, där antalet variabler som tas bort visas, och tar sedan bort alla från listan. Det går inte att ångra.

!!! warning
    Undvik att spåra variabler som ändras kontinuerligt, såsom mätvärden och sensoravläsningar. Det genererar ett mycket stort antal loggposter och gör loggen svår att använda. Spårningsloggen är avsedd för variabler som ändras sällan och avsiktligt, exempelvis börvärden, styrsignaler och konfigurationsvärden.
<!-- --8<-- [end:body-2] -->
