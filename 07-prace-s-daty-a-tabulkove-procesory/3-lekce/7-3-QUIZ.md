<!--
title: Čištění a transformace: práce, kterou výsledek skrývá – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je data cleaning?**

<!-- data-randomize="true" -->
[(X)] Převádění nepravidelností do konzistentní podoby při zachování významu.
[( )] Mazání všech neobvyklých hodnot.
[( )] Pouze změna barev.
[( )] Tvorba grafu.

---

**2. Proč mohou `A203` a `A203 ` být pro program různé hodnoty?**

<!-- data-randomize="true" -->
[(X)] Druhá hodnota obsahuje navíc mezeru.
[( )] Program ignoruje text.
[( )] Číslice se neporovnávají.
[( )] Jde vždy o stejný binární zápis.

---

**3. Proč prázdná buňka není totéž co nula?**

<!-- data-randomize="true" -->
[(X)] Chybějící údaj a platná nulová hodnota mají jiný význam.
[( )] Nula se nedá uložit.
[( )] Prázdná buňka je vždy číslo.
[( )] Tabulky rozlišují jen text.

---

**4. Co je imputace?**

<!-- data-randomize="true" -->
[(X)] Odhad chybějící hodnoty podle zvoleného postupu.
[( )] Trvalé odstranění celého sloupce.
[( )] Převod jednotek.
[( )] Seřazení záznamů.

---

**5. Podle čeho se rozhoduje, zda jsou dva řádky duplicitní?**

<!-- data-randomize="true" -->
[(X)] Podle významového klíče nebo kombinace identifikátorů.
[( )] Pouze podle stejné barvy.
[( )] Vždy podle všech znaků řádku bez kontextu.
[( )] Podle pořadí v souboru.

---

**6. Co je outlier?**

<!-- data-randomize="true" -->
[(X)] Hodnota výrazně vzdálená ostatním.
[( )] Každá chybějící hodnota.
[( )] Každá hodnota nad průměrem.
[( )] Textová buňka.

---

**7. Proč se outlier nemá automaticky odstranit?**

<!-- data-randomize="true" -->
[(X)] Může být skutečným důležitým zjištěním.
[( )] Nelze jej nikdy najít.
[( )] Vždy zvyšuje přesnost.
[( )] Je vždy chybný.

---

**8. Co mohou dělat transformace dat?**

<!-- data-randomize="true" -->
[[X]] odvozovat nové proměnné
[[X]] spojovat tabulky
[[X]] měnit široký a dlouhý tvar
[[X]] agregovat časové intervaly
[[ ]] automaticky dokazovat kauzalitu

---

**9. Co znamená ETL?**

<!-- data-randomize="true" -->
[(X)] Extract, Transform, Load.
[( )] Evaluate, Test, Link.
[( )] Encode, Transfer, List.
[( )] Export, Type, Label.

---

**10. Proč se raw data nemají přepisovat?**

<!-- data-randomize="true" -->
[(X)] Aby bylo možné proces zopakovat a opravit chyby transformace.
[( )] Protože je nelze kopírovat.
[( )] Protože jsou vždy správná.
[( )] Aby se zvětšil soubor.


# 2. Interaktivní shrnutí kapitoly

## Nepravidelnosti dat

Člověk může považovat `A203`, `a203` a `A203 ` za tutéž učebnu, počítač je však může rozlišovat. Čištění dat vytváří konzistentní [[reprezentaci]] a přitom nesmí svévolně měnit význam.

Prvním krokem bývá profil dat: typy, minimum, maximum, chybějící hodnoty a [[duplicity]].

## Chybějící hodnoty

Prázdná buňka není [[nula]]. Chybění může znamenat poruchu senzoru, neprovedené měření nebo neaplikovatelnou vlastnost. Imputace vytváří odhad, nikoli skutečně naměřenou hodnotu.

Duplicitu určujeme pomocí významového [[klíče]], například `senzor_id + cas`.

## Jednotky, kategorie a outliery

Před porovnáním je nutné sjednotit [[jednotky]]. Kategorie je vhodné mapovat pomocí dohledatelné tabulky.

Outlier může být chyba, ale také důležitá událost. Rozhodnutí o odstranění musí vycházet z dat i věcného [[kontextu]].

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] 215 °C v učebně je důvod ke kontrole
[[X]] neobvyklou hodnotu nelze automaticky označit za chybu
[[X]] mapování kategorií má být dohledatelné
[[ ]] každou chybějící hodnotu nahradíme nulou

## Transformace a reprodukovatelnost

Transformace vytvářejí odvozené proměnné, spojují zdroje a mění tvar dat. ETL znamená Extract, [[Transform]], Load.

Původní [[raw]] data se zachovávají. Nad nimi vzniká vyčištěná verze a analýza, aby bylo možné celý postup zopakovat.
