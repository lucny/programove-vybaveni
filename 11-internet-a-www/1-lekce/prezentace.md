## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**ARPANET: Zárodek dnešního internetu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát. Přesně tak fungovaly klasické komunikační sítě ještě před vznikem internetu. Tvůrci ARPANETu však přišli s odvážnou myšlenkou: místo jediné centrály vytvořit síť, která si sama najde novou cestu i v případě výpadků. Řešení problémů studené války se tak stalo základem technologie, kterou dnes používáme při každém odeslání fotografie, sledování videa nebo videohovoru. Když pochopíte principy ARPANETu, zjistíte, že internet není žádné kouzlo, ale mimořádně promyšlený technický systém založený na několika geniálně jednoduchých myšlenkách.

**ARPANET** vznikl roku **1969** jako výzkumný projekt americké agentury ARPA. Jeho cílem bylo vytvořit **decentralizovanou síť**, která bude fungovat i při výpadku části infrastruktury. Jedním z hlavních problémů bylo propojit **počítače různých výrobců**, které používaly odlišné architektury.

Síť umožnila **sdílení výpočetního výkonu** mezi vzdálenými univerzitami a výzkumnými institucemi. Místo klasického telefonního spojení využila **přepojování paketů (Packet Switching)**. Data se rozdělí na malé pakety, které mohou cestovat různými trasami.

Pokud některá cesta přestane fungovat, pakety si automaticky najdou jinou. Roku **1983** přešel ARPANET na protokoly **TCP/IP**, čímž vznikl základ dnešního internetu. První přenesenou zprávou mělo být slovo **LOGIN**, ale systém po písmenech **LO** spadl.

Moderní internet dodnes využívá stejné základní principy: decentralizaci, paketový přenos a standardizované protokoly.

***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Internet a intranet**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte. Vše používá podobné síťové technologie, ale nepatří to do stejného prostoru. **Internet** propojuje sítě po celém světě, zatímco **intranet** zpřístupňuje vybrané služby pouze členům organizace. Umět oba pojmy rozlišit je důležité nejen pro správu sítí, ale i pro pochopení přístupových práv, firewallu a bezpečné práce s daty.

**Internet** je globální „síť sítí“, která propojuje mnoho samostatně spravovaných sítí. Zařízení a sítě spolu komunikují pomocí společných pravidel – zejména sady protokolů **TCP/IP**. Přenos může využívat optická vlákna, metalické kabely, Wi‑Fi, mobilní sítě, satelity i podmořské kabely.

**Páteřní síť (backbone)** přenáší velké objemy dat mezi významnými uzly a sítěmi. **Intranet** je neveřejná síť nebo soubor služeb určených členům jedné organizace. Intranet může používat stejné technologie jako web: prohlížeč, HTTP/HTTPS, DNS i IP adresy.

Přístup do intranetu bývá omezen přihlášením, umístěním ve vnitřní síti, VPN nebo jejich kombinací. **Firewall** provoz filtruje podle nastavených pravidel; sám o sobě neověřuje vždy totožnost uživatele. Intranet není totéž co **extranet**. Extranet zpřístupňuje vybranou část interních služeb také partnerům či zákazníkům.

Připojení intranetu k internetu neznamená, že jsou všechny interní služby veřejně dostupné.

***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Přepojování okruhů a paketů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta. Internet postupuje jinak: zprávu rozdělí na menší části, které sdílejí síť s daty ostatních uživatelů. Právě **přepojování paketů** umožňuje, aby po jedné infrastruktuře současně proudila videa, hry, e-maily i školní úkoly. Rozdíl mezi okruhem a paketem vysvětluje, proč internet efektivně využívá kapacitu a dokáže reagovat na změny v síti.

**Přepojování okruhů** vytvoří před přenosem vyhrazenou cestu mezi koncovými body. Kapacita okruhu zůstává rezervována po dobu spojení, i když účastníci právě mlčí. Klasickým příkladem byla tradiční telefonní síť; moderní telefonie může používat pakety.

