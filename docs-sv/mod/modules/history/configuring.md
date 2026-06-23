---
title: Historik — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Historik — Konfigurering

## Följa ett signal { #tracking-a-signal }

Panelen **Följ signal** håller diagrammet centrerat på en specifik signal när dess värde förändras över tid.

**Så här följer du en signal:**

1. Välj en signal från rullgardinsmenyn.
2. Klicka på **Följ**. Den följda signalen har en tjockare linje och de övriga linjerna tonas ned i färg.

**Så här slutar du följa:**

1. Klicka på **Sluta följa**. Diagrammet återgår till sin normala visning.

## Sparade signalgrupper { #saved-signal-groups }

Signalgrupper kan sparas och läsas in igen för att slippa välja om samma signaler varje gång. Sparade grupper hanteras från avsnittet **Sparade grupper** i panelen **Följ signal**.

![Panelen Sparade grupper med fältet för gruppnamn, rullgardinsmeny och importknapp](/docs/sv/Images/History/history-saved-signals.png){align=center}

**Så här sparar du en signalgrupp:**

1. Välj signalerna och klicka på **Använd** så att de visas i diagrammet.
2. Skriv ett namn i fältet **Ange gruppnamn**.
3. Klicka på **Spara grupp**. Gruppen sparas och visas i rullgardinsmenyn **Välj sparad grupp**.

**Så här läser du in en sparad grupp:**

1. Välj gruppen från rullgardinsmenyn **Välj sparad grupp**.
2. Klicka på **Använd grupp**. Signalerna från gruppen väljs och tillämpas i diagrammet.

**Så här tar du bort en sparad grupp:**

1. Välj gruppen från rullgardinsmenyn **Välj sparad grupp**.
2. Klicka på **Ta bort grupp**. Gruppen tas bort. Detta påverkar inte den loggade signaldatan.

### Importera grupper från andra vyer { #importing-groups-from-other-views }

Både den projektövergripande Historiken och den vyspecifika Historiken låter dig importera sparade grupper som skapats i andra vyer. Det gör att du kan återanvända en grupp som sparats i en vy utan att behöva skapa den på nytt.

![Dialogruta för sparade grupper med Alla sparade till vänster och Valda till höger](/docs/sv/Images/History/history-import-groups.png){align=center}

**Så här importerar du grupper från andra vyer:**

1. Klicka på **Importera grupper från vyer** i avsnittet **Sparade grupper**. En dialogruta öppnas.
2. Den vänstra panelen (**Alla sparade**) listar alla sparade grupper i projektet — både projektövergripande grupper och grupper sparade i andra vyer, organiserade efter källa.
3. Välj en grupp och klicka på **→** för att flytta den till den högra panelen (**Valda**).
4. Upprepa för varje grupp du vill importera.
5. Klicka på **Importera och stäng**. Grupperna läggs till i den aktuella listan med sparade grupper.

Om du vill ta bort en grupp från ditt urval innan import, väljer du den i den högra panelen och klickar på **←**. Klicka på **Rensa tillagda** för att tömma den högra panelen helt.

!!! note
    Att importera en grupp kopierar den till den aktuella kontexten. Ändringar i den ursprungliga gruppen efter import återspeglas inte.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — öppna den vyspecifika popup-rutan från ett skript och felsökning
<!-- --8<-- [end:body] -->
