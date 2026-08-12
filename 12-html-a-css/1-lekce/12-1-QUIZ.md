<!--
title: HTML: dokument, kterému rozumí člověk i stroj – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.**

<!-- data-randomize="true" -->
[(X)] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu
[( )] Validní kód není totéž co kvalitní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? V běžné řeči se často zaměňují pojmy značka — tag a element.**

<!-- data-randomize="true" -->
[(X)] Element, značka, atribut a vnořování
[( )] Hypertext a značkovací jazyk
[( )] Kostra moderního dokumentu
[( )] Validní kód není totéž co kvalitní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.**

<!-- data-randomize="true" -->
[(X)] Kostra moderního dokumentu
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Validní kód není totéž co kvalitní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Validace kontroluje, zda dokument odpovídá syntaktickým pravidlům standardu.**

<!-- data-randomize="true" -->
[(X)] Validní kód není totéž co kvalitní web
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**5. Které tvrzení odpovídá tématu Hypertext a značkovací jazyk?**

<!-- data-randomize="true" -->
[(X)] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.
[( )] Element a je jedním z prvků, které odlišily web od běžného elektronického dokumentu.
[( )] Obrázek vkládáme elementem img, ale kvalitní zápis řeší více než samotnou cestu k souboru.

---

**6. Které tvrzení odpovídá tématu Validní kód není totéž co kvalitní web?**

<!-- data-randomize="true" -->
[(X)] Validace kontroluje, zda dokument odpovídá syntaktickým pravidlům standardu.
[( )] HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.
[( )] Element a je jedním z prvků, které odlišily web od běžného elektronického dokumentu.
[( )] Obrázek vkládáme elementem img, ale kvalitní zápis řeší více než samotnou cestu k souboru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Hypertext a značkovací jazyk
[[X]] Element, značka, atribut a vnořování
[[X]] Kostra moderního dokumentu
[[ ]] Nadpis není „větší text“
[[ ]] Odkaz vytváří web

---

**8. Které téma tvoří jednu z hlavních částí kapitoly HTML: dokument, kterému rozumí člověk i stroj?**

<!-- data-randomize="true" -->
[(X)] Element, značka, atribut a vnořování
[( )] Projekt je víc než `index.html`
[( )] DevTools: laboratoř přímo v prohlížeči
[( )] Praktický pracovní postup

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[[X]] V běžné řeči se často zaměňují pojmy značka — tag a element.
[[ ]] HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.
[[ ]] Element a je jedním z prvků, které odlišily web od běžného elektronického dokumentu.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Validní kód není totéž co kvalitní web
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

# 2. Interaktivní shrnutí kapitoly

## HTML popisuje význam dokumentu

HTML je značkovací jazyk pro strukturu a význam webového obsahu. Hypertext umožňuje propojit dokumenty odkazy; značení říká, která část je nadpis, odstavec, navigace nebo tabulková data. HTML proto [[ popisuje algoritmus aplikace | (vytváří sémantickou strukturu dokumentu) | určuje pouze barvy a rozměry prvků ]].

Element zahrnuje značku, obsah a případnou koncovou značku. Atribut doplňuje vlastnost elementu, například cíl odkazu, zdroj obrázku nebo jazyk dokumentu. Třída class může být společná více prvkům, zatímco [[id]] má v dokumentu jednoznačně označit konkrétní prvek.

## Základní kostra

Kořenovým elementem je html, metadata a odkazy na zdroje patří do head a viditelný obsah do [[body]]. Deklarace typu dokumentu pomáhá prohlížeči použít moderní režim zpracování.

Nastavení charset na UTF-8 určuje znakové kódování. Atribut lang pomáhá čtečkám obrazovky a překladovým nástrojům a viewport ovlivňuje přirozené zobrazení na mobilních zařízeních.

**Které prvky patří do kvalitní kostry HTML dokumentu?**

<!-- data-randomize="true" -->
[[X]] smysluplný title
[[X]] správně nastavený jazyk dokumentu
[[X]] deklarované znakové kódování
[[ ]] tabulkový layout celé stránky

## Validita a kvalita

Validátor hledá porušení syntaktických pravidel, například chyby ve vnoření nebo nepovolené atributy. Validní dokument ale může být stále nepřístupný, pomalý nebo obsahově matoucí.

Validace je tedy [[ konečný důkaz kvality webu | (jedna z více vrstev kontroly) | náhrada uživatelského testování ]]. Vedle ní je potřeba kontrolovat sémantiku, přístupnost, použitelnost, funkčnost a výkon.
