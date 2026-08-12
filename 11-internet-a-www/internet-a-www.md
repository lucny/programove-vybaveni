# Internet a WWW

> Internet není jedna služba ani jeden server. Je to globální soustava vzájemně propojených sítí, nad níž fungují web, e-mail, vyhledávání, cloudové služby a stále větší množství aplikací a zařízení. Pochopení internetu proto začíná u paketů, adres a protokolů a pokračuje přes služby a World Wide Web až k bezpečnosti, vyhledávání a současným technologickým změnám.

# 1. Principy internetu

> Jak se z experimentální sítě se čtyřmi uzly stal celosvětový systém, který propojuje miliardy zařízení?

Tato lekce vysvětluje internet jako **síť sítí**. Postupně propojuje historické důvody vzniku ARPANETu, rozdíl mezi internetem a intranetem, přepojování paketů, role protokolů IP, TCP a UDP, adresování, DNS a praktickou cestu dat mezi aplikací a vzdáleným serverem.

## 1.1 ARPANET: Zárodek dnešního internetu

Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát. Přesně tak fungovaly klasické komunikační sítě ještě před vznikem internetu. Tvůrci ARPANETu však přišli s odvážnou myšlenkou: místo jediné centrály vytvořit síť, která si sama najde novou cestu i v případě výpadků. Řešení problémů studené války se tak stalo základem technologie, kterou dnes používáme při každém odeslání fotografie, sledování videa nebo videohovoru. Když pochopíte principy ARPANETu, zjistíte, že internet není žádné kouzlo, ale mimořádně promyšlený technický systém založený na několika geniálně jednoduchých myšlenkách.

**ARPANET** vznikl roku **1969** jako výzkumný projekt americké agentury ARPA. Jeho cílem bylo vytvořit **decentralizovanou síť**, která bude fungovat i při výpadku části infrastruktury. Jedním z hlavních problémů bylo propojit **počítače různých výrobců**, které používaly odlišné architektury.

Síť umožnila **sdílení výpočetního výkonu** mezi vzdálenými univerzitami a výzkumnými institucemi. Místo klasického telefonního spojení využila **přepojování paketů (Packet Switching)**. Data se rozdělí na malé pakety, které mohou cestovat různými trasami.

Pokud některá cesta přestane fungovat, pakety si automaticky najdou jinou. Roku **1983** přešel ARPANET na protokoly **TCP/IP**, čímž vznikl základ dnešního internetu. První přenesenou zprávou mělo být slovo **LOGIN**, ale systém po písmenech **LO** spadl.

Moderní internet dodnes využívá stejné základní principy: decentralizaci, paketový přenos a standardizované protokoly.


## 1.2 Internet a intranet

Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte. Vše používá podobné síťové technologie, ale nepatří to do stejného prostoru. **Internet** propojuje sítě po celém světě, zatímco **intranet** zpřístupňuje vybrané služby pouze členům organizace. Umět oba pojmy rozlišit je důležité nejen pro správu sítí, ale i pro pochopení přístupových práv, firewallu a bezpečné práce s daty.

**Internet** je globální „síť sítí“, která propojuje mnoho samostatně spravovaných sítí. Zařízení a sítě spolu komunikují pomocí společných pravidel – zejména sady protokolů **TCP/IP**. Přenos může využívat optická vlákna, metalické kabely, Wi‑Fi, mobilní sítě, satelity i podmořské kabely.

**Páteřní síť (backbone)** přenáší velké objemy dat mezi významnými uzly a sítěmi. **Intranet** je neveřejná síť nebo soubor služeb určených členům jedné organizace. Intranet může používat stejné technologie jako web: prohlížeč, HTTP/HTTPS, DNS i IP adresy.

Přístup do intranetu bývá omezen přihlášením, umístěním ve vnitřní síti, VPN nebo jejich kombinací. **Firewall** provoz filtruje podle nastavených pravidel; sám o sobě neověřuje vždy totožnost uživatele. Intranet není totéž co **extranet**. Extranet zpřístupňuje vybranou část interních služeb také partnerům či zákazníkům.

Připojení intranetu k internetu neznamená, že jsou všechny interní služby veřejně dostupné.


## 1.3 Přepojování okruhů a paketů

Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta. Internet postupuje jinak: zprávu rozdělí na menší části, které sdílejí síť s daty ostatních uživatelů. Právě **přepojování paketů** umožňuje, aby po jedné infrastruktuře současně proudila videa, hry, e-maily i školní úkoly. Rozdíl mezi okruhem a paketem vysvětluje, proč internet efektivně využívá kapacitu a dokáže reagovat na změny v síti.

**Přepojování okruhů** vytvoří před přenosem vyhrazenou cestu mezi koncovými body. Kapacita okruhu zůstává rezervována po dobu spojení, i když účastníci právě mlčí. Klasickým příkladem byla tradiční telefonní síť; moderní telefonie může používat pakety.

**Přepojování paketů** rozdělí data na menší samostatné jednotky – pakety. Paket obsahuje užitečná data a řídicí informace, například adresy. Směrovače předávají pakety postupně mezi sítěmi.

Různé pakety stejného přenosu mohou, ale nemusí, projít různými trasami. Pořadí příchodu nemusí být stejné jako pořadí odeslání. Sdílení linek zvyšuje efektivitu, ale zatížení sítě může způsobit zpoždění, kolísání zpoždění nebo ztrátu paketů.

Spolehlivost a správné pořadí může zajistit vyšší protokol, například **TCP**.


## 1.4 IP, TCP a UDP

Stažení maturitní práce a živý přenos ze hry mají odlišné priority. U souboru nesmí chybět ani bajt, zatímco u živého videa může být lepší přehlédnout krátkou chybu než čekat na opožděná data. Internet proto nepoužívá jediný univerzální způsob doručení. **IP** řeší adresování a cestu mezi sítěmi, zatímco **TCP** a **UDP** nabízejí aplikacím odlišné transportní služby.

**IP** zajišťuje adresování a předávání datagramů mezi sítěmi. IP funguje metodou „best effort“: samo nezaručuje doručení, pořadí ani odstranění duplicit. **TCP** je spojovaná transportní služba nad IP.

TCP používá pořadová čísla, potvrzování, opakovaný přenos a řízení toku i zahlcení. Spojení TCP se běžně navazuje pomocí tří kroků **SYN → SYN‑ACK → ACK**. TCP poskytuje aplikaci uspořádaný proud bajtů, nikoli „hotové soubory“.

**UDP** je nespojovaná datagramová transportní služba s malou režijní zátěží. UDP samo nepotvrzuje doručení ani nezajišťuje pořadí; aplikace si může potřebné funkce doplnit. UDP neznamená nulové zpoždění ani automaticky rychlejší přenos za všech okolností.

Web dnes může používat TCP (HTTP/1.1, HTTP/2) i protokol QUIC nad UDP (HTTP/3). O vhodnosti nerozhoduje jen typ aplikace, ale požadavek na spolehlivost, latenci a způsob, jakým je protokol navržen.


## 1.5 IP adresy

Když pošlete balík, nestačí znát jméno příjemce – zásilka potřebuje adresu. Podobně síť potřebuje vědět, odkud data přicházejí a kam mají směřovat. IP adresa však není neměnné „rodné číslo počítače“: může se měnit, může označovat síťové rozhraní a stejná soukromá adresa se může opakovat v mnoha domácnostech. Pochopení IPv4, IPv6 a NAT pomáhá při zapojování sítí i hledání závad.

