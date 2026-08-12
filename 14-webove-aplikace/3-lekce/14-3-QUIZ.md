<!--
title: Šablony, formuláře a vstupní data – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Django Templates umožňují vložit data do HTML a používat jednoduché řídicí konstrukce.**

<!-- data-randomize="true" -->
[(X)] Šablona kombinuje strukturu a data, ne celou aplikační logiku
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Django Forms propojují HTML formulář se serverovou validací.**

<!-- data-randomize="true" -->
[(X)] Formulář: pohodlí pro uživatele, nedůvěra pro server
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Regulární výrazy — regular expressions, regex popisují vzory v textu.**

<!-- data-randomize="true" -->
[(X)] Regulární výraz je nástroj, ne univerzální validátor
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Webová aplikace pracuje se dvěma odlišnými skupinami souborů.**

<!-- data-randomize="true" -->
[(X)] Soubory, statická data a uživatelská média
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**5. Které tvrzení odpovídá tématu Šablona kombinuje strukturu a data, ne celou aplikační logiku?**

<!-- data-randomize="true" -->
[(X)] Django Templates umožňují vložit data do HTML a používat jednoduché řídicí konstrukce.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**6. Které tvrzení odpovídá tématu Soubory, statická data a uživatelská média?**

<!-- data-randomize="true" -->
[(X)] Webová aplikace pracuje se dvěma odlišnými skupinami souborů.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Šablona kombinuje strukturu a data, ne celou aplikační logiku
[[X]] Formulář: pohodlí pro uživatele, nedůvěra pro server
[[X]] Regulární výraz je nástroj, ne univerzální validátor
[[ ]] Od statické stránky k systému se stavem
[[ ]] MVC a příbuzné návrhové vzory

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Šablony, formuláře a vstupní data?**

<!-- data-randomize="true" -->
[(X)] Formulář: pohodlí pro uživatele, nedůvěra pro server
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Django Templates umožňují vložit data do HTML a používat jednoduché řídicí konstrukce.
[[X]] Django Forms propojují HTML formulář se serverovou validací.
[[ ]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[ ]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Soubory, statická data a uživatelská média
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

# 2. Interaktivní shrnutí kapitoly

## Šablona není místo pro všechnu logiku

Šablona propojuje strukturu stránky s připravenými daty. Podmínky a cykly mají sloužit hlavně prezentaci; obchodní pravidla a databázové dotazy patří do vhodnějších vrstev. Automatické escapování omezuje riziko, že se textová data změní na [[spustitelný]] HTML nebo JavaScript.

## Formulář a nedůvěryhodný vstup

Formulář usnadňuje zadání dat, ale server nesmí předpokládat, že požadavek vznikl právě v něm. Musí ověřit typ, rozsah, povinné hodnoty, vazby i oprávnění uživatele.

Django formulář může spojit převod vstupu, validaci a chybové zprávy. Úspěšná klientská kontrola [[ stačí jako bezpečnostní záruka | (nenahrazuje serverovou validaci) | automaticky autorizuje uživatele ]].

## Regulární výraz ve správné roli

Regulární výraz dobře kontroluje lokální textový vzor, například tvar identifikátoru. Neověří však, zda e-mailová schránka existuje, datum dává smysl v obchodním procesu nebo uživatel smí operaci provést.

**Co může vyžadovat víc než regulární výraz?**

<!-- data-randomize="true" -->
[[X]] ověření existence záznamu
[[X]] kontrola oprávnění
[[X]] porovnání hodnot více polí
[[ ]] rozpoznání pevného formátu krátkého kódu

## Statické soubory a média

Statické soubory jsou součástí aplikace, například CSS nebo ikony. Uživatelská média vznikají nahráním a musí se považovat za nedůvěryhodná data. Je potřeba omezit velikost a typ, bezpečně vytvořit název a ukládat je mimo místo, odkud by se mohly spouštět jako kód.

V produkci se statické soubory obvykle shromažďují a obsluhují jiným mechanismem než vývojový server. Cesta k médiím a jejich přístupová pravidla musí odpovídat citlivosti obsahu.
