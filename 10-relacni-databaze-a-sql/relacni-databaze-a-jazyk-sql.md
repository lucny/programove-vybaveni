# Relační databáze a jazyk SQL

Relační databáze jsou nenápadnou součástí téměř každé digitální služby. Když si student rezervuje učebnu, zákazník zaplatí objednávku nebo lékař otevře kartu pacienta, aplikace musí bezpečně najít správná data, propojit je a uložit změnu tak, aby nevznikl rozpor. Samotná tabulka v databázi přitom nestačí. Důležitý je promyšlený model, pravidla integrity, dotazovací jazyk SQL i způsob, jakým s databází pracuje aplikace.

Celým textem proto prochází příklad školního systému pro rezervaci učeben. Uživatelé v něm vyhledávají volné místnosti, vytvářejí rezervace a přihlašují účastníky. Správce školy potřebuje souhrny vytížení a administrátor zajišťuje bezpečnost a dostupnost. Na jednom realistickém systému tak lze ukázat cestu od návrhu dat až po dotaz, který odpoví na praktickou otázku.

---

# Lekce 1: Relační model – data jako tvrzení a vztahy

## 1.1 Proč nestačí jedna velká tabulka

Jednoduchý seznam rezervací by mohl obsahovat datum, čas, číslo učebny, kapacitu, jméno organizátora, jeho e-mail a názvy všech účastníků. Dokud má seznam deset řádků, vypadá použitelně. Jakmile se však změní kapacita učebny, je nutné opravit každý řádek, ve kterém se učebna objevuje. Překlep v jediném z nich vytvoří dvě různé verze téhož údaje. Smazání poslední rezervace určité učebny by navíc mohlo odstranit i jedinou informaci o její existenci.

Relační databáze řeší podobné potíže tím, že rozděluje fakta podle jejich významu. Údaj o učebně patří do tabulky `ucebna`, údaje o člověku do tabulky `uzivatel` a konkrétní událost do tabulky `rezervace`. Vztah mezi rezervací a účastníky zachytí další tabulka. Každé tvrzení se tak pokud možno ukládá na jednom místě a ostatní části databáze se na něj odkazují.

Relační model formuloval Edgar F. Codd na začátku sedmdesátých let. Jeho matematickým základem je **relace**, tedy množina uspořádaných n-tic. V běžném databázovém systému ji prakticky vnímáme jako tabulku. Sloupce představují **atributy**, řádky jednotlivé n-tice neboli záznamy a každému atributu přísluší určitá **doména** povolených hodnot. Databázové SQL tabulky nejsou přesnou kopií matematických relací – mohou například pracovat s `NULL` a bez omezení připustit duplicitní řádky. Myšlenka popsat data pomocí vztahů a operovat nad nimi jako nad celky však zůstává základem.

## 1.2 Tabulka, řádek, sloupec a datový typ

Dobrá tabulka zastupuje jeden druh objektu nebo události. Tabulka `ucebna` může mít sloupce `ucebna_id`, `oznaceni`, `kapacita` a `budova`; tabulka `rezervace` sloupce `rezervace_id`, `ucebna_id`, `organizator_id`, `zacatek`, `konec` a `ucel`. Jeden řádek rezervace pak tvrdí, že určitý organizátor obsadil určitou učebnu v konkrétním čase.

Sloupec má kromě názvu také datový typ. Text, celé číslo, desetinné číslo, datum, časový okamžik a logická hodnota nejsou zaměnitelné obaly. Typ určuje, které hodnoty lze uložit a jaké operace dávají smysl. Datum lze chronologicky řadit a odčítat, zatímco text `"12. 3. 2026"` je pro databázi jen posloupnost znaků závislá na zápisu. Peněžní částky je obvykle vhodnější ukládat jako přesné desetinné číslo než jako binární číslo s plovoucí desetinnou čárkou.

Zvláštní hodnotou je `NULL`. Neznamená nulu ani prázdný text, ale chybějící, neznámou nebo nepoužitelnou hodnotu. Proto se na ni neptáme pomocí `= NULL`, nýbrž pomocí `IS NULL`. Porovnání s neznámou hodnotou totiž nevede jednoduše k pravdě či nepravdě; SQL používá tříhodnotovou logiku s výsledky pravda, nepravda a neznámo. To je důvod, proč mohou řádky s `NULL` z výsledku podmínky nečekaně zmizet.

## 1.3 Klíče dávají záznamům identitu

Každý řádek musí být spolehlivě rozlišitelný. **Kandidátský klíč** je minimální kombinace atributů, která záznam jednoznačně určuje. U uživatele může být kandidátem školní e-mail; databázový návrhář z kandidátů zvolí **primární klíč**. Často jde o uměle vytvořené číselné nebo UUID identifikační číslo, protože jméno ani e-mail nemusejí být po celou dobu neměnné. Další kandidátské klíče lze chránit omezením `UNIQUE`.

