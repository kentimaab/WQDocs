---
title: Användare och behörigheter
description: Skapa och hantera användare och behörigheter i WideQuick.
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Användare och behörigheter
???+ info "Krav"
    Följande skript krävs för att använda Användare och behörigheter samt all
    relaterad funktionalitet som täcks i guiderna för Användare och behörigheter:
    
    * `scUsers`
    * `scAlert`

WideQuick gör det möjligt att skapa användarprofiler med specifika behörigheter, vilket möjliggör
rollbaserad åtkomstkontroll i hela applikationen. Profiler kan konfigureras för att
begränsa eller bevilja åtkomst till specifika vyer och åtgärder.

## Lägga till och redigera användare { #adding-and-editing-users }

Användare kan hanteras i antingen **WideQuick® Designer** eller **WideQuick® Runtime**.

### WideQuick® Designer

I projektträdet, dubbelklicka på **Användare och behörigheter**. För att lägga till en ny användare,
högerklicka på **Användare** och välj **Lägg till användare...**. För att redigera en befintlig användare,
dubbelklicka på **Användare**, högerklicka på användaren och välj **Egenskaper...**.

### WideQuick® Runtime

Navigera till **Inställningar** i huvudmenyn och öppna vyn **Inställningar**. Under
**Användare och behörigheter** klicka på **Ändra användare**. Klicka på **Lägg till...** för att skapa en ny
användare eller välj en befintlig användare och klicka på **Redigera...** för att ändra den.

![Users](/docs/sv/Images/User_and_privileges/Users.png)

#### Användarinställningar

* **Användare** — användarnamnet för profilen
* **Beskrivning** — en valfri beskrivning av användaren
* **Lösenord** / **Verifiera lösenord** — ett valfritt lösenord för användaren
* **Behörigheter** — bevilja eller neka behörigheter genom att dubbelklicka på en behörighet, eller
markera den och klicka på **Bevilja** eller **Neka**

![Edit Users](/docs/sv/Images/User_and_privileges/Edit_Users.png)

## Lägga till och redigera behörigheter { #adding-and-editing-privileges }

I projektträdet, dubbelklicka på **Användare och behörigheter**. För att lägga till en ny behörighet,
högerklicka på **Behörigheter** och välj **Lägg till behörighet...**. För att redigera en befintlig
behörighet, dubbelklicka på **Behörigheter**, högerklicka på behörigheten och välj
**Egenskaper...**.

* **Behörighet** — behörighetens namn
* **Beskrivning** — en valfri beskrivning av behörigheten
* **Standard** — om behörigheten är **Beviljad** eller **Nekad** som standard
* **Virtuell behörighet** — om en användare beviljas denna behörighet kommer de även att
beviljas alla behörigheter som valts här
* **Användare** — bevilja eller neka användare genom att dubbelklicka på en användare, eller markera den och
klicka på **Bevilja** eller **Neka**

![Privilege](/docs/sv/Images/User_and_privileges/Privilege.png)

## Ramverkets behörigheter { #framework-privileges }

Ramverket levereras med behörigheterna nedan, definierade i `Privileges.kdat`.

!!! warning "Alla ramverkets behörigheter är nekade som standard"
    Samtliga är definierade med `Default="denied"`. En behörighet som tillkommer i en ny version är därför otillgänglig för alla roller tills den tilldelas, även för roller som redan har de närliggande behörigheterna. Gå efter en uppgradering igenom tilldelningarna för varje behörighet som versionen införde.