IP adresa identifikuje síťové rozhraní v rámci IP komunikace a umožňuje směrování. **IPv4** má 32 bitů a obvykle se zapisuje čtyřmi desetinnými čísly od 0 do 255. Celý prostor IPv4 obsahuje přibližně **4,3 miliardy** adres, ale ne všechny lze přidělit běžným zařízením.

**IPv6** má 128 bitů a zapisuje se hexadecimálně do skupin oddělených dvojtečkami. IPv6 nabízí přibližně **3,4 × 10^38** adres. Nuly v IPv6 lze zkracovat; dvojité dvojtečky `::` lze v jedné adrese použít jen jednou.

**Veřejná IP adresa** je globálně směrovatelná a musí být v daném kontextu jedinečná. Soukromé rozsahy IPv4 jsou `10.0.0.0/8`, `172.16.0.0/12` a `192.168.0.0/16`. Soukromé IPv4 adresy se na veřejném internetu přímo nesměrují a mohou se v různých sítích opakovat.

**NAT** překládá adresy; domácí router často pomocí NAPT/PAT rozlišuje více zařízení také čísly portů. NAT není totéž co firewall, přestože obě funkce často zajišťuje stejný router. Adresa `203.0.113.0/24` ze snímku patří k rozsahu vyhrazenému pro dokumentaci, proto je vhodná do výuky.


## 1.6 DNS

Lidé si snadno zapamatují `moodle.sspu-opava.cz`, ale směrování v síti pracuje s IP adresami. **DNS** propojuje oba světy: vyhledává záznamy spojené s doménovými jmény. Bez DNS by internet nepřestal fyzicky fungovat, ale místo názvů bychom často museli zadávat adresy a řada služeb by se kvůli závislosti na jménech rozbila. DNS je proto jeden z nenápadných základů každého načtení webu či doručení e-mailu.

**DNS (Domain Name System)** je distribuovaný hierarchický systém jmen a záznamů. Resolver hledá odpověď v cache, nebo se dotazuje dalších DNS serverů. Hierarchie se při technickém čtení sleduje zprava: kořen `.`, TLD, doména druhé úrovně a další subdomény.

V `moodle.sspu-opava.cz` je `.cz` TLD, `sspu-opava` doména druhé úrovně a `moodle` subdoména/hostitelský název. Kořenová zóna obsahuje informace, které ukazují k serverům domén nejvyšší úrovně. **A** záznam mapuje jméno na IPv4, **AAAA** na IPv6.

**CNAME** vytváří alias, **MX** určuje poštovní servery a **TXT** nese textová data. **TTL** udává, jak dlouho může být záznam uložen v cache. DNS odpověď nemusí vždy obsahovat jednu IP adresu; může vrátit více adres nebo jiný druh záznamu.

DNS tradičně není šifrované; existují varianty DNS over HTTPS a DNS over TLS. **DNSSEC** ověřuje původ a integritu DNS dat, ale samo nešifruje dotazy.


## 1.7 Cesta paketu

Klepnutí na tlačítko „Nahrát“ trvá zlomek sekundy, ale fotografie mezitím projde celým řetězcem činností. Aplikace vytvoří data, transportní a síťové protokoly doplní řídicí informace, místní síť je předá routeru a další směrovače je posouvají k datovému centru. Jednotlivé části mohou dorazit v jiném pořadí nebo se některá může ztratit. Porozumění této cestě spojuje IP adresy, DNS, routery, TCP i fyzická média do jednoho funkčního obrazu internetu.

Aplikace připraví data fotografie a předá je transportní vrstvě. Data se při přenosu dělí na menší jednotky; přesné názvy závisí na vrstvě a protokolu. **Zapouzdření** postupně přidává hlavičky transportní, síťové a linkové vrstvy.

DNS může před přenosem přeložit jméno cloudové služby na IP adresu. Zdrojová a cílová IP adresa určují konce IP komunikace; routery podle cíle volí další krok. Domácí nebo školní router může provádět NAT mezi soukromou a veřejnou adresou.

Každý router rozhoduje o dalším úseku cesty, nikoli obvykle o celé trase od začátku do konce. Různé pakety mohou projít různými trasami, ale často po určitou dobu používají trasu stejnou. Optické, metalické a bezdrátové spoje přenášejí bity různým fyzickým způsobem.

TCP může rozpoznat chybějící data a zajistit jejich opakovaný přenos. Cílový systém data předá správné aplikaci, která ověří a uloží fotografii. „Cloud“ není oblak, ale vzdálená infrastruktura datových center a služeb.


# 2. Internetové služby a URL

> Stejná síť přenáší webové stránky, e-maily, hovory i soubory. Jak počítače poznají, o jakou službu jde a kam mají data předat?

Tato lekce navazuje na principy internetu a soustředí se na jeho konkrétní služby. Vysvětluje vztah mezi službou a protokolem, význam síťových portů, rozdíl mezi architekturou klient–server a peer-to-peer a přesnou stavbu webové adresy URL.

## 2.1 Internet a jeho služby

Když sledujete video, posíláte e-mail nebo hrajete online hru, používáte pokaždé stejný internet, ale jinou službu. Internet je především infrastruktura a pravidla propojení sítí. Web, e-mail či videohovor jsou aplikace, které tuto infrastrukturu využívají. Rozlišení těchto vrstev pomáhá pochopit, proč může fungovat internetové připojení, i když konkrétní web nebo služba právě nefunguje.

**Internet** je globální propojení sítí založené na sadě protokolů TCP/IP. Fyzickou infrastrukturu tvoří optická a metalická vedení, rádiové spoje, routery, servery a datová centra. **Internetová služba** poskytuje konkrétní užitek: web, e-mail, přenos souborů, streaming, komunikaci či hry.

**WWW není internet**; je pouze jednou ze služeb provozovaných nad internetem. **Protokol** určuje pravidla komunikace mezi programy a zařízeními. Web běžně používá HTTP/HTTPS, e-mail několik poštovních protokolů a živá komunikace další protokoly.

Jedna služba může využívat více protokolů a jeden protokol může sloužit více aplikacím. Data různých služeb se přenášejí jako pakety přes společnou infrastrukturu. Výpadek jedné služby nemusí znamenat výpadek internetového připojení.

Rychlost služby ovlivňuje nejen přípojka, ale také server, trasa, zatížení sítě, latence a použitý protokol.


## 2.2 Internetové služby a protokoly

Počítač musí poznat nejen kam data poslat, ale také jak s nimi zacházet. E-mail je potřeba odeslat, uložit a synchronizovat, správce serveru potřebuje bezpečný vzdálený přístup a videohovor musí reagovat téměř okamžitě. Každá služba proto používá vhodné aplikační a transportní protokoly. Znalost jejich rolí pomáhá při konfiguraci programů i hledání chyb.

**Služba** popisuje, co uživatel získává; **protokol** popisuje pravidla komunikace. **SMTP** slouží k odesílání a předávání elektronické pošty. **IMAP** umožňuje pracovat se schránkou uloženou na serveru a synchronizovat její stav.

**POP3** stahuje zprávy; mazání ze serveru závisí na nastavení klienta, není povinné. **FTP** je tradiční protokol pro přenos souborů, ale sám nešifruje přihlašovací údaje ani data. **FTPS** je FTP zabezpečené pomocí TLS.

**SFTP** je samostatný protokol pro přenos souborů provozovaný typicky přes SSH; není „FTP přes SSH“. **SSH** poskytuje šifrovaný vzdálený přístup, spouštění příkazů a další bezpečné funkce. Telnet neposkytuje běžné šifrování a pro vzdálenou správu přes nedůvěryhodnou síť není vhodný.

