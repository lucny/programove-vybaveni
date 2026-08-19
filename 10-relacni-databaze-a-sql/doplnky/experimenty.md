# Experimenty

*Poznámka: Následující text vychází z vašich zdrojů, ze kterých čerpá teoretické koncepty, strukturu lekcí a odborné termíny (což je vždy označeno příslušnou citací). Konkrétní návodné postupy, scénáře experimentů a odkazy na externí softwarové nástroje a webové aplikace jsou mým vlastním doplněním nad rámec zdrojového textu, abych plně vyhověl vašemu zadání. Tyto externí informace si můžete chtít nezávisle ověřit.*

Tento dokument obsahuje 36 praktických úloh rozdělených do šesti kapitol, které vám umožní vyzkoušet si práci s relačními databázemi v praxi pomocí volně dostupných nástrojů.

---

### Lekce 1: Data jako tabulky, vztahy a pravidla
*Teoretický základ: Databáze rozděluje skutečnosti do relací (tabulek) a využívá klíče pro zajištění identity a vztahů (1:N, 1:1, N:M). Záznamy mohou obsahovat hodnotu NULL vyjadřující chybějící údaj.*

**1. Zkoumání významu hodnoty NULL**
*   **Nástroj:** [DB Fiddle](https://www.db-fiddle.com/) (Online)
*   **Postup:** Vytvořte tabulku `clanek` se sloupci `titulek` a `publikovan_at`. Vložte jeden článek s aktuálním datem a jeden koncept s hodnotou `NULL`. Následně si vyzkoušejte napsat dotaz `SELECT * FROM clanek WHERE publikovan_at = NULL` a zjistíte, že nevrátí nic. Poté dotaz opravte na správné `IS NULL`.

**2. Otestování primárního a alternativního klíče**
*   **Nástroj:** [W3Schools SQL Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) (Online)
*   **Postup:** Vytvořte tabulku s umělým klíčem `clanek_id` jako `PRIMARY KEY` a sloupcem `slug` jako alternativním klíčem s omezením `UNIQUE`. Pokuste se vložit dva články se stejným slugem. Databáze by měla vyhodit chybu, čímž si v praxi ověříte identitu záznamů.

**3. Vynucení referenční integrity cizím klíčem**
*   **Nástroj:** [DB Browser for SQLite](https://sqlitebrowser.org/) (Zdarma ke stažení)
*   **Postup:** Založte tabulku `uzivatel` a tabulku `clanek` s cizím klíčem `autor_id`, který odkazuje na uživatele. Zkuste do tabulky `clanek` vložit záznam s `autor_id`, které v tabulce uživatelů neexistuje. Systém operaci odmítne jako porušení pravidla.

**4. Modelování vztahu 1:N (Autor a jeho články)**
*   **Nástroj:** [DrawSQL](https://drawsql.app/) (Online)
*   **Postup:** Založte si nový diagram. Vytvořte entitu Autor a entitu Článek. Použijte nástroj pro spojení a nastavte vztah tak, aby cizí klíč ležel na straně „mnoho“ (v tabulce Článek). Vizuálně tak uvidíte, jak se struktura propíše do definice tabulky.

**5. Modelování vztahu N:M přes vazební tabulku**
*   **Nástroj:** [QuickDBD](https://www.quickdatabasediagrams.com/) (Online)
*   **Postup:** Vztah N:M nelze vyjádřit jediným klíčem. Do textového editoru nástroje napište definice tabulek `Clanek` a `Stitek`. Následně vytvořte třetí tabulku `Clanek_Stitek`, která bude obsahovat cizí klíče na obě předchozí. Sledujte, jak program automaticky vykreslí propojovací čáry.

**6. Hra SQL Island – Záchrana pomocí tabulek**
*   **Nástroj:** [SQL Island](http://www.sql-island.de/) (Online simulace)
*   **Postup:** Otevřete interaktivní simulaci. Pomocí jednoduchých příkazů v prostředí textové hry objevujte strukturu místních relačních tabulek, abyste našli obyvatele, předměty a z ostrova se zachránili. Slouží k upevnění mentálního modelu fungování tabulek.

---

### Lekce 2: Od požadavků k dobře navrženému schématu
*Teoretický základ: Schémata navrhujeme pomocí ER diagramů a následně je normalizujeme (1NF, 2NF, 3NF), abychom omezili anomálie. Změny schématu se ukládají jako migrace.*

**1. Kreslení v notaci Crow's foot**
*   **Nástroj:** [diagrams.net (Draw.io)](https://app.diagrams.net/) (Online / Desktop)
*   **Postup:** V levém menu si zapněte knihovnu tvarů „Entity Relation“. Vytvořte entity redakčního systému a pomocí spojnic typu Crow's foot (vraní nožka) nastavte kardinality vztahů přímo na koncích čar tak, jak to popisují principy ER modelování.

**2. Experiment s 1. normální formou (1NF) a vícehodnotovými atributy**
*   **Nástroj:** Google Sheets / MS Excel
*   **Postup:** Vytvořte si tabulku redakčního systému, kde do jedné buňky vložíte více štítků oddělených čárkou. Poté zkuste pomocí filtrů najít všechny články pouze s jedním specifickým štítkem. Uvědomte si složitost takové operace a data rozdělte do více tabulek, aby každá buňka byla atomická.

**3. Odstranění tranzitivních závislostí (3NF)**
*   **Nástroj:** [SQL Fiddle](http://sqlfiddle.com/) (Online)
*   **Postup:** Navrhněte tabulku `clanek`, která obsahuje `rubrika_id` i `nazev_rubriky`. Jde o porušení 3NF. Uložte záznamy. Následně vyzkoušejte, jak složité je přejmenovat rubriku (musíte aktualizovat mnoho řádků). Upravte schéma přesunutím názvu do samostatné tabulky `rubrika`.

**4. Reverse a Forward Engineering**
*   **Nástroj:** [MySQL Workbench](https://www.mysql.com/products/workbench/) (Zdarma ke stažení)
*   **Postup:** Pomocí nástroje vytvořte grafický ER model tabulek. Následně v menu zvolte možnost "Forward Engineer". Nástroj za vás z grafického modelu vygeneruje skutečný DDL SQL skript (příkazy CREATE TABLE).

**5. Identifikace a modelování slabé entity**
*   **Nástroj:** [dbdiagram.io](https://dbdiagram.io/) (Online)
*   **Postup:** Napište definici tabulky `Clanek` a tabulky `Revize`. Nastavte primární klíč tabulky `Revize` jako složený ze sloupců `(clanek_id, cislo_revize)`, protože revize nedává smysl bez vlastníka. Vygenerujte vizualizaci a prozkoumejte kardinalitu.

**6. Textové migrace databáze**
*   **Nástroj:** [Flyway](https://flywaydb.org/) (Open-source CLI / Desktop)
*   **Postup:** Stáhněte si Flyway. Vytvořte dva soubory: `V1__Create_clanek_table.sql` a `V2__Add_stav_column.sql`. Připojte Flyway k lokální SQLite nebo MySQL databázi a spusťte migraci. Ověříte si, že se schéma mění řízeně a verzovaně, nikoliv ručním zásahem na serveru.

---

### Lekce 3: Správa databáze, uživatelé a spolehlivost dat
*Teoretický základ: DBA spravuje oprávnění (GRANT, REVOKE), dostupnost a integritu dat. Pro efektivní hledání se tvoří indexy a zajišťuje se bezpečné zálohování.*

**1. Princip nejmenších oprávnění v praxi**
*   **Nástroj:** [pgAdmin](https://www.pgadmin.org/) s PostgreSQL
*   **Postup:** Vytvořte dvě role: `redaktor` a `ctenar`. Pomocí příkazu `GRANT SELECT ON clanek TO ctenar` a `GRANT INSERT, UPDATE ON clanek TO redaktor` omezte přístupy. Zkuste se přihlásit jako `ctenar` a smazat článek. Databáze operaci odepře.

**2. Doménová integrita pomocí klauzule CHECK**
*   **Nástroj:** [DB Browser for SQLite](https://sqlitebrowser.org/) (Zdarma ke stažení)
*   **Postup:** Vytvořte tabulku `clanek` a k atributu `stav` přidejte omezení `CHECK (stav IN ('koncept', 'schvalen', 'publikovan'))`. Zkuste vložit článek se stavem 'smazano'. Experiment prokáže, jak databáze sama chrání platnost dat.

**3. Testování kaskádového mazání (CASCADE)**
*   **Nástroj:** [DB Fiddle](https://www.db-fiddle.com/) (Online)
*   **Postup:** Vytvořte vazební tabulku pro štítky s pravidlem `ON DELETE CASCADE` u cizího klíče článku. Vložte článek a propojte ho se štítkem. Poté článek smažte. Výpisem (SELECT) z vazební tabulky zjistíte, že podpůrné vazby zmizely automaticky společně s článkem.

**4. Sledování vlivu indexu na exekuční plán**
*   **Nástroj:** [SQLite CLI](https://www.sqlite.org/cli.html) (Součást Windows/Linux)
*   **Postup:** Vytvořte tabulku se 100 000 řádky (můžete použít jednoduchý skript). Spusťte hledání s použitím příkazu `EXPLAIN QUERY PLAN SELECT * FROM tabulka WHERE sloupec = 'hodnota'`. Zjistíte, že systém musí projít všechny řádky. Vytvořte index a operaci zopakujte – všimněte si okamžité změny exekučního plánu na efektivnější prohledávání.

**5. Import a export z CSV**
*   **Nástroj:** [DBeaver](https://dbeaver.io/) (Zdarma ke stažení)
*   **Postup:** Vytvořte si v Excelu seznam uživatelů a uložte jej jako formát CSV. V DBeaveru klikněte pravým tlačítkem na cílovou tabulku a vyberte "Import Data". Při tomto kroku zjistíte úskalí s dohodou o formátu data a oddělovačích, o kterých text hovoří.

**6. Záloha a obnova jako nutná prevence**
*   **Nástroj:** [phpMyAdmin](https://www.phpmyadmin.net/) (Zdarma online demo nebo lokální instalace)
*   **Postup:** Otevřete existující databázi a pomocí záložky Export vytvořte SQL dump. Smažte všechny tabulky (simulace havárie). Poté použijte záložku Import a soubor nahrajte zpět. Uvědomíte si, že obnova se musí zkoušet, protože neověřený soubor není záloha.

---

### Lekce 4: SQL od změny dat k přesné otázce
*Teoretický základ: Jazyk SQL slouží ke změně dat (DML) a dotazování (DQL). Základem jsou příkazy INSERT, UPDATE, DELETE a selekce se spojováním (JOIN) a agregacemi (COUNT, SUM).*

**1. Hromadná změna a opatrnost (UPDATE)**
*   **Nástroj:** [W3Schools SQL Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)
*   **Postup:** Vyzkoušejte si, jaké to je zapomenout klauzuli `WHERE`. Spusťte příkaz `UPDATE clanek SET stav = 'publikovan';`. Výsledkem bude kompletní přepsání všech záznamů. Zkuste experiment znovu, nejprve s `SELECT` ověřením a poté s přesně cíleným `WHERE clanek_id = 1`.

**2. Filtrování a stabilní řazení (ORDER BY)**
*   **Nástroj:** [HackerRank SQL](https://www.hackerrank.com/domains/sql) (Online úkoly)
*   **Postup:** Otevřete si základní úlohy na výběr dat. Pomocí `WHERE` odfiltrujte záznamy. Vyzkoušejte si, že bez klauzule `ORDER BY` není zaručeno pořadí výsledku. Použijte dva řadicí klíče pro dosažení stabilního pořadí.

**3. Vizuální demonstrace INNER JOIN a LEFT JOIN**
*   **Nástroj:** [SQL Joins Visualizer](https://sql-joins.leopard.in.ua/) (Online)
*   **Postup:** V tomto nástroji si klikáním měňte typy spojení dvou množin (A a B). Prohlédněte si, že `INNER JOIN` ponechá jen párované záznamy, zatímco `LEFT JOIN` zachová i články bez odpovídající rubriky a zbytek vyplní hodnotou `NULL`.

**4. Výpočet souhrnných statistik pomocí agregací**
*   **Nástroj:** [SQLZoo](https://sqlzoo.net/) (Online)
*   **Postup:** V sekci SUM and COUNT si vyzkoušejte dotazy na výpočet agregací. Prozkoumejte, jak se chová `COUNT(*)` (počítá všechny řádky) oproti `COUNT(sloupec)`, který bude ignorovat hodnoty NULL.

**5. Filtrování skupin klauzulí HAVING**
*   **Nástroj:** [DB Browser for SQLite](https://sqlitebrowser.org/)
*   **Postup:** Spojte články a rubriky a pomocí `GROUP BY rubrika_id` spočítejte články v každé z nich. Pokuste se k filtrování použít klauzuli `WHERE COUNT(*) > 5` a všimněte si chyby. Přepište to správně s využitím `HAVING`, které pracuje až se sestavenými skupinami.

**6. Logické rozdělení složitého dotazu (CTE)**
*   **Nástroj:** [DB Fiddle](https://www.db-fiddle.com/)
*   **Postup:** Použijte klauzuli `WITH` k vytvoření společného tabulkového výrazu (CTE) pro dočasný výpočet (např. průměrná délka článku). Tuto pojmenovanou dočasnou strukturu pak použijte v hlavním `SELECT` příkazu. Zjistíte, že dotaz je daleko čitelnější než vnořené poddotazy.

---

### Lekce 5: Databáze jako aktivní součást aplikace
*Teoretický základ: Pokročilé vlastnosti databází zahrnují pohledy, triggery, procedury a izolaci transakcí (ACID, MVCC, zamykání) pro zajištění konzistence u složitých operací.*

**1. Skrývání citlivých údajů přes pohledy (Views)**
*   **Nástroj:** [DB Fiddle](https://www.db-fiddle.com/)
*   **Postup:** Máte tabulku s uživateli obsahující citlivé e-maily a interní poznámky. Vytvořte pohled pomocí `CREATE VIEW verejni_autori AS SELECT jmeno, biografie FROM uzivatel`. Zjistíte, že tímto jednoduše sjednotíte bezpečný výstup pro veřejnou webovou aplikaci.

**2. Automatický audit pomocí triggeru**
*   **Nástroj:** [PostgreSQL v DB Fiddle](https://www.db-fiddle.com/)
*   **Postup:** Vytvořte tabulku `historie_zmen`. Nastavte trigger (databázovou spoušť), který reaguje na `UPDATE` u článku. Pokaždé, když redaktor změní titulek nebo stav, trigger automaticky zachytí starou a novou hodnotu do logovací tabulky.

**3. Testování vlastností ACID pomocí transakcí**
*   **Nástroj:** Příkazový řádek (CLI) nebo DBeaver
*   **Postup:** Spusťte transakci příkazem `BEGIN TRANSACTION`. Vložte novou rubriku a změňte článek. Pokud nastane chyba, zavolejte `ROLLBACK`. Ujistíte se, že buď proběhnou oba kroky, nebo ani jeden, takže data nezůstanou v nekonzistentním stavu.

**4. Simulace uváznutí (Deadlock)**
*   **Nástroj:** Dvě okna prohlížeče v aplikaci jako [PopSQL](https://popsql.com/) nebo dvě instance lokálního terminálu (např. MySQL).
*   **Postup:** V prvním terminálu zahajte transakci a zamkněte tabulku A. Ve druhém terminálu zahajte transakci a zamkněte tabulku B. Poté se pokuste v prvním terminálu přistoupit k tabulce B a současně ve druhém k tabulce A. Databázový systém jednu z transakcí ukončí, aby uváznutí vyřešil.

**5. Centralizace logiky do uložené procedury**
*   **Nástroj:** [Oracle Live SQL](https://livesql.oracle.com/) (ZDARMA po registraci)
*   **Postup:** Využijte procedurální jazyk (např. PL/SQL v Oracle). Napište uloženou proceduru `publikuj_clanek(id)`, která sama zkontroluje stav, doplní datum publikace, zapíše do audit logu a transakci potvrdí (COMMIT). Uvědomíte si výhodu odstínění logiky od samotné webové aplikace.

**6. Implementace optimistického zamykání**
*   **Nástroj:** Jednoduchý Python/PHP skript nebo ruční SQL test
*   **Postup:** Přidejte k článku sloupec `verze`. Dva "uživatelé" načtou článek ve stejný moment (verze 1). První odešle úpravu: `UPDATE clanek SET ..., verze = 2 WHERE verze = 1`. Změna projde. Druhý se pokusí o to samé (hledá verzi 1, která už neexistuje), a operace ohlásí konflikt, čímž nepřepíše cizí práci.

---

### Lekce 6: Od Accessu k podnikovým databázím
*Teoretický základ: Architektura RDBMS sahá od souborových (Access, SQLite) po klient-server systémy a cloud. Bezpečnostní mechanismy musí chránit proti rizikům, jako je SQL injection.*

**1. Průzkum desktopové databáze**
*   **Nástroj:** MS Access (Součást Windows/Office) nebo [LibreOffice Base](https://www.libreoffice.org/discover/base/) (Zdarma alternativa)
*   **Postup:** Otevřete aplikaci. Uvidíte, jak snadno lze vytvořit celou aplikaci (tabulky, dotazy, formuláře i sestavy) na jednom místě pro prototypování nebo školní výuku. Zkuste si představit, proč to naopak není vhodné pro systém s mnoha souběžnými čtenáři a zapisovateli z internetu.

**2. Práce se souborovou databází v jediné knihovně**
*   **Nástroj:** [SQLite](https://www.sqlite.org/) (Zdarma)
*   **Postup:** Vytvořte databázi v SQLite. Uvidíte, že celý systém je ve skutečnosti pouze jeden soubor (`databaze.db`) na vašem disku. Nepotřebujete žádný běžící server, což je ideální pro mobilní aplikace a offline koncepty.

**3. Průzkum spravované cloudové služby**
*   **Nástroj:** [Supabase](https://supabase.com/) (Má bezplatný plán)
*   **Postup:** Založte si projekt v cloudu. Vyzkoušíte si koncept "managed" služby, která za vás z velké části řeší běh serveru, jeho dostupnost i některé zálohy. Služba vám rovnou nabídne grafické rozhraní a autentizaci.

**4. Jak vypadá SQL Injection v praxi**
*   **Nástroj:** [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) (Bezpečnostní pískoviště simulující zranitelný e-shop)
*   **Postup:** Otevřete tuto výukovou aplikaci. V přihlašovacím formuláři zadejte do pole pro e-mail: `' OR '1'='1`. Protože aplikační vrstva spojila vstup přímo se zadáním bez kontroly, pozměnili jste strukturu dotazu a aplikace vás neoprávněně přihlásí.

**5. Obrana proti SQL Injection (Parametrizované dotazy)**
*   **Nástroj:** [Replit](https://replit.com/) (Online kódování) s Pythonem a knihovnou `sqlite3`
*   **Postup:** Vytvořte v Pythonu připojení k lokální DB. Připravte zranitelný příkaz (spojování řetězců pomocí `+`). Poté jej opravte do podoby s parametry: `cursor.execute("SELECT * FROM uzivatel WHERE jmeno = ?", (jmeno,))`. Tímto izolujete strukturu SQL od vkládaných hodnot.

**6. Bezpečné ukládání tajných klíčů**
*   **Nástroj:** [HashiCorp Vault](https://developer.hashicorp.com/vault/downloads) (Dev mode) nebo soubory prostředí (`.env`)
*   **Postup:** Vyzkoušejte si vyjmout přihlašovací heslo k databázi z vašeho kódu. Uložte ho do odděleného konfiguračního `.env` souboru nebo do specializovaného trezoru pro tajné údaje, abyste se vyvarovali ukládání hesel ve zdrojovém kódu na Gitu, jak varuje text.