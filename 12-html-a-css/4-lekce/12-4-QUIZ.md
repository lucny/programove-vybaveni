<!--
title: Layout: od normálního toku k Flexboxu a Gridu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Než použijeme jakýkoli layout systém, prohlížeč skládá dokument podle normal flow.**

<!-- data-randomize="true" -->
[(X)] Normální tok je výchozí, ne překážka
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Flexbox je vhodný tam, kde prvky organizujeme především v jednom směru — do řádku nebo sloupce.**

<!-- data-randomize="true" -->
[(X)] Flexbox: když řešíme hlavně jeden směr
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? CSS Grid řeší dvourozměrné rozložení.**

<!-- data-randomize="true" -->
[(X)] Grid: vztahy v řádcích i sloupcích
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Původní responzivní webdesign se často vysvětloval jako tři verze: mobil, tablet a desktop.**

<!-- data-randomize="true" -->
[(X)] Responzivní design není sada tří obrazovek
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

---

**5. Které tvrzení odpovídá tématu Normální tok je výchozí, ne překážka?**

<!-- data-randomize="true" -->
[(X)] Než použijeme jakýkoli layout systém, prohlížeč skládá dokument podle normal flow.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**6. Které tvrzení odpovídá tématu Responzivní design není sada tří obrazovek?**

<!-- data-randomize="true" -->
[(X)] Původní responzivní webdesign se často vysvětloval jako tři verze: mobil, tablet a desktop.
[( )] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[( )] V běžné řeči se často zaměňují pojmy značka — tag a element.
[( )] Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element html, hlavička head a viditelné tělo body.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Normální tok je výchozí, ne překážka
[[X]] Flexbox: když řešíme hlavně jeden směr
[[X]] Grid: vztahy v řádcích i sloupcích
[[ ]] Hypertext a značkovací jazyk
[[ ]] Element, značka, atribut a vnořování

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Layout: od normálního toku k Flexboxu a Gridu?**

<!-- data-randomize="true" -->
[(X)] Flexbox: když řešíme hlavně jeden směr
[( )] Projekt je víc než `index.html`
[( )] DevTools: laboratoř přímo v prohlížeči
[( )] Praktický pracovní postup

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Než použijeme jakýkoli layout systém, prohlížeč skládá dokument podle normal flow.
[[X]] Flexbox je vhodný tam, kde prvky organizujeme především v jednom směru — do řádku nebo sloupce.
[[ ]] Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy.
[[ ]] V běžné řeči se často zaměňují pojmy značka — tag a element.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Responzivní design není sada tří obrazovek
[( )] Hypertext a značkovací jazyk
[( )] Element, značka, atribut a vnořování
[( )] Kostra moderního dokumentu

# 2. Interaktivní shrnutí kapitoly

## Normální tok

Blokové prvky se v normálním toku skládají pod sebe a řádkové prvky uvnitř řádku. Tento výchozí mechanismus je základem stabilního dokumentu; není nutné každý prvek ručně pozicovat.

Absolutní pozicování vyjme prvek z běžného toku, proto se hodí pro konkrétní překrytí, nikoli jako univerzální nástroj layoutu. Stabilní rozvržení obvykle [[ respektuje přirozený tok a používá specializované layouty | umísťuje každý prvek souřadnicemi | převádí celý obsah na obrázek ]].

## Flexbox

Flexbox řeší rozložení převážně v jednom směru. Kontejner určuje hlavní a příčnou osu; vlastnosti justify-content a align-items řídí rozmístění na těchto osách. Jednotlivé položky mohou růst, zmenšovat se nebo se zalamovat.

Hlavní směr určuje [[flex-direction]]. Flexbox se hodí pro navigace, řady ovládacích prvků nebo zarovnání komponent.

## Grid

CSS Grid pracuje současně s řádky a sloupci. Umožňuje definovat stopy, mezery a oblasti a pak do nich umístit obsah. Jednotka fr rozděluje [[ dostupný prostor mřížky | velikost písma dokumentu | počet síťových požadavků ]].

**Kdy je vhodný který nástroj?**

<!-- data-randomize="true" -->
[[X]] Flexbox — uspořádání prvků v jednom hlavním směru
[[X]] Grid — vztahy mezi řádky a sloupci
[[X]] normální tok — běžný textový dokument
[[ ]] absolutní pozicování — povinný základ každého responzivního webu

## Responzivní návrh

Responzivní web reaguje na dostupný prostor a možnosti zařízení. Používá pružné rozměry, zalamování, media queries a obsahové breakpointy. Cílem není vytvořit tři pevné verze, ale rozvržení, které se chová smysluplně i mezi nimi.
