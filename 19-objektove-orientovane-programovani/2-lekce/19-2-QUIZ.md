<!--
title: Struktura třídy a zapouzdření – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co uchovávají atributy objektu?**

<!-- data-randomize="true" -->
[(X)] Jeho stav a data.
[( )] Pouze názvy metod.
[( )] Historii verzí třídy.
[( )] Instrukce operačního systému.

---

**2. Kdy se automaticky volá konstruktor?**

<!-- data-randomize="true" -->
[(X)] Při vytváření objektu.
[( )] Při každém čtení atributu.
[( )] Jen při ukončení programu.
[( )] Při překladu komentáře.

---

**3. K čemu slouží destruktor?**

<!-- data-randomize="true" -->
[(X)] K uvolnění prostředků při zániku objektu.
[( )] K počátečnímu nastavení atributů.
[( )] K vytvoření odvozené třídy.
[( )] K přetížení každé metody.

---

**4. Jak se jmenuje konstruktor v Pythonu?**

<!-- data-randomize="true" -->
[(X)] __init__.
[( )] __del__.
[( )] constructor.
[( )] @property.

---

**5. Jak se označuje destruktor třídy Osoba v C++?**

<!-- data-randomize="true" -->
[(X)] ~Osoba().
[( )] __init__().
[( )] delete Osoba().
[( )] void constructor().

---

**6. Jaký je rozdíl mezi instančním a třídním atributem?**

<!-- data-randomize="true" -->
[(X)] Instanční patří objektu, třídní je sdílen všemi instancemi.
[( )] Třídní atribut má každý objekt vždy vlastní.
[( )] Instanční atribut existuje bez objektu pouze jednou.
[( )] Liší se jen názvem, nikoli vlastnictvím.

---

**7. Co je zapouzdření?**

<!-- data-randomize="true" -->
[(X)] Skrytí interního stavu a řízený přístup přes veřejné rozhraní.
[( )] Zkopírování všech atributů do globálního prostoru.
[( )] Povinná vícenásobná dědičnost.
[( )] Automatické ukládání objektu na disk.

---

**8. Které přínosy má zapouzdření?**

<!-- data-randomize="true" -->
[[X]] kontrola změn stavu
[[X]] ochrana invariantů
[[X]] možnost změnit vnitřní reprezentaci
[[X]] jasné veřejné rozhraní
[[ ]] přímá změna každého atributu odkudkoli
[[ ]] zrušení potřeby metod

---

**9. Co v C++ znamená private?**

<!-- data-randomize="true" -->
[(X)] Prvek je přístupný pouze z metod dané třídy.
[( )] Prvek je dostupný odkudkoli.
[( )] Prvek je dostupný jen potomkům a třídě.
[( )] Prvek neexistuje v paměti.

---

**10. K čemu slouží setter?**

<!-- data-randomize="true" -->
[(X)] K řízenému nastavení atributu včetně kontroly nové hodnoty.
[( )] K automatickému zrušení objektu.
[( )] K vytvoření třídního atributu.
[( )] K načtení všech objektů ze souboru.


# 2. Interaktivní shrnutí kapitoly

## Stav a chování v jedné třídě

Atributy uchovávají stav objektu, metody nad tímto stavem provádějí operace. Metoda se volá na konkrétním objektu, takže může pracovat s jeho vlastními hodnotami. V Pythonu je tato instance v metodě dostupná přes parametr [[self]].

Konstruktor nastavuje počáteční platný stav. V C++ má jméno třídy, v Pythonu se používá [[__init__]]. Destruktor řeší úklid prostředků při zániku; v C++ má tvar s vlnkou, v Pythonu existuje `__del__`, jeho načasování však souvisí s automatickou správou paměti.

## Co patří objektu a co třídě

Instanční atribut má každý objekt vlastní, například zůstatek konkrétního účtu. Třídní neboli statický atribut existuje jednou a sdílejí jej všechny instance, například celkový [[počet účtů]].

**Vyber správná tvrzení o prvcích třídy:**

<!-- data-randomize="true" -->
[[X]] konstruktor inicializuje nový objekt
[[X]] instanční metoda pracuje se stavem konkrétní instance
[[X]] třídní atribut může evidovat údaj společný všem objektům
[[X]] destruktor může uvolňovat držené prostředky
[[ ]] každý třídní atribut má každá instance v samostatné kopii

## Zapouzdření chrání pravidla objektu

Interní stav nemá být libovolně přepisován zvenčí. Bankovní účet například nabídne vklad a výběr, místo aby dovolil nastavit zůstatek na jakoukoli hodnotu. [[Zapouzdření]] vytváří veřejné rozhraní a skrývá implementační detaily.

C++ rozlišuje `public`, `protected` a [[private]]. Python soukromí nevynucuje stejně přísně, ale podtržítko signalizuje neveřejný prvek. Dekorátor [[@property]] umožňuje zachovat pohodlný zápis atributu a zároveň provést kontrolu v getteru či setteru.

Setter má smysl jen tehdy, pokud opravdu řídí změnu. Mechanické zpřístupnění každého privátního atributu bez pravidel by zapouzdření [[ (oslabilo) | automaticky zesílilo | změnilo na dědičnost ]]. Výhodou rozhraní je také možnost změnit vnitřní reprezentaci bez úpravy všech uživatelů třídy.
