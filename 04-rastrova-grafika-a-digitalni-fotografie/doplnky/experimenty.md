<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Rastrová grafika a digitální fotografie

> **⚠️ Upozornění k nástrojům a bezpečnosti**
>
> Teoretické principy navazují na studijní materiál. Konkrétní aplikace, odkazy a pracovní postupy jsou externím praktickým doplněním; jejich rozhraní se mohou měnit. Pracujte pouze s vlastními soubory, neosobními testovacími daty a veřejnými výukovými službami. Neobcházejte omezení cizích systémů, nesdílejte hesla, tokeny, osobní údaje ani licencovaný obsah.

## Jak pracovat v laboratoři

> **🗂️ Před každým experimentem**
>
> Připravte si pracovní zápis se čtyřmi poli: **předpověď**, **postup**, **pozorování**, **vysvětlení**. Rozdíl mezi předpovědí a výsledkem není chyba; je to příležitost ověřit, kde byla původní představa neúplná.

> **🧰 Jak číst bloky v této lekci**
>
> - **💡 Koncept / 🎯 Cíl** říká, jaký princip dokazujete.
> - **🧰 Nástroj** uvádí prostředí, jehož ovládání je jen prostředek, ne cíl.
> - **🧭 Postup** provádějte pomalu a zapisujte si viditelné změny.
> - **🔎 Ověření a interpretace** promění klikání v důkaz a vysvětlení.

> **📝 Šablona zápisu do laboratorního deníku**
>
> Tento blok zkopírujte pod každý vypracovaný experiment a doplňte jej vlastním obsahem.

```text
Předpověď:
Pozorování / důkaz:
Vysvětlení pojmem z kapitoly:
Omezení nebo zdroj možné chyby:
```

> „Pozorování není vysvětlení; vysvětlení spojuje důkaz s principem.“
>
> — laboratorní zásada pro tuto lekci


Tento dokument obsahuje praktické experimenty a úlohy pro hlubší pochopení principů rastrové grafiky a digitální fotografie. Nástroje využívají bezplatný software a webové aplikace.

---

