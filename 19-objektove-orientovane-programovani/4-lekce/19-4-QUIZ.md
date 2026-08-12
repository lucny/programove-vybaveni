<!--
title: Objekty a správa paměti – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co se děje při vytvoření objektu?**

<!-- data-randomize="true" -->
[(X)] Přidělí se paměť, konstruktor inicializuje stav a vznikne reference či ukazatel.
[( )] Objekt se vždy ihned uloží na disk.
[( )] Všechny atributy se stanou globálními.
[( )] Překladač odstraní definici třídy.

---

**2. Jak se v C++ liší objekt na stacku a heapu?**

<!-- data-randomize="true" -->
[(X)] Stackový zaniká s oborem, heapový vytvořený new vyžaduje řízené uvolnění.
[( )] Heapový zaniká vždy dříve než stackový.
[( )] Stackový lze vytvořit pouze v Pythonu.
[( )] Mezi nimi není rozdíl v životnosti.

---

**3. Co musí následovat po new u ručně spravovaného objektu v C++?**

<!-- data-randomize="true" -->
[(X)] Odpovídající delete, když objekt už není potřeba.
[( )] Povinný import garbage collectoru.
[( )] Převod objektu na hodnotový typ.
[( )] Uložení objektu do globální proměnné.

---

**4. Co vznikne při hodnotovém přiřazení objektu v C++?**

<!-- data-randomize="true" -->
[(X)] Kopie obsahu objektu.
[( )] Druhý ukazatel na tutéž instanci za všech okolností.
[( )] Automaticky odvozená třída.
[( )] Objekt bez atributů.

---

**5. Co vznikne při zkopírování reference v Pythonu?**

<!-- data-randomize="true" -->
[(X)] Dvě proměnné odkazují na tentýž objekt.
[( )] Vždy hluboká nezávislá kopie.
[( )] Nová třída bez konstruktoru.
[( )] Objekt se přesune na stack.

---

**6. Co je memory leak?**

<!-- data-randomize="true" -->
[(X)] Paměť zůstane obsazená, protože nebyla správně uvolněna.
[( )] Objekt se zkopíruje hodnotou.
[( )] Garbage collector odstraní používaný objekt.
[( )] Stack se automaticky vyprázdní po bloku.

---

**7. K čemu slouží inteligentní ukazatel v moderním C++?**

<!-- data-randomize="true" -->
[(X)] Váže životnost dynamického objektu na spravující objekt a automatizuje uvolnění.
[( )] Zvyšuje počet ručních delete.
[( )] Převádí C++ objekt na Python.
[( )] Ukládá objekt trvale do souboru.

---

**8. Co dělá garbage collector?**

<!-- data-randomize="true" -->
[(X)] Vyhledává objekty, které už nejsou používány, a uvolňuje jejich paměť.
[( )] Inicializuje každý objekt při vytvoření.
[( )] Zajišťuje správnost hodnot atributů.
[( )] Překládá třídy do strojového kódu.

---

**9. Která tvrzení o Pythonu odpovídají kapitole?**

<!-- data-randomize="true" -->
[[X]] Proměnné odkazují na objekty na haldě.
[[X]] Paměť je spravována automaticky.
[[X]] Při přiřazení se běžně kopíruje reference.
[[ ]] Programátor musí každý objekt rušit pomocí delete.
[[ ]] Objekty vždy vznikají na stacku.

---

**10. Proč nelze v Pythonu spoléhat na přesný okamžik __del__?**

<!-- data-randomize="true" -->
[(X)] Jeho volání závisí na automatické správě paměti a implementaci.
[( )] Metoda __del__ se nikdy nesmí definovat.
[( )] Python nemá objekty ani reference.
[( )] Destruktor se volá pouze při překladu.


# 2. Interaktivní shrnutí kapitoly

## Vznik objektu má tři části

Při instancování se přidělí paměť, [[konstruktor]] nastaví počáteční stav a program získá hodnotu, referenci nebo ukazatel, přes který s objektem pracuje. Životnost objektu závisí na jazyce i místě vytvoření.

V C++ může lokální objekt vzniknout na [[stacku]] a automaticky zanikne na konci oboru. Objekt vytvořený `new` leží na heapu a při ruční správě musí být uvolněn pomocí [[delete]].

## Kopie nebo další cesta ke stejnému objektu

Hodnotové přiřazení v C++ může vytvořit samostatnou kopii. Změna kopie pak původní objekt neovlivní. Ukazatele či reference mohou naopak mířit na stejnou instanci, takže změna přes jeden odkaz je viditelná přes druhý.

Pythonové proměnné běžně obsahují reference. Po `osoba2 = osoba1` [[ (obě jména ukazují na tentýž objekt) | vznikne vždy nezávislá hluboká kopie | původní objekt okamžitě zanikne ]]. Chceme-li kopii, musíme ji vytvořit vědomě odpovídajícím postupem.

**Vyber správná tvrzení o životnosti objektů:**

<!-- data-randomize="true" -->
[[X]] C++ objekt na stacku obvykle zanikne s oborem platnosti
[[X]] neuvolněný objekt na heapu může způsobit memory leak
[[X]] inteligentní ukazatel automatizuje správu vlastnictví
[[X]] Python používá automatickou správu paměti
[[ ]] přiřazení reference vždy vytváří novou nezávislou instanci

## Ruční a automatická správa

Zapomenuté `delete` ponechá dynamickou paměť obsazenou a vznikne [[memory leak]]. Moderní C++ proto používá inteligentní ukazatele, například `unique_ptr`, které svážou uvolnění s životností správce.

Python využívá [[garbage collector]] a další mechanismy běhového prostředí. Jakmile objekt není potřebný, paměť lze uvolnit bez příkazu `delete`. Pohodlí ale neznamená, že vývojář nemusí rozumět referencím nebo držení prostředků.

## Destruktor a prostředky

Destruktor se v C++ volá při zániku objektu a může uvolnit paměť, soubor či jiný prostředek. U Pythonu není přesný okamžik `__del__` zaručen, protože závisí na správě objektů. Pro důležité prostředky proto není rozumné spoléhat jen na [[ (neurčitý okamžik garbage collectoru) | konstruktor rodičovské třídy | hodnotovou kopii objektu ]].
