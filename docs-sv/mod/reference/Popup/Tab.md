---
title: Flik
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Flik

Flik-popupen är den standardpopup som öppnas när ett `DynTouch`-objekt klickas.
Den fungerar som ett navigeringsnav för alla andra tillgängliga popupar för det objektet och
ger en omedelbar överblick över objektets aktuella status.

![Tab popup](/docs/sv/Images/Popups/Tab.png)

## Meny

Sektionen **Meny** längst upp visar en knapp för varje popup som är tillgänglig för
objektet. Följande popupar visas alltid oavsett vilka suffix objektet har:

* **Historik**
* **Underhåll**
* **Objektinfo**
* **Trend**

Ytterligare popupar — såsom **Process** eller **Styrning** — visas bara när objektet
har signaler som matchar de suffix som är konfigurerade för den popupen. Se
[Suffix - Popupar](../../../mod/guides/create-a-popup.md#configure-popup) för mer information
om hur popupar kopplas till suffix.

Menyn stöder maximalt 15 flikar. För information om hur du skapar anpassade popupar,
se [Skapa popup](../../../mod/guides/create-a-popup.md).

## Översikt

Sektionen **Översikt** visar allmän information om objektet:

* **Namn** — objektnamnet härlett från taggstrukturen
* **Anslutning** — den anslutning som objektet tillhör
* **Enhet** — den enhet som objektet tillhör
* **System** — det system som objektet tillhör
* En miniatyrvy av objektet som det visas i processvyn, automatiskt
genererad från dess placering i **Arbetsvy**

## Larmstatistik

Översikten visar även en livesammanfattning av objektets larmstatus:

* **Totalt antal aktiva larm**
* **Antal okvitterade larm**
* **Antal kvitterade larm**

Dessa värden härleds automatiskt från objektets taggnamn och kräver ingen
ytterligare konfiguration.

## Underhållsstatistik

Under larmstatistiken visas en sammanfattning av objektets underhållsstatus:

* **Totalt antal underhållsuppgifter**
* **Antal pågående underhållsuppgifter**
* **Antal missade underhållsuppgifter**

Dessa värden härleds också automatiskt från objektets taggnamn.
<!-- --8<-- [end:body] -->
