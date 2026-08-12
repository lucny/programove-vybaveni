## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**JOIN skládá související řádky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vazební tabulka a vztah N:M**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Pohledy skrývají složitost, ne cenu výpočtu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Procedury, funkce a triggery**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Databáze mohou obsahovat uložené funkce a procedury. Funkce obvykle vrací hodnotu nebo tabulku, procedura představuje volaný postup; přesné možnosti se mezi produkty výrazně liší. Hodí se pro operaci, která musí být jednotná pro více aplikací, nebo pro práci těsně spojenou s daty. Ne každá obchodní logika však patří do databáze. Skrytý a rozsáhlý procedurální kód může ztížit testování, verzování i přechod na jiný systém.

**Trigger – spoušť** se automaticky aktivuje při události, například před nebo po vložení, změně či odstranění řádku. Může vést auditní stopu nebo udržovat technický odvozený údaj. Jeho výhodou je, že reaguje bez ohledu na použitou aplikaci; nevýhodou je méně viditelné chování. Trigger nemá nahrazovat jednoduché `CHECK`, cizí klíč ani správně navrženou transakci.

Uložená procedura ani trigger automaticky nechrání před SQL injection. Pokud uvnitř skládá příkaz spojováním textu s nedůvěryhodným vstupem, zranitelnost zůstává. Bezpečnost vyžaduje oddělit příkaz od dat a správně nastavit oprávnění.

---

# Lekce 6: Transakce, výkon, bezpečnost a provoz

***
