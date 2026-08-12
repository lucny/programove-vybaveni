<!--
title: Virtuální, rozšířená a smíšená realita – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co označuje XR?**

<!-- data-randomize="true" -->
[(X)] Zastřešující rodinu VR, AR a MR.
[( )] Pouze virtuální realitu.
[( )] Typ grafického formátu.
[( )] Metodu ray tracingu.

---

**2. Co je typické pro VR?**

<!-- data-randomize="true" -->
[(X)] Nahrazuje většinu běžného vizuálního vjemu digitálním prostředím.
[( )] Vždy pouze přidá malý objekt do reálného obrazu.
[( )] Nepoužívá stereoskopii.
[( )] Nemůže zobrazit reálné místo.

---

**3. Co je typické pro AR?**

<!-- data-randomize="true" -->
[(X)] Přidává digitální obsah k pohledu na reálné prostředí.
[( )] Vždy zcela nahrazuje okolní svět.
[( )] Nepotřebuje tracking.
[( )] Je totéž co 360° video.

---

**4. Co zdůrazňuje mixed reality?**

<!-- data-randomize="true" -->
[(X)] Prostorové ukotvení digitálních objektů a jejich vztah k reálnému prostředí.
[( )] Pouze vyšší rozlišení displeje.
[( )] Výhradně použití gamepadu.
[( )] Zákaz passthrough kamer.

---

**5. Co je stereoskopická disparita?**

<!-- data-randomize="true" -->
[(X)] Rozdíl obrazů pro levé a pravé oko podporující vjem hloubky.
[( )] Kolísání snímkové frekvence.
[( )] Chyba trackingu.
[( )] Barevná odchylka čočky.

---

**6. Co sleduje 3DoF?**

<!-- data-randomize="true" -->
[(X)] Tři rotační stupně volnosti.
[( )] Tři translační osy bez rotace.
[( )] Polohu očí a rukou.
[( )] Šest os pohybu.

---

**7. Co přidává 6DoF oproti 3DoF?**

<!-- data-randomize="true" -->
[(X)] Tři translační osy polohy.
[( )] Tři další barevné kanály.
[( )] Vyšší refresh rate.
[( )] Další tři kamery jako nutnou podmínku.

---

**8. Co je SLAM?**

<!-- data-randomize="true" -->
[(X)] Současná lokalizace zařízení a mapování okolí.
[( )] Metoda komprese stereoskopického videa.
[( )] Typ PBR materiálu.
[( )] Animace rukou pomocí keyframů.

---

**9. Které způsoby interakce mohou XR systémy používat?**

<!-- data-randomize="true" -->
[[X]] tracked controllers
[[X]] hand tracking
[[X]] eye tracking
[[X]] hlas
[[X]] haptiku
[[ ]] pouze klávesnici

---

**10. Proč je nízká motion-to-photon latency důležitá?**

<!-- data-randomize="true" -->
[(X)] Snižuje nesoulad mezi pohybem hlavy a obrazem a omezuje nevolnost.
[( )] Zvyšuje počet polygonů modelu.
[( )] Určuje velikost gamutu.
[( )] Nahrazuje tracking.


# 2. Interaktivní shrnutí kapitoly

## XR, VR, AR a MR

[[XR]] je společný pojem pro VR, AR a MR. VR nahrazuje většinu pohledu digitálním prostředím, AR přidává digitální prvky do reality a mixed reality zdůrazňuje jejich prostorové [[ukotvení]] a reakci na okolí.

Moderní passthrough headset může mezi těmito režimy plynule přecházet.

## Headset a stereoskopie

Headset používá displeje, optiku a senzory. Každé oko dostává mírně jiný obraz, což vytváří stereoskopickou [[disparitu]]. Důležité jsou rozlišení, field of view, refresh rate a motion-to-photon latency.

Pixels per degree lépe než samotné rozlišení vyjadřuje hustotu pixelů v části [[zorného]] pole.

## Tracking

3DoF sleduje pitch, yaw a [[roll]]. 6DoF přidává polohu v osách x, y a z.

Inside-out tracking používá kamery na headsetu a inerciální senzory. [[SLAM]] současně odhaduje polohu zařízení a vytváří mapu prostředí.

**Vyber prvky, které může AR systém detekovat:**

<!-- data-randomize="true" -->
[[X]] roviny
[[X]] stěny
[[X]] podlahu
[[X]] prostorové body
[[ ]] pouze vytištěné QR kódy jako jedinou možnost

## Interakce a komfort

XR může používat ovladače, hand tracking, eye tracking, hlas a [[haptiku]]. Eye tracking lze využít pro foveated rendering, který soustředí výpočetní kvalitu do oblasti pohledu.

Vysoká latence nebo nízká a nestabilní obnovovací frekvence může zvyšovat [[cybersickness]]. Systém proto musí reagovat na pohyb hlavy velmi rychle.

## Vývojové platformy

VR a AR aplikace se vyvíjejí například v Unity nebo Unreal Engine. [[OpenXR]] poskytuje otevřený standard pro komunikaci aplikací s XR zařízeními, WebXR přináší XR do webového prostředí a A-Frame zjednodušuje tvorbu webových 3D/XR scén.

Hlavním technickým úkolem XR není jen vykreslit 3D model, ale propojit stereoskopii, tracking, prostorové mapování a interakci v reálném [[čase]].
