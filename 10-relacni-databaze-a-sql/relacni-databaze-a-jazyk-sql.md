# Relační databáze a jazyk SQL

> Redakční systém na první pohled pracuje s textem, obrázky a webovými stránkami. V jeho pozadí však musí někdo spolehlivě uchovat články, autory, rubriky, štítky, pracovní verze i okamžik publikování. Relační databáze dává těmto údajům strukturu a pravidla; jazyk SQL umožňuje strukturu vytvořit, data měnit a klást nad nimi otázky.

Představme si internetový magazín. Autor rozepsaný článek uloží, editor jej zkontroluje, šéfredaktor schválí a systém jej v určený čas zveřejní. Článek patří do rubriky, může mít více štítků a během práce vzniká několik revizí. Veřejný web přitom smí zobrazit jen publikovaný obsah, zatímco redakce potřebuje i koncepty a historii změn. Tento jeden příklad bude provázet celý text: od prvního datového modelu přes SQL až po správu, zabezpečení a výběr vhodného databázového systému.

# Lekce 1: Data jako tabulky, vztahy a pravidla

## 1.1 Proč redakci nestačí jeden soubor

Malý web může zpočátku ukládat články do samostatných souborů nebo do jedné tabulky. S rostoucím počtem autorů se však objeví otázky, na které takové uspořádání odpovídá obtížně. Které články napsala určitá autorka? Kolik jich vyšlo v jednotlivých rubrikách? Které koncepty čekají na schválení? Co se stane se jménem autora ve stovkách článků, když si je změní?

Relační databáze rozděluje různé druhy skutečností do samostatných **relací**, v běžné praxi reprezentovaných tabulkami. Údaje o uživateli patří do tabulky `uzivatel`, články do `clanek`, rubriky do `rubrika` a štítky do `stitek`. Místo opakovaného opisování jména autora obsahuje článek odkaz na jediný záznam uživatele. Databáze tak není jen úložiště buněk. Je to model skutečnosti, který zachycuje identity objektů, jejich vlastnosti, vzájemné vztahy a pravidla platnosti.

Relační model formuloval Edgar F. Codd na začátku sedmdesátých let. Jeho důležitá myšlenka spočívala v oddělení logického pohledu na data od způsobu, jak jsou fyzicky uložena na disku. Uživatel popisuje, jaké údaje chce, zatímco databázový systém rozhoduje, zda použije index, projde tabulku nebo zvolí jiný plán. Díky tomu lze nad stejnými daty klást nové otázky, aniž by pro každou musel vzniknout zvláštní soubor.

## 1.2 Relační datový model a jeho části

**Schéma databáze** popisuje její strukturu: názvy tabulek, sloupce, datové typy, klíče, omezení a další objekty. Vlastní obsah databáze v určitém okamžiku se někdy označuje jako její stav. Schéma říká například, že tabulka `clanek` má sloupce `clanek_id`, `autor_id`, `rubrika_id`, `titulek`, `slug`, `stav` a `publikovan_at`; konkrétní řádek pak popisuje jeden článek.

Sloupce představují **atributy**, řádky **n-tice** neboli záznamy. Každému atributu přísluší **doména**, tedy množina přípustných hodnot. Doménu netvoří jen obecný datový typ. U atributu `stav` mohou být povoleny například jen hodnoty `koncept`, `ke_kontrole`, `schvalen` a `publikovan`; u data publikace jde o platný časový okamžik nebo o nevyplněnou hodnotu, pokud článek dosud nevyšel. Databázový typ, omezení `NOT NULL`, výčtové hodnoty a kontroly `CHECK` společně převádějí význam domény do konkrétních pravidel.

Matematická relace je množina n-tic, takže nezáleží na pořadí řádků ani sloupců a totožné n-tice se neopakují. SQL tabulka je praktická realizace tohoto principu, nikoli jeho dokonalá kopie. Bez omezení může obsahovat duplicitní řádky a pracuje s hodnotou `NULL`. `NULL` neznamená nulu ani prázdný text; vyjadřuje chybějící, neznámou nebo nepoužitelnou hodnotu. Proto se na ni neptáme `= NULL`, ale `IS NULL`. Rozdíl je důležitý například u `publikovan_at`: koncept nemá čas publikace, ale jeho identifikátor ani titulek chybět nesmějí.

## 1.3 Klíče dávají záznamům identitu

**Superklíč** je libovolná kombinace atributů, která řádek jednoznačně určí. **Kandidátský klíč** je minimální superklíč: žádný jeho atribut již nelze odebrat bez ztráty jednoznačnosti. Z kandidátských klíčů návrhář zvolí **primární klíč** a ostatní mohou zůstat alternativními klíči chráněnými omezením `UNIQUE`.

U článku lze uvažovat o veřejné adrese `slug`, například `jak-funguje-relacni-databaze`. Ta má být jedinečná, redakce ji však může před publikací změnit. Pro vnitřní identitu je proto vhodnější neměnný umělý klíč `clanek_id`, vytvořený jako číslo nebo UUID. Přirozený klíč vychází z významu dat, například e-mail uživatele; umělý neboli zástupný klíč systém přidává pouze pro identifikaci. Ani jedna volba není automaticky správná. Dobrý klíč má být jednoznačný, stabilní, co nejjednodušší a nesmí zbytečně odhalovat citlivé informace.

Klíč může být **složený** z více sloupců. Vazební tabulka `clanek_stitek` může mít primární klíč `(clanek_id, stitek_id)`. Tato dvojice nejen identifikuje řádek, ale současně brání tomu, aby byl stejný štítek k témuž článku přiřazen dvakrát. Podobně může mít revize článku klíč `(clanek_id, cislo_revize)`: revize číslo 3 dává smysl jen ve vztahu ke konkrétnímu článku.

