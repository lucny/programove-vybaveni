## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Transakce chrání celek operace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Index je rejstřík s provozní cenou**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Index je pomocná datová struktura, která umožňuje najít řádky bez procházení celé tabulky. Pro vyhledávání rezervací učebny podle času může být užitečný složený index:

```sql
CREATE INDEX idx_rezervace_ucebna_zacatek
ON rezervace (ucebna_id, zacatek);
```

Pořadí sloupců je podstatné. Tento index dobře podporuje hledání podle učebny a začátku, nemusí však stejně pomoci dotazu pouze podle `zacatek`. Kromě běžných B-tree indexů existují podle produktu fulltextové, prostorové a další specializované struktury. `UNIQUE` index navíc může vynucovat jedinečnost, ale obecně je vhodné významové pravidlo zapisovat jako omezení schématu.

Index není bezplatné zrychlení. Zabírá místo a každý `INSERT`, `UPDATE` či `DELETE` jej musí udržovat. Při čtení velké části tabulky může být sekvenční průchod rychlejší než mnoho jednotlivých přístupů přes index. O skutečném postupu rozhoduje optimalizátor podle statistik a ceny operací.

Příkaz `EXPLAIN` zobrazí plán dotazu; varianta `EXPLAIN ANALYZE` jej v řadě systémů také provede a změří, takže se u měnících příkazů musí používat obezřetně. Optimalizace začíná správnou otázkou, vhodným schématem a měřením. Přidávat index ke každému sloupci nebo přepisovat dotaz podle dojmu často databázi spíše zatíží.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**SQL injection a princip nejmenších oprávnění**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Záloha, replikace a obnova nejsou totéž**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Záloha má smysl jen tehdy, pokud z ní lze obnovit požadovaný stav. SQL dump je přenositelný a čitelný způsob logické zálohy menších systémů, ale velké databáze často používají fyzické zálohy a průběžné archivování transakčních záznamů. Správce stanoví, kolik dat je přijatelné ztratit a jak dlouho smí obnova trvat, a postup pravidelně testuje.

Replika udržuje další průběžnou kopii databáze kvůli dostupnosti nebo čtení. Chybné smazání se však může okamžitě přenést i na ni. **Replikace proto není záloha.** Stejně tak export do CSV nezachytí celé schéma, omezení, oprávnění a transakční stav databáze.

Monitorování sleduje dostupnost, dobu dotazů, čekání na zámky, využití úložiště, chybovost a úspěch záloh. Samotné číslo bez kontextu nestačí. Pomalý dotaz může být důsledkem chybějícího indexu, zastaralých statistik, nevhodného modelu, čekání na jinou transakci nebo prostě požadavku na příliš mnoho dat.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Databáze v aplikaci a role AI**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Aplikace obvykle nepředává uživateli přímé připojení k databázi. Přijme požadavek, ověří identitu a oprávnění, provede validační a obchodní pravidla, spustí parametrizované dotazy v transakci a vrátí pouze potřebný výsledek. Databázová připojení jsou nákladná, proto se často sdílejí v omezeném **poolu připojení**. Objektově-relační mapování (**ORM**) může převádět objekty programu na tabulky a vytvářet SQL, ale neodstraňuje potřebu rozumět klíčům, transakcím ani výkonu. Špatně použitý ORM může například nenápadně spustit stovky jednotlivých dotazů místo jednoho spojení.

Generativní AI může navrhnout schéma, vysvětlit chybovou zprávu nebo sestavit první verzi dotazu. Nezná však automaticky skutečný význam dat, místní oprávnění ani důsledky změny. Vymyšlený název sloupce je snadno odhalitelný; horší je syntakticky správný dotaz, který násobí řádky chybným spojením nebo interpretuje `NULL` jako nulu. Dotaz vytvořený AI je proto třeba číst, spouštět nejprve nad bezpečnými testovacími daty, ověřit očekávaný počet řádků a před změnou dat použít transakci či kontrolní kopii. Do veřejné AI služby se nemají vkládat skutečná hesla, osobní údaje ani neveřejný obsah databáze.

---

# Závěrečné propojení: od světa k odpovědi

Relační databáze nezačíná příkazem `CREATE TABLE`, ale porozuměním skutečnosti, kterou má systém zachytit. Analýza rozliší objekty, události a pravidla. ER model ukáže vztahy a kardinality. Normalizace odhalí, zda je každý fakt uložen na správném místě. Klíče a omezení převedou významová pravidla do schématu, které je dokáže vynucovat.

SQL potom pracuje nad celými množinami řádků. `SELECT` vybírá a transformuje, `WHERE` filtruje, `JOIN` znovu propojuje normalizovaná fakta a `GROUP BY` mění detailní záznamy na souhrn. `INSERT`, `UPDATE` a `DELETE` mění stav systému, a proto musí respektovat integritu a transakční hranice. Pohledy, procedury a triggery mohou soustředit opakovanou logiku, ale jejich přínos závisí na čitelnosti a správném použití.

V provozu se k logické správnosti přidávají další otázky: co nastane při dvou současných požadavcích, který index skutečně pomůže, kdo smí operaci provést a zda lze data po havárii obnovit. Kvalitní databázové řešení proto není nejdelší SQL dotaz ani největší počet tabulek. Je to systém, v němž model odpovídá realitě, pravidla chrání data, dotazy dávají ověřitelné odpovědi a provoz počítá s chybou člověka, programu i techniky.

***
