<!--
title: 5. Datová komprese – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč lze některá data účinně komprimovat?**

<!-- data-randomize="true" -->
[( )] Protože každý soubor obsahuje prázdné bajty.
[(X)] Protože obsahují opakující se nebo předvídatelné struktury.
[( )] Protože komprese vždy odstraní polovinu bitů.
[( )] Protože procesor mění význam dat.

---

**2. Co musí platit pro bezeztrátovou kompresi?**

<!-- data-randomize="true" -->
[( )] Výsledek musí být vždy desetkrát menší.
[( )] Část detailů může být odstraněna.
[(X)] Původní data musí být obnovena bitově přesně.
[( )] Lze ji použít jen na text.

---

**3. Které formáty jsou v kapitole uvedeny jako bezeztrátové?**

<!-- data-randomize="true" -->
[[X]] ZIP
[[X]] 7z
[[X]] PNG
[[X]] FLAC
[[ ]] MP3
[[ ]] JPEG

---

**4. Kde je ztrátová komprese obvykle přijatelná?**

<!-- data-randomize="true" -->
[[X]] fotografie pro web
[[X]] streamované video
[[X]] hudba pro běžný poslech
[[ ]] zdrojový kód
[[ ]] databázová data vyžadující přesnou obnovu

---

**5. Soubor se zmenšil z 10 MB na 2 MB. Jaký je kompresní poměr?**

<!-- data-randomize="true" -->
[( )] 2 : 1
[(X)] 5 : 1
[( )] 8 : 1
[( )] 10 : 1

---

**6. Jaká je procentuální úspora v předchozím příkladu?**

<!-- data-randomize="true" -->
[( )] 20 %
[( )] 50 %
[(X)] 80 %
[( )] 500 %

---

**7. Který princip využívá RLE?**

<!-- data-randomize="true" -->
[( )] Častým znakům dává kratší kódy.
[(X)] Série stejných hodnot zapisuje úsporněji.
[( )] Šifruje opakované bloky.
[( )] Převádí obraz na vektory.

---

**8. Co je podstatou Huffmanova kódování?**

<!-- data-randomize="true" -->
[( )] Všechny symboly mají stejnou délku.
[( )] Opakované bloky se vždy zapisují číslem.
[(X)] Častější symboly dostávají kratší kódy.
[( )] Data se ukládají bez bitů.

---

**9. Které tvrzení o MP4 je správné?**

<!-- data-randomize="true" -->
[( )] MP4 je jeden konkrétní video kodek.
[(X)] MP4 je kontejner pro různé datové proudy.
[( )] MP4 je bezeztrátový archivní algoritmus.
[( )] MP4 může obsahovat pouze obraz.

---

**10. Které dvojice formátu nebo kodeku a použití odpovídají textu?**

<!-- data-randomize="true" -->
[[X]] FLAC — bezeztrátový zvuk
[[X]] JPEG — fotografie
[[X]] Opus — zvuk
[[X]] H.264 — video
[[ ]] PNG — ztrátový hudební kodek
[[ ]] ZIP — video kodek


# 2. Interaktivní shrnutí kapitoly

## Proč komprese funguje

Komprese mění reprezentaci dat tak, aby zabírala méně místa. Využívá především [[ šifrování | (redundanci a předvídatelné struktury) | změnu významu dat ]].

Například řetězec `AAAAAAAAAAAA` lze popsat úsporněji jako `12×A`. Takový princip funguje jen tehdy, když vstupní data mají vhodnou [[strukturu]]. Soubor, který už byl účinně komprimován, se dalším zabalením často zmenší jen málo.

Komprese a archivace nejsou totožné. Archiv může více souborů spojit do jednoho balíčku, zatímco komprese se snaží [[ soubory šifrovat | (snížit jejich datový objem) | změnit jejich licenci ]].

## Bezeztrátová a ztrátová komprese

Bezeztrátová komprese musí po dekompresi obnovit [[ přibližně podobná data | (bitově přesně původní data) | pouze viditelnou část souboru ]]. Je proto vhodná pro programy, databáze, textové dokumenty nebo zdrojové kódy.

Ztrátová komprese část informace záměrně [[odstraní]]. Používá se tam, kde lze méně významné části obrazu, zvuku nebo videa zjednodušit a získat výrazně menší soubor.

**Vyber správné příklady:**

<!-- data-randomize="true" -->
[[X]] PNG — bezeztrátový obraz
[[X]] FLAC — bezeztrátový zvuk
[[X]] JPEG — ztrátový obraz
[[X]] MP3 — ztrátový zvuk
[[X]] H.264 — ztrátové video
[[ ]] ZIP — ztrátová fotografie

Rozhodnutí mezi oběma přístupy závisí na tom, zda musí být původní data obnovena [[přesně]].

## Poměr, úspora a kvalita

Když se soubor zmenší z 10 MB na 2 MB, kompresní poměr je [[ 2 : 1 | (5 : 1) | 8 : 1 ]] a úspora činí [[80]] procent.

U ztrátové komprese se musí hledat kompromis mezi velikostí a [[kvalitou]]. U zvuku a videa se často používá pojem bitrate, tedy počet bitů za [[sekundu]].

Stejný bitrate přitom automaticky neznamená stejnou kvalitu. Záleží také na kodeku, nastavení a charakteru [[obsahu]].

## Klasické kompresní principy

RLE neboli Run-Length Encoding je výhodné u dlouhých sérií stejných hodnot. Řetězec `AAAAAAABBBCC` lze zjednodušeně zapsat jako [[ AAAAAAABBBCC | (7A3B2C) | 3A7B2C ]]. Jeho účinnost proto závisí na opakování.

Huffmanovo kódování využívá četnost symbolů. Častějším symbolům přiděluje [[ delší | (kratší) | vždy stejně dlouhá ]] kódová slova.

Algoritmy rodiny Lempel-Ziv využívají opakující se sekvence a nahrazují je odkazy na již známé části nebo položky [[slovníku]].

## Formát, kontejner a kodek

Kodek je algoritmus nebo implementace pro kódování a dekódování dat. [[kontejner]] je struktura, která může spojovat několik datových proudů a metadata.

Soubor MP4 může například obsahovat video H.264, zvuk AAC, titulky a metadata. H.264 je v tomto příkladu [[ kontejner | (video kodek) | archivní formát ]], zatímco MP4 je kontejner.

Při volbě formátu nestačí sledovat příponu. Důležité jsou také kompatibilita, velikost, kvalita, rychlost zpracování a [[podpora]] v cílovém prostředí.

Hlavní myšlenka kapitoly: komprese využívá strukturu a [[redundanci]] dat; bezeztrátová zachovává vše, ztrátová získává větší úsporu za cenu řízené ztráty informace.
