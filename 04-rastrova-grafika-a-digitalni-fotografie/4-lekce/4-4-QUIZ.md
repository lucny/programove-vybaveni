<!--
title: Rastrový editor a nedestruktivní práce s obrazem – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co dělá výběr v rastrovém editoru?**

<!-- data-randomize="true" -->
[(X)] Určuje oblast, na kterou bude operace působit.
[( )] Mění automaticky rozlišení celého obrazu.
[( )] Vždy maže pixely mimo oblast.
[( )] Převádí obraz do CMYK.

---

**2. Jaký je rozdíl mezi ořezem a změnou velikosti?**

<!-- data-randomize="true" -->
[(X)] Ořez odstraní část obrazu, změna velikosti přepočítá počet pixelů.
[( )] Jde o totožné operace.
[( )] Ořez vždy interpoluje celý obraz.
[( )] Změna velikosti pouze přesune výběr.

---

**3. Co může mít vrstva?**

<!-- data-randomize="true" -->
[[X]] obsah
[[X]] průhlednost
[[X]] masku
[[X]] transformaci
[[X]] režim prolnutí
[[ ]] pouze jednu pevnou barvu

---

**4. Co dělá režim Multiply?**

<!-- data-randomize="true" -->
[(X)] Typicky ztmavuje kombinaci vrstev.
[( )] Vždy zesvětluje.
[( )] Maže spodní vrstvu.
[( )] Mění rozměry dokumentu.

---

**5. Co je hlavní výhodou masky vrstvy?**

<!-- data-randomize="true" -->
[(X)] Skrývá část obsahu bez jeho trvalého smazání.
[( )] Vždy zmenší soubor.
[( )] Převádí vrstvu na vektor.
[( )] Nahrazuje historii úprav.

---

**6. Co je adjustment layer?**

<!-- data-randomize="true" -->
[(X)] Vrstva uchovávající parametrickou korekci místo přepsaných pixelů.
[( )] Vrstva obsahující pouze text.
[( )] Automaticky sloučený obraz.
[( )] Formát komprese.

---

**7. K čemu slouží smart object?**

<!-- data-randomize="true" -->
[(X)] Pomáhá zachovat zdroj při opakovaných transformacích a filtrech.
[( )] Vždy převádí obraz na 8 bitů.
[( )] Nahrazuje alfa kanál.
[( )] Je to druh histogramu.

---

**8. Co ukazuje histogram?**

<!-- data-randomize="true" -->
[(X)] Rozložení tónových hodnot v obrazu.
[( )] Počet vrstev dokumentu.
[( )] Seznam EXIF metadat.
[( )] Přesný subjektivní stupeň kvality.

---

**9. Co je clipping?**

<!-- data-randomize="true" -->
[(X)] Sloučení hodnot na kraj rozsahu se ztrátou detailu.
[( )] Přepnutí mezi vrstvami.
[( )] Změna DPI tiskárny.
[( )] Vektorové oříznutí cesty.

---

**10. Které činnosti mohou dělat moderní AI nástroje editoru?**

<!-- data-randomize="true" -->
[[X]] výběr objektu
[[X]] odstranění pozadí
[[X]] redukci šumu
[[X]] zvětšení obrazu
[[X]] generativní doplnění obsahu
[[ ]] zaručenou rekonstrukci původní reality


# 2. Interaktivní shrnutí kapitoly

## Výběr, ořez a transformace

Výběr určuje oblast účinku operace. Může vzniknout geometricky, podle barvy, hran nebo pomocí AI [[segmentace]]. Ořez odstraní část obrazu, zatímco transformace mění velikost, rotaci či perspektivu.

Opakované destruktivní transformace mohou kvalitu zhoršovat, proto jsou výhodné nedestruktivní postupy.

## Vrstvy a masky

Vrstva je samostatně editovatelný prvek s obsahem, průhledností, maskou a efekty. Režim [[prolnutí]] určuje matematickou kombinaci pixelů s vrstvami pod ní.

Maska obsah nemaže, ale řídí jeho [[viditelnost]]. Černá typicky skryje, bílá zobrazí a odstíny šedé vytvoří částečný účinek.

**Vyber výhody masek:**

<!-- data-randomize="true" -->
[[X]] nedestruktivní skrytí obsahu
[[X]] možnost pozdější opravy
[[X]] lokální omezení korekce
[[ ]] automatická změna rozlišení
[[ ]] trvalé smazání pixelů

## Nedestruktivní workflow

Adjustment layer uchovává parametrickou [[korekci]]. Smart object pomáhá chránit zdroj při transformacích a některých filtrech. RAW editory často ukládají recept úprav a původní data nemění.

Editovat obraz tedy nemusí znamenat přepisovat původní [[pixely]].

## Histogram, filtry a AI

Histogram zobrazuje rozložení tónových hodnot. Nahromadění hodnot na krajích může signalizovat [[clipping]]. Levels nastavují černý a bílý bod, Curves umožňují pružnější mapování tónů.

Doostření zvyšuje lokální kontrast hran; neobjevuje skutečný detail, který v obrazu není. Generativní AI může syntetizovat nový [[obsah]], proto je nutné odlišovat korekci od tvorby nové informace.
