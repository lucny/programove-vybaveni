<!--
title: Trojrozměrné modelování a digitální scéna – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co může obsahovat 3D scéna kromě geometrie?**

<!-- data-randomize="true" -->
[(X)] Materiály, světla, kamery, animace a simulace.
[( )] Pouze textové poznámky.
[( )] Výhradně polygonální síť bez dalších dat.
[( )] Jen jednu kameru a žádné materiály.

---

**2. Z čeho je tvořen polygonální mesh?**

<!-- data-randomize="true" -->
[[X]] vrcholy
[[X]] hrany
[[X]] plochy
[[ ]] povinně pouze kružnice
[[ ]] výhradně bitmapové pixely

---

**3. Proč grafické karty často pracují s trojúhelníky?**

<!-- data-randomize="true" -->
[(X)] Trojúhelník je vždy rovinný a dobře rasterizovatelný.
[( )] Trojúhelník má vždy nejméně dat.
[( )] GPU neumí jiné souřadnice.
[( )] Trojúhelníky nevyžadují vrcholy.

---

**4. Co je topologie mesh?**

<!-- data-randomize="true" -->
[(X)] Způsob propojení vrcholů a hran.
[( )] Barva materiálu.
[( )] Rozlišení textury.
[( )] Poloha kamery.

---

**5. Co dělá subdivision surface?**

<!-- data-randomize="true" -->
[(X)] Z hrubší sítě vytváří hladší povrch.
[( )] Převádí model na texturu.
[( )] Vždy snižuje počet polygonů.
[( )] Nahrazuje UV mapping.

---

**6. Co znamená retopology?**

<!-- data-randomize="true" -->
[(X)] Vytvoření vhodnější, obvykle jednodušší topologie podle detailního modelu.
[( )] Změnu barevného prostoru.
[( )] Přidání světla.
[( )] Převod materiálu na PBR.

---

**7. Co je UV mapping?**

<!-- data-randomize="true" -->
[(X)] Převod povrchu 3D modelu do 2D souřadnic pro textury.
[( )] Převod kamery do perspektivy.
[( )] Výpočet stínu.
[( )] Změna počtu snímků za sekundu.

---

**8. Které mapy může používat PBR materiál?**

<!-- data-randomize="true" -->
[[X]] base color
[[X]] roughness
[[X]] metallic
[[X]] normal
[[X]] displacement
[[ ]] baud

---

**9. Co je principem PBR?**

<!-- data-randomize="true" -->
[(X)] Konzistentní fyzikálně uvěřitelné chování materiálů ve světle.
[( )] Pouze realistická barva bez světla.
[( )] Vždy filmový path tracing.
[( )] Automatická tvorba geometrie.

---

**10. Jak se liší perspektivní a ortografická projekce?**

<!-- data-randomize="true" -->
[(X)] Perspektivní zmenšuje vzdálené objekty, ortografická zachovává měřítko.
[( )] Ortografická vždy rozostřuje pozadí.
[( )] Perspektivní nemá kameru.
[( )] Jde jen o dva názvy pro stejné zobrazení.


# 2. Interaktivní shrnutí kapitoly

## Scéna a polygonální síť

3D scéna obsahuje geometrii, materiály, textury, světla, kamery, animace a simulace. Samotný [[model]] je jen jedna její část.

Polygonální mesh tvoří vrcholy, [[hrany]] a plochy. GPU často pracuje s trojúhelníky, protože jsou vždy rovinné a jejich rasterizace je jednoznačná.

Topologie určuje, jak jsou prvky sítě propojeny. Pro animaci je důležitá zejména v místech [[deformace]], například kolem kloubů.

## Modelovací přístupy

NURBS se hodí pro hladké technické povrchy, subdivision vytváří hladký povrch z hrubší sítě a sculpting připomíná digitální [[sochařství]].

Retopology vytváří z detailního modelu vhodnější síť pro animaci nebo real-time použití.

## UV a textury

[[UV]] mapping rozkládá 3D povrch do 2D prostoru. Textury mohou obsahovat base color, roughness, metallic, normal nebo displacement.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] normal mapa mění dojem orientace povrchu bez stejné geometrické složitosti
[[X]] displacement může skutečně posouvat geometrii
[[X]] procedurální textura může vznikat matematicky
[[ ]] UV mapa určuje fyzickou ohniskovou vzdálenost kamery

## Materiály, kamera a světlo

PBR používá materiálový model, který se snaží být fyzikálně konzistentní. Roughness ovlivňuje ostrost [[odrazů]], metallic chování kovu a dielektrika.

Perspektivní kamera zmenšuje vzdálené objekty; ortografická zachovává měřítko. Scéna může používat point, spot, directional nebo area lights a HDRI [[environment]] pro okolní osvětlení.
