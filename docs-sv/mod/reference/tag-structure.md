---
title: Taggstruktur
product: mod
page_type: reference
status: draft
last_reviewed: 2026-06-16
tags:
 - MOD
---

<!-- --8<-- [start:body] -->

# Taggstruktur

WideQuick Modular Framework använder en flexibel taggstruktur för att förenkla konfigurationen
och minska time to market för WideQuick-applikationer. Taggstrukturen gör det möjligt
att ansluta ett stort antal taggar till ett objekt utan att manuellt behöva ansluta
varje tagg till objektet.

Denna enkelhet gör det också lätt att importera ett stort antal taggar och automatiskt
ansluta dem till objekt, vilket gör det enkelt att utöka och modifiera befintliga
projekt.

För att en tagg ska följa taggstrukturen i WideQuick måste den
bestå av följande fem delar:

* **Connection**
* **Device**
* **System**
* **Object name**
* **Suffix**

!!! tip
    Om du är osäker på om ditt variabelnamn är korrekt kan du använda textfältet
    nedan för att bekräfta det. Det blir grönt när namnet är korrekt.

    <div class="tag-validator">
        <input type="text" id="tagInput" placeholder="Enter your tag">
        <p id="feedback" class="hidden">✅ Variable name is valid!</p>
    </div>

Se bilden nedan:

![tag structure](/docs/sv/Images/Tag_Structure/tagStruct.svg){style="box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.5);"}

### Connection { #connection }
**Connection** representerar anslutningstypen, till exempel **Modbus**, **OPC**, eller
märke och modell på PLC:n, exempelvis **Siemens** eller **SAIA**.

### Device { #device }
**Device** representerar ett elskåp, till exempel `AS01` eller liknande.

### System { #system }
**System** representerar vilket system taggen tillhör, till exempel `LB01`, `Intake`
eller `Outlet`.

### Object name { #object-name }
**Object name** representerar namnet på själva objektet, till exempel en temperatursensor
`GT11`, en motor `M01` eller en pump `P23`.

### Suffix { #suffix }
**Suffix** representerar vilken typ av signal taggen representerar, till exempel ett
mätvärde, ett börvärde eller en statusindikator.

!!! note "Namnge taggar"
    Det här är bara exempel — taggar kan namnges fritt så länge de följer
    strukturen `Connection.Device.Sys_Component_Suffix`.

!!! example "Exempeltaggar"
    `Skane.Kallby.AS01_pump07_IO`

    `Kentima.Staffanstrop.Skap03_GT11_MV`

    `Modbus.AS01.Kallby_Motor01_LG`



## Konfigurera taggar i OPC DA & OPC UA { #configuring-tags-in-opc-da-opc-ua }
Att konfigurera **OPC**-taggar så att de följer standarden är enkelt. Taggarna behöver
helt enkelt namnges enligt strukturen.

![OPC tag structure](/docs/sv/Images/Tag_Structure/tagStructure_OPC.png)


## Konfigurera taggar i Modbus Serial & Modbus TCP/IP { #configuring-tags-in-modbus-serial-modbus-tcpip }
**Modbus**-taggar ska också följa samma taggstruktur. Dock hämtas både
**Connection**- och **Device**-delen från anslutningsnamnet respektive enhetsnamnet
enligt bilden nedan. Det innebär att taggen i **Tag Editor** bara
behöver innehålla `Sys_Component_Suffix`.

![Modbus tag structure](/docs/sv/Images/Tag_Structure/tagStructure_MB.png)



## Ansluta objekt till taggar { #connecting-objects-to-tags }

Innan taggar ansluts till ett objekt måste objektet först skapas.
[Läs om Skapa objekt här](../guides/create-an-object.md)

När ett objekt har skapats behöver `DynTouch`-objektet anslutas till taggarna.
Det görs genom att ange tagginformationen i egenskaperna för `DynTouch`-objektet,
enligt bilden nedan. På så sätt kan WideQuick automatiskt hitta alla
taggar som är anslutna till objektet.

![Configuring DynTouch](/docs/sv/Images/Tag_Structure/DynTouch.png)