Primární klíč může být i **složený**. V tabulce `ucastnik_rezervace` může dvojice `(rezervace_id, uzivatel_id)` současně říkat, ke které rezervaci uživatel patří, a zabránit jeho dvojímu přihlášení. Umělý identifikátor není povinný v každé tabulce; rozhodující je stabilní a jednoznačná identita.

**Cizí klíč** propojuje řádek s řádkem jiné, případně stejné tabulky. Hodnota `rezervace.ucebna_id` musí odpovídat existující učebně. Databázový systém tak dokáže odmítnout rezervaci neexistující místnosti. Cizí klíč tedy není jen pomůcka pro dotazy, ale pravidlo referenční integrity.

## 1.4 Kardinalita a převod vztahů do tabulek

Vztah **1:N** znamená, že jedna učebna může mít mnoho rezervací, ale každá rezervace se týká právě jedné učebny. Cizí klíč se proto umístí na stranu „mnoho“, tedy do tabulky `rezervace`. U vztahu **1:1** patří odkaz obvykle tam, kde dává významově smysl, a jeho jedinečnost se zajistí omezením `UNIQUE`. Příkladem může být uživatel a jeho volitelný profil s rozšířenými údaji.

Vztah **N:M** nelze zachytit jediným cizím klíčem. Jedna rezervace má více účastníků a jeden uživatel se účastní více rezervací. Vznikne proto **vazební tabulka** `ucastnik_rezervace`, jejíž každý řádek představuje jedno přihlášení. Vazební tabulka může nést i vlastní údaje, například čas přihlášení nebo roli účastníka.

Kardinalita sama neříká vše. Návrh musí určit také povinnost vztahu. Rezervace musí mít organizátora, ale uživatel nemusí mít žádnou rezervaci. Tyto rozdíly se později projeví v povolení či zákazu `NULL`, v cizích klíčích a ve způsobu spojování tabulek.

---

# Lekce 2: Od požadavků k databázovému schématu

## 2.1 Návrh začíná otázkami, ne tabulkami

Databáze není cílem sama o sobě. Nejdříve je třeba zjistit, co má systém umět, kdo jej používá a která pravidla nesmí porušit. U rezervačního systému mohou požadavky znít: student vidí volné učebny, učitel vytvoří rezervaci, správce zablokuje místnost kvůli opravě a vedení zjistí vytížení budov. Zároveň nesmějí vzniknout dvě platné rezervace stejné učebny ve stejném čase.

Při analýze se hledají entity, jejich vlastnosti, vztahy a obchodní pravidla. Nestačí opsat políčka z formuláře. Jedno pole „účastníci“ by například v uživatelském rozhraní mohlo působit přirozeně, ale v databázi skrývá opakující se skupinu lidí. Stejně tak věta „rezervace má stav“ vyžaduje rozhodnutí, které stavy existují a jaké přechody mezi nimi jsou povolené.

Následuje **konceptuální návrh**, který popisuje význam dat bez ohledu na konkrétní databázový produkt. **Logický návrh** převádí koncept do tabulek, atributů, klíčů a omezení. **Fyzický návrh** řeší konkrétní datové typy, indexy, rozdělení dat a provozní nastavení zvoleného systému, například PostgreSQL, MySQL, MariaDB, SQL Server nebo Oracle Database. Tato úroveň ovlivňuje výkon, neměla by však opravovat chybný významový model.

## 2.2 ER diagram jako mapa významu

**ER diagram – Entity-Relationship Diagram** zobrazuje entity, jejich atributy a vztahy. V praxi se často používá notace „crow's foot“, v níž symboly na koncích čar vyjadřují minimum a maximum účasti ve vztahu. Diagram školních rezervací může obsahovat entity `Uzivatel`, `Ucebna`, `Rezervace` a `Ucast`. Mezi učebnou a rezervací je vztah 1:N, mezi uživatelem a rezervací může být jednou vztah organizátora 1:N a podruhé vztah účasti N:M.

Diagram není obrázek vytvořený až po hotové databázi. Je to komunikační nástroj, na kterém může učitel, správce školy i vývojář odhalit rozdílné představy dříve, než vznikne kód. Například otázka, zda lze rezervaci přesunout mezi učebnami, rozhoduje o tom, zda je učebna vlastností rezervace, nebo zda má systém evidovat samostatné časové intervaly a historii změn.

**Slabá entita** nemá úplnou identitu bez svého vlastníka. Typickým příkladem je položka objednávky označená pořadovým číslem pouze v rámci jedné objednávky; identifikuje ji tedy dvojice `(objednavka_id, poradi)`. Faktura naproti tomu běžně vlastní samostatné číslo a automaticky slabou entitou není. Toto rozlišení ukazuje, proč návrh nelze odvodit jen z názvu objektu.

