<!--
title: Soubory, adresáře a data na disku – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je soubor z pohledu operačního systému?**

<!-- data-randomize="true" -->
[(X)] Pojmenovaný celek dat doplněný metadaty.
[( )] Pouze název s příponou určující obsah.
[( )] Vždy souvislý blok fyzicky uložený na disku.
[( )] Výhradně dokument vytvořený uživatelem.

---

**2. Které údaje mohou patřit mezi metadata souboru?**

<!-- data-randomize="true" -->
[[X]] název
[[X]] velikost
[[X]] vlastník
[[X]] čas změny
[[X]] přístupová práva
[[ ]] barva ikony v průzkumníku

---

**3. Co se stane po přejmenování `obrazek.jpg` na `obrazek.txt`?**

<!-- data-randomize="true" -->
[(X)] Změní se název, nikoli automaticky skutečný formát.
[( )] Soubor se převede na prostý text.
[( )] Obsah se zkomprimuje jako TXT.
[( )] Operační systém přepíše všechny bajty.

---

**4. Co může systém využít k rozpoznání skutečného typu souboru?**

<!-- data-randomize="true" -->
[[X]] příponu
[[X]] MIME type
[[X]] metadata
[[X]] bajtovou signaturu
[[ ]] pouze ikonu aplikace

---

**5. Která cesta je absolutní ve Windows?**

<!-- data-randomize="true" -->
[(X)] C:\Users\Student\Documents\data.csv
[( )] data\data.csv
[( )] ../images/logo.png
[( )] ./projekt/index.html

---

**6. Co obvykle znamená `..` v relativní cestě?**

<!-- data-randomize="true" -->
[(X)] Nadřazený adresář.
[( )] Kořen disku.
[( )] Aktuální soubor.
[( )] Libovolný znak.

---

**7. Která tvrzení o programových a datových souborech jsou správná?**

<!-- data-randomize="true" -->
[[X]] Pythonový `.py` může být textový i programový soubor.
[[X]] Dokument s makry může obsahovat data i instrukce.
[[X]] Role souboru závisí na kontextu použití.
[[ ]] Program musí být vždy jediný binární soubor.
[[ ]] Textový a programový soubor jsou vždy protiklady.

---

**8. Jaký je rozdíl mezi programem na disku a procesem?**

<!-- data-randomize="true" -->
[(X)] Proces je běžící instance programu v paměti.
[( )] Proces je přípona spustitelného souboru.
[( )] Program je vždy běžící a proces uložený.
[( )] Jde o dva názvy pro stejnou věc.

---

**9. Které soubory mohou být skripty podle kapitoly?**

<!-- data-randomize="true" -->
[[X]] .py
[[X]] .js
[[X]] .sh
[[X]] .ps1
[[ ]] .jpg
[[ ]] .pdf

---

**10. Proč může být soubor `faktura.pdf.exe` nebezpečný?**

<!-- data-randomize="true" -->
[(X)] Při skrytých příponách může vypadat jako dokument, ale být spustitelný.
[( )] Každý PDF soubor je ve skutečnosti EXE.
[( )] Dvojitá přípona automaticky soubor zašifruje.
[( )] Windows spouští vždy první příponu.


# 2. Interaktivní shrnutí kapitoly

## Soubor a jeho skutečný typ

Soubor je pojmenovaný celek dat uložený v [[souborovém]] systému. Operační systém s ním pracuje jako s posloupností bajtů doplněnou o metadata, například název, velikost, vlastníka, čas změny a oprávnění.

Přípona je praktická pomůcka, ale [[ vždy přesně určuje formát | (sama o sobě nezaručuje skutečný obsah) | určuje fyzické umístění na disku ]]. Skutečný typ může systém rozpoznávat také podle MIME typu nebo charakteristické bajtové [[signatury]].

## Adresáře a cesty

Adresáře vytvářejí hierarchický [[strom]]. V Unixu je kořen označen `/`, zatímco Windows běžně používá písmena jednotek. Absolutní cesta začíná od jednoznačného počátku, relativní cesta se vztahuje k aktuálnímu adresáři.

Zápis `..` obvykle označuje [[ kořenový | (nadřazený) | aktuální ]] adresář a `.` adresář aktuální. Relativní cesty jsou praktické zejména v přenositelných projektech.

**Vyber správná tvrzení o zástupných znacích:**

<!-- data-randomize="true" -->
[[X]] `*` tradičně zastupuje libovolnou posloupnost znaků.
[[X]] `?` tradičně zastupuje jeden znak.
[[ ]] `*` vždy označuje kořen disku.
[[ ]] `?` vždy znamená nadřazený adresář.

## Programy, data a procesy

Rozdělení na programové a datové soubory je užitečné, ale hranice není absolutní. Skript `.py` je textový soubor a zároveň může obsahovat [[programové]] instrukce. Dokument s makry může kombinovat data i vykonávaný obsah.

Program na disku není totéž co proces. Po spuštění operační systém vytvoří běžící [[proces]]. Jedna aplikace přitom může používat více procesů, knihoven, konfigurací a datových souborů.

## Skripty, knihovny a bezpečnost

Skript je interpretován příslušným prostředím; v Unixu může první řádek obsahovat [[shebang]]. Knihovny poskytují znovupoužitelný kód a mohou být statické nebo dynamické. Konflikty verzí závislostí mohou vést k problému označovanému jako dependency [[hell]].

Asociace souboru pouze říká, kterou aplikaci systém nabídne k jeho otevření. Bezpečné je proto [[ spoléhat na ikonu | (kontrolovat skutečný typ, příponu a původ souboru) | vždy přejmenovat stažený soubor ]].
