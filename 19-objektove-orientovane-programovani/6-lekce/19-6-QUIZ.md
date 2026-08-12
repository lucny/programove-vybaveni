<!--
title: Návrh objektového programu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co má objekt Vypujcka v příkladu knihovny spojovat?**

<!-- data-randomize="true" -->
[(X)] Konkrétní Knihu s konkrétním Čtenářem.
[( )] Pouze dvě textové kopie bez objektových vztahů.
[( )] Uživatelské rozhraní s databázovým serverem.
[( )] Dva zdrojové soubory bez instancí.

---

**2. Co je kompozice?**

<!-- data-randomize="true" -->
[(X)] Skládání objektu z dalších spolupracujících objektů.
[( )] Dědění každé součásti ze stejného rodiče.
[( )] Automatické vytváření kopií objektu.
[( )] Přetížení konstruktoru mnoha parametry.

---

**3. Který vztah odpovídá kompozici?**

<!-- data-randomize="true" -->
[(X)] Auto má Motor.
[( )] Pes je Zvíře.
[( )] Kočka je Savec.
[( )] Nákladní auto je Vozidlo.

---

**4. Jaká kontrolní otázka pomáhá rozlišit dědičnost a kompozici?**

<!-- data-randomize="true" -->
[(X)] Jde o vztah „je“, nebo „má“?
[( )] Je objekt uložen na stacku, nebo heapu?
[( )] Používá jazyk závorky, nebo odsazení?
[( )] Má metoda dva, nebo tři parametry?

---

**5. Co znamená jasná odpovědnost třídy?**

<!-- data-randomize="true" -->
[(X)] Třída řeší soudržný, srozumitelně vymezený úkol.
[( )] Třída obsahuje všechny funkce celé aplikace.
[( )] Každá metoda musí být v samostatné třídě.
[( )] Třída nesmí spolupracovat s jinými objekty.

---

**6. Proč je nevhodné, aby Student zároveň ukládal databázi, posílal e-mail a tvořil PDF?**

<!-- data-randomize="true" -->
[(X)] Míchá mnoho různých odpovědností a změny se vzájemně ovlivňují.
[( )] Objekt nesmí mít více než jeden atribut.
[( )] Python nepodporuje více metod ve třídě.
[( )] Každá činnost vyžaduje dědičnost.

---

**7. Která vrstva má v jednoduchém modelu řešit pravidla aplikace?**

<!-- data-randomize="true" -->
[(X)] Aplikační logika.
[( )] Uživatelské rozhraní.
[( )] Datové úložiště bez pravidel.
[( )] Operační systém.

---

**8. Které části rozlišuje MVC?**

<!-- data-randomize="true" -->
[[X]] Model
[[X]] View
[[X]] Controller
[[ ]] Compiler
[[ ]] Container

---

**9. Co je návrhový vzor?**

<!-- data-randomize="true" -->
[(X)] Osvědčený obecný způsob uspořádání spolupráce pro opakující se problém.
[( )] Hotová knihovna použitelná bez přizpůsobení.
[( )] Povinné pravidlo každého objektového programu.
[( )] Konkrétní syntaxe jediného jazyka.

---

**10. Jakou úlohu má vzor Observer?**

<!-- data-randomize="true" -->
[(X)] Upozornit přihlášené pozorovatele na změnu stavu.
[( )] Vytvářet objekty bez znalosti jejich typu.
[( )] Ukládat objekty přímo do databáze.
[( )] Zajistit, že existuje jen jeden objekt třídy.


# 2. Interaktivní shrnutí kapitoly

## Objekty spolupracují

Skutečná aplikace není sbírka izolovaných tříd. Ve školní knihovně objekt `Vypujcka` odkazuje na objekt [[Kniha]] a [[Ctenar]]. Vztah uchovává skutečné objekty, ne nutně kopie všech jejich textových údajů.

Návrh proto zkoumá nejen atributy a metody, ale také to, kdo s kým komunikuje a kdo nese odpovědnost za konkrétní pravidlo.

## „Je“ proti „má“

Dědičnost vyjadřuje specializaci: Pes [[je]] Zvíře. Kompozice skládá celek ze součástí: Auto [[má]] Motor. Model, v němž Auto dědí z Motoru, by zaměnil význam vztahu.

Kompozice dovoluje součást vyměnit, například benzinový motor za elektromotor, aniž by se auto muselo stát jiným druhem motoru. Dědičnost proto nemá být výchozí volbou pro každý vztah.

**Vyber přirozená přiřazení:**

<!-- data-randomize="true" -->
[[X]] Pes je Zvíře — dědičnost
[[X]] Počítač má Procesor — kompozice
[[X]] Výpůjčka spojuje Knihu a Čtenáře — spolupráce objektů
[[X]] Auto může dostat jiný Motor — výměna komponenty
[[ ]] Objednávka je Položka — přirozená specializace

## Jedna srozumitelná odpovědnost

Třída `Student` nemá zároveň ukládat databázi, posílat e-maily, tvořit PDF a počítat statistiky. Tyto úkoly lze rozdělit mezi `StudentRepository`, `EmailService` a generátor dokumentu. Dobrá kontrolní otázka zní: lze odpovědnost třídy popsat [[ jen výčtem mnoha nesouvisejících činností | (jednou krátkou větou) | pouze názvem programovacího jazyka ]]?

Rozdělení se nesmí změnit v opačný extrém jedné třídy na každou maličkost. Hledá se soudržný celek, který lze měnit a testovat s omezenými dopady.

## Vrstvy a MVC

Ve větší aplikaci se odděluje uživatelské rozhraní, aplikační logika a data. Tlačítko nemá obsahovat SQL dotazy a objekt knihy nemá rozhodovat o barvě tlačítka. V MVC představuje [[Model]] data a pravidla, View zobrazení a [[Controller]] zpracování požadavků a propojení částí.

## Vzory jsou slovník, ne povinnost

Návrhový vzor popisuje osvědčené uspořádání pro opakující se problém. [[Observer]] rozesílá změnu přihlášeným pozorovatelům, Factory odděluje vytváření objektů od jejich používání. Vzor není hotový kus kódu a má se [[ (přizpůsobit konkrétní situaci) | použít v každé třídě bez ohledu na problém | naučit pouze jako název ]]. Jednoduchý problém může mít lepší přímé řešení.
