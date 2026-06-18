---
title: Versioner — WWT
product: wwt
page_type: release
status: draft
last_reviewed: 2026-06-16
tags:
 - WWT
---

# Versioner — WWT

Versionsnoteringar för WideQuick WWT. Den senaste versionen visas först. Varje version
är byggd på en specifik version av WideQuick Modular Framework, länkad under dess
rubrik. För det fullständiga ramverkets ändringslogg, se
[MOD-versioner](../../mod/releases/index.md).



## WideQuick WWT 2024.1.0 { #wwt-2024-1-0 }

Utgiven 2024-09-03

**Modular Framework-version**: [WideQuick MOD 2024.1.0](../../mod/releases/index.md#mod-2024-1-0)

<details class="release" markdown="1" open>
<summary>Versionsnoteringar</summary>

Den första officiella versionen av WideQuick WWT — vatten- och avloppskoncept byggt på Modular Framework. Dess funktionsuppsättning är identisk med [WideQuick MOD 2024.1.0](../../mod/releases/index.md#mod-2024-1-0); WWT skiljer sig endast i sin dedikerade tematik och en uppsättning WWT-specifika vyer. Det erbjuder en temad, behörighetsstyrd operatörsmiljö med ett komplett PID/processgrafikbibliotek, larmhantering, trender, rapporter, underhåll, säkerhetskopiering och spårningslogg, så att ett nytt projekt startar från ett fungerande system snarare än en tom canvas.

### Nya funktioner

| Funktion | Beskrivning |
| --- | --- |
| Modulär arkitektur | Ramverket är byggt av fristående moduler (larm, trender, rapporter, underhåll, säkerhetskopiering m.m.) som kan återanvändas och kombineras oberoende av varandra, så att ett projekt bara inkluderar det som behövs. |
| Temasystem | Inbyggda ljusa och mörka teman med en gemensam färgpalett namngiven enligt Google Material-konventionen. Teman växlar konsekvent i alla vyer, objekt och navigeringsfältet. |
| Inloggnings- och behörighetssystem | Rollbaserad inloggning med vyspärrning, så att användare bara ser och når de vyer och åtgärder som deras behörighetsnivå tillåter. Obehöriga åtgärder möts av tydliga felmeddelanden istället för tysta fel. |
| Navigationssystem | En huvudmeny plus en automatiskt genererad undernavigering som bygger sig själv från projektets vyer och håller menyerna synkroniserade när vyer läggs till. |
| Suffix-system | En central suffix/alias-mekanism som låter samma objektgrafik återanvändas för många processobjekt utan att behöva bygga om vyer. |
| Dynamiska arbetsvy-objekt (DynTouch) | Interaktiva processobjekt som lever upp med live-värden och klickbara popups. |
| Säkerhetskopiering och återställning | Operatörer kan välja variabler (med sökning), spara deras värden och återställa dem senare, med de ursprungliga variabelnamnen bevarade. |

### Nya och uppdaterade moduler

| Modul | Beskrivning |
| --- | --- |
| Processobjektbibliotek | En komplett uppsättning P&ID-symboler: pumpar, ventiler, aktuatorer, rör, kärl/tankar, värmeväxlare, kompressorer, instrument och PID-styrobjekt, alla konsekvent skalade och stiliserade. |
| Larmmodul | Live-larmlistor med filtrering, larmräknare i navigeringsfältet, larmgruppering och larmklass, stöd för automatisk kvittering samt extern avisering via e-post och GSM-modem. |
| Trender och historik | Trendvyer med konsekvent legendnamnsättning och temakänliga färger för läsbara flerkurvediagram. |
| Rapportmodul | Manuell och schemalagd rapportgenerering med en gemensam mall, med en rapportkö och e-postleverans för automatiska rapporter. |
| Underhållsmodul | Underhållsschemaläggning och maskinkort för planering och uppföljning av servicearbete. |
| Spårningslogg | Spårar variabel- och strukturändringar (inklusive initialvärden), med filtrering, sortering och en dedikerad databas. |
| Popup- och objektinformationssystem | Standardiserade objektpopups med värdesvisning, decimaler, behörigheter och per-objektsinställningar. |
| Fjärr- och flersystemsstöd | En fjärrsystemshanterare med startprogram och aggregerade larmantal från anslutna system. |

</details>
