<!--
title: Přesné kreslení a práce s vektorovými objekty – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. K čemu slouží snapping?**

<!-- data-randomize="true" -->
[(X)] K přesnému přichytávání objektů k definovaným bodům a liniím.
[( )] K rasterizaci celého dokumentu.
[( )] K výpočtu barevného gamutu.
[( )] K převodu textu na bitmapu.

---

**2. K čemu lze objekt přichytit?**

<!-- data-randomize="true" -->
[[X]] mřížce
[[X]] hraně jiného objektu
[[X]] středu
[[X]] průsečíku
[[X]] vodítku
[[ ]] pouze levému hornímu rohu dokumentu

---

**3. Kolika body je definována kubická Bézierova křivka?**

<!-- data-randomize="true" -->
[(X)] Čtyřmi.
[( )] Dvěma.
[( )] Třemi.
[( )] Pěti.

---

**4. Co dělají řídicí body Bézierovy křivky?**

<!-- data-randomize="true" -->
[(X)] Ovlivňují směr a zakřivení segmentu.
[( )] Vždy leží přímo na výsledné křivce.
[( )] Určují barvu výplně.
[( )] Rasterizují segment.

---

**5. Co je výhodou B-spline?**

<!-- data-randomize="true" -->
[(X)] Umožňuje lokální kontrolu hladkého tvaru pomocí více bodů.
[( )] Je vždy přesnější než každý Bézier.
[( )] Používá pouze dva body.
[( )] Je to rastrový filtr.

---

**6. Co znamená NURBS?**

<!-- data-randomize="true" -->
[(X)] Non-Uniform Rational B-Spline.
[( )] New Universal Raster Bitmap System.
[( )] Numeric Unified Rendering Base Shape.
[( )] Network User Resolution Base Scale.

---

**7. Které jsou boolean operace nad tvary?**

<!-- data-randomize="true" -->
[[X]] union
[[X]] intersection
[[X]] difference
[[X]] exclusive or
[[ ]] gamma

---

**8. Proč záleží na pořadí transformací?**

<!-- data-randomize="true" -->
[(X)] Složené transformace nemusí být komutativní.
[( )] Každá transformace dává vždy stejný výsledek.
[( )] Rotace a posun jsou jen grafické styly.
[( )] Pořadí ovlivňuje pouze barvu.

---

**9. Co může definovat stroke?**

<!-- data-randomize="true" -->
[[X]] barvu
[[X]] tloušťku
[[X]] typ čáry
[[X]] styl zakončení
[[X]] způsob spojení segmentů
[[ ]] textový obsah objektu

---

**10. Co se ztratí při převodu textu na křivky?**

<!-- data-randomize="true" -->
[(X)] Editovatelnost a sémantika skutečného textu.
[( )] Vektorová geometrie znaků.
[( )] Možnost zobrazit tvar bez fontu.
[( )] Obrys znaku.


# 2. Interaktivní shrnutí kapitoly

## Přesnost a snapping

Mřížky, vodítka a [[snapping]] umožňují přesně umisťovat objekty. Zarovnání a distribuce jsou spolehlivější než ruční posouvání „od oka“.

Vektorový editor tak pracuje s geometrickými [[vztahy]], ne jen s vizuálním dojmem.

## Bézierovy křivky

Kubická Bézierova křivka má počáteční bod, dva řídicí body a koncový bod, tedy celkem [[4]] body. Řídicí body ovlivňují směr a zakřivení.

Příliš mnoho uzlů často vede k nerovnostem. Kvalitní tvar se snaží používat [[ co nejhustší síť bodů bez ohledu na tvar | (co nejjednodušší geometrii odpovídající tvaru) | maximální počet uzlů ]].

## B-spline, NURBS a boolean operace

B-spline poskytuje lokální kontrolu nad křivkou. NURBS přidává racionální váhy a umí přesně reprezentovat některé geometrické tvary, například [[kružnice]].

**Vyber boolean operace:**

<!-- data-randomize="true" -->
[[X]] union
[[X]] intersection
[[X]] difference
[[X]] exclusive or
[[ ]] antialiasing

Boolean union vytváří skutečně spojenou geometrii, zatímco pouhé seskupení ponechá objekty [[samostatné]].

## Transformace a styl

Transformace zahrnují posun, rotaci, měřítko, zrcadlení a zkosení. Lze je zapisovat maticemi a [[skládat]]. Pořadí operací může měnit výsledek.

Stroke je obrys a fill [[výplň]]. Gradient vytváří plynulý přechod barev. Pořadí objektů určuje, co se vykreslí nad čím.

Text je vhodné ponechat jako skutečný text, pokud potřebujeme editaci nebo přístupnost. Převod na [[křivky]] je užitečný jen tehdy, když potřebujeme nezávislost na konkrétním fontu.
