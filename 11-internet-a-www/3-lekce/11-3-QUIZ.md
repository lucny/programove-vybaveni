<!--
title: World Wide Web a HTTP – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Internet existoval dříve než web, ale práce s informacemi byla složitější a roztříštěná.**

<!-- data-randomize="true" -->
[(X)] Vznik a princip World Wide Webu
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Prohlížeč neobsahuje všechny stránky internetu.**

<!-- data-randomize="true" -->
[(X)] HTTP komunikace: klient a server
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Při přihlášení nebo platbě putují mezi prohlížečem a serverem citlivé údaje.**

<!-- data-randomize="true" -->
[(X)] HTTP a HTTPS
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? HTTP je bezstavové, přesto e-shop udrží košík a škola pozná přihlášeného uživatele.**

<!-- data-randomize="true" -->
[(X)] Cookies, relace a webová úložiště
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**5. Které tvrzení odpovídá tématu Vznik a princip World Wide Webu?**

<!-- data-randomize="true" -->
[(X)] Internet existoval dříve než web, ale práce s informacemi byla složitější a roztříštěná.
[( )] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[( )] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.
[( )] Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta.

---

**6. Které tvrzení odpovídá tématu Cookies, relace a webová úložiště?**

<!-- data-randomize="true" -->
[(X)] HTTP je bezstavové, přesto e-shop udrží košík a škola pozná přihlášeného uživatele.
[( )] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[( )] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.
[( )] Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Vznik a princip World Wide Webu
[[X]] HTTP komunikace: klient a server
[[X]] HTTP a HTTPS
[[ ]] ARPANET: Zárodek dnešního internetu
[[ ]] Internet a intranet

---

**8. Které téma tvoří jednu z hlavních částí kapitoly World Wide Web a HTTP?**

<!-- data-randomize="true" -->
[(X)] HTTP a HTTPS
[( )] Internet věcí
[( )] Generativní AI a hledání informací
[( )] Internet, bezpečnost, soukromí a pravdivost

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Internet existoval dříve než web, ale práce s informacemi byla složitější a roztříštěná.
[[X]] Prohlížeč neobsahuje všechny stránky internetu.
[[ ]] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[[ ]] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Cookies, relace a webová úložiště
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

# 2. Interaktivní shrnutí kapitoly

## Web není celý internet

World Wide Web je systém vzájemně propojených zdrojů dostupných přes internet. Prohlížeč získává dokumenty a další data ze serverů a skládá je do stránky. Základ webu tvoří adresování pomocí URL, komunikace pomocí [[HTTP]] a dokumenty propojené hypertextovými odkazy.

## Požadavek a odpověď

HTTP pracuje v modelu klient–server. Klient odešle požadavek s metodou, cílem, hlavičkami a případně tělem; server vrátí odpověď se stavovým kódem, hlavičkami a obsahem.

Metoda GET typicky získává reprezentaci zdroje, zatímco POST předává data ke zpracování. Stavové kódy rozdělujeme do skupin: úspěch začíná číslicí [[2]], chyba klienta číslicí 4 a chyba serveru číslicí 5.

**Která spojení jsou správná?**

<!-- data-randomize="true" -->
[[X]] 200 — úspěšná odpověď
[[X]] 404 — požadovaný zdroj nebyl nalezen
[[X]] 500 — chyba na straně serveru
[[ ]] 301 — chyba hesla uživatele

## HTTPS chrání přenos

HTTPS je HTTP přenášené přes zabezpečené spojení. Šifrování omezuje možnost odposlechu a změny dat po cestě a certifikát pomáhá ověřit identitu serveru. Samotné HTTPS však [[ zaručuje pravdivost každého webu | (nepotvrzuje důvěryhodnost obsahu stránky) | nahrazuje autentizaci uživatele ]].

## Jak si web pamatuje stav

HTTP je ze své podstaty bezstavové. Server proto může relaci spojit s identifikátorem uloženým v [[cookie]]. Citlivý stav má zůstat na serveru; cookie často nese jen identifikátor relace.

Webová úložiště v prohlížeči slouží jinému účelu. localStorage uchovává data déle, sessionStorage je váže na relaci dané karty. Ani jedno se neposílá automaticky s každým HTTP požadavkem jako cookies.
