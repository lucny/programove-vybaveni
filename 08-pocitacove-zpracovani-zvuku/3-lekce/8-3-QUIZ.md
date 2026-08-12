<!--
title: Audio soubory, komprese a psychoakustika – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je WAV?**

<!-- data-randomize="true" -->
[(X)] Kontejner, který často obsahuje nekomprimované PCM audio.
[( )] Vždy ztrátový kodek.
[( )] Výhradně MIDI formát.
[( )] Bezeztrátový kodek identický s FLAC.

---

**2. Co je FLAC?**

<!-- data-randomize="true" -->
[(X)] Bezeztrátově komprimovaný audio formát.
[( )] Ztrátový kodek.
[( )] Pouze kontejner bez komprese.
[( )] MIDI protokol.

---

**3. Co je MP3?**

<!-- data-randomize="true" -->
[(X)] Ztrátový audio kodek/formát využívající psychoakustiku.
[( )] Bezeztrátová archivní komprese.
[( )] Nekomprimované PCM.
[( )] Pouze stereo kontejner.

---

**4. Co je frekvenční maskování?**

<!-- data-randomize="true" -->
[(X)] Silná složka může ztížit vnímání blízké slabší složky.
[( )] Odstranění všech vysokých frekvencí.
[( )] Změna panoramy.
[( )] Kvantizace v čase.

---

**5. Co je časové maskování?**

<!-- data-randomize="true" -->
[(X)] Silný impuls ovlivní vnímání slabších zvuků těsně před nebo po něm.
[( )] Zvuk se maskuje po celou nahrávku.
[( )] Pouze změna sample rate.
[( )] Stereo zpoždění.

---

**6. Co udává bitrate?**

<!-- data-randomize="true" -->
[(X)] Množství dat připadajících na jednotku času.
[( )] Počet bitů jednoho PCM vzorku.
[( )] Počet kanálů.
[( )] Frekvenci tónu.

---

**7. Co je VBR?**

<!-- data-randomize="true" -->
[(X)] Proměnný datový tok podle složitosti obsahu.
[( )] Pevný datový tok.
[( )] Proměnná bitová hloubka mikrofonu.
[( )] Typ HRTF.

---

**8. Které kodeky kapitola uvádí jako modernější alternativy k MP3?**

<!-- data-randomize="true" -->
[[X]] AAC
[[X]] Opus
[[ ]] PNG
[[ ]] MIDI

---

**9. Co je HRTF?**

<!-- data-randomize="true" -->
[(X)] Model směrových změn zvuku způsobených hlavou a ušima.
[( )] Metoda bezeztrátové komprese.
[( )] Bitová hloubka.
[( )] Audio konektor.

---

**10. Co je objektové audio?**

<!-- data-randomize="true" -->
[(X)] Zvukové objekty nesou informaci o poloze a systém je rozmístí podle sestavy.
[( )] Každý zvuk je pevně uložen jen v levém kanálu.
[( )] Mono nahrávka.
[( )] Výhradně analogový formát.


# 2. Interaktivní shrnutí kapitoly

## Tři strategie

WAV často uchovává nekomprimované [[PCM]] a je vhodný jako pracovní formát. FLAC komprimuje bezeztrátově a po rozbalení vrátí původní data. MP3 používá [[ztrátovou]] kompresi.

Volba tedy závisí na prioritě: editace, archiv nebo distribuce.

## Psychoakustika

MP3 není obyčejný ZIP. Využívá frekvenční a časové [[maskování]], tedy vlastnosti lidského sluchu. Kodek hledá části, u nichž může snížit přesnost s co nejmenším slyšitelným dopadem.

Příliš silná komprese vede k artefaktům, například kovovým výškám nebo rozmazaným [[transientům]].

## Bitrate

Bitrate vyjadřuje datový tok. CBR jej drží přibližně konstantní, zatímco [[VBR]] přiděluje složitým částem více dat.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] vyšší bitrate obvykle dovoluje zachovat více detailů
[[X]] výsledek závisí také na kodeku a obsahu
[[X]] Opus může být při nízkých tocích účinnější než starší MP3
[[ ]] stejný bitrate znamená vždy stejnou kvalitu u každého kodeku

## Prostorový zvuk

Stereo používá dva kanály. Binaurální audio a [[HRTF]] mohou ve sluchátkách vytvářet prostorový dojem. Objektové audio popisuje zvuk také jeho polohou v [[prostoru]].
