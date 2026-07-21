---
title: Navigation — Konfigurering
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Navigation — Konfigurering
Det här avsnittet beskriver hur du konfigurerar modulen Navigation för att passa dina behov. Det
inkluderar hantering av åtkomstkontroll via behörighetsinställningar samt konfigurering av hur
begränsade vyer visas för användare.

Innan du börjar, se till att du är bekant med grunderna i modulen Navigation.
Om inte, se [Navigation — Kom igång](get-started.md).


## Ange behörighetskrav för vyer { #setting-privilege-requirements-on-views }
Eftersom menysystemet genereras automatiskt kan vyer inte döljas eller inaktiveras
på det traditionella sättet via säkerhetsfliken. Istället hanteras behörigheter via
inställningar i **WideQuick® Runtime**.

För att komma åt dessa inställningar, starta projektet och navigera till
**Huvudmeny → Inställningar → Arbetsvyer → Arbetsvyer - Behörighet**.

Här visas två menygrupper: **Main_Menu** och **System**. Expandera dessa för att välja
en specifik vy eller en **Arbetsvy**-mapp och tilldela sedan önskad **Behörighet** från
listan. **Arbetsvyn** är sedan bara tillgänglig för användare med rätt behörighet.
Behörigheter kan tillämpas på både enskilda **Arbetsvy** och hela **Arbetsvy**-mappar.

![SettingPriv](/docs/sv/Images/Navigation/SettingPriv.png)

!!! note "Krypterade projekt"
    Om ditt projekt är krypterat kan **WideQuick** inte föreslå behörigheter.
    Istället måste du skriva in namnet på **Behörigheten** manuellt.

!!! note "Behörighet"
    Inställningarna för **Behörighet** gäller för båda navigationssystemen.

## Visningsinställningar för begränsade vyer { #display-settings-for-restricted-views }
Det finns flera inställningar som styr hur begränsade mappar visas för användare
utan den nödvändiga behörigheten. Dessa inställningar finns under **Inställningar** i
**WideQuick® Runtime**.

![DisplayPriv](/docs/sv/Images/Navigation/Display%20priv.png)

Det finns två växlingsalternativ: **Visa låsta menyer** och **Visa låsta undermenyer**. Dessa
växlar erbjuder tre meningsfulla kombinationer. Observera att om **Visa låsta menyer** är
inaktiverat visas inte dess undermenyer oavsett inställningen för **Visa låsta undermenyer**.


![Kombinationer av visningsinställningar](/docs/sv/Images/Navigation/Combined,%20options.png){align=center}


* **Vänster** — Båda aktiverade.
* **Mitten** — Visa låsta menyer aktiverat, Visa låsta undermenyer inaktiverat.
* **Höger** — Visa låsta menyer inaktiverat — undermenyer visas inte oavsett inställning.

## Nästa steg { #next-steps }

* [Utöka](extending.md) — GoTo-funktion och anpassade navigationsikoner
<!-- --8<-- [end:body] -->
