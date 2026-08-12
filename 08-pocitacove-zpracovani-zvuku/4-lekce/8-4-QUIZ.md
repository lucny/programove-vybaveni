<!--
title: Jak lze zvuk vytvářet v počítači – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je syntéza zvuku?**

<!-- data-randomize="true" -->
[(X)] Vytváření zvukového signálu matematicky nebo algoritmicky.
[( )] Pouze nahrávání mikrofonem.
[( )] Komprese MP3.
[( )] Převod WAV na FLAC.

---

**2. Které základní průběhy může generovat oscilátor?**

<!-- data-randomize="true" -->
[[X]] sinusový
[[X]] obdélníkový
[[X]] pilový
[[ ]] JPEG

---

**3. Co dělá filtr v syntetizátoru?**

<!-- data-randomize="true" -->
[(X)] Tvaruje frekvenční obsah signálu.
[( )] Generuje MIDI Note On.
[( )] Mění souborovou příponu.
[( )] Převádí mono na text.

---

**4. Co je sampling?**

<!-- data-randomize="true" -->
[(X)] Použití nahraných zvukových vzorků jako zdroje nástroje.
[( )] Pouze A/D vzorkování mikrofonu.
[( )] Změna bitratu.
[( )] Databázový dotaz.

---

**5. Co znamená A v ADSR?**

<!-- data-randomize="true" -->
[(X)] Attack.
[( )] Amplitude.
[( )] Audio.
[( )] Average.

---

**6. Co znamená Sustain v ADSR?**

<!-- data-randomize="true" -->
[(X)] Úroveň držená během trvání tónu po attack a decay.
[( )] Doba po uvolnění klávesy.
[( )] Počáteční náběh.
[( )] Frekvence oscilátoru.

---

**7. Co přenáší MIDI?**

<!-- data-randomize="true" -->
[(X)] Hudební a řídicí události, ne výslednou zvukovou vlnu.
[( )] Vždy hotové PCM audio.
[( )] Pouze text písně.
[( )] Video snímky.

---

**8. Co může MIDI Note On obsahovat?**

<!-- data-randomize="true" -->
[(X)] Číslo noty a velocity.
[( )] Vzorkovací frekvenci mikrofonu.
[( )] Kompletní WAV soubor.
[( )] Barevný profil.

---

**9. Co je DAW?**

<!-- data-randomize="true" -->
[(X)] Digital Audio Workstation.
[( )] Digital Analog Wave.
[( )] Dynamic Audio Web.
[( )] Data Arrangement Window.

---

**10. Co může DAW kombinovat?**

<!-- data-randomize="true" -->
[[X]] audio stopy
[[X]] MIDI
[[X]] virtuální nástroje
[[X]] efekty
[[X]] časovou osu
[[ ]] pouze jeden mono soubor


# 2. Interaktivní shrnutí kapitoly

## Syntéza a sampling

Zvuk nemusí vzniknout mikrofonem. [[Syntéza]] jej vytváří algoritmicky, například z oscilátorů generujících sinus, obdélník nebo pilu. Filtry a další moduly mění jeho spektrum a vývoj.

Sampling používá skutečné nahrané [[vzorky]] jako zdroj. Virtuální klavír tak může přehrávat mnoho nahrávek skutečného nástroje.

## ADSR

Obálka [[ADSR]] popisuje vývoj parametru v čase: Attack, Decay, Sustain a Release. Stejný oscilátor může díky jiné obálce působit jako velmi odlišný nástroj.

## MIDI

MIDI neposílá hotový zvuk. Přenáší události typu Note On, Note Off, číslo noty a [[velocity]]. Virtuální nástroj teprve rozhodne, jaký zvuk zazní.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] MIDI dovoluje snadno změnit nástroj
[[X]] MIDI umožňuje upravit tempo nebo výšku not
[[X]] MIDI není výsledná akustická nahrávka
[[ ]] MIDI je vždy WAV

## DAW

[[DAW]] je digitální studio kombinující vícestopý záznam, mix, MIDI sekvencer, efekty a virtuální nástroje. Projekt je časová osa více [[vrstev]], které lze samostatně upravovat.