**Cizí klíč** odkazuje na kandidátský, nejčastěji primární klíč jiné nebo téže tabulky. `clanek.autor_id` například odkazuje na `uzivatel.uzivatel_id`. Databázový systém pak odmítne článek s neexistujícím autorem. Cizí klíč tedy není pouhá pomůcka pro spojování tabulek; je to vykonatelné pravidlo referenční integrity.

## 1.4 Kardinality a propojení tabulek

Vztah **1:N** znamená, že jeden řádek na první straně může souviset s mnoha řádky na druhé straně. Jeden autor může napsat více článků, ale každý článek má jednoho hlavního autora. Cizí klíč proto leží na straně „mnoho“, tedy v tabulce `clanek`. Stejný tvar má vztah rubriky k článkům nebo článku k jeho revizím.

Vztah **1:1** se používá tehdy, když každému záznamu odpovídá nejvýše jeden záznam na druhé straně. Uživatelský účet může mít například jeden volitelný redakční profil s biografií a fotografií. Cizí klíč v profilu musí být zároveň jedinečný. Rozdělení 1:1 dává smysl, když jsou rozšiřující údaje volitelné, citlivější nebo se s nimi pracuje jiným způsobem; není však vhodné štěpit tabulky bez důvodu.

Vztah **N:M** nelze vyjádřit jediným cizím klíčem. Článek může mít více štítků a jeden štítek označuje mnoho článků. Vznikne proto vazební tabulka `clanek_stitek`, jejíž každý řádek představuje jedno přiřazení. Vazba může mít i vlastní atribut, například kdo štítek přiřadil nebo kdy se tak stalo.

Kardinalita má také minimum. Článek musí mít autora, ale před rozdělením obsahu do rubrik může být rubrika volitelná. Diagram proto nemá sdělovat pouze „jeden“ a „mnoho“, ale také „právě jeden“, „nejvýše jeden“, „žádný nebo více“. Tyto významy se později promítnou do cizích klíčů, omezení `NOT NULL` a jedinečnosti.

# Lekce 2: Od požadavků k dobře navrženému schématu

## 2.1 Návrh začíná prací redakce, ne názvy tabulek

Prvním krokem je sběr a analýza požadavků. Návrhář zjišťuje, kdo bude systém používat, jaké činnosti provádí, co musí systém evidovat a která pravidla nesmějí být porušena. Autor potřebuje ukládat koncepty, editor přidělovat připomínky, šéfredaktor schvalovat publikaci a návštěvník zobrazit jen zveřejněné články. Zároveň je třeba rozhodnout, zda může mít článek více autorů, zda se má zachovat každá revize a zda lze jednou použitý `slug` později znovu přidělit.

Výsledkem **konceptuálního návrhu** je model významu dat nezávislý na konkrétním produktu. **Logický návrh** převádí entity a vztahy do tabulek, atributů, klíčů a omezení relačního modelu. **Fyzický návrh** již zohledňuje konkrétní databázový systém: volí přesné datové typy, indexy, způsob uložení velkých textů a další provozní vlastnosti. Následuje implementace, naplnění testovacími daty, ověření dotazů, výkonu a oprávnění a teprve potom nasazení.

Návrh není jednorázová kresba. Když redakce později zavede spoluautorství nebo placený obsah, schéma se musí bezpečně změnit. Změny se proto ukládají jako verzované **migrace databáze**, které lze opakovat v testovacím i produkčním prostředí. Tím se schéma stává součástí vývoje aplikace, nikoli ručně udržovaným tajemstvím jednoho serveru.

## 2.2 ER diagram jako společná mapa

**ER model — Entity-Relationship model** zachycuje entity, jejich atributy a vztahy. Entita představuje rozlišitelný objekt nebo událost, například článek, uživatele, rubriku nebo revizi. Atribut popisuje jeho vlastnost a vztah vyjadřuje souvislost mezi entitami. V tradiční Chenově notaci se entity kreslí jako obdélníky, vztahy jako kosočtverce a atributy jako elipsy. V praxi se často používá kompaktnější notace crow's foot, která zobrazuje atributy přímo v blocích entit a na koncích čar vyznačuje kardinality.

Diagram redakčního systému může obsahovat entity `Uzivatel`, `Clanek`, `Rubrika`, `Stitek` a `Revize`. Zvláštní pozornost si zaslouží vícehodnotové a složené atributy. „Celé jméno“ lze v konceptuálním modelu chápat jako složený atribut z jména a příjmení, pokud je redakce potřebuje samostatně. Seznam štítků je vícehodnotový atribut, který se v relačním schématu převede na samostatnou entitu a vazební tabulku. Není vhodné ukládat jej do jediného textu odděleného čárkami.

**Slabá entita** nemá úplnou identitu bez svého vlastníka. Jestliže je revize označena pořadovým číslem pouze v rámci článku, identifikuje ji až dvojice `(clanek_id, cislo_revize)`. Její existence navíc nedává smysl bez článku. Pokud však každá revize získá celosystémové `revize_id`, může být v relační implementaci identifikována samostatně. Slabost tedy neplyne z názvu entity, ale ze způsobu její identity a existenční závislosti.

ER diagram slouží k domluvě, ne jen k dokumentaci hotové databáze. Editor může z diagramu zjistit, zda model umožňuje spoluautorství; vývojář na něm odhalí, že jeden textový atribut `autori` by byl pro vyhledávání i integritu problematický. Přesný diagram tak odstraňuje nejasnosti dříve, než se promění v kód a data.

## 2.3 Převod konceptuálního modelu do tabulek

Silná entita obvykle vytvoří vlastní tabulku. Vztah 1:N se převede vložením cizího klíče na stranu N. Vztah N:M vyžaduje vazební tabulku s cizími klíči na obě původní tabulky. Vícehodnotový atribut se rovněž přesune do samostatné tabulky a slabá entita získá klíč obsahující identitu vlastníka, případně vlastní zástupný klíč doplněný vhodným omezením jedinečnosti.

