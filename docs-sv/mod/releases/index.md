---
title: Versioner — Modular Framework
product: mod
page_type: release
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

# Versioner — Modular Framework

Versionshistorik för WideQuick Modular Framework. Den senaste versionen visas
först. Varje koncept som bygger på ramverket (BMS, WWT) är kopplat till en
specifik MOD-version och länkar tillbaka till sin post här.

## WideQuick MOD 2026.1.0 { #mod-2026-1-0 }

<details class="release" markdown="1" open>
<summary>Utgiven 2026-05-20</summary>

Den andra huvudversionen av WideQuick Modular Framework bygger vidare på grunden från 2024.1.0 med flera nya moduler och ett stort antal förbättringar av användarvänligheten. De viktigaste tilläggen är fullt stöd för flera språk, en intern loggbok, en underhållskalender, dokumenthantering och väsentligt bredare stöd för webb- och fjärrklienter — vilket gör ramverket enklare att driftsätta, konfigurera och använda för team och anläggningar.

### Nya funktioner

| Funktion                        | Beskrivning                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stöd för flera språk            | Vyer, skript, objektbiblioteket, dynamik och datastore är nu fullt översättningsbara, med en inbyggd språkväljare och flaggikoner för att byta språk under körning.                                                                                                                                                                            |
| Verktygstipssystem              | En ny mekanism för verktygstips (`scToolTip`) lägger till kontextuella hjälprutor i hela systemet, inklusive för historik- och kartobjekt.                                                                                                                                                                                                |
| Omskrivet arbetsvy-animationssystem | Animationssystemet har byggts om från grunden för att vara mer mångsidigt och enklare att konfigurera, med en tillhörande inställningsvy och hjälpfunktioner för att läsa användardefinierade temafärger.                                                                                                                                |
| ObjectFinder & goTo             | Varje objekt indexeras automatiskt med sin vysökväg och sitt namn, och den nya funktionen `goTo` låter dig hoppa direkt till vilket objekt som helst från var som helst i projektet.                                                                                                                                                      |
| Projektövergripande historik    | Historik kan nu visas för hela projektet, inte bara för ett enskilt objekt, med automatisk decimalskalning och ett bredare färgspann för lättlästa trender med flera kurvor.                                                                                                                                                              |
| Konfigurerbart körningsbeteende  | Uppdateringsfrekvensen för värdevisning är nu justerbar under körning, och valt tema (ljust/mörkt) sparas och återställs vid nästa start.                                                                                                                                                                                                      |
| Automatisk datalagring          | Loggrar och historik rensar nu automatiskt data som är äldre än en angiven ålder (t.ex. två år), vilket förhindrar att databaser växer obegränsat över tid.                                                                                                                                                                               |
| Import av äldre vyer            | Vyer som byggts i WideQuick BMS 8.0 eller tidigare kan lyftas direkt in i Modular Framework, där deras symboler omedelbart målas om till de nya, omdesignade objekten och behåller samma kopplingar. Användbart även utanför BMS-kontext, eftersom vissa projekt byggdes på BMS 8.0 utan avsikt att använda det för fastighetsautomation. |

### Nya och uppdaterade moduler

