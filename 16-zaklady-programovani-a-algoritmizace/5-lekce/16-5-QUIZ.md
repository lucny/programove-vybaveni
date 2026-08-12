<!--
title: Syntaxe, zdrojový kód a ladění – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co určuje syntaxe programovacího jazyka?**

<!-- data-randomize="true" -->
[(X)] Pravidla správného zápisu programu.
[( )] Výhradně význam požadavků uživatele.
[( )] Rychlost konkrétního procesoru.
[( )] Strukturu souborového systému.

---

**2. Kdo obvykle odhalí porušení syntaxe?**

<!-- data-randomize="true" -->
[(X)] Překladač nebo interpret.
[( )] Pouze koncový uživatel.
[( )] Síťový směrovač.
[( )] Databázový server bez spuštění kódu.

---

**3. Jakou úlohu mají komentáře?**

<!-- data-randomize="true" -->
[(X)] Vysvětlují kód, aniž by ovlivňovaly jeho běh.
[( )] Nahrazují všechny příkazy programu.
[( )] Mění hodnoty proměnných při spuštění.
[( )] Překládají program do bytecode.

---

**4. Jak se v C a Pythonu liší deklarace proměnné?**

<!-- data-randomize="true" -->
[(X)] C uvádí datový typ, Python jej při přiřazení odvodí.
[( )] Python vždy vyžaduje typ a C jej zakazuje.
[( )] V obou jazycích se proměnné zapisují binárně.
[( )] C používá pouze odsazení, Python závorky.

---

**5. Jak se typicky vymezují bloky kódu v Pythonu a C?**

<!-- data-randomize="true" -->
[(X)] Python odsazením, C složenými závorkami.
[( )] Python středníkem, C pouze komentářem.
[( )] Python hranatými závorkami, C odsazením.
[( )] V obou jazycích pouze prázdným řádkem.

---

**6. Co je syntaktická chyba?**

<!-- data-randomize="true" -->
[(X)] Zápis porušující pravidla jazyka.
[( )] Správně zapsaný kód s chybnou logikou.
[( )] Porucha pevného disku při ukládání.
[( )] Pomalý, ale správný algoritmus.

---

**7. Co je sémantická chyba v kontextu kapitoly?**

<!-- data-randomize="true" -->
[(X)] Program běží, ale kvůli chybné logice dává jiný výsledek.
[( )] Chybějící středník zachycený překladačem.
[( )] Dělení nulou vzniklé až při vykonání.
[( )] Komentář s překlepem bez vlivu na program.

---

**8. Která situace je typickou běhovou chybou?**

<!-- data-randomize="true" -->
[(X)] Dělení nulou při vykonávání programu.
[( )] Chybně odsazený blok odmítnutý před spuštěním.
[( )] Nevhodně pojmenovaná, ale funkční proměnná.
[( )] Příliš dlouhý komentář.

---

**9. Které nástroje nebo postupy pomáhají při ladění?**

<!-- data-randomize="true" -->
[[X]] debugger
[[X]] logování
[[X]] jednotkové testy
[[X]] code review
[[ ]] odstranění všech chybových zpráv
[[ ]] náhodné přepisování kódu

---

**10. Co umožňuje debugger?**

<!-- data-randomize="true" -->
[(X)] Krokovat kód a sledovat hodnoty proměnných.
[( )] Automaticky dokázat správnost každého algoritmu.
[( )] Převést Python na vývojový diagram bez kontroly.
[( )] Nahradit dokumentaci programovacího jazyka.


# 2. Interaktivní shrnutí kapitoly

## Pravidla konkrétního jazyka

Algoritmus popisuje myšlenku řešení, ale zdrojový kód ji musí vyjádřit podle pravidel zvoleného jazyka. Tato pravidla tvoří [[syntaxi]]. Překladač nebo interpret dokáže porušení často lokalizovat a doplnit chybovou zprávu.

Komentář je určen čtenáři a běh programu nemění. Dokumentace jazyka je důležitá, protože přesný význam konstrukcí nelze bezpečně odvozovat jen podle podobnosti s jiným jazykem.

## Jeden algoritmus, jiný zápis

V C se při deklaraci zapisuje typ, například `int x = 5;`, zatímco Python hodnotu přiřadí jako `x = 5` a typ odvodí. Blok v Pythonu vymezuje [[odsazení]], v C [[složené závorky]]. Rozdílný zápis nemění podstatu algoritmu, ale chybná syntaxe zabrání jeho správnému zpracování.

Převod algoritmu do kódu proto vyžaduje současně pochopit logiku řešení i vyjadřovací prostředky jazyka. Pouhé doslovné přepsání pseudokódu [[ vždy vytvoří spustitelný program | (nemusí respektovat syntaxi a chování cílového jazyka) | odstraní potřebu testování ]].

## Tři různé druhy chyb

Syntaktická chyba porušuje zápis, například chybějící středník či vadné odsazení. Sémantická chyba znamená chybnou logiku: program může běžet, ale počítá něco jiného. [[Běhová]] chyba se objeví až při vykonávání, například při dělení nulou nebo neplatném indexu.

**Vyber vhodné způsoby hledání chyb:**

<!-- data-randomize="true" -->
[[X]] krokovat program debuggerem
[[X]] sledovat hodnoty pomocí logování
[[X]] ověřovat části programu jednotkovými testy
[[X]] nechat změnu zkontrolovat při code review
[[ ]] ignorovat chybové zprávy a měnit kód náhodně

## Ladění jako řízené zkoumání

Debugger dovoluje zastavit program, postupovat instrukci po instrukci a pozorovat proměnné. [[Logování]] zachycuje průběh i tam, kde interaktivní krokování není praktické. Testy opakovatelně porovnávají chování s očekáváním a code review přináší pohled dalšího vývojáře.

Úspěšné spuštění tedy není jediným kritériem. Program musí mít správnou syntaxi, odpovídat zamýšlené logice a zvládat situace, které mohou nastat až za běhu.
