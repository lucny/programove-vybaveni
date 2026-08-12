## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak prohlížeč promění kód ve stránku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Webová stránka nepřichází do počítače jako hotový obrázek. Prohlížeč získá HTML, CSS, JavaScript a média, vytvoří z nich vnitřní datové struktury, vypočítá rozložení a výsledek vykreslí. Je současně síťovým klientem, interpretem webových standardů, prostředím pro programy i bezpečnostní bariérou mezi stránkou a zařízením.

Prohlížeč je **webový klient**, který odesílá požadavky a zpracovává odpovědi. HTML popisuje obsah a strukturu dokumentu, nikoli jeho kompletní vzhled. Prohlížeč parsuje HTML a vytváří strom **DOM**.

CSS určuje prezentaci, rozložení, typografii a přizpůsobení různým obrazovkám. Z CSS vzniká interní model stylů; společně s DOM ovlivňuje výsledný render tree. Při **layoutu** prohlížeč vypočítá velikost a polohu viditelných prvků.

Při **paintu** kreslí pixely; vrstvy mohou být následně složeny při compositingu. JavaScript může měnit DOM, styly, reagovat na události a komunikovat se serverem. JavaScript není nutný pro každou stránku; kvalitní statický obsah může fungovat i bez něj.

HTML dokument může vyvolat další požadavky na CSS, skripty, obrázky, písma a data. Různé prohlížeče mají odlišné implementace, ale řídí se společnými webovými standardy. Renderování je průběžný proces: prohlížeč může zobrazovat část obsahu ještě před úplným stažením.

***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rozhraní a ekosystém webových prohlížečů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Adresní řádek, karty, historie, profily a rozšíření vypadají jako běžné ovládací prvky, ale každý z nich souvisí se soukromím a bezpečností. Pod podobným povrchem navíc různé prohlížeče sdílejí nebo vyvíjejí odlišná jádra. Znalost rozhraní a enginů pomáhá při volbě prohlížeče, testování webů i řešení problémů s kompatibilitou.

Adresní řádek často funguje jako **omnibox**: přijímá URL i hledané výrazy. Před potvrzením je vhodné zkontrolovat skutečný hostitel a schéma HTTPS. Tlačítka zpět a vpřed procházejí historii dané karty; obnovení znovu načte nebo ověří zdroj.

Karty oddělují více otevřených dokumentů, ale mohou sdílet profil, cookies a oprávnění. Záložka ukládá odkaz; stažená „offline stránka“ či cache ukládá také obsah. Profil může synchronizovat historii, hesla, karty a nastavení prostřednictvím účtu poskytovatele.

Rozšíření získávají oprávnění a mohou ovlivňovat obsah stránek; instalujte jen potřebná a důvěryhodná. **Blink** používají Chromium, Chrome, Edge, Opera a Brave; jednotlivé prohlížeče se přesto liší funkcemi a nastavením. Firefox používá engine **Gecko** a JavaScriptový engine SpiderMonkey.

Safari používá **WebKit** a JavaScriptCore. Tor Browser je upravený Firefox zaměřený na použití sítě Tor; není to samostatný vykreslovací engine. DuckDuckGo je také vyhledávač; jeho prohlížeče mohou podle platformy využívat systémové enginy.

Rozmanitost enginů pomáhá odhalovat chyby kompatibility a omezuje závislost webu na jediné implementaci.

***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**DevTools: digitální rentgen webové stránky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Vývojářské nástroje ukazují rozdíl mezi tím, co vidí uživatel, a tím, co prohlížeč skutečně zpracovává. Lze prohlížet DOM a CSS, sledovat požadavky, číst chyby, měřit výkon a simulovat různé obrazovky. Úpravy jsou většinou pouze místní a dočasné — DevTools nejsou způsob, jak změnit cizí server.

DevTools otevřete často klávesou `F12` nebo `Ctrl+Shift+I`. **Elements/Inspector** zobrazuje aktuální DOM a aplikované CSS. DOM v DevTools nemusí být totožný s původním HTML, protože jej upravil parser nebo JavaScript.

Místní změna textu či stylu obvykle zmizí po obnovení a nemění server. **Console** zobrazuje chyby a umožňuje spouštět JavaScript v kontextu stránky. Do konzole nevkládejte cizí kód, kterému nerozumíte; může pracovat s přihlášenou relací.

**Network** ukazuje požadavky, metody, stavové kódy, hlavičky, časování a velikosti. Záznam Network často začíná až po otevření nástrojů a obnovení stránky. **Sources/Debugger** umožňuje číst skripty, zastavit běh a krokovat program.