**Přepojování paketů** rozdělí data na menší samostatné jednotky – pakety. Paket obsahuje užitečná data a řídicí informace, například adresy. Směrovače předávají pakety postupně mezi sítěmi.

Různé pakety stejného přenosu mohou, ale nemusí, projít různými trasami. Pořadí příchodu nemusí být stejné jako pořadí odeslání. Sdílení linek zvyšuje efektivitu, ale zatížení sítě může způsobit zpoždění, kolísání zpoždění nebo ztrátu paketů.

Spolehlivost a správné pořadí může zajistit vyšší protokol, například **TCP**.

***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**IP, TCP a UDP**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Stažení maturitní práce a živý přenos ze hry mají odlišné priority. U souboru nesmí chybět ani bajt, zatímco u živého videa může být lepší přehlédnout krátkou chybu než čekat na opožděná data. Internet proto nepoužívá jediný univerzální způsob doručení. **IP** řeší adresování a cestu mezi sítěmi, zatímco **TCP** a **UDP** nabízejí aplikacím odlišné transportní služby.

**IP** zajišťuje adresování a předávání datagramů mezi sítěmi. IP funguje metodou „best effort“: samo nezaručuje doručení, pořadí ani odstranění duplicit. **TCP** je spojovaná transportní služba nad IP.

TCP používá pořadová čísla, potvrzování, opakovaný přenos a řízení toku i zahlcení. Spojení TCP se běžně navazuje pomocí tří kroků **SYN → SYN‑ACK → ACK**. TCP poskytuje aplikaci uspořádaný proud bajtů, nikoli „hotové soubory“.

**UDP** je nespojovaná datagramová transportní služba s malou režijní zátěží. UDP samo nepotvrzuje doručení ani nezajišťuje pořadí; aplikace si může potřebné funkce doplnit. UDP neznamená nulové zpoždění ani automaticky rychlejší přenos za všech okolností.

Web dnes může používat TCP (HTTP/1.1, HTTP/2) i protokol QUIC nad UDP (HTTP/3). O vhodnosti nerozhoduje jen typ aplikace, ale požadavek na spolehlivost, latenci a způsob, jakým je protokol navržen.

***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**IP adresy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Když pošlete balík, nestačí znát jméno příjemce – zásilka potřebuje adresu. Podobně síť potřebuje vědět, odkud data přicházejí a kam mají směřovat. IP adresa však není neměnné „rodné číslo počítače“: může se měnit, může označovat síťové rozhraní a stejná soukromá adresa se může opakovat v mnoha domácnostech. Pochopení IPv4, IPv6 a NAT pomáhá při zapojování sítí i hledání závad.

IP adresa identifikuje síťové rozhraní v rámci IP komunikace a umožňuje směrování. **IPv4** má 32 bitů a obvykle se zapisuje čtyřmi desetinnými čísly od 0 do 255. Celý prostor IPv4 obsahuje přibližně **4,3 miliardy** adres, ale ne všechny lze přidělit běžným zařízením.

**IPv6** má 128 bitů a zapisuje se hexadecimálně do skupin oddělených dvojtečkami. IPv6 nabízí přibližně **3,4 × 10^38** adres. Nuly v IPv6 lze zkracovat; dvojité dvojtečky `::` lze v jedné adrese použít jen jednou.

**Veřejná IP adresa** je globálně směrovatelná a musí být v daném kontextu jedinečná. Soukromé rozsahy IPv4 jsou `10.0.0.0/8`, `172.16.0.0/12` a `192.168.0.0/16`. Soukromé IPv4 adresy se na veřejném internetu přímo nesměrují a mohou se v různých sítích opakovat.

