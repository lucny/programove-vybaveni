# Vývojářské nástroje a verzovací systémy

# 1. Fáze tvorby programu a vývojářské nástroje

Vývoj softwaru probíhá v několika fázích, přičemž každá z nich vyžaduje specifické nástroje pro efektivní řízení a realizaci projektu.

## 1.1 Návrh a plánování

- **Význam:** V této fázi se definuje struktura aplikace, algoritmy a logika programu.
- **Používané nástroje:**
  - **UML (Unified Modeling Language)** – standardizovaný jazyk pro vizualizaci návrhu pomocí diagramů.
  - Existují diagramy pro různé účely, např. **diagram tříd** pro modelování tříd a vztahů mezi nimi, **diagramy aktivit** pro popis procesů a toku dat, **diagramy stavů** pro modelování stavů objektů apod.
  - Modelovací nástroje jako **draw.io** nebo **DIA** pro schémata a databázové diagramy.

## 1.2 Psaní a ladění programového kódu

- **Význam:** Samotné programování ve zvoleném jazyce.
- **Používané nástroje:**
  - **IDE (Integrated Development Environment)** umožňuje psaní, ladění a testování kódu v rámci jednoho prostředí.
  - **Textové editory** jako Visual Studio Code, Sublime Text nebo Atom pro psaní kódu.
  - **Konzolové editory** jako Vim nebo Nano pro rychlé úpravy skriptů.

## 1.3 Testování programů

- **Význam:** Zajištění správné funkčnosti aplikace a odstranění chyb.
- **Používané nástroje:**
  - K testování se používají různé nástroje, jako jsou xUnit nebo JUnit pro testování jednotek kódu (tzv. unit testy), Selenium pro testování webových stránek nebo Postman pro testování API.

## 1.4 Správa verzí a spolupráce

- **Význam:** Umožňuje týmový vývoj, sledování změn a návrat k předchozím verzím kódu.
- **Používané nástroje:**
  - **Git** pro verzování zdrojového kódu.
  - Platformy jako **GitHub** pro sdílení a spolupráci na projektech.

## 1.5 Dokumentace

- **Význam:** Zajištění srozumitelnosti a udržitelnosti kódu.
- **Používané nástroje:**
  - **Markdown** – speciální značkovací jazyk pro psaní jednoduchých textových dokumentů.
  - **Sphinx** pro generování dokumentace z komentářů v kódu (např. v Pythonu).
  - Existují i cloudové platformy jako **Read the Docs** pro sdílení dokumentace.

# 2. IDE, pomůcky pro editaci a refaktorování kódu

## 2.1 Co je IDE a proč je důležité?

- **Integrované vývojové prostředí (IDE)** kombinuje editor kódu, kompilátor, debugger a další nástroje do jednoho rozhraní.
- Součástí IDE jsou obvykle:
  - **Debugger:** umožňuje programátorům ladit svůj kód a hledat a opravovat chyby v aplikaci.
  - **Integrace s verzovacím systémem:** umožňuje programátorům pracovat s různými verzemi kódu a synchronizovat své změny s ostatními členy týmu.
  - **Automatické sestavování a testování:** umožňuje programátorům sestavit aplikaci z kódu a spustit automatické testy na základě definovaných specifikací.
  - **Správce balíčků:** umožňuje programátorům snadno instalovat a spravovat knihovny a závislosti používané v aplikaci.

## 2.2 Editační pomůcky

- **Automatické doplňování kódu** – šetří čas při psaní opakujících se struktur.
- **Snippets** – šablony kódu, které usnadňují opakující se úkoly.
- **Zvýrazňování syntaxe** – zvýrazňuje klíčová slova a struktury pro lepší čitelnost kódu.
- **Code linting** – nástroje jako ESLint analyzují kód a upozorňují na potenciální chyby.
- **Navigace v kódu** – umožňuje rychlé hledání funkcí, tříd a proměnných.

## 2.3 Refaktorování kódu

Refaktorování je proces **změny struktury kódu bez změny jeho vnější funkcionality**. Cílem je zlepšit čitelnost, udržitelnost a efektivitu kódu.

Pro refaktorování kódu se používají různé techniky:

