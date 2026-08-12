<!--
title: Webová API a komunikace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? API — Application Programming Interface je rozhraní, přes které jeden program využívá funkce nebo data jiného programu.**

<!-- data-randomize="true" -->
[(X)] Webová API
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Původní web fungoval převážně tak, že každá důležitá akce načetla nový HTML dokument.**

<!-- data-randomize="true" -->
[(X)] AJAX a Fetch API
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? REST — Representational State Transfer je architektonický styl pro síťové aplikace.**

<!-- data-randomize="true" -->
[(X)] REST API
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Běžná komunikace přes HTTP je založena na modelu požadavek → odpověď.**

<!-- data-randomize="true" -->
[(X)] WebSocket a Socket.IO
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu Webová API?**

<!-- data-randomize="true" -->
[(X)] API — Application Programming Interface je rozhraní, přes které jeden program využívá funkce nebo data jiného programu.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**6. Které tvrzení odpovídá tématu WebSocket a Socket.IO?**

<!-- data-randomize="true" -->
[(X)] Běžná komunikace přes HTTP je založena na modelu požadavek → odpověď.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Webová API
[[X]] AJAX a Fetch API
[[X]] REST API
[[ ]] Klient a server
[[ ]] Frontend a backend

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Webová API a komunikace?**

<!-- data-randomize="true" -->
[(X)] REST API
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] API — Application Programming Interface je rozhraní, přes které jeden program využívá funkce nebo data jiného programu.
[[X]] Původní web fungoval převážně tak, že každá důležitá akce načetla nový HTML dokument.
[[ ]] Web je založen na komunikaci mezi programy.
[[ ]] Pojmy frontend a backend popisují dvě různé části webové aplikace.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] WebSocket a Socket.IO
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## API jako rozhraní

Webové API zpřístupňuje data nebo operace pomocí dohodnutých požadavků a odpovědí. Klient nemusí znát vnitřní implementaci serveru; potřebuje znát adresy, metody, formát dat a význam chyb.

Fetch API umožňuje odeslat HTTP požadavek bez načtení celé stránky. Vrácený Promise nejprve reprezentuje HTTP odpověď; data JSON je potřeba následně [[ znovu odeslat serveru | (asynchronně načíst z těla odpovědi) | převést na HTML tabulku ]].

## REST

REST orientuje rozhraní na zdroje a používá význam HTTP metod. GET čte, POST typicky vytváří, PUT nebo PATCH mění a DELETE odstraňuje. Stavové kódy mají odpovídat výsledku operace.

Dobrá URL pojmenovává zdroj, nikoli každý krok procedury. Bezstavovost znamená, že server má mít v každém požadavku informace potřebné k jeho zpracování.

**Které vlastnosti podporují srozumitelné REST API?**

<!-- data-randomize="true" -->
[[X]] konzistentní názvy zdrojů
[[X]] smysluplné HTTP metody
[[X]] odpovídající stavové kódy
[[ ]] vracení stavu 200 pro každou chybu

## GraphQL

GraphQL dovoluje klientovi popsat strukturu požadovaných dat. Může omezit přenos nepotřebných polí, ale přesouvá část složitosti do schématu, resolverů, autorizace a řízení náročnosti dotazů. Není automatickou náhradou RESTu pro každý projekt.

## Komunikace v reálném čase

WebSocket udržuje obousměrné spojení, v němž může server poslat zprávu bez nového HTTP dotazu klienta. Hodí se pro chat, živé přehledy nebo spolupráci. Socket.IO přidává nad základní komunikaci další mechanismy a [[ není totožné se samotným protokolem WebSocket | funguje pouze bez sítě | ukládá data do relační databáze ]].

Volba mezi REST, GraphQL a trvalým spojením závisí na charakteru dat a komunikace, ne na tom, který název působí moderněji.
