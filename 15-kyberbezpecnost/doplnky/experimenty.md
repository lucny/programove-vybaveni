<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní a bezpečně vedená laboratorní cvičení.
-->

# Laboratoř: Kyberbezpečnost

> **⚠️ Upozornění k nástrojům a bezpečnosti**
>
> Teoretické principy vycházejí ze studijních materiálů. Konkrétní nástroje a postupy jsou praktickým doplněním a jejich rozhraní se mohou změnit. Používejte pouze vlastní testovací data; nezadávejte hesla, tokeny, osobní údaje, licencovaný obsah ani údaje z cizích účtů. Bezpečnostní jevy zkoumejte popisně, v lokálním labu nebo v explicitně určeném výukovém sandboxu.

## Jak pracovat v laboratoři

> **🗂️ Pracovní zápis**
>
> Ke každé úloze vyplňte **předpověď**, **postup**, **pozorování**, **vysvětlení** a **omezení**. Nejprve popisujte fakta, teprve potom z nich vyvozujte závěr.

> **🧰 Význam bloků**
>
> - **💡 Koncept / 🎯 Cíl** vysvětluje, který princip ověřujete.
> - **🧰 Nástroj** uvádí prostředí; cílem není naučit se klikání, ale porozumět technologii.
> - **🧭 Postup** provádějte po malých, kontrolovatelných krocích.
> - **🔎 Ověření** přemění aktivitu v doložený výsledek.

> **📝 Šablona zápisu do laboratorního deníku**
>
> Tento blok lze zkopírovat pod každý experiment a vyplnit vlastním obsahem.

```text
Předpověď:
Pozorování / důkaz:
Vysvětlení pojmem z kapitoly:
Omezení nebo zdroj možné chyby:
```

> „Pozorování není vysvětlení; vysvětlení spojuje důkaz s principem.“
>
> — laboratorní zásada pro tuto lekci


Tento dokument obsahuje praktické úlohy a experimenty, které slouží k reálnému otestování konceptů probíraných v jednotlivých kapitolách. Ke každému experimentu je přiložen návodný postup a odkaz na využitý nástroj.

## 1. Kyberprostor, hrozby a řízení bezpečnosti

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Tato kapitola definuje kyberprostor a CIA triádu (důvěrnost, integrita, dostupnost) a ukazuje, jak se řídí rizika.