- **Zjednodušení a zpřehlednění kódu**, odstranění duplicit, zlepšení názvů proměnných a funkcí.
- **Optimalizace kódu** pro lepší výkon a efektivitu, např. nahrazení pomalých algoritmů rychlejšími.
- **Odstranění zbytečného kódu** a nepoužívaných funkcí.
- **Rozdělení kódu do menších funkcí** pro lepší modularitu a znovupoužitelnost.

# 3. Nástroje pro ladění a testování kódu, vývoj řízený testy

## 3.1 Ladění kódu (debugging)

Proces hledání a opravování chyb v kódu s využitím různých nástrojů a technik.

- **Nástroje pro debugging:**
  - **Debugger v IDE** umožňuje sledovat hodnoty proměnných, krokovat kód a zastavit běh programu v určitých bodech (breakpoints).
  - **Logování** – výpis informací o průběhu programu do konzole nebo souboru.
  - **Výjimky a chybová hlášení** – zprávy o chybách v kódu, které pomáhají identifikovat problémové části. Používá se např. `try...except` v Pythonu.

## 3.2 Testování kódu

- **Automatizované testy** zajišťují, že změny kódu neovlivní jeho správnou funkčnost. Patří k nim např.:
  - **Unit testy** – testování jednotlivých částí kódu (funkcí, tříd) odděleně s využitím testovacích frameworků jako `unittest` (Python) nebo JUnit (Java). Principem je ověření, zda daná část kódu funguje správně. Dosahuje se toho pomocí tzv. **assertions** (tvrzení), které porovnávají očekávané a skutečné hodnoty.
  - **Integrační testy** – testování interakcí mezi různými částmi aplikace, např. testování API nebo databázových operací.
  - **Funkční testy** – testování aplikace z pohledu uživatele (UI testy), např. simulace interakcí s webovou stránkou nebo desktopovou aplikací.
  - **Testování výkonu** – měření rychlosti a efektivity aplikace za různých podmínek.

## 3.3 Vývoj řízený testy (TDD – Test-Driven Development)

- Nejprve se píše test, poté se implementuje kód, který jej splňuje.
- Přispívá k lepší udržitelnosti kódu a snazšímu refaktorování.
- V praxi se TDD používá při vývoji softwaru, kde je klíčové zajistit správnou funkčnost a minimalizovat chyby. Příkladem je vývoj webových aplikací nebo knihoven.

# 4. Správa závislostí, virtuální prostředí, kontejnery

## 4.1 Správa závislostí

- Závislostmi se rozumí knihovny, balíčky a moduly, které jsou potřebné pro běh aplikace.
- Správa závislostí zajišťuje, že jsou všechny potřebné knihovny nainstalovány a aktualizovány.
- Příkladem nástroje pro správu závislostí je **npm (Node.js Package Manager)** pro JavaScript nebo **pip** pro Python.
- V Pythonu se pro správu závislostí používá soubor `requirements.txt`, kde jsou uvedeny všechny potřebné knihovny a jejich verze.
- V Node.js se pro správu závislostí používá soubor `package.json`, kde jsou uvedeny závislosti a další informace o projektu.

## 4.2 Virtuální prostředí

- **Izoluje závislosti projektu**, aby se zabránilo konfliktům mezi různými verzemi knihoven.
- Umožňuje **snadnou migraci projektu** na jiné zařízení nebo sdílení s ostatními vývojáři.
- V Pythonu se pro vytvoření virtuálního prostředí používá nástroj **virtualenv** nebo **venv**.
- Součástí virtuálního prostředí je **izolovaný Python interpreter a oddělený adresář s knihovnami** pro daný projekt.

## 4.3 Kontejnerizace (Docker, Kubernetes)

