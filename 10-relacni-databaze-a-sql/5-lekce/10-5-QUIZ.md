<!--
title: Když odpověď leží ve více tabulkách – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. K čemu slouží JOIN?**

<!-- data-randomize="true" -->
[(X)] K kombinaci souvisejících řádků z více tabulek.
[( )] K vytvoření zálohy.
[( )] K změně datového typu.
[( )] K řízení transakce.

---

**2. Co typicky znamená samotné JOIN bez upřesnění?**

<!-- data-randomize="true" -->
[(X)] INNER JOIN.
[( )] LEFT JOIN.
[( )] FULL JOIN.
[( )] CROSS JOIN.

---

**3. Co dělá LEFT JOIN?**

<!-- data-randomize="true" -->
[(X)] Zachová všechny řádky levé tabulky a doplní NULL při chybějícím protějšku.
[( )] Zachová jen shody.
[( )] Maže nepárové řádky.
[( )] Vytváří kartézský součin vždy.

---

**4. Proč může podmínka pravé tabulky ve WHERE pokazit LEFT JOIN?**

<!-- data-randomize="true" -->
[(X)] Může odstranit řádky s NULL a fakticky z něj udělat vnitřní spojení.
[( )] WHERE se po JOIN nikdy neprovádí.
[( )] LEFT JOIN zakazuje WHERE.
[( )] NULL se vždy rovná FALSE.

---

**5. Co způsobí chybějící podmínka spojení?**

<!-- data-randomize="true" -->
[(X)] Kartézský součin.
[( )] Automatickou deduplikaci.
[( )] Vždy syntaktickou chybu.
[( )] Vytvoření indexu.

---

**6. K čemu slouží vazební tabulka ve vztahu N:M?**

<!-- data-randomize="true" -->
[(X)] Reprezentuje jednotlivé vazby mezi dvěma množinami záznamů.
[( )] Nahrazuje primární klíče.
[( )] Ukládá všechny ID v jednom textu.
[( )] Je jen dočasná.

---

**7. Co je self join?**

<!-- data-randomize="true" -->
[(X)] Spojení tabulky se sebou samou pomocí různých aliasů.
[( )] JOIN bez ON.
[( )] Poddotaz bez FROM.
[( )] Materializovaný pohled.

---

**8. Co je view?**

<!-- data-randomize="true" -->
[(X)] Pojmenovaný dotaz používaný podobně jako tabulka.
[( )] Vždy fyzická kopie dat.
[( )] Index.
[( )] Transakce.

---

**9. Co je materializovaný pohled?**

<!-- data-randomize="true" -->
[(X)] Pohled, jehož výsledek je fyzicky uložen a musí se obnovovat.
[( )] Alias tabulky.
[( )] Dočasný CTE.
[( )] Trigger.

---

**10. K čemu mohou sloužit procedury, funkce a triggery?**

<!-- data-randomize="true" -->
[[X]] sjednocení databázové logiky
[[X]] auditní stopa
[[X]] automatická reakce na změnu
[[X]] výpočty těsně u dat
[[ ]] automatická ochrana před každou SQL injection


# 2. Interaktivní shrnutí kapitoly

## JOIN jako cesta modelem

Normalizovaná databáze ukládá fakta odděleně. JOIN je skládá podle [[vztahů]]. INNER JOIN ponechá shody, LEFT JOIN zachová všechny řádky levé tabulky.

Podmínka, která určuje shodu, často patří do [[ON]]. Neopatrné `WHERE` nad pravou stranou může odstranit NULL a změnit smysl LEFT JOINu. Chceme-li například vypsat všechny učebny i ty bez aktivní rezervace, stav rezervace patří do podmínky spojení, ne do následného filtru `WHERE`.

Nezadaný typ `JOIN` obvykle znamená `INNER JOIN`, takže bez protějšku řádek ve výsledku nezůstane. Chybějící či chybná podmínka spojení vytvoří kartézský součin: každá řádka jedné tabulky se spojí s každou řádkou druhé. Mnoho duplicit pak není důvod přidat [[DISTINCT]]; správným řešením je opravit vztah v `ON`.

## N:M a self join

Vazební tabulka je přirozeným řešením vztahu [[N:M]]. Každý její řádek představuje jednu vazbu a může nést další údaje.

Vazba účasti tak může kontrolovat jedinečnost přihlášení, uložit čas přihlášení a stejně dobře vyhledat lidi dané rezervace i rezervace daného člověka. Uložení seznamu identifikátorů do textu by tyto operace i kontrolu zbytečně komplikovalo. Každý `JOIN` je jeden krok po vztahu v datovém modelu.

Self join používá dvě role téže tabulky, například pracovníka a jeho [[vedoucího]]. Dva aliasy nejsou jen zkratka: dovolují rozlišit dva různé významy stejného zdroje, pokud `vedouci_id` odkazuje na dalšího uživatele.

## Pohledy

View je pojmenovaný dotaz. Může zjednodušit složitou logiku nebo omezit zpřístupněné sloupce. Běžný view výsledek obvykle fyzicky [[neukládá]].

Materializovaný pohled data uchovává a musí se obnovovat. Může tím urychlit náročný přehled, ale mezi obnovami může být zastaralý. Běžný pohled naopak při použití přidá svůj dotaz do plánu; skrývá složitost zápisu, nikoli cenu jeho výpočtu. Pohled také není absolutní bezpečnostní bariéra, protože jeho účinek závisí na oprávněních, vlastnictví a konkrétním databázovém systému.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] chybný JOIN se nemá maskovat DISTINCT
[[X]] view není automaticky absolutní bezpečnostní bariéra
[[X]] materializovaný view může být zastaralý
[[ ]] každý trigger je lepší než CHECK constraint

## Procedury a triggery

Uložené funkce a procedury mohou centralizovat operace. [[Trigger]] se automaticky spouští při události, například INSERT nebo UPDATE. Skrytá logika však může komplikovat testování, proto má mít jasný důvod.

Funkce obvykle vrací hodnotu nebo tabulku, zatímco procedura představuje volaný postup; přesné rozdíly se liší mezi produkty. Trigger se může aktivovat před nebo po vložení, změně či odstranění řádku, například kvůli auditní stopě nebo technickému odvozenému údaji. Nemá ale nahrazovat jednoduchý `CHECK`, cizí klíč ani správně navrženou transakci. Ani procedura či trigger samy nebrání SQL injection: pokud skládají příkaz z nedůvěryhodného textu, zranitelnost zůstává.

## Čitelnost a viditelnost logiky

Pohled, procedura i trigger mohou soustředit logiku používanou na více místech, ale každý přináší vlastní cenu. Pohled může zpřístupnit jen vybrané sloupce či řádky, nenahrazuje však bezpečnostní model. Rozsáhlý procedurální kód skrytý v databázi se hůře testuje, verzzuje a přenáší na jiný produkt. Trigger reaguje i tehdy, když data mění jiná aplikace, což je výhoda pro audit, ale zároveň ztěžuje hledání příčiny změny. Použití těchto prostředků má mít jasný význam a být pro tým dohledatelné.