**SIP** často zajišťuje navázání a řízení multimediální relace, zatímco **RTP** přenáší média. Konkrétní komunikační aplikace mohou používat vlastní kombinace a moderní protokoly, nejen SIP/RTP.

**Šifrování není jen zámek u názvu.** Ověřujte také certifikát, hostitelský klíč a důvěryhodnost serveru. Šifrované spojení s útočníkem není bezpečný cíl.

## 2.3 Síťové porty

IP adresa přivede data ke správnému zařízení, ale na něm současně běží prohlížeč, poštovní klient, hra i další programy. Čísla portů pomáhají transportní vrstvě a operačnímu systému rozlišit jednotlivé komunikační konce. Port tedy není fyzická zásuvka, ale 16bitové číslo používané protokoly TCP, UDP a dalšími transporty.

Port je logický identifikátor v rozsahu **0–65535**. TCP a UDP mají oddělené prostory portů; stejné číslo může být registrováno pro oba protokoly. Spojení se rozlišuje kombinací protokolu, zdrojové a cílové IP adresy a zdrojového a cílového portu.

**Systémové porty** mají rozsah `0–1023`. **Uživatelské/registrované porty** mají rozsah `1024–49151`. **Dynamické/soukromé porty** mají rozsah `49152–65535`.

Server obvykle naslouchá na známém portu; klient používá dočasný zdrojový port. Běžné hodnoty: SSH `22/TCP`, SMTP `25/TCP`, DNS `53/UDP` i `53/TCP`, HTTP `80/TCP`, IMAP `143/TCP`, HTTPS `443/TCP` i `443/UDP`. Číslo portu je konvence, nikoli bezpečnostní záruka. Službu lze nakonfigurovat na jiné číslo.

Otevřený port znamená, že na dané kombinaci adresy a transportu pravděpodobně naslouchá služba; neříká, že je bezpečná. Firewall může provoz na portech povolit, omezit nebo blokovat.


## 2.4 Klient–server a peer-to-peer

Při návštěvě webu žádá prohlížeč server o obsah. Při sdílení v P2P síti může tentýž počítač data současně přijímat i poskytovat ostatním. Tyto modely určují, kde leží data, kdo řídí komunikaci, jak se systém rozšiřuje a kde vznikají rizika. Ve skutečnosti mnoho služeb používá hybridní architekturu, která kombinuje centrální koordinaci s přímou komunikací účastníků.

**Klient** zahajuje požadavek na službu; **server** požadavky přijímá a odpovídá. Klientem a serverem jsou role programů, ne nutně konkrétní typy počítačů. Model klient–server usnadňuje centrální správu, aktualizace, řízení přístupu a zálohování.

Jeden nedostatečně dimenzovaný server může být úzkým místem nebo jediným bodem selhání. Reálné služby riziko snižují replikací, load balancingem, cachemi a více datovými centry. V **peer-to-peer (P2P)** mohou uzly vystupovat současně jako klienti i servery.

P2P může rozdělit přenos a úložiště mezi mnoho účastníků. Dostupnost P2P zdroje závisí na počtu aktivních peerů, jejich kapacitě a pravidlech protokolu. P2P není automaticky anonymní, nelegální ani bezpečné; jde o architektonický model.

P2P síť může potřebovat centrální prvek pro vyhledávání, přihlášení nebo navázání spojení. **Hybridní model** kombinuje centrální služby a přímou komunikaci peerů.


## 2.5 URL

Jediný řádek v adresním poli může určit způsob komunikace, server, port, cestu, parametry i místo uvnitř dokumentu. Správné čtení URL pomáhá při tvorbě webů, diagnostice i ochraně před phishingem. Rozhodující je zejména přesně poznat skutečný název hostitele, protože podvodná adresa může důvěryhodná slova schovat do cesty nebo subdomény.

**URL (Uniform Resource Locator)** identifikuje umístění zdroje a způsob, jak k němu přistoupit. Obecný příklad: `https://moodle.sspu-opava.cz:443/course/index.php?categoryid=3#sekce`. **Schéma** `https` určuje pravidla přístupu; běžně používá HTTP zabezpečené pomocí TLS.

**Hostitel** `moodle.sspu-opava.cz` je doménové jméno, které DNS může přeložit na IP adresu. Volitelný **port** následuje za dvojtečkou; výchozí port HTTPS je 443 a obvykle se nezapisuje. **Cesta** `/course/index.php` identifikuje zdroj v prostoru spravovaném serverem; nemusí odpovídat skutečné složce či souboru na disku.

**Query** začíná `?` a obvykle obsahuje dvojice `klíč=hodnota` oddělené znakem `&`. **Fragment** začíná `#` a označuje část výsledného zdroje; prohlížeč jej běžně neposílá v HTTP požadavku serveru. URL může obsahovat procentní kódování, například `%20` pro mezeru.


# 3. World Wide Web a HTTP

> Jak se z jednoduché sítě propojených dokumentů stal aplikační prostor pro weby, služby, přihlášení a interaktivní aplikace?

Tato lekce vysvětluje vznik World Wide Webu, základní princip komunikace HTTP, rozdíl mezi HTTP a HTTPS, význam metod a stavových kódů a mechanismy, které bezstavovému webu umožňují udržovat přihlášení, košík nebo uživatelské preference.

## 3.1 Vznik a princip World Wide Webu

Internet existoval dříve než web, ale práce s informacemi byla složitější a roztříštěná. Tim Berners‑Lee v CERNu navrhl systém, ve kterém dokumenty dostanou adresu a lze mezi nimi přecházet pomocí odkazů. Spojení hypertextu, otevřených standardů a internetu vytvořilo prostředí, které dnes používají miliardy lidí.

**Internet** je infrastruktura propojených sítí; **WWW** je jedna ze služeb, která ji využívá. Tim Berners‑Lee předložil v CERNu návrh webu v březnu **1989**. První webový prohlížeč a editor **WorldWideWeb** vznikl roku **1990** na počítači NeXT.

První webový server běžel na adrese `info.cern.ch`. Web spojuje dokumenty pomocí **hypertextových odkazů**. Tři základní stavební prvky jsou **HTML**, **URI/URL** a **HTTP**.

HTML popisuje strukturu obsahu, URL identifikuje zdroj a HTTP zajišťuje výměnu požadavků a odpovědí. Prohlížeč je klient, který získaný obsah interpretuje a vykresluje. Web se rychle rozšířil díky otevřenosti standardů a rozhodnutí CERNu zpřístupnit základní webový software bez licenčních poplatků.

Dne 30. dubna **1993** CERN uvolnil základní webový software do veřejné domény. Grafický prohlížeč **Mosaic** z roku 1993 pomohl web přiblížit široké veřejnosti.


## 3.2 HTTP komunikace: klient a server

Prohlížeč neobsahuje všechny stránky internetu. Po zadání adresy vyhledá server, odešle mu požadavek a z odpovědí postupně složí stránku. Jediná stránka může vyvolat desítky až stovky dalších požadavků na obrázky, styly, skripty, písma nebo data API. Pochopení tohoto rozhovoru je základem tvorby webu i diagnostiky problémů.

**HTTP** je aplikační protokol založený na výměně požadavků a odpovědí. **Klient** navazuje komunikaci a posílá požadavek; **server** požadavek zpracuje a odpoví. Požadavek obsahuje metodu, cíl požadavku, hlavičky a někdy tělo.

