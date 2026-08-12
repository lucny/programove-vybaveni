<!--
title: Postprodukce, export a distribuce – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je NLE?**

<!-- data-randomize="true" -->
[(X)] Non-Linear Editor.
[( )] Network Live Encoder.
[( )] New Layer Export.
[( )] Non-Lossy Engine.

---

**2. Co znamená nedestruktivní střih videa?**

<!-- data-randomize="true" -->
[(X)] Projekt ukládá rozhodnutí a zdrojové klipy obvykle zůstávají nezměněné.
[( )] Každý střih přepisuje originál.
[( )] Zdroj lze po importu smazat.
[( )] Video se vždy převede na proxy.

---

**3. Co je proxy?**

<!-- data-randomize="true" -->
[(X)] Lehčí pracovní kopie náročného zdrojového videa.
[( )] Finální master.
[( )] Titulkový soubor.
[( )] Barevný profil.

---

**4. Jaký je rozdíl mezi color correction a color grading?**

<!-- data-randomize="true" -->
[(X)] Korekce sjednocuje a opravuje, grading vytváří styl a náladu.
[( )] Jde o totéž.
[( )] Grading je pouze komprese.
[( )] Korekce mění fps.

---

**5. Co je chroma key?**

<!-- data-randomize="true" -->
[(X)] Nahrazení vybrané barvy pozadí jiným obrazem.
[( )] Převod 4:2:0 na 4:4:4 bez ztráty.
[( )] Titulkování.
[( )] Komprese zvuku.

---

**6. Proč není LUT univerzální opravný filtr?**

<!-- data-randomize="true" -->
[(X)] Je to převodní nebo tvůrčí tabulka a nemůže zachránit libovolně špatný zdroj.
[( )] LUT se používá jen pro zvuk.
[( )] Nepracuje s barvami.
[( )] Vždy zvyšuje rozlišení.

---

**7. Co je vhodné zachovat jako dlouhodobý master?**

<!-- data-randomize="true" -->
[(X)] Kvalitní výstup s dostatečnou rezervou, ne jen webovou silně komprimovanou kopii.
[( )] Pouze nejmenší MP4.
[( )] Jen proxy.
[( )] Pouze projekt bez médií.

---

**8. Co je adaptivní streaming?**

<!-- data-randomize="true" -->
[(X)] Přehrávač za běhu volí vhodnou kvalitu podle podmínek.
[( )] Vždy posílá jediný původní soubor.
[( )] Přenáší pouze zvuk.
[( )] Je synonymem RTMP.

---

**9. Které technologie kapitola spojuje s distribucí videa přes HTTP?**

<!-- data-randomize="true" -->
[[X]] HLS
[[X]] MPEG-DASH
[[X]] CDN
[[X]] buffer
[[ ]] BIOS

---

**10. Co patří k přístupnému a archivovatelnému video projektu?**

<!-- data-randomize="true" -->
[[X]] titulky
[[X]] případný audiopopis
[[X]] licenční evidence
[[X]] zdrojové záběry a projekt
[[X]] oddělená záloha
[[ ]] pouze synchronizovaná složka


# 2. Interaktivní shrnutí kapitoly

## Nelineární střih

NLE ukládá střihová rozhodnutí a původní média obvykle nemění. Projekt proto není totéž co samotné [[zdrojové soubory]]. Pokud je přesuneme nebo smažeme, editor je nemusí najít.

Proxy je lehčí pracovní náhrada, která usnadňuje plynulý střih; finální export se vrací k plné [[kvalitě]].

## Obraz a zvuk

Barevná korekce nejprve sjednotí záběry, grading potom vytváří styl. Histogram, waveform a [[vectorscope]] pomáhají kontrolovat obraz objektivněji než náhodně nastavený monitor.

Chroma key vyžaduje kvalitně natočené a rovnoměrně osvětlené pozadí.

## Export

Export se řídí cílem, ne nejvyšším číslem. Z 1080p zdroje nevznikne pouhým exportem do 4K skutečný nový [[detail]]. Podobně převod 25 fps na 60 fps vyžaduje opakování nebo odhad snímků.

**Před odevzdáním zkontroluj:**

<!-- data-randomize="true" -->
[[X]] synchronizaci zvuku
[[X]] titulky
[[X]] barevnost a hlasitost
[[X]] začátek a konec
[[X]] skutečně vyexportovaný soubor
[[ ]] pouze hlášku „export dokončen“

## Streaming a archivace

Platforma může vytvořit více variant a používat adaptivní [[streaming]] pomocí HLS nebo MPEG-DASH. RTMP se často používá jako vstup živého streamu k serveru.

Archiv má uchovat zdroje, projekt, master, licence a oddělenou [[zálohu]]. Synchronizace sama o sobě zálohu nenahrazuje.