| Modul                | Beskrivning                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objektbibliotek      | En omdesignad uppsättning processsymboler (ventiler, givare, spjäll med mera) med ett renare, moderniserat utseende. Objekten standardiserades avseende teckenstorlek, decimaler, rubriker och beskrivningar, och digitala värdesvisningar lades till. Det är dessa symboler som äldre BMS 8.0-vyer målas om till vid import.                                                                                                     |
| dashboard      | En ny konfigurerbar dashboard byggd från ett bibliotek med återanvändbara widgetobjekt (`Dashboard Widgets.klib`). Widgets fungerar på dator, webb och fjärrklient, startdashboarden som visas efter inloggning är konfigurerbar, och exempeldashboards ingår att bygga vidare på.                                                                                                                              |
| Loggbok              | En ny modul för att skapa, bläddra i och filtrera tidsstämplade loggposter i hela projektet. Filtrera på ämne, datumintervall och användare; öppna den förfiltrerad på ett specifikt ämne; och bädda in mallen `LogBookEntryButton` i valfri vy.                                                                                                                                                                                   |
| Kalender             | En ny kalendermodul med månadsnavigering, miniikalender och en sidopanel för kommande händelser. Underhållsuppgifter visas som kalenderhändelser med statusbaserade färger och automatiska påminnelser inför planerat arbete.                                                                                                                                                                                                       |
| Dokument             | En ny dokumenthanteringsmodul med en filväljare för att ladda upp dokument och en hanterare (`scDoc`) för att koppla dokument till objekt, validerad för dator, fjärrklient och webb.                                                                                                                                                                                                                                             |
| Karthanterare        | En ny kartmodul med en exempelvy och webbkompatibelt kartstöd, samt en ny uppsättning kartnavigeringsindikatorobjekt för att placera och länka objekt på en karta.                                                                                                                                                                                                                                                                |
| Underhåll            | Kraftigt utökat: återkommande underhållsuppgifter med ett trädvysobjekt för urval, realtidssynkronisering mellan alla anslutna klienter, uppdateringsknappar, en underhållsräknare per användare på dashboarden, samt status- och prioritetsfärger genomgående. En ny **systemidentitets**-mekanism registrerar varje system, taggar uppgifter per system och lägger till en systemkolumn och ett filter så att en enda underhållsdatabas kan betjäna flera installationer. |
| Rapporter            | Rapportschemaläggaren stödjer nu två tidsintervall per dag och schemaläggning via alias, visar tydliga statusmeddelanden och kan skapas och köras från fjärrklienter. Rapporter från en befintlig WideQuick-installation kan också migreras in i ett Modular Framework-projekt.                                                                                                                                                    |
| Larm                 | En ny larmfrekvensvy visar hur ofta larm inträffar, fjärrlarm kan schemaläggas i larmscheman med sin larmklass och grupp, larmscheman har fått välj-alla / avmarkera-alla-knappar för larmgrupper, knappen "Visa information" stödjer visningsskript, och larmlogghändelser registreras inte längre dubbelt.                                                                                                               |
| Webb- och fjärrklienter | Stor utökning av klientstödet: rapportskapande, redigering av larmscheman och loggvisaren fungerar nu på WideQuick Web och fjärrklienter, och suffix, vybehörigheter och underhållsstatus synkroniseras mellan alla klienter.                                                                                                                                                                                                    |

### Ändringar

| Område               | Beskrivning                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Navigering           | "Loggar" har flyttats in i "Rapporter & loggar", "Underhåll & loggar" har bytt namn till "Underhåll", enskilda menyalternativ kan döljas under körning, och en knapp för att visa om dolda undernavigeringsalternativ har lagts till.                                                                                                                                                          |
| Inloggning & användare | Inloggning är nu möjlig via en kombinationsruta istället för att skriva ett användarnamn, och inloggningskravet kan inaktiveras från inställningsvyn.                                                                                                                                                                                                                                    |
| Användare & behörigheter | Nya demoanvändare har lagts till, var och en med en rimlig rollbaserad behörighetsnivå, och behörighetssystemet har omarbetats: behörigheter har bytt namn från det gamla schemat till ett nytt, dedikerade behörigheter har lagts till för underhålls- och loggboksåtgärder, och användare får nu ett tydligt meddelande när de saknar behörighet för en åtgärd. Rollen `Servicetekniker` har bytt namn till `service`. |
| Processvärdesobjekt  | Värdeuppdateringar drivs nu av en datastore-lyssnare istället för dynamik, vilket ger lättare rendering för inaktuella eller långsamt föränderliga variabler eftersom objektet bara ritas om när värdet faktiskt ändras.                                                                                                                                                                   |
| Larmterminologi      | Larmterminologin har standardiserats: "Allvarlighetsgrad" är nu "Larmklass" och "Bekräfta/Bekräftbara" är nu "Kvittera/Kvitterbara" i vyer och översättningar.                                                                                                                                                                                                                           |
| Inställningar        | Inställningar som inte är tillgängliga på fjärr-/webbklienter är nu tydligt inaktiverade.                                                                                                                                                                                                                                                                                                |
| Kartindikatorer      | En ny uppsättning kartnavigeringsindikatorobjekt har introducerats och används nu som standard. De tidigare kartindikatorerna används inte längre i ramverkets vyer men är fullt funktionella och beter sig precis som tidigare, så befintliga projekt som använder dem påverkas inte.                                                                                                    |
| **Licensiering**     | Projektet levereras nu under BSD 3-klausulslicensen, tillsammans med tredjepartslicenstexter och attributioner.                                                                                                                                                                                                                                                                           |

### Icke bakåtkompatibla ändringar & migrering

