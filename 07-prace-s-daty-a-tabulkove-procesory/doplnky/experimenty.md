<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Práce s daty a tabulkové procesory

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


## 1. Od otázky k datové sadě

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato kapitola zdůrazňuje, že data nezačínají v tabulce, ale správnou analytickou otázkou a definicí toho, co přesně měříme. Zde jsou experimenty pro pochopení struktury a sběru dat:

### Experiment 1.1: Návrh sběru dat a vynucení datových typů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [KoboToolbox](https://www.kobotoolbox.org/) (Online)
> **Postup**: Založte si bezplatný účet a vytvořte formulář pro měření teploty ve škole. Přidejte otázky: "Identifikátor učebny" (nastavte jako rozbalovací seznam/kategorii), "Teplota" (nastavte striktně jako desetinné číslo) a "Čas měření" (typ datum a čas). Vyplňte formulář třikrát s chybami (např. zkuste do teploty napsat "teplo") a pozorujte, jak vás systém nepustí, čímž už při sběru chráníte kvalitu dat.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Generování fiktivních dat ve formátu "Tidy data"

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Mockaroo](https://www.mockaroo.com/) (Online)
> **Postup**: Vytvořte schéma obdélníkové tabulky, kde jeden řádek bude představovat jedno měření. Nastavte sloupce: `cas` (Datetime), `ucebna_id` (Custom List: A203, B105), `teplota_c` (Number). Vygenerujte 100 řádků fiktivních senzorových dat a stáhněte je jako CSV. Všimněte si, že každá buňka obsahuje pouze jedinou hodnotu.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Seznámení se surovými daty z API

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Postman](https://www.postman.com/) (Online / Ke stažení)
> **Postup**: Zdroje zmiňují získávání dat přes aplikační programové rozhraní (API). V Postmanu vložte do řádku veřejnou URL adresu (např. bezplatné API pro aktuální počasí) a odešlete "GET" dotaz. Prohlédněte si výsledek – neuvidíte úhlednou tabulku, ale hierarchický datový výpis (často formát JSON), který se do tabulky teprve musí transformovat.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Zkoumání reálných metadat a datových slovníků

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Portál otevřených dat ČR](https://data.gov.cz/) (Online)
> **Postup**: Vyhledejte libovolnou datovou sadu (např. kapacity škol). Otevřete záložku s dokumentací. Zkuste najít, jak je sada popsaná – podle textu fungují metadata jako "návod k použití". Najděte, zda autor vysvětluje jednotky, časové období a licenci, abyste předešli falešně přesné interpretaci.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Formulace analytických otázek nad cizí sadou

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Kaggle](https://www.kaggle.com/) (Online)
> **Postup**: Najděte si sadu zaměřenou na vzdělávání (vyhledejte "Student Performance"). Prostudujte dostupné sloupce. Na základě textu, který říká, že dobrá otázka určuje, co se bude pozorovat, sepište 3 konkrétní analytické otázky, na které by tato data dokázala odpovědět, a 1 otázku, která z těchto dat zodpovědět nepůjde.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Vizualizace datového mentálního modelu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Draw.io](https://app.diagrams.net/) (Online)
> **Postup**: Text nabízí mentální model: otázka → sběr → kontrola → struktura → analýza → interpretace → rozhodnutí. Pomocí tvarů a šipek v tomto bezplatném nástroji nakreslete vývojový diagram, který na tento model namapuje konkrétní příklad z textu (např. řešení vydýchaných učeben a spotřeby energií).


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Od otázky k datové sadě“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Tabulkový procesor jako datová laboratoř

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tabulkový procesor odděluje zdrojová data od reportu a surovou hodnotu od jejího vizuálního formátu. Následující úkoly vám pomohou pochopit fungování pod kapotou:

### Experiment 2.1: Průzkum struktur CSV a XLSX

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Poznámkový blok (Windows) nebo [Notepad++](https://notepad-plus-plus.org/)
> **Postup**: Zdroje uvádějí, že CSV je prostý text oddělený znaky a nepřenáší vzorce ani barvy. Vytvořte v Excelu/Calcu malou tabulku (2 sloupce, obarvěte jednu buňku žlutě) a uložte ji jako XLSX i CSV. Následně oba soubory otevřete v textovém editoru (Poznámkový blok). Zatímco CSV bude čitelný text s čárkami nebo středníky, XLSX se zobrazí jako změť nečitelných znaků.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Rozbalení hierarchického formátu JSON

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [JSON Crack](https://jsoncrack.com/) (Online)
> **Postup**: JSON umí vyjádřit vnořené objekty. Najděte si na internetu jakoukoliv ukázku JSON kódu (nebo požádejte AI o "ukázkový JSON profilu studenta"). Vložte kód do levého panelu v JSON Crack. Sledujte, jak se data rozvětví do vizuálního stromu, a zamyslete se nad tím, jak byste tuto větvenou strukturu převáděli do jediné ploché "Tidy" tabulky.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Relativní, absolutní a smíšené odkazování v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: LibreOffice Calc, MS Excel nebo Google Sheets
> **Postup**: Vytvořte tabulku s cenami vybavení učeben v Kč ve sloupci A a do buňky H1 napište kurz eura (např. 25). V buňce B2 vytvořte vzorec `=A2/H1` a zkopírujte jej dolů. Všimněte si, že vzorec přestane fungovat (relativní odkaz se posunul z H1 na H2). Změňte vzorec na `=A2/$H$1`, což je absolutní odkaz zamykající buňku kurzového převodu, a zkopírujte jej znovu.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Spojování tabulek funkcí XLOOKUP / VLOOKUP

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: LibreOffice Calc, MS Excel nebo Google Sheets
> **Postup**: Text zmiňuje doplňování dat z jiné tabulky pomocí funkce pro vyhledávání. Na List 1 vložte tabulku s údaji: `ucebna_id` a `teplota`. Na List 2 si vytvořte "slovník": `ucebna_id` a `patro`. Pomocí vyhledávací funkce (VLOOKUP, případně XLOOKUP) přiřaďte ke každé teplotě na Listu 1 správné patro podle identifikátoru učebny.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Agregace dat pomocí kontingenční tabulky

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [PivotTable.js](https://pivottable.js.org/examples/) (Online) nebo tabulkový procesor
> **Postup**: Kontingenční tabulka vytváří agregovaný pohled. Načtěte do nástroje libovolná data (např. CSV vygenerované v experimentu 1.2). Přetáhněte `ucebna_id` do řádků a `teplota_c` do hodnot. Změňte agregační funkci ze "Součtu" (Count/Sum) na "Průměr" (Average). Všimněte si, že se mění otázka, nikoli původní data.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Oddělení informace od formátování buněk

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: LibreOffice Calc, MS Excel nebo Google Sheets
> **Postup**: Zdroje varují, že barva buňky není spolehlivým datovým údajem. Vytvořte tabulku deseti měření, u dvou hodnot obarvěte pozadí červeně (jako simulaci chybného senzoru). Poté zkuste tabulku pomocí nástroje Filtr filtrovat jen na chybné senzory. Zjistíte, že s barvou se pracuje hůře. Následně vytvořte nový sloupec s názvem `stav` a hodnotou "porucha" pro červené buňky. Nyní data vyfiltrujte znovu.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Tabulkový procesor jako datová laboratoř“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Čištění a transformace: práce, kterou výsledek skrývá

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Čištění není jen kosmetická úprava, ale rozhodování, které ovlivní výsledek. Základem je nezničit si původní surová data (raw data).

### Experiment 3.1: Bleskové profilování obřích souborů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [VisiData](https://visidata.org/) (Terminál / Windows přes WSL) nebo pro snazší přístup "Průzkum" v Google Sheets.
> **Postup**: Text radí zkontrolovat minimum, maximum a chybějící hodnoty, aby se odhalila např. teplota 215 °C. Nahrajte velkou (tisíce řádků) nevyčištěnou sadu do aplikace, zvolte funkci Data Profiling (nebo stiskněte Shift+F ve VisiData). Sledujte, jak program okamžitě ukáže, kolik prázdných buněk a jaká extrémní maxima se v jednotlivých sloupcích skrývají.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: ování s imputací (doplňováním chybějících dat)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Orange Data Mining](https://orangedatamining.com/) (Ke stažení)
> **Postup**: Text varuje, že nula není totéž co prázdná buňka, a zmiňuje imputaci (odhad) mediánem. V Orange vložte widget "File" se svými daty, kde smažete pár buněk teplot. Připojte k němu widget "Impute" a zkuste chybějící data nahradit a) průměrem, b) náhodnou hodnotou. Následně si data zobrazte ve widgetu "Data Table" a posuďte změnu.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Pochopení časových značek (Timestamps)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Epoch Converter](https://www.epochconverter.com/) (Online)
> **Postup**: Zápis `03/04/2026` je pro člověka i počítač matoucí. Tento nástroj ukazuje, jak počítače ukládají čas jako tzv. "Unix Epoch" (počet vteřin od r. 1970). Zadejte dnešní datum a vygenerujte si toto číslo (např. 1723900000). To ukazuje, že čas je ve skutečnosti pro počítač vždy jen jedno spojité číslo, a jakýkoliv jiný zápis (jako `YYYY-MM-DD`) je pouze "lidským formátem".

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Dolování čistých dat ze zrádných PDF formátů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Tabula](https://tabula.technology/) (Ke stažení - Open Source)
> **Postup**: Data jsou často pro čistou analýzu nedostupná, protože jsou esteticky formátována v PDF zprávách. Stáhněte si libovolnou výroční školní nebo firemní zprávu v PDF s vloženou tabulkou. Otevřete ji v aplikaci Tabula, označte kurzorem myši pouze oblast samotné tabulky a nechte si ji extrahovat do čistého a uspořádaného CSV souboru.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Jednoznačné identifikátory a spojování tabulek (JOIN)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [SQLite Online](https://sqliteonline.com/) (Online)
> **Postup**: Spojování podle textového jména je rizikové, je lepší použít identifikátor (např. `ucebna_id`). V tomto prostředí si vytvořte dvě jednoduché tabulky příkazem SQL. První s `ucebna_id` a teplotou, druhou s `ucebna_id` a názvem třídy. Následně napište příkaz `SELECT * FROM tabulka1 JOIN tabulka2 ON tabulka1.ucebna_id = tabulka2.ucebna_id` a sledujte, jak se bezchybně propojí.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Vytvoření opakovatelného ETL řetězce

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Power Query (součást Windows/Excel - karta Data -> Načíst data)
> **Postup**: Ručně upravovat stažená data znamená zapomenout kroky. Pomocí Power Query importujte zkušební CSV. V editoru umažte jeden nepotřebný sloupec a odfiltrujte prázdné hodnoty. Všimněte si okénka vpravo, které zaznamenává "Aplikovaný postup". Původní (raw) data se nijak nepřepisují a pokud se změní zdrojový soubor, stačí kliknout na tlačítko "Aktualizovat vše".


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Čištění a transformace: práce, kterou výsledek skrývá“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Od souhrnu ke statistickému uvažování

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Zdroje varují, že velké datové sady nejsou automaticky kvalitní a že aritmetický průměr může velmi snadno lhát. K osahání statistických konceptů využijte tyto nástroje:

### Experiment 4.1: Jak odlehlá hodnota (Outlier) posouvá průměr

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DrawMyData](https://robertgrantstats.co.uk/drawmydata.html) (Online)
> **Postup**: Text zmiňuje, že průměr využívá všechny hodnoty a reaguje na extrémy, zatímco medián je stabilnější. Na prázdné plátno bodového grafu "naklikejte" cluster pěti bodů těsně u sebe. Poznamenejte si vypočítaný průměr. Poté klikněte na jedno jediné místo v extrémním horním pravém rohu. Sledujte, jak dramaticky tato jediná odlehlá hodnota vychýlila průměrnou osu.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Vizualizace variability pomocí histogramu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [GeoGebra Statistics Calculator](https://www.geogebra.org/classic#data) (Online)
> **Postup**: Rozdělení dat skvěle ukáže histogram, který seskupuje hodnoty do navazujících intervalů. Vložte do tabulky 30 různých fiktivních teplot (např. od 18 °C do 30 °C). Klikněte na vytvoření histogramu. Následně pomocí posuvníku měňte "šířku intervalu" (bin width). Sledujte, jak volba intervalu mění celý optický příběh o tom, kde je ve třídách "nejčastější teplota".

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Mezikvartilové rozpětí a Krabicový graf (Box plot)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [RAWGraphs](https://rawgraphs.io/) (Online)
> **Postup**: Dvě učebny mohou mít stejný průměr, ale v jedné hodnoty kolísají drastičtěji. Vygenerujte si data se dvěma sloupci (`ucebna`, `teplota`). Nakopírujte je do RAWGraphs. Z nabídky vizualizací vyberte "Box plot". Tento graf vám názorně vykreslí medián jako čáru uprostřed a kvartily tvořící krabici (tzv. IQR - mezikvartilové rozpětí).

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Trénink odhadu korelačního koeficientu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Guess the Correlation](http://guessthecorrelation.com/) (Online)
> **Postup**: Zdroje říkají, že korelace udává směr a sílu lineární souvislosti v intervalu -1 až +1. Tato webová hra vám zobrazí bodový graf (scatterplot) a vaším úkolem je hodnotu R co nejpřesněji "uhodnout". Odehrajte 10 kol. Naučíte se tím intuitivně odlišit silný vztah (blížící se 1 nebo -1) od chaotického shluku bodů (kolem 0).

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Korelace není kauzalita (Spurious Correlations)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Spurious Correlations (tylervigen.com)](https://www.tylervigen.com/spurious-correlations) (Online)
> **Postup**: Silná korelace nedokazuje příčinu a dvě řady mohou růst ze zcela nesouvisejících důvodů. Navštivte tento web. Najděte libovolný absurdní graf (například korelaci počtu utonulých v bazénu s filmy Nicolase Cage). Pro sebe si sepište jednu větu s argumentem inspirovaným textem o tom, proč silná korelace na tomto grafu nereprezentuje kauzální příčinu.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Náhodná nejistota a výběrový vzorek

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [StatKey](https://www.lock5stat.com/StatKey/) (Online)
> **Postup**: Každé měření ze vzorku obsahuje náhodnou nejistotu. Zvolte záložku "Bootstrap Dotplot of Mean". Nástroj ukazuje, co se stane, když ze stejné populace vytáhnete tisíc různých náhodných vzorků. Všimněte si "zvonovité křivky" výsledků, která ilustruje, že jeden konkrétní vzorek nemusí naprosto přesně odpovídat celkové populaci.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Od souhrnu ke statistickému uvažování“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Graf jako odpověď, ne jako dekorace

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Kapitola zdůrazňuje, že graf je odpovědí na konkrétní otázku, ne ozdobou tabulky, a že manipulací s měřítkem lze vytvořit falešné drama.

### Experiment 5.1: Rozhodovací strom pro typ grafu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [From Data to Viz](https://www.data-to-viz.com/) (Online)
> **Postup**: Text udává, že pro vztah obsazenosti a CO₂ se volí bodový graf a pro vývoj spojnicový. Otevřete interaktivní strom na tomto webu. Zadejte, že máte "Jednu číselnou a jednu kategorickou proměnnou" (např. porovnání učeben podle teploty). Proklikejte se doporučeními a zjistěte, proč vám strom nabídne sloupcový graf a varuje před 3D perspektivou.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Přístupnost a testování barev

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Viz Palette](https://projects.susielu.com/viz-palette) (Online)
> **Postup**: Graf má mít jen tolik barev, kolik je potřeba k rozlišení. Zvolte si v tomto nástroji 5 náhodných barev, kterými byste obarvili pět různých školních učeben v grafu. Zapněte filtr "Deuteranopia" (nejběžnější barvoslepost) a podívejte se na simulaci – zřejmě zjistíte, že některé učebny najednou splývají do stejného odstínu a je třeba paletu změnit.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Zavádějící oříznutí osy Y

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Datawrapper](https://www.datawrapper.de/) (Online)
> **Postup**: Vytvořte tabulku o 2 řádcích: "Třída A" - hodnota 98, "Třída B" - hodnota 100. Nahrajte ji do Datawrapper a zvolte "Bar chart" (sloupcový graf). Následně v nastavení osy Y zrušte výchozí bod "0" a nechte graf začínat na hodnotě "95". Sledujte, jak se minimální dvouprocentní rozdíl vizuálně promění v dramaticky obrovský skok, což je přesně to, před čím text varuje.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Tvorba interaktivního dashboardu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Looker Studio](https://lookerstudio.google.com/) (Online - dříve Google Data Studio)
> **Postup**: Dashboard není nástěnka pro všechny grafy, ale pro konkrétní rozhodnutí. Přihlaste se Google účtem, založte prázdný report a napojte ho na libovolnou Google tabulku. Vložte dva grafy (např. časovou řadu teplot). Následně z horní lišty přidejte ovládací prvek "Rozbalovací seznam" a propojte ho se sloupcem `ucebna_id`. Vyzkoušejte si, jak jedno kliknutí uživatele změní data v obou grafech najednou.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Kritika špatných a zavádějících vizualizací

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [WTF Visualizations (viz.wtf)](https://viz.wtf/) (Online)
> **Postup**: Dvě nesouvisející řady lze zarovnat tak, že působí totožně. Projděte si tuto galerii reálných grafů z médií. Vyberte 3 grafy a zkuste k nim přiřadit konkrétní hřích, který kapitola 5 zmiňuje. Zaměřte se na hledání nevhodných 3D efektů, špatných výsečových grafů se spoustou podílů nebo os, které nezačínají na nule.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Data Storytelling: Animovaný přechod k rozhodnutí

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Flourish](https://flourish.studio/) (Online)
> **Postup**: Interpretace má oddělovat zjištění, vysvětlení a doporučení. Zkuste si ve Flourish vytvořit bezplatný účet, vyberte formát "Story" (Příběh). Vložte jeden výchozí graf a do druhého snímku udělejte "zoom" na konkrétní odlehlý bod, o kterém text píše (např. učebnu, kde extrémně roste CO₂). Animace pomáhá čtenáři projít vaším argumentem od začátku do konce.


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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Graf jako odpověď, ne jako dekorace“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Trend, predikce a odpovědný datový workflow

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato kapitola varuje, že matematická extrapolace do neznáma je riskantní a ukazuje limity práce jak s modely, tak s osobními údaji. 

### Experiment 6.1: Riziko Extrapolace: Když model věští

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Desmos Graphing Calculator](https://www.desmos.com/) (Online)
> **Postup**: Lineární regrese popíše data přímkou (y = ax + b). Vložte do levého sloupce v Desmos body: (0, 10), (5, 20), (10, 30). Nástroj proloží rovnoměrně stoupající přímku (reprezentující např. spotřebu energie při klesající venkovní teplotě). Oddalte zobrazení (zoom out) na X = 200. Zamyslete se a vysvětlete, proč by tato matematická interpolace v realitě narazila (fyzikální limit kotle, zničení budovy).

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Klouzavý průměr vyhlazující šum

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/) (Online)
> **Postup**: Zdroje říkají, že kolísavý průběh lze vyhladit okénkem sousedních hodnot. Vyhledejte na webu jakoukoliv divokou časovou řadu (např. spotřeba energie). V sekci "Edit Graph" přidejte druhou čáru a nastavte úpravu (Units) na "Moving Average" v délce 12 měsíců. Vizuálně porovnejte, jak delší okno vyhladí krátké výkyvy, ale začne reagovat se zpožděním.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Overfitting (Přeučení modelu na trénovacích datech)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [TensorFlow Playground](https://playground.tensorflow.org/) (Online)
> **Postup**: Je nutné používat trénovací a testovací data, jinak model selže na neviděných případech. Otevřete hřiště neuronových sítí. Zaškrtněte políčko "Show test data". Nechte model, ať se učí složitou strukturu (velký počet neuronů a skrytých vrstev). Sledujte, jak se po dlouhé době pozadí (předpověď) začne klikatit, jen aby zasáhlo každý jeden "trénovací" bod. Model se přeučil.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Ověření AI asistenta (Halucinace z podstaty)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: ChatGPT, Gemini, Copilot (Libovolný LLM chat)
> **Postup**: Text varuje, že AI nemá skrytou správnou odpověď, může zaměnit sloupce nebo tvrdit kauzalitu z korelace. Vložte do chatu jednoduchý dotaz: "V tabulce mi klesá spotřeba energie, a ve stejném období klesl i prodej nanuků. Proč prodej nanuků ovlivňuje školní kotelnu?" Sledujte, zda se AI chytí do pasti a začne obhajovat kauzalitu, nebo vás (správně) upozorní na chybějící souvislost.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Pseudonymizace vs. Anonymizace v datech

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Tabulkový procesor (LibreOffice/Excel)
> **Postup**: Pouhé smazání jména z databáze (pseudonymizace) nestačí pro ochranu soukromí. Vytvořte si sešit se 3 žáky a sloupci: `Třída`, `Pohlaví`, `Omluvené hodiny`, `Datum narození`. Smažte sloupec se jmény a zkuste si odpovědět, zda víte, kdo je ve škole jediný "Chlapec, narozený v dubnu 2011 z 8.B s 50 absencemi". Potvrďte si, že kombinace znaků vytvořila nevratný unikátní identifikátor a k anonymizaci nedošlo.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Reprodukovatelný projektový sešit

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google Colab](https://colab.research.google.com/) (Online)
> **Postup**: Dobrý datový projekt umožňuje, aby kdokoli ověřil postup i závěr. Založte si zdarma Jupyter Notebook v Google Colab. Prostředí ukazuje, jak lze střídat vysvětlující dokumentaci a reálný postup. Přidejte jeden blok formátovaného "Textu", kam napíšete "Toto je jednoduchý pokus" a jeden blok "Kódu", kam zadáte jednoduchý příkaz (např. matematickou rovnici 2+2) a stisknete "Run". Vznikne vám plně reprodukovatelný log vašich myšlenek i práce.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Trend, predikce a odpovědný datový workflow“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
