<!--
title: IDE, editace a refaktorování kódu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co obvykle integruje IDE?**

<!-- data-randomize="true" -->
[(X)] Editor, překladač nebo běhové prostředí, debugger a další nástroje.
[( )] Pouze textový procesor a tabulkový kalkulátor.
[( )] Výhradně správu cloudového účtu.
[( )] Jen prohlížeč hotové dokumentace.

---

**2. Jaký přínos má integrace verzovacího systému v IDE?**

<!-- data-randomize="true" -->
[(X)] Umožňuje pracovat se změnami a synchronizovat je z jednoho prostředí.
[( )] Automaticky rozhoduje o správnosti algoritmu.
[( )] Nahrazuje repozitář i jeho historii.
[( )] Převádí větve na jednotkové testy.

---

**3. Co dělá automatické doplňování kódu?**

<!-- data-randomize="true" -->
[(X)] Navrhuje relevantní názvy a konstrukce při psaní.
[( )] Spouští aplikaci bez zdrojového kódu.
[( )] Maže všechny nepoužité soubory.
[( )] Nahrazuje návrh rozhraní aplikace.

---

**4. Co jsou snippets?**

<!-- data-randomize="true" -->
[(X)] Připravené šablony často používaných úseků kódu.
[( )] Záznamy chyb v produkčním systému.
[( )] Samostatné větve v Gitu.
[( )] Balíčky operačního systému.

---

**5. Jak pomáhá zvýrazňování syntaxe?**

<!-- data-randomize="true" -->
[(X)] Vizuálně odlišuje klíčová slova a strukturu kódu.
[( )] Mění význam příkazů programu.
[( )] Zvyšuje taktovací frekvenci procesoru.
[( )] Zajišťuje bezchybnou logiku.

---

**6. Co je linting?**

<!-- data-randomize="true" -->
[(X)] Statická analýza upozorňující na možné chyby a problematický styl.
[( )] Měření síťové propustnosti aplikace.
[( )] Ruční slučování binárních souborů.
[( )] Vytváření databázových záloh.

---

**7. Co znamená refaktorování?**

<!-- data-randomize="true" -->
[(X)] Změnu vnitřní struktury bez změny vnější funkcionality.
[( )] Přidání nové uživatelské funkce.
[( )] Překlad programu do jiného přirozeného jazyka.
[( )] Odstranění všech automatických testů.

---

**8. Které změny mohou být refaktorováním?**

<!-- data-randomize="true" -->
[[X]] odstranění duplicit
[[X]] zlepšení názvů
[[X]] rozdělení dlouhé funkce
[[X]] odstranění mrtvého kódu
[[ ]] změna požadovaného výsledku funkce
[[ ]] zrušení podporované funkce aplikace

---

**9. Proč je navigace v kódu užitečná?**

<!-- data-randomize="true" -->
[(X)] Umožňuje rychle přejít k definici funkcí, tříd a proměnných.
[( )] Zajišťuje automatické nasazení na produkci.
[( )] Určuje datové typy bez znalosti jazyka.
[( )] Nahrazuje souborový systém projektu.

---

**10. Jaký je hlavní cíl refaktorování?**

<!-- data-randomize="true" -->
[(X)] Zlepšit čitelnost, udržovatelnost nebo efektivitu při zachování chování.
[( )] Zvětšit počet řádků za každou cenu.
[( )] Skrýt chyby před testovacím systémem.
[( )] Převést zdrojový kód na dokumentaci.


# 2. Interaktivní shrnutí kapitoly

## Jedno prostředí, více nástrojů

Integrované vývojové prostředí neznamená pouze barevný editor. [[IDE]] propojuje psaní kódu s jeho sestavením či spuštěním, laděním, testy, správou balíčků a často také Gitem. Díky společnému kontextu může například přejít od chybové zprávy přímo k odpovídajícímu řádku.

Integrace [[ nenahrazuje znalost programu | (zkracuje cestu mezi souvisejícími vývojovými činnostmi) | zaručuje správnost každé změny ]]. Vývojář stále rozhoduje, co má kód dělat.

## Pomůcky při psaní

Automatické doplňování navrhuje názvy a konstrukce, [[snippets]] vkládají připravené šablony. Zvýraznění syntaxe zlepšuje orientaci a navigace umožňuje přejít k definici symbolu nebo najít jeho použití.

Linting analyzuje kód bez nutnosti procházet všechny větve programu za běhu. Nástroj jako [[ESLint]] může upozornit na podezřelý zápis či porušení pravidel projektu, ale jeho nález je třeba správně vyhodnotit.

**Které činnosti podporují čitelnost a orientaci v kódu?**

<!-- data-randomize="true" -->
[[X]] zvýrazňování syntaxe
[[X]] navigace mezi symboly
[[X]] smysluplné automatické doplňování
[[X]] linting podle pravidel projektu
[[ ]] náhodné přejmenování veřejných funkcí

## Refaktorování zachovává vnější chování

Při refaktorování se mění uspořádání kódu, nikoli jeho požadovaná funkcionalita. Může jít o odstranění duplicity, přesnější název, rozdělení dlouhé funkce nebo odstranění nepoužívané části. Pokud uživatel po změně dostává jiný výsledek, nejde pouze o [[refaktorování]].

Testy jsou při těchto úpravách důležitou pojistkou. Umožňují ověřit, že změna struktury zachovala chování. Optimalizace může být součástí úpravy, ale nemá bez důvodu obětovat srozumitelnost; cílem je [[ (lépe uspořádaný a udržitelný kód) | co nejkratší zápis za každou cenu | změna funkcí bez nové specifikace ]].
