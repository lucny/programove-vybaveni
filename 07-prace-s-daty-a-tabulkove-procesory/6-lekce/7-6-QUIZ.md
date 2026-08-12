<!--
title: Trend, predikce a odpovědný datový workflow – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co může obsahovat časová řada?**

<!-- data-randomize="true" -->
[(X)] Trend, sezónnost a šum.
[( )] Pouze lineární trend.
[( )] Vždy jen náhodu.
[( )] Výhradně kategorická data.

---

**2. Co dělá klouzavý průměr?**

<!-- data-randomize="true" -->
[(X)] Vyhlazuje krátkodobé kolísání pomocí sousedních období.
[( )] Odstraňuje všechny chyby měření.
[( )] Dokazuje trend.
[( )] Převádí data na procenta.

---

**3. Co vyjadřuje R²?**

<!-- data-randomize="true" -->
[(X)] Jakou část variability sledovaných dat model zachycuje.
[( )] Pravděpodobnost kauzality.
[( )] Počet trénovacích řádků.
[( )] Přesnost senzoru.

---

**4. Co je interpolace?**

<!-- data-randomize="true" -->
[(X)] Odhad uvnitř rozsahu známých hodnot.
[( )] Odhad mimo známý rozsah.
[( )] Vyhlazení grafu.
[( )] Rozdělení dat.

---

**5. Co je extrapolace?**

<!-- data-randomize="true" -->
[(X)] Odhad mimo rozsah známých dat.
[( )] Použití mediánu.
[( )] Výpočet uvnitř známého rozsahu.
[( )] Čištění dat.

---

**6. Proč se oddělují trénovací a testovací data?**

<!-- data-randomize="true" -->
[(X)] Aby se ověřilo chování modelu na dosud neviděných případech.
[( )] Aby se zdvojnásobil počet dat.
[( )] Aby se model naučil testovací odpovědi.
[( )] Kvůli barvě grafu.

---

**7. Co je overfitting?**

<!-- data-randomize="true" -->
[(X)] Přílišné přizpůsobení trénovacím datům s horším výkonem na nových datech.
[( )] Příliš malý sešit.
[( )] Chyba v importu CSV.
[( )] Použití jednoduchého modelu.

---

**8. Kdy může být vhodné přejít od tabulky k jinému nástroji?**

<!-- data-randomize="true" -->
[[X]] při velkém objemu
[[X]] při opakovaném workflow
[[X]] při potřebě verzovat postup
[[X]] při složitější automatizaci
[[ ]] pouze když tabulka nemá barvy

---

**9. Jak má být používán AI asistent při datové práci?**

<!-- data-randomize="true" -->
[(X)] Jeho návrhy se mají testovat na známých případech a kontrolovat proti zdroji.
[( )] Jeho výsledek se považuje za automaticky správný.
[( )] Může ignorovat význam sloupců.
[( )] Není nutné uchovat vstupní data.

---

**10. Co patří k odpovědnému datovému workflow?**

<!-- data-randomize="true" -->
[[X]] ochrana soukromí
[[X]] dokumentace kroků
[[X]] reprodukovatelnost
[[X]] kontrola zdrojů
[[ ]] neoprávněné nahrávání citlivých dat do AI


# 2. Interaktivní shrnutí kapitoly

## Trend a model

Časová řada může obsahovat trend, [[sezónnost]] a šum. Klouzavý průměr průběh vyhlazuje, ale delší okno skrývá více krátkodobých změn.

Lineární regrese používá model `y = ax + b`. Hodnota [[R²]] říká, jakou část variability dat model zachycuje, nikoli zda je vztah příčinný.

## Predikce

Interpolace odhaduje uvnitř známého rozsahu, [[extrapolace]] mimo něj a je proto riskantnější. Trénovací data slouží k nastavení modelu, testovací data k nezávislé kontrole.

Overfitting znamená [[přeučení]] na trénovací sadě. U časových řad je nutné respektovat směr času a nepouštět budoucí informace do tréninku.

## Nástroje a automatizace

Tabulkový procesor je výborný pro průzkum a menší analýzy. Power Query, databáze nebo Python jsou vhodnější, když ruční postup přestává být opakovatelný a [[kontrolovatelný]].

**Vyber správná pravidla práce s AI:**

<!-- data-randomize="true" -->
[[X]] ověřit vzorec na ručně známých případech
[[X]] zkontrolovat prázdné a krajní hodnoty
[[X]] uchovat vstup i kód
[[ ]] považovat přesvědčivou odpověď za důkaz správnosti

## Etika a reprodukovatelnost

Citlivá data se do externí služby nevkládají bez oprávnění. Reprodukovatelnost vyžaduje zdokumentované zdroje, transformace a [[verze]] nástrojů. AI zvyšuje potřebu rozumět postupu, ne ji snižuje.