Odpověď obsahuje stavový kód, hlavičky a případně tělo s reprezentací zdroje. Metoda **GET** žádá reprezentaci zdroje; **POST** předává data ke zpracování podle pravidel služby. Hlavičky nesou metadata, například podporované formáty, typ obsahu, cache nebo autentizační údaje.

`Content-Type` popisuje formát těla, například `text/html` nebo `image/png`. Stavový kód shrnuje výsledek, například `200`, `404` nebo `500`. HTML dokument obvykle odkazuje na další zdroje, které prohlížeč vyžádá samostatně.

HTTP je bezstavové: význam každého požadavku lze chápat samostatně; stav aplikace doplňují cookies, tokeny či serverové relace. Server nemusí být jeden fyzický počítač a nemusí být vždy dostupný.

**HTTP zpráva má jasně oddělené části.** Požadavek obvykle obsahuje metodu, cíl požadavku, hlavičky a někdy tělo. Odpověď obsahuje stavový kód, hlavičky a případně tělo. Hlavička `Content-Type` popisuje formát těla, například `text/html` nebo `image/png`.

**Jedna stránka znamená mnoho požadavků.** První HTML dokument často obsahuje odkazy na obrázky, styly, skripty, písma nebo data API. Prohlížeč proto po získání hlavního dokumentu vytváří další samostatné HTTP požadavky.


## 3.3 HTTP a HTTPS

Při přihlášení nebo platbě putují mezi prohlížečem a serverem citlivé údaje. Nezabezpečené HTTP je předává bez ochrany transportní vrstvy. HTTPS přidává TLS, které šifruje komunikaci, kontroluje její integritu a umožňuje ověřit identitu serveru pomocí certifikátu. Neříká však, že je web poctivý nebo bez chyb.

**HTTPS** je HTTP komunikace chráněná protokolem **TLS**. Šifrování omezuje možnost číst obsah komunikace cestou. Integrita umožňuje odhalit neoprávněnou změnu přenášených dat.

Autentizace serveru využívá certifikát a řetězec důvěry certifikačních autorit. Certifikát svazuje veřejný klíč s identitou, zejména s doménovými jmény. Prohlížeč kontroluje platnost certifikátu, jméno hostitele, podpis a další podmínky.

TLS naváže kryptografické klíče; obsah pak chrání efektivní symetrické šifrování. HTTPS běžně používá port 443, HTTP port 80. HTTPS nechrání kompromitovaný server, neodstraní malware ani neposoudí poctivost provozovatele.

Zámek znamená chráněné spojení k uvedenému hostiteli, nikoli automaticky bezpečný obchod. Část metadat komunikace může zůstat pozorovatelná, například IP cíle a objem provozu. Varování před neplatným certifikátem se nemá bez rozmyslu obcházet.


## 3.4 HTTP metody a stavové kódy

Webový požadavek musí říct, co má server udělat, a odpověď musí oznámit výsledek. K tomu slouží HTTP metody a stavové kódy. Nejde jen o GET, POST, 200 a 404: přesné rozlišení bezpečných a idempotentních metod i skupin odpovědí pomáhá vytvářet spolehlivá API a rychleji hledat chyby.

**GET** žádá reprezentaci zdroje a má být bezpečnou metodou bez požadované změny stavu serveru. **HEAD** je podobné GET, ale server neposílá tělo odpovědi. **POST** předává data ke zpracování; jeho opakování může vytvořit více výsledků.

**PUT** typicky vytvoří nebo nahradí stav cílového zdroje a je idempotentní. **DELETE** žádá odstranění vazby na zdroj a je definováno jako idempotentní. Bezpečná metoda nemá žádat změnu stavu; idempotentní metoda má při opakování stejný zamýšlený účinek jako při jednom provedení.

Data v URL nejsou „vlastnost GET“; query lze použít i u jiných metod. Data v těle POST nejsou šifrována samotnou metodou — chrání je až HTTPS. `1xx` informuje, `2xx` značí úspěch, `3xx` další postup či přesměrování.

`4xx` znamená, že požadavek nelze splnit kvůli problému na straně požadavku či oprávnění. `5xx` označuje, že server při zpracování platného požadavku selhal. `200 OK`, `201 Created`, `204 No Content`, `301`, `302`, `400`, `401`, `403`, `404`, `429` a `500` patří k běžným kódům.


## 3.5 Cookies, relace a webová úložiště

HTTP je bezstavové, přesto e-shop udrží košík a škola pozná přihlášeného uživatele. Webová aplikace si stav doplňuje pomocí cookies, serverových relací a úložišť v prohlížeči. Tyto mechanismy nejsou zaměnitelné: cookie se může automaticky posílat serveru, zatímco `localStorage` zůstává v prohlížeči, dokud jej skript výslovně nepoužije.

HTTP je bezstavové; stav aplikace se vytváří dalšími mechanismy. Server nastaví cookie hlavičkou `Set-Cookie`, prohlížeč ji může v dalších požadavcích vracet v hlavičce `Cookie`. Cookie je dvojice jméno–hodnota s pravidly rozsahu a platnosti.

**Relační cookie** bez `Expires` nebo `Max-Age` běžně zanikne po skončení relace prohlížeče; přesné obnovení relace může chování ovlivnit. **Trvalá cookie** má nastavenou dobu platnosti. Serverová **session** obvykle uchovává stav na serveru; cookie nese pouze náhodný identifikátor relace.

Identifikátor session nemá obsahovat heslo ani citlivá osobní data. `Secure` omezuje odesílání cookie na HTTPS, `HttpOnly` brání přístupu JavaScriptu a `SameSite` omezuje některé cross-site požadavky. `Path` a `Domain` určují rozsah, kam se cookie posílá.

**localStorage** ukládá řetězcová data pro daný origin a běžně přetrvá zavření prohlížeče. Data `localStorage` se neposílají automaticky s HTTP požadavkem, ale JavaScript stránky je může číst. Citlivé autentizační tokeny v `localStorage` jsou rizikové při XSS; pro session ID se obvykle doporučuje bezpečně nastavená `HttpOnly` cookie.

Cookies neslouží jen ke sledování; mohou být technicky nutné pro přihlášení, košík či preference.


# 4. Webové prohlížeče, bezpečnost a digitální stopa

> Prohlížeč není jen okno do internetu: načítá kód, vykresluje stránku, spouští programy, spravuje přihlášení a současně chrání zařízení před cizím obsahem.

Tato lekce vysvětluje, jak prohlížeč promění HTML, CSS a JavaScript ve výslednou stránku, jak fungují jeho hlavní ovládací prvky a vykreslovací enginy, co dokážou DevTools, jak chránit soukromí a jak vzniká digitální stopa.

## 4.1 Jak prohlížeč promění kód ve stránku

Webová stránka nepřichází do počítače jako hotový obrázek. Prohlížeč získá HTML, CSS, JavaScript a média, vytvoří z nich vnitřní datové struktury, vypočítá rozložení a výsledek vykreslí. Je současně síťovým klientem, interpretem webových standardů, prostředím pro programy i bezpečnostní bariérou mezi stránkou a zařízením.

Prohlížeč je **webový klient**, který odesílá požadavky a zpracovává odpovědi. HTML popisuje obsah a strukturu dokumentu, nikoli jeho kompletní vzhled. Prohlížeč parsuje HTML a vytváří strom **DOM**.

CSS určuje prezentaci, rozložení, typografii a přizpůsobení různým obrazovkám. Z CSS vzniká interní model stylů; společně s DOM ovlivňuje výsledný render tree. Při **layoutu** prohlížeč vypočítá velikost a polohu viditelných prvků.

