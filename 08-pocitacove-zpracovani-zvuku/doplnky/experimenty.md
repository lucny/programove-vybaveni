<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Počítačové zpracování zvuku

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


## 1. Zvuk jako fyzikální a informační jev

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 1.1: Vizualizace mechanického vlnění částic

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Zvuk je mechanické vlnění, při kterém částice kmitají, ale necestují od zdroje k posluchači.
> **Nástroj**: [PhET Interactive Simulations - Sound](https://phet.colorado.edu/en/simulations/waves-intro)
> **Postup**: Otevřete simulaci a přepněte na záložku "Zvuk". Spusťte generování z reproduktoru a zaškrtněte možnost "Zobrazit částice". Sledujte konkrétní jednu označenou částici (např. červeným křížkem) a vizuálně si ověřte, že pouze kmitá kolem své rovnovážné osy a nikam neodcestuje, zatímco vlna (energie) putuje prostorem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Hranice lidského sluchu a čistý tón

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Lidský sluch pokrývá frekvence zhruba od 20 Hz do 20 kHz, tón A4 má 440 Hz. Čistý tón obsahuje jen jednu frekvenci bez barvy.
> **Nástroj**: [Online Tone Generator](https://www.onlinetonegenerator.com/)
> **Postup**: Nasaďte si sluchátka na bezpečnou (nižší) hlasitost. Zadejte hodnotu `440` a stiskněte Play – uslyšíte čistý koncertní tón A4 bez barvy nástroje. Poté zkoušejte postupně snižovat frekvenci až na 20 Hz a zvyšovat k hranici 15–20 kHz, čímž si otestujete fyzikální limity svého vlastního vnímání (vysoké frekvence s věkem přestáváme slyšet).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Aditivní syntéza barvy zvuku (timbre)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Hudební nástroje nebo hlas se skládají ze základní frekvence a sady frekvenčních složek, které tvoří barvu zvuku (timbre).
> **Nástroj**: [Falstad Fourierova řada](https://www.falstad.com/fourier/)
> **Postup**: V online apletu vidíte řadu posuvníků reprezentujících čisté harmonické tóny (sinusovky). Zkuste vytáhnout pouze první posuvník – uslyšíte čistý tón. Následně si z roletky vyberte předvolbu "Sawtooth" (pilovitá vlna). Uslyšíte jasnou barvu zvuku a uvidíte, jak přesně se z desítek jednoduchých frekvenčních posuvníků složila složitá výsledná vlna.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Spektrogram v reálném čase

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Spektrogram spojuje čas (vodorovně) a frekvenci (svisle) do jednoho obrazu, na kterém lze jasně vidět sykavky řeči nebo harmonické tóny.
> **Nástroj**: [Chrome Music Lab - Spectrogram](https://musiclab.chromeexperiments.com/Spectrogram/)
> **Postup**: Otevřete aplikaci a povolte přístup k mikrofonu. Vydávejte do mikrofonu hluboké hučení, následně zpívejte samohlásku "Á" a nakonec dlouze zasyčte "Tssss". Na obrazovce uvidíte, jak se hučení drží dole (nízké frekvence), samohláska "Á" vykreslí zřetelné pruhy (harmonické složky) a sykavka pokryje obrazovku náhodným „šumem“ vysoko nahoře.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Časový průběh vs. Frekvence v editoru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Klasická zvuková křivka ukazuje amplitudu v čase, ale obtížně z ní poznáme barvu zvuku, k čemuž slouží spektrum.
> **Nástroj**: [Audacity](https://www.audacityteam.org/) (desktopová aplikace)
> **Postup**: Nahrajte do Audacity 10 sekund svého hlasu. Uvidíte klasickou amplitudu v čase. Klikněte na malou šipku vedle názvu stopy (vlevo) a v menu vyberte "Spektrogram" (Spectrogram). Zvuková vlna se změní na tepelnou mapu frekvencí, kde jas barvy ukazuje sílu složky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Decibely akustického tlaku (dB SPL)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: 0 dB SPL znamená práh slyšení a 80 dB SPL v místnosti popisuje fyzikální tlak, což je zcela odlišné od digitálních -6 dBFS.
> **Nástroj**: Aplikace typu NIOSH Sound Level Meter (iOS) nebo Sound Meter (Android)
> **Postup**: Nainstalujte si do telefonu měřič dB SPL. Běžte do co nejtišší místnosti a odečtěte hodnotu (často uvidíte zhruba 30-40 dB SPL). Nula dB SPL totiž neznamená absolutní ticho. Následně pusťte hudbu a sledujte, jak hodnoty logaritmicky narůstají.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Zvuk jako fyzikální a informační jev“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Od mikrofonu k digitální nahrávce

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 2.1: Pozorování směrových charakteristik

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Mikrofon může být kardioidní, osmičkový nebo všesměrový (omnidirectional). Natáčením řešíme problémy ještě před použitím softwaru.
> **Nástroj**: [Neumann Polar Pattern Interactive Tool](https://en-de.neumann.com/) (nebo fyzický mikrofon s přepínáním charakteristik)
> **Postup**: Na stránce výrobce či ve vlastním DAW si prohlédněte interaktivní mapu osmičkové charakteristiky. Pokud máte mikrofon přepnutý na kardioidu, nahrajte hlas a při mluvení jím otočte o 180 stupňů (k sobě zadní částí). Uslyšíte drastický propad citlivosti přesně z toho směru, který je určen k odfiltrování hluku počítače nebo místnosti.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Proximity efekt a plosivy v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Při těsném přiblížení ke směrovému mikrofonu roste vliv basů (proximity effect) a dochází k nárazům hlásek "P" a "B" (plosivy).
> **Nástroj**: Jakýkoliv zvukový editor s mikrofonem (např. Audacity).
> **Postup**: Nastavte mikrofon na stůl bez pop filtru. Přibližte ústa na 2 cm a řekněte důrazně „Petr a Pavel pijí pivo“. Poté odstupte na 20 cm a větu zopakujte. Při poslechu nahrávky jasně uvidíte a uslyšíte, že první věta má rázy, které narážejí na mikrofon a znějí zastřeně basově.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Zkreslení signálu a Clipping

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Překročíme-li při záznamu maximální limit (0 dBFS), vrchol signálu se ploše ořízne a vznikne nevratné zkreslení (clipping).
> **Nástroj**: [Online Web Oscilloscope](https://oscillo.com/) nebo Audacity.
> **Postup**: Otevřete osciloskop. Normálně mluvte – uvidíte plynulou zvukovou křivku s rezervou (headroom). Poté do mikrofonu zakřičte nebo do něj foukněte. Pozorujte, jak vlna překročí limity zobrazení a vrchní obloučky jsou zcela rovně oříznuty, čímž se vytvoří agresivní, chraplavý digitální zvuk, který pouhým ztišením už nelze opravit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Vizuální důkaz Aliasingu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Podle Nyquistova teorému musí být vzorkovací frekvence alespoň dvojnásobná oproti nejvyšší nahrávané frekvenci; jinak vzniká falešný signál – aliasing.
> **Nástroj**: [Desmos Graphing Calculator - Aliasing demo](https://www.desmos.com/calculator)
> **Postup**: Najděte si v grafickém kalkulátoru nebo si představte ukázku "aliasingu". Nakreslete velmi hustou sinusovku (vysoká frekvence). Pokud na ní uděláte body (vzorky) jen velmi zřídka (nízké vzorkování) a pokusíte se tyto řídké body spojit plynulou čarou, vznikne vám opticky zbrusu nová široká sinusovka o nízké frekvenci, která v původním zvuku neexistovala.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Poslech kvantizačního šumu a Ditheringu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Snížení bitové hloubky vede ke kvantizačnímu zkreslení. Přidání slabého, záměrného šumu (dither) zlepší subjektivní kvalitu.
> **Nástroj**: [Audiocheck.net - Dithering Test](https://www.audiocheck.net/audiotests_dithering.php)
> **Postup**: Otevřete si na stránce test ditheringu. Pusťte si ukázku 8-bitového audia s extrémně tichým tónem a bez ditheru – uslyšíte ošklivý písklavý pazvuk (kvantizační chybu). Poté přepněte na 8-bitovou verzi s aktivním ditheringem. Uslyšíte sice jemný šum jako u magnetofonu, ale onen rušivý pazvuk zcela zmizí – chyba se díky šumu rozptýlila.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Interní směrování (Routing) zvuku

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Počítač nesměruje jedničky a nuly přímo do reproduktoru. Celá cesta zahrnuje A/D převodník a softwarové vrstvy, než jde signál do D/A převodníku sluchátek.
> **Nástroj**: [Voicemeeter (Windows)](https://vb-audio.com/Voicemeeter/) nebo [BlackHole (macOS)](https://existential.audio/blackhole/)
> **Postup**: Nainstalujte si virtuální mixážní pult. V operačním systému nastavte jako výchozí výstup virtuální kabel, nikoliv sluchátka. V programu (např. Voicemeeter) poté ručně "propojte" vizuální posuvník vstupu do hardwarového výstupu A1 (vaše sluchátka). Pochopíte tak v praxi, jak zvuková data tečou odděleně jako digitální toky a můžete je nezávisle směrovat mezi aplikacemi.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Od mikrofonu k digitální nahrávce“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Audio soubory, komprese a psychoakustika

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 3.1: Porovnání velikosti a typu formátů (WAV, FLAC, MP3)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: WAV je pracovní kontejner bez ztrátové komprese, FLAC je bezeztrátově zabalený soubor (jako ZIP pro audio) a MP3 ušetří místo psychoakustickým zahozením dat.
> **Nástroj**: [fre:ac - Free Audio Converter](https://www.freac.org/)
> **Postup**: Stáhněte si do počítače delší, ideálně minutovou hudební ukázku ve formátu WAV. Vložte ji do fre:ac a vyexportujte ji jednou jako FLAC (úroveň 5) a podruhé jako MP3 (128 kbps). V průzkumníku souborů porovnejte jejich velikosti v megabytech. Zatímco FLAC se po rozbalení stoprocentně obnoví, MP3 je zlomkově velká, protože část obsahu smazala.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Slepý ABX test komprese

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Ztrátová komprese spoléhá na to, že posluchač neodhalí odstraněné informace. Snížíme-li bitrate, maskování přestane fungovat ideálně.
> **Nástroj**: [Digitalfeed.net ABX test](http://abx.digitalfeed.net/)
> **Postup**: Otevřete v prohlížeči ABX test, který hraje bezeztrátový vzorek (A), ztrátový vzorek (B) a skrytý testovací vzorek (X). Vaším úkolem je poslechem (ideálně na dobrých sluchátkách) uhodnout, zda vzorek X patří pod A nebo B. U toku 320 kbps zjistíte, že je lidský sluch téměř neschopný rozeznat ztrátovou kompresi od originálu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Vizuální odhalení MP3 formátu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Ztrátový kodek odstraňuje složky, které považuje za nepodstatné, a nižší bitrate začne viditelně řezat do vysokých frekvencí.
> **Nástroj**: [Spek (Acoustic Spectrum Analyser)](http://spek.cc/)
> **Postup**: Stáhněte bezplatný nástroj Spek. Nahrajte do něj původní WAV soubor a vygenerovanou MP3 z Experimentu 3.1 (128 kbps). Porovnáním obou spektrogramů uvidíte u MP3 zcela rovnou černou čáru odstřihující horní okraj grafu (často nad 15 nebo 16 kHz), což dokazuje psychoakustický algoritmus v praxi.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Psychoakustika a Frekvenční maskování

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Silný tón může způsobit, že frekvenčně nebo časově blízký slabší tón lidský mozek přestane vnímat, z čehož těží formát MP3.
> **Nástroj**: [Auditoryneuroscience.com (Psychoacoustics)](https://auditoryneuroscience.com/)
> **Postup**: V sekci frekvenčního maskování si přehrajte interaktivní ukázku, kde zní testovací tón a maskovací šum (např. úder činelu v hudbě). Postupným upravováním hlasitosti nebo šířky maskovacího pásma si na svém vlastním uchu ověříte okamžik, kdy fyzicky přítomný slabý tón přestanete absolutně slyšet.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Iluze binaurálního zvuku na stereu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Model HRTF dokáže ošálit mozek jemnými změnami zvuku, takže se zdá, že zvuk letí např. zezadu, přestože máme na uších jen standardní levé a pravé sluchátko.
> **Nástroj**: YouTube - hledat heslo [„Virtual Barber Shop“](https://www.youtube.com/watch?v=IUDTlvagjJA)
> **Postup**: Nasaďte si jakákoliv běžná stereo sluchátka, zavřete oči a pusťte nahrávku "Virtual Barber Shop". Mozek zpracuje HRTF informaci v nahrávce a vytvoří dokonalou iluzi, že kadeřník s nůžkami chodí kolem vás, naklání se shora i zezadu, čímž je překonán limit klasického levého/pravého kanálu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Umisťování zvuku ve 3D prostoru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Objektové audio nepracuje s pevnými kanály, ale s umístěním zdroje v prostoru, které sluchátka simulují pomocí HRTF a binaurálních modelů.
> **Nástroj**: [Web Audio API Spatialization](https://panner-node.glitch.me/) nebo Sennheiser AMBEO Orbit VST (ve vlastním DAW).
> **Postup**: Otevřete interaktivní 3D ukázku v prohlížeči. Uvidíte hlavu posluchače a bod, který vydává tón. Myší bod uchopte a pomalu s ním kružte kolem uší grafiky nebo jej zvedejte do výšky. Poslouchejte, jak modelátor v reálném čase filtruje frekvence tak, aby dokonale napodobil vlastnosti hlavy a uší.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Audio soubory, komprese a psychoakustika“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Jak lze zvuk vytvářet v počítači

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 4.1: Subtraktivní syntéza (tvarování signálu)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Digitální tón vytváříme synteticky z oscilátoru (sinus, obdélník, pila) a následným tvarováním, například aplikováním filtrů.
> **Nástroj**: [Ableton Learning Synths - Oscillators](https://learningsynths.ableton.com/)
> **Postup**: V interaktivním tutoriálu přejděte na záložku "Oscillator". Tažením myši přepínejte mezi základními tvary vln. Uslyšíte, že "Saw" (pila) je agresivní a bzučivá, na rozdíl od tupého sinusu. Následně stáhněte frekvenci filtru ("Filter") a sledujte, jak se zvuk zakulatí (filtr uřízne vysoké frekvence u agresivní vlny).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Tvarování průběhu pomocí obálky ADSR

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Obálka určuje, jak se hodnota zvuku (např. hlasitost) mění v čase od stisku do puštění klávesy. Fáze jsou Attack, Decay, Sustain a Release.
> **Nástroj**: [Ableton Learning Synths - Envelopes](https://learningsynths.ableton.com/envelopes/)
> **Postup**: Zobrazte si kontrolky ADSR obálky. Prodlužte hodnotu *Attack* (náběh) na maximum a stiskněte virtuální klávesu – místo ostrého úderu klavíru získáte pomalu nabíhající smyčcový zvuk. Následně prodlužte *Release* (doznívání), pusťte klávesu a poslouchejte, jak tón dlouze odplouvá do ticha i bez držení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Protokol MIDI a práce s Piano Roll

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: MIDI neobsahuje nahraný zvuk vln (audio), ale digitální příkazy typu "zahraj notu" (Note On) a "přestaň hrát" (Note Off).
> **Nástroj**: [Online Sequencer](https://onlinesequencer.net/)
> **Postup**: V mřížce "Piano roll" naklikejte myší několik barevných obdélníků (MIDI událostí). Pusťte přehrávání a přesvědčte se, že bloky nejsou samotný zvuk. Následně v menu změňte nástroj (např. z Piano na 8-bit Synth). Protože se změnily jen instrukce a nikoli vlny, stejná melodie začne okamžitě hrát naprosto jiným zvukem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Od notového zápisu do hudební produkce

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Notový zápis lze převést na MIDI instrukce, přiřadit je virtuálním nástrojům a přehrát bez přítomnosti skutečných hudebníků.
> **Nástroj**: [MuseScore](https://musescore.org/cs)
> **Postup**: Nainstalujte tento bezplatný notační program. Vytvořte nový projekt a vložte do běžné osnovy jednoduchou písničku (kliknutím umístěte čtvrtové a osminové noty). Po stisknutí Play program vaše vizuální noty interpretuje jako MIDI signály, které interně rozeznívají vestavěné modely hudebních nástrojů.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Sampling nahraných vzorků

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Virtuální nástroj nemusí pracovat s čistou matematikou; formou samplingu může reagovat na MIDI stisky přehráváním dříve nahraných fyzických vzorků (samplů).
> **Nástroj**: [Decent Sampler](https://www.decentsamples.com/) (standalone aplikace)
> **Postup**: Stáhněte sampler a z knihovny Pianobook do něj načtěte libovolný bezplatný nasamplovaný nástroj (např. starý rodinný klavír). Klikáním na virtuální klávesnici programu aktivujete MIDI instrukce, na které program reaguje přehráváním specifických, detailně přednahraných zlomků reálného klavíru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Základní práce ve vícestopém DAW editoru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Digital Audio Workstation (DAW) je časová osa vrstev, kde se kombinuje zachycené audio z mikrofonu a MIDI data ovládající syntezátor.
> **Nástroj**: [BandLab](https://www.bandlab.com/) (online DAW)
> **Postup**: V prohlížeči založte nový projekt s prázdnou časovou osou. Vytvořte první stopu (Audio) a nahrajte do ní mluvené slovo. Poté vytvořte druhou stopu (Virtual Instruments) a pomocí klávesnice k ní zapište MIDI podkres. Přehráním projektu uslyšíte, jak v DAW mícháte vrstvu mechanického audia (hlas) a datově generovanou vrstvu syntetizátoru.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Jak lze zvuk vytvářet v počítači“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Od syrové nahrávky k hotovému zvuku

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 5.1: Nedestruktivní střih a vyhlazení řezu (Crossfade)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: V moderním projektu úpravy původní zdrojový WAV nemění. Spojením dvou úseků by mohl vzniknout rušivý skok, který řeší crossfade.
> **Nástroj**: [AudioMass](https://audiomass.co/)
> **Postup**: Nahrajte do webového editoru libovolnou mp3 píseň. Vyznačte velký kus uprostřed a smažte jej (nedestruktivně pro zdrojový soubor na disku). Pusťte zvuk přes místo řezu – pravděpodobně uslyšíte ošklivé puknutí (kliknutí) v důsledku nespojité vlny. Oba okraje řezu označte a aplikujte efekt "Fade" (crossfade). Následný poslech odhalí, že kliknutí díky vyhlazenému překrytí zmizelo.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Tónový charakter s Ekvalizérem (EQ)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: EQ řeší frekvenční vztahy; nemění samotný obsah (např. slova), ale odstraňuje dunivé ruchy (rumble) nebo zvýrazňuje řečové frekvence.
> **Nástroj**: [TDR Nova](https://www.tokyodawn.net/tdr-nova/) (nebo zabudovaný grafický EQ v Audacity)
> **Postup**: Nahrajte větu, v níž úmyslně ťuknete do stojanu stolu, abyste vytvořili hluboký rumble. Zapněte grafický EQ. Uchopte bod v levé části frekvenčního grafu (např. pod 80 Hz) a stáhněte jej příkře dolů, čímž aplikujete takzvaný High-Pass (Low-Cut) filtr. Uslyšíte, že hluboké dunění zmizí, zatímco hlavní srozumitelnost a pásmo vašeho hlasu zůstanou nedotčené.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Úprava rozdílů dynamickou kompresí

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Dynamická komprese odstraňuje rozdíly hlasitostí (tiché části oproti hlasitým špičkám). Neplést s datovou kompresí zmenšující MB soubory.
> **Nástroj**: [Klanghelm DC1A](https://klanghelm.com/contents/products/DC1A.php) nebo Audacity (Efekt -> Kompresor).
> **Postup**: Nahrajte 15 sekund řeči, kde střídáte velmi tichý šepot a následné hlasité zvolání. Aplikujte dynamický kompresor (nastavte hluboký Treshold/Práh a Ratio na 4:1). Po aplikaci uvidíte, že vlnové křivky šepotu zůstaly nedotčeny, ale obří špičky zvolání systém automaticky stáhl dolů. Hlas se tím výrazně vyrovnal.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Redukce šumu otiskem a meze záchrany

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Klasické algoritmy dokážou potlačit stálý profil brumu/šumu, pokud jej ale aplikujete agresivně, začnou zvuk deformovat do vodového artefaktu.
> **Nástroj**: Audacity (Efekt -> Redukce šumu)
> **Postup**: Pusťte v pozadí vysavač nebo větrák. Nahrajte pět sekund "ticha" (pouze hluku spotřebiče) a poté do tohoto hluku něco řekněte. Označte v editoru pouze oněch 5 sekund ticha a klikněte na "Získat profil šumu". Následně označte celou nahrávku a profil šumu aplikujte. Při maximálním vytažení redukce (agresivním potlačení) slyšíte sice vymizelý větrák, ale z vašeho hlasu zbyde podivný kovový robot ("vodový" charakter).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Měření hlasitosti pro mastering (LUFS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Mastering je finální příprava mixu pro distribuci. Musí zohledňovat digitální špičky a subjektivně vnímanou hlasitost před publikací.
> **Nástroj**: [Loudness Penalty](https://www.loudnesspenalty.com/)
> **Postup**: Vezměte svůj vyexportovaný audio soubor a nahrajte jej do tohoto bezplatného analyzéru. Systém změří jeho reálnou integrovanou hlasitost a na obrazovce vám ukáže seznam platforem (Spotify, YouTube, Apple Podcasts) a číslo v decibelech. Zjistíte tak přesně, jestli vaše nahrávka splňuje distribuční normy, nebo o kolik decibelů bude platformou uměle ztlumena/zesílena (proces zvaný normalization).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Testování automatizovaného workflow

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Pro běžný podcast stačí jasné postupy priorit (dobře nahrát -> čistit -> vyrovnat hlasy a masterovat). Část umí řešit automaty.
> **Nástroj**: [Auphonic (bezplatný limitovaný účet)](https://auphonic.com/)
> **Postup**: Do systému Auphonic nahrajte syrový, nesestříhaný rozhovor, ve kterém je jeden člověk mírně potichu a druhý velmi hlasitý. Vyberte automatický profil "Adaptive Leveler" a vyexportujte zvuk. Služba provede workflow popsané v 5. kapitole – jemnou kompresi pro vyrovnání tichého hlasu a konečné stanovení hlasitosti před publikací, což slouží jako dokonalý ilustrační příklad funkčního postprodukčního řetězce.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Od syrové nahrávky k hotovému zvuku“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Umělá inteligence mění práci se zvukem

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 6.1: Transkripce a Diarizace (ASR)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Systém Automatic Speech Recognition (ASR) vyhledává ve zvuku vzory odpovídající řeči a bleskově je přepisuje, přičemž dovede rozlišit mluvčí (diarizace).
> **Nástroj**: [MacWhisper](https://macwhisper.com/) nebo podobný nástroj na bázi modelu OpenAI Whisper.
> **Postup**: Stáhněte jakýkoliv podcast nebo hodinový záznam z přednášky. Vložte soubor do aplikace a zvolte model (např. Small). Sledujte neuvěřitelnou rychlost, se kterou software převede obrovské vlny na textové odstavce s přesným oddělením odstavců typu "Mluvčí 1" a "Mluvčí 2", přestože jména nezná.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Úprava a střih audia jako ve Wordu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Díky ASR už v moderních aplikacích nestříháme klikáním na nečitelné křivky a průběhy, ale mažeme věty přímo z přepsaného textu.
> **Nástroj**: [Descript (Web / Desktop)](https://www.descript.com/)
> **Postup**: Nahrajte do bezplatné verze Descriptu zkušební monolog. Software vytvoří jeho přepis (text). Najděte přeřeknutí a klávesou Delete smažte ono konkrétní slovo (případně výplňové slovo "ééé"). Tím, že smažete slovo z textového dokumentu, program automaticky na pozadí vystřihne příslušnou vlnu v časové ose a zacelí ránu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Řízení prosodie ve TTS (Text-to-Speech)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Moderní syntéza negeneruje slova staticky a roboticky; na základě textu vytváří prosodii (rytmus, důrazy, emoce, pauzy).
> **Nástroj**: [ElevenLabs (TTS)](https://elevenlabs.io/)
> **Postup**: Otevřete generátor hlasu a zadejte větu ze studijního materiálu: *„Tak tohle jsem opravdu nečekal.“*. Následně zadejte stejnou větu podruhé, ale do závorek nebo uvozovek vložte kontext a interpunkci, např.: *„Hahaha, tak tohle... tohle jsem OPRAVDU nečekal!“*. Uslyšíte jasný důkaz toho, že model nevyužil pevně nasamplovaná slova, ale dynamicky změnil rytmus, intonaci a dech hlasu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Rizika Hlasového klonování (Voice cloning)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Z krátké nahrávky řeči lze vygenerovat klon lidského hlasu a naučit ho novým větám. Samotný hlas do telefonu proto už není důkazem identity.
> **Nástroj**: [ElevenLabs (Voice Cloning)] / [AI Voice Detector - AI or Not](https://www.aiornot.com/)
> **Postup**: Ve stejné službě si nahrajte minutový vzorek svého vlastního hlasu a vygenerujte "svým hlasem" větu: „Ahoj, jsem v úzkých, pošli mi prosím na účet peníze“. Sledováním obrovské míry realismu si prakticky uvědomíte význam varování před AI podvody v bezpečnostních protokolech. Uložený soubor poté pošlete do detektoru typu AIorNot a prozkoumejte, jestli systém dokáže zachytit mikroskopické artefakty syntézy a podvod odhalit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Odhalení skrytých struktur (Source Separation)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: AI separace neumí najít skutečnou původní "skrytou" stopu, ale podle natrénovaných modelů odhaduje frekvenční zdroje ze směsi.
> **Nástroj**: [Moises.ai](https://moises.ai/) nebo Ultimate Vocal Remover.
> **Postup**: Vezměte starší komerční píseň (kde znáte hudbu i zpěv) a nahrajte ji do platformy Moises. Na obrazovce se vám po chvíli objeví posuvníky pro separovaný vokál, basu, bicí a syntezátory. Ztište hudbu a stáhněte pouze vokál (A Capella). Poslouchejte velmi detailně (na lepších sluchátkách). Zaznamenáte „artefakty“ – zvláštní praskání nebo zkreslené slabiky, což dokazuje, že nejde o čistou nahrávku z původního studia, ale o zpětnou pravděpodobnostní rekonstrukci umělou inteligencí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Generativní workflow formou promptování (Text-to-Audio)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Systém generativní umělé inteligence dnes zvládá podle textového promptu modelovat ruchové zvuky, strukturu písně nebo náladu.
> **Nástroj**: [Stable Audio](https://stableaudio.com/) nebo hudební [Suno](https://suno.com/)
> **Postup**: Otevřete generátor text-to-audio a zadejte do něj prompt přímo ze zadání: *"Těžké kovové dveře se zavřou v prázdné podzemní hale, krátký výrazný dozvuk."*. Nechte model vytvořit výstup. Zkuste to několikrát. Nástroj pokaždé vygeneruje zbrusu nová zvuková data (bez použití existujících WAV vzorků ze standardních knihoven). Tím je zřejmé, že se AI postupně stává dalším běžným zdrojem zvuku pro kreativce hned vedle fyzických mikrofonů.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Umělá inteligence mění práci se zvukem“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
