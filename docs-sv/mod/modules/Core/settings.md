---
title: Inställningar
description: Översikt över vyn Inställningar i WideQuick Runtime.
product: mod
page_type: module
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body-1] -->
# Inställningar

Vyn **Inställningar** i **WideQuick® Runtime** ger tillgång till alla
systemkonfigurationsalternativ. Navigera till **Inställningar** i huvudmenyn och
öppna vyn **Inställningar**.
<!-- --8<-- [end:body-1] -->

![Settings](/docs/sv/Images/Settings/Settings.png)

<!-- --8<-- [start:body-2] -->
Varje avsnitt är låst med en egen behörighet. En användare som saknar den ser avsnittets
inställningar inaktiverade och täckta av texten *Kräver privilegiet*, följt av
behörighetens namn.

| Avsnitt | Behörighet |
|---|---|
| Allmänna inställningar | `Settings_Project` |
| Processbilder | `Settings_Process_Images` |
| Användare och behörigheter | `EditUsers` |
| Navigering | `Settings_Navigation` |
| Avancerade inställningar | `Debug` |

Några knappar kontrollerar dessutom en egen behörighet. De anges vid respektive
inställning nedan. Se [Användare och behörigheter](users-privileges.md#framework-privileges).

---

## Allmänna inställningar

**Applikationsnamn** — namnet på applikationen som visas i namnlisten.
Klicka på **Ändra Applikationsnamn** för att uppdatera det.

**WideQuick version** — visar den för tillfället installerade versionen av **WideQuick®**.
Skrivskyddat.

**Systeminfo** — visar anslutningsinformation för det aktuella systemet. Klicka
på **Visa Systeminfo** för att öppna dialogen, som visar server- och klient-Runtime-namn,
IP-adress och port.

**XXX version** — visar den för tillfället installerade konceptversionen av **WideQuick®**.
Skrivskyddat.

**Språk** — applikationens visningsspråk. Klicka på **Byt språk** för att byta
språk. Se [här](../../../mod/guides/languages.md) för mer information.

**Enheter** — det enhetssystem som används för visning av värden, till exempel SI. Klicka
på **Ändra Enhetssystem** för att växla mellan enhetssystem.

**Tid** — visar aktuellt systemdatum och -tid. Klicka på **Ändra tid** för att
justera den.

**Tema** — växlar mellan de tillgängliga applikationsteman, till exempel ljust
och mörkt läge.

**SMTP Inställningar** — konfigurerar den SMTP-server som används för att skicka e-postaviseringar.
Klicka på **Ändra** för att öppna konfigurationsdialogen. **Ändra** kräver `editSMTP`. Se
[Larm — Utöka](../Core/alarms/extending.md#email-notifications) för mer
information.

**Fjärrsystem** — hanterar anslutningar till fjärranslutna WideQuick Runtime-instanser. Klicka
på **Hantera fjärrsystem** för att lägga till eller konfigurera fjärrsystem. Se [här](../../../mod/guides/remote-systems.md) för mer
information.

**Anslutna klienter** — visar antalet för tillfället anslutna fjärrklienter.
Klicka på **Visa anslutna klienter** för att se en lista över aktiva anslutningar.

**Schema** — WideQuick:s inbyggda schemaläggningssystem, som startar konfigurerade
schemalagda uppgifter såsom rapportgenerering. Varje schema har sitt eget intervall. Bara
`ReportSchedules`, som letar efter rapporter som ska skapas, körs var 5:e minut. Klicka på **Ändra
Schema** för att konfigurera scheman. **Ändra Schema** kräver `Schedules`.

**Arkiverade anteckningar** — klicka på **Radera alla** för att permanent radera alla
arkiverade loggboksanteckningar, efter en bekräftelse. Kräver `Logbook_Delete`. Se
[Loggbok — Utöka](../logbook/extending.md#archiving).

---

## Processbilder

**Visa namnskyltar** — växlar huruvida objektens namnskyltar är synliga i processvyn.

**Visa dynTouch** — växlar huruvida `DynTouch`-objektgränser är synliga,
användbart för felsökning av objektplacering i **WideQuick® Designer**.

**Supportobjekt font storlek** — anger teckenstorleken för supportobjekt såsom värdevisningar.
Ange ett värde eller använd pilarna för att justera.

**Global decimal inställning** — anger antalet decimaler som visas för numeriska
värden i hela applikationen. Ange ett värde eller använd pilarna för att justera.

**Uppdateringsfrekvens värdevisare (ms)** — styr hur ofta värdevisningar
uppdateras, i millisekunder. Lägre värden uppdaterar oftare men kräver mer
bearbetning. Ange ett värde eller använd pilarna för att justera.

**Handsymbol** — den symbol som visas när ett objekt är i manuellt läge. Klicka
på **Ändra handsymbol** för att ändra den.

---

## Användare och behörigheter

**Användare** — visar den för tillfället inloggade användaren. Klicka på **Ändra användare** för att
växla till ett annat användarkonto. Se [här](users-privileges.md) för mer information.

**Lösenord** — klicka på **Ändra lösenord** för att ändra lösenordet för den aktuella
användaren.

**Kräv inloggning** — när aktiverat måste användare logga in innan de får tillgång till systemet.
När inaktiverat kringgås inloggningsskärmen och användaren går in som oautentiserad.
Se [Inloggningskonfigurationer](../../guides/Login%20Config/#require-login) för mer
information.

**Kräv användarnamn** — när aktiverat måste användare skriva sitt fullständiga användarnamn när
de loggar in. När inaktiverat visas istället en kombinationsruta med alla tillgängliga användare.
Se [Inloggningskonfigurationer](../../guides/Login%20Config/#require-username)
för mer information.

---

## Navigering

**Visa låsta menyknappar** — växlar huruvida menyalternativ som kräver en behörighet är
synliga för användare som saknar behörigheten. Se
[Navigering — Konfigurering](Navigation/configuring.md#setting-privilege-requirements-on-views)
för mer information.

**Visa låsta submenyknappar** — växlar huruvida undermenyalternativ som kräver en behörighet
är synliga för användare som saknar behörigheten. Se
[Navigering — Konfigurering](Navigation/configuring.md#setting-privilege-requirements-on-views)
för mer information.

**Fullskärmsmeny** — växlar huruvida navigationen körs i helskärmsläge.

**Direktnavigering (karta)** — när aktiverat navigerar ett klick på ett nålobjekt på en karta
direkt till dess länkade **Arbetsvy**. När inaktiverat visas först en informationspanel
som låter användaren välja om denne vill navigera. Se
[Kartor — Konfigurering](../maps/configuring.md#direct-navigation) för mer information.

---

## Avancerade inställningar

**Debuggträd** — klicka på **DebugTree** för att öppna objektträdet för den körande
applikationen, för att granska dess objekt vid felsökning.

**Konsol** — klicka på **Öppna konsol** för att öppna skriptkonsolen, som visar
skriptutdata och fel under körning.

**Aktivera debug log** — när aktiverat skrivs en detaljerad felsökningslogg till disk.
Användbart för att diagnostisera problem i produktionsmiljöer.

**GSM Modem** — konfigurerar det GSM-modem som används för SMS-larmaviseringar. Klicka
på **Ändra GSM inställningar** för att öppna konfigurationsdialogen. Se
[Larm — Utöka](alarms/extending.md#sms-notifications) för mer
information.

**Shutdown option** — visas bara på OE200-paneler. Klicka på **Open config** för att välja
vad som ska hända när WideQuick stängs ned. Kräver `Config`.

---

**Avsluta WideQuick** — knappen längst ned till höger i vyn stänger WideQuick,
efter en bekräftelse.
<!-- --8<-- [end:body-2] -->