## 2.3 Normalizace odstraňuje skryté závislosti

Normalizace rozděluje data tak, aby jeden fakt nebyl zbytečně uložen na mnoha místech a nevznikaly **anomálie vložení, změny a odstranění**. Není to samoúčelná soutěž v počtu tabulek. Je to způsob, jak vyjádřit, na čem který údaj skutečně závisí.

V **první normální formě (1NF)** má každá pozice tabulky jednu hodnotu odpovídající dané doméně a neopakují se skupiny sloupců typu `ucastnik1`, `ucastnik2`, `ucastnik3`. Seznam účastníků se proto nepíše do jednoho textového pole; každý vztah se uloží jako samostatný řádek vazební tabulky. „Atomická“ hodnota přitom závisí na zamýšleném použití. Celá poštovní adresa může být pro jeden systém jediným textem, zatímco doručovací systém ji potřebuje rozdělit.

**Druhá normální forma (2NF)** řeší částečnou závislost na složeném klíči. Kdyby tabulka účasti s klíčem `(rezervace_id, uzivatel_id)` obsahovala také `email_uzivatele`, e-mail by závisel pouze na `uzivatel_id`, nikoli na celé dvojici. Patří tedy do tabulky uživatelů. U tabulky s jednosloupcovým klíčem je podmínka 2NF splněna automaticky, pokud je již v 1NF.

**Třetí normální forma (3NF)** odstraňuje tranzitivní závislosti neklíčových atributů. Kdyby tabulka učeben obsahovala `budova_id` i `adresa_budovy`, adresa by závisela na budově a teprve budova na učebně. Údaj o adrese patří do samostatné tabulky `budova`. Praktická pomůcka říká, že neklíčový údaj má popisovat „klíč, celý klíč a nic než klíč“, ale skutečné rozhodnutí vychází z funkčních závislostí a významu dat.

Vyšší normální formy řeší další druhy závislostí, pro základní návrh však obvykle stačí dobře porozumět prvním třem. Někdy se data záměrně **denormalizují**, například v analytickém skladu nebo kvůli velmi častému čtení. Takový krok má být vědomým kompromisem s jasným způsobem, jak udržet kopie konzistentní, ne opravou špatně navrženého dotazu.

## 2.4 Omezení převádějí pravidla do databáze

Pravidlo, které zůstane pouze v dokumentaci nebo ve formuláři jedné aplikace, lze snadno obejít jiným importem či programem. Proto se co nejvíce pravidel zapisuje přímo do schématu. `PRIMARY KEY` chrání identitu, `FOREIGN KEY` odkazy, `UNIQUE` jedinečnost, `NOT NULL` povinné údaje a `CHECK` podmínky nad hodnotou či řádkem.

Databáze může například kontrolovat, že kapacita učebny je kladná a konec rezervace následuje po začátku. Složitější pravidlo zákazu překrývajících se rezervací vyžaduje podle systému zvláštní omezení, transakční logiku nebo bezpečně napsanou proceduru. Jednoduchá kontrola „nejprve se podívám a potom vložím“ v aplikaci nestačí: mezi těmito dvěma kroky může stejný termín obsadit jiný uživatel.

---

# Lekce 3: Vytvoření databáze a bezpečné změny dat

## 3.1 SQL je deklarativní jazyk

**SQL – Structured Query Language** slouží k definici, čtení a změnám dat v relačních databázích. Je převážně deklarativní: uživatel popíše, jaký výsledek chce, zatímco databázový optimalizátor volí plán provedení. Stejný dotaz může podle velikosti tabulek, indexů a statistik použít zcela jiný postup, aniž by se změnil jeho význam.

Příkazy se tradičně dělí do skupin. **DDL** definuje strukturu (`CREATE`, `ALTER`, `DROP`), **DML** pracuje s daty (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, případně `MERGE`), **DCL** řídí oprávnění (`GRANT`, `REVOKE`) a **TCL** ovládá transakce (`COMMIT`, `ROLLBACK`). Hranice nejsou ve všech učebnicích ani databázových systémech totožné; důležitější než zkratky je rozumět účinku příkazu.

SQL je standardizovaný jazyk, ale jednotlivé produkty mají vlastní datové typy, funkce a rozšíření. `LIMIT` je běžné v PostgreSQL, MySQL či SQLite, zatímco standardní SQL používá také konstrukci `FETCH FIRST`. Následující ukázky jsou záměrně blízké PostgreSQL a standardnímu SQL; při práci s jiným systémem je třeba ověřit jeho dokumentaci.

## 3.2 Schéma jako spustitelná specifikace

Základ rezervačního systému lze vytvořit takto:

```sql
CREATE TABLE uzivatel (
    uzivatel_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email       VARCHAR(255) NOT NULL UNIQUE,
    jmeno       VARCHAR(100) NOT NULL,
    role        VARCHAR(20) NOT NULL
                CHECK (role IN ('student', 'ucitel', 'spravce'))
);

CREATE TABLE ucebna (
    ucebna_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    oznaceni  VARCHAR(20) NOT NULL UNIQUE,
    kapacita  INTEGER NOT NULL CHECK (kapacita > 0),
    budova    VARCHAR(50) NOT NULL
);

CREATE TABLE rezervace (
    rezervace_id  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ucebna_id     BIGINT NOT NULL REFERENCES ucebna(ucebna_id),
    organizator_id BIGINT NOT NULL REFERENCES uzivatel(uzivatel_id),
    zacatek       TIMESTAMP NOT NULL,
    konec         TIMESTAMP NOT NULL,
    ucel          VARCHAR(200) NOT NULL,
    stav          VARCHAR(20) NOT NULL DEFAULT 'aktivni',
    CHECK (konec > zacatek),
    CHECK (stav IN ('aktivni', 'zrusena'))
);

CREATE TABLE ucastnik_rezervace (
    rezervace_id BIGINT REFERENCES rezervace(rezervace_id)
                  ON DELETE CASCADE,
    uzivatel_id  BIGINT REFERENCES uzivatel(uzivatel_id)
                  ON DELETE CASCADE,
    prihlasen_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (rezervace_id, uzivatel_id)
);
```

Názvy, přesné typy i automatické generování identifikátorů se mezi produkty liší. Důležitý je mentální model: definice tabulky nepopisuje jen sloupce, ale také povinnosti a vztahy. Volba `ON DELETE CASCADE` u účasti znamená, že po odstranění rezervace zaniknou i její vazby na účastníky. U odkazu na učebnu jsme kaskádu nepovolili, takže použitou učebnu nelze bez dalšího smazat. Kaskádové mazání je užitečné, ale při nevhodném použití může odstranit více dat, než uživatel čeká.

Změna struktury příkazem `ALTER TABLE` je v prázdné školní databázi snadná, v provozu však může trvat, blokovat další operace nebo vyžadovat doplnění hodnot do milionů řádků. Proto se změny schématu verzují pomocí **migrací**, testují na kopii dat a nasazují s plánem návratu.

## 3.3 INSERT, UPDATE a DELETE mění stav systému

Novou učebnu a rezervaci vložíme příkazem `INSERT`:

```sql
INSERT INTO ucebna (oznaceni, kapacita, budova)
VALUES ('B203', 28, 'Budova B');

INSERT INTO rezervace
    (ucebna_id, organizator_id, zacatek, konec, ucel)
VALUES
    (3, 12, '2026-09-14 14:00', '2026-09-14 15:30',
     'Konzultace projektu');
```

Příkaz by měl uvádět cílové sloupce výslovně. Kód pak není závislý na jejich fyzickém pořadí a je čitelnější. Pro hromadný import se používají specializované mechanismy nebo dávkové vkládání, nikoli tisíce ručně sestavených jednotlivých dotazů.

Změna a odstranění řádků vyžadují podmínku:

```sql
UPDATE rezervace
SET stav = 'zrusena'
WHERE rezervace_id = 481;

DELETE FROM ucastnik_rezervace
WHERE rezervace_id = 481
  AND uzivatel_id = 37;
```

Zapomenuté `WHERE` změní nebo smaže všechny řádky tabulky. Před rizikovou operací je rozumné spustit výběr se stejnou podmínkou, ověřit počet dotčených řádků a pracovat v transakci. V provozních systémech se rezervace často fyzicky nemaže, ale označí jako zrušená. **Měkké smazání** zachová historii, zároveň však komplikuje každý dotaz a samo nenahrazuje auditní záznam ani pravidla uchovávání osobních údajů.

## 3.4 Databázový server, klient a role uživatelů

Databázový systém se často skládá ze serveru a klientů. Server přijímá spojení, ověřuje uživatele, plánuje dotazy, řídí souběh a ukládá data. Klientem může být administrační program, příkazová řádka, analytický nástroj nebo webová aplikace používající databázový ovladač. Nástroje jako pgAdmin, MySQL Workbench či DBeaver práci zpříjemňují, ale pravidla nevytváří grafické rozhraní – vykonává je databázový server.

Správce databáze (**DBA**) se stará o účty, oprávnění, zálohy, obnovu, aktualizace, sledování výkonu a dostupnost. Název superuživatele není univerzálně `root`; závisí na produktu a instalaci. Aplikace navíc nemá běžet s nejvyššími právy. Účet rezervační služby má dostat pouze oprávnění, která skutečně potřebuje.

---

# Lekce 4: SELECT – od otázky k výsledku

## 4.1 Projekce, filtrování a řazení

Příkaz `SELECT` nemění uložená data, ale vytváří výslednou tabulku. Nejjednodušší dotaz vybere sloupce a přejmenuje je pro čtenáře:

