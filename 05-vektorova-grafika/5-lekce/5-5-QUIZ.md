<!--
title: Rendering a animace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je rendering?**

<!-- data-randomize="true" -->
[(X)] Výpočet výsledného 2D obrazu z popisu 3D scény.
[( )] Pouze modelování polygonů.
[( )] Záznam pohybu herce.
[( )] Komprese textury.

---

**2. Co dělá rasterizační pipeline?**

<!-- data-randomize="true" -->
[(X)] Promítá a převádí geometrii na fragmenty a pixely.
[( )] Sleduje vždy všechny paprsky světla fyzikálně.
[( )] Používá jen CPU bez GPU.
[( )] Vytváří rig postavy.

---

**3. Které techniky se používají jako aproximace v rasterizačním renderingu?**

<!-- data-randomize="true" -->
[[X]] shadow maps
[[X]] reflection probes
[[X]] screen-space reflections
[[X]] baked lightmaps
[[ ]] výhradně path tracing

---

**4. Jak se v klasickém ray tracingu často vysílá primární paprsek?**

<!-- data-randomize="true" -->
[(X)] Z kamery do scény.
[( )] Vždy ze světla do všech směrů.
[( )] Z objektu do kamery bez průsečíků.
[( )] Pouze mezi dvěma pixely obrazovky.

---

**5. Co je path tracing?**

<!-- data-randomize="true" -->
[(X)] Monte Carlo metoda simulující transport světla pomocí náhodného vzorkování cest.
[( )] Algoritmus pro tvorbu skeletonu.
[( )] Formát 3D souboru.
[( )] Typ UV mapy.

---

**6. Co je global illumination?**

<!-- data-randomize="true" -->
[(X)] Obecný pojem pro techniky zahrnující nepřímé osvětlení.
[( )] Jeden konkrétní shader s pevnou implementací.
[( )] Pouze ambient occlusion.
[( )] Vždy synonymum rasterizace.

---

**7. Co odhaduje ambient occlusion?**

<!-- data-randomize="true" -->
[(X)] Míru geometrického zakrytí bodu vůči okolnímu světlu.
[( )] Rychlost animace.
[( )] Barevný gamut.
[( )] Velikost textury.

---

**8. Co je keyframe?**

<!-- data-randomize="true" -->
[(X)] Klíčový okamžik s ručně určenou hodnotou animované vlastnosti.
[( )] Každý jednotlivý renderovaný pixel.
[( )] Typ shaderu.
[( )] Síťový snímek dat.

---

**9. Co patří k animaci postavy?**

<!-- data-randomize="true" -->
[[X]] rigging
[[X]] bones
[[X]] skinning
[[X]] inverse kinematics
[[ ]] UV komprese jako hlavní animační princip

---

**10. Co je motion capture?**

<!-- data-randomize="true" -->
[(X)] Záznam pohybu reálného člověka nebo objektu do animačních dat.
[( )] Automatické generování textur.
[( )] Výpočet global illumination.
[( )] Typ particle shaderu.


# 2. Interaktivní shrnutí kapitoly

## Rendering

Rendering převádí popis 3D scény na výsledný [[obraz]]. Real-time aplikace musí renderovat desítky až stovky snímků za sekundu, film může věnovat jednomu snímku výrazně více času.

Rasterizace transformuje vrcholy, promítne geometrii a převádí trojúhelníky na fragmenty. Efekty jako odrazy nebo stíny často využívají [[aproximace]].

## Ray tracing a path tracing

Ray tracing sleduje paprsky a průsečíky se scénou. Primární paprsek se prakticky často vysílá z [[kamery]] do scény.

Path tracing je Monte Carlo metoda, která náhodně vzorkuje další cesty světla. S rostoucím počtem vzorků klesá [[šum]]. Denoising může obraz vyčistit s menším počtem vzorků.

Global illumination zahrnuje také [[nepřímé]] osvětlení. Path tracing je jednou z jeho metod.

## Ambient occlusion

AO odhaduje, jak moc je bod povrchu zakrytý okolní geometrií. Pomáhá zvýraznit kontaktní stíny, ale není úplnou fyzikální simulací [[světla]].

## Animace

Keyframe animace zadává hodnoty v klíčových časech a mezistavy vznikají [[interpolací]]. Animační křivky řídí zrychlení a časování.

**Vyber prvky riggingu postavy:**

<!-- data-randomize="true" -->
[[X]] bones
[[X]] skinning
[[X]] váhy vrcholů
[[X]] inverse kinematics
[[ ]] barevný profil ICC

Motion capture poskytuje pohybová data, která je často nutné čistit a přizpůsobit postavě. Particle system řídí velké množství jednoduchých [[částic]] podle pravidel.
