## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Internet a jeho služby**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Když sledujete video, posíláte e-mail nebo hrajete online hru, používáte pokaždé stejný internet, ale jinou službu. Internet je především infrastruktura a pravidla propojení sítí. Web, e-mail či videohovor jsou aplikace, které tuto infrastrukturu využívají. Rozlišení těchto vrstev pomáhá pochopit, proč může fungovat internetové připojení, i když konkrétní web nebo služba právě nefunguje.

**Internet** je globální propojení sítí založené na sadě protokolů TCP/IP. Fyzickou infrastrukturu tvoří optická a metalická vedení, rádiové spoje, routery, servery a datová centra. **Internetová služba** poskytuje konkrétní užitek: web, e-mail, přenos souborů, streaming, komunikaci či hry.

**WWW není internet**; je pouze jednou ze služeb provozovaných nad internetem. **Protokol** určuje pravidla komunikace mezi programy a zařízeními. Web běžně používá HTTP/HTTPS, e-mail několik poštovních protokolů a živá komunikace další protokoly.

Jedna služba může využívat více protokolů a jeden protokol může sloužit více aplikacím. Data různých služeb se přenášejí jako pakety přes společnou infrastrukturu. Výpadek jedné služby nemusí znamenat výpadek internetového připojení.

Rychlost služby ovlivňuje nejen přípojka, ale také server, trasa, zatížení sítě, latence a použitý protokol.

***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Internetové služby a protokoly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Počítač musí poznat nejen kam data poslat, ale také jak s nimi zacházet. E-mail je potřeba odeslat, uložit a synchronizovat, správce serveru potřebuje bezpečný vzdálený přístup a videohovor musí reagovat téměř okamžitě. Každá služba proto používá vhodné aplikační a transportní protokoly. Znalost jejich rolí pomáhá při konfiguraci programů i hledání chyb.

**Služba** popisuje, co uživatel získává; **protokol** popisuje pravidla komunikace. **SMTP** slouží k odesílání a předávání elektronické pošty. **IMAP** umožňuje pracovat se schránkou uloženou na serveru a synchronizovat její stav.

**POP3** stahuje zprávy; mazání ze serveru závisí na nastavení klienta, není povinné. **FTP** je tradiční protokol pro přenos souborů, ale sám nešifruje přihlašovací údaje ani data. **FTPS** je FTP zabezpečené pomocí TLS.

**SFTP** je samostatný protokol pro přenos souborů provozovaný typicky přes SSH; není „FTP přes SSH“. **SSH** poskytuje šifrovaný vzdálený přístup, spouštění příkazů a další bezpečné funkce. Telnet neposkytuje běžné šifrování a pro vzdálenou správu přes nedůvěryhodnou síť není vhodný.

**SIP** často zajišťuje navázání a řízení multimediální relace, zatímco **RTP** přenáší média. Konkrétní komunikační aplikace mohou používat vlastní kombinace a moderní protokoly, nejen SIP/RTP.

**Šifrování není jen zámek u názvu.** Ověřujte také certifikát, hostitelský klíč a důvěryhodnost serveru. Šifrované spojení s útočníkem není bezpečný cíl.

***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Síťové porty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


IP adresa přivede data ke správnému zařízení, ale na něm současně běží prohlížeč, poštovní klient, hra i další programy. Čísla portů pomáhají transportní vrstvě a operačnímu systému rozlišit jednotlivé komunikační konce. Port tedy není fyzická zásuvka, ale 16bitové číslo používané protokoly TCP, UDP a dalšími transporty.

Port je logický identifikátor v rozsahu **0–65535**. TCP a UDP mají oddělené prostory portů; stejné číslo může být registrováno pro oba protokoly. Spojení se rozlišuje kombinací protokolu, zdrojové a cílové IP adresy a zdrojového a cílového portu.

**Systémové porty** mají rozsah `0–1023`. **Uživatelské/registrované porty** mají rozsah `1024–49151`. **Dynamické/soukromé porty** mají rozsah `49152–65535`.