| Ändring                        | Migreringsinformation                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objekt använder nu SuffixAlias | Alla ramverksobjekt har konverterats för att referera till värden via ett `SuffixAlias` istället för suffix direkt, och egenskapen lades till i popupobjekt för att göra detta explicit. Projekt som uppgraderar från 2024.1.0 måste definiera ett suffixalias för varje objekt; objekt med ett okonfigurerat alias markeras visuellt i vyerna. Det är det huvudsakliga migreringssteget för denna version. |
| Namnbyte av behörigheter       | Behörigheter har bytt namn från det gamla schemat till ett nytt. Projekt som uppgraderar från 2024.1.0 bör kontrollera sina behörighetstilldelningar efter uppgraderingen, eftersom anpassade tilldelningar kopplade till de gamla behörighetsnamnen behöver mappas om till de nya.                                                                                                            |
| Suffixlagring                  | `scSuffix.suffixObj` är nu uppdelat i tre kolumner. Befintliga projekt uppgraderas automatiskt första gången projektet öppnas; ingen manuell åtgärd krävs.                                                                                                                                                                                                                                    |
| Underhållssystemidentitet      | Vid första start migreras befintliga underhållsuppgifter till det aktuella systemet baserat på värdnamn, och en migreringsdialog visas om ett namnbyte på applikationen upptäcks. Granska tilldelningen efteråt för att bekräfta att uppgifter tillskrivs rätt system.                                                                                                                        |

</details>

## WideQuick MOD 2024.1.0 { #mod-2024-1-0 }

<details class="release" markdown="1">
<summary>Utgiven 2024-09-03</summary>

Den första officiella versionen av WideQuick Modular Framework — en färdig HMI/SCADA-mall sammansatt av
oberoende, återanvändbara moduler. Den tillhandahåller en temad, behörighetsstyrd operatörsmiljö med ett komplett
bibliotek av processgrafik, larmhantering, trender, rapporter, underhåll, säkerhetskopiering och spårningslogg,
så att ett nytt projekt startar från ett fungerande system snarare än en blank canvas.

### Nya funktioner

| Funktion                              | Beskrivning                                                                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Modulär arkitektur                    | Ramverket är byggt av fristående moduler (larm, trender, rapporter, underhåll, säkerhetskopiering m.m.) som kan återanvändas och kombineras oberoende av varandra, så ett projekt inkluderar bara det som behövs. |
| Temasystem                            | Inbyggda ljusa och mörka teman med en delad färgpalett namngiven enligt Googles Material-konvention. Teman växlar konsekvent i alla vyer, objekt och navigeringslisten.                               |
| Inloggning & behörighetssystem        | Rollbaserad inloggning med vylåsning, så att användare bara ser och når de vyer och åtgärder som deras behörighetsnivå tillåter. Otillåtna åtgärder bemöts med tydliga felmeddelanden istället för tysta fel. |
| Navigeringssystem                     | En huvudmeny plus en automatgenererad undernavigering som bygger sig själv utifrån projektets vyer och håller menyerna i synk när vyer läggs till.                                                    |
| Suffixsystem                          | En central suffix-/aliasmekanism som låter samma objektgrafik återanvändas för många processobjekt utan att behöva bygga om vyer.                                                                     |
| Dynamiska arbetsvy-objekt (DynTouch)  | Interaktiva processobjekt som aktiveras med livevärden och klickbara popups.                                                                                                                           |
| Säkerhetskopiering & återställning    | Operatörer kan välja variabler (med sökfunktion), spara deras värden och återställa dem senare, med de ursprungliga variabelnamnen bevarade.                                                          |

### Nya och uppdaterade moduler

| Modul                          | Beskrivning                                                                                                                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Processobjektbibliotek         | En komplett uppsättning P&ID-symboler: pumpar, ventiler, ställdon, rör, kärl/tankar, värmeväxlare, kompressorer, instrument och PID-reglerobjekt, alla konsekvent skalade och stiliserade. |
| Larmmodul                      | Levande larmlistor med filtrering, larmräknare i navigeringslisten, larmgruppering och larmklass, stöd för autokvittering samt extern avisering via e-post och GSM-modem.  |
| Trender & historik             | Trendvyer med konsekvent namngivning av teckenförklaringar och temavänliga färger för lättlästa flerkurvsgrafar.                                                                   |
| Rapportmodul                   | Manuell och schemalagd rapportgenerering med en gemensam mall, en rapportkö och e-postleverans för automatiska rapporter.                                                          |
| Underhållsmodul                | Underhållsschemaläggning och maskinkort för planering och uppföljning av servicearbeten.                                                                                           |
| Spårningslogg                  | Spårar variabel- och strukturändringar (inklusive initialvärden), med filtrering, sortering och en dedikerad databas.                                                              |
| Popup- & objektinformationssystem | Standardiserade objektpopups med värdesvisningar, decimaler, behörigheter och per-objektinställningar.                                                                           |
| Fjärr- och flersystemsstöd     | En fjärrsystemshanterare med startprogram och aggregerade larmantal från anslutna system.                                                                                         |

</details>