- Kontejnerizace umožňuje **snadné nasazení aplikací a izolaci prostředí** mezi vývojem a produkčním prostředím.
- **Docker** je platforma pro vytváření, nasazování a běh kontejnerů.
- **Kontejner** obsahuje aplikaci a její uživatelské závislosti, ale sdílí jádro operačního systému hostitele. Kontejnery jsou **přenositelné a izolované**, což pomáhá zajistit konzistentní běh aplikace napříč různými prostředími.
- **Dockerfile** je soubor, který popisuje, jak sestavit obraz (*image*). Kontejner je běžící instance vytvořená z tohoto obrazu. Obrazy lze sdílet a nasazovat do různých prostředí.
- **Docker Compose** je nástroj pro definici a spouštění více kontejnerů jako jednoho celku. Příkladem může být aplikace s databází a webovým serverem. Konfigurace je uložena v souboru `docker-compose.yml`. Jeho spuštěním (pomocí příkazu `docker-compose up`) se vytvoří a spustí všechny kontejnery podle definice.
- **Kubernetes** je orchestrátor kontejnerů, který umožňuje spravovat a škálovat kontejnery v různých prostředích.

# 5. Verzovací systémy, jejich funkce a využití v praxi

## 5.1 Verzovací systém

- Umožňuje **správu verzí kódu a sledování změn** v jednotlivých souborech. Patří k základním nástrojům pro vývoj softwaru a spolupráci v týmu.
- **Centrální systémy** mají jeden centrální repozitář, ke kterému se připojují vývojáři. Příkladem je **Subversion (SVN)**.
- **Distribuované systémy** mají každý vývojář svůj vlastní repozitář a mohou pracovat offline. Příkladem je **Git**.
- K důležitým funkcím verzovacích systémů patří:
  - **Historie změn** – zaznamenávání a ukládání změn v kódu s popisky a časovými razítky (commity).
  - **Větvení a slučování** – umožňuje pracovat na různých částech kódu současně (branches) a následně sloučit změny do jednoho celku (merge).
  - **Sdílení a spolupráce** – umožňuje více vývojářům pracovat na jednom projektu a synchronizovat své změny (push, pull).
  - **Zpětné získání verzí** – umožňuje se vrátit k předchozím verzím kódu a porovnávat změny mezi nimi (diff).
- **Git** je nejpoužívanějším distribuovaným verzovacím systémem, který je oblíbený pro svou rychlost, flexibilitu a širokou podporu.
- **GitHub** je platforma pro sdílení a spolupráci na projektech postavených na Gitu. Umožňuje vytvářet repozitáře, spravovat issues a pull requests a sdílet kód s ostatními.

## 5.2 Využití v praxi

- **Individuální vývoj:** Snadná správa verzí kódu při dlouhodobém vývoji.
- **Týmová spolupráce:** Každý člen týmu může pracovat na samostatné větvi a následně provést **sloučení změn (merge)**.
- **Open-source projekty:** Sdílení kódu na platformách jako **GitHub** nebo **GitLab**.

# 6. Využití umělé inteligence při programování

## 6.1 Od automatického doplňování k AI asistentovi

Nástroje založené na **umělé inteligenci (AI)** se staly součástí současného vývojového prostředí. Mohou pomáhat při psaní a vysvětlování kódu, hledání chyb, tvorbě testů, refaktoringu i práci s rozsáhlejším projektem. Nejde však o náhradu znalostí programátora. Vygenerovaný kód je nutné chápat, ověřovat a testovat stejně jako kód napsaný člověkem.

Klasické vývojové prostředí již dlouho nabízí **automatické doplňování kódu (autocomplete)**, zvýraznění syntaxe, navigaci mezi symboly nebo statickou analýzu. Tyto nástroje obvykle pracují podle syntaxe jazyka, typů, názvů funkcí a informací dostupných v projektu.

AI asistenti tento princip rozšiřují. Dokážou pracovat s přirozeným jazykem a na základě kontextu navrhovat celé bloky programu, vysvětlovat existující kód nebo provádět změny ve více souborech.

Vývoj lze zjednodušeně popsat jako postup:

**automatické doplňování → generování kódu → konverzační asistent → programovací agent**

- **Automatické doplňování** navrhuje názvy funkcí, metod, proměnných nebo krátké části kódu.
- **Generování kódu** vytváří delší úseky programu podle komentáře nebo zadání v přirozeném jazyce.
- **Konverzační asistent** umožňuje o projektu diskutovat, ptát se na význam kódu nebo požadovat konkrétní úpravy.
- **Programovací agent** může dostat širší úkol, prozkoumat projekt, změnit více souborů, spustit příkazy nebo testy a podle jejich výsledků další postup upravit.

