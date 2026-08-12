<!--
title: Stav, autentizace a autorizace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Každý HTTP požadavek je samostatná zpráva.**

<!-- data-randomize="true" -->
[(X)] HTTP si uživatele samo nepamatuje
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Autentizace ověřuje identitu.**

<!-- data-randomize="true" -->
[(X)] Autentizace odpovídá „kdo jsi?“, autorizace „co smíš?“
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Heslo se na serveru nemá ukládat v čitelné podobě.**

<!-- data-randomize="true" -->
[(X)] Hesla, vícefaktorové ověřování a passkeys
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Heslo se na serveru nemá ukládat v čitelné podobě.**

<!-- data-randomize="true" -->
[(X)] Hesla, vícefaktorové ověřování a passkeys
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**5. Které tvrzení odpovídá tématu HTTP si uživatele samo nepamatuje?**

<!-- data-randomize="true" -->
[(X)] Každý HTTP požadavek je samostatná zpráva.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**6. Které tvrzení odpovídá tématu Hesla, vícefaktorové ověřování a passkeys?**

<!-- data-randomize="true" -->
[(X)] Heslo se na serveru nemá ukládat v čitelné podobě.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] HTTP si uživatele samo nepamatuje
[[X]] Autentizace odpovídá „kdo jsi?“, autorizace „co smíš?“
[[X]] Hesla, vícefaktorové ověřování a passkeys
[[ ]] Od statické stránky k systému se stavem
[[ ]] MVC a příbuzné návrhové vzory

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Stav, autentizace a autorizace?**

<!-- data-randomize="true" -->
[(X)] Autentizace odpovídá „kdo jsi?“, autorizace „co smíš?“
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Každý HTTP požadavek je samostatná zpráva.
[[X]] Autentizace ověřuje identitu.
[[ ]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[ ]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Hesla, vícefaktorové ověřování a passkeys
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

# 2. Interaktivní shrnutí kapitoly

## HTTP si identitu nepamatuje

Jednotlivé HTTP požadavky jsou samostatné. Aplikace proto používá relaci: prohlížeč obvykle uchovává identifikátor v cookie a server k němu přiřadí stav. Citlivé údaje nemají být bez potřeby uloženy přímo v klientské cookie.

Cookie relace má používat vhodné atributy, například HttpOnly, Secure a SameSite. Ty omezují některé způsoby zneužití, ale nenahrazují celkový bezpečnostní návrh.

## Autentizace a autorizace

Autentizace odpovídá na otázku [[kdo]] je uživatel. Autorizace rozhoduje, co smí provést s konkrétním zdrojem. Přihlášený uživatel proto nemusí mít oprávnění číst nebo měnit každý záznam.

Kontrola oprávnění musí proběhnout na serveru u každé chráněné operace. Skrytí odkazu v rozhraní je pouze úprava prezentace.

**Která tvrzení jsou správná?**

<!-- data-randomize="true" -->
[[X]] Autentizace ověřuje identitu.
[[X]] Autorizace se vztahuje ke konkrétní akci nebo zdroji.
[[X]] Relace propojuje více požadavků se stavem uživatele.
[[ ]] Přihlášení automaticky povoluje všechny operace.

## Hesla a další faktory

Server nemá ukládat heslo v otevřeném tvaru. Ukládá výsledek pomalé heslové hashovací funkce se solí. Při přihlášení zpracuje zadané heslo stejným postupem a porovná výsledek.

Vícefaktorové ověřování kombinuje nezávislé faktory. Passkeys používají kryptografický pár klíčů a jsou odolnější vůči phishingu než opakovaně zadávané heslo, protože soukromý klíč [[ neopouští zařízení uživatele | posílá se serveru při každém přihlášení | nahrazuje veškerou autorizaci aplikace ]].
