---
title: Config.db
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---
<!-- --8<-- [start:body] -->

# Config-databas

Config-databasen är den centrala konfigurationsdatabasen. Den lagrar beständigt applikationstillstånd som behöver överleva omstarter — navigationsstrukturer, objektregistreringar, schemalagda jobb, sparade användarinställningar och modulspecifik konfiguration för de flesta MOD-moduler.

## Larm { #alarms }

| Tabell | Beskrivning |
|---|---|
| `AlarmObjects` | Mappar larmnamn till deras enhetsnycklar. Används av `scAlarmFinder` för att avgöra vilken enhet ett larm tillhör. |
| `mail_schedules` | Aviseringscheman för larme-post och SMS. Varje rad definierar ett tidsfönster, aktiva dagar, allvarlighetsfilter och larmgruppsfilter. |
| `mailStats` | Logg över varje utgående e-post- och SMS-försök — tidsstämpel, mottagare, lyckad-flagga och eventuellt felmeddelande. |

## Navigation { #navigation }

| Tabell | Beskrivning |
|---|---|
| `navMenu` | Huvudnavigationsmenyn, lagrad som JSON. Byggs och uppdateras av `scNav` vid körning. |
| `subNavs` | Undernavigationsstrukturer för enskilda vyer, lagrade som JSON. Hanteras av `scSubNav`. |
| `viewPrivilegies` | Behörighetskrav per arbetsvy-namn. Styr vilka användare som har åtkomst till en given vy. |

## Historik { #history }

| Tabell | Beskrivning |
|---|---|
| `History_SavedSignals_Project` | Projektövergripande sparade signalgrupper i historikmodulen. Tillgängliga för alla användare. |
| `History_SavedSignals_View` | Vyspecifika sparade signalgrupper i historikmodulen. Begränsade till en specifik arbetsvy. |

## Loggbok { #logbook }

| Tabell | Beskrivning |
|---|---|
| `logbook` | Loggboksposter — text, ämne, författare och tidsstämpel. |
| `logbook_contexts` | Ämnes- och kontextdefinitioner som används för att kategorisera loggboksposter. |

## Rapporter { #reports }

| Tabell | Beskrivning |
|---|---|
| `ReportQueue` | Väntande rapportgenereringsjobb som väntar på att bearbetas av `scReports`. |
| `reportSchedules` | Schemalagda automatiska rapportkonfigurationer — frekvens, tidsfönster, loggenhet, mottagare och utdataformat. |
| `reportStats` | Historik över slutförda och misslyckade rapportjobb, inklusive felräkningar och tidsstämplar. |

## Dokument { #documents }

| Tabell | Beskrivning |
|---|---|
| `documents` | Dokumentmetadataposter. |
| `document_files` | Filreferenser för dokument — antingen en lokal filsökväg eller en online-URL. |
| `document_file_objects_mapping` | Mappar dokumentfiler till processobjekt via anslutning, enhet, system och objektnamn. |

## Objekt { #objects }

| Tabell | Beskrivning |
|---|---|
| `ObjectList` | Mappar processobjekt till de Arbetsvyer de visas i och deras Datalager-namn. Används av `scObjectFinder` och `scLinking` för att lösa upp objektplatser vid körning. |

## Styrkurvor { #control-curves }

| Tabell | Beskrivning |
|---|---|
| `StyrkurvaProfile` | Sparade styrkurveprofiler per tagg. Lagrar profilnamn, beskrivning och en JSON-representation av kurvan. |

## Tidskanaler { #time-channels }

| Tabell | Beskrivning |
|---|---|
| `TimeChannelProfile` | Sparade tidskanalsprofiler per tagg. Lagrar profilnamn, beskrivning och en JSON-representation av schemat. |
<!-- --8<-- [end:body] -->
