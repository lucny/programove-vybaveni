## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vznik a princip World Wide Webu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Internet existoval dříve než web, ale práce s informacemi byla složitější a roztříštěná. Tim Berners‑Lee v CERNu navrhl systém, ve kterém dokumenty dostanou adresu a lze mezi nimi přecházet pomocí odkazů. Spojení hypertextu, otevřených standardů a internetu vytvořilo prostředí, které dnes používají miliardy lidí.

**Internet** je infrastruktura propojených sítí; **WWW** je jedna ze služeb, která ji využívá. Tim Berners‑Lee předložil v CERNu návrh webu v březnu **1989**. První webový prohlížeč a editor **WorldWideWeb** vznikl roku **1990** na počítači NeXT.

První webový server běžel na adrese `info.cern.ch`. Web spojuje dokumenty pomocí **hypertextových odkazů**. Tři základní stavební prvky jsou **HTML**, **URI/URL** a **HTTP**.

HTML popisuje strukturu obsahu, URL identifikuje zdroj a HTTP zajišťuje výměnu požadavků a odpovědí. Prohlížeč je klient, který získaný obsah interpretuje a vykresluje. Web se rychle rozšířil díky otevřenosti standardů a rozhodnutí CERNu zpřístupnit základní webový software bez licenčních poplatků.

Dne 30. dubna **1993** CERN uvolnil základní webový software do veřejné domény. Grafický prohlížeč **Mosaic** z roku 1993 pomohl web přiblížit široké veřejnosti.

***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**HTTP komunikace: klient a server**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Prohlížeč neobsahuje všechny stránky internetu. Po zadání adresy vyhledá server, odešle mu požadavek a z odpovědí postupně složí stránku. Jediná stránka může vyvolat desítky až stovky dalších požadavků na obrázky, styly, skripty, písma nebo data API. Pochopení tohoto rozhovoru je základem tvorby webu i diagnostiky problémů.

**HTTP** je aplikační protokol založený na výměně požadavků a odpovědí. **Klient** navazuje komunikaci a posílá požadavek; **server** požadavek zpracuje a odpoví. Požadavek obsahuje metodu, cíl požadavku, hlavičky a někdy tělo.

Odpověď obsahuje stavový kód, hlavičky a případně tělo s reprezentací zdroje. Metoda **GET** žádá reprezentaci zdroje; **POST** předává data ke zpracování podle pravidel služby. Hlavičky nesou metadata, například podporované formáty, typ obsahu, cache nebo autentizační údaje.

`Content-Type` popisuje formát těla, například `text/html` nebo `image/png`. Stavový kód shrnuje výsledek, například `200`, `404` nebo `500`. HTML dokument obvykle odkazuje na další zdroje, které prohlížeč vyžádá samostatně.

HTTP je bezstavové: význam každého požadavku lze chápat samostatně; stav aplikace doplňují cookies, tokeny či serverové relace. Server nemusí být jeden fyzický počítač a nemusí být vždy dostupný.

**HTTP zpráva má jasně oddělené části.** Požadavek obvykle obsahuje metodu, cíl požadavku, hlavičky a někdy tělo. Odpověď obsahuje stavový kód, hlavičky a případně tělo. Hlavička `Content-Type` popisuje formát těla, například `text/html` nebo `image/png`.

**Jedna stránka znamená mnoho požadavků.** První HTML dokument často obsahuje odkazy na obrázky, styly, skripty, písma nebo data API. Prohlížeč proto po získání hlavního dokumentu vytváří další samostatné HTTP požadavky.

***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**HTTP a HTTPS**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při přihlášení nebo platbě putují mezi prohlížečem a serverem citlivé údaje. Nezabezpečené HTTP je předává bez ochrany transportní vrstvy. HTTPS přidává TLS, které šifruje komunikaci, kontroluje její integritu a umožňuje ověřit identitu serveru pomocí certifikátu. Neříká však, že je web poctivý nebo bez chyb.

**HTTPS** je HTTP komunikace chráněná protokolem **TLS**. Šifrování omezuje možnost číst obsah komunikace cestou. Integrita umožňuje odhalit neoprávněnou změnu přenášených dat.

Autentizace serveru využívá certifikát a řetězec důvěry certifikačních autorit. Certifikát svazuje veřejný klíč s identitou, zejména s doménovými jmény. Prohlížeč kontroluje platnost certifikátu, jméno hostitele, podpis a další podmínky.