Při **paintu** kreslí pixely; vrstvy mohou být následně složeny při compositingu. JavaScript může měnit DOM, styly, reagovat na události a komunikovat se serverem. JavaScript není nutný pro každou stránku; kvalitní statický obsah může fungovat i bez něj.

HTML dokument může vyvolat další požadavky na CSS, skripty, obrázky, písma a data. Různé prohlížeče mají odlišné implementace, ale řídí se společnými webovými standardy. Renderování je průběžný proces: prohlížeč může zobrazovat část obsahu ještě před úplným stažením.


## 4.2 Rozhraní a ekosystém webových prohlížečů

Adresní řádek, karty, historie, profily a rozšíření vypadají jako běžné ovládací prvky, ale každý z nich souvisí se soukromím a bezpečností. Pod podobným povrchem navíc různé prohlížeče sdílejí nebo vyvíjejí odlišná jádra. Znalost rozhraní a enginů pomáhá při volbě prohlížeče, testování webů i řešení problémů s kompatibilitou.

Adresní řádek často funguje jako **omnibox**: přijímá URL i hledané výrazy. Před potvrzením je vhodné zkontrolovat skutečný hostitel a schéma HTTPS. Tlačítka zpět a vpřed procházejí historii dané karty; obnovení znovu načte nebo ověří zdroj.

Karty oddělují více otevřených dokumentů, ale mohou sdílet profil, cookies a oprávnění. Záložka ukládá odkaz; stažená „offline stránka“ či cache ukládá také obsah. Profil může synchronizovat historii, hesla, karty a nastavení prostřednictvím účtu poskytovatele.

Rozšíření získávají oprávnění a mohou ovlivňovat obsah stránek; instalujte jen potřebná a důvěryhodná. **Blink** používají Chromium, Chrome, Edge, Opera a Brave; jednotlivé prohlížeče se přesto liší funkcemi a nastavením. Firefox používá engine **Gecko** a JavaScriptový engine SpiderMonkey.

Safari používá **WebKit** a JavaScriptCore. Tor Browser je upravený Firefox zaměřený na použití sítě Tor; není to samostatný vykreslovací engine. DuckDuckGo je také vyhledávač; jeho prohlížeče mohou podle platformy využívat systémové enginy.

Rozmanitost enginů pomáhá odhalovat chyby kompatibility a omezuje závislost webu na jediné implementaci.


## 4.3 DevTools: digitální rentgen webové stránky

Vývojářské nástroje ukazují rozdíl mezi tím, co vidí uživatel, a tím, co prohlížeč skutečně zpracovává. Lze prohlížet DOM a CSS, sledovat požadavky, číst chyby, měřit výkon a simulovat různé obrazovky. Úpravy jsou většinou pouze místní a dočasné — DevTools nejsou způsob, jak změnit cizí server.

DevTools otevřete často klávesou `F12` nebo `Ctrl+Shift+I`. **Elements/Inspector** zobrazuje aktuální DOM a aplikované CSS. DOM v DevTools nemusí být totožný s původním HTML, protože jej upravil parser nebo JavaScript.

Místní změna textu či stylu obvykle zmizí po obnovení a nemění server. **Console** zobrazuje chyby a umožňuje spouštět JavaScript v kontextu stránky. Do konzole nevkládejte cizí kód, kterému nerozumíte; může pracovat s přihlášenou relací.

**Network** ukazuje požadavky, metody, stavové kódy, hlavičky, časování a velikosti. Záznam Network často začíná až po otevření nástrojů a obnovení stránky. **Sources/Debugger** umožňuje číst skripty, zastavit běh a krokovat program.

**Performance** pomáhá hledat dlouhé úlohy, vykreslování a problémy s odezvou. Režim zařízení simuluje viewport a některé vlastnosti, ale nenahrazuje test na skutečném telefonu. DevTools mohou zobrazit cookies, tokeny a další citlivá data; snímky obrazovky je nutné před sdílením zkontrolovat.

**DevTools mění hlavně místní pohled.** Úprava textu, CSS nebo atributů v panelu Elements se obvykle projeví jen v paměti konkrétního prohlížeče. Po obnovení se stránka znovu sestaví z dat serveru a lokální změny zmizí. Změna ceny v DOM proto nemění databázi ani skutečnou transakci.


## 4.4 Bezpečnost a soukromí v prohlížeči

Prohlížeč spravuje hesla, relace, historii, platby i přístup ke kameře a mikrofonu. Současně spouští kód z cizích webů a rozšíření. Bezpečnost proto nevytváří jediný „anonymní režim“, ale vrstvy: aktualizace, HTTPS, izolace webů, správná oprávnění, ochrana účtu a promyšlená práce s cookies a doplňky.

Aktualizace opravují známé zranitelnosti prohlížeče a jeho komponent. HTTPS chrání přenos k uvedenému hostiteli, ale nezaručuje poctivý obsah. Soukromé/anonymní okno omezuje hlavně ukládání místní historie a dat po skončení relace.

Soukromý režim neskrývá provoz před navštíveným webem, školou, zaměstnavatelem ani poskytovatelem sítě. Stažené soubory a vytvořené záložky mohou po zavření soukromého okna zůstat. Cookies první strany mohou držet přihlášení a preference; cookies či jiné mechanismy třetích stran mohou sledovat uživatele napříč weby.

Blokování cookies třetích stran omezuje část sledování, ne všechny techniky fingerprintingu. Rozšíření může číst a měnit stránky v rozsahu udělených oprávnění. Důvěryhodné rozšíření se může změnit aktualizací nebo změnou vlastníka.

Oprávnění ke kameře, mikrofonu, poloze a oznámením mají být udělena jen potřebným webům. Správce hesel pomáhá používat dlouhá unikátní hesla; účet chraňte vícefaktorovým ověřením. Mazání cookies může odhlásit uživatele, ale neodstraní data již uložená na serverech.


## 4.5 Digitální stopa a paměť webu

Smazání historie odstraní seznam navštívených stránek z vašeho prohlížeče, ale nevrátí odeslaný příspěvek, nesmaže serverové logy ani kopie u jiných lidí. Digitální stopa vzniká vědomou aktivitou i automatickým zpracováním technických údajů. Ne všechno zůstane navždy, ale nad zveřejněnými daty rychle ztrácíme úplnou kontrolu.

**Historie prohlížení** je místní záznam navštívených adres v konkrétním profilu prohlížeče. Její smazání neodstraňuje záznamy na serverech, DNS resolverech, školní bráně ani synchronizovaných účtech. **Aktivní digitální stopa** vzniká například zveřejněním příspěvku, komentáře, fotografie či formuláře.

**Pasivní stopa** zahrnuje technická a analytická data sbíraná při používání služby. IP adresa, čas, typ zařízení, přibližná poloha, cookies a fingerprint mohou pomoci spojovat události. Metadata mohou prozradit více než samotný obsah, například čas, místo a sociální vazby.

Kopie mohou vzniknout sdílením, snímkem obrazovky, cache, zálohou, vyhledávačem nebo archivací. **Wayback Machine** archivuje část veřejného webu od roku 1996, nikoli celý internet ani každou stránku. Některé stránky nejsou archivovány kvůli technickým omezením, pravidlům, přihlášení nebo žádosti provozovatele.

Digitální stopa není vždy „nesmazatelná“, ale úplné dohledání a odstranění všech kopií může být obtížné či nemožné. Omezování stopy začíná minimalizací sdílených dat, nastavením publika a pravidelným auditem účtů. Práva na přístup, opravu či výmaz osobních údajů mají výjimky a neznamenají automatické odstranění všech veřejných archivů.