**NAT** překládá adresy; domácí router často pomocí NAPT/PAT rozlišuje více zařízení také čísly portů. NAT není totéž co firewall, přestože obě funkce často zajišťuje stejný router. Adresa `203.0.113.0/24` ze snímku patří k rozsahu vyhrazenému pro dokumentaci, proto je vhodná do výuky.

***

## Snímek 1.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**DNS**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Lidé si snadno zapamatují `moodle.sspu-opava.cz`, ale směrování v síti pracuje s IP adresami. **DNS** propojuje oba světy: vyhledává záznamy spojené s doménovými jmény. Bez DNS by internet nepřestal fyzicky fungovat, ale místo názvů bychom často museli zadávat adresy a řada služeb by se kvůli závislosti na jménech rozbila. DNS je proto jeden z nenápadných základů každého načtení webu či doručení e-mailu.

**DNS (Domain Name System)** je distribuovaný hierarchický systém jmen a záznamů. Resolver hledá odpověď v cache, nebo se dotazuje dalších DNS serverů. Hierarchie se při technickém čtení sleduje zprava: kořen `.`, TLD, doména druhé úrovně a další subdomény.

V `moodle.sspu-opava.cz` je `.cz` TLD, `sspu-opava` doména druhé úrovně a `moodle` subdoména/hostitelský název. Kořenová zóna obsahuje informace, které ukazují k serverům domén nejvyšší úrovně. **A** záznam mapuje jméno na IPv4, **AAAA** na IPv6.

**CNAME** vytváří alias, **MX** určuje poštovní servery a **TXT** nese textová data. **TTL** udává, jak dlouho může být záznam uložen v cache. DNS odpověď nemusí vždy obsahovat jednu IP adresu; může vrátit více adres nebo jiný druh záznamu.

DNS tradičně není šifrované; existují varianty DNS over HTTPS a DNS over TLS. **DNSSEC** ověřuje původ a integritu DNS dat, ale samo nešifruje dotazy.

***

## Snímek 1.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Cesta paketu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Klepnutí na tlačítko „Nahrát“ trvá zlomek sekundy, ale fotografie mezitím projde celým řetězcem činností. Aplikace vytvoří data, transportní a síťové protokoly doplní řídicí informace, místní síť je předá routeru a další směrovače je posouvají k datovému centru. Jednotlivé části mohou dorazit v jiném pořadí nebo se některá může ztratit. Porozumění této cestě spojuje IP adresy, DNS, routery, TCP i fyzická média do jednoho funkčního obrazu internetu.

Aplikace připraví data fotografie a předá je transportní vrstvě. Data se při přenosu dělí na menší jednotky; přesné názvy závisí na vrstvě a protokolu. **Zapouzdření** postupně přidává hlavičky transportní, síťové a linkové vrstvy.

DNS může před přenosem přeložit jméno cloudové služby na IP adresu. Zdrojová a cílová IP adresa určují konce IP komunikace; routery podle cíle volí další krok. Domácí nebo školní router může provádět NAT mezi soukromou a veřejnou adresou.

Každý router rozhoduje o dalším úseku cesty, nikoli obvykle o celé trase od začátku do konce. Různé pakety mohou projít různými trasami, ale často po určitou dobu používají trasu stejnou. Optické, metalické a bezdrátové spoje přenášejí bity různým fyzickým způsobem.

TCP může rozpoznat chybějící data a zajistit jejich opakovaný přenos. Cílový systém data předá správné aplikaci, která ověří a uloží fotografii. „Cloud“ není oblak, ale vzdálená infrastruktura datových center a služeb.


# 2. Internetové služby a URL

> Stejná síť přenáší webové stránky, e-maily, hovory i soubory. Jak počítače poznají, o jakou službu jde a kam mají data předat?

Tato lekce navazuje na principy internetu a soustředí se na jeho konkrétní služby. Vysvětluje vztah mezi službou a protokolem, význam síťových portů, rozdíl mezi architekturou klient–server a peer-to-peer a přesnou stavbu webové adresy URL.

***
