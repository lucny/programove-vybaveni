## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Projekce, filtrování a řazení**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Výrazy, funkce a práce s NULL**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Agregace mění úroveň detailu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Poddotazy a CTE rozdělují složitou otázku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***