Server obvykle naslouchá na známém portu; klient používá dočasný zdrojový port. Běžné hodnoty: SSH `22/TCP`, SMTP `25/TCP`, DNS `53/UDP` i `53/TCP`, HTTP `80/TCP`, IMAP `143/TCP`, HTTPS `443/TCP` i `443/UDP`. Číslo portu je konvence, nikoli bezpečnostní záruka. Službu lze nakonfigurovat na jiné číslo.

Otevřený port znamená, že na dané kombinaci adresy a transportu pravděpodobně naslouchá služba; neříká, že je bezpečná. Firewall může provoz na portech povolit, omezit nebo blokovat.

***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Klient–server a peer-to-peer**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při návštěvě webu žádá prohlížeč server o obsah. Při sdílení v P2P síti může tentýž počítač data současně přijímat i poskytovat ostatním. Tyto modely určují, kde leží data, kdo řídí komunikaci, jak se systém rozšiřuje a kde vznikají rizika. Ve skutečnosti mnoho služeb používá hybridní architekturu, která kombinuje centrální koordinaci s přímou komunikací účastníků.

**Klient** zahajuje požadavek na službu; **server** požadavky přijímá a odpovídá. Klientem a serverem jsou role programů, ne nutně konkrétní typy počítačů. Model klient–server usnadňuje centrální správu, aktualizace, řízení přístupu a zálohování.

Jeden nedostatečně dimenzovaný server může být úzkým místem nebo jediným bodem selhání. Reálné služby riziko snižují replikací, load balancingem, cachemi a více datovými centry. V **peer-to-peer (P2P)** mohou uzly vystupovat současně jako klienti i servery.

P2P může rozdělit přenos a úložiště mezi mnoho účastníků. Dostupnost P2P zdroje závisí na počtu aktivních peerů, jejich kapacitě a pravidlech protokolu. P2P není automaticky anonymní, nelegální ani bezpečné; jde o architektonický model.

P2P síť může potřebovat centrální prvek pro vyhledávání, přihlášení nebo navázání spojení. **Hybridní model** kombinuje centrální služby a přímou komunikaci peerů.

***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**URL**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jediný řádek v adresním poli může určit způsob komunikace, server, port, cestu, parametry i místo uvnitř dokumentu. Správné čtení URL pomáhá při tvorbě webů, diagnostice i ochraně před phishingem. Rozhodující je zejména přesně poznat skutečný název hostitele, protože podvodná adresa může důvěryhodná slova schovat do cesty nebo subdomény.

**URL (Uniform Resource Locator)** identifikuje umístění zdroje a způsob, jak k němu přistoupit. Obecný příklad: `https://moodle.sspu-opava.cz:443/course/index.php?categoryid=3#sekce`. **Schéma** `https` určuje pravidla přístupu; běžně používá HTTP zabezpečené pomocí TLS.

**Hostitel** `moodle.sspu-opava.cz` je doménové jméno, které DNS může přeložit na IP adresu. Volitelný **port** následuje za dvojtečkou; výchozí port HTTPS je 443 a obvykle se nezapisuje. **Cesta** `/course/index.php` identifikuje zdroj v prostoru spravovaném serverem; nemusí odpovídat skutečné složce či souboru na disku.

**Query** začíná `?` a obvykle obsahuje dvojice `klíč=hodnota` oddělené znakem `&`. **Fragment** začíná `#` a označuje část výsledného zdroje; prohlížeč jej běžně neposílá v HTTP požadavku serveru. URL může obsahovat procentní kódování, například `%20` pro mezeru.


# 3. World Wide Web a HTTP

> Jak se z jednoduché sítě propojených dokumentů stal aplikační prostor pro weby, služby, přihlášení a interaktivní aplikace?

Tato lekce vysvětluje vznik World Wide Webu, základní princip komunikace HTTP, rozdíl mezi HTTP a HTTPS, význam metod a stavových kódů a mechanismy, které bezstavovému webu umožňují udržovat přihlášení, košík nebo uživatelské preference.

***
