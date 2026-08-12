## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**CMS je specializovaná webová aplikace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**CMS — Content Management System** umožňuje vytvářet, upravovat a publikovat obsah bez ručního editování HTML. WordPress je známý univerzální CMS v PHP, v ekosystému Pythonu existují systémy jako Django CMS nebo Wagtail. Redakční systém obvykle přidává workflow, role, média, šablony, revize a administraci.

Klasický CMS generuje veřejné stránky sám. **Headless CMS** odděluje správu obsahu od prezentační vrstvy a poskytuje obsah přes API. Jeden backend pak může zásobovat web, mobilní aplikaci i informační panel. Cena za flexibilitu je větší integrační složitost: někdo musí vytvořit frontend, řešit náhledy, cache, autentizaci a propojení při publikaci.

Page builder je jiný typ nástroje. Umožňuje vizuálně skládat layout a komponenty. Může urychlit práci editorů, ale při nekontrolovaném použití vytváří nekonzistentní design a složitá data. CMS proto není jen „program, ve kterém se kliká místo kódování“; je to systém pro správu obsahu a jeho životního cyklu.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**PWA, SPA, serverless a další architektury**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Progressive Web App — PWA** je webová aplikace využívající schopnosti platformy tak, aby se v podporovaném prostředí chovala více jako instalovatelná aplikace. Service Worker může řídit cache a offline scénáře, manifest popisuje instalaci a Web APIs mohou podle oprávnění nabídnout další integraci.

PWA není jeden framework ani záruka offline funkčnosti. Vývojář musí přesně navrhnout, co se má stát bez sítě a jak se synchronizují změny. Offline formulář, který uživateli dovolí napsat dlouhý text a po obnovení spojení jej ztratí, není dobrá PWA jen proto, že má ikonu na ploše.

**Serverless** znamená, že vývojář nasazuje funkce nebo služby bez přímé správy dlouhodobě běžícího serveru. Servery samozřejmě fyzicky existují; provozuje je platforma. Výhodou je automatické škálování a účtování podle využití, nevýhodou mohou být limity prostředí, cold start, cena při určitých vzorech zátěže a závislost na platformě.

Mikroslužby rozdělují systém do samostatně nasaditelných služeb. Pro globální bankovní platformu mohou být vhodné, pro školní aplikaci se třemi tabulkami však mohou přinést více síťové a provozní složitosti než užitku. **Monolit není synonymum špatné architektury**. Dobře modulární monolit je často nejjednodušší výchozí řešení a službu lze oddělit teprve tehdy, když existuje skutečný provozní důvod.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vývojový server není produkční server**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Příkaz `python manage.py runserver` je určen pro vývoj. Produkční aplikace potřebuje konfiguraci, která počítá s bezpečností, paralelními požadavky, restartem procesu, logováním a statickými soubory.

Django lze provozovat přes **WSGI** nebo modernější **ASGI** rozhraní. WSGI je tradiční synchronní rozhraní Python webových aplikací. ASGI podporuje také asynchronní komunikaci a dlouhodobější spojení. Aktuální Django má asynchronní API v řadě částí, ale neznamená to, že je potřeba každou view automaticky přepsat na `async def`. Asynchronní přístup dává největší smysl u I/O scénářů, které z něj skutečně těží.

Před aplikačním serverem může stát reverzní proxy nebo cloudový load balancer, který ukončuje HTTPS, směruje provoz a obsluhuje cache. Databáze může běžet jako spravovaná služba. Statické soubory lze posílat přes CDN a uživatelská média ukládat do objektového úložiště.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Hosting, VPS, kontejnery a PaaS**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Nejjednodušší webhosting bývá vhodný pro tradiční PHP nebo statické stránky, ale nemusí umožnit libovolně spouštět Pythonový proces. **VPS — Virtual Private Server** dává správci virtuální stroj a velkou kontrolu, zároveň však přenáší odpovědnost za aktualizace, firewall, zálohy a monitoring.

**Kontejner** zabalí aplikaci a její runtime závislosti do reprodukovatelného obrazu. Docker tím neřeší databázové zálohy ani bezpečnost automaticky; pomáhá především standardizovat prostředí mezi vývojem a produkcí.

**PaaS — Platform as a Service** umožňuje nasadit aplikaci bez správy většiny serverové infrastruktury. Platforma může zajistit build, HTTPS, restart procesů, logy a propojení s databází. Cloudové služby mohou poskytovat podobné funkce v různě modulární podobě.

Volba mezi VPS, kontejnerovou platformou a PaaS není soutěž o profesionalitu. Rozhoduje rozpočet, zkušenost týmu, požadovaná kontrola, způsob škálování a kritičnost služby.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Konfigurace produkce**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Django produkce vyžaduje několik principů, které se nemají odkládat „na později“. `DEBUG` musí být vypnutý, `ALLOWED_HOSTS` omezuje přijímané hostnames a tajné klíče nemají být ve veřejném repozitáři. HTTPS musí být správně vynuceno a cookie mají odpovídat bezpečnostnímu režimu.

Nastavení se často odděluje podle prostředí: vývoj může používat lokální SQLite a debug nástroje, produkce PostgreSQL, externí úložiště a bezpečné secrets. Cílem není mít dva různé programy, ale stejný kód s kontrolovanou konfigurací.

Před nasazením je vhodné spouštět frameworkové systémové kontroly, testy a databázové migrace. Nasazení by mělo být opakovatelné: když server selže, tým má umět z dokumentovaného postupu nebo automatizovaného pipeline vytvořit nový.

