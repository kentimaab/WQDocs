---
title: Historik — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-10-12
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->

# Historik — Konfigurering

## Följa ett signal { #tracking-a-signal }

Panelen **Följ signal** framhäver en specifik signal i diagrammet.

**Följa en signal:**

1. Välj en signal från rullgardinsmenyn.
2. Klicka på **Följ**. Den följda signalen har en tjockare linje och de övriga linjerna tonas ned i färg.

**Sluta följa:**

1. Klicka på **Sluta följa**. Diagrammet återgår till sin normala visning.

## Sparade signalgrupper { #saved-signal-groups }

Signalgrupper kan sparas och läsas in igen för att slippa välja om samma signaler varje gång. Sparade grupper hanteras från avsnittet **Sparade grupper** i panelen **Följ signal**.
<!-- --8<-- [end:body-1] -->

![Panelen Sparade grupper med fältet för gruppnamn, rullgardinsmeny och importknapp](/docs/sv/Images/History/history-saved-signals.png){align=center}

<!-- --8<-- [start:body-2] -->
**Spara en signalgrupp:**

1. Välj signalerna och klicka på **Använd** så att de visas i diagrammet.
2. Skriv ett namn i fältet **Ange gruppnamn**.
3. Klicka på **Spara grupp**. Gruppen sparas och visas i rullgardinsmenyn **Välj sparad grupp**.

**Läsa in en sparad grupp:**

1. Välj gruppen från rullgardinsmenyn **Välj sparad grupp**.
2. Klicka på **Använd grupp**. Signalerna från gruppen väljs och tillämpas i diagrammet. I den projektövergripande Historiken läggs de till bland de signaler som redan är valda. I den vyspecifika Historiken ersätter de det aktuella urvalet.

**Ta bort en sparad grupp:**

1. Välj gruppen från rullgardinsmenyn **Välj sparad grupp**.
2. Klicka på **Ta bort grupp**. Gruppen tas bort. Detta påverkar inte den loggade signaldatan.

### Importera grupper från andra vyer { #importing-groups-from-other-views }

Både den projektövergripande Historiken och den vyspecifika Historiken kan hämta signalerna i sparade grupper som skapats i andra vyer, så att en grupp som sparats i en vy kan återanvändas utan att skapas på nytt.
<!-- --8<-- [end:body-2] -->

![Dialogruta för sparade grupper med Alla sparade till vänster och Valda till höger](/docs/sv/Images/History/history-import-groups.png){align=center}

<!-- --8<-- [start:body-3] -->
**Importera grupper från andra vyer:**

1. Klicka på **Hämta signaler från grupper i driftbilder** (projektövergripande Historik) eller **Hämta signaler från andra grupper** (vyspecifik Historik) i avsnittet **Sparade grupper**. En dialogruta öppnas.
2. Den vänstra panelen (**Alla sparade**) listar sparade grupper organiserade efter källa. I den projektövergripande Historiken listas grupperna som sparats i vyer. I den vyspecifika Historiken listas de projektövergripande grupperna under **Projekt** och grupperna som sparats i andra vyer.
3. Välj en grupp och klicka på **→** för att flytta den till den högra panelen (**Valda**).
4. Upprepa för varje grupp som ska importeras.
5. Klicka på **Hämta och stäng**. Signalerna i de valda grupperna markeras i trädet **Signaler**, och knappen **Tillämpa** visar det nya antalet. Ett meddelande visar hur många signaler som hämtades, och dialogrutan stängs när meddelandet kvitteras.
6. Klicka på **Tillämpa** för att plotta signalerna.

För att ta bort en grupp från urvalet innan import, markera den i den högra panelen och klicka på **←**. Klicka på **Rensa tillagda** för att tömma den högra panelen helt.

!!! note
    Importen hämtar bara signalerna. Grupperna läggs inte till i rullgardinsmenyn **Välj sparad grupp**. För att behålla urvalet som en grupp här, spara det med **Spara grupp**.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — öppna den vyspecifika popup-rutan från ett skript och felsökning
<!-- --8<-- [end:body-3] -->