```sql
SELECT oznaceni AS ucebna, kapacita
FROM ucebna
WHERE budova = 'Budova B'
  AND kapacita >= 24
ORDER BY kapacita DESC, oznaceni ASC;
```

`SELECT` určuje požadované výrazy, `FROM` zdroj, `WHERE` podmínku a `ORDER BY` pořadí. Bez `ORDER BY` není pořadí výsledku zaručeno, i když se při několika spuštěních náhodou jeví stejně. `SELECT *` je užitečný při průzkumu, v aplikaci je však lepší vyjmenovat potřebné sloupce: výsledek je stabilnější, srozumitelnější a nepřenáší zbytečná data.

Podmínky používají porovnání, logické operátory `AND`, `OR`, `NOT`, množinu `IN`, interval `BETWEEN` a vzor `LIKE`. Závorky jsou důležité, protože `AND` má přednost před `OR`. Pro chybějící hodnotu platí `IS NULL` nebo `IS NOT NULL`. Pokud chceme odstranit duplicitní kombinace ve výsledku, použijeme `DISTINCT`; ten však nemá zakrývat špatné spojení tabulek.

Omezení počtu výsledků pomocí `LIMIT`, případně standardního `FETCH FIRST`, dává smysl společně s řazením. Dotaz „deset největších učeben“ musí nejprve definovat, co znamená největší a jak rozhodnout při shodě. Bez deterministického pořadí není ani stránkování výsledků stabilní.

## 4.2 Výrazy, funkce a práce s NULL

Ve výběru nemusí být pouze uložené sloupce. Lze počítat délku rezervace, spojovat text nebo vytvářet kategorie:

```sql
SELECT rezervace_id,
       ucel,
       CASE
           WHEN stav = 'zrusena' THEN 'neplatná'
           WHEN zacatek < CURRENT_TIMESTAMP THEN 'proběhlá'
           ELSE 'plánovaná'
       END AS kategorie
FROM rezervace;
```

Funkce pro text, čísla a čas se mezi produkty částečně liší. Také výpočty s `NULL` obvykle vracejí `NULL`, protože výsledek s neznámou hodnotou nelze určit. Funkce `COALESCE(hodnota, nahrada)` vybere první hodnotu, která není `NULL`, a je vhodná například pro zobrazení náhradního popisku. Nemá však bezmyšlenkovitě měnit „neznámou kapacitu“ na nulu – tyto stavy znamenají něco jiného.

Logické pořadí zpracování dotazu se liší od pořadí zápisu. Zjednodušeně vznikne zdroj z `FROM` a `JOIN`, následuje filtrování `WHERE`, seskupení `GROUP BY`, filtr skupin `HAVING`, výpočet výrazů `SELECT`, odstranění duplicit a nakonec řazení a omezení výsledku. To vysvětluje například, proč alias vytvořený v `SELECT` obvykle nelze použít ve `WHERE` stejné úrovně dotazu.

## 4.3 Agregace mění úroveň detailu

Agregační funkce `COUNT`, `SUM`, `AVG`, `MIN` a `MAX` shrnují více řádků. Chceme-li zjistit počet aktivních rezervací pro jednotlivé učebny, seskupíme je:

```sql
SELECT ucebna_id,
       COUNT(*) AS pocet_rezervaci,
       MIN(zacatek) AS prvni_termin,
       MAX(konec) AS posledni_termin
FROM rezervace
WHERE stav = 'aktivni'
GROUP BY ucebna_id
HAVING COUNT(*) >= 5
ORDER BY pocet_rezervaci DESC;
```

`WHERE` odstraňuje jednotlivé řádky před seskupením, zatímco `HAVING` filtruje až hotové skupiny. Ve výběru seskupeného dotazu smí být zpravidla jen seskupovací sloupce a agregované výrazy. Jinak by databáze nevěděla, kterou z několika hodnot skupiny zobrazit.

`COUNT(*)` počítá řádky, zatímco `COUNT(sloupec)` pouze řádky, v nichž daný sloupec není `NULL`. `AVG` rovněž neznámé hodnoty ignoruje. Výsledek průměru proto může klamat, pokud chybějí údaje právě u určité skupiny. SQL provede výpočet správně, ale nezaručí správnou interpretaci.

## 4.4 Poddotazy a CTE rozdělují složitou otázku

**Poddotaz** je dotaz vložený do jiného dotazu. Lze jím například najít učebny s nadprůměrnou kapacitou:

```sql
SELECT oznaceni, kapacita
FROM ucebna
WHERE kapacita > (SELECT AVG(kapacita) FROM ucebna);
```

Pro delší postup bývá čitelnější **CTE – Common Table Expression** zavedený klauzulí `WITH`. Pojmenuje pomocný výsledek platný pro jeden dotaz:

