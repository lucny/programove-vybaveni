<!--
title: Barva: od lidského oka k číslům v počítači – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je barva z hlediska kapitoly?**

<!-- data-randomize="true" -->
[(X)] Výsledek interakce světla, materiálu, oka a mozku.
[( )] Jednoduchá absolutní vlastnost objektu.
[( )] Pouze RGB trojice bez kontextu.
[( )] Výhradně vlnová délka jednoho fotonu.

---

**2. Které typy čípků lidské oko používá pro barevné vidění?**

<!-- data-randomize="true" -->
[[X]] S
[[X]] M
[[X]] L
[[ ]] R jako samostatný standardní typ
[[ ]] B jako samostatný standardní typ

---

**3. Co je RGB?**

<!-- data-randomize="true" -->
[(X)] Aditivní model skládající světlo ze tří složek.
[( )] Subtraktivní model tiskových inkoustů.
[( )] Model pouze pro černobílý tisk.
[( )] Jiný název pro ICC profil.

---

**4. Co platí pro neutrální šedou v RGB?**

<!-- data-randomize="true" -->
[(X)] R, G a B mají stejnou hodnotu.
[( )] R je vždy 255 a ostatní 0.
[( )] Obsahuje pouze kanál K.
[( )] Nemá žádné číselné hodnoty.

---

**5. Které jsou běžné RGB barevné prostory?**

<!-- data-randomize="true" -->
[[X]] sRGB
[[X]] Display P3
[[X]] Adobe RGB
[[ ]] CMYK jako jeden RGB prostor
[[ ]] DPI

---

**6. Proč se v tisku používá samostatný kanál K?**

<!-- data-randomize="true" -->
[(X)] Kvůli kvalitě, neutralitě, ekonomice a detailu černé.
[( )] Protože cyan nelze tisknout.
[( )] Aby se tisk změnil na aditivní.
[( )] Protože monitor používá čtyři subpixely.

---

**7. Co je gamut?**

<!-- data-randomize="true" -->
[(X)] Rozsah barev, které systém dokáže reprezentovat nebo reprodukovat.
[( )] Počet pixelů obrazu.
[( )] Typ tiskového papíru.
[( )] Velikost souboru.

---

**8. K čemu slouží ICC profil?**

<!-- data-randomize="true" -->
[(X)] Popisuje barevné chování zařízení nebo pracovního prostoru.
[( )] Určuje počet snímků za sekundu.
[( )] Šifruje obrazový soubor.
[( )] Nahrazuje kalibraci optiky.

---

**9. Jaký je rozdíl mezi kalibrací a profilací monitoru?**

<!-- data-randomize="true" -->
[(X)] Kalibrace nastaví stav, profilace změří jeho skutečné chování.
[( )] Jde o stejnou operaci.
[( )] Profilace mění počet pixelů.
[( )] Kalibrace vytváří vždy nový barevný prostor.

---

**10. Proč jsou HSL/HSV užitečné?**

<!-- data-randomize="true" -->
[(X)] Umožňují intuitivněji ovládat odstín, sytost a světlost/jas.
[( )] Jsou fyzikálně přesným modelem lidského oka.
[( )] Nahrazují všechny ICC profily.
[( )] Jsou určeny jen pro tiskárny.


# 2. Interaktivní shrnutí kapitoly

## Barva a lidské vidění

Barva není pouze vlastnost pixelu. Vzniká interakcí světla, materiálu a vnímání. Lidské oko používá tři typy čípků označované S, M a [[L]], jejichž citlivosti se překrývají.

Proto není přesné chápat oko jako tři jednoduché „RGB senzory“. Barva v počítači je modelovaná číselná [[reprezentace]].

## RGB a CMYK

RGB je [[aditivní]] model: začínáme od tmy a přidáváme světlo. Hodnota `(255,255,255)` je v osmibitovém RGB bílá a stejné hodnoty všech kanálů tvoří neutrální šedou.

CMYK je [[subtraktivní]] model pro tisk. Obsahuje cyan, magenta, yellow a black. Převod z RGB do CMYK závisí na konkrétní tiskové podmínce, papíru, inkoustech a profilu.

## HSL, HSV a barevné prostory

HSL a HSV jsou pohodlné pro člověka, protože oddělují odstín, sytost a světlost či jas. Nejsou však perceptuálně [[uniformní]].

sRGB, Display P3 a Adobe RGB jsou odlišné barevné prostory. Stejná RGB trojice proto nemusí znamenat úplně stejnou fyzickou [[barvu]].

## Gamut a ICC

[[gamut]] je rozsah barev, které systém dokáže reprezentovat nebo reprodukovat. ICC profil popisuje chování konkrétního zařízení nebo pracovního prostoru.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] sRGB má širokou podporu na webu
[[X]] Display P3 má širší gamut než sRGB
[[X]] ICC profil pomáhá převádět barvy mezi zařízeními
[[ ]] DPI je barevný prostor
[[ ]] všechny monitory zobrazují stejné RGB hodnoty fyzicky stejně

Kalibrace nastavuje zařízení do definovaného stavu, profilace jeho chování [[měří]] a popisuje.