### Experiment 1.1: Identifikace aktiv a modelování hrozeb (Papír/Notepad)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit rovnici aktivum → hrozba → zranitelnost.
> **Postup**: 1. Vypište svá 3 nejcennější digitální aktiva (např. e-mail, bankovnictví, fotky). 2. Ke každému napište 2 hrozby (např. krádež telefonu, zapomenuté heslo). 3. Identifikujte svou zranitelnost (např. nemám zálohu). 4. Navrhněte opatření (zapnutí automatické zálohy).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.2: Otestování zranitelnosti softwaru (NVD NIST)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, jak se evidují chyby v programech.
> **Nástroj**: [National Vulnerability Database (NVD)](https://nvd.nist.gov/)
> **Postup**: 1. Otevřete NVD. 2. Do vyhledávání (Search Vulnerabilities) zadejte verzi vašeho prohlížeče (např. "Chrome 114"). 3. Projděte si nalezené zranitelnosti (CVE) a podívejte se na jejich závažnost (CVSS skóre).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.3: Zkoumání fyzické infrastruktury internetu (Shodan)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Uvědomit si, že kyberprostor stojí na fyzickém hardwaru.
> **Nástroj**: [Shodan.io](https://www.shodan.io/)
> **Postup**: 1. Zaregistrujte si bezplatný účet. 2. Prohlédněte si pouze veřejnou úvodní stránku, vysvětlující články nebo poskytnutý učitelský snímek výsledků. 3. Popište, proč samotná veřejná viditelnost zařízení ještě nedává oprávnění se k němu připojit ani jej testovat.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.4: Ověření úniku osobních údajů (Have I Been Pwned)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zkontrolovat narušení důvěrnosti vašich dat.
> **Nástroj**: [Have I Been Pwned](https://haveibeenpwned.com/)
> **Postup**: 1. Použijte připravený fiktivní příklad nebo se pod dohledem učitele seznamte s ukázkovým výsledkem. Nevkládejte školní ani cizí e-mailové adresy. 2. Z ukázky určete, jaký typ údajů mohl uniknout a které kroky by měl majitel účtu následně provést. 3. Navrhněte bezpečnou reakci: změna hesla, zapnutí MFA, kontrola znovupoužití hesla a obezřetnost vůči navazujícím podvodům.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.5: Sledování útoků v reálném čase (Kaspersky Cybermap)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vizualizovat globální hrozby a útoky.
> **Nástroj**: [Kaspersky Cyberthreat Real-Time Map](https://cybermap.kaspersky.com/)
> **Postup**: 1. Otevřete mapu a přepněte do 2D/3D zobrazení. 2. Sledujte, jaké typy hrozeb (např. ODS - On-Demand Scanner zachycení) jsou nejčastější v ČR. 3. V menu prozkoumejte statistiky nejvíce zasažených zemí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.6: Simulace narušení dostupnosti (DoS na vlastní kůži)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vyzkoušet si útok na dostupnost (Denial of Service).
> **Nástroj**: Vestavěné nastavení sítě ve Windows/mobilu.
> **Postup**: 1. Zapněte si na mobilním telefonu a počítači "Režim letadlo" (odpojení od sítě). 2. Zkuste pracovat 15 minut – otevřít kalendář, číst dokumenty, přehrát hudbu. 3. Sepište si, které služby byly nedostupné a jak silná byla vaše závislost na cloudu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Kyberprostor, hrozby a řízení bezpečnosti“ a vysvětlete ho na vlastním konkrétním pozorování.

## 2. Malware a sociální inženýrství

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Kapitola rozebírá šíření škodlivého softwaru a psychologickou manipulaci (phishing, baiting).

### Experiment 2.1: Analýza podezřelého souboru bez otevření (VirusTotal)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Naučit se skenovat přílohy více antiviry najednou.
> **Nástroj**: [VirusTotal](https://www.virustotal.com/)
> **Postup**: 1. Vezměte libovolný běžný soubor (např. PDF). 2. Nahrajte jej na portál VirusTotal. 3. Počkejte na analýzu od desítek antivirových motorů. 4. Prozkoumejte záložky "Details" a "Behavior", které ukazují, jak by se soubor zachoval v systému.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.2: Test rozpoznání phishingu (Google Phishing Quiz)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Prakticky si otestovat obranu proti sociálnímu inženýrství.
> **Nástroj**: [Google Phishing Quiz](https://phishingquiz.withgoogle.com/)
> **Postup**: 1. Otevřete kvíz a zadejte libovolné (klidně fiktivní) jméno a e-mail. 2. Pozorně čtěte ukázkové e-maily a hádejte, zda jde o "Phishing" nebo "Legitimní". 3. Prostudujte si vysvětlení u každé odpovědi, proč e-mail obsahoval varovné znaky (např. falešná doména).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.3: Bezpečný náhled na podezřelý odkaz (URLScan.io)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Prohlédnout si podvodný web bez rizika nákazy.
> **Nástroj**: [URLScan.io](https://urlscan.io/)
> **Postup**: 1. Najděte zkrácený odkaz (např. na sociálních sítích). 2. Vložte jej do URLScan a spusťte sken. 3. Nástroj web navštíví za vás a pořídí jeho screenshot, ukáže vám, kam přesně odkazuje a z jaké země server běží.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.4: Odhalení maskované identity v e-mailu (Hlavičky zpráv)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit skutečného odesílatele a nenaletět autoritě.
> **Nástroj**: Váš e-mailový klient (Gmail, Outlook).
> **Postup**: 1. Otevřete libovolný e-mail ve své schránce. 2. V Gmailu klikněte na tři tečky vpravo nahoře a zvolte "Zobrazit originál" (Show original). 3. Najděte položky `Return-Path:` a ověřte výsledky SPF a DKIM testů, které odhalují, zda e-mail není podvržen.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.5: Zkoumání triků v sociálním inženýrství (PhishTank)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Poznat, jak přesně útočníci napodobují známé značky.
> **Nástroj**: [PhishTank](https://www.phishtank.com/)
> **Postup**: 1. Běžte na stránky PhishTank. 2. Klikněte na "Verify a phish". 3. Prohlédněte si seznam aktuálně nahlášených útoků. 4. Všimněte si domén, které útočníci používají pro napodobení Microsoftu, PayPal nebo bank.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.6: Práce v izolovaném prostředí (Windows Sandbox)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Omezit prostor pro spuštění neznámého kódu.
> **Nástroj**: Windows Sandbox (součást Windows 10/11 Pro/Enterprise).
> **Postup**: 1. Otevřete nabídku Start a najděte "Zapnout nebo vypnout funkce systému Windows". 2. Zaškrtněte "Windows Sandbox" pouze na počítači, kde to povoluje správce, a restartujte PC. 3. Spusťte Windows Sandbox. 4. Vytvořte uvnitř vlastní neškodný textový soubor nebo spusťte předem připravený učitelský program typu „Hello“. 5. Sandbox zavřete a znovu otevřete; ověřte, že testovací soubor zmizel. Nezískávejte ani nespouštějte neznámé programy nebo malware.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Malware a sociální inženýrství“ a vysvětlete ho na vlastním konkrétním pozorování.

## 3. Rozpoznání napadení a vícevrstvá obrana

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Tato část zdůrazňuje, že prevence nestačí a je třeba budovat obranu do hloubky, analyzovat logy a testovat zálohy.

### Experiment 3.1: Sledování vlastních logů a procesů (Prohlížeč událostí)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Hledat stopy po incidentech a podezřelých událostech.
> **Nástroj**: Prohlížeč událostí (Event Viewer) ve Windows.
> **Postup**: 1. Stiskněte Win+R, napište `eventvwr` a potvrďte. 2. Jděte do Protokoly systému Windows -> Zabezpečení. 3. Hledejte Událost ID 4624 (Úspěšné přihlášení) nebo ID 4625 (Neúspěšné přihlášení). 4. Ověřte, zda se do vašeho PC nesnažil přihlásit někdo jiný.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.2: Audit skrytých a po startu spouštěných programů (Autoruns)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Detekovat potenciální rootkity či spyware běžící na pozadí.
> **Nástroj**: [Sysinternals Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns) (od Microsoftu).
> **Postup**: 1. Stáhněte a spusťte Autoruns jako správce. 2. Projděte si záložku "Logon". Zde vidíte vše, co se spouští se systémem. 3. Klikněte na "Options" a zaškrtněte "Check VirusTotal.com". 4. Nechte program prověřit všechny soubory a hledejte ty s červeným hodnocením.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.3: Odposlech vlastního síťového provozu (Wireshark)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Porozumět paketům a zjistit, co vidí případný útočník na síti.
> **Nástroj**: [Wireshark](https://www.wireshark.org/)
> **Postup**: 1. Nainstalujte Wireshark. 2. Vyberte svůj aktivní síťový adaptér (např. Wi-Fi) a klikněte na "Start capturing". 3. Otevřete prohlížeč a načtěte libovolnou stránku. 4. Zastavte zachytávání. Do filtru nahoře napište `http` nebo `dns`. 5. Zkuste v paketech přečíst, jaká data odcházejí v čitelné podobě.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.4: Pravidlo 3-2-1 a obnova zálohy (Test obnovy)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, zda vaše záloha funguje dříve, než zaútočí ransomware.
> **Nástroj**: Libovolný zálohovací program, který používáte (např. Historie souborů Windows), a stopky.
> **Postup**: 1. Vytvořte si složku s testovacími dokumenty a zálohujte je na externí disk. 2. Smažte testovací složku z PC. 3. Zapněte stopky. 4. Pokuste se složku z externího disku obnovit zpět. 5. Zapište si čas a zhodnoťte, zda byste takto dokázali obnovit celý počítač.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.5: Skenování zranitelností domácí sítě (Nmap)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Odhalit nepovolená zařízení (IoT, cizí mobily) ve vaší síti.
> **Nástroj**: [Zenmap / Nmap](https://nmap.org/zenmap/)
> **Postup**: 1. Zjistěte svou lokální IP adresu (přes `ipconfig` v příkazovém řádku, např. 192.168.1.5). 2. Do Zenmap do pole Target zadejte `192.168.1.0/24` (pokryje celou síť). 3. Zvolte profil "Quick scan" a odklepněte. 4. Zkontrolujte nalezená zařízení a otevřené porty.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.6: Principy firewallu v praxi (Windows Defender Firewall)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vyzkoušet si blokování síťové komunikace programu.
> **Nástroj**: Brána Windows Defender Firewall s pokročilým zabezpečením.
> **Postup**: 1. Otevřete nastavení firewallu ve Windows. 2. Vlevo klikněte na "Odchozí pravidla" a vytvořte "Nové pravidlo". 3. Vyberte cestu k libovolnému nainstalovanému webovému prohlížeči (např. Edge). 4. Zvolte "Blokovat připojení". 5. Zkuste v prohlížeči načíst stránku – firewall ji zablokuje. Následně pravidlo smažte.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Rozpoznání napadení a vícevrstvá obrana“ a vysvětlete ho na vlastním konkrétním pozorování.

## 4. Digitální identita, autentizace a hesla

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Tato část se zaměřuje na vícefaktorovou autentizaci (MFA), délku hesla, passkeys a ochranu před útoky hrubou silou [56–62].

### Experiment 4.1: Analýza odolnosti hesel (How Secure Is My Password)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Uvědomit si vliv délky hesla při útoku Brute force.
> **Nástroj**: [Security.org - How Secure Is My Password](https://www.security.org/how-secure-is-my-password/)
> **Postup**: 1. Otevřete stránku. *(Upozornění: Nikdy nezadávejte své skutečné heslo, pouze testovací obměny!)* 2. Zadejte "Heslo2026!". Zjistíte, že prolomení trvá velmi krátce. 3. Zadejte "ZelenaZabaSkacePresKaluze". Uvidíte, jak radikálně delší heslová fráze prodlouží čas potřebný k prolomení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.2: Instalace a použití správce hesel (Bitwarden)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Odbourat nutnost pamatovat si desítky hesel a řešit jejich jedinečnost.
> **Nástroj**: [Bitwarden](https://bitwarden.com/)
> **Postup**: 1. Nainstalujte si rozšíření Bitwarden do prohlížeče. 2. Vytvořte si jedno silné, dlouhé "Hlavní heslo" (Master Password). 3. Zkuste si ve správci vygenerovat náhodné 20místné heslo a uložte jej jako přístup k fiktivní službě.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.3: Nasazení druhého faktoru - TOTP (Google Authenticator / Authy)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Nastavit nezávislý prvek (Něco, co mám) pro ochranu účtu.
> **Nástroj**: Aplikace Authy nebo Google Authenticator v mobilu.
> **Postup**: 1. Stáhněte si aplikaci do mobilního telefonu. 2. Přihlaste se na svůj účet např. na Facebooku, Googlu nebo GitHubu. 3. V nastavení bezpečnosti najděte "Zapnout dvoufázové ověření (Aplikace)". 4. Naskenujte mobilem zobrazený QR kód a zadejte vygenerovaný 6místný kód. 


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.4: Vyzkoušení technologie Passkeys (Passkeys.io)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit přihlašování založené na asymetrické kryptografii bez hesel.
> **Nástroj**: [Passkeys.io](https://www.passkeys.io/)
> **Postup**: 1. Z mobilu nebo PC s otiskem prstu/Windows Hello jděte na web Passkeys.io. 2. Klikněte na "Try Passkeys". 3. Vytvořte si fiktivní účet – místo hesla vás zařízení vyzve k biometrickému ověření nebo zadání PINu k zařízení. 4. Odhlaste se a znovu přihlaste, abyste viděli, jak je proces plynulý.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.5: Zkoumání kompromitovaných hesel (Have I Been Pwned: Passwords)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ověřit riziko znovupoužití hesla (Credential stuffing).
> **Nástroj**: [HIBP Passwords](https://haveibeenpwned.com/Passwords)
> **Postup**: 1. Běžte do sekce Passwords pouze tehdy, pokud učitel poskytl fiktivní demonstrační řetězec; nikdy nezadávejte vlastní ani cizí skutečné heslo. 2. Z ukázkového výsledku vyčtěte, proč častý nebo znovupoužitý řetězec představuje riziko. 3. Navrhněte bezpečnější alternativu: dlouhou jedinečnou heslovou frázi uloženou ve správci hesel.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.6: Audit znovupoužitých hesel v prohlížeči (Chrome/Edge)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Aplikovat princip jedinečnosti hesel.
> **Nástroj**: Správce hesel ve vašem prohlížeči (např. Chrome Password Manager).
> **Postup**: 1. Prostudujte si dokumentaci nebo učitelský snímek funkce „Zkontrolovat hesla“; neotevírejte ani nesdílejte seznam vlastních uložených přístupů před třídou. 2. Pojmenujte tři typy varování: slabé heslo, kompromitované heslo a opakované použití. 3. Navrhněte bezpečnou reakci pro fiktivní účet: vytvořit jedinečné heslo ve správci, zapnout MFA a staré heslo odstranit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Digitální identita, autentizace a hesla“ a vysvětlete ho na vlastním konkrétním pozorování.

## 5. Ochrana dat a kryptografie

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Kapitola řeší šifrování dat v klidu a při přenosu, hashovací funkce a problematiku TLS certifikátů.

### Experiment 5.1: Výpočet hashe pro kontrolu integrity (PowerShell / CyberChef)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ověřit, že i nepatrná změna dat radikálně změní hash.
> **Nástroj**: Windows PowerShell (vestavěný nástroj).
> **Postup**: 1. Vytvořte na ploše textový dokument `test.txt` s textem "Ahoj". 2. Otevřete PowerShell a napište `Get-FileHash C:\Users\VaseJmeno\Desktop\test.txt`. 3. Zapište si výsledný SHA256 hash. 4. Změňte v souboru jedno písmeno na "ahoj", uložte a vypočítejte hash znovu. Porovnejte propastný rozdíl.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.2: Symetrické šifrování dat at rest (7-Zip)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ochránit soubor heslem (algoritmem AES) před narušením důvěrnosti.
> **Nástroj**: [7-Zip](https://www.7-zip.org/)
> **Postup**: 1. Vytvořte složku s citlivým obrázkem. 2. Klikněte na ni pravým tlačítkem a zvolte 7-Zip -> "Přidat do archivu...". 3. V sekci "Šifrování" zadejte silné heslo a ujistěte se, že je vybrána metoda AES-256. 4. Zaškrtněte i "Šifrovat názvy souborů" a potvrďte. Zkuste archiv otevřít bez hesla.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.3: Kontrola důvěryhodnosti TLS certifikátu (Prohlížeč)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Otestovat end-to-end šifrování k webu (data in transit) a PKI.
> **Nástroj**: Webový prohlížeč.
> **Postup**: 1. Otevřete stránku vaší banky. 2. Klikněte na ikonu zámku v adresním řádku a zvolte "Zabezpečené připojení" -> "Certifikát je platný". 3. Zkoumejte detaily: Kdo certifikát vydal (Vydavatel)? Jakému subjektu? Jaká je doba platnosti?


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.4: Analýza šifrování serveru (SSL Labs)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Otestovat sílu konfigurace TLS libovolného webu.
> **Nástroj**: [Qualys SSL Labs Server Test](https://www.ssllabs.com/ssltest/)
> **Postup**: 1. Otevřete stránku SSL Labs. 2. Zadejte libovolnou URL adresu (např. e-shopu nebo školy). 3. Počkejte několik minut na výsledek testu. 4. Sledujte výslednou známku (A až F) a zjistěte, zda server nepodporuje nebezpečné a staré protokoly.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.5: Asymetrické šifrování zprávy (CyberChef)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit roli veřejného a soukromého klíče (šifrování pro příjemce).
> **Nástroj**: [CyberChef](https://gchq.github.io/CyberChef/)
> **Postup**: 1. Otevřete nástroj a do "Recipe" přidejte "Generate PGP Key Pair". 2. Vygenerujte si klíče a zkopírujte veřejný klíč. 3. Recipe vymažte a přidejte "PGP Encrypt". 4. Do nastavení vložte dříve zkopírovaný veřejný klíč. 5. Do pole "Input" zadejte tajnou zprávu. Získáte zašifrovaný ciphertext, který rozšifruje už jen držitel soukromého klíče.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.6: Ověření End-to-End E2EE komunikace (Signal/WhatsApp)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Znemožnit Man-in-the-Middle útok potvrzením klíčů.
> **Nástroj**: Signal nebo WhatsApp na mobilu.
> **Postup**: 1. Otevřete chat s kamarádem, se kterým sedíte ve stejné místnosti. 2. Klikněte na jeho jméno a najděte "Ověřit bezpečnostní kód" / "Bezpečnostní čísla". 3. Naskenujte QR kód z jeho telefonu. Tím nezávisle potvrdíte, že komunikace putuje šifrovaně přímo mezi vašimi zařízeními a nikdo třetí neposlouchá.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Ochrana dat a kryptografie“ a vysvětlete ho na vlastním konkrétním pozorování.

## 6. Bezpečnost jako proces: od jednotlivce k organizaci

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.

Závěrečná kapitola staví bezpečnost jako nepřetržitý proces zaměřený na Zero Trust, inventarizaci, aktualizace a omezení privilegií [73–77].

### Experiment 6.1: Inventarizace osobních aktiv (Papír/Excel)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, co vlastně musíte chránit (první krok bezpečnostního procesu).
> **Nástroj**: Tabulkový procesor (Excel) nebo papír.
> **Postup**: 1. Projděte domácnost a zapište si všechna IT aktiva (PC, mobil, router, chytrá TV, robotický vysavač). 2. U každého zapište operační systém. 3. Zhodnoťte kritičnost (Nízká/Vysoká) a datum poslední kontroly aktualizace.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.2: Audit třetích stran a aplikací v cloudu (Správa Google/Apple účtu)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Uplatnit Zero trust přístup pro cloudové služby a model sdílené odpovědnosti.
> **Nástroj**: [Zabezpečení Google Účtu](https://myaccount.google.com/security) (nebo obdoba u Applu/Microsoftu).
> **Postup**: 1. Přihlaste se do svého Google účtu a jděte na kartu "Zabezpečení". 2. Sjeďte k sekci "Vaše propojení s aplikacemi a službami třetích stran". 3. Rozklikněte seznam. 4. Najděte a smažte oprávnění starým aplikacím a hrám, které již nepoužíváte, ale mají přístup k vašemu e-mailu či disku.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.3: Nastavení principu nejmenších oprávnění (Windows Účty)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zabránit tomu, aby lidská chyba poskytla malwaru administrátorský přístup k PC.
> **Nástroj**: Nastavení účtů Windows.
> **Postup**: 1. Ve Windows přejděte do Nastavení -> Účty -> Rodina a jiní uživatelé. 2. Přidejte "Dalšího uživatele" bez účtu Microsoft. 3. Vytvořte lokální účet typu "Standardní uživatel" (ne Správce!). 4. Přihlaste se na tento účet a používejte ho pro běžné surfování. Zjistíte, že instalace programů nebo smazání klíčových souborů najednou vyžaduje potvrzení administrátorským heslem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.4: Segmentace chytré domácnosti (Nastavení Routeru)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Oddělit nezabezpečená IoT zařízení od pracovních počítačů (obrana do hloubky).
> **Nástroj**: Administrace vašeho domácího Wi-Fi routeru.
> **Postup**: 1. Přihlaste se do správy vašeho domácího routeru (často 192.168.1.1 v prohlížeči). 2. Najděte funkci "Guest Network" (Síť pro hosty). 3. Vytvořte nezávislou síť se samostatným heslem a ujistěte se, že je zaškrtnuto "Izolovat od lokální sítě". 4. Připojte do ní chytré žárovky nebo televize. Pokud je někdo napadne, nedostane se do vašeho osobního PC.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.5: Zhodnocení konce životního cyklu softwaru (End of Life Audit)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Řídit rizika starých zranitelností, na které již neexistují opravy.
> **Nástroj**: Vyhledávač / Nastavení PC.
> **Postup**: 1. Zkontrolujte verzi operačního systému na všech telefonech a PC v rodině. 2. Najděte datum vydání poslední bezpečnostní aktualizace. 3. Pomocí webu (např. *endoflife.date*) vyhledejte daný systém (třeba Windows 10 nebo Android 11) a zjistěte, zda je tento systém ještě podporován výrobcem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.6: Návrh plánu reakce na incident (Word/Papír)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Být připraveni v souladu s fázemi incident response (detekce → reakce → obnova).
> **Nástroj**: Dokument ve Wordu.
> **Postup**: 1. Sepište si konkrétní krizový plán (tzv. Playbook) pro situaci "Ukradli mi na ulici odemčený telefon". 2. Jaká jsou tři nejdůležitější telefonní čísla (na papíře, protože mobil nemáte)? 3. Jaká je přesná URL adresa pro vzdálené vymazání vašeho zařízení přes účet Google/Apple? 4. Které bankovní karty musíte zablokovat a jak? (Tento postup si vytiskněte a uschovejte).

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

[[ Který závěr z experimentu je nejkvalitnější? ]]

[( )] „Nástroj ukázal výsledek, proto je úloha hotová.“
[(X)] „Výsledek doložím, vysvětlím probíraným principem a uvedu hranici modelu nebo nástroje.“
[( )] „Stačí zopakovat název technologie.“

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Bezpečnost jako proces: od jednotlivce k organizaci“ a vysvětlete ho na vlastním konkrétním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| formulovat bezpečný test a předpověď |  |  |
| zaznamenat důkaz výsledku |  |  |
| vysvětlit výsledek odborným pojmem |  |  |
| pojmenovat omezení modelu či nástroje |  |  |
| zachovat ochranu dat a hranice oprávnění |  |  |
