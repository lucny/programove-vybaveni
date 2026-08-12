## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**SQL je deklarativní jazyk**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**SQL – Structured Query Language** slouží k definici, čtení a změnám dat v relačních databázích. Je převážně deklarativní: uživatel popíše, jaký výsledek chce, zatímco databázový optimalizátor volí plán provedení. Stejný dotaz může podle velikosti tabulek, indexů a statistik použít zcela jiný postup, aniž by se změnil jeho význam.

Příkazy se tradičně dělí do skupin. **DDL** definuje strukturu (`CREATE`, `ALTER`, `DROP`), **DML** pracuje s daty (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, případně `MERGE`), **DCL** řídí oprávnění (`GRANT`, `REVOKE`) a **TCL** ovládá transakce (`COMMIT`, `ROLLBACK`). Hranice nejsou ve všech učebnicích ani databázových systémech totožné; důležitější než zkratky je rozumět účinku příkazu.

SQL je standardizovaný jazyk, ale jednotlivé produkty mají vlastní datové typy, funkce a rozšíření. `LIMIT` je běžné v PostgreSQL, MySQL či SQLite, zatímco standardní SQL používá také konstrukci `FETCH FIRST`. Následující ukázky jsou záměrně blízké PostgreSQL a standardnímu SQL; při práci s jiným systémem je třeba ověřit jeho dokumentaci.

***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Schéma jako spustitelná specifikace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**INSERT, UPDATE a DELETE mění stav systému**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Databázový server, klient a role uživatelů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Databázový systém se často skládá ze serveru a klientů. Server přijímá spojení, ověřuje uživatele, plánuje dotazy, řídí souběh a ukládá data. Klientem může být administrační program, příkazová řádka, analytický nástroj nebo webová aplikace používající databázový ovladač. Nástroje jako pgAdmin, MySQL Workbench či DBeaver práci zpříjemňují, ale pravidla nevytváří grafické rozhraní – vykonává je databázový server.

Správce databáze (**DBA**) se stará o účty, oprávnění, zálohy, obnovu, aktualizace, sledování výkonu a dostupnost. Název superuživatele není univerzálně `root`; závisí na produktu a instalaci. Aplikace navíc nemá běžet s nejvyššími právy. Účet rezervační služby má dostat pouze oprávnění, která skutečně potřebuje.

---

# Lekce 4: SELECT – od otázky k výsledku

***