```sql
WITH vytizeni AS (
    SELECT ucebna_id, COUNT(*) AS pocet
    FROM rezervace
    WHERE stav = 'aktivni'
    GROUP BY ucebna_id
)
SELECT u.oznaceni, v.pocet
FROM vytizeni AS v
JOIN ucebna AS u ON u.ucebna_id = v.ucebna_id
WHERE v.pocet >= 10;
```

CTE není automaticky rychlejší; jeho hlavní výhodou je často srozumitelnost. Databázový optimalizátor může podle produktu a verze pomocný výsledek začlenit do plánu nebo jej samostatně materializovat.

---

# Lekce 5: Když odpověď leží ve více tabulkách

## 5.1 JOIN skládá související řádky

Normalizovaná databáze ukládá fakta odděleně, ale uživatel chce souvislou odpověď. `JOIN` kombinuje řádky podle podmínky vztahu:

```sql
SELECT r.rezervace_id,
       u.oznaceni AS ucebna,
       z.jmeno AS organizator,
       r.zacatek,
       r.ucel
FROM rezervace AS r
JOIN ucebna AS u
  ON u.ucebna_id = r.ucebna_id
JOIN uzivatel AS z
  ON z.uzivatel_id = r.organizator_id
WHERE r.stav = 'aktivni'
ORDER BY r.zacatek;
```

Nezadaný typ `JOIN` obvykle znamená `INNER JOIN`: ve výsledku zůstanou pouze odpovídající dvojice. `LEFT JOIN` zachová každý řádek levé tabulky a při chybějícím protějšku doplní sloupce pravé strany hodnotami `NULL`. To se hodí pro otázku „ukaž všechny učebny, i ty bez rezervace“.

U vnějšího spojení záleží na umístění podmínky. Podmínka pravé tabulky ve `WHERE` může odstranit právě řádky s `NULL` a nechtěně změnit chování `LEFT JOIN` na vnitřní spojení. Kritérium, které má rozhodovat o shodě, proto často patří do `ON`:

```sql
SELECT u.oznaceni, COUNT(r.rezervace_id) AS aktivni_rezervace
FROM ucebna AS u
LEFT JOIN rezervace AS r
  ON r.ucebna_id = u.ucebna_id
 AND r.stav = 'aktivni'
GROUP BY u.ucebna_id, u.oznaceni;
```

Chybějící nebo chybná podmínka spojení vytvoří kartézský součin, tedy každou kombinaci řádků. Výsledné tisíce duplicit nejsou důvodem přidat `DISTINCT`; je třeba opravit vztah.

## 5.2 Vazební tabulka a vztah N:M

Seznam účastníků jedné rezervace vede přes vazební tabulku:

```sql
SELECT r.ucel, u.jmeno, u.email
FROM rezervace AS r
JOIN ucastnik_rezervace AS ur
  ON ur.rezervace_id = r.rezervace_id
JOIN uzivatel AS u
  ON u.uzivatel_id = ur.uzivatel_id
WHERE r.rezervace_id = 481
ORDER BY u.jmeno;
```

Každý `JOIN` odpovídá jednomu kroku v datovém modelu. Zápis není technická překážka, kterou by bylo třeba obcházet uložením seznamu identifikátorů do textu. Právě vazební tabulka dovoluje kontrolovat jedinečnost účasti, přidat čas přihlášení a efektivně vyhledat jak lidi dané rezervace, tak rezervace daného člověka.

Tabulku lze spojit i samu se sebou – **self join**. Pokud by uživatel měl `vedouci_id` odkazující na jiného uživatele, dva aliasy téže tabulky by zobrazily pracovníka a jeho vedoucího. Alias tedy není jen zkratka; umožňuje rozlišit různé role stejného zdroje.

## 5.3 Pohledy skrývají složitost, ne cenu výpočtu

**Pohled – view** je pojmenovaný dotaz, který se používá podobně jako tabulka:

```sql
CREATE VIEW aktivni_rezervace AS
SELECT r.rezervace_id, u.oznaceni, r.zacatek, r.konec, r.ucel
FROM rezervace AS r
JOIN ucebna AS u ON u.ucebna_id = r.ucebna_id
WHERE r.stav = 'aktivni';
```

Pohled sjednocuje často používanou logiku a může zpřístupnit jen vybrané řádky či sloupce. Běžný pohled však obvykle neukládá výsledek; při použití se jeho dotaz znovu stane součástí plánu. **Materializovaný pohled** výsledek fyzicky uchovává a může výrazně urychlit náročný přehled, ale musí se obnovovat a mezi obnovami může být zastaralý.

Pohled není absolutní bezpečnostní bariéra. Záleží na oprávněních, vlastnictví a chování konkrétního databázového systému. Je jednou vrstvou návrhu přístupu, nikoli náhradou celého bezpečnostního modelu.

## 5.4 Procedury, funkce a triggery

