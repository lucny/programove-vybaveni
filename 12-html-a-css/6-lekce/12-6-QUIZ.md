<!--
title: Od zdrojového souboru k publikovanému webu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Jednoduchý web může mít jen několik souborů, ale i u něj se vyplatí přehledná struktura: text projekt/ ├── index.html ├── kontakt.html ├── styles/ │ └── main.css ├── images/ │ ├──…**

<!-- data-randomize="true" -->
[(X)] Projekt je víc než `index.html`
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Nástroje pro vývojáře v prohlížeči umožňují prohlížet DOM, měnit CSS za běhu, sledovat box model, simulovat rozměry zařízení a zjišťovat, který styl skutečně vyhrál v kaskádě.**

<!-- data-randomize="true" -->
[(X)] DevTools: laboratoř přímo v prohlížeči
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Při tvorbě nové stránky je výhodné nezačínat barvami.**

<!-- data-randomize="true" -->
[(X)] Praktický pracovní postup
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Při tvorbě nové stránky je výhodné nezačínat barvami.**

<!-- data-randomize="true" -->
[(X)] Praktický pracovní postup
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**5. Které tvrzení odpovídá tématu Projekt je víc než `index.html`?**

<!-- data-randomize="true" -->
[(X)] Jednoduchý web může mít jen několik souborů, ale i u něj se vyplatí přehledná struktura: text projekt/ ├── index.html ├── kontakt.html ├── styles/ │ └── main.css ├── images/ │ ├──…
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**6. Které tvrzení odpovídá tématu Praktický pracovní postup?**

<!-- data-randomize="true" -->
[(X)] Při tvorbě nové stránky je výhodné nezačínat barvami.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Projekt je víc než `index.html`
[[X]] DevTools: laboratoř přímo v prohlížeči
[[X]] Praktický pracovní postup
[[ ]] Hypertext a značkovací jazyk
[[ ]] Element, značka, atribut a vnořování

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Od zdrojového souboru k publikovanému webu?**

<!-- data-randomize="true" -->
[(X)] DevTools: laboratoř přímo v prohlížeči
[( )] Výkon je součást designu
[( )] Projekt je víc než `index.html`
[( )] Praktický pracovní postup

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Jednoduchý web může mít jen několik souborů, ale i u něj se vyplatí přehledná struktura: text projekt/ ├── index.html ├── kontakt.html ├── styles/ │ └── main.css ├── images/ │ ├──…
[[X]] Nástroje pro vývojáře v prohlížeči umožňují prohlížet DOM, měnit CSS za běhu, sledovat box model, simulovat rozměry zařízení a zjišťovat, který styl skutečně vyhrál v kaskádě.
[[ ]] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[[ ]] V běžné řeči se často zaměňují pojmy značka — tag a element.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Praktický pracovní postup
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

# 2. Interaktivní shrnutí kapitoly

## Projekt tvoří více zdrojů

Publikovaný web obvykle není jediný soubor index.html. Projekt obsahuje HTML dokumenty, styly, skripty, obrázky, fonty a další prostředky uspořádané do smysluplných složek. Relativní cesta se vyhodnocuje podle umístění dokumentu, absolutní webová cesta začíná od kořene webu.

Názvy souborů mají být stabilní a přenositelné. Rozdíl mezi velkými a malými písmeny může na jednom systému projít a na produkčním serveru způsobit [[ chybu cesty | změnu barvy | pomalejší databázový dotaz ]].

## DevTools a průběžná kontrola

Vývojářské nástroje dovolují kontrolovat DOM, výsledné CSS, konzoli, síťové požadavky i různé velikosti viewportu. Úpravy v DevTools jsou vhodné pro experiment, ale samy se neuloží do [[zdrojových]] souborů.

**Co má smysl kontrolovat před publikací?**

<!-- data-randomize="true" -->
[[X]] nefunkční odkazy a chybějící soubory
[[X]] zobrazení na různých šířkách
[[X]] ovládání klávesnicí
[[X]] chyby v konzoli
[[ ]] pouze vzhled titulní stránky

## Pracovní postup

Rozumný postup začíná obsahem a strukturou, pokračuje stylováním a interakcemi a průběžně používá validaci a testování. Změny je vhodné ukládat ve verzovacím systému, aby bylo možné dohledat jejich důvod a vrátit se k funkčnímu stavu.

## Publikace

Před nasazením je potřeba zkontrolovat produkční cesty, velikost prostředků, metadata, přístupnost a chování bez vývojového prostředí. Úspěšné otevření souboru z disku [[ zaručuje stejné chování na serveru | (nenahrazuje test nasazené verze přes HTTP) | potvrzuje správnost všech relativních cest ]].
