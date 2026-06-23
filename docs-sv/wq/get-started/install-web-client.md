---
title: Installera WideQuick Web Client
product: wq
page_type: getstarted
status: draft
last_reviewed: 2026-06-16
tags:
 - WQ
---

# Installera WideQuick Web Client

## WideQuick® Web Client Config Tool

Sedan **WideQuick** version 8 levereras webbklienten med ett grafiskt verktyg för
att konfigurera `.ini`-filen som installeras tillsammans med webbklienten. Verktyget
tillhandahåller ett grafiskt gränssnitt för att redigera alla inställningar i
`.ini`-filen.

![WideQuick Web Client Config Tool – Web server](/docs/sv/Images/install_wq/wqWebClientConfigTool.png)

### Arkiv-menyn

* **Ny** — skapar en ny konfiguration
* **Öppna** — öppnar en befintlig konfiguration
* **Spara** — sparar den aktuella konfigurationen
* **Spara som...** — sparar en kopia av den aktuella konfigurationen

!!! note
    Om konfigurationsfilen kräver förhöjda behörigheter för att sparas kan en
    UAC-dialog visas.

* **Avsluta** — avslutar programmet

### Inställningar-menyn

* **Lagra relativa sökvägar** — när aktiverat konverteras alla sökvägar i
konfigurationen till relativa sökvägar, relativt platsen för konfigurationsfilen
* **Starta om tjänst** — startar om tjänsten **WideQuick Web Client**. Endast
tillgänglig i Windows när den inlästa konfigurationen används av tjänsten. Tjänsten
måste startas om efter varje konfigurationsändring för att ändringarna ska träda
i kraft.

---

## Fliken Webbserver

Fliken **Webbserver** innehåller initialiseringsvärdena för **WideQuick® Web
Client**, lagrade i avsnittet `[web-server]` i `.ini`-filen.

* **Http-address** — den IP-adress som **WideQuick® Web Client** lyssnar på.
Standardvärdet är `0.0.0.0`, vilket motsvarar alla tillgängliga IP-adresser på
datorn. Om detta sätts till `127.0.0.1` eller `localhost` blir servern otillgänglig
för andra datorer i nätverket.

* **Http-port** — den HTTP-port som används för inkommande anslutningar. Om fältet
lämnas tomt används port `80` för HTTP-anslutningar och `443` för HTTPS-anslutningar.

* **Console** — när aktiverat körs **WideQuick® Web Client** med ett synligt
konsollfönster för felsökning.

* **Threading** — styr trådningsmodellen. `free` tillåter webbklienten att skapa
så många trådar som behövs. `strict` använder ett fast antal trådar under hela
processens körning.

* **docroot** — katalogen för webbklientens resurser. Standardvärdet är `./data`.
Ändra detta om du vill använda anpassade resurser.

* **error_root** — katalogen som innehåller anpassade felsidor (`.html`).
Standardvärdet är `.` för att visa de inbyggda standardfelsidorna. För att lägga
till en anpassad felsida, placera filer med följande namn i den angivna katalogen:

```{ .txt .no-copy title="error_root catalogue" }
.
├─ 200-ok.html
├─ 201-created.html
├─ 202-accepted.html
├─ 204-nocontent.html
├─ 300-multiple-choices.html
├─ 301-moved-permanently.html
├─ 302-found.html
├─ 303-see-other.html
├─ 304-not-modified.html
├─ 307-moved-temporarily.html
├─ 400-bad-request.html
├─ 401-unauthorized.html
├─ 403-forbidden.html
├─ 404-not-found.html
├─ 413-request-entity-too-large.html
├─ 500-internal-server-error.html
├─ 501-not-implemented.html
├─ 502-bad-gateway.html
└─ 503-service-unavailable.html
```

För en specifikation av HTTP-felkoder, se
[www.w3schools.com/tags/ref_httpmessages](http://www.w3schools.com/tags/ref_httpmessages.asp){target="_blank"}.

* **use_https** — när aktiverat använder webbservern HTTPS för alla anslutningar.

!!! note
    Om **use_https** är aktiverat måste `ssl_certificate`, `ssl_private_key` och
    `ssl_temp_dh` alla anges, annars kan servern inte starta.

* **ssl_certificate** — det SSL-certifikat som används för säker kommunikation.
Krävs endast när **use_https** är aktiverat.

* **ssl_private_key** — den privata servernyckeln som används för säker kommunikation.
Krävs endast när **use_https** är aktiverat.

* **ssl_temp_dh** — de slumpmässiga Diffie-Hellman-parametrarna som används för
säkert nyckelutbyte. Krävs endast när **use_https** är aktiverat.

---

## Fliken WideQuick® Runtime Server

Fliken **WideQuick® Runtime Server** konfigurerar de **WideQuick® Runtime**-instanser
som **WideQuick® Web Client** kan ansluta till, lagrade i avsnittet `[wqre-server]`
i `.ini`-filen.

![WideQuick Web Client Config Tool – WideQuick® Runtime Server](/docs/sv/Images/install_wq/wqWebRuntimeServer.png)

* **Name** — serverns namn. Kan användas som ett URL-argument, till exempel ansluter
`localhost/?wqruntime=server1` till servern med namnet `server1`. Alla icke-standardservrar
lagras under sin egen `[name]`-nod i `.ini`-filen.

* **Hostname** — IP-adressen till datorn som kör **WideQuick® Runtime**.
`127.0.0.1` innebär att **WideQuick® Runtime** och **WideQuick® Web Client** körs
på samma maskin.

* **Port** — anslutningsporten som angetts för visningsåtkomst i
**WideQuick®**-projektegenskaperna.

* **Cache size** — storleken på filcachen i MB. Ange `0` för att inaktivera
cachning helt.

* **Workview** — den arbetsvy som visas vid anslutning via en webbläsare. Lämna
tomt för att använda startvyn som angetts i **WideQuick® Runtime**-projektet.

* **Workviews** — lista över arbetsvyer som kan användas som URL-argument, till
exempel `localhost/?view=Workview2.kvie`. Separerade med mellanslag, lagrade som
`view_args` i `.ini`-filen.

* **Export variables** — lista över variabler som exponeras via URL:en, till
exempel `localhost/?export_var1=11&export_var2=22`. Separerade med mellanslag,
lagrade som `export_vars` i `.ini`-filen.

---

## Fliken WideQuick® Web Client

Fliken **WideQuick® Web Client** konfigurerar uppdaterings- och synkroniseringsfrekvenser,
lagrade i avsnittet `[wqweb]` i `.ini`-filen.

![WideQuick Web Client Config Tool – WideQuick® Web Client](/docs/sv/Images/install_wq/wqWebConfigWebClient.png)

* **refreshrate** — hur ofta **WideQuick® Web Client** synkroniserar data med
**WideQuick® Runtime**.

* **gfxupdaterate** — hur ofta **WideQuick® Web Client** uppdaterar det grafiska
gränssnittet i webbläsaren.

* **Max reconnect attempts** — det maximala antalet återanslutningsförsök. Ange
`0` för att inaktivera återanslutning. Ange `-1` för att försöka på obestämd tid.

* **Reconnect delay** — hur många sekunder som ska väntas mellan återanslutningsförsök.

* **File path** — katalogen där loggfiler lagras.
**WideQuick® Web Client** kräver skrivbehörighet till den här mappen.

* **Error, warning and debug** — växlar för vilka loggnivåer som skrivs till
loggfilen.

---

## Konfigurera .ini-filen manuellt

`.ini`-filen kan också redigeras manuellt med en textredigerare med administrativa
rättigheter. Standardfilens plats är:

* **Windows (64-bit)** — `C:\Program Files (x86)\Kentima AB\WideQuick Web Client`
* **Debian** — `/etc/wqweb/`

Standardinnehållet i `wqweb.ini` efter installation:

```{.ini title="wqweb.ini"}
[web-server]
http-address=127.0.0.1
http-port=80
docroot=.
error_root=.
console=true
use_https=false
ssl_certificate=cert.pem
ssl_private_key=server.key
ssl_temp_dh=dh2048.pem
[wqre-server]
hostname=127.0.0.1
port=2122
workview=
view_args=
export_vars=
[wqweb]
refreshrate=250
gfxupdaterate=250
[logger]
filepath=C:/ProgramData/Kentima AB/WQWebClient/Log
error=true
warning=true
debug=true
```

---

## Konfigurera WideQuick®-projektet

För att **WideQuick® Web Client** ska kunna ansluta till ett projekt måste projektet
konfigureras på samma sätt som för **WideQuick® Remote Client**.

### Visningsåtkomst

Projektet måste ha en aktiv port för visningsåtkomst som anger TCP/IP-porten för
kommunikation mellan **WideQuick® Runtime** och **WideQuick® Web Client**.
Porten konfigureras i projektegenskaperna, till exempel port `2122`.

### Läs- och skrivåtkomst till Datalager-variabler

För alla variabler och larm vars värden ska överföras till eller från klienten
måste visningsåtkomsten ställas in på **Läs** och/eller **Skriv** efter behov.

### Startvy

Vilken vy som helst i ett projekt kan ställas in som startvy för **WideQuick® Web Client**,
oberoende av startvyn för **WideQuick® Runtime**. Alla andra fönster är
undervyer till huvudvyn och stängs automatiskt när deras överordnade stängs.

För att ange en startvy för webbklienten, högerklicka på valfri vy och välj
**Ange som startvy för WQWeb**.

---

## Ansluta med en webbläsare

När **WideQuick® Web Client**, **WideQuick® Runtime**-projektet och webbservern
är konfigurerade kan projektet visas i valfri webbläsare utan att installera
några ytterligare insticksprogram.

URL-formatet är: http://ServerName:ConnectionPort

Där `ServerName` är webbserverns IP-adress, datornamn eller fullständig URL.

---

## Egenskaper som stöds

**Variabler och datatyper** — alla variabeltyper stöds.

**Dynamik** — alla former av dynamik stöds, med vissa undantag. Se
[Egenskaper som inte stöds](#egenskaper-som-inte-stods) för detaljer.

**Arbetsvyer** — den vy som anges i konfigurationsfilen visas vid anslutning.
Navigation är sedan möjlig via funktionen `link()` eller en multiviewer.

**Grupper och instanser** — fullt stöd för grupper och instanser.

**Databasanslutningar** — virtuella databaser stöds.

**Fjärrsystem** — stöds, inklusive information hämtad från flera fjärrsystem,
`linkRemote()`-funktionalitet och konfiguration av fjärrsystem i multiviewern.

**Användare och behörigheter** — användare kan logga in och ut, byta lösenord
och redigera användare via skript och dialoger.

**Språk** — översättning av både projekt och applikation stöds.

**Skript** — de flesta skriptfunktioner stöds. Se
[Egenskaper som inte stöds](#egenskaper-som-inte-stods) för undantag.

**EthirisView** — fullt stöd.

**History-objekt** — stöds som ett avancerat analytiskt verktyg för att studera
enskilda signaler eller deras inbördes relationer över en eller flera loggenheter.

**E-post** — e-postsystemet stöds. E-post skickas från den server som
**WideQuick® Web Client** är ansluten till.

Följande objekt stöds till största delen, med viss funktionalitet som saknas:

* Alarm – Blockeringslista
* Alarm – Frekvenslista
* Alarm – Lista
* Alarm – Logg
* Alarm – Rad
* Arch
* Bar Chart 2
* Box
* Button – tillfällig (visar inte unik text när den klickas)
* Check box
* Combo box (ej redigerbar)
* Custom Button
* Custom Spin box
* Datetime Edit
* Ellipse
* EthirisView
* Event List 2
* History
* History2
* HTML
* Image
* Line
* Line Chart 2
* Map View
* Multiviewer
* Object list
* Polygon
* Radio button
* Report view
* Slider
* Spin box
* Table
* Text
* Text box
* Trend
* Triangle
* Tree view

---

## Egenskaper som inte stöds

### Dynamik

Följande dynamiska egenskap stöds inte:

* Flytta arbetsvyer till förgrunden

### Arbetsvyer

**WideQuick® Web Client** visar inga menyer i arbetsvyer.

### Objekt

Vissa delade egenskaper stöds inte av **WideQuick® Web Client** för något objekt:

* Andra ramar än solid eller ingen
* Teckensnitt stöder inte genomstrykning eller understrykning
* Om webbläsaren inte har tillgång till det angivna teckensnittet används ett
liknande teckensnitt istället

!!! note
    För att säkerställa att projektet ser så likt ut som möjligt bör endast
    teckensnitt med god webbsupport väljas om projektet är avsett att användas med
    **WideQuick® Web Client**.

Följande objekt stöds inte via **WideQuick® Web Client**:

* ActiveX
* Bar Chart
* Camera
* Combo box (redigerbar)
* Event list
* Gauge
* Knob
* Line Chart
* Tab

!!! note
    Tabbindex för objektnavigering stöds inte.

### Enhetssystem

**WideQuick® Web Client** stöder inte enhetsomvandlingar.

### Skript

Följande funktioner stöds inte av **WideQuick® Web Client**:

* **Bitmap-objekt** — `print()`
* **COMObject-objekt**
* **Debugger-objekt**
* **File-objekt**
* **Kör externt program**
* **Messenger-objekt**
* **Process-objekt**
* **SerialPort-objekt**
* **UnitSystemCollection-objekt**
* **Arbetsvy-objekt** — följande funktioner stöds inte:
    * `grab()`
    * `print()`
    * `translate()`
    * `mapTo()`
    * `mapFrom()`
    * `mapToScreen()`
    * `mapFromScreen()`
