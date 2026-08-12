<!--
title: Od mikrofonu k digitální nahrávce – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co dělá mikrofon?**

<!-- data-randomize="true" -->
[(X)] Převádí změny akustického tlaku na elektrický signál.
[( )] Převádí digitální data přímo na světlo.
[( )] Komprimuje MP3.
[( )] Generuje MIDI události.

---

**2. Které typy mikrofonů kapitola uvádí?**

<!-- data-randomize="true" -->
[[X]] dynamický
[[X]] kondenzátorový
[[X]] páskový
[[ ]] bitmapový

---

**3. Co je typické pro kardioidní mikrofon?**

<!-- data-randomize="true" -->
[(X)] Je nejcitlivější zepředu a méně zezadu.
[( )] Snímá stejně ze všech stran.
[( )] Snímá jen ze stran.
[( )] Nemá membránu.

---

**4. Co je proximity effect?**

<!-- data-randomize="true" -->
[(X)] Zesílení nízkých frekvencí při malém odstupu u některých směrových mikrofonů.
[( )] Digitální clipping.
[( )] Zpoždění zvuku.
[( )] Ztrátová komprese.

---

**5. Co pomáhá omezit plosivy?**

<!-- data-randomize="true" -->
[(X)] Pop filtr nebo mírné natočení mikrofonu mimo osu úst.
[( )] Vyšší bitrate.
[( )] Nižší vzorkovací frekvence.
[( )] Stereo panorama.

---

**6. Co je headroom?**

<!-- data-randomize="true" -->
[(X)] Rezerva pod maximální digitální úrovní.
[( )] Prostor nad mikrofonem.
[( )] Délka místnosti.
[( )] Rozsah frekvencí sluchátek.

---

**7. Co je clipping?**

<!-- data-randomize="true" -->
[(X)] Oříznutí vrcholu signálu po překročení dostupného rozsahu.
[( )] Bezeztrátová komprese.
[( )] Zkrácení souboru bez změny zvuku.
[( )] Stereo efekt.

---

**8. Co může obsahovat audio interface?**

<!-- data-randomize="true" -->
[[X]] mikrofonní předzesilovač
[[X]] A/D převodník
[[X]] D/A převodník
[[X]] sluchátkový výstup
[[ ]] Bayerovu masku

---

**9. Co říká Nyquistův-Shannonův teorém pro vzorkování?**

<!-- data-randomize="true" -->
[(X)] Vzorkovací frekvence musí být vyšší než dvojnásobek nejvyšší zachovávané frekvence.
[( )] Musí se rovnat nejvyšší frekvenci.
[( )] Bitová hloubka musí být 2× vyšší než sample rate.
[( )] Vzorkování nepotřebuje filtr.

---

**10. Proč se používá dither?**

<!-- data-randomize="true" -->
[(X)] Rozptýlí kvantizační zkreslení při snížení bitové hloubky.
[( )] Odstraní clipping.
[( )] Zvýší sample rate.
[( )] Změní mono na stereo.


# 2. Interaktivní shrnutí kapitoly

## Mikrofon a směrovost

Mikrofon převádí akustický tlak na [[elektrický]] signál. Dynamické, kondenzátorové a páskové mikrofony používají různé konstrukční principy.

Polární charakteristika říká, odkud mikrofon poslouchá. Kardioida je citlivá hlavně [[zepředu]], omnidirectional ze všech směrů a figure-eight zepředu i zezadu.

## Praktický záznam

Často více pomůže správná vzdálenost a místnost než dražší technika. Pro hlas je vhodný mikrofon relativně blízko, pop filtr a kontrola ve [[sluchátkách]].

Gain se nastavuje tak, aby nejhlasitější místa nepřekročila maximum. Rezerva se nazývá [[headroom]] a překročení rozsahu vede ke clippingu.

## Digitalizační řetězec

Nahrávání lze shrnout: **zvuk → mikrofon → předzesilovač → [[A/D]] → digitální data**. Při přehrávání probíhá opačný směr přes D/A převod.

Vzorkovací frekvence určuje počet vzorků za sekundu. U 44,1 kHz je Nyquistova frekvence [[22,05]] kHz.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] příliš nízký sample rate může způsobit aliasing
[[X]] anti-aliasing filtr omezuje vysoké frekvence před převodem
[[X]] 24bitový záznam dává větší rezervu než 16bitový
[[ ]] 192 kHz automaticky zaručí lepší mikrofonní záznam

## Bitová hloubka

Bitová hloubka určuje počet kvantizačních úrovní. Při převodu na nižší bitovou hloubku lze použít [[dither]], tedy velmi slabý záměrný šum.
