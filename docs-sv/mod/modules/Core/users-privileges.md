---
title: Användare och behörigheter
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

Användare kan hanteras i antingen **WideQuick Designer®** eller **WideQuick Runtime®**.

### WideQuick Designer®

I projektträdet, dubbelklicka på **Användare och behörigheter**. För att lägga till en ny användare,
högerklicka på **Användare** och välj **Lägg till användare...**. För att redigera en befintlig användare,
dubbelklicka på **Användare**, högerklicka på användaren och välj **Egenskaper...**.

### WideQuick Runtime®

Navigera till **Inställningar** i huvudmenyn och öppna vyn **Inställningar**. Under
**Användare och behörigheter** klicka på **Byt användare**. Klicka på **Lägg till...** för att skapa en ny
användare eller välj en befintlig användare och klicka på **Redigera...** för att ändra den.

![Users](/Images/User_and_privileges/Users.png)

#### Användarinställningar

* **Användare** — användarnamnet för profilen
* **Beskrivning** — en valfri beskrivning av användaren
* **Lösenord** / **Verifiera lösenord** — ett valfritt lösenord för användaren
* **Behörigheter** — bevilja eller neka behörigheter genom att dubbelklicka på en behörighet, eller
markera den och klicka på **Bevilja** eller **Neka**

![Edit Users](/Images/User_and_privileges/Edit_Users.png)

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

![Privilege](/Images/User_and_privileges/Privilege.png)

## Begränsa arbetsvyer med behörighet { #restricting-arbetsvyer-by-privilege }

Åtkomst till specifika **arbetsvyer** kan begränsas baserat på behörigheter. Navigera
till **Inställningar → Arbetsvyer → Arbetsvyer - Behörighet** i huvudmenyn.

![arbetsvy Privilege](/Images/User_and_privileges/WorkView_privleage.png)

Välj den **arbetsvy** där begränsningen ska tillämpas. Konfigurationsalternativ
visas på höger sida av vyn.

![arbetsvy Settings](/Images/User_and_privileges/Settings.png)

Välj den önskade behörigheten från rullgardinsmenyn och klicka på **Spara** för att tillämpa
ändringen.

För information om hur begränsade **arbetsvyer** visas i navigeringsmenyn och
hur man konfigurerar de två visningsstilarna för låsta vyer, se
[Navigering — Konfigurering](../Core/Navigation/configuring#setting-privilege-requirements-on-views--setting-privilege-requirements-on-views-).
<!-- --8<-- [end:body] -->
