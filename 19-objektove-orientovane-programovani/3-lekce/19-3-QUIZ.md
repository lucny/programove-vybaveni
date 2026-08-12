<!--
title: Dědičnost a polymorfismus – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je dědičnost?**

<!-- data-randomize="true" -->
[(X)] Mechanismus, při němž odvozená třída přebírá a rozšiřuje prvky základní třídy.
[( )] Kopírování objektu do nové proměnné.
[( )] Skrývání všech metod před potomky.
[( )] Ukládání tříd do souboru.

---

**2. Jaký vztah má vyjadřovat dědičnost?**

<!-- data-randomize="true" -->
[(X)] Specializaci typu „potomek je rodičovský typ“.
[( )] Složení typu „objekt má součást“.
[( )] Pouhé současné použití dvou tříd.
[( )] Pořadí vytváření objektů v paměti.

---

**3. Co může odvozená třída udělat s metodou rodiče?**

<!-- data-randomize="true" -->
[(X)] Překrýt ji vlastní specializovanou implementací.
[( )] Pouze ji smazat ze zdrojového jazyka.
[( )] Změnit ji na globální proměnnou.
[( )] Používat ji jen bez vytvoření objektu.

---

**4. Co je polymorfismus?**

<!-- data-randomize="true" -->
[(X)] Stejné rozhraní vyvolá různé chování podle konkrétního typu objektu.
[( )] Každý objekt musí mít odlišný název metody.
[( )] Třída smí mít pouze jednu instanci.
[( )] Objekty nemohou sdílet společného předka.

---

**5. Jak se projeví polymorfismus u metody zvuk()?**

<!-- data-randomize="true" -->
[(X)] Pes, kočka a pták reagují na stejné volání vlastním způsobem.
[( )] Všechny třídy musí vypsat totožný text.
[( )] Metodu lze volat jen na základní třídě.
[( )] Typ objektu se při volání ignoruje.

---

**6. Co znamená přetěžování metod?**

<!-- data-randomize="true" -->
[(X)] Více metod stejného jména s různými parametry.
[( )] Přepsání metody potomkem.
[( )] Volání stejné metody vícekrát v cyklu.
[( )] Příliš pomalé vykonávání metody.

---

**7. Jak Python obvykle nahrazuje klasické přetěžování z C++?**

<!-- data-randomize="true" -->
[(X)] Výchozími parametry nebo proměnným počtem argumentů.
[( )] Vícenásobným spuštěním interpretu.
[( )] Povinným použitím globálních funkcí.
[( )] Zákazem stejného názvu metody.

---

**8. Které přínosy může mít vhodná dědičnost?**

<!-- data-randomize="true" -->
[[X]] znovupoužití společného kódu
[[X]] logická hierarchie typů
[[X]] specializace překrytím metod
[[X]] snazší údržba společného chování
[[ ]] automatické odstranění všech vazeb
[[ ]] vhodnost pro každý vztah mezi objekty

---

**9. Co může komplikovat vícenásobná dědičnost?**

<!-- data-randomize="true" -->
[(X)] Konflikty metod pocházejících z různých rodičů.
[( )] Nemožnost vytvořit jediný atribut.
[( )] Zákaz polymorfismu.
[( )] Povinnou ruční správu každého objektu.

---

**10. Který vztah je přirozeným příkladem dědičnosti?**

<!-- data-randomize="true" -->
[(X)] Pes je Zvíře.
[( )] Auto má Motor.
[( )] Objednávka obsahuje Položky.
[( )] Knihovna eviduje Výpůjčky.


# 2. Interaktivní shrnutí kapitoly

## Obecný typ a jeho specializace

Dědičnost vytváří vztah mezi základní a odvozenou třídou. Potomek přebírá veřejné a chráněné prvky, může přidat další a některé metody [[překrýt]]. Vztah má dávat smysl jako „je“: `Pes je Zvire`.

Společný kód zůstává v rodiči a specializace v potomcích. Dědičnost proto [[ (není automaticky vhodná pro každý vztah) | vždy nahrazuje kompozici | znamená pouhé kopírování zdrojového souboru ]].

## Stejné volání, různá reakce

[[Polymorfismus]] dovoluje pracovat s různými objekty přes společné rozhraní. Volání `zvuk()` může u psa vyvolat štěkání a u kočky mňoukání, aniž by volající musel přepisovat základní postup pro každý typ.

**Vyber projevy polymorfního návrhu:**

<!-- data-randomize="true" -->
[[X]] společné jméno metody pro různé potomky
[[X]] chování zvolené podle skutečného typu objektu
[[X]] možnost zpracovat kolekci různých zvířat jednotným postupem
[[ ]] nutnost ručně zjišťovat typ před každým voláním
[[ ]] všechny implementace musí dělat přesně totéž

## Překrytí není přetížení

Překrytí znamená, že potomek poskytne vlastní implementaci zděděné metody. [[Přetěžování]] označuje více verzí stejného jména s různými parametry, jak je běžné v C++. Python klasické přetěžování podle signatury nepodporuje stejně; často používá výchozí parametry či proměnný počet argumentů.

Záměna pojmů vede k nepřesnému návrhu: překrytí souvisí s dědičností a dynamickým chováním, přetížení s různými způsoby volání téže pojmenované operace.

## Opětovné použití s rozmyslem

Změna společné metody v základní třídě se může projevit u všech potomků. To šetří duplicitu, ale zároveň vytváří vazbu, kterou je nutné kontrolovat. Vícenásobná dědičnost může přinést konflikt stejných metod z více rodičů.

Dobrá hierarchie proto vyjadřuje skutečnou specializaci. Vztah `Auto má Motor` se nemá modelovat děděním, protože auto [[ (není motorem) | je zvláštním druhem motoru | musí překrýt každý atribut motoru ]].