Při převodu je nutné zachovat význam, ne pouze tvary z obrázku. Pokud jeden článek může mít více autorů, nestačí sloupec `autor_id` v článku; vznikne tabulka `clanek_autor`, která může obsahovat i pořadí autorů nebo druh jejich příspěvku. Pokud má článek právě jednoho odpovědného autora, lze tento vztah ponechat samostatně a současně evidovat další spoluautory. Různé vztahy mezi stejnými entitami mohou mít odlišný význam a nesmějí se bezmyšlenkovitě sloučit.

Zvláštním případem je vztah tabulky k sobě samé. Rubrika může mít nadřazenou rubriku, například `Technologie` může obsahovat podřízenou rubriku `Databáze`. Sloupec `nadrazena_id` pak odkazuje zpět na `rubrika.rubrika_id`. Kořenová rubrika má tento odkaz prázdný. I takový model potřebuje pravidla, aby například nevznikl kruh, v němž je rubrika nepřímo vlastní předkyní.

## 2.4 Normalizace na příkladu redakčních dat

Normalizace uspořádává atributy podle jejich funkčních závislostí. Jejím cílem není vytvořit co nejvíce tabulek, ale uložit každý fakt na vhodném místě a omezit anomálie. Pokud se jméno rubriky opakuje u každého článku, změna názvu vyžaduje úpravu mnoha řádků. Při vymazání posledního článku by mohla zmizet i jediná informace o existenci rubriky. A novou prázdnou rubriku by nebylo kam vložit. Jde o anomálie změny, odstranění a vložení.

V **první normální formě (1NF)** obsahuje každá pozice jednu hodnotu z příslušné domény a nevznikají opakující se skupiny sloupců typu `stitek1`, `stitek2`, `stitek3`. Hodnota je atomická vzhledem k zamýšlenému použití. Text článku může být pro databázi jedna hodnota, i když obsahuje tisíce slov; seznam samostatně vyhledávaných štítků jednou hodnotou není.

**Druhá normální forma (2NF)** vyžaduje 1NF a plnou závislost každého neklíčového atributu na celém kandidátském klíči. Problém se projeví hlavně u složených klíčů. Kdyby `clanek_stitek` s klíčem `(clanek_id, stitek_id)` obsahovala `titulek_clanku` a `nazev_stitku`, první údaj by závisel pouze na `clanek_id` a druhý pouze na `stitek_id`. Patří proto do rodičovských tabulek. Tabulka s jednosloupcovým klíčem nemůže mít částečnou závislost na části klíče.

**Třetí normální forma (3NF)** odstraňuje tranzitivní závislosti neklíčových atributů. Pokud by tabulka `clanek` obsahovala `rubrika_id` i `nazev_rubriky`, název by nezávisel přímo na článku, ale na jeho rubrice. Uloží se proto pouze v tabulce `rubrika`. Praktická pomůcka říká, že neklíčový atribut má vypovídat o „klíči, celém klíči a ničem než klíči“. Skutečné rozhodnutí však vždy vychází z významu dat.

Vyšší normální formy řeší složitější závislosti. Pro běžný redakční systém je důležitější správně pochopit první tři než mechanicky počítat úroveň normalizace. Někdy se kvůli měření návštěvnosti nebo rychlému čtení vytvoří odvozený údaj či analytická kopie. Taková **denormalizace** má být vědomým a zdokumentovaným kompromisem s jasným způsobem aktualizace, nikoli náhradou za nepochopený model.

## 2.5 Nástroje podporují návrh, ale nerozhodují za návrháře

ER diagram lze vytvořit v univerzálním nástroji, například diagrams.net, nebo v nástroji zaměřeném na databáze. MySQL Workbench, pgModeler či prostředí některých databázových klientů umějí z modelu vygenerovat SQL skript (**forward engineering**) a z existující databáze vytvořit diagram (**reverse engineering**). Druhý postup dobře dokumentuje aktuální strukturu, sám však nevysvětlí původní požadavky ani nepozná nevhodně navržené závislosti.

Při společném vývoji je výhodné uchovávat vedle diagramu také textové migrace v systému správy verzí. Nástroje jako Flyway, Liquibase nebo migrační mechanismus použitého frameworku zapisují změny schématu ve správném pořadí. Grafický návrh pomáhá porozumění, migrace zajišťují opakovatelné nasazení. Žádné tlačítko „normalizovat“ však nenahradí znalost toho, co znamená článek, revize nebo schválení v konkrétní redakci.

# Lekce 3: Správa databáze, uživatelé a spolehlivost dat

## 3.1 Databázový server, klient a správce

**Systém řízení báze dat — DBMS, Database Management System** přijímá dotazy, kontroluje oprávnění a integritu, řídí souběžnou práci, volí plány provedení a zajišťuje uložení dat. U serverových systémů běží databázový server jako služba a klienti se k němu připojují po síti nebo lokálně. Klientem může být příkazový řádek, administrační program, analytický nástroj nebo redakční aplikace používající databázový ovladač.

Databázový administrátor (**DBA**) spravuje účty a oprávnění, zálohy a obnovu, aktualizace, kapacitu, výkon, dostupnost a bezpečnost. U malé aplikace může stejnou roli zastávat vývojář; ve velké organizaci jde o specializovaný tým. Grafické nástroje jako pgAdmin, MySQL Workbench, SQL Server Management Studio nebo univerzální DBeaver zpřístupňují mnoho operací přehledněji, ale ve výsledku komunikují s databázovým systémem. Důležitá pravidla proto musejí být v databázi a v opakovatelných skriptech, ne jen v nastavení jednoho počítače.

