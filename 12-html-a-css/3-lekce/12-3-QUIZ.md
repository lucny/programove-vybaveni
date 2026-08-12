<!--
title: CSS: kaskáda, selektory a box model – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? CSS — Cascading Style Sheets popisuje prezentaci strukturovaného dokumentu.**

<!-- data-randomize="true" -->
[(X)] CSS není „HTML s barvami“
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Představme si nadpis, na který se vztahuje obecné pravidlo pro všechny h2, pravidlo třídy .warning, styl v konkrétním komponentu a uživatelské nastavení.**

<!-- data-randomize="true" -->
[(X)] Jak kaskáda rozhodne spor
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Základní selektory vybírají element, třídu nebo identifikátor: p, .note, menu.**

<!-- data-randomize="true" -->
[(X)] Selektory jako dotaz na dokument
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Starší poučka někdy říká, že responzivní web musí používat relativní jednotky a pixely jsou špatně.**

<!-- data-randomize="true" -->
[(X)] Jednotky nejsou soutěž „pixely proti procentům“
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**5. Které tvrzení odpovídá tématu CSS není „HTML s barvami“?**

<!-- data-randomize="true" -->
[(X)] CSS — Cascading Style Sheets popisuje prezentaci strukturovaného dokumentu.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**6. Které tvrzení odpovídá tématu Jednotky nejsou soutěž „pixely proti procentům“?**

<!-- data-randomize="true" -->
[(X)] Starší poučka někdy říká, že responzivní web musí používat relativní jednotky a pixely jsou špatně.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] CSS není „HTML s barvami“
[[X]] Jak kaskáda rozhodne spor
[[X]] Selektory jako dotaz na dokument
[[ ]] Hypertext a značkovací jazyk
[[ ]] Element, značka, atribut a vnořování

---

**8. Které téma tvoří jednu z hlavních částí kapitoly CSS: kaskáda, selektory a box model?**

<!-- data-randomize="true" -->
[(X)] Selektory jako dotaz na dokument
[( )] Projekt je víc než `index.html`
[( )] DevTools: laboratoř přímo v prohlížeči
[( )] Praktický pracovní postup

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] CSS — Cascading Style Sheets popisuje prezentaci strukturovaného dokumentu.
[[X]] Představme si nadpis, na který se vztahuje obecné pravidlo pro všechny h2, pravidlo třídy .warning, styl v konkrétním komponentu a uživatelské nastavení.
[[ ]] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[[ ]] V běžné řeči se často zaměňují pojmy značka — tag a element.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Jednotky nejsou soutěž „pixely proti procentům“
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

# 2. Interaktivní shrnutí kapitoly

## CSS odděluje obsah a prezentaci

HTML popisuje strukturu, CSS určuje vzhled a rozložení. Pravidlo se skládá ze selektoru a deklarací vlastností. Styl lze připojit externím souborem, který usnadňuje opakované použití a správu.

Kaskáda řeší situaci, kdy na stejný prvek působí více pravidel. Rozhoduje původ pravidla, důležitost, specificita a pořadí. Pozdější pravidlo tedy [[ vyhraje vždy bez výjimky | (rozhodne jen tehdy, když předchozí kritéria nerozhodla) | automaticky zruší dědičnost ]].

## Selektory

Selektor může vybírat element, třídu, identifikátor, atribut nebo vztah mezi prvky. Třída začíná tečkou, identifikátor znakem [[#]]. Pseudotřídy popisují stav nebo pozici, například hover či first-child.

Příliš specifické selektory komplikují údržbu. Užitečné je volit takovou přesnost, která vyjádří záměr, ale neváže styl zbytečně na dlouhou cestu dokumentem.

## Box model

Každý prvek lze chápat jako obsah obklopený paddingem, rámečkem a marginem. Ve výchozím modelu content-box se zadaná šířka vztahuje na obsah; s box-sizing: border-box zahrnuje také padding a border.

**Které části patří do box modelu?**

<!-- data-randomize="true" -->
[[X]] content
[[X]] padding
[[X]] border
[[X]] margin
[[ ]] databázový index

## Jednotky podle účelu

Pixely jsou užitečné pro přesné malé rozměry, rem vychází z kořenové velikosti písma, procenta reagují na rodiče a jednotky viewportu na okno. Volba jednotky má vycházet ze vztahu, který chceme zachovat. Responzivita proto nevzniká mechanickým nahrazením všech px za [[procenta]].
