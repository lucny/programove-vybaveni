<!--
title: 3. Kódování v informatice – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč se v digitální elektronice používá především dvojková reprezentace?**

<!-- data-randomize="true" -->
[( )] Protože všechny hodnoty jsou sudé.
[( )] Protože procesor používá deset číslic.
[(X)] Protože lze spolehlivě rozlišovat dva logické stavy.
[( )] Protože dvojkový zápis je vždy kratší.

---

**2. Které zápisy představují hodnotu 56 v desítkové soustavě?**

<!-- data-randomize="true" -->
[[X]] `111000₂`
[[X]] `70₈`
[[X]] `38₁₆`
[[ ]] `111000₁₀`
[[ ]] `56₁₆`

---

**3. Kolika bitům odpovídá jedna hexadecimální číslice?**

<!-- data-randomize="true" -->
[( )] 2
[( )] 3
[(X)] 4
[( )] 8

---

**4. Která operace má za hlavní cíl utajit obsah před neoprávněným příjemcem?**

<!-- data-randomize="true" -->
[( )] kódování
[( )] komprese
[(X)] šifrování
[( )] hashování

---

**5. Která tvrzení o QR kódu jsou správná?**

<!-- data-randomize="true" -->
[[X]] Je dvourozměrný maticový kód.
[[X]] Obsahuje prvky pro orientaci čtečky.
[[X]] Může využívat opravné kódy.
[[ ]] Každý černý modul je přímo jeden datový bit.
[[ ]] Bez připojení k internetu jej nelze přečíst.

---

**6. Co správně vystihuje vztah Unicode a UTF-8?**

<!-- data-randomize="true" -->
[( )] Jsou to dva názvy téhož standardu.
[(X)] Unicode určuje znaky, UTF-8 jejich bajtové uložení.
[( )] UTF-8 je starší sedmibitová tabulka.
[( )] Unicode je způsob komprese textu.

---

**7. Které tvrzení platí pro původní ASCII?**

<!-- data-randomize="true" -->
[( )] Je šestnáctibitové.
[(X)] Je sedmibitové.
[( )] Obsahuje všechny jazyky světa.
[( )] Je totožné s UTF-16.

---

**8. Jaký rozsah má běžný osmibitový unsigned integer?**

<!-- data-randomize="true" -->
[( )] −128 až 127
[( )] −255 až 255
[(X)] 0 až 255
[( )] 0 až 127

---

**9. Co může znamenat bitový vzor `11111111`?**

<!-- data-randomize="true" -->
[[X]] unsigned hodnotu 255
[[X]] signed hodnotu −1
[[X]] část barvy
[[X]] část instrukce
[[ ]] vždy jedině číslo 255

---

**10. Proč může být `0.1 + 0.2` u floating pointu nepatrně odlišné od `0.3`?**

<!-- data-randomize="true" -->
[( )] Desetinné sčítání procesor nepodporuje.
[( )] Hodnota 0,3 je matematicky neurčitá.
[( )] Jazyk přidává náhodnou odchylku.
[(X)] Některé desetinné hodnoty nelze binárně uložit přesně.


# 2. Interaktivní shrnutí kapitoly

## Číselné soustavy

Počítače uvnitř používají především [[binární]] reprezentaci. Dvojková soustava má dvě číslice, `0` a `1`, a stejně jako desítková soustava je [[ nepoziční | (poziční) | pouze symbolická ]]. Váhy jednotlivých pozic jsou mocniny čísla [[2]].

V informatice je praktická také [[hexadecimální]] soustava se základem 16. Používá číslice `0–9` a písmena `A–F`. Jedna její číslice odpovídá přesně [[4]] bitům, takže dlouhé binární hodnoty lze zapisovat přehledněji.

Například `1101 0110₂` lze zapsat jako [[ D8 | (D6) | C6 ]] v hexadecimální soustavě.

## Převody a význam zápisu

Číselná soustava nemění matematickou hodnotu čísla, pouze [[ jeho datový typ | (způsob jeho zápisu) | velikost paměti ]]. Při převodu binárního čísla do desítkové soustavy sčítáme váhy pozic, na kterých je jednička.

Při převodu mezi binární a hexadecimální soustavou seskupujeme bity po [[4]]. V mnoha programovacích jazycích se pro hexadecimální hodnoty používá prefix [[0x]] a pro binární hodnoty prefix [[0b]].

## Čtyři odlišné operace

Kódování, komprese, šifrování a hashování mají rozdílný účel. **Vyber všechna správná spojení:**

<!-- data-randomize="true" -->
[[X]] kódování — změna reprezentace
[[X]] komprese — zmenšení objemu
[[X]] šifrování — utajení obsahu
[[X]] hashování — kontrolní otisk
[[ ]] Base64 — bezpečné šifrování
[[ ]] ZIP — kryptografický hash

Base64 je příkladem [[ šifrování | (kódování) | komprese ]]. Kryptografický hash je navržen tak, aby se z něj běžně nedal rekonstruovat původní [[obsah]].

## Čárové kódy a QR

Čárový kód může nést pouze identifikátor, podle kterého informační systém vyhledá další údaje. QR kód je [[ jednorozměrný | (dvourozměrný) | analogový ]] maticový kód. Obsahuje nejen uživatelská data, ale také struktury pro orientaci, synchronizaci a opravu chyb.

Díky redundantním údajům lze některé poškozené QR kódy stále přečíst. Používají se zde mechanismy založené například na Reed-Solomonových [[kódech]].

## Text: ASCII, Unicode a UTF-8

Původní [[ASCII]] je sedmibitový standard se 128 kódovými hodnotami. Pro další jazyky později vznikala různá osmibitová kódování, například Windows-1250 nebo ISO-8859-2.

Unicode řeší problém společného číselného označení znaků. Konkrétnímu znaku přiřazuje [[ kódovací tabulku | (kódový bod) | bitovou hloubku ]]. Například `á` má označení `U+00E1`.

UTF-8 naproti tomu určuje, jak znak uložit do [[bajtů]]. Je proměnné délky: základní ASCII znaky používají jeden bajt, jiné znaky mohou používat více bajtů.

## Celá a desetinná čísla

Osmibitový unsigned integer má `2^8` kombinací a rozsah [[ 0 až 127 | (0 až 255) | −128 až 127 ]]. Záporná celá čísla moderní počítače běžně reprezentují pomocí dvojkového [[doplňku]].

Pevná šířka typu znamená omezený rozsah. Jeho překročení se označuje jako integer [[overflow]].

Reálná čísla se často ukládají jako floating point. Zjednodušeně obsahují znaménko, exponent a [[significand]]. Mnoho desetinných hodnot v binární soustavě nelze uložit přesně, a počítač proto pracuje s jejich [[ přesnou kopií | (aproximací) | textovou podobou ]].

Hlavní myšlenka kapitoly: počítač ukládá bitové vzory a jejich konkrétní [[význam]] určují pravidla kódování a datové typy.