Správa zahrnuje také pozorování provozu. Sleduje se dostupnost, počet spojení, dlouhé a blokované dotazy, využití paměti a úložiště, četnost chyb i úspěšnost záloh. Optimalizace začíná měřením; náhodné přidávání indexů nebo změna konfigurace bez znalosti skutečné zátěže může stav zhoršit.

## 3.2 Databázové účty, role a oprávnění

Je nutné odlišit uživatele redakční aplikace od databázového účtu. Autorka přihlášená do redakčního systému obvykle nemá vlastní přímé spojení k databázi. Aplikace ověří její identitu a pravidla „smí upravit své koncepty“, zatímco sama používá omezený databázový účet. Vedle něj může existovat účet jen pro čtení statistik, účet pro migrace schématu a samostatný administrátor.

Databázové systémy sdružují oprávnění do **rolí**. Příkazy `GRANT` a `REVOKE` přidělují nebo odebírají právo připojit se, číst určité tabulky, měnit data, spouštět procedury či upravovat schéma. Názvy superuživatelů se mezi produkty liší; aplikace rozhodně nemá běžet jako `root`, `postgres`, `sa` nebo jiný správce s neomezenými právy.

Zásada **nejmenších oprávnění** říká, že každý účet dostane jen to, co nezbytně potřebuje. Veřejná část webu může číst bezpečný pohled publikovaných článků, ale nemá důvod vidět e-maily autorů ani koncepty. Účet pro export newsletteru nepotřebuje mazat tabulky. Omezení rozsahu oprávnění nezabrání každé chybě, výrazně však zmenší její dopad.

## 3.3 Integrita: pravidla platí pro každý vstup

**Entitová integrita** zajišťuje jednoznačnou identitu každého řádku: primární klíč je jedinečný a nesmí být `NULL`. **Referenční integrita** chrání vztahy mezi tabulkami. Článek nemůže odkazovat na neexistující rubriku a revize nemůže patřit k neexistujícímu článku. Při změně nebo odstranění rodičovského záznamu lze zvolit odmítnutí operace, kaskádovou změnu či odstranění nebo nastavení odkazu na `NULL`. Volba `ON DELETE CASCADE` je vhodná například pro pomocné vazby štítků po odstranění článku, ale nebezpečná tam, kde by skryla významnou ztrátu historie.

**Doménová integrita** omezuje jednotlivé hodnoty pomocí datových typů, `NOT NULL`, `CHECK`, `UNIQUE` a dalších pravidel. Datum publikace nesmí být text v libovolném formátu, e-mail uživatele má být jedinečný a stav článku má pocházet z povolené množiny. Některá pravidla přesahují jeden řádek a vyžadují transakci, trigger nebo jiný mechanismus. Databáze však má hlídat co nejvíce základních invariantů, protože data mohou přicházet z webového formuláře, importu, administrace i další aplikace.

Validace v uživatelském rozhraní zlepšuje použitelnost, ale nenahrazuje integritu databáze. Formulář může upozornit na chybějící titulek dříve, než odešle data; omezení `NOT NULL` je poslední ochrana pro všechny možné cesty zápisu.

## 3.4 Index jako rejstřík s cenou

Index je pomocná datová struktura, která umožňuje najít řádky bez úplného procházení tabulky. Běžný stromový index dobře slouží rovnosti, rozsahům a řazení. Jedinečný index současně pomáhá vynutit jedinečnost. Složený index obsahuje více sloupců a jeho pořadí musí odpovídat skutečným dotazům. Pro redakční web může být užitečný jedinečný index na `slug` a složený index na `(stav, publikovan_at)`, protože úvodní stránka často hledá právě publikované články a řadí je podle času.

Fulltextové hledání v titulku a těle článku potřebuje specializovaný index a liší se podle databázového systému. Nelze je nahradit běžným indexem na dlouhém textu. Stejně tak není pravda, že každý sloupec má být indexován. Index zabírá místo a každý `INSERT`, `UPDATE` nebo `DELETE` jej musí udržovat. U malé tabulky rubrik může být úplné načtení levnější než práce s indexem.

Primární a jedinečná omezení bývají v konkrétních RDBMS realizována pomocí indexu, logické pravidlo a fyzická struktura však nejsou totéž. O vhodnosti indexu rozhoduje plán dotazu a reálná data. Příkaz či nástroj typu `EXPLAIN` ukáže, jak databáze zamýšlí dotaz provést; teprve měření potvrdí, zda změna skutečně pomohla.

## 3.5 Export, import, záloha a obnova

Export přenáší data do jiného tvaru. **CSV** se hodí pro jednoduchá tabulková data, ale neuchovává klíče, datové typy ani vztahy a vyžaduje dohodu o kódování, oddělovači, formátu data a zápisu `NULL`. **JSON** lépe zachytí vnořenou strukturu pro webové API, **XML** se stále používá v některých integračních systémech. **SQL dump** může obsahovat příkazy pro vytvoření schématu a vložení dat; mezi různými produkty však nemusí být plně přenositelný. Nativní binární export bývá účinný pro obnovu ve stejném databázovém systému.

Export není automaticky záloha. Záloha má známý rozsah, čas vzniku, pravidla uchování a ověřený postup obnovy. Musí zahrnout nejen tabulky, ale podle potřeby také schéma, role, procedury, konfiguraci a související soubory, například obrázky článků uložené mimo databázi. Replikace rovněž není záloha: smazaný článek nebo chybná změna se může rychle přenést i na repliku.

Obnova se musí zkoušet. Soubor, který nikdo nedokáže načíst, není spolehlivá ochrana. Redakce by měla znát cílovou ztrátu dat a přijatelnou dobu výpadku, chránit zálohy šifrováním a přístupovými právy a uchovávat alespoň jednu kopii odděleně od hlavního systému.

# Lekce 4: SQL od změny dat k přesné otázce

## 4.1 Jeden jazyk, více dialektů

