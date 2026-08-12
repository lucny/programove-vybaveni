<!--
title: Sémantická struktura, odkazy, média a formuláře – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.**

<!-- data-randomize="true" -->
[(X)] Nadpis není „větší text“
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Element a je jedním z prvků, které odlišily web od běžného elektronického dokumentu.**

<!-- data-randomize="true" -->
[(X)] Odkaz vytváří web
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Obrázek vkládáme elementem img, ale kvalitní zápis řeší více než samotnou cestu k souboru.**

<!-- data-randomize="true" -->
[(X)] Obrázek není jen soubor vedle HTML
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Formuláře jsou místem, kde uživatel přestává být pouhým čtenářem.**

<!-- data-randomize="true" -->
[(X)] Formulář je rozhovor mezi člověkem a systémem
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**5. Které tvrzení odpovídá tématu Nadpis není „větší text“?**

<!-- data-randomize="true" -->
[(X)] HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**6. Které tvrzení odpovídá tématu Formulář je rozhovor mezi člověkem a systémem?**

<!-- data-randomize="true" -->
[(X)] Formuláře jsou místem, kde uživatel přestává být pouhým čtenářem.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Nadpis není „větší text“
[[X]] Odkaz vytváří web
[[X]] Obrázek není jen soubor vedle HTML
[[ ]] Hypertext a značkovací jazyk
[[ ]] Element, značka, atribut a vnořování

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Sémantická struktura, odkazy, média a formuláře?**

<!-- data-randomize="true" -->
[(X)] Obrázek není jen soubor vedle HTML
[( )] Projekt je víc než `index.html`
[( )] DevTools: laboratoř přímo v prohlížeči
[( )] Praktický pracovní postup

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] HTML dává obsahu význam. Nadpisy h1 až h6 vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma.
[[X]] Element a je jedním z prvků, které odlišily web od běžného elektronického dokumentu.
[[ ]] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[[ ]] V běžné řeči se často zaměňují pojmy značka — tag a element.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Formulář je rozhovor mezi člověkem a systémem
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

# 2. Interaktivní shrnutí kapitoly

## Sémantická struktura

Nadpisy vytvářejí hierarchii dokumentu, nikoli jen různé velikosti textu. Hlavní oblasti stránky lze vyjádřit elementy header, nav, main, article, section a footer. Správně zvolený element pomáhá [[ pouze grafickému editoru | (prohlížeči, vyhledávači i asistivním technologiím) | výhradně serverové databázi ]].

Odkaz vzniká elementem a a jeho cíl určuje atribut [[href]]. Text odkazu má popisovat cíl; neurčité „klikněte zde“ ztrácí význam mimo okolní odstavec.

## Média a tabulková data

Obrázek potřebuje správnou cestu v src a textovou alternativu v alt. Alternativní text nepřepisuje každý detail, ale předává účel obrázku v daném kontextu. Dekorativní obrázek může mít prázdný alt, aby jej čtečka zbytečně neoznamovala.

Tabulka patří skutečným datům se vztahy mezi řádky a sloupci. Záhlaví označuje element [[th]] a popisek tabulky caption. Používat tabulku k rozložení celé stránky zaměňuje význam datové struktury za vizuální layout.

## Formulář jako dialog

Formulář sbírá vstupy a odesílá je ke zpracování. Element label musí být spojen s ovládacím prvkem, aby jeho význam chápal uživatel i asistivní technologie. Atribut name určuje jméno odesílané hodnoty.

**Co zlepšuje použitelnost formuláře?**

<!-- data-randomize="true" -->
[[X]] jednoznačné popisky polí
[[X]] vhodné typy vstupů
[[X]] srozumitelné chybové zprávy
[[ ]] spoléhání pouze na barvu chybného pole

Kontrola v prohlížeči zvyšuje pohodlí, ale server musí vstupy ověřit znovu. Klientskou validaci lze obejít, takže bezpečnostní pravidla patří [[ pouze do HTML atributů | (také na serverovou stranu) | jen do grafického návrhu ]].