För att snabba upp processen att ansluta flera objekt till sina taggar behöver man inte
ange samma **Connection**-, **Device**- och **System**-information på varje objekt i
vyn. Dessa egenskaper kan i stället anges på **Arbetsvy**-egenskaperna. Om ett
`DynTouch`-objekt lämnas tomt försöker det hämta informationen från vyn i stället.

![Tag structure view](/docs/sv/Images/Tag_Structure/tagStructure%20view.png)

!!! tip "Objektnamn"
    Det är möjligt att hoppa över att ange objektnamnet på `DynTouch`-objektet genom
    att namnge objektet till objektnamnet.
    ![object name](/docs/sv/Images/Tag_Structure/Object%20name.png)

## Suffixalias { #suffix-alias }

Suffixaliassystemet gör det möjligt att mappa suffix till läsbara aliasnamn,
som används för att automatiskt ansluta signaler till rätt visningselement på
objekt. Detta eliminerar behovet av att manuellt tilldela signaler till enskilda objekt
och gör det enkelt att anpassa sig till olika taggnamnskonventioner i hela systemet.

Detta mönster gäller för alla dynamiska objekt i standardobjektbiblioteken —
deras värdesvisningselement är namngivna för att matcha suffixaliaslistan, vilket möjliggör
automatisk signaltilldelning när ett objekt ansluts till en tagg.

Till exempel har objektet `analogDamper` i objektbiblioteket **Dampers** ett
visningselement som heter `analogOutputValue`. Om suffixet `_R` mappas till aliaset
`analogOutputValue` kommer WideQuick automatiskt att tilldela alla signaler som slutar på `_R` till
det visningselementet när objektet ansluts till en tagg.

Det innebär också att om ett projekt använder en annan suffixkonvention — till exempel
`_R2` i stället för `_R` — behöver integratören bara uppdatera aliaset en gång och ändringen
tillämpas på alla objekt i systemet.

### Konfigurera suffixalias { #configuring-suffix-aliases }

Suffixalias konfigureras i **WideQuick® Runtime** genom att navigera till
**Inställningar → Suffix → Suffix Alias - Arbetsvyer**.

![Suffix settings](/docs/sv/Images/Tag_Structure/SuffixAlias_Procces.png)

Varje suffixalias har följande inställningar:

* **Suffix** — Det faktiska taggsuffixet som ska mappas, till exempel `_R` eller `_E`.
* **Enhet** — Den enhet som visas bredvid värdet, till exempel `kWh` eller `°C`.
* **Decimaler** — Antalet decimaler som visas för värdet.
* **Beskrivning** — En läsbar beskrivning av vad suffixet representerar.

Inställningarna för **Enhet**, **Decimaler** och **Beskrivning** tillämpas systemövergripande på
alla visningselement som är anslutna till en signal med det suffixet.

!!! note
    Liknande aliassystem finns för objektanimationer och popuper. Se
    [Arbetsvy Animations](../guides/workview-animations.md) och [Popups](Popup/index.md) för mer information.

## Specialegenskaper på taggar { #special-properties-on-tags }
Det är möjligt att definiera taggspecifika egenskaper och beskrivningar för en tagg, vilket
åsidosätter de regler som anges för taggen i popuper och andra objekt. Se
[Skapa popup](../guides/create-a-popup.md) för mer information.

Det görs genom att ange specifika värden i beskrivningsfältet för taggen i
**Tag Editor**.

Följande värden kan åsidosättas:

* **Beskrivning** — Anges genom att skriva taggbeskrivningen i fältet **Beskrivning**
i **Tag Editor** fram till det första semikolonet (`;`).
* **Decimaler** — Anges genom att skriva `DECIMAL=X;` där `X` representerar antalet
decimaler som ska visas.
* **Skrivrättighet** — Anges genom att skriva `PRIV=privilege;` där `privilege` representerar
en rättighet i användarsystemet.

Exemplet nedan anger beskrivningen "Börvärde" med 2 decimaler och
kräver rättigheten "Config" för att kunna redigera:

![tag desc](/docs/sv/Images/Tag_Structure/tagDesc.png)

!!! warning
    Taggen måste innehålla en beskrivning för att åsidosättningen ska fungera. Det går inte
    att skriva enbart `DECIMAL=3;` utan att även ange en beskrivning.
