---
title: Skapa popup
product: mod
page_type: guide
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->
# Skapa popup
WideQuick Modular Framework levereras med flera förkonfigurerade popups, till exempel
historik, trend och underhåll. Det är också möjligt att skapa helt anpassade popups
anpassade till specifika objekt och arbetsflöden. Den här guiden förklarar hur man skapar
en anpassad popup från grunden — från att importera taggar och konfigurera suffix till
att bygga vyn och koppla den till ett objekt.

Innan du börjar, se till att du är bekant med taggstrukturen som används i
WideQuick Modular Framework. Om inte, se [Taggstruktur](../reference/tag-structure.md).

Det finns tre steg i att skapa en anpassad popup:

* Importera först de taggar som ska visas och styras i popupen. Se
[Importera taggar](#import-tags) för mer information.
* Konfigurera sedan suffixen för de nyligen importerade taggarna och koppla dem till
den specifika popupen. Se [Konfigurera popup](#configure-popup) för mer information.
* Skapa slutligen popup-vyn. Se [Bygg popup](#build-popup) för mer information.

I det här exemplet kommer vi att bygga en popup för pumpstyring. Pumpen kommer att kallas
`pump06`.


## Importera taggar { #import-tags }
Det första steget är att importera de taggar som ska visas och styras. Dessa taggar måste följa
taggstrukturen:

`Connection.Device.Sys_objectName_suffix`

Suffixet kan vara vad du vill, men kom ihåg det till nästa steg där popupen
konfigureras. Mer information om taggstruktur finns i
[Taggstruktur](../reference/tag-structure.md).

I det här exemplet importerar vi 5 taggar från PLC:n för att styra pumpen:

1. Den första taggen visar om pumpen är på eller av. Den ges suffixet
`_IO`. Detta är en skrivskyddad tagg i PLC:n.
2. Den andra taggen startar eller stoppar pumpen. Den ges suffixet `_start`.
Detta är en läs/skriv-tagg i PLC:n.
3. Den tredje taggen är börvärdet för pumpens varvtal. Den ges suffixet
`_setpoint`. Detta är en läs/skriv-tagg i PLC:n.
4. Den fjärde taggen är pumpens faktiska varvtal. Den ges suffixet `_rpm`.
Detta är en skrivskyddad tagg i PLC:n.
5. Den femte taggen är en felsignal, aktiv när pumpen har stött på ett fel.
Den ges suffixet `_error`. Detta är en skrivskyddad tagg i PLC:n.

![Importerade taggar](/docs/sv/Images/Create_Popup/tagList_popup.png)

!!! note "Återanvända taggar"
    En tagg kan visas på flera popups. Det är inte nödvändigt att importera samma
    tagg flera gånger.



## Konfigurera popup { #configure-popup }

När taggarna har importerats är nästa steg att konfigurera dem och koppla dem
till popupen. Detta görs i några steg:

* Starta projektet.
* Navigera till **Inställningar → Suffix → Suffix Alias - Popups**.

![Navigering till inställningar](/docs/sv/Images/Create_Popup/Navigation.gif){width="400"}

* Skapa en ny suffixkategori genom att trycka på **Lägg till ny kategori** och ge
den nya kategorin ett namn. Eftersom vi skapar en popup för pumpstyring, namnge den
**Pump Control**.

![Lägga till kategori](/docs/sv/Images/Create_Popup/Adding%20category.gif)

* Markera den nya kategorin i listan och klicka på **Lägg till nytt suffixalias i vald kategori**. I det här exemplet börjar vi med taggen med suffixet `_IO`, som visar
om pumpen är på eller inte. Namnge detta suffix **Active**.

![Lägga till suffix](/docs/sv/Images/Create_Popup/Adding%20suffix.gif)

* Fyll i relevant information för detta suffixalias:

![Konfigurera suffix](/docs/sv/Images/Create_Popup/suffix_config.png)

* **Suffix** — Suffixet som angetts på taggen, i det här fallet `_IO`.
* **Writable** — Lämna inaktiverat eftersom detta är en skrivskyddad tagg i PLC:n.
* **Write privilege** — Lämna tomt eftersom detta suffix inte är skrivbart.
* **Decimals** — Lämna som det är eftersom detta är en booleansk signal utan decimaler.
* **Unit** — Ange enheten för suffixet. Eftersom detta är en booleansk behövs ingen enhet.
* **Description** — En beskrivning av vad detta suffix representerar. Eftersom detta är en
statussignal, ange `On/Off signal`.

!!! tip "Specifik information per tagg"
    Det är möjligt att skriva över skrivprivilegiet, antalet decimaler och
    suffixbeskrivningen per tagg genom att ange informationen i taggbeskrivningen.
    Se [Taggstruktur](../reference/tag-structure.md) för mer information.

Upprepa dessa steg för de fyra återstående taggarna. I det här exemplet kommer suffixen att
namnges enligt följande:

* `_setpoint` — **Setpoint**
* `_rpm` — **RPM**
* `_error` — **Error**
* `_start` — **Start**

Den färdiga listan bör se ut ungefär så här:

![Konfigurerade suffix](/docs/sv/Images/Create_Popup/configured_suffixes.png)

## Välja popup-mall { #choosing-a-popup-template }

WideQuick Modular Framework inkluderar tre popup-mallstorlekar att välja mellan
beroende på popupens komplexitet och mängden innehåll som ska visas:

| Mall | Bredd | Använd när |
|---|---|---|
| **Template_Popup_Small** | 490px | Enkla popups med få rader |
| **Template_Popup_Medium** | 980px | Mer komplexa popups med mer innehåll |
| **Template_Popup_Large** | 1480px | Omfattande popups med maximalt innehåll |

Alla tre mallar finns under **Arbetsvyer → Templates**. Knapparna och layouten
skalas automatiskt med mallstorleken, så processen för att bygga en popup är
densamma oavsett vilken mall som väljs.

!!! tip
    När du är osäker, börja med **Template_Popup_Small**. Eftersom popups skalas
    automatiskt baserat på tillgängliga taggar räcker ofta en mindre mall
    och resulterar i en renare, mer fokuserad popup.


## Bygg popup { #build-popup }

Det sista steget är att bygga popup-vyn för att styra pumpen och visa
information.

Det finns två sätt att angripa detta — börja från en ny **Arbetsvy** eller kopiera en
befintlig mallvy. Det enklaste sättet är att börja med mallvyn,
som innehåller alla nödvändiga skript och konfigurationer. Kopiera **Arbetsvyn:**
**Template_Popup_Small** som finns under **Arbetsvyer → Templates** och namnge den nya
**Arbetsvyn:** **Pump Control**.

!!! note "Namngivning av popups"
    Popupen behöver inte heta samma sak som suffixgruppen som skapades i
    föregående steg. Detta är bara en tillfällighet i det här exemplet.

Vyn kan nu byggas med objekt från objektbiblioteket **CustomPopupObjects**.
Detta bibliotek innehåller objekt för att visa och styra taggar. Om en
tagg inte är tillgänglig för objektet som visar popupen, döljs objektet
automatiskt och popupen skalas om för att undvika tomt utrymme.

Börja med att lägga till ett objekt för att visa om pumpen har startats. Objektet
`StatusRow` är idealiskt för detta. Dra ett `StatusRow` in i vyn, markera det
och öppna fliken **Properties**. Ställ in egenskapen **SuffixAlias** till **Active** för att
koppla detta objekt till suffixet `_IO`:

![Statusrad](/docs/sv/Images/Create_Popup/StatusRow2.png)

!!! note "Suffix"
    **SuffixAlias** på **CustomPopupObjects** refererar till namnet som getts till
    suffixet i föregående steg, inte det faktiska suffixet. I det här exemplet, ange
    **Active** istället för `_IO`.

Lägg sedan till kontroller för att starta och stoppa pumpen med objektet `2Button_row`.
En knapp för start och en för stopp. I det här exemplet stoppar inställningen av `_start`
till `0` pumpen och inställningen till `1` startar den. Fyll i egenskaperna
därefter:

![2 knappar start](/docs/sv/Images/Create_Popup/2Button_start2.png)

Lägg sedan till en rad för att ställa in börvärdet och en annan för att visa det faktiska varvtalet
med objektet `ValueRow`. Detta objekt tillåter värdesinmatning om **Writable** var
aktiverat i föregående steg, annars visas värdet som skrivskyddat. Eftersom
**Writable** var aktiverat för börvärdet men inte för varvtalet, lägg till två `ValueRow`-objekt
och ställ in deras **SuffixAlias** till **Setpoint** respektive **RPM**.

Lägg slutligen till ett `StatusRow` för att visa om pumpen har stött på ett fel.
Den slutliga vyn bör se ut ungefär så här:

![Felrad](/docs/sv/Images/Create_Popup/Error.png)

Det sista steget är att ändra storlek på vyn för att ta bort tomt utrymme längst ned. Högerklicka
på vyn i projektträdet och välj **Properties**. Att ställa in höjden till
ungefär `520` säkerställer att alla objekt är synliga samtidigt som det tomma
utrymmet tas bort. Objektet `foreGroundBox2` behöver inte ändras i storlek eftersom det skalas om
automatiskt med vyn.

Starta applikationen och navigera till **Inställningar → Suffix → Suffix - Popups**.
Välj **Pump Control** och uppdatera **View** till den nyligen skapade vyn **Pump Control**
som visas nedan:

![Popup-konfiguration](/docs/sv/Images/Create_Popup/view_config.png)

Allt som återstår är att starta projektet och klicka på `pump06` för att se popupen **Pump Control**. Se [Skapa objekt](create-an-object.md) för att skapa ett objekt i en
**Arbetsvy**.

<div markdown style="display: flex; justify-content: center; align-items: center; gap: 1.5rem;">

![pump06](/docs/sv/Images/Create_Popup/pump06.png){style="height:500px;"}

![pump control](/docs/sv/Images/Create_Popup/pump%20control.png){style="height:500px;"}

</div>


## Automatisk skalning { #automatic-scaling }

Innehållet som visas för ett objekt är direkt kopplat till vilka signaler, taggar eller
variabler som är tillgängliga för det objektet. När en popup laddas skalas vyn
automatiskt om och alla rader i den anpassade popupen som inte är relevanta för
det länkade objektet döljs.

!!! note "Automatisk skalning"
    Mer information om automatisk skalning finns
    [här](automatic-scaling.md).

För att illustrera detta läggs en andra pump kallad `pump07` till. Denna pump har samma
signaler som `pump06` förutom att den inte har en feltagg (`_error`).

![pump07](/docs/sv/Images/Create_Popup/pump07_tags.png)

När `pump07` klickas på döljer popupen automatiskt felstatusraden
och skalas om för att ta bort det tomma utrymmet:

![pump control skalad](/docs/sv/Images/Create_Popup/Pump%20control_scaled.png)

På grund av denna funktion bör popups alltid byggas för att visa det maximala antalet
taggar — **värsta tänkbara** scenariot — och skalas sedan automatiskt om
beroende på det faktiska antalet tillgängliga taggar för objektet.

## Öppna en popup { #opening-a-popup }
Följande avsnitt täcker de två sätten en popup kan öppnas i WideQuick.
Öppningsmetoden bestäms av hur objektet `DynTouch` är konfigurerat i
**WideQuick Designer®**.

Det finns två sätt att öppna en popup i WideQuick, var och en med ett annorlunda visuellt
beteende:

* **`app.popOut`** — Öppnar popupen som ett sidofält i den aktuella vyn. Resten
av vyn skuggas, vilket håller användaren i sammanhang samtidigt som uppmärksamheten fokuseras på
popupen. Detta är standardbeteendet för de flesta inbyggda popups.

* **`view.link`** — Öppnar popupen som ett flytande fönster ovanpå den aktuella vyn,
liknande en traditionell dialog. Detta är användbart när popup-innehållet behöver mer
visuell separation från den underliggande vyn.

<div class="figure-row" markdown>

<figure markdown="span">
  ![view.link](/docs/sv/Images/Create_Popup/view.link.png)
  <figcaption>Använder view.link.</figcaption>
</figure>

<figure markdown="span">
  ![app.popOut](/docs/sv/Images/Create_Popup/app.popOut.png)
  <figcaption>Använder app.popOut.</figcaption>
</figure>


</div>



!!! tip
    Använd **`app.popOut`** för de flesta popups — det håller användaren orienterad i den
    aktuella vyn. Använd **`view.link`** när popup-innehållet är tillräckligt komplext för att
    motivera fullständig visuell separation från den underliggande vyn.

## Öppna en specifik popup direkt { #opening-a-specific-popup-directly }

Som standard öppnar ett klick på ett `DynTouch`-objekt fliknavigeringen först, vilket låter
användaren välja vilken popup som ska visas. I fall där användare ofta navigerar
till en specifik popup — till exempel **Maneuver** — är det möjligt att kringgå fliknavigeringen
och öppna den popupen direkt.

Detta görs genom att använda objekten `_DynTouch_DirectLink` eller `_DynTouchRounded_DirectLink`
istället för det vanliga `DynTouch`-objektet. Dessa finns i samma
objektbibliotek som det vanliga `DynTouch`-objektet.

För att konfigurera en direktlänk, ställ in egenskapen **startPopup** på objektet till
namnet på den popup som ska öppnas vid klick:

![DirectLink DynTouch](/docs/sv/Images/Create_Popup/Direct_Link_prop.png)

!!! tip
    Använd `_DynTouch_DirectLink` när användare ofta navigerar till en specifik popup-flik.
    Detta sparar ett extra klick och förbättrar arbetsflödet för operatörer som
    regelbundet interagerar med samma popup.


<!-- --8<-- [end:body] -->