**SQL — Structured Query Language** je převážně deklarativní jazyk pro relační databáze. Popisuje požadovaný výsledek, ne přesný algoritmus jeho získání. Tradičně se rozlišuje **DDL** pro definici struktury (`CREATE`, `ALTER`, `DROP`), **DML** pro změny dat (`INSERT`, `UPDATE`, `DELETE`), **DQL** pro dotazování pomocí `SELECT`, **DCL** pro oprávnění (`GRANT`, `REVOKE`) a **TCL** pro řízení transakcí (`COMMIT`, `ROLLBACK`). Toto školní členění není ve všech zdrojích stejné; důležitější je rozumět účinku příkazu.

SQL je standardizované, jednotlivé produkty však používají vlastní dialekty. Liší se automatické generování klíčů, datové typy, funkce pro datum a text, omezení počtu řádků i jazyk procedur. `LIMIT` používají například SQLite, MySQL/MariaDB a PostgreSQL, zatímco jiné systémy používají `TOP` nebo standardní `FETCH FIRST`. Princip dotazu je přenositelný, přesnou syntaxi je nutné ověřit pro zvolený RDBMS.

## 4.2 Základní schéma a změnové dotazy

Zjednodušené jádro redakční databáze lze v dialektu blízkém standardnímu SQL vytvořit takto:

```sql
CREATE TABLE uzivatel (
    uzivatel_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email       VARCHAR(255) NOT NULL UNIQUE,
    jmeno       VARCHAR(120) NOT NULL
);

CREATE TABLE rubrika (
    rubrika_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nazev      VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE clanek (
    clanek_id     BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autor_id      BIGINT NOT NULL REFERENCES uzivatel(uzivatel_id),
    rubrika_id    BIGINT REFERENCES rubrika(rubrika_id),
    titulek       VARCHAR(200) NOT NULL,
    slug          VARCHAR(220) NOT NULL UNIQUE,
    telo          TEXT NOT NULL,
    stav          VARCHAR(20) NOT NULL DEFAULT 'koncept',
    vytvoren_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    publikovan_at TIMESTAMP,
    verze          INTEGER NOT NULL DEFAULT 1,
    CHECK (stav IN ('koncept', 'ke_kontrole', 'schvalen', 'publikovan')),
    CHECK (stav <> 'publikovan' OR publikovan_at IS NOT NULL)
);

CREATE TABLE stitek (
    stitek_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nazev     VARCHAR(80) NOT NULL UNIQUE
);

CREATE TABLE clanek_stitek (
    clanek_id BIGINT NOT NULL REFERENCES clanek(clanek_id)
               ON DELETE CASCADE,
    stitek_id BIGINT NOT NULL REFERENCES stitek(stitek_id),
    PRIMARY KEY (clanek_id, stitek_id)
);
```

Příkaz `INSERT` přidává řádky. Je bezpečnější uvést cílové sloupce výslovně, aby zápis nezávisel na jejich fyzickém pořadí:

```sql
INSERT INTO rubrika (nazev)
VALUES ('Technologie');

INSERT INTO clanek
    (autor_id, rubrika_id, titulek, slug, telo)
VALUES
    (12, 3, 'Jak funguje databázový index',
     'jak-funguje-databazovy-index', 'Text článku...');
```

`UPDATE` mění existující řádky a `DELETE` je odstraňuje. Zapomenutá podmínka `WHERE` zasáhne celou tabulku, proto se před rozsáhlou změnou ověřuje stejná podmínka pomocí `SELECT`, počet dotčených řádků a možnost návratu v transakci.

```sql
UPDATE clanek
SET stav = 'ke_kontrole'
WHERE clanek_id = 184
  AND stav = 'koncept';

DELETE FROM clanek_stitek
WHERE clanek_id = 184
  AND stitek_id = 7;
```

## 4.3 Stavba výběrového dotazu

Výběrový dotaz vytváří výslednou tabulku. Jeho častá podoba je:

```sql
SELECT vyrazy
FROM zdroj
JOIN dalsi_zdroj ON podminka_spojeni
WHERE podminka_radku
GROUP BY seskupovaci_sloupce
HAVING podminka_skupiny
ORDER BY vyrazy
FETCH FIRST pocet ROWS ONLY;
```

Jednoduchý dotaz na publikované články z roku 2026 může vypadat takto:

```sql
SELECT titulek, slug, publikovan_at
FROM clanek
WHERE stav = 'publikovan'
  AND publikovan_at >= DATE '2026-01-01'
ORDER BY publikovan_at DESC, clanek_id DESC;
```

`SELECT` určuje požadované sloupce nebo výrazy, `FROM` zdroj, `WHERE` filtr řádků a `ORDER BY` pořadí. Bez `ORDER BY` není pořadí výsledku zaručeno. Druhý řadicí klíč zajišťuje stabilní pořadí článků se shodným časem. `SELECT *` je užitečný při průzkumu, v aplikaci je však vhodnější vyjmenovat potřebné sloupce: výsledek je čitelnější, méně závislý na změně schématu a nepřenáší zbytečná nebo citlivá data.

Logické pořadí vyhodnocení se liší od zápisu. Zjednodušeně se nejprve sestaví zdroj z `FROM` a `JOIN`, potom se použije `WHERE`, vytvoří skupiny `GROUP BY`, filtrují se pomocí `HAVING`, vypočtou se výrazy `SELECT` a nakonec se výsledek seřadí a omezí. Proto obvykle nelze alias vytvořený v `SELECT` použít ve `WHERE` téže úrovně dotazu.

## 4.4 Podmínky, NULL a spojování tabulek

Podmínky používají porovnání, `AND`, `OR`, `NOT`, množinu `IN`, interval `BETWEEN` nebo vzor `LIKE`. Závorky odstraňují nejasnosti při kombinování podmínek. Na chybějící čas publikace se ptáme `publikovan_at IS NULL`, nikoli `publikovan_at = NULL`. Výraz s neznámou hodnotou totiž často vede k výsledku „neznámo“, který filtrem `WHERE` neprojde.

