<!--
title: Ladění, testování a TDD – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je breakpoint?**

<!-- data-randomize="true" -->
[(X)] Místo, na němž debugger pozastaví běh programu.
[( )] Test, který vždy musí selhat.
[( )] Bod sloučení dvou větví Gitu.
[( )] Soubor se seznamem závislostí.

---

**2. K čemu slouží krokování v debuggeru?**

<!-- data-randomize="true" -->
[(X)] Ke sledování vykonávání programu po jednotlivých krocích.
[( )] K automatickému psaní dokumentace.
[( )] K přepínání verzí knihoven.
[( )] K nasazování kontejnerů.

---

**3. Jak pomáhá logování?**

<!-- data-randomize="true" -->
[(X)] Zaznamenává informace o průběhu a stavu programu.
[( )] Mění zdrojový kód při každém běhu.
[( )] Zajišťuje, že výjimka nikdy nevznikne.
[( )] Nahrazuje všechny testovací scénáře.

---

**4. Co ověřuje assertion v testu?**

<!-- data-randomize="true" -->
[(X)] Zda skutečný výsledek odpovídá očekávanému.
[( )] Zda je soubor uložen v repozitáři.
[( )] Zda IDE používá tmavý motiv.
[( )] Zda program obsahuje komentář.

---

**5. Co je předmětem unit testu?**

<!-- data-randomize="true" -->
[(X)] Jednotlivá funkce, metoda nebo třída v izolaci.
[( )] Celé uživatelské rozhraní v produkci.
[( )] Pouze rychlost síťového připojení.
[( )] Historie všech commitů projektu.

---

**6. Co ověřuje integrační test?**

<!-- data-randomize="true" -->
[(X)] Spolupráci více částí aplikace.
[( )] Pravopis názvů proměnných.
[( )] Samostatnou funkci bez závislostí.
[( )] Pouze vzhled dokumentace.

---

**7. Co ověřuje funkční test?**

<!-- data-randomize="true" -->
[(X)] Chování aplikace z pohledu uživatele.
[( )] Vnitřní implementaci jediné pomocné funkce.
[( )] Správu verzí nainstalovaných balíčků.
[( )] Vytvoření virtuálního prostředí.

---

**8. Které činnosti patří k testování popsanému v kapitole?**

<!-- data-randomize="true" -->
[[X]] jednotkové testy
[[X]] integrační testy
[[X]] funkční testy
[[X]] výkonové testy
[[ ]] náhodné mazání kódu
[[ ]] ignorování očekávaných výsledků

---

**9. Jak začíná cyklus TDD?**

<!-- data-randomize="true" -->
[(X)] Nejprve se napíše test očekávaného chování.
[( )] Nejprve se odstraní všechny staré testy.
[( )] Nejprve se aplikace nasadí do produkce.
[( )] Nejprve se vytvoří uživatelská dokumentace.

---

**10. Proč TDD usnadňuje refaktorování?**

<!-- data-randomize="true" -->
[(X)] Existující testy pomáhají hlídat zachování chování.
[( )] Zakazuje měnit vnitřní strukturu kódu.
[( )] Automaticky vytvoří nejrychlejší algoritmus.
[( )] Nahrazuje potřebu spouštět program.


# 2. Interaktivní shrnutí kapitoly

## Ladění hledá příčinu

Debugger umožňuje zastavit běh na [[breakpointu]], krokovat příkazy a pozorovat hodnoty proměnných. Vývojář tak nehádá jen podle výsledku, ale sleduje skutečnou cestu programu. Chybová hlášení a výjimky navíc ukazují typ a místo problému.

[[Logování]] je užitečné tam, kde nelze program pohodlně zastavit. Záznam průběhu může zachytit vstup, důležité rozhodnutí i vznik chyby, musí však poskytovat relevantní informace a nezahltit výstup.

## Test je opakovatelné očekávání

Unit test izolovaně ověřuje malou část programu. Assertion porovná skutečný výsledek s [[očekávaným]]. Integrační test se zaměřuje na spolupráci částí, funkční test na chování celé funkce aplikace z pohledu uživatele a výkonový test na rychlost či efektivitu.

**Vyber správná přiřazení:**

<!-- data-randomize="true" -->
[[X]] unit test — samostatná funkce nebo třída
[[X]] integrační test — komunikace aplikace s databází
[[X]] funkční test — uživatelský scénář v rozhraní
[[X]] výkonový test — chování při různém zatížení
[[ ]] assertion — náhodná změna očekávané hodnoty

Automatizace je důležitá, protože stejné ověření lze spustit po každé změně. Selhání testu však neříká automaticky, zda je chybný program, test nebo původní předpoklad; výsledek je nutné [[ (interpretovat podle požadovaného chování) | vždy obejít odstraněním assertion | považovat za chybu testovacího nástroje ]].

## TDD mění pořadí práce

Vývoj řízený testy začíná testem, který popisuje očekávané chování. Poté vznikne nejmenší implementace, která jej splní, a kód lze upravit do lepší struktury. Zjednodušeně jde o osu [[ (test → implementace → refaktorování) | implementace → produkce → odstranění testu | dokumentace → nasazení → návrh ]].

Testy tak fungují jako bezpečnostní síť při dalších změnách. TDD ale neznamená, že není potřeba ladění, integrační ověření nebo úsudek vývojáře; zaměřuje vývoj na předem formulované a kontrolovatelné chování.