**Performance** pomáhá hledat dlouhé úlohy, vykreslování a problémy s odezvou. Režim zařízení simuluje viewport a některé vlastnosti, ale nenahrazuje test na skutečném telefonu. DevTools mohou zobrazit cookies, tokeny a další citlivá data; snímky obrazovky je nutné před sdílením zkontrolovat.

**DevTools mění hlavně místní pohled.** Úprava textu, CSS nebo atributů v panelu Elements se obvykle projeví jen v paměti konkrétního prohlížeče. Po obnovení se stránka znovu sestaví z dat serveru a lokální změny zmizí. Změna ceny v DOM proto nemění databázi ani skutečnou transakci.

***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Bezpečnost a soukromí v prohlížeči**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Prohlížeč spravuje hesla, relace, historii, platby i přístup ke kameře a mikrofonu. Současně spouští kód z cizích webů a rozšíření. Bezpečnost proto nevytváří jediný „anonymní režim“, ale vrstvy: aktualizace, HTTPS, izolace webů, správná oprávnění, ochrana účtu a promyšlená práce s cookies a doplňky.

Aktualizace opravují známé zranitelnosti prohlížeče a jeho komponent. HTTPS chrání přenos k uvedenému hostiteli, ale nezaručuje poctivý obsah. Soukromé/anonymní okno omezuje hlavně ukládání místní historie a dat po skončení relace.

Soukromý režim neskrývá provoz před navštíveným webem, školou, zaměstnavatelem ani poskytovatelem sítě. Stažené soubory a vytvořené záložky mohou po zavření soukromého okna zůstat. Cookies první strany mohou držet přihlášení a preference; cookies či jiné mechanismy třetích stran mohou sledovat uživatele napříč weby.

Blokování cookies třetích stran omezuje část sledování, ne všechny techniky fingerprintingu. Rozšíření může číst a měnit stránky v rozsahu udělených oprávnění. Důvěryhodné rozšíření se může změnit aktualizací nebo změnou vlastníka.

Oprávnění ke kameře, mikrofonu, poloze a oznámením mají být udělena jen potřebným webům. Správce hesel pomáhá používat dlouhá unikátní hesla; účet chraňte vícefaktorovým ověřením. Mazání cookies může odhlásit uživatele, ale neodstraní data již uložená na serverech.

***

## Snímek 4.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Digitální stopa a paměť webu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Smazání historie odstraní seznam navštívených stránek z vašeho prohlížeče, ale nevrátí odeslaný příspěvek, nesmaže serverové logy ani kopie u jiných lidí. Digitální stopa vzniká vědomou aktivitou i automatickým zpracováním technických údajů. Ne všechno zůstane navždy, ale nad zveřejněnými daty rychle ztrácíme úplnou kontrolu.

**Historie prohlížení** je místní záznam navštívených adres v konkrétním profilu prohlížeče. Její smazání neodstraňuje záznamy na serverech, DNS resolverech, školní bráně ani synchronizovaných účtech. **Aktivní digitální stopa** vzniká například zveřejněním příspěvku, komentáře, fotografie či formuláře.

**Pasivní stopa** zahrnuje technická a analytická data sbíraná při používání služby. IP adresa, čas, typ zařízení, přibližná poloha, cookies a fingerprint mohou pomoci spojovat události. Metadata mohou prozradit více než samotný obsah, například čas, místo a sociální vazby.

Kopie mohou vzniknout sdílením, snímkem obrazovky, cache, zálohou, vyhledávačem nebo archivací. **Wayback Machine** archivuje část veřejného webu od roku 1996, nikoli celý internet ani každou stránku. Některé stránky nejsou archivovány kvůli technickým omezením, pravidlům, přihlášení nebo žádosti provozovatele.

Digitální stopa není vždy „nesmazatelná“, ale úplné dohledání a odstranění všech kopií může být obtížné či nemožné. Omezování stopy začíná minimalizací sdílených dat, nastavením publika a pravidelným auditem účtů. Práva na přístup, opravu či výmaz osobních údajů mají výjimky a neznamenají automatické odstranění všech veřejných archivů.

# 5. Vyhledávače, SEO a informační gramotnost

> Vyhledávač neukazuje celý web ani čistou pravdu. Nabízí výběr dokumentů, reklam a odpovědí vytvořený z indexu podle konkrétního dotazu, kontextu a pravidel řazení.

Tato lekce vysvětluje, jak vyhledávače objevují stránky, vytvářejí index, řadí výsledky a kombinují organický obsah s reklamou. Současně rozvíjí praktické dovednosti efektivního hledání, ověřování zdrojů a ochrany soukromí.

***