Příklady současných nástrojů zahrnují například **GitHub Copilot, OpenAI Codex, Claude Code** nebo AI funkce integrované přímo do vývojových prostředí. Konkrétní produkty se rychle mění, důležitější je proto pochopit obecný princip jejich práce.

## 6.2 AI při psaní, vysvětlování a úpravách kódu

AI může při programování zastávat několik různých rolí. Nejjednodušší je pomoc při psaní nového kódu. Programátor může například zadat:

> Vytvoř funkci v Pythonu, která načte CSV soubor, odstraní prázdné řádky a vrátí seznam slovníků.

AI může připravit návrh funkce, který programátor dále upraví a otestuje. Stejným způsobem lze využít AI také k vysvětlení cizího nebo staršího kódu, doplnění komentářů a dokumentace, návrhu refaktoringu nebo převodu jednoduchého řešení mezi programovacími jazyky.

Mezi běžné možnosti patří:

- **generování nového kódu** podle slovního popisu,
- **doplňování rozepsaných funkcí** a opakujících se konstrukcí,
- **vysvětlení existujícího kódu** krok za krokem,
- **refaktoring** bez změny vnějšího chování programu,
- **tvorba dokumentace** a komentářů,
- **převod jednoduchých částí programu** mezi různými jazyky nebo knihovnami,
- **návrh alternativního řešení** stejného problému.

Kvalita výsledku silně závisí na kvalitě zadání a dostupném kontextu. Obecný požadavek „napiš program“ obvykle poskytne horší výsledek než přesnější specifikace obsahující účel, vstupy, očekávané výstupy, omezení a prostředí, ve kterém má kód fungovat.

Užitečné zadání proto často obsahuje:

**cíl → vstup → očekávaný výstup → omezení → relevantní kontext projektu**

AI nedokáže automaticky poznat všechny nevyřčené požadavky. Pokud například neví, jaké verze knihoven projekt používá nebo jak je uspořádána jeho architektura, může navrhnout řešení, které do projektu nezapadne.

## 6.3 AI při ladění, testování a code review

AI lze využít také při hledání chyb. Programátor může modelu předložit chybovou zprávu, relevantní část kódu a popis očekávaného chování. AI může navrhnout možné příčiny problému a postup, jak jednotlivé hypotézy ověřit.

Rozumný pracovní postup může vypadat takto:

**chyba → reprodukce → hypotéza → test → oprava → nové spuštění testů**

Důležitá je právě **reprodukce chyby**. Pokud programátor nedokáže popsat, kdy problém nastává, může AI pouze hádat. Stejně jako při běžném ladění je proto vhodné nejprve určit konkrétní vstup a situaci, která chybu vyvolá.

AI může pomoci také při testování:

- navrhnout **unit testy** pro jednotlivé funkce,
- hledat **hraniční případy** (*edge cases*),
- generovat testovací data,
- vysvětlovat příčinu selhání testu,
- navrhovat testy pro chybu, která byla právě opravena,
- kontrolovat změny při **code review**.

Například pro funkci, která počítá průměr hodnot, nestačí otestovat pouze běžný seznam čísel. AI může upozornit také na prázdný seznam, záporné hodnoty, velmi velká čísla nebo chybný datový typ.

AI však **nenahrazuje debugger ani automatické testy**. Její návrh je hypotéza, kterou je třeba ověřit spuštěním programu, testů nebo kontrolou skutečného stavu proměnných.

## 6.4 Agentní programování: když AI dostane celý úkol

Pokročilejší AI nástroje mohou fungovat jako **programovací agenti**. Místo vytvoření jednoho úseku kódu dostanou širší úkol a samostatně provedou více kroků.

Příklad zadání:

> Přidej do aplikace export dat do CSV. Nejprve prozkoumej strukturu projektu, navrhni postup, proveď potřebné změny, přidej testy a na závěr shrň změněné soubory.

Agent může podle dostupných oprávnění:

1. prohledat soubory projektu,
2. najít relevantní části kódu,
3. vytvořit plán změn,
4. upravit jeden nebo více souborů,
5. spustit kompilaci, linter nebo testy,
6. vyhodnotit vzniklé chyby,
7. provést další opravy,
8. připravit souhrn změn nebo diff k lidské kontrole.