Databáze mohou obsahovat uložené funkce a procedury. Funkce obvykle vrací hodnotu nebo tabulku, procedura představuje volaný postup; přesné možnosti se mezi produkty výrazně liší. Hodí se pro operaci, která musí být jednotná pro více aplikací, nebo pro práci těsně spojenou s daty. Ne každá obchodní logika však patří do databáze. Skrytý a rozsáhlý procedurální kód může ztížit testování, verzování i přechod na jiný systém.

**Trigger – spoušť** se automaticky aktivuje při události, například před nebo po vložení, změně či odstranění řádku. Může vést auditní stopu nebo udržovat technický odvozený údaj. Jeho výhodou je, že reaguje bez ohledu na použitou aplikaci; nevýhodou je méně viditelné chování. Trigger nemá nahrazovat jednoduché `CHECK`, cizí klíč ani správně navrženou transakci.

Uložená procedura ani trigger automaticky nechrání před SQL injection. Pokud uvnitř skládá příkaz spojováním textu s nedůvěryhodným vstupem, zranitelnost zůstává. Bezpečnost vyžaduje oddělit příkaz od dat a správně nastavit oprávnění.

---

# Lekce 6: Transakce, výkon, bezpečnost a provoz

## 6.1 Transakce chrání celek operace

Přihlášení účastníka může zahrnovat kontrolu kapacity, vložení vazby a zápis události do auditu. Pokud se provede pouze část, databáze zůstane v rozporu. **Transakce** sdružuje operace do jednoho logického celku:

```sql
BEGIN;

INSERT INTO ucastnik_rezervace (rezervace_id, uzivatel_id)
VALUES (481, 37);

UPDATE rezervace
SET ucel = 'Konzultace týmového projektu'
WHERE rezervace_id = 481;

COMMIT;
```

Při chybě lze místo `COMMIT` použít `ROLLBACK`. Vlastnosti transakcí se shrnují zkratkou **ACID**. Atomicita znamená „všechno, nebo nic“. Konzistence říká, že transakce převádí databázi mezi stavy splňujícími definovaná pravidla – databáze však sama nepozná pravidlo, které návrhář vůbec nezapsal. Izolace omezuje nežádoucí vliv souběžných transakcí a trvalost zajišťuje, že potvrzená změna přežije běžný výpadek.

Izolace není vždy absolutní. Databázové systémy nabízejí úrovně, které vyvažují přísnost a souběh. Slabší izolace může připustit, že dva kroky jednoho procesu uvidí odlišný stav; silnější může častěji čekat nebo rušit konfliktní transakce. Pro dvojí rezervaci stejného termínu je nejlepší, když je zákaz překryvu vyjádřen omezením nebo správnou transakční strategií, nikoli pouze nadějí, že dva uživatelé nekliknou současně.

**Deadlock** vznikne, když transakce čekají v kruhu na prostředky držené jedna druhou. Databáze jednu z nich obvykle zruší, aby kruh přerušila. Aplikace proto musí umět některé transakce bezpečně zopakovat a držet je krátké; nemá například během otevřené transakce čekat, až uživatel potvrdí dialog.

## 6.2 Index je rejstřík s provozní cenou

Index je pomocná datová struktura, která umožňuje najít řádky bez procházení celé tabulky. Pro vyhledávání rezervací učebny podle času může být užitečný složený index:

```sql
CREATE INDEX idx_rezervace_ucebna_zacatek
ON rezervace (ucebna_id, zacatek);
```

Pořadí sloupců je podstatné. Tento index dobře podporuje hledání podle učebny a začátku, nemusí však stejně pomoci dotazu pouze podle `zacatek`. Kromě běžných B-tree indexů existují podle produktu fulltextové, prostorové a další specializované struktury. `UNIQUE` index navíc může vynucovat jedinečnost, ale obecně je vhodné významové pravidlo zapisovat jako omezení schématu.

Index není bezplatné zrychlení. Zabírá místo a každý `INSERT`, `UPDATE` či `DELETE` jej musí udržovat. Při čtení velké části tabulky může být sekvenční průchod rychlejší než mnoho jednotlivých přístupů přes index. O skutečném postupu rozhoduje optimalizátor podle statistik a ceny operací.

Příkaz `EXPLAIN` zobrazí plán dotazu; varianta `EXPLAIN ANALYZE` jej v řadě systémů také provede a změří, takže se u měnících příkazů musí používat obezřetně. Optimalizace začíná správnou otázkou, vhodným schématem a měřením. Přidávat index ke každému sloupci nebo přepisovat dotaz podle dojmu často databázi spíše zatíží.

## 6.3 SQL injection a princip nejmenších oprávnění

Nebezpečný program sestaví dotaz spojením příkazu a uživatelského textu:

```text
"SELECT * FROM uzivatel WHERE email = '" + vstup + "'"
```

