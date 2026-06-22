---
title: Teman — Kom igång
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Teman — Kom igång
???+ info "Krav"
    Följande skript krävs för att använda Teman och all
    relaterad funktionalitet som täcks i guiderna för Teman:
    
    * `scThemes`
    * `scAlert`

## Ljust och mörkt läge { #light-and-dark-mode }

WideQuick MOD levereras med både ett ljust och ett mörkt tema. De två varianterna delar samma färgstruktur men inverterar ytans hierarki. Bakgrunder som är ljusa i den ena varianten blir mörka i den andra, och textfärger justeras därefter.

![Jämförelse av ljust och mörkt tema](/Images/Themes/theme-light-dark.png){align=center}

## Byta tema { #switching-themes }

### I WideQuick Designer® { #in-widequick-designer }

Starttema är det tema som applikationen använder när den läses in första gången. Det ställs in i **WideQuick Designer®**. Öppna grenen **Teman** i projektträdet för att se alla tillgängliga teman. Högerklicka på önskat tema och välj **Ange som starttema**.

### I WideQuick Runtime® { #in-widequick-runtime }

Temat kan växlas mellan ljust och mörkt under körning utan att applikationen behöver startas om. I **WideQuick Runtime®**, navigera till **Inställningar** och använd temaväxlaren. Inställningen sparas och behålls mellan omstarter.

## Hur objekt följer teman { #how-objects-follow-themes }

Alla objekt i projektet använder temafärgsroller i stället för fasta färger. När temat ändras uppdateras varje bakgrund, textfärg, kant och yta automatiskt. Ingen manuell justering behövs per objekt.

Detta gäller även larmstatussfärger. Objekt med aktiva larm visar färger såsom larm- och varningsindikatorer definierade i temat, vilket säkerställer visuell konsekvens mellan teman. Se [arbetsvy-animationer](../../../guides/arbetsvy-animations.md) för hur larmstatusanimationer konfigureras.

## Nästa steg { #next-steps }

* [Konfigurera](configuring.md) — ändra enskilda färger och tilldela färgroller till objekt
* [Utöka](extending.md) — skapa ett anpassat tema som följer en grafisk profil
<!-- --8<-- [end:body] -->
