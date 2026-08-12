<!--
title: Komprese, kodeky a kontejnery – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč je nekomprimované video datově náročné?**

<!-- data-randomize="true" -->
[(X)] Každý snímek obsahuje miliony pixelů a snímků je mnoho za sekundu.
[( )] Video neumí používat binární data.
[( )] Zvuk vždy zabírá většinu souboru.
[( )] Kontejner zdvojnásobuje každý snímek.

---

**2. Co je kodek?**

<!-- data-randomize="true" -->
[(X)] Metoda a realizace pro kódování a dekódování média.
[( )] Pouze přípona souboru.
[( )] Kontejner pro titulky.
[( )] Typ monitoru.

---

**3. Co je intraframe komprese?**

<!-- data-randomize="true" -->
[(X)] Každý snímek se zpracovává převážně samostatně.
[( )] Ukládají se jen změny mezi snímky.
[( )] Komprimuje pouze zvuk.
[( )] Je vždy bezeztrátová.

---

**4. Co je interframe komprese?**

<!-- data-randomize="true" -->
[(X)] Využívá podobnost mezi snímky v čase.
[( )] Komprimuje každý snímek bez vztahu k okolí.
[( )] Nemůže používat klíčové snímky.
[( )] Je určena pouze pro fotografie.

---

**5. Co je GOP?**

<!-- data-randomize="true" -->
[(X)] Group of Pictures.
[( )] Graphic Output Profile.
[( )] General Optical Pixel.
[( )] Global Overlay Package.

---

**6. Co udává bitrate videa?**

<!-- data-randomize="true" -->
[(X)] Množství dat za sekundu.
[( )] Počet pixelů.
[( )] Poměr stran.
[( )] Počet barevných kanálů.

---

**7. Co je VBR?**

<!-- data-randomize="true" -->
[(X)] Proměnný datový tok podle složitosti scény.
[( )] Pevný datový tok.
[( )] Proměnná snímková frekvence jako jediný význam.
[( )] Bezeztrátový kodek.

---

**8. Které video kodeky kapitola uvádí?**

<!-- data-randomize="true" -->
[[X]] H.264/AVC
[[X]] HEVC/H.265
[[X]] VP9
[[X]] AV1
[[ ]] MP4

---

**9. Co je multimediální kontejner?**

<!-- data-randomize="true" -->
[(X)] Obálka organizující video, audio, titulky a metadata.
[( )] Algoritmus komprese obrazu.
[( )] Pouze zvuková stopa.
[( )] Barevný prostor.

---

**10. Proč dva soubory `.mp4` nemusí přehrát stejné zařízení?**

<!-- data-randomize="true" -->
[(X)] Mohou obsahovat různé kodeky uvnitř stejného kontejneru.
[( )] MP4 nemá žádnou specifikaci.
[( )] Přípona vždy určuje zařízení.
[( )] Jeden musí být analogový.


# 2. Interaktivní shrnutí kapitoly

## Proč komprimujeme

Nekomprimované video produkuje obrovský datový tok. Komprese využívá podobnost pixelů v jednom snímku i podobnost mezi sousedními [[snímky]].

Kodek určuje, jak se médium kóduje a dekóduje. Ztrátová komprese část informace odstraní ve prospěch menšího [[datového toku]].

## Intraframe a interframe

Intraframe komprese zpracovává snímky převážně samostatně a bývá příjemnější pro střih. Interframe komprese používá referenční snímky a odhad [[pohybu]]. Skupina souvisejících snímků se nazývá GOP.

Jemný chaotický pohyb jako déšť nebo konfety je pro interframe kompresi náročný.

## Bitrate a kodeky

Velikost lze orientačně odhadnout jako `bitrate × čas / 8`. CBR drží tok přibližně konstantní, [[VBR]] ho rozděluje podle složitosti.

H.264 nabízí velmi širokou kompatibilitu, HEVC vyšší účinnost, VP9 webové použití a [[AV1]] moderní otevřenou distribuci.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] novější kodek může být účinnější, ale hůře podporovaný
[[X]] opakované ztrátové překódování může zhoršovat obraz
[[X]] bitrate se musí hodnotit spolu s kodekem a obsahem
[[ ]] nejvyšší rozlišení vždy znamená nejlepší kvalitu při stejném toku

## Kontejner

MP4, MKV, WebM nebo MOV jsou [[kontejnery]]. Jeden MP4 může obsahovat H.264, jiný HEVC. Diagnostika proto musí rozlišovat kontejner a [[kodek]] jednotlivých stop.