## 1. Rastrový obraz: svět složený z pixelů

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 1.1: Zkoumání mřížky pixelů a interpolace

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Photopea](https://www.photopea.com/) (online)
> **Postup**: Otevři libovolnou detailní fotografii. Začni obraz přibližovat (zoomovat) pomocí nástroje lupa, dokud se obraz nerozpadne na pravidelnou mřížku barevných čtverečků. Tento experiment vizuálně dokazuje, že rastrový obraz má konečný počet vzorků a je tvořen diskrétní mřížkou.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Pixel Art jako esence rastru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Piskel](https://www.piskelapp.com/) (online)
> **Postup**: Vytvoř nové plátno o velikosti pouhých 16x16 pixelů. Nakresli jednoduchý symbol (např. smajlíka) tím, že každému jednotlivému pixelu přiřadíš konkrétní barvu. To demonstruje absolutní základ rastrové grafiky, která nedefinuje objekty matematicky, ale obarvuje pozice v mřížce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Vliv PPI na fyzický tisk

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DPI / PPI Calculator](https://www.dpicalculator.com/) (online)
> **Postup**: Zadej rozměry obrazu 1920 × 1080 px. Změň hodnotu PPI na 72 a podívej se na výslednou fyzickou velikost v centimetrech. Poté změň PPI na 300. Uvidíš, že pixelové rozměry zůstaly stejné, ale obraz by se na papír vytiskl mnohem menší, protože vzorky jsou k sobě nahuštěny.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Ořez (Crop) vs. Změna velikosti (Resize)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Paint.NET](https://www.getpaint.net/) (Windows) nebo Photopea
> **Postup**: Otevři fotografii. Nejprve použij nástroj *Ořez* na střed fotografie a zkontroluj počet pixelů – kvalita zbylých pixelů se nezměnila, jen jich je méně. Krok vrať a použij funkci *Změna velikosti obrazu* na 50 %. Nyní se musely hodnoty pixelů matematicky přepočítat (resampling).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Jak funguje 8bitový RGB zápis

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [HexEd.it](https://hexed.it/) (online)
> **Postup**: Vytvoř v Malování (Windows) obrázek 2x2 pixely, vybarvi je červeně, ulož jako 24bitové BMP bez komprese a nahraj do HexEd.it. V surových datech uvidíš přesně se opakující číselné hexadecimální hodnoty (např. FF 00 00), což dokazuje, že každý pixel je složen ze tří barevných kanálů, z nichž každý má 256 úrovní.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Průhlednost a Alfa kanál v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Photopea](https://www.photopea.com/) (online)
> **Postup**: Vytvoř nový soubor s průhledným pozadím. Nakresli černý kruh a v panelu vrstev mu sniž "Krytí" (Opacity) na 50 %. Přes něj nakresli červený pruh. Uvidíš, jak alfa kanál matematicky řídí, nakolik je podkladový obraz viditelný přes horní vrstvu.

---


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Rastrový obraz: svět složený z pixelů“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Obrazové formáty, velikost a komprese

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 2.1: Hledání kompresních artefaktů JPEGu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Squoosh.app](https://squoosh.app/) (online)
> **Postup**: Nahraj detailní a ostrou fotografii. Vpravo zvol formát JPEG a sniž kvalitu pod 10 %. Pomocí dělící čáry porovnej originál a komprimovanou verzi. Jasně uvidíš blokování, kroužkování kolem hran a ztrátu jemných textur.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Omezení 8bitové palety formátu GIF

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Ezgif](https://ezgif.com/) (online)
> **Postup**: Nahraj plnobarevnou fotografii (např. krajinu s plynulým přechodem oblohy) do konvertoru JPG to GIF. Výsledný obrázek bude mít rozbité přechody (tzv. banding), protože GIF dokáže uložit maximálně 256 barev a dochází k výrazné ztrátě barevné informace.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Bezeztrátová komprese PNG v akci

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [TinyPNG](https://tinypng.com/) (online)
> **Postup**: Udělej klasický screenshot textu na obrazovce (uloží se jako PNG). Nahraj ho na TinyPNG. Nástroj soubor zmenší často i o 70 %, aniž by došlo k rozmazání hran písmen. Formát PNG se snaží zachovat každý pixel přesně, ale chytrá algoritmizace dat jej umí efektivně zmenšit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: s resamplováním a interpolací

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [FastStone Image Viewer](https://www.faststone.org/) (Windows)
> **Postup**: Otevři malou ikonku nebo pixel art (např. 64x64 px). Dej změnit velikost (Resize) na 500x500 px. Nejprve použij filtr *Bilinear* – obraz bude rozmazaný, protože algoritmus tvoří plynulé přechody. Poté krok vrať a použij *Nearest neighbour* – zvětšený obraz bude mít tvrdé a ostré hrany přesně kopírující původní body.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Dávková konverze a datový objem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [XnConvert](https://www.xnview.com/en/xnconvert/) (Windows/macOS)
> **Postup**: Nahraj velký nekomprimovaný soubor (např. TIFF) s fotkou. V záložce Výstup nastav generování 3 kopií: jednu jako JPEG, druhou jako WebP a třetí jako AVIF. Porovnej velikosti vzniklých souborů na disku. WebP a AVIF často nabídnou mnohem lepší poměr kvality a velikosti.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Čtení skrytých technických struktur souboru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Jeffrey's Image Metadata Viewer](http://exif.regex.info/exif.cgi) (online)
> **Postup**: Nahraj běžnou fotografii pořízenou fotoaparátem. Nástroj ti ukáže, že obrazový formát definuje nejen jak uložit pixely, ale slouží jako kontejner pro hlavičky, kompresní matice, a desítky dalších datových polí.

---


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Obrazové formáty, velikost a komprese“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Barva: od lidského oka k číslům v počítači

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 3.1: Aditivní skládání světla v RGB

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Colorizer.org](http://colorizer.org/) (online)
> **Postup**: V panelu RGB nastav všechny tři hodnoty (červená, zelená, modrá) na hodnotu 0, čímž získáš absolutní černou (tmu). Následně nastav všechny tři kanály na 255. Získáš čistě bílou. Když nastavíš všechny na stejnou hodnotu, např. 128, dostaneš neutrální šedou.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Intuitivní vnímání barev pomocí modelu HSL

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Colorizer.org](http://colorizer.org/) (online)
> **Postup**: Vyber si libovolnou barvu pomocí RGB posuvníků. Následně přejdi k posuvníkům HSL (Hue, Saturation, Lightness). Zkus změnit pouze H (odstín), aniž bys změnil sytost nebo jas. Zjistíš, že model HSL je pro člověka mnohem intuitivnější na ovládání než skládání červeného, zeleného a modrého světla v RGB.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Test barvosleposti a designové přístupnosti

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) (online)
> **Postup**: Vytvoř jednoduchou grafiku s červeným a zeleným textem (např. CHYBA a SPRÁVNĚ). Nahraj ji do simulátoru a zapni "Deuteranopia" (nejčastější porucha vnímání zelené). Zjistíš, že obě barvy splynou. Toto dokazuje, že barva by nikdy neměla být jediným nositelem významu v informační grafice.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Ztráta barev mimo tiskový gamut CMYK

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [RGB2CMYK.org](https://www.rgb2cmyk.org/) (online)
> **Postup**: Vezmi fotografii s extrémně zářivými, neónovými barvami (svítivě modrá nebo zelená). Proveď konverzi do CMYKu. Vizuálně porovnej oba soubory. Svítivé barvy výrazně "pohasnou", protože CMYK je subtraktivní model s menším rozsahem a leží mimo jeho gamut.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Oční test kalibrace monitoru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Lagom LCD Monitor Test](http://www.lagom.nl/lcd-test/) (online)
> **Postup**: Přejdi na test "Black level" (Úroveň černé) a "White saturation" (Saturace bílé). Postupuj podle pokynů a zjisti, zda tvůj monitor neslévá nejtmavší a nejsvětlejší stíny do jedné barvy. Cílem profilace a kalibrace je dosáhnout reprodukovatelného chování zařízení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Pitva barev na obrazovce

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Microsoft PowerToys - Color Picker](https://learn.microsoft.com/en-us/windows/powertoys/color-picker) (Windows)
> **Postup**: Po instalaci aktivuj kapátko (Win+Shift+C). Najeď myší na jakoukoliv barvu ve tvém operačním systému (ikonku, web). Nástroj ti okamžitě ukáže její RGB reprezentaci, což dokazuje, že barva v počítači je pouze modelovaná číselná reprezentace.

---


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Barva: od lidského oka k číslům v počítači“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Rastrový editor a nedestruktivní práce s obrazem

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 4.1: Pochopení režimů prolnutí (Blend Modes)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Pixlr E](https://pixlr.com/e/) (online)
> **Postup**: Nahraj fotografii na vrstvu 1. Vytvoř nad ní vrstvu 2 a vyplň ji plynulým černobílým přechodem. U horní vrstvy změň režim prolnutí na *Multiply* (Násobit) – všimni si, že bílá barva z vrstvy 2 zmizí a černá obraz ztmaví. Změň na *Screen* (Závoj) – černá zmizí a bílá obraz přesvětlí. Režim prolnutí je matematická operace nad hodnotami pixelů obou vrstev.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Skrývání pixelů pomocí masek vrstev

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Pixlr E](https://pixlr.com/e/) (online)
> **Postup**: Umísti dvě různé fotografie na dvě vrstvy nad sebou. Horní vrstvě přidej *Masku vrstvy*. Vezmi měkký štětec s černou barvou a maluj do masky. Pixely horní vrstvy začnou mizet. Přepni na bílou barvu a maluj znovu – pixely se vrátí. To dokazuje, že maska pixely nemaže, ale pouze řídí míru jejich viditelnosti.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Nedestruktivní korekční vrstvy (Adjustment Layers)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Photopea](https://www.photopea.com/) (online)
> **Postup**: Otevři snímek a nepřepisuj jej přímo. V panelu vrstev přidej novou korekční vrstvu "Křivky" (Curves) nebo "Odstín a Sytost". Uprav hodnoty. Tuto vrstvu můžeš kdykoliv skrýt, smazat nebo změnit její intenzitu, čímž edituješ obraz pouze jako "recept na zobrazení", nikoliv destrukcí původních dat.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Analýza histogramu a clippingu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Photopea](https://www.photopea.com/) (online) nebo ImageJ
> **Postup**: Otevři fotografii a zapni zobrazení Histogramu. Vytvoř korekční vrstvu "Úrovně" (Levels) a extrémně posuň bílý bod doleva. Na histogramu uvidíš "clipping světel" – obrovská masa pixelů se natlačí na pravý okraj grafu a ve fotografii se velké plochy slijí do čisté bílé barvy bez jakéhokoliv detailu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: AI automatická segmentace objektu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [remove.bg](https://www.remove.bg/) (online)
> **Postup**: Nahraj portrétní fotografii se složitým pozadím. AI systém během pár sekund odhadne obrysy člověka a pozadí zprůhlední. Dřívější nástroje jako kouzelná hůlka pracovaly s podobností barvy, dnešní AI umí rozeznat kontext jako "člověk" nebo "vlasy".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Klonování vs. AI Syntéza textury

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Cleanup.pictures](https://cleanup.pictures/) (online)
> **Postup**: Nahraj fotografii s překážejícím objektem (např. pták na obloze). Nástroj zamaluj přes objekt. Na rozdíl od starého klonovacího razítka (které jen kopírovalo pixely odjinud), umělá inteligence zde analyzuje okolí a vytváří pravděpodobnou texturu – dochází k syntéze nového obsahu.

---


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Rastrový editor a nedestruktivní práce s obrazem“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Digitální fotoaparát: jak se světlo mění na data

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 5.1: Trénink expozičního trojúhelníku

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [CameraSim](https://camerasim.com/) (online)
> **Postup**: Spusť simulaci zrcadlovky. Nastav velmi krátký čas závěrky (např. 1/1000 s). Fotografie ztmavne. Zvyš ISO, aby se obraz znovu prosvětlil. Výsledek bude jasný, ale plný šumu. ISO do fotoaparátu totiž fyzicky nepřidalo další světlo, pouze zesílilo původní slabý signál.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Vliv clony na hloubku ostrosti

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DOF Simulator](https://dofsimulator.net/) (online)
> **Postup**: V simulátoru nastav clonu na f/1.8. Uvidíš, že postava je ostrá, ale pozadí se silně rozmaže (menší hloubka ostrosti). Poté clonu přivři na f/11. Pozadí se zaostří. Clona reguluje otvor pro světlo a zároveň zásadně ovlivňuje hloubku ostrosti.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Výpočet crop faktoru objektivu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [mmcalc.com](https://mmcalc.com/) (online)
> **Postup**: Zadej ohniskovou vzdálenost 50 mm pro "Full Frame" senzor. Poté totéž ohnisko zadej pro malý senzor APS-C. Úhel záběru na menším snímači bude mnohem užší, jako bys použil teleobjektiv (tzv. ekvivalentní ohnisková vzdálenost).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Laboratorní dynamický rozsah snímačů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [PhotonsToPhotos](https://www.photonstophotos.net/) (online)
> **Postup**: Přejdi na grafy "Photographic Dynamic Range". Porovnej moderní velký Full Frame fotoaparát s kompaktem. Rozdíl mezi nejslabším a nejsilnějším signálem, který systém dokáže zachytit (dynamický rozsah), bude zásadně odlišný.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Extrakce hloubkové mapy (Depth Map)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Depthy](https://depthy.me/) (online)
> **Postup**: Vyfoť na moderním mobilním telefonu fotografii v "Portrétním režimu" (kdy telefon synteticky rozmaže pozadí) a nahraj ji na tuto stránku. Depthy extrahuje skrytou hloubkovou mapu, což je ukázkou výpočetní fotografie (computational photography) – obraz nevznikl jen optikou, ale odhadem umělé inteligence.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Pohled na skutečná surová data (Demosaicing)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DCRaw](https://www.cybercom.net/~dcoffin/dcraw/) (Příkazová řádka) nebo ImageGlass (Windows)
> **Postup**: Pokus se zobrazit neupravený .CR2 nebo .NEF formát přímo přes utilitu čtoucí Bayerovu masku bez demosaicingu. Uvidíš zrnitý, šedivý vzor, protože fotosenzory samotné zachycují pouze množství fotonů (jas) pro červenou, zelenou či modrou. Teprve software z nich výpočtem vytvoří RGB mřížku (demosaicing).

---


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Digitální fotoaparát: jak se světlo mění na data“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Zpracování, publikace a důvěryhodnost

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 6.1: Vyvážení bílé (White Balance) nad RAWem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [RawTherapee](https://rawtherapee.com/) (Windows/macOS)
> **Postup**: Otevři RAW soubor fotografovaný s teplým žárovkovým světlem. V modulu vyvážení bílé posuň teplotu v Kelvinech dolů, čímž obraz ochladíš a zneutralizuješ. Na RAW datech tato operace funguje bez destrukce, protože původní měření senzorů z fotoaparátu zůstalo zachováno.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Těžba EXIF metadat

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Pic2Map](https://www.pic2map.com/) (online) nebo ExifTool
> **Postup**: Nahraj neupravenou fotografii pořízenou chytrým telefonem ze své dovolené. Nástroj ze souboru přečte čas pořízení, model fotoaparátu a v mnoha případech rovnou vykreslí přesné GPS souřadnice do mapy. Dokazuje to, že metadata mají svou odvrácenou stranu týkající se soukromí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Záchrana stínů a práce s dynamickým rozsahem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [RawTherapee](https://rawtherapee.com/) (Windows/macOS) nebo Photopea
> **Postup**: Vezmi RAW snímek s velmi tmavými stíny. V nástrojích pro tónové mapování vytáhni expozici stínů silně nahoru. Zjistíš, že RAW uchovává větší tónovou rezervu a detaily vystoupí ze tmy. Zároveň si ale všimneš, že razantní vytahování stínů výrazně zvýrazní šum.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Zjišťování důvěryhodnosti a digitální forenzní analýza

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Forensically](https://29a.ch/photo-forensics/) (online)
> **Postup**: Nahraj fotografii, ve které jsi klonovacím razítkem něco zamaskoval. Zapni nástroje jako "Clone Detection" nebo "Error Level Analysis". Nástroj se pokusí vizualizovat anomálie v šumu a detekovat manipulaci, i když na první pohled fotografie působí realisticky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Standard C2PA a ověřování historie

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Verify - Content Credentials](https://contentcredentials.org/verify) (online)
> **Postup**: Nahraj fotografii vygenerovanou moderní AI službou nebo upravenou novým Photoshopem s vloženými C2PA daty. Nástroj ze souboru přečte kryptograficky ověřitelné informace o tom, kdy a kým byl snímek vytvořen nebo upraven. 


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Hledání kompromisu pro webový export

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Caesium Image Compressor](https://saerasoft.com/caesium) (Windows)
> **Postup**: Otevři fotografii, kterou chceš připravit pro web. Změň její kompresní úroveň na 60 % a podívej se na náhled a datovou velikost (z megabajtů na stovky kilobajtů). Export pro web nespočívá v nesmyslném údaji 72 DPI, ale ve vhodném zmenšení rozměrů a dostatečně silné kompresi, která soubor zmenší za přijatelné vizuální ztráty.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Zpracování, publikace a důvěryhodnost“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
