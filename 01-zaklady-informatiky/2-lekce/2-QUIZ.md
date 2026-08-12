<!--
title: 2. Principy digitalizace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je signál v souvislosti s informací?**

<!-- data-randomize="true" -->
[( )] Význam sdělení.
[(X)] Fyzický nositel informace.
[( )] Druh datového souboru.
[( )] Výsledek algoritmu.

---

**2. Které jevy mohou sloužit jako fyzická reprezentace informace?**

<!-- data-randomize="true" -->
[[X]] elektrické napětí
[[X]] světelný impuls
[[X]] rádiová vlna
[[X]] změna magnetizace
[[ ]] datový typ
[[ ]] algoritmus

---

**3. Co je typické pro digitální reprezentaci?**

<!-- data-randomize="true" -->
[( )] Pracuje jen s optickými signály.
[( )] Vždy přesně kopíruje spojitý jev.
[(X)] Používá diskrétní hodnoty.
[( )] Nevyužívá fyzické nosiče.

---

**4. Co určuje vzorkovací frekvence?**

<!-- data-randomize="true" -->
[( )] Počet bitů jednoho vzorku.
[( )] Počet amplitudových úrovní.
[(X)] Počet měření za sekundu.
[( )] Počet zvukových kanálů.

---

**5. Co může vzniknout při příliš pomalém vzorkování?**

<!-- data-randomize="true" -->
[( )] komprese
[( )] šifrování
[(X)] aliasing
[( )] hashování

---

**6. Která tvrzení o kvantování jsou správná?**

<!-- data-randomize="true" -->
[[X]] Převádí hodnotu na jednu z konečného počtu úrovní.
[[X]] Souvisí s bitovou hloubkou.
[[X]] Může způsobit kvantizační chybu.
[[ ]] Určuje časový odstup vzorků.
[[ ]] Zajišťuje bezeztrátovou kompresi.

---

**7. Kolik různých hodnot lze reprezentovat pomocí 8 bitů?**

<!-- data-randomize="true" -->
[( )] 64
[(X)] 256
[( )] 128
[( )] 512

---

**8. Jaký základní datový tok má stereo PCM 44,1 kHz / 16 bit?**

<!-- data-randomize="true" -->
[( )] 705 600 bit/s
[( )] 882 000 bit/s
[(X)] 1 411 200 bit/s
[( )] 2 822 400 bit/s

---

**9. Která tvrzení správně rozlišují bit a byte?**

<!-- data-randomize="true" -->
[[X]] Značka bitu je `b`.
[[X]] Značka bajtu je `B`.
[[X]] Jeden byte tvoří osm bitů.
[[ ]] Jeden bit tvoří osm bajtů.
[[ ]] Mbit/s a MB znamenají totéž.

---

**10. Která dvojice jednotek používá binární předpony?**

<!-- data-randomize="true" -->
[( )] kB a MB
[( )] MB a GB
[(X)] MiB a GiB
[( )] kbit a Mbit


# 2. Interaktivní shrnutí kapitoly

## Informace a její fyzická podoba

Aby bylo možné informaci uložit, přenést nebo automaticky zpracovat, musí mít nějakou fyzickou reprezentaci. Tou je [[signál]]. Může jít například o elektrické napětí, světelný impuls, rádiovou vlnu nebo změnu magnetizace.

Je důležité rozlišovat informaci a signál. Informace představuje [[ fyzickou velikost | (význam, který interpretujeme) | pouze binární číslo ]], zatímco signál je její fyzický nositel. Stejná informace proto může během přenosu několikrát změnit fyzickou podobu.

Digitální technika stále pracuje s reálnými fyzikálními jevy, ale určité rozsahy hodnot interpretuje jako [[ spojité nekonečné hodnoty | (diskrétní logické stavy) | náhodné odchylky ]].

## Analogový a digitální svět

Analogový signál se mění [[ po přesně určených krocích | (spojitě) | pouze mezi nulou a jedničkou ]]. Digitální reprezentace naproti tomu používá diskrétní hodnoty. Její významnou výhodou je, že správně přečtená digitální data lze kopírovat [[bitově]] přesně.

To ale neznamená, že převod spojitého jevu do digitální podoby je bez omezení. Při digitalizaci musíme určit, **kdy** měříme a **s jakou přesností** hodnoty ukládáme. Tyto dvě operace se nazývají [[vzorkování]] a [[kvantování]].

## Vzorkování a kvantování

Vzorkování znamená, že v pravidelných okamžicích změříme hodnotu signálu. Počet měření za sekundu je [[ vzorkovací hloubka | (vzorkovací frekvence) | datová komprese ]] a udává se v hertzech.

Při 44,1 kHz vznikne za jednu sekundu [[44100]] vzorků. Při příliš nízké vzorkovací frekvenci může vzniknout jev nazývaný [[aliasing]].

Kvantování řeší jinou otázku: [[ kdy hodnotu změříme | (s jakou přesností ji uložíme) | kudy ji přeneseme ]]. Možný rozsah rozdělí na konečný počet úrovní. Počet těchto úrovní souvisí s bitovou hloubkou. Pro `n` bitů existuje `2^n` různých kombinací.

**Vyber správná spojení:**

<!-- data-randomize="true" -->
[[X]] 2 bity — 4 hodnoty
[[X]] 4 bity — 16 hodnot
[[X]] 8 bitů — 256 hodnot
[[X]] 16 bitů — 65 536 hodnot
[[ ]] 8 bitů — 128 hodnot
[[ ]] 16 bitů — 16 384 hodnot

Rozdíl mezi skutečnou analogovou hodnotou a nejbližší dostupnou úrovní se označuje jako kvantizační [[chyba]].

## Bit, byte a množství dat

Základní jednotkou digitální informace je [[bit]]. Osm bitů tvoří jeden [[byte]]. Značky `b` a `B` proto nelze zaměňovat: síťová rychlost se běžně udává v Mbit/s, zatímco velikost souboru v MB.

U jednotek velikosti je vhodné rozlišovat desítkové a binární předpony. `1 MB` znamená [[ 1 048 576 B | (1 000 000 B) | 1 024 B ]], zatímco `1 MiB` znamená [[1048576]] bajtů.

Datový tok nekomprimovaného zvuku lze vypočítat jako:

**vzorkovací frekvence × bitová hloubka × počet [[kanálů]]**

Hlavní myšlenka kapitoly: digitalizace převádí fyzikální jev na posloupnost diskrétních čísel; vzorkování určuje **kdy** měříme, kvantování **jak přesně** hodnotu uložíme.