# 5. Vyhledávače, SEO a informační gramotnost

> Vyhledávač neukazuje celý web ani čistou pravdu. Nabízí výběr dokumentů, reklam a odpovědí vytvořený z indexu podle konkrétního dotazu, kontextu a pravidel řazení.

Tato lekce vysvětluje, jak vyhledávače objevují stránky, vytvářejí index, řadí výsledky a kombinují organický obsah s reklamou. Současně rozvíjí praktické dovednosti efektivního hledání, ověřování zdrojů a ochrany soukromí.

## 5.1 Vyhledávače: od katalogů k odpovědním systémům

Vyhledávač už nezobrazuje jen seznam modrých odkazů. Kombinuje webové stránky, mapy, videa, databáze, reklamy a někdy generované souhrny. Čím pohodlnější je odpověď přímo ve výsledcích, tím důležitější je poznat její původ, ověřit zdroje a rozlišit vyhledání dokumentu od odpovědi vytvořené modelem.

První webové katalogy třídily odkazy ručně podle kategorií. Moderní vyhledávače automaticky procházejí web, vytvářejí index a řadí výsledky. Výsledková stránka může obsahovat organické odkazy, reklamy, mapy, obrázky, rychlé odpovědi i AI souhrny.

Vyhledávač není neutrální zrcadlo webu; vybírá a řadí pomocí pravidel, modelů a dostupných dat. Výsledek mohou ovlivnit dotaz, jazyk, region, zařízení, aktuálnost, nastavení a někdy historie či účet. Personalizace není u všech služeb stejná a „stejný výsledek pro všechny“ nelze obecně slíbit.

Generovaný souhrn může kombinovat více zdrojů, ale může také chybovat nebo špatně citovat. U zdraví, práva, financí a dalších závažných témat je nutné otevřít původní důvěryhodné zdroje. Reklamní výsledek má být označen a jeho umístění není důkaz odbornosti.

Google, Bing, Seznam.cz, DuckDuckGo a Ecosia se liší zdroji výsledků, funkcemi, obchodním modelem i ochranou soukromí. Tržní podíly se mění podle země, zařízení a metodiky; procento bez zdroje a data není spolehlivý údaj.


## 5.2 Procházení webu: crawling

Vyhledávač nemůže zařadit stránku, o které neví. Automatizovaný crawler proto navštěvuje známé adresy, načítá obsah, sleduje odkazy a plánuje další návštěvy. Neprochází však celý web nepřetržitě a stránka bez odkazů není nutně neviditelná — lze ji objevit také ze sitemap, ručního odeslání či jiných signálů.

**Crawler**, robot nebo spider je automatický klient, který stahuje webové zdroje. Začíná seznamem známých URL a frontou adres určených k návštěvě. Nové URL objevuje z odkazů, sitemap a dalších zdrojů.

Crawler rozhoduje, co a jak často navštíví; kapacita a ohleduplnost k serveru jsou omezené. HTTP kódy, přesměrování, DNS chyby a rychlost serveru ovlivňují procházení. `robots.txt` dává crawlerům pokyny, které cesty smějí požadovat; není bezpečnostní bariéra.

Zákaz crawlování automaticky nezaručuje odstranění URL z výsledků. Pro zákaz indexace se používá například `noindex`, který ale crawler musí moci načíst. XML sitemap usnadňuje oznámení důležitých nebo změněných URL, nezaručuje indexaci.

Odkazy by měly být technicky dostupné crawlerům a mít smysluplný text. JavaScriptový web může vyžadovat vykreslení; složitost může objevování a analýzu zpomalit. Googlebot, Bingbot, SeznamBot a DuckDuckBot jsou příklady crawlerů různých služeb.

## 5.3 Indexace: vyhledatelný rejstřík webu

Při každém dotazu vyhledávač neprochází miliardy webů znovu. Pracuje s předem vytvořeným indexem, podobně jako čtenář s rejstříkem knihy. Do něj ukládá zpracované informace o dokumentech, jejich obsahu, jazyku, odkazech a dalších znacích. Nalezení crawlerem však ještě neznamená indexaci ani zobrazení ve výsledcích.

**Crawling** získává zdroje; **indexace** analyzuje a organizuje informace pro vyhledávání. Vyhledávač obvykle neukládá jen „kopii celého webu“, ale různé reprezentace, signály a někdy cache. Při analýze rozpoznává text, titulky, jazyk, odkazy, obrázky, strukturovaná data a další prvky.

Duplicity a velmi podobné URL může seskupit a vybrat **kanonickou** verzi. `rel="canonical"` je doporučení, nikoli absolutní příkaz. Direktiva `noindex` žádá, aby stránka nebyla ve výsledcích.

`robots.txt` řídí crawling; není správným nástrojem pro spolehlivé `noindex`. K indexaci nemusí dojít kvůli nízké kvalitě, duplicitě, chybě, blokování či nedostupnosti. Dynamický obsah musí být pro crawler technicky získatelný a srozumitelný.

Strukturovaná data pomáhají popsat význam, ale nezaručují rozšířený výsledek ani lepší pozici. Index se průběžně aktualizuje; starý výsledek může přetrvat do dalšího zpracování.

## 5.4 Ranking: jak vyhledávač řadí výsledky

Index může obsahovat mnoho dokumentů odpovídajících stejnému dotazu. Ranking z nich vytvoří pořadí, které se snaží nabídnout užitečnou odpověď. Přesné algoritmy nejsou veřejným jednoduchým vzorcem a mění se. Klíčová slova ani odkazy proto samy o sobě nestačí; důležité jsou záměr, kvalita, kontext a použitelnost.

**Ranking** řadí kandidátní výsledky pro konkrétní dotaz. Relevance vyjadřuje, jak dobře dokument odpovídá významu a záměru dotazu. Systémy mohou hodnotit jazyk, lokalitu, aktuálnost, typ obsahu a mnoho dalších signálů.

Odkazy mohou fungovat jako signál důležitosti, ale hodnotí se kontext a kvalita, ne jen počet. **PageRank** je historicky významný odkazový algoritmus, nikoli úplný popis dnešního rankingu. E‑E‑A‑T je koncept pro hodnocení kvality a důvěryhodnosti, nikoli jeden veřejný číselný „ranking faktor“.

U citlivých YMYL témat je důvěryhodnost zdroje zvlášť důležitá. Výsledek může ovlivnit zařízení, jazyk, přibližná poloha a nastavení. Vysoká pozice nedokazuje pravdivost a nízká pozice nedokazuje nepravdivost.

Manipulativní odkazy, skrytý text a obsah vytvořený jen pro algoritmy mohou porušovat pravidla spamu. Kvalitní obsah má uspokojit potřebu člověka, uvést zdroje a umožnit posoudit autora či provozovatele.

## 5.5 SEO a placené vyhledávání

Výsledková stránka kombinuje algoritmicky řazené odkazy s placenými reklamami. SEO pomáhá vyhledávačům i lidem pochopit a najít web; placené kampaně kupují reklamní prostor podle aukčních a kvalitativních pravidel. Ani jedno není záruka důvěryhodnosti a „SEO je zdarma“ je zjednodušení — neplatí se za organický klik, ale kvalitní obsah i technická správa stojí čas a peníze.

**SEO** je optimalizace viditelnosti webu v neplacených výsledcích. SEO pomáhá crawlerům objevit obsah, vyhledávači jej pochopit a uživateli vybrat výsledek. Organická pozice se nekupuje přímo od vyhledávače.