Data redakce jsou rozdělena do tabulek, a proto je spojujeme operací `JOIN`:

```sql
SELECT c.titulek,
       u.jmeno AS autor,
       r.nazev AS rubrika
FROM clanek AS c
JOIN uzivatel AS u ON u.uzivatel_id = c.autor_id
LEFT JOIN rubrika AS r ON r.rubrika_id = c.rubrika_id
WHERE c.stav = 'publikovan'
ORDER BY c.publikovan_at DESC;
```

Vnitřní `JOIN` ponechá jen řádky s odpovídajícím protějškem. `LEFT JOIN` zachová všechny články a u článku bez rubriky doplní do jejích sloupců `NULL`. Podmínka spojení musí popisovat skutečný vztah klíčů; chybějící nebo chybná podmínka může vytvořit obrovské množství nesouvisejících kombinací. `DISTINCT` sice odstraní shodné výsledné řádky, nemá však zakrývat špatně navržené spojení.

## 4.5 Agregace odpovídá na souhrnné otázky

Funkce `COUNT`, `SUM`, `AVG`, `MIN` a `MAX` shrnují více řádků. Chceme-li zjistit rubriky s alespoň deseti publikovanými články, vytvoříme skupinu pro každou rubriku:

```sql
SELECT r.nazev,
       COUNT(*) AS pocet_clanku,
       MAX(c.publikovan_at) AS posledni_publikace
FROM rubrika AS r
JOIN clanek AS c ON c.rubrika_id = r.rubrika_id
WHERE c.stav = 'publikovan'
GROUP BY r.rubrika_id, r.nazev
HAVING COUNT(*) >= 10
ORDER BY pocet_clanku DESC;
```

`WHERE` filtruje jednotlivé články před seskupením, `HAVING` až hotové skupiny. `COUNT(*)` počítá řádky, zatímco `COUNT(sloupec)` jen řádky, v nichž sloupec není `NULL`. Podobně průměr neznámé hodnoty ignoruje. SQL může výpočet provést technicky správně, ale uživatel stále musí posoudit, zda data a zvolený souhrn odpovídají položené otázce.

Složitější otázku lze rozdělit poddotazem nebo společným tabulkovým výrazem `WITH` (**CTE, Common Table Expression**). Tyto prostředky zvyšují čitelnost, pokud pojmenovávají logický mezivýsledek. Nejsou automatickou zárukou vyššího výkonu; o plánu opět rozhoduje konkrétní databázový systém.

# Lekce 5: Databáze jako aktivní součást aplikace

## 5.1 Pohledy poskytují řízený pohled na data

**Pohled — view** je pojmenovaný dotaz, který se používá podobně jako tabulka. Může skrýt složité spojení, sjednotit často používaný výběr nebo zpřístupnit jen bezpečnou část dat. Pohled `verejne_clanky` může obsahovat titulek, slug, jméno autora a čas publikace, ale vynechat e-mail, pracovní poznámky a koncepty.

```sql
CREATE VIEW verejne_clanky AS
SELECT c.clanek_id, c.titulek, c.slug,
       c.publikovan_at, u.jmeno AS autor
FROM clanek AS c
JOIN uzivatel AS u ON u.uzivatel_id = c.autor_id
WHERE c.stav = 'publikovan';
```

Běžný pohled data sám neukládá; při použití se vyhodnotí jeho dotaz. Proto nezrychlí výpočet jen tím, že dostal jméno. **Materializovaný pohled** naopak výsledek fyzicky uchovává a musí se obnovovat. Hodí se například pro náročné přehledy návštěvnosti, u nichž nevadí malé zpoždění. Podpora a syntaxe materializovaných pohledů se mezi produkty liší.

## 5.2 Triggery reagují na události

**Trigger — databázová spoušť** automaticky reaguje na `INSERT`, `UPDATE`, `DELETE` nebo jinou podporovanou událost. Může před změnou upravit či ověřit hodnoty nebo po změně zapsat auditní záznam. V redakčním systému může zaznamenat přechod článku do stavu `publikovan` nebo uložit, kdo a kdy změnil důležitý údaj.

Trigger je užitečný tam, kde pravidlo musí platit pro všechny cesty zápisu. Zároveň však skrývá činnost, kterou volající příkaz přímo neukazuje. Nevhodně navržené triggery se mohou řetězit, zpomalovat zápis a komplikovat hledání chyb. Jednoduchá omezení proto patří do `CHECK`, `UNIQUE` či cizích klíčů; trigger má řešit skutečně událostní nebo auditní logiku, kterou nelze vyjádřit přímočařeji.

## 5.3 Uložené procedury a funkce

**Uložená procedura** je pojmenovaný program uložený v databázovém systému. Může přijímat parametry, provést více příkazů, pracovat s transakcí a vrátit výsledky. **Uložená funkce** typicky vrací hodnotu nebo tabulku a v některých RDBMS ji lze použít uvnitř SQL výrazu. Přesná hranice mezi funkcí a procedurou i jejich jazyky se mezi PostgreSQL, MySQL/MariaDB, SQL Serverem a Oracle výrazně liší.

Procedura může soustředit kritický krok, například publikaci článku, která ověří stav, nastaví čas, vytvoří auditní záznam a zařadí článek do fronty dalších operací. Umožní také přidělit aplikaci právo spustit konkrétní operaci, aniž by získala volné právo měnit všechny tabulky. Nevýhodou je větší závislost na produktu, náročnější verzování a rozdělení logiky mezi databázi a aplikaci.