Útočník může do vstupu vložit část SQL a změnit význam příkazu. Obrana nespočívá v ručním nahrazování apostrofů, ale v **parametrizovaném dotazu**, kde kód a data putují do databáze odděleně:

```text
SELECT uzivatel_id, jmeno
FROM uzivatel
WHERE email = ?
```

Konkrétní značka parametru závisí na ovladači. Hodnota se nevkládá do SQL řetězce; předá se zvlášť přes databázové API. Parametry obvykle nelze použít místo názvu tabulky nebo směru řazení, a tak se podobné volby vybírají z pevného seznamu povolených možností.

Další vrstvou je **princip nejmenších oprávnění**. Veřejná část aplikace nepotřebuje právo mazat tabulky a reportovací účet nemá měnit rezervace. Citlivá data se chrání při přenosu i uložení, přístupy se zaznamenávají a tajné údaje se neukládají do zdrojového kódu. Hesla uživatelů se nešifrují „pro pozdější přečtení“, ale ukládají jako odolné solené hashe vytvořené algoritmem určeným pro hesla.

## 6.4 Záloha, replikace a obnova nejsou totéž

Záloha má smysl jen tehdy, pokud z ní lze obnovit požadovaný stav. SQL dump je přenositelný a čitelný způsob logické zálohy menších systémů, ale velké databáze často používají fyzické zálohy a průběžné archivování transakčních záznamů. Správce stanoví, kolik dat je přijatelné ztratit a jak dlouho smí obnova trvat, a postup pravidelně testuje.

Replika udržuje další průběžnou kopii databáze kvůli dostupnosti nebo čtení. Chybné smazání se však může okamžitě přenést i na ni. **Replikace proto není záloha.** Stejně tak export do CSV nezachytí celé schéma, omezení, oprávnění a transakční stav databáze.

Monitorování sleduje dostupnost, dobu dotazů, čekání na zámky, využití úložiště, chybovost a úspěch záloh. Samotné číslo bez kontextu nestačí. Pomalý dotaz může být důsledkem chybějícího indexu, zastaralých statistik, nevhodného modelu, čekání na jinou transakci nebo prostě požadavku na příliš mnoho dat.

## 6.5 Databáze v aplikaci a role AI

Aplikace obvykle nepředává uživateli přímé připojení k databázi. Přijme požadavek, ověří identitu a oprávnění, provede validační a obchodní pravidla, spustí parametrizované dotazy v transakci a vrátí pouze potřebný výsledek. Databázová připojení jsou nákladná, proto se často sdílejí v omezeném **poolu připojení**. Objektově-relační mapování (**ORM**) může převádět objekty programu na tabulky a vytvářet SQL, ale neodstraňuje potřebu rozumět klíčům, transakcím ani výkonu. Špatně použitý ORM může například nenápadně spustit stovky jednotlivých dotazů místo jednoho spojení.

Generativní AI může navrhnout schéma, vysvětlit chybovou zprávu nebo sestavit první verzi dotazu. Nezná však automaticky skutečný význam dat, místní oprávnění ani důsledky změny. Vymyšlený název sloupce je snadno odhalitelný; horší je syntakticky správný dotaz, který násobí řádky chybným spojením nebo interpretuje `NULL` jako nulu. Dotaz vytvořený AI je proto třeba číst, spouštět nejprve nad bezpečnými testovacími daty, ověřit očekávaný počet řádků a před změnou dat použít transakci či kontrolní kopii. Do veřejné AI služby se nemají vkládat skutečná hesla, osobní údaje ani neveřejný obsah databáze.

---

# Závěrečné propojení: od světa k odpovědi

Relační databáze nezačíná příkazem `CREATE TABLE`, ale porozuměním skutečnosti, kterou má systém zachytit. Analýza rozliší objekty, události a pravidla. ER model ukáže vztahy a kardinality. Normalizace odhalí, zda je každý fakt uložen na správném místě. Klíče a omezení převedou významová pravidla do schématu, které je dokáže vynucovat.

SQL potom pracuje nad celými množinami řádků. `SELECT` vybírá a transformuje, `WHERE` filtruje, `JOIN` znovu propojuje normalizovaná fakta a `GROUP BY` mění detailní záznamy na souhrn. `INSERT`, `UPDATE` a `DELETE` mění stav systému, a proto musí respektovat integritu a transakční hranice. Pohledy, procedury a triggery mohou soustředit opakovanou logiku, ale jejich přínos závisí na čitelnosti a správném použití.

V provozu se k logické správnosti přidávají další otázky: co nastane při dvou současných požadavcích, který index skutečně pomůže, kdo smí operaci provést a zda lze data po havárii obnovit. Kvalitní databázové řešení proto není nejdelší SQL dotaz ani největší počet tabulek. Je to systém, v němž model odpovídá realitě, pravidla chrání data, dotazy dávají ověřitelné odpovědi a provoz počítá s chybou člověka, programu i techniky.

