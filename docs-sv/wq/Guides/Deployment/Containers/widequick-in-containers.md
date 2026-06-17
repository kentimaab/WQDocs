---
title: WideQuick i containrar
product: wq
page_type: overview
status: draft
last_reviewed: 2026-06-16
tags:
 - WQ
---

# WideQuick i containrar

![WQContainerintro](/assets/Images/WQContainers.png)


## Introduktion

Om du någonsin har brottats med att driftsätta flera HMI:er eller hantera SCADA över flera anläggningar vet du hur snabbt det kan bli komplicerat. Tänk om det fanns ett sätt att förenkla driftsättningen, minska huvudvärken och göra dina system mer skalbara – och samtidigt spara resurser? Svaret är **containrar**.

I den här guiden utforskar vi hur körning av WideQuick i containrar kan förändra dina automationsprojekt, oavsett om du hanterar byggnadsautomation eller stora industrianläggningar. Redo att framtidssäkra dina HMI/SCADA-driftsättningar?

!!! Note "Vem är den här guiden för?"

    - Automationsingenjörer som hanterar HMI/SCADA-system inom industri eller byggnadsautomation.
    - Systemintegratörer som driftsätter och underhåller automationsprojekt med flera anläggningar eller i stor skala.
    - IT-administratörer som stöder containermiljöer för industriell programvara.




## Vad är programvarucontainrar?

Tänk på en container som en **portabel, självständig låda** som innehåller allt din programvara behöver för att köra – förutom operativsystemet självt. Till skillnad från skrymmande virtuella maskiner som har sitt eget OS delar containrar värddatorns OS, vilket gör dem lätta och blixtsnabba.

Varför spelar det roll för dig? Därför att containrar låter dig köra flera WideQuick-instanser sida vid sida utan att behöva oroa dig för konflikter eller slösade resurser. Det är som att ha flera mini-servrar inuti en eller flera fysiska maskiner, var och en perfekt isolerad och redo att köra.

Det finns många fördelar med att köra i en container, bland annat:

- **Isolering:** Varje container körs i sitt eget isolerade utrymme och minimerar konflikter.
- **Portabilitet:** Containrar kan köras konsekvent på olika hårdvara och i olika miljöer.
- **Effektivitet:** Lägre overhead jämfört med fullständiga virtuella maskiner.

## Varför bör du containerisera WideQuick?

### Kör fler HMI:er, använd mindre hårdvara

**Tänk dig följande**: Du har i uppdrag att driftsätta dussintals HMI:er i ett stort byggnadskomplex eller på flera industrianläggningar. Traditionellt sett skulle du antingen dedikera en separat industri-PC eller panel till varje HMI, eller sätta upp en virtuell maskin för varje instans. Även om detta tillvägagångssätt fungerar, blir det snabbt ineffektivt och svårt att skala när man hanterar en stor HMI-flotta – särskilt när den är utspridd över stora geografiska områden eller staplad i komplexa virtuella miljöer.

Med containrar kan du bryta dig fri från dessa gamla begränsningar. Istället för att binda upp hårdvara eller stapla VM:ar kan du köra flera WideQuick-instanser på en enda server, var och en i sin egen isolerade container. Det minskar hårdvarukostnaderna, sänker energiförbrukningen och effektiviserar hela driftsättningen.

- Vill du skala upp? Starta bara en container till.

- Behöver du uppdatera? Byt ut imagen och starta om.

Det är ett smartare och snålare sätt att leverera robusta HMI/SCADA-lösningar för modern byggnadsförvaltning och industriautomation.



### Uppdateringar som inte saktar ner dig

När en ny version av WideQuick släpps innebar uppdateringar tidigare att du behövde hantera installationer på varje maskin. Med containrar är det lika enkelt som att byta ut containerimageen och starta om. Klart! Varje instans är uppdaterad på några minuter.

- Uppdatera alla WideQuick-instanser genom att helt enkelt uppdatera containerimageen och starta om containrarna.
- Återgå snabbt till tidigare versioner vid behov.

### Konsekvens du kan lita på

Att driftsätta programvara i olika miljöer leder ofta till svåra buggar och saknade beroenden.
Containrar säkerställer att din WideQuick-installation körs exakt likadant överallt – på din laptop, din server eller i molnet.