TLS naváže kryptografické klíče; obsah pak chrání efektivní symetrické šifrování. HTTPS běžně používá port 443, HTTP port 80. HTTPS nechrání kompromitovaný server, neodstraní malware ani neposoudí poctivost provozovatele.

Zámek znamená chráněné spojení k uvedenému hostiteli, nikoli automaticky bezpečný obchod. Část metadat komunikace může zůstat pozorovatelná, například IP cíle a objem provozu. Varování před neplatným certifikátem se nemá bez rozmyslu obcházet.

***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**HTTP metody a stavové kódy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Webový požadavek musí říct, co má server udělat, a odpověď musí oznámit výsledek. K tomu slouží HTTP metody a stavové kódy. Nejde jen o GET, POST, 200 a 404: přesné rozlišení bezpečných a idempotentních metod i skupin odpovědí pomáhá vytvářet spolehlivá API a rychleji hledat chyby.

**GET** žádá reprezentaci zdroje a má být bezpečnou metodou bez požadované změny stavu serveru. **HEAD** je podobné GET, ale server neposílá tělo odpovědi. **POST** předává data ke zpracování; jeho opakování může vytvořit více výsledků.

**PUT** typicky vytvoří nebo nahradí stav cílového zdroje a je idempotentní. **DELETE** žádá odstranění vazby na zdroj a je definováno jako idempotentní. Bezpečná metoda nemá žádat změnu stavu; idempotentní metoda má při opakování stejný zamýšlený účinek jako při jednom provedení.

Data v URL nejsou „vlastnost GET“; query lze použít i u jiných metod. Data v těle POST nejsou šifrována samotnou metodou — chrání je až HTTPS. `1xx` informuje, `2xx` značí úspěch, `3xx` další postup či přesměrování.

`4xx` znamená, že požadavek nelze splnit kvůli problému na straně požadavku či oprávnění. `5xx` označuje, že server při zpracování platného požadavku selhal. `200 OK`, `201 Created`, `204 No Content`, `301`, `302`, `400`, `401`, `403`, `404`, `429` a `500` patří k běžným kódům.

***

## Snímek 3.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Cookies, relace a webová úložiště**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


HTTP je bezstavové, přesto e-shop udrží košík a škola pozná přihlášeného uživatele. Webová aplikace si stav doplňuje pomocí cookies, serverových relací a úložišť v prohlížeči. Tyto mechanismy nejsou zaměnitelné: cookie se může automaticky posílat serveru, zatímco `localStorage` zůstává v prohlížeči, dokud jej skript výslovně nepoužije.

HTTP je bezstavové; stav aplikace se vytváří dalšími mechanismy. Server nastaví cookie hlavičkou `Set-Cookie`, prohlížeč ji může v dalších požadavcích vracet v hlavičce `Cookie`. Cookie je dvojice jméno–hodnota s pravidly rozsahu a platnosti.

**Relační cookie** bez `Expires` nebo `Max-Age` běžně zanikne po skončení relace prohlížeče; přesné obnovení relace může chování ovlivnit. **Trvalá cookie** má nastavenou dobu platnosti. Serverová **session** obvykle uchovává stav na serveru; cookie nese pouze náhodný identifikátor relace.

Identifikátor session nemá obsahovat heslo ani citlivá osobní data. `Secure` omezuje odesílání cookie na HTTPS, `HttpOnly` brání přístupu JavaScriptu a `SameSite` omezuje některé cross-site požadavky. `Path` a `Domain` určují rozsah, kam se cookie posílá.

**localStorage** ukládá řetězcová data pro daný origin a běžně přetrvá zavření prohlížeče. Data `localStorage` se neposílají automaticky s HTTP požadavkem, ale JavaScript stránky je může číst. Citlivé autentizační tokeny v `localStorage` jsou rizikové při XSS; pro session ID se obvykle doporučuje bezpečně nastavená `HttpOnly` cookie.

Cookies neslouží jen ke sledování; mohou být technicky nutné pro přihlášení, košík či preference.


# 4. Webové prohlížeče, bezpečnost a digitální stopa

> Prohlížeč není jen okno do internetu: načítá kód, vykresluje stránku, spouští programy, spravuje přihlášení a současně chrání zařízení před cizím obsahem.

Tato lekce vysvětluje, jak prohlížeč promění HTML, CSS a JavaScript ve výslednou stránku, jak fungují jeho hlavní ovládací prvky a vykreslovací enginy, co dokážou DevTools, jak chránit soukromí a jak vzniká digitální stopa.

***
