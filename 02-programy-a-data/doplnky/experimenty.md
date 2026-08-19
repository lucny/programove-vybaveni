<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Programové vybavení, operační systémy a cloud

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


Tento dokument obsahuje sadu 36 praktických úloh (6 pro každou kapitolu), které propojují teorii operačních systémů, virtualizace a cloudu s reálnými ukázkami pomocí dostupného softwaru.

---

## 1. Kapitola: Soubory, adresáře a data na disku

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 1.1: Změna přípony a chování operačního systému

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Průzkumník Windows / Finder (integrovaný)
> **Cíl**: Demonstrovat, že přípona je pouze vizuální identifikátor pro asociaci aplikací, ale samotná data nemění.
> **Postup**: 
    1. Ve Správci souborů povolte zobrazení přípon souborů (Zobrazení > Zobrazit přípony názvů souborů).
    2. Zkopírujte libovolný malý obrázek (`obrazek.jpg`) na plochu.
    3. Přejmenujte jej na `obrazek.txt`. 
    4. Sledujte, jak se změní ikona souboru. Poklepáním soubor otevřete – systém spustí Poznámkový blok a pokusí se číst obrázek jako rozsypaný text.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Zkoumání bajtových signatur (Magic numbers)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [HexEd.it](https://hexed.it/) (zdarma online)
> **Cíl**: Ukázat, jak operační systém bezpečně rozpozná formát uvnitř souboru.
> **Postup**: 
    1. Otevřete webovou stránku HexEd.it.
    2. Nahrajte na web původní obrázek `obrazek.jpg` nebo `.png`.
    3. V hexa výpisu prozkoumejte první řádek dat. Naleznete tam unikátní hlavičku (např. `89 50 4E 47` pro PNG), které se neformálně říká magic number.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Stromová vizualizace pomocí příkazové řádky (CLI)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazový řádek / PowerShell
> **Cíl**: Pochopit stromovou strukturu adresářů a absolutní a relativní cesty.
> **Postup**: 
    1. Otevřete Příkazový řádek (cmd.exe).
    2. Přejděte na disk C: (příkaz `cd C:\`).
    3. Napište příkaz `tree /F | more` (parametr /F vypíše i soubory).
    4. Sledujte vizualizaci logického stromu složek, který se liší od fyzického uložení na disku.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Skript jako text a běžící program

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Notepad++](https://notepad-plus-plus.org/) a CLI
> **Cíl**: Dokázat, že hranice mezi "textovým" a "programovým" souborem není absolutní.
> **Postup**: 
    1. V Notepad++ vytvořte soubor a vložte do něj kód: `echo Ahoj svete` a na další řádek `pause`.
    2. Uložte jej na plochu jako `test.bat`.
    3. Dvojklikem na ploše jej spusťte jako běžící program. Následně jej znovu otevřete v editoru jako běžný textový dokument.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Skutečný formát vs. falešná maska

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [TrID Online](https://mark0.net/soft-trid-e.html)
> **Cíl**: Odhalit skrytý obsah v souboru s matoucí nebo falešnou příponou (např. riziko u faktura.pdf.exe).
> **Postup**: 
    1. Vezměte libovolný PDF dokument, přejmenujte jeho příponu na `.mp3`.
    2. Nahrajte tento poškozený "MP3" soubor do online analyzátoru TrID.
    3. Nástroj ignoruje příponu a podle struktury neomylně vyhodnotí pravděpodobnost, že se jedná o PDF dokument.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Anatomie jednoho programu v mnoha procesech

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Sysinternals Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
> **Cíl**: Rozlišit program uložený na disku od množiny procesů v běžící paměti.
> **Postup**: 
    1. Stáhněte a spusťte Process Explorer.
    2. Otevřete webový prohlížeč (Chrome/Firefox) a otevřete 5 různých webových stránek.
    3. V Process Exploreru najděte proces prohlížeče – vizuálně uvidíte, že jde o strom desítek vnořených, izolovaných a spolupracujících procesů (karet a rozšíření).

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Soubory, adresáře a data na disku“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Kapitola: Systémové a aplikační programy

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 2.1: Analýza procesorové platformy a UEFI

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [CPU-Z](https://www.cpuid.com/softwares/cpu-z.html)
> **Cíl**: Ukázat platformu, na které operační systém a hardware fungují.
> **Postup**: 
    1. Spusťte nástroj CPU-Z.
    2. Na kartě *CPU* analyzujte instrukční sady (např. x86-64, AVX), které určují kompatibilitu aplikačního kódu.
    3. Na kartě *Mainboard* zkontrolujte verzi a datum svého BIOS/UEFI firmware (rozhraní pod operačním systémem).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Sledování komunikace přes API

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Sysinternals Process Monitor (ProcMon)](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
> **Cíl**: Ukázat roli OS jako prostředníka při zápisu dat.
> **Postup**: 
    1. Spusťte ProcMon (začne automaticky zachytávat události).
    2. Otevřete Poznámkový blok a uložte prázdný soubor.
    3. V ProcMonu filtrujte proces `notepad.exe` a vyhledejte událost "WriteFile". Uvidíte přesně API volání, kterým aplikace žádá jádro (kernel) OS o obsloužení disku.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Zkoumání ovladačů (Drivers)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DriverView](https://www.nirsoft.net/utils/driverview.html)
> **Cíl**: Ukázat, kolik softwaru stojí mezi OS a samotným hardwarem.
> **Postup**: 
    1. Spusťte jednoduchou utilitu DriverView.
    2. Skryjte ovladače od Microsoftu (View -> Hide Windows Drivers).
    3. Prohlédněte si seznam ovladačů dodaných výrobci třetích stran (pro grafiku, síť či Wi-Fi), které překládají systémové povely do řeči hardwaru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Překlad kódu pro různé platformy v reálném čase

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Compiler Explorer (Godbolt)](https://godbolt.org/)
> **Cíl**: Demonstrovat překlad pro x86-64 vs. ARM64 (kompatibilita architektury).
> **Postup**: 
    1. Otevřete Godbolt ve webovém prohlížeči.
    2. Nalevo zadejte jednoduchý C++ kód (např. funkce sčítání).
    3. Napravo přidejte dva překladače: jeden pro x86-64 (např. x86-64 gcc) a druhý pro ARM. Sledujte, jak se ze stejného kódu tvoří naprosto odlišné strojové instrukce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Síťový provoz napříč systémovými vrstvami

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Wireshark](https://www.wireshark.org/)
> **Cíl**: Vyzkoušet síťové diagnostické nástroje.
> **Postup**: 
    1. Nainstalujte a spusťte Wireshark. Vyberte svůj aktivní síťový adaptér.
    2. Otevřete příkazový řádek a proveďte ping na libovolný server (např. `ping 8.8.8.8`).
    3. Ve Wiresharku zastavte snímání a najděte ICMP pakety, které prošly od vaší utility až k síťové kartě.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Vrstvy moderní webové aplikace

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Wappalyzer](https://www.wappalyzer.com/) (Doplněk do prohlížeče)
> **Cíl**: Pochopit, že i aplikace je vrstvený systém backendu, databází a frontendu.
> **Postup**: 
    1. Nainstalujte Wappalyzer do prohlížeče.
    2. Přejděte na populární web (např. e-shop nebo blog).
    3. Klikněte na ikonu doplňku. Zobrazí se seznam vrstev: operační systém serveru, webový server, databáze a javascriptové knihovny.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Systémové a aplikační programy“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Kapitola: Softwarové licence

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 3.1: Překlad nesrozumitelné licence (MIT, GPL)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [TLDRLegal](https://tldrlegal.com/)
> **Cíl**: Rozlišit permisivní a copyleftové licence.
> **Postup**: 
    1. Otevřete web TLDRLegal.
    2. Vyhledejte "GNU GPL v3" (copyleftová) a porovnejte ji s licencí "MIT" (permisivní).
    3. Projděte si sloupce "Can, Cannot, Must". Zjistíte, že i open source podmiňuje použití přesnými pravidly (např. zachování copyrightové poznámky).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Vyhledání skrytých hrozeb v EULA

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [ToS;DR (Terms of Service; Didn't Read)](https://tosdr.org/)
> **Cíl**: Prověřit podmínky proprietárního softwaru, cloudových služeb a konzumace uživatelských dat.
> **Postup**: 
    1. Na webu ToS;DR vyhledejte vaši oblíbenou sociální síť nebo cloudové úložiště.
    2. Prozkoumejte sekci rizik ("Grade"). Zjistíte, zda služba například omezuje možnosti právních sporů (Class Action Waiver), což je častý rys EULA.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Konfigurátor licencí Creative Commons

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Creative Commons License Chooser](https://chooser-beta.creativecommons.org/)
> **Cíl**: Vytvořit vhodnou CC licenci (vhodné pro multimédia, na rozdíl od kódu).
> **Postup**: 
    1. Otevřete průvodce CC.
    2. Interaktivně zaškrtněte, že chcete povolit modifikace díla, ale pouze k nekomerčním účelům.
    3. Nástroj automaticky vygeneruje grafický odznak a text licenci "CC BY-NC".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Výběr licence pro vlastní programovací projekt

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Choose a License](https://choosealicense.com/)
> **Cíl**: Zjistit, že repozitář na webu není automaticky volně dostupný bez licenčního souboru.
> **Postup**: 
    1. Představte si, že publikujete kód, u kterého chcete, aby se na odvozená díla musela vztahovat stejná práva (copyleft).
    2. Proklikejte se průvodcem na webu a zjistěte, jaký text ze standardního katalogu musíte vložit do souboru `LICENSE.md` ve vašem adresáři.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Analýza softwarové kompozice (SCA) s FOSSA

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [FOSSA CLI](https://fossa.com/) / [ClearlyDefined.io](https://clearlydefined.io/)
> **Cíl**: Vyzkoušet si podnikovou identifikaci závislostí a licenčních limitů.
> **Postup**: 
    1. V ClearlyDefined zadejte jméno libovolného známého open source balíčku (např. `react` nebo `vue`).
    2. Systém zkontroluje podkladová data (source-available status, patenty) a oznámkuje balíček dle čistoty autorských práv.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Nalezení Freeware/FOSS alternativy s uzavřeným softwarem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [AlternativeTo.net](https://alternativeto.net/)
> **Cíl**: Prakticky rozlišit mezi placeným proprietárním SW, předplatným a Open Source.
> **Postup**: 
    1. Najděte známý proprietární software na předplatné (např. Adobe Photoshop).
    2. Nastavte filtr licencování výhradně na "Open Source".
    3. Identifikujte alternativy (např. GIMP, Krita) a ověřte si na jejich webu pod jakou svobodnou licencí operují.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Softwarové licence“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Kapitola: Emulace a virtualizace

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 4.1: Instalace virtuálního stroje (Hosted hypervisor)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Oracle VM VirtualBox](https://www.virtualbox.org/)
> **Cíl**: Vytvořit virtuální stroj typu Type 2 hypervisor, přidělit mu RAM a jádra.
> **Postup**: 
    1. Stáhněte a nainstalujte VirtualBox.
    2. Vytvořte nový počítač, nastavte mu 2GB virtuální operační paměti a připojte stažený ISO obraz (např. Ubuntu Linux).
    3. Spusťte guest systém – izolovaný OS poběží ve vašem okně s vlastním kernelem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Magie snapshotů ve virtuálním stroji

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: VirtualBox (z předchozího kroku)
> **Cíl**: Vyzkoušet záznam stavu a okamžitý návrat, ověřit, že to není záloha dat.
> **Postup**: 
    1. Když virtuální systém z experimentu 4.1 běží, klikněte na volbu Pořídit snímek (Snapshot).
    2. Uvnitř virtuálního systému úmyslně smažte důležitý soubor z plochy.
    3. Virtuální stroj vypněte a použijte volbu Obnovit snapshot. Soubor bude okamžitě zpět.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Emulace historické platformy

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DOSBox](https://www.dosbox.com/)
> **Cíl**: Nasimulovat procesor a paměťovou mapu původního MS-DOSu.
> **Postup**: 
    1. Nainstalujte DOSBox.
    2. Vytvořte lokální adresář na vašem disku (např. `C:\stare_hry`).
    3. Příkazem `mount c c:\stare_hry` uvnitř DOSBoxu namapujete složku do emulovaného hardwaru a vyzkoušíte překlad architektury.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Kontejnerizace s webovým serverem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Podman](https://podman.io/) (nebo Docker)
> **Cíl**: Demonstrovat, že kontejnery nejsou malé virtuální stroje a sdílí jádro OS.
> **Postup**: 
    1. Nainstalujte Podman (do Windows přes WSL nebo na Linuxu).
    2. V terminálu spusťte `podman run -p 8080:80 nginx`.
    3. Tento příkaz stáhne aplikační obraz a spustí izolovaný server Nginx sdílející systémový kernel. Web uvidíte na adrese localhost:8080.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Překlad instrukcí uvnitř webového prohlížeče

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [WebVM.io](https://webvm.io/)
> **Cíl**: Vyzkoušet extrémní formu emulace a WebAssembly přímo na webu.
> **Postup**: 
    1. Otevřete v prohlížeči stránku WebVM.
    2. Během chvíle nabootuje plnohodnotný terminál Debian Linuxu přímo ve vašem prohlížeči, aniž by na pozadí běžel dedikovaný cloudový server. Celý běh je emulován lokálně.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Kompatibilní vrstva

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Dokumentace Microsoft WSL](https://learn.microsoft.com/en-us/windows/wsl/)
> **Cíl**: Spustit nativní Linuxový kód ve Windows pomocí kompatibilní vrstvy / skryté virtualizace.
> **Postup**: 
    1. Otevřete PowerShell jako administrátor a spusťte příkaz `wsl --install`.
    2. Po restartu a konfiguraci otevřete Linuxový terminál ve Windows.
    3. Příkazem `cd /mnt/c` přejděte na váš fyzický Windows disk (propojení světů).

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Emulace a virtualizace“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Kapitola: Cloudové služby

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 5.1: Rozdíl mezi IaaS a PaaS v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Vercel](https://vercel.com/) (PaaS) vs libovolný VPS poskytovatel
> **Cíl**: Ukázat provozní model PaaS, kde uživatel neřeší operační systém.
> **Postup**: 
    1. Založte si bezplatný účet na platformě Vercel (PaaS).
    2. Vyberte šablonu statického webu a nasaďte ji (Deploy).
    3. Všimněte si, že jste se nestarali o instalaci Apache, síť ani OS (na rozdíl od modelu IaaS).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Objektové cloudové úložiště vs. Stromový adresář

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Cyberduck](https://cyberduck.io/)
> **Cíl**: Prozkoumat cloudová úložiště prostřednictvím API místo klasických adresářů.
> **Postup**: 
    1. Stáhněte klienta Cyberduck.
    2. Můžete se připojit na AWS S3 testovací bucket, nebo na existující cloud (OneDrive/Google Drive).
    3. Sledujte, že nástroj nepřipojuje disk přes písmeno (jako `D:`), ale přistupuje k logickým objektům čistě síťovým tunelem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Nebezpečí automatické synchronizace

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Syncthing](https://syncthing.net/)
> **Cíl**: Dokázat varování ze skript, že "synchronizace není záloha".
> **Postup**: 
    1. Spusťte Syncthing na dvou složkách (nebo zařízení, např. PC a mobil).
    2. Do složky uložte dokument, počkejte na obousměrnou synchronizaci.
    3. Smažte soubor z prvního zařízení – téměř okamžitě zmizí i z druhého. 


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Lokální nasazení cloudových služeb (Místní AWS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [LocalStack](https://localstack.cloud/)
> **Cíl**: Odpojit cloud od cloudu – ukázat, že jde primárně o vrstvu rozhraní.
> **Postup**: 
    1. Spusťte kontejner LocalStack.
    2. Pomocí příkazové řádky simulujte požadavek na AWS S3 bucket. Emulátor API vrátí stejná data, jako byste komunikovali se skutečným veřejným datovým centrem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Návrh cloudové infrastruktury (Architektura)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Draw.io / diagrams.net](https://app.diagrams.net/)
> **Cíl**: Namodelovat hybridní cloud strategii chránící před vendor lock-in.
> **Postup**: 
    1. Otevřete online kreslící nástroj.
    2. Načtěte ikonografii AWS (nebo Azure).
    3. Nakreslete architekturu, kde privátní databáze zůstává za lokálním firewallem (Private cloud), ale webový server se dynamicky škáluje ve veřejném cloudu s balancerem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: FinOps a složitost účtování cloudu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Online Pricing Calculator (např. Azure Pricing Calculator)
> **Cíl**: Odhalit složitost cloudového škálování a měření využití.
> **Postup**: 
    1. Otevřete oficiální cloudovou kalkulačku.
    2. Přidejte virtuální server, obrovské množství síťového odchozího trafficu (např. 50 TB) a databázovou managed službu.
    3. Všimněte si, že cloud není automaticky levnější, a analyzujte cenu za sítě a elasticitu.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Cloudové služby“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Kapitola: Správa programů a dat

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 6.1: Instalace přes terminálového správce balíčků

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Winget (integrován ve Windows 11) / APT v Linuxu
> **Cíl**: Vyzkoušet moderní a zabezpečenou formu stahování repozitářů namísto klikání na setup.exe.
> **Postup**: 
    1. Spusťte Příkazový řádek (cmd.exe).
    2. Napište `winget search VLC` pro nalezení balíčku (řeší zdroj balíčku a verzi).
    3. Nainstalujte program povělem `winget install VideoLAN.VLC`. O automatizaci a stažení se postará OS.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Bezpečnost instalačního dodavatelského řetězce

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [VirusTotal](https://www.virustotal.com/)
> **Cíl**: Kontrola původu softwaru a hashe pro obranu proti *supply-chain attack*.
> **Postup**: 
    1. Stáhněte si na disk drobný bezplatný program (třeba instalátor Putty).
    2. Nahrajte tento `.exe` soubor na web VirusTotal.
    3. Zkontrolujte záložku Details: podívejte se na sekci s digitálním podpisem, zda je platný a vypočtený kontrolní součet odpovídá oficiální stránce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: "Sirotčí" soubory po odinstalaci

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Bulk Crap Uninstaller (BCUninstaller)](https://www.bcuninstaller.com/)
> **Cíl**: Demonstrovat, že odinstalace záměrně ponechává cache a složité závislosti v systému.
> **Postup**: 
    1. Nainstalujte do systému novou aplikaci a poté ji nechte BCUninstallerem odebrat.
    2. Nástroj vám graficky vykreslí vše, co běžný odinstalátor zapomněl (zápisy v registrech Windows, zbytkové cache složky v AppData) a nabídne jejich hluboké odstranění.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Historické zranitelnosti z End-of-Life (EOL) softwaru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [CVE Details](https://www.cvedetails.com/)
> **Cíl**: Doložit nebezpečí používání programů mimo podporu bez aktualizací.
> **Postup**: 
    1. Na portálu zadejte například "Windows 7" nebo prastarou verzi vašeho oblíbeného prohlížeče.
    2. Prohlédněte si seznam bezpečnostních chyb (CVE) označených jako kritické, na které útočníkům stačí jen běžně dostupné automatizované skripty (protože už neexistuje oprava).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Pravidlo 3-2-1 a neměnné zálohy v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Kopia](https://kopia.io/)
> **Cíl**: Naučit se oddělit produkční data od zašifrovaných, historických bodů v čase (řeší ransomwarový incident).
> **Postup**: 
    1. Stáhněte si zálohovací software Kopia.
    2. Vyberte prázdnou složku na externím disku nebo v cloudu jako "Repository".
    3. Nastavte zálohu složky "Dokumenty". Důležité: Kopia neukládá data čitelná přes běžný průzkumník. Šifruje je a drží deduplikované historie v čase. Ransomware by smazal pouze zašifrované bloky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Životní cyklus a neviditelná data v "Koši"

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Recuva (od CCleaneru)](https://www.ccleaner.com/recuva)
> **Cíl**: Fyzicky ukázat, že smazání do Koše a z Koše nemění bloky dat na paměťovém médiu a lze to obnovit.
> **Postup**: 
    1. Vložte starý (nedůležitý) USB Flash disk, vložte tam obrázek a použijte klávesy Shift + Delete (trvalé smazání).
    2. Spusťte nástroj Recuva a naskenujte disk.
    3. Uvidíte "neviditelný" soubor. Klikněte na Obnovit (Recover) a data jsou bezpečně zpět. Diskuze nad retenčními mechanismy a minimalizací dat je na místě.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Kapitola: Správa programů a dat“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