SEO není zdarma: vyžaduje výzkum, tvorbu obsahu, vývoj, měření a údržbu. **SEM** se používá různě; v praxi často označuje placený search marketing, širší význam může zahrnovat i SEO. Placené výsledky mají být označeny jako reklama nebo sponzorovaný obsah.

U PPC inzerent obvykle platí za kliknutí, ale existují i jiné modely účtování. Pořadí reklamy nemusí určovat jen nejvyšší nabídka; roli hraje kvalita a relevance. Organické výsledky mohou přinášet dlouhodobou návštěvnost, ale pozice nejsou trvalé ani garantované.

Kvalitní SEO staví na užitečném originálním obsahu, přístupnosti, rychlosti, mobilní použitelnosti a technické správnosti. **Keyword stuffing**, kupování manipulativních odkazů a klamavé stránky jsou rizikové spamové techniky. Konverze a přínos pro uživatele jsou důležitější než samotná návštěvnost či první pozice.

## 5.6 Efektivní vyhledávání

Dobré hledání není soutěž v počtu operátorů. Začíná formulací informační potřeby, pokračuje zpřesněním dotazu a končí ověřením zdroje. Operátory mohou omezit šum, ale jejich podpora se mezi vyhledávači mění a výsledky nejsou úplné. Profesionál proto umí dotaz několikrát přeformulovat a zdroj číst kriticky.

Nejprve určete, zda hledáte definici, návod, aktuální zprávu, odbornou studii, data nebo konkrétní dokument. Krátký výstižný dotaz bývá lepší než celá vágní otázka; moderní vyhledávače však rozumějí i přirozenému jazyku. Uvozovky často hledají přesnou frázi: `"přepojování paketů"`.

Znaménko minus může vyloučit význam: `jaguar -auto`. `site:cvut.cz` omezuje výsledky na doménu nebo web. `filetype:pdf` hledá určitý typ souboru, ale neprokazuje jeho odbornost ani bezpečnost.

Operátory lze kombinovat, jejich dostupnost a přesné chování se mohou měnit. Pro aktuální témata přidejte časové období a zkontrolujte datum události i datum publikace. Pro odborné informace preferujte primární zdroj: standard, zákon, dokumentaci, datovou sadu či původní studii.

Výsledek posuzujte podle autora, provozovatele, důkazů, data, účelu a nezávislého potvrzení. AI odpověď nebo úryvek výsledku není náhradou za přečtení zdroje. Když nic nenajdete, použijte synonyma, širší pojem, anglický termín nebo jiný vyhledávač/databázi.

## 5.7 Personalizace a soukromí při vyhledávání

Vyhledávač může využít polohu, jazyk, zařízení, účet a předchozí aktivitu, aby nabídl relevantnější výsledky. To je užitečné při hledání dopravy či restaurace, ale vytváří otázky soukromí a možné omezení pohledu. Soukromější vyhledávač snižuje množství spojovaných dat, nezaručuje však objektivní či stejné výsledky pro celý svět.

Personalizace může využívat účet, historii, přibližnou polohu, jazyk, zařízení a nastavení. Lokalizace výsledků není totéž co dlouhodobý osobní profil; může vycházet jen z aktuálního regionu. **Filtrační bublina** je hypotéza, že výběr obsahu může omezovat setkání s odlišnými informacemi; její síla závisí na službě a situaci.

Žádný vyhledávač neposkytuje dokonale neutrální pořadí — vždy vybírá zdroje a používá ranking. DuckDuckGo uvádí, že nevytváří osobní historii vyhledávání a reklamy cílí podle aktuálního dotazu. Soukromější vyhledávání neanonymizuje automaticky následnou návštěvu cílového webu.

Vyhledávač může využívat výsledky či infrastrukturu partnerů, aniž by jim musel předat osobní identifikátory. Soukromé okno omezuje místní historii, ale samo nezabrání vyhledávači či síti vidět požadavek. HTTPS brání poskytovateli sítě číst obsah dotazu, ale může zůstat vidět, ke které službě se připojujete.

Odhlášení, vypnutí historie a správa aktivity mohou omezit personalizaci, ne nutně veškeré zpracování. Pro citlivé dotazy používejte důvěryhodnou službu, kontrolujte nastavení a po přechodu na výsledek myslete na zásady cílového webu. Soukromí je kompromis mezi množstvím dat, pohodlím, lokalizací a obchodním modelem služby.


# 6. Vývoj internetu, nové technologie a digitální rizika

> Internet se neustále mění, ale jeho další vývoj není jen otázkou vyšší rychlosti. Současně řešíme nové modely webu, miliardy zařízení, nedostatek adres, generativní AI, kybernetické útoky i důvěryhodnost informací.

Tato lekce propojuje historii internetu se současnými technologickými a společenskými změnami. Ukazuje, jak vznikaly jednotlivé vrstvy internetu, co přinesly Web 2.0, Web3, IoT a IPv6, jak pracovat s generativní AI a jak chránit systémy, data, soukromí i informační prostředí.

## 6.1 Milníky internetu: od paketů k propojenému světu

Internet nevznikl jedním vynálezem ani v jediné firmě. Postupně spojil výzkum paketových sítí, otevřené protokoly, akademickou infrastrukturu, komerční poskytovatele, web, mobilní zařízení a cloud. Historická osa pomáhá rozlišit internet od jeho služeb a ukazuje, proč interoperabilita a otevřené standardy změnily experimentální síť v globální infrastrukturu.

Roku **1969** propojil ARPANET první čtyři uzly; první pokus o vzdálené přihlášení skončil po písmenech `LO`. ARPANET nebyl celý dnešní internet, ale významná experimentální paketová síť. Vint Cerf a Bob Kahn patří mezi hlavní autory koncepce propojení různých sítí pomocí TCP/IP.

Dne **1. ledna 1983** přešel ARPANET z NCP na TCP/IP. NSFNET a další akademické sítě v 80. a 90. letech pomohly internet rozšířit. Tim Berners‑Lee navrhl WWW v CERNu roku 1989; první server a prohlížeč vznikly roku 1990.

CERN roku 1993 uvolnil základní webový software bez licenčních poplatků. Google byl založen roku **1998**, ale vyhledávače existovaly již dříve. Pojem **Web 2.0** popisuje posun k interaktivním platformám a uživatelskému obsahu; nemá jedno datum ani technickou verzi.

Chytré telefony, mobilní sítě a cloud přenesly internet do každodenního života. IoT a generativní AI jsou současné vrstvy služeb a zařízení využívající internet, nikoli náhrada jeho základních protokolů. Vývoj tvoří práce mnoha univerzit, států, firem, standardizačních komunit i jednotlivců.

## 6.2 Evoluce webu: čtení, tvorba a decentralizace

Označení Web 1.0, Web 2.0 a Web3 nejsou oficiální verze jako HTTP/2. Jsou to zjednodušující popisy různých trendů. Raný web nebyl pouze pasivní, sociální web není jediným modelem současnosti a blockchain automaticky nedává uživateli kontrolu. Užitečné je proto porovnávat konkrétní vlastnosti, nikoli věřit marketingovým nálepkám.

**Web 1.0** neoznačuje standard, ale rané období převážně dokumentových a publikačních webů. I raný web obsahoval formuláře, diskuse a možnost tvorby; hranice období nejsou ostré. **Web 2.0** popisuje interaktivní aplikace, uživatelský obsah, API, sociální sítě a platformy.

V modelu platforem uživatel obsah vytváří, ale data i pravidla často spravuje centrální provozovatel. Síťový efekt zvyšuje užitek platformy, ale může také posílit závislost na jednom poskytovateli. **Web3** je nejednotný pojem spojovaný s blockchainy, tokeny, kryptografickými peněženkami a decentralizovanými aplikacemi.

