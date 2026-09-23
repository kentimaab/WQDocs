# Skicka SMS med Teltonika – Översikt

!!! info "Licenskrav"
    Användning av pluginet kräver en Advance-licens med optionen .NET-plugin, eller en Premium-licens.

!!! warning "Linux"
    Teltonika-pluginet fungerar endast för Windows OS

Med hjälp av ett .NET-plugin kan WideQuick skicka SMS direkt från systemet, utan mellanliggande tjänster eller externa SMS-gateways. Pluginet kommunicerar med en Teltonika-router via dess inbyggda REST API och skickar SMS genom det mobilnät som routern är ansluten till.

## Varför skicka SMS från WideQuick?

E-post och larmklienter fungerar bra så länge någon aktivt bevakar dem, men ett SMS når fram direkt till mobilen även när ingen sitter framför en HMI eller är inloggad i systemet. Det gör SMS särskilt värdefullt för SCADA- och HMI-tillämpningar, där en snabb reaktion på en processavvikelse kan förhindra driftstopp, skador eller ett regelbrott, till exempel:

- **Ett kritiskt processlarm går aktivt** – operatörer, underhållspersonal eller jourhavande ingenjörer får omedelbar notis om ett hög-/lågnivålarm, tryck-, temperatur- eller annat kritiskt processlarm, oavsett var de befinner sig.
- **En obemannad eller avlägsen anläggning behöver uppmärksamhet utanför kontorstid** – ett SMS skickas direkt om ett kritiskt larm inträffar kvällar, nätter eller helger, när ingen operatör bevakar HMI:n.
- **Eskalering av olösta larm** – om ett larm förblir aktivt längre än förväntat kan ett uppföljande SMS skickas till en sekundär kontakt eller jourhavande ingenjör.
- **Utrustnings- eller kommunikationsproblem** – SMS vid till exempel ett pump- eller motorfel, förlorad kommunikation med en PLC eller RTU, fullt lagringsutrymme eller andra tekniska avvikelser som kräver snabb åtgärd.

Eftersom SMS skickas via routerns eget mobilnätsabonnemang är lösningen dessutom oberoende av anläggningens internetuppkoppling, vilket gör den robust vid nätverksstörningar där e-postbaserade notifieringar annars skulle utebli – särskilt värdefullt för avlägsna pumpstationer, reningsverk och andra obemannade anläggningar.

## Vilka Teltonika-routrar stöds?

Pluginet fungerar med Teltonika-routrar som kör RutOS och som exponerar Web API / REST API. För att använda API:et krävs följande lägsta firmwareversion:

| Routerfamilj | Lägsta firmwareversion |
|--------------|-------------------------|
| RUT2, RUT9, RUTM, RUTC, TRB och övriga familjer | 7.15 eller senare |
| RUTX-familjen | 7.12 eller senare |

Funktionen för att skicka SMS ligger under **Mobile Utilities**, ett inbyggt gränssnitt i RutOS som finns med på alla Teltonikas mobila routrar (RUT-, RUTX- och TRB-serierna) – det är alltså inget separat paket som behöver installeras via Package Manager, utan en standardfunktion så länge firmwarekravet ovan är uppfyllt.