Typický agentní cyklus lze vyjádřit:

**zadání → plán → změna → spuštění → kontrola výsledku → oprava → diff → lidské schválení**

Tento způsob práce se liší od běžného chatování s AI především tím, že model používá **nástroje**. Může například číst a zapisovat soubory, vyhledávat v projektu, spouštět příkazy v terminálu nebo pracovat s verzovacím systémem.

S rostoucí samostatností agenta roste také význam kontroly. Agent může velmi rychle provést rozsáhlou změnu, ale stejnou rychlostí může rozšířit i chybný předpoklad do více částí projektu.

## 6.5 Kontext projektu, instrukce a spolupráce s AI

AI pracuje pouze s informacemi, které má v daném okamžiku k dispozici. **Kontext** proto patří k nejdůležitějším faktorům ovlivňujícím kvalitu výsledku.

Pro práci nad skutečným projektem může být důležité, aby AI znala například:

- účel a architekturu projektu,
- používaný programovací jazyk a framework,
- způsob instalace závislostí,
- strukturu adresářů,
- pravidla pojmenování a formátování kódu,
- způsob spouštění a testování aplikace,
- části systému, které se nemají měnit,
- očekávané chování výsledku.

Tyto informace mohou být uloženy přímo v projektu. Význam mají například soubory `README.md`, technická dokumentace, testy, konfigurace projektu nebo specializované **instrukční soubory pro AI agenty**.

Dobře organizovaný projekt tak pomáhá nejen lidem, ale také AI. Pokud jsou názvy proměnných srozumitelné, moduly mají jasné odpovědnosti, testy popisují očekávané chování a dokumentace vysvětluje způsob spuštění, AI se v projektu orientuje podstatně lépe.

S AI lze proto pracovat podobně jako s novým členem vývojového týmu. Nestačí mu sdělit pouze „oprav projekt“. Potřebuje znát pravidla, omezení, dostupné nástroje a způsob, podle kterého lze poznat, že je úkol splněn.

## 6.6 Proč AI kód nemůžeme slepě přijímat

Kód vytvořený AI může na první pohled působit velmi přesvědčivě, ale stále může obsahovat chyby. Model generuje pravděpodobné řešení na základě zadaného kontextu a naučených vzorů; nemá automatickou záruku, že navržený program skutečně odpovídá požadavkům.

Mezi typická rizika patří:

- použití **neexistující funkce nebo API**,
- použití zastaralého způsobu práce s knihovnou,
- nesprávné pochopení zadání,
- přehlédnutí hraničních případů,
- zavedení bezpečnostní chyby,
- vytvoření zbytečně složitého řešení,
- změna jiné části programu, která s původním úkolem nesouvisí,
- kód, který sice projde některými testy, ale porušuje architekturu projektu.

Každou významnější AI změnu je proto vhodné podrobit stejnému procesu jako změnu vytvořenou člověkem:

1. **přečíst a pochopit změněný kód,**
2. zkontrolovat **diff**, tedy přesný rozdíl oproti předchozí verzi,
3. spustit program, kompilaci nebo statickou kontrolu,
4. spustit automatické testy,
5. podle potřeby provést bezpečnostní nebo výkonovou kontrolu,
6. teprve potom změnu uložit do verzovacího systému.

Verzovací systém je při práci s AI mimořádně užitečný. Před větší změnou lze vytvořit samostatnou větev a po práci agenta přesně zkontrolovat, co změnil. Pokud je výsledek chybný, lze změny snadno zahodit nebo se vrátit k předchozí verzi.

Základní princip lze shrnout:

**AI může kód navrhnout nebo upravit, ale odpovědnost za jeho přijetí zůstává na vývojáři.**

Využití AI při programování proto nejlépe funguje jako propojení všech nástrojů popsaných v tomto materiálu:

**IDE poskytuje pracovní prostředí → testy ověřují chování → Git uchovává a porovnává změny → AI pomáhá změny navrhovat a provádět → programátor výsledek chápe, kontroluje a schvaluje.**