- Eliminera problemet med "det fungerar på min maskin" genom att säkerställa att varje driftsättning är identisk.
- Minska felsökningstid orsakad av saknade beroenden eller konfigurationsskillnader.

### Skala upp eller ner efter behov

Behöver du lägga till fler HMI:er för en ny anläggning eller ett nytt projekt? Starta bara fler containrar. Behöver du färre? Stäng av några. Det är automationsdriftsättning med den flexibilitet du alltid velat ha.

- Containrar använder mindre minne och CPU än traditionella virtuella maskiner, vilket låter dig maximera hårdvaruutnyttjandet.

## Verkliga användningsfall

- **Byggnadsförvaltningssystem:** Kör en dedikerad WideQuick-container för varje byggnad, allt centralt hanterat med lätthet.
- **Stora industrianläggningar:** Driftsätt flera HMI:er på delade servrar, vilket minskar hårdvarubehovet och förenklar underhållet.
- **Verksamhet på flera anläggningar:** Standardisera dina HMI-driftsättningar på alla platser för att säkerställa konsekventa uppdateringar och prestanda.

## Kom igång: Din första WideQuick-container

### Steg 1: Installera Docker
[Ladda ner Docker](https://docs.docker.com/get-started/get-docker/){.md-button .md-button--secondary target="_blank"}

Docker är din ingång till containermagin. Docker Desktop är ett enkelt och heltäckande sätt att komma igång med containrar på Windows. Det innehåller allt du behöver, inklusive Docker-motorn, kommandoradsverktyg och ett användarvänligt gränssnitt – så att du kan bygga, köra och hantera containrar direkt från skrivbordet. För automationsingenjörer och systemintegratörer innebär det att du inte behöver oroa dig för manuell installation eller kompatibilitetsproblem: Docker Desktop tar hand om allt det tunga arbetet.

När du arbetar med WideQuick är det viktigt att köra containrar i Windows-containerläge, eftersom körning av WideQuick i en container för närvarande kräver en Windows-miljö. Docker Desktop låter dig växla mellan Linux- och Windows-containrar med ett enda klick, vilket säkerställer att dina WideQuick-instanser körs smidigt och nativamente på ditt system.


Ladda ner och installera Docker Desktop för Windows och växla sedan till Windows-containerläge.


![Switch to Windows](/assets/Images/SwitchToWindows.png)


### Steg 2: Hämta din/dina WideQuick-image(ar)

!!! Note "Vad är en containerimage?"

    Tänk på en image som en "ritning" – ett färdigt paket med allt som behövs för att köra din WideQuick-applikation, som programvara, bibliotek och inställningar. Det är som att ha en optimerad miljö för att köra WideQuick!

    Du kan dock inte köra imagen direkt – du använder imagen för att **starta en container**. Containern är den levande, fungerande versionen. En image, många containrar. Vill du köra mer än en HMI eller SCADA på samma server? Du kan starta flera containrar från samma image!

När du söker efter "Kentima" på Docker Hub via Docker Desktop får du tillgång till världens största bibliotek med färdiga containerimager. Vi är värd för våra WideQuick-containerimager i ett **publikt arkiv** på Docker Hub, vilket gör det enkelt för alla i gemenskapen att komma åt och driftsätta dem. Docker Hub fungerar som ett centralt "bibliotek" för containerimager, där organisationer som Kentima kan publicera officiella och aktuella imager som alla kan använda.

Genom att använda Docker Hub som vårt officiella arkiv får du:

- **Omedelbar åtkomst:** Hitta de senaste WideQuick-imagerna på sekunder! Inget behov av att leta efter installationsfiler eller oroa dig för inaktuella filer.
- **Trygghet:** Alla imager är verifierade och underhållna, så du vet att du får rätt produkt direkt från källan.
- **Uppdateringar med ett klick:** Behöver du en ny version? Hämta bara den uppdaterade imagen. Inga komplexa uppgraderingsskript eller manuella nedladdningar.
- **Teamsamarbete:** Alla i ditt team kan hämta samma image och säkerställa konsekvens i alla dina driftsättningar.

Kort sagt säkerställer vårt publika Docker Hub-arkiv att du snabbt och tryggt kan komma igång med WideQuick-containrar, utan hinder mellan dig och ditt nästa automationsprojekt.


#### Steg att följa

![Pull image from Dockerhub](/assets/Images/pullimage.gif){width=800}

- Sök efter "Kentima" på Docker Hub i Docker Desktop.
- Du hittar imager för WideQuick Runtime och WideQuick Web Client.
- Hämta den image du behöver.

### Steg 3: Licensiera rätt

Innan du kan starta din nya WideQuick-container behöver du en **universell licensnyckel**. Tänk på den som ditt allroundkort för att köra WideQuick i en modern containermiljö. För att få en nyckel kontaktar du vårt säljteam så ordnar de det. Du hittar kontaktinformation [här](https://www.kentima.com/sv-SE/Kontakt)

Den universella licensen är utformad för att fungera sömlöst med containrar och göra din driftsättningsprocess smidig och flexibel.

#### Så här fungerar det:

- **Skaffa din universella produktnyckel:** Det här är din huvudnyckel för containerdriftsättningar.
- **Generera en licensnyckel:** Använd din universella produktnyckel för att skapa en unik licensnyckel för ditt specifika WideQuick-projekt.
- **Lägg till nyckeln i ditt projekt:** Placera projektnyckeln i din WideQuick-projektmapp, som innehåller dina projektfiler.
- **Starta din container:** Nu är du redo att köra – din WideQuick-instans startar, och när containern ansluter till licensservern körs en fullt licensierad applikation redo för användning.

Med den universella licensen kan du starta, flytta eller skala WideQuick-containrar med tillförsikt. Oavsett om du kör en HMI eller hundra på dina anläggningar!

!!! Note
    Alla versioner 13.4 och senare stöder universella licensnycklar och fungerar utmärkt med containrar!

### Steg 4: Kör containern
![Run a container](/assets/Images/RunNewContainer.png)


- Starta containern från imagen i Docker Desktop.
    
    Konfigurera:
    
    - **Containernamn:** Ange ett lämpligt namn för din container. Du kan också låta Docker bestämma.
    - **Värdport:** Ange portmappning. Det låter dig ange vilken port på din värddator som mappas till port 2122 inuti containern.
    - **Värdsökväg:** Sökväg till ditt WideQuick-projekt på din värddator.
    - **Containersökväg:** Ange `c:/wqproject` inuti containern. Det här är "Startup"-mappen för din container.

Du kan nu nå din nyligen driftsatta container via WideQuick Remote Client!

!!! Tip "Om du föredrar att använda kommandoraden"

        docker run -d --name widequick-runtime1 \
            -p 2122:2122 \
            -v C:\MyProjects\WQProject:c:/wqproject \
            kentima/widequick-runtime:latest


    Ändra:
    
    *  -p 2122:2122 för att matcha dina portmappningar
    * -v C:\MyProjects\WQProject till din projektmapp 
    *  kentima/widequick-runtime:latest till relevant image, till exempel kentima/widequick-runtime:14 


#### Steg att följa

1. Starta WideQuick Remote Client
2. Lägg till ett system som pekar på 127.0.0.1 port 2122
3. Du har nu åtkomst till din Runtime som befinner sig inuti din container!

!!! Note "En snabb notering om säkerhet"

    Containrar hjälper naturligt till att hålla dina applikationer separerade och säkra. Tänk på dem som individuella säkerhetsfack för dina HMI:er. Men kom ihåg att även de bästa säkerhetsfunktionerna fungerar bäst i kombination med smarta rutiner. Följ alltid din organisations IT-policyer och branschstandarder, särskilt när du kör kritiska industriella system. Lite vaksamhet räcker långt för att hålla din automationsmiljö säker och stabil!

## Vill du göra ändringar? Enkelt!

Redigera bara ditt projekt i WideQuick Designer, gör dina ändringar och spara. Starta om containern så träder ändringarna i kraft nästan direkt.

## Redo att ta steget?

Containrar förändrar hur automationsingenjörer driftsätter och hanterar HMI/SCADA-lösningar. Med WideQuick i containrar får du skalbarhet, effektivitet och tillförlitlighet – allt samlat i ett snyggt och hanterbart paket.


**Vad händer härnäst?**

- Kontakta säljavdelningen för att skaffa din egen universella produktnyckel!
- Prova att driftsätta WideQuick-containrar i din miljö lokalt.
- Hör av dig för en personlig demo eller expertrådgivning.
- Skala med lätthet!