| Behörighet | Ger |
|---|---|
| `AlarmControl` | Kvittera och blockera larm |
| `Schedules` | Lägga till och redigera scheman |
| `TimeChannels` | Styra tidkanaler |
| `EditUsers` | Redigera användare, samt inställningarna **Kräv inloggning** och **Kräv användarnamn** |
| `Config` | Konfigurationsåtgärder, bland annat att rensa underhållsloggen |
| `editSMTP` | Redigera SMTP-konfigurationen |
| `Debug` | Felsökning. Inte avsett för driftsatta applikationer |
| `Logbook_View` | Visa loggboksposter |
| `Logbook_Add` | Lägga till loggboksposter |
| `Logbook_Edit` | Redigera befintliga loggboksposter |
| `Logbook_Archive` | Arkivera och återställa loggboksposter i den globala loggboksvyn |
| `Logbook_Delete` | Radera alla arkiverade anteckningar från inställningsvyn |
| `Logbook_Context` | Lägga till, ta bort och redigera loggbokskontexter |
| `Documents_View` | Visa och öppna dokument |
| `Documents_Upload` | Ladda upp nya dokument |
| `Documents_Edit` | Redigera dokumentnamn och metadata |
| `Documents_Link` | Koppla dokument till och från objekt |
| `Documents_Delete` | Ta bort dokument |
| `Documents_Sync` | Synkronisera databasen med filsystemet |
| `Maintenance_Add` | Lägga till nya underhållsuppgifter |
| `Maintenance_Edit` | Redigera status och beskrivning för underhållsuppgifter |
| `Maintenance_EditExtended` | Redigera tilldelad person, prioritet och deadline |
| `Maintenance_Templates` | Lägga till och ta bort återkommande underhåll i **Underhåll - Återkommande**. Underhållsmallar använder `Maintenance_Add` och `Maintenance_Edit` |
| `ControlCurve_ChangeProfile` | Växla mellan styrkurvans profiler |
| `ControlCurve_EditProfiles` | Redigera styrkurvans profiler |
| `ControlCurve_ManualControl` | Ändra styrkurvans värden direkt |
| `Settings_Project` | Ändra allmänna projektinställningar såsom språk, enheter, tid, SMTP och applikationsnamn |
| `Settings_Navigation` | Ändra navigeringsinställningar såsom fullskärmsmeny, direktnavigering och visning av låsta menyer |
| `Settings_Process_Images` | Ändra visningsinställningar för processbilder såsom namnskyltar, teckenstorlek, decimaler och handsymbol |
| `Setpoints` | Ändra börvärden och reglerparametrar på signaler märkta `PRIV=Setpoints` |
| `AlarmLimits` | Ändra larmgränser och larmfördröjningar på signaler märkta `PRIV=AlarmLimits` |
| `ManualCommand` | Sätta objekt i manuellt läge och ge manuella kommandon på signaler märkta `PRIV=ManualCommand` |
| `SystemConfig` | Ändra givarkalibrering och skalning på signaler märkta `PRIV=SystemConfig` |
| `TagInfo` | Reserverad för visning av tagginformation. Definierad, men används ännu inte av någon vy eller signal |

## Virtuella privilegier { #virtual-privileges }

Ett virtuellt privilegium gör det möjligt för ett enskilt privilegium att automatiskt
tilldela ett eller flera ytterligare privilegier. När en användare tilldelas ett
privilegium som innehåller virtuella privilegier får de även tillgång till alla
privilegier som ingår i det, utan att behöva tilldela dem individuellt.

**Exempel:** Om privilegiet `EditUsers` har `EditName` och `EditPassword` som
virtuella privilegier kommer alla användare som tilldelats `EditUsers` automatiskt
även att ha `EditName` och `EditPassword`.

Virtuella privilegier konfigureras i privilegieegenskaperna i **WideQuick®
Designer**. I projektträdet markeras privilegier som innehåller virtuella privilegier
med en särskild ikon.

<figure markdown="span">
  ![VirtualPrivilege](/docs/sv/Images/User_and_privileges/Virtual.png)
  <figcaption>Ikon i projektträdet.</figcaption>
</figure>

För att lägga till virtuella privilegier till ett privilegium, öppna
privilegieegenskaperna och klicka på knappen **Virtuellt privilegium** för att välja
vilka privilegier som ska ingå.

## Begränsa Arbetsvyer med behörighet { #restricting-workviews-by-privilege }

Åtkomst till specifika **Arbetsvyer** kan begränsas baserat på behörigheter. Navigera
till **Inställningar → Arbetsvyer → Arbetsvyer - Privilegie** i huvudmenyn.

![arbetsvy Privilege](/docs/sv/Images/User_and_privileges/Workview_privleage.png)

Välj den **Arbetsvy** där begränsningen ska tillämpas. Konfigurationsalternativ
visas på höger sida av vyn.

![arbetsvy Settings](/docs/sv/Images/User_and_privileges/Settings.png)

Välj den önskade behörigheten från rullgardinsmenyn och klicka på **Spara** för att tillämpa
ändringen.

För information om hur begränsade **Arbetsvyer** visas i navigeringsmenyn och
hur man konfigurerar de två visningsstilarna för låsta vyer, se
[Navigering — Konfigurering](../Core/Navigation/configuring#setting-privilege-requirements-on-views--setting-privilege-requirements-on-views-).
<!-- --8<-- [end:body] -->
