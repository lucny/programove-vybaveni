<!--
title: Bezpečnost webové aplikace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Bezpečnost nezačíná seznamem názvů útoků.**

<!-- data-randomize="true" -->
[(X)] Základní pravidlo: klientský vstup není důvěryhodný
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Cross-Site Scripting — XSS vzniká, když aplikace vloží nedůvěryhodná data do stránky tak, že je prohlížeč interpretuje jako aktivní obsah.**

<!-- data-randomize="true" -->
[(X)] XSS: když se data stanou kódem
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? SQL injection vzniká, když se nedůvěryhodný vstup stane součástí syntaxe databázového dotazu.**

<!-- data-randomize="true" -->
[(X)] SQL injection: dotaz není řetězec ke slepování
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Aplikace může mít správný kód a přesto být nebezpečná kvůli provozu.**

<!-- data-randomize="true" -->
[(X)] Bezpečnost konfigurace a závislostí
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**5. Které tvrzení odpovídá tématu Základní pravidlo: klientský vstup není důvěryhodný?**

<!-- data-randomize="true" -->
[(X)] Bezpečnost nezačíná seznamem názvů útoků.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**6. Které tvrzení odpovídá tématu Bezpečnost konfigurace a závislostí?**

<!-- data-randomize="true" -->
[(X)] Aplikace může mít správný kód a přesto být nebezpečná kvůli provozu.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Základní pravidlo: klientský vstup není důvěryhodný
[[X]] XSS: když se data stanou kódem
[[X]] SQL injection: dotaz není řetězec ke slepování
[[ ]] Od statické stránky k systému se stavem
[[ ]] MVC a příbuzné návrhové vzory

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Bezpečnost webové aplikace?**

<!-- data-randomize="true" -->
[(X)] SQL injection: dotaz není řetězec ke slepování
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Bezpečnost nezačíná seznamem názvů útoků.
[[X]] Cross-Site Scripting — XSS vzniká, když aplikace vloží nedůvěryhodná data do stránky tak, že je prohlížeč interpretuje jako aktivní obsah.
[[ ]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[ ]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Bezpečnost konfigurace a závislostí
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

# 2. Interaktivní shrnutí kapitoly

## Vstup z klienta není důvěryhodný

Útočník nemusí používat připravený formulář. Může změnit požadavek, identifikátor záznamu i hlavičky. Server proto musí ověřovat data, oprávnění a očekávaný stav operace nezávisle na klientském rozhraní.

Bezpečnostní kontrola má být na místě, které chrání skutečný zdroj. Pouhá validace v JavaScriptu [[ zastaví upravený síťový požadavek | (zlepšuje použitelnost, ale není bezpečnostní hranicí) | nahrazuje databázová omezení ]].

## Když se data změní na kód

XSS vzniká, když aplikace vloží nedůvěryhodná data do stránky tak, že je prohlížeč interpretuje jako kód. Obranou je kontextové escapování, bezpečná práce s DOM a omezení nebezpečných konstrukcí. Content Security Policy může doplnit ochranu, nikoli zakrýt chybný výstup.

SQL injection vzniká skládáním dotazu z textu uživatele. Hodnoty se mají předávat odděleně pomocí [[parametrizovaných]] dotazů nebo bezpečného ORM rozhraní.

## Požadavek může zneužít přihlášený prohlížeč

CSRF přiměje prohlížeč odeslat nežádoucí požadavek se stávajícími přihlašovacími údaji. Ochrana používá CSRF tokeny, vhodné cookies a správné rozlišení operací, které mění stav.

**Přiřaď obranu k riziku:**

<!-- data-randomize="true" -->
[[X]] XSS — escapování podle kontextu
[[X]] SQL injection — parametrizace dotazu
[[X]] CSRF — ověřovaný CSRF token
[[X]] broken access control — kontrola oprávnění u zdroje
[[ ]] všechny útoky — pouze skrytí tlačítka

## Oprávnění, konfigurace a závislosti

Broken access control nastává, když server neověří, zda uživatel smí pracovat s konkrétním objektem. Změna čísla v URL nesmí zpřístupnit cizí záznam.

Do produkce nepatří debug režim, výchozí tajné klíče ani zbytečně otevřené služby. Závislosti je nutné evidovat a aktualizovat, protože chyba v knihovně se stává součástí bezpečnostního profilu aplikace.