Web3 není totéž co **Web 3.0** ve významu sémantického webu. Blockchain může rozdělit správu záznamu, ale aplikace může stále záviset na centrálním webu, API, burze nebo vývojovém týmu. Držení privátního klíče přináší kontrolu i odpovědnost; jeho ztráta může být nevratná.

Veřejný blockchain není automaticky soukromý a neměnný záznam komplikuje opravu či výmaz dat. Decentralizace má stupně: technickou, organizační, datovou i ekonomickou. Současný web kombinuje statické stránky, platformy, federované systémy, P2P i blockchainové služby.

## 6.3 Internet věcí

Termostat, hodinky, kamera nebo průmyslový senzor dokážou měřit okolí, reagovat a komunikovat s dalšími systémy. Pohodlí však znamená dlouhodobý sběr dat, závislost na aktualizacích a novou útočnou plochu. U IoT proto nestačí posoudit funkci zařízení; je třeba hodnotit celý produkt včetně aplikace, cloudu, účtu a podpory výrobce.

**IoT** zahrnuje fyzická zařízení se senzory či akčními členy a síťovou komunikací. Zařízení nemusí být přímo připojeno k veřejnému internetu; může komunikovat přes bránu, telefon či místní síť. Senzor měří, akční člen provádí činnost a řídicí software rozhoduje.

Data mohou být zpracována lokálně na edge zařízení, v bráně nebo v cloudu. IoT se používá v domácnostech, zdravotnictví, dopravě, energetice, zemědělství i průmyslu. Přínosem může být automatizace, včasná detekce, úspora zdrojů a lepší rozhodování.

Rizika zahrnují slabou identitu zařízení, zranitelnosti, špatné aktualizace, únik dat a fyzické dopady útoku. Výchozí nebo sdílená hesla jsou riziková; zařízení má podporovat bezpečnou konfiguraci. Důležitá je ověřitelná aktualizace firmwaru a jasná doba podpory.

Síťová segmentace omezuje škody při napadení jednoho zařízení. Sbírejte jen potřebná data a ověřte, kam odcházejí, jak dlouho se ukládají a kdo k nim má přístup. Zařízení bez podpory je třeba nahradit, izolovat nebo odpojit.

## 6.4 Generativní AI a hledání informací

Klasický vyhledávač předkládá zdroje, zatímco generativní model vytváří novou odpověď na základě naučených vzorů a případně dohledaných dokumentů. Je rychlý při vysvětlování, porovnávání a návrhu postupu, ale může přesvědčivě vytvořit nepravdivý údaj nebo neexistující citaci. Informační gramotnost proto nekončí promptem — začíná kontrolou.

Generativní jazykový model vytváří text na základě statistických vzorů, nikoli zaručeného „porozumění pravdě“. Samotný model nemusí mít přístup k aktuálnímu webu; některé produkty kombinují model s vyhledáváním či nástroji. **RAG** doplňuje generování o nalezené dokumenty, ale kvalita odpovědi stále závisí na výběru a interpretaci zdrojů.

Citace může být správná, nepřesná nebo zcela smyšlená; odkaz je nutné otevřít. Model může halucinovat fakta, osoby, právní předpisy, ceny i technické parametry. Odpověď ovlivňuje prompt, kontext, nastavení modelu a dostupné zdroje.

Kontext konverzace není spolehlivá dlouhodobá paměť ani databáze faktů. Do veřejného AI nástroje nevkládejte hesla, osobní údaje, obchodní tajemství ani neveřejné školní dokumenty. AI je vhodná pro brainstorming, vysvětlení, návrhy dotazů, strukturování a transformaci textu s kontrolou člověka.

U medicíny, práva, financí, bezpečnosti a hodnocení lidí je nutná zvýšená opatrnost a odborný zdroj. Primární zdroj, datum, autor a metodika mají větší důkazní hodnotu než plynulost odpovědi. Odpovědnost za použití výsledku zůstává na člověku a organizaci.

## 6.5 Internet, bezpečnost, soukromí a pravdivost

Internet zpřístupnil znalosti a spolupráci, ale stejná infrastruktura přenáší podvody, útoky i manipulaci. Ochrana neznamená jednu aplikaci nebo zákaz technologií. Vzniká kombinací bezpečných účtů, aktualizovaných zařízení, omezeného sdílení dat, ověřování informací a připravenosti na incident.

Kybernetická bezpečnost chrání **důvěrnost, integritu a dostupnost** systémů a dat. Mezi běžné hrozby patří phishing, malware, ransomware, krádež účtu, zneužití zranitelnosti a sociální inženýrství. Základem jsou aktualizace, unikátní hesla ve správci hesel, MFA, zálohy a nejmenší potřebná oprávnění.

MFA výrazně zvyšuje ochranu, ale phishingu odolné bezpečnostní klíče či passkeys jsou silnější než jednorázové SMS kódy. Záloha proti ransomwaru má být oddělená, testovaná a chráněná před přepsáním útočníkem. GDPR nedává absolutní „právo být zapomenut“; právo na výmaz má podmínky a výjimky.

Osobní údaj je informace vztahující se k identifikované či identifikovatelné osobě. Minimalizace znamená sbírat a uchovávat jen data potřebná pro konkrétní účel. Dezinformace je nepravdivý či zavádějící obsah šířený se záměrem klamat; omyl bez tohoto záměru je misinformation.

Deepfake je syntetický nebo upravený obsah; jeho existence sama neurčuje záměr ani pravdivost kontextu. Ověřování zahrnuje původní zdroj, autora, datum, kontext, důkazy a nezávislé potvrzení. Digitální stopa nemusí být navždy dostupná, ale kopie a logy mohou přetrvat mimo naši kontrolu.

Technologie nejsou zcela neutrální: jejich návrh, výchozí nastavení a obchodní model ovlivňují chování i rizika.

# Závěrečné propojení

Internet lze chápat jako několik navazujících vrstev. Fyzická infrastruktura a směrovače propojují samostatné sítě, IP zajišťuje adresování a předávání paketů a transportní protokoly poskytují aplikacím různé způsoby přenosu. Nad touto vrstvou vznikají služby, které používají vlastní aplikační protokoly, síťové porty a modely komunikace klient–server, peer-to-peer nebo jejich kombinace.

World Wide Web je jednou z těchto služeb. Spojuje adresy zdrojů, HTTP a hypertextové dokumenty; prohlížeč z přijatého HTML, CSS a JavaScriptu vytváří výsledné rozhraní. HTTPS chrání komunikaci pomocí TLS, zatímco cookies, relace a webová úložiště doplňují stav, který samotné HTTP neudržuje.

Nad webem fungují vyhledávače, které obsah nejprve objevují, indexují a teprve potom řadí. Výsledek vyhledávání proto není přímým obrazem celého webu ani automatickou zárukou pravdivosti. Stejný princip informační opatrnosti je důležitý u generativní AI: plynulá odpověď nebo automaticky vytvořená citace nenahrazuje ověření původního zdroje.

Internet se přitom dále vyvíjí. IPv6 rozšiřuje adresní prostor, IoT připojuje fyzická zařízení, nové modely webu mění způsob tvorby a vlastnictví služeb a generativní AI mění způsob práce s informacemi. Základní otázky však zůstávají stejné: **kde data vznikají, kudy procházejí, podle jakých pravidel se přenášejí, kdo je zpracovává a komu můžeme důvěřovat**.