Uložená procedura sama o sobě nezabrání SQL injection. Pokud uvnitř skládá příkaz z neověřeného textu, je zranitelná stejně jako aplikace. Bezpečnost přinášejí parametrizované příkazy, kontrolované oprávnění a omezené rozhraní, nikoli pouhý fakt, že je kód uložen v databázi.

## 5.4 Transakce chrání smysl celé operace

**Transakce** sdružuje několik kroků do jednoho logického celku. Při publikaci může být třeba změnit stav článku, nastavit čas a zapsat událost do historie. Buď proběhnou všechny kroky, nebo žádný. Základní vlastnosti se shrnují zkratkou **ACID**: atomicita chrání nedělitelnost, konzistence přechod mezi platnými stavy, izolace omezuje vzájemné rušení souběžných transakcí a trvalost zajišťuje, že potvrzená změna přežije selhání podle garancí systému.

```sql
BEGIN;

UPDATE clanek
SET stav = 'publikovan',
    publikovan_at = CURRENT_TIMESTAMP
WHERE clanek_id = 184
  AND stav = 'schvalen';

INSERT INTO audit_clanku (clanek_id, udalost, vznikla_at)
VALUES (184, 'publikace', CURRENT_TIMESTAMP);

COMMIT;
```

Pokud druhý krok selže, aplikace použije `ROLLBACK` a článek nezůstane v napůl publikovaném stavu. V reálné aplikaci je nutné ověřit i počet změněných řádků: nulový výsledek prvního příkazu může znamenat, že článek nebyl schválen nebo jej mezitím změnil někdo jiný.

## 5.5 Souběh, zámky a izolace

Databáze obsluhuje více uživatelů současně. Bez řízení souběhu by dva editoři mohli načíst stejnou verzi článku, každý ji změnit a pozdější uložení by tiše přepsalo práci prvního. Databázové systémy používají zámky, víceverzové řízení souběhu (**MVCC**) a izolační úrovně. Čtení tak podle systému a nastavení nemusí blokovat zápis, přesto musí databáze chránit konfliktní změny.

Při **pesimistickém** přístupu aplikace potřebný řádek zamkne a ostatní čekají. U dlouhé editace článku by to bylo nepraktické. Redakční systém proto může použít **optimistické zamykání**: článek obsahuje číslo verze a aktualizace proběhne pouze tehdy, pokud se od načtení nezměnilo.

```sql
UPDATE clanek
SET telo = :nove_telo,
    verze = verze + 1
WHERE clanek_id = :id
  AND verze = :puvodni_verze;
```

Pokud se nezmění žádný řádek, aplikace oznámí konflikt a nabídne porovnání verzí. Parametry označené dvojtečkou neposílají hodnoty jako kus SQL textu; ovladač je předává odděleně.

**Deadlock** vznikne, když dvě transakce drží prostředky, které ta druhá potřebuje, a vzájemně čekají. Databázový systém jednu obvykle ukončí a aplikace musí umět bezpečně opakovat celou transakci. Riziko se snižuje krátkými transakcemi a jednotným pořadím změn. Vyšší izolace odstraňuje více anomálií, může však omezit souběh; správná volba závisí na významu operace.

# Lekce 6: Od Accessu k podnikovým databázím

## 6.1 Stejný model, různá architektura

Označení „relační databáze“ popisuje datový model, nikoli jednu velikost programu. Produkty se liší architekturou, správou, licencí, možnostmi souběhu, dostupností i nástroji. Databáze pro osobní katalog, mobilní aplikaci, veřejný magazín a globální mediální dům mohou používat tabulky a SQL, přesto mají velmi rozdílné provozní požadavky.

**Microsoft Access** spojuje souborovou relační databázi s grafickými nástroji pro tabulky, dotazy, formuláře, sestavy a jednoduchou aplikační logiku. Hodí se pro výuku, prototyp, osobní evidenci nebo menší týmovou aplikaci v prostředí Microsoft Office. Není to jen „horší SQL server“; jeho předností je rychlé vytvoření celé desktopové aplikace. Souborová architektura a limity velikosti i souběhu však nejsou vhodné pro veřejný redakční systém s mnoha uživateli. Access může také sloužit jako uživatelské rozhraní nad tabulkami uloženými na serveru.

**SQLite** je malý vestavěný databázový engine. Neběží jako samostatný server; aplikace pracuje přímo s databázovým souborem prostřednictvím knihovny. Je výborný pro mobilní a desktopové aplikace, lokální data, testy nebo přenosný archiv. Redakční aplikace spuštěná na notebooku může v SQLite uchovávat offline koncepty. Centrální webovou redakci s mnoha souběžnými zápisy je obvykle vhodnější postavit na klient-serverovém RDBMS: SQLite dovoluje více čtenářů, ale zápisy do jednoho souboru musí koordinovat a v jednom okamžiku zapisuje jediný zapisovatel.

## 6.2 MySQL, MariaDB a PostgreSQL pro webové aplikace

**MySQL** a **MariaDB** jsou samostatné klient-serverové relační systémy se společnou historií a do značné míry podobným SQL, nejsou však totožné a jejich funkce se postupně rozcházejí. Oba se často používají pro webové aplikace a redakční systémy. Výchozí transakční úložiště rodiny InnoDB podporuje cizí klíče, transakce a řízení souběhu. Pro nový projekt je třeba porovnávat konkrétní podporované verze, provozní prostředí a požadované funkce, nikoli předpokládat úplnou zaměnitelnost.

**PostgreSQL** je otevřený objektově-relační systém známý důrazem na standardy, rozšiřitelnost a bohaté datové typy. Vedle klasických tabulek nabízí například práci s JSON, fulltextové hledání, pokročilé indexy a rozšíření. Pro redakční systém může spojit spolehlivý relační model s vyhledáváním a s některými méně pravidelnými metadaty, aniž by se základní struktura článků vzdala klíčů a omezení.