***

## Snímek 6.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Testování a automatizovaný průchod změny**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Webovou aplikaci nelze spolehlivě ověřit jediným klikáním v prohlížeči. **Jednotkové testy** kontrolují malé části logiky, například pravidlo pro výpočet ceny nebo oprávnění uživatele. **Integrační testy** sledují spolupráci více částí, třeba view, databáze a autentizace. **End-to-end test** simuluje celý uživatelský scénář: přihlášení, vyplnění formuláře a zobrazení výsledku. Každý typ zachytí jinou třídu chyb a není účelné nahrazovat všechny pouze jedním obřím testem.

Praktický význam testů se ukáže při změně. Vývojář upraví model článku, vytvoří migraci a současně změní formulář. Lokálně vše vypadá správně, ale starší část aplikace stále očekává původní pole. Automatizovaný test může tuto regresi zachytit dříve, než se kód dostane k uživatelům. Stejný princip platí pro bezpečnostní chyby: test může ověřit, že anonymní uživatel nedostane odpověď s cizími daty a že editor nemůže provést administrátorskou operaci.

V týmovém projektu se tyto kontroly často zapojují do **CI/CD — Continuous Integration / Continuous Delivery nebo Deployment**. Po každé změně repozitáře systém sestaví prostředí, spustí testy, statické kontroly a podle pravidel připraví nebo provede nasazení. CI/CD není samo o sobě záruka kvality; automatizuje pouze kroky, které tým správně definoval. Jeho hlavní hodnota spočívá v opakovatelnosti: stejná změna prochází stejným kontrolním řetězcem bez ohledu na to, kdo ji vytvořil.

***

## Snímek 6.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Provoz začíná po úspěšném deployi**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Aplikace, která prošla lokálními testy, může v produkci narazit na reálný provoz. Potřebuje proto **monitoring**, logování, zálohy a plán obnovy. Logy mají pomoci zjistit, co se stalo, ale nemají bezmyšlenkovitě ukládat hesla, session tokeny nebo osobní údaje.

Databázová záloha má hodnotu teprve tehdy, když lze obnovu skutečně provést. Stejně důležité je vědět, kolik dat se při havárii smí ztratit a jak dlouho může služba stát. Malý školní projekt může mít jednoduchý denní backup, kritická aplikace potřebuje propracovanější strategii.

Cache může snížit zátěž databáze a urychlit odpovědi, ale vytváří otázku, kdy se má stará hodnota zneplatnit. CDN přiblíží statická data uživateli, ale dynamickou autorizovanou odpověď nelze bez rozmyslu veřejně cacheovat. Škálování tedy není jen „přidat další server“; musí respektovat stav, databázi a konzistenci.

***

## Snímek 6.8

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**AI jako další služba v architektuře**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Současné webové aplikace stále častěji přidávají funkce založené na generativní AI: shrnutí článku, vyhledávání v přirozeném jazyce, klasifikaci, překlad nebo asistenta. Z architektonického pohledu je užitečné považovat model za další externí nebo interní službu s API, latencí, cenou, limity a chybovostí.

Výstup modelu není důvěryhodný programový příkaz jen proto, že vznikl uvnitř aplikace. Pokud AI vytvoří HTML, SQL, URL nebo argument pro další nástroj, musí projít stejnou kontrolou jako jiné nedůvěryhodné vstupy. Stejně tak citlivá data nemají být automaticky posílána cizí službě bez posouzení ochrany soukromí a smluvních podmínek.

AI tak nepřepisuje základní pravidla webového inženýrství. Naopak zvýrazňuje jejich význam: jasně definované rozhraní, validace, autorizace, audit a odpovědnost za výsledek zůstávají podstatné.

# Závěrečné propojení

Webová aplikace je spolupráce vrstev, které musí mít jasně rozdělenou odpovědnost. Prohlížeč zobrazuje rozhraní a posílá požadavky. Routing určuje, která část backendu je zpracuje. View nebo služba ověří vstup a oprávnění, model a ORM pracují s databází a šablona nebo API sestaví odpověď. Session a autentizace propojí jednotlivé požadavky s uživatelem a bezpečnostní mechanismy chrání hranice mezi nedůvěryhodným vstupem a citlivou operací.

Celý cyklus lze shrnout:

**požadavek → routing → autentizace a autorizace → aplikační logika → ORM/databáze → odpověď → render → další uživatelská akce**

Framework jako Django tento proces výrazně usnadňuje, ale nenahrazuje porozumění principům. ORM neodstraňuje potřebu rozumět databázi, automatické escapování neznamená konec XSS a vestavěné přihlášení neřeší chybně navržená oprávnění. Stejně tak Docker, cloud nebo serverless neodstraňují provozní odpovědnost — pouze ji jinak rozdělují.

Nejdůležitější schopností proto není zapamatovat si soubor `views.py` nebo jeden příkaz pro deploy. Je to schopnost sledovat, **kde se data právě nacházejí, kdo jim může věřit, kdo o jejich použití rozhoduje a co se stane při chybě**. Tento mentální model zůstane platný i tehdy, až konkrétní frameworky a cloudové služby vystřídají nové generace nástrojů.

## Referenční zdroje pro další studium

- Django Documentation — https://docs.djangoproject.com/
- OWASP Top 10 — https://owasp.org/Top10/
- OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/
- MDN Web Security — https://developer.mozilla.org/en-US/docs/Web/Security
- WebAuthn — https://www.w3.org/TR/webauthn-3/

***