O výsledné kvalitě nerozhoduje značka sama. Špatně navržené schéma, chybějící zálohy nebo aplikace s administrátorským účtem jsou problém v každém produktu. Naopak běžný redakční systém mohou při správném návrhu dobře obsloužit MySQL, MariaDB i PostgreSQL. Výběr ovlivní zkušenost týmu, hosting, kompatibilita aplikace, nástroje, licence, požadavky na dostupnost a očekávaný růst.

## 6.3 SQL Server, Oracle a spravované cloudové služby

**Microsoft SQL Server** je podnikový RDBMS úzce propojený s ekosystémem Microsoftu. Používá dialekt Transact-SQL, nabízí nástroje pro správu, integraci, analytiku, vysokou dostupnost a bezpečnost a existuje v různých edicích včetně variant pro menší projekty a výuku. Dává smysl tam, kde organizace využívá související platformu, potřebuje centrální podporu a provozuje mnoho kritických aplikací.

**Oracle Database** je rozsáhlý podnikový objektově-relační systém určený také pro velmi náročné transakční a konsolidované provozy. Nabízí vlastní procedurální jazyk PL/SQL, pokročilou správu, vysokou dostupnost a víceuživatelskou architekturu. Jeho možnosti, licencování a provozní složitost odpovídají především organizacím, které je skutečně využijí; pro malý magazín by obvykle šlo o nepřiměřené řešení.

Databázi lze provozovat na vlastním serveru, ve virtuálním stroji, v kontejneru nebo jako **spravovanou cloudovou službu**. Spravovaná služba může převzít část aktualizací, záloh, replikace a monitorování. Nemění však relační model a nepřenáší všechnu odpovědnost na poskytovatele. Tým stále navrhuje schéma, účty, síťový přístup, pravidla obnovy, klasifikaci dat a kontroluje náklady i závislost na konkrétní službě.

## 6.4 Volba podle skutečného použití

Pro školní prototyp redakce s formuláři a sestavami může být vhodný Access. Samostatná desktopová aplikace nebo lokální pracovní kopie využije SQLite. Veřejný web s několika editory obvykle potřebuje klient-serverový MySQL, MariaDB nebo PostgreSQL. Velká mediální skupina může volit PostgreSQL, SQL Server či Oracle podle stávající infrastruktury, podpory, dostupnosti a integrace s dalšími systémy. Ani počet řádků sám o sobě výběr neurčuje; důležité jsou souběžné operace, složitost dotazů, požadovaný výpadek, způsob nasazení a schopnosti týmu.

Při rozhodování je užitečné vytvořit malý realistický prototyp a změřit kritické činnosti: publikaci, načtení titulní strany, fulltextové hledání, hromadný import i obnovu ze zálohy. Produktový seznam funkcí neodhalí nevhodný datový model ani provozní postup, který tým neumí bezpečně používat.

## 6.5 Bezpečnost začíná před prvním dotazem

Webový prohlížeč se nemá připojovat přímo k databázi. Běžná architektura vede požadavek přes aplikační server, který ověří uživatele, autorizuje konkrétní operaci a databázi osloví omezeným účtem. Databázový port nemá být bez důvodu dostupný z veřejného internetu, spojení se chrání šifrováním a hesla i klíče se ukládají do správy tajných údajů, nikoli do zdrojového kódu.

Nejznámějším aplikačním rizikem je **SQL injection**. Vzniká, když program spojí vstup uživatele přímo s textem dotazu. Útočník pak může změnit jeho strukturu. Správnou obranou jsou parametrizované dotazy nebo připravené příkazy, v nichž je struktura SQL oddělena od hodnot. Samotné nahrazování apostrofů, skrytí chyb nebo uložená procedura nejsou obecnou náhradou parametrizace. Dynamicky volené názvy sloupců či směr řazení je třeba vybírat z předem povoleného seznamu.

Další vrstvy tvoří nejmenší oprávnění, pravidelné bezpečnostní aktualizace, audit důležitých změn, ochrana záloh, omezení osobních údajů a bezpečné mazání podle pravidel organizace. Šifrování disku chrání odcizené médium, ale nebrání oprávněné aplikaci přečíst data; šifrování spojení chrání přenos, nikoli chybný dotaz. Bezpečnost proto nevytváří jedna funkce, ale soustava vrstev.

Stejně důležitá je dostupnost. Repliky mohou zkrátit výpadek a rozložit čtení, ale nevrátí článek přepsaný lidskou chybou. Záloha bez nácviku obnovy je pouze naděje. Redakční systém potřebuje sledování, plán aktualizací, obnovitelné zálohy a postup pro incident stejně jako správné klíče a dotazy.

# Závěrečné propojení: od redakčního procesu k bezpečné publikaci

Relační databáze začíná porozuměním skutečnosti. Z práce autorů a editorů vznikne konceptuální model; z entit a vztahů tabulky, klíče a omezení; z dobře navrženého schématu databáze, nad níž lze pomocí SQL přesně měnit a vybírat data. Pohledy, triggery, procedury a transakce pak z databáze dělají aktivní součást aplikace, která chrání pravidla i při souběžné práci.

Celý postup lze shrnout jako sled:

**požadavky redakce → ER model → normalizované schéma → integrita a oprávnění → SQL operace → bezpečná aplikace → publikovaný obsah**

Výběr mezi Accessem, SQLite, MySQL/MariaDB, PostgreSQL, SQL Serverem a Oracle přichází až poté, co je jasné, jaká data a provoz má systém zvládnout. Produkty se liší měřítkem a správou, základní otázky však zůstávají stejné: Co tento řádek znamená? Čím je jednoznačný? Na které jiné údaje odkazuje? Kdo jej smí změnit? Co se stane při chybě a jak data obnovíme? Právě odpovědi na tyto otázky odlišují skutečný databázový systém od pouhé hromady tabulek.
