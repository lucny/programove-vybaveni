<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní a bezpečně vedená laboratorní cvičení.
-->

# Laboratoř: Základy programování a algoritmizace

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


*Upozornění: Koncepty, definice a teorie v tomto dokumentu vycházejí přímo z vašich zdrojových textů. Konkrétní zmíněné aplikace, online nástroje a podrobné kroky k experimentům však ve zdrojích uvedeny nejsou. Jedná se o mé externí znalosti, které jsem začlenil, abych splnil váš požadavek na praktické procvičení teoretických poznatků. Doporučuji si funkčnost odkazů a nástrojů případně nezávisle ověřit.*

Tento dokument obsahuje 36 praktických úloh (6 pro každou kapitolu) navržených tak, aby s využitím bezplatných nástrojů otestovaly a vizualizovaly koncepty popsané ve vašem textu.

---

## 1. Základní pojmy z programování

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


V této kapitole se zaměřujeme na to, co je to algoritmus, program a jak fungují překladače. 

### Experiment 1.1: Analýza algoritmu z reálného života

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit, že algoritmus je přesný a konečný postup řešení s jasnými kroky.
> **Nástroj**: Poznámkový blok (Notepad) ve Windows.
> **Postup**: 
    1. Otevřete Poznámkový blok.
    2. Představte si algoritmus „Uvař čaj“ z textu a zkuste ho rozepsat detailněji (např. co když v konvici není voda?).
    3. Přidejte podmínky (tzv. rozhodování). Příklad: „Pokud je konvice prázdná -> Napusť vodu. Jinak -> Zapni konvici.“ 
    4. Zkontrolujte, zda váš postup splňuje konečnost, definovanost a má vstupy a výstupy.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.2: Testování kompilovaného vs. interpretovaného jazyka

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Poznat rozdíl mezi kompilátorem (překládá vše najednou) a interpretem (překládá řádek po řádku).
> **Nástroj**: [Replit](https://replit.com/) (online editor).
> **Postup**: 
    1. Na Replit.com si bez přihlášení otevřete prostředí pro jazyk **Python** (interpretovaný jazyk). 
    2. Napište na první řádek `print("Ahoj")` a na druhý chybový řádek `print(1/0)`. Spusťte program. Všimněte si, že se nejprve vypíše "Ahoj" a až pak program spadne.
    3. Otevřete si prostředí pro jazyk **C++** (kompilovaný jazyk) a napište podobný chybný kód. 
    4. Všimněte si, že u C++ kompilátor nahlásí chybu předem a program se vůbec nespustí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.3: Vytvoření programu v prohlížeči (Kalkulačka)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Napsat jednoduchý program přijímající vstupy a provádějící výpočty.
> **Nástroj**: [Programiz Python Compiler](https://www.programiz.com/python-programming/online-compiler/).
> **Postup**: 
    1. Otevřete odkaz s online překladačem.
    2. Smažte předpřipravený kód a vložte svůj: `a = int(input("Zadej cislo: "))` a na další řádek `print(a * 2)`.
    3. Klikněte na "Run" a do konzole napište číslo.
    4. Sledujte, jak počítač jako výstup zobrazí dvojnásobek čísla.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.4: Úprava webové stránky (Značkovací vs. programovací jazyky)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ověřit si, že HTML/CSS jsou značkovací a stylovací jazyky, nikoliv plnohodnotné programovací jazyky.
> **Nástroj**: Webový prohlížeč (Chrome/Edge/Firefox).
> **Postup**: 
    1. Otevřete libovolnou webovou stránku (např. Google).
    2. Stiskněte klávesu `F12` (Nástroje pro vývojáře) a přejděte na záložku `Elements` (Prvky).
    3. Najděte libovolný text na stránce, dvakrát na něj klikněte a přepište ho.
    4. Sledujte změnu. Všimněte si, že HTML definuje pouze strukturu a vzhled, ale neobsahuje žádné instrukce pro výpočty jako programovací jazyky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.5: Vizualizace zpracování instrukcí pomocí Python Tutor

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vidět na vlastní oči, jak počítač (procesor) zpracovává zdrojový kód instrukci po instrukci.
> **Nástroj**: [Python Tutor](https://pythontutor.com/).
> **Postup**: 
    1. Klikněte na "Start visualizing your code now".
    2. Vložte jednoduchý skript, např. tři řádky: `x = 5`, `y = 10`, `z = x + y`.
    3. Klikněte na "Visualize Execution".
    4. Tlačítkem "Next" krokujte program a sledujte, jak se v paměti postupně vytvářejí proměnné.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 1.6: Generování Bytecode v Pythonu

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Prozkoumat mezikrok mezi zdrojovým a strojovým kódem (bytecode).
> **Nástroj**: Online kompilátor Pythonu s modulem dis (např. [JDoodle](https://www.jdoodle.com/python3-programming-online/)).
> **Postup**: 
    1. Vložte do editoru kód: `import dis` a na další řádek definujte jednoduchou funkci `def secist(a, b): return a + b`.
    2. Na třetí řádek dejte příkaz `dis.dis(secist)`.
    3. Spusťte program. Ve výpisu uvidíte "bytecode" – instrukce virtuálního stroje (jako `LOAD_FAST`, `BINARY_ADD`), které python interpret používá k vykonání kódu.

---


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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Základní pojmy z programování“ a vysvětlete ho na vlastním konkrétním pozorování.

## 2. Vývoj programování, nižší a vyšší programovací jazyky

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


Zde otestujeme rozdíly v syntaxi a úrovni abstrakce mezi nižšími (assembler) a vyššími (C++, Python) jazyky.

### Experiment 2.1: Zkoumání Strojového Kódu (Binární reprezentace)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit, že programy jsou uloženy jako binární posloupnosti nul a jedniček, kterým rozumí procesor.
> **Nástroj**: [HexEd.it](https://hexed.it/) (Online Hex editor).
> **Postup**: 
    1. Otevřete stránku HexEd.it.
    2. Klikněte na "Open file" a nahrajte jakýkoliv malý spustitelný soubor z vašeho Windows (např. `C:\Windows\notepad.exe`).
    3. Sledujte hexa a binární reprezentaci. Všimněte si, že je to pro člověka nečitelné. Tyto hodnoty reprezentují přesné instrukce pro procesor.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.2: Simulace Assembleru (Nižší jazyk)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zkusit si programování v jazyce blízkém hardwaru pomocí mnemotechnických zkratek.
> **Nástroj**: [Little Man Computer (LMC)](https://peterhigginson.co.uk/LMC/).
> **Postup**: 
    1. Otevřete LMC simulátor.
    2. Do levého okna napište instrukce v assembleru: `INP` (načti), `STA 99` (ulož do paměti 99), `OUT` (vypiš), `HLT` (zastav).
    3. Klikněte na "Submit" a poté na "Run".
    4. Sledujte, jak simulovaný procesor načítá instrukce a přesouvá data (abstrakce je velmi nízká).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.3: Srovnání vyššího jazyka C++ a Assembleru

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vidět, jak kompilátor převádí vysokoúrovňový, dobře čitelný kód na nižší instrukce (assembler).
> **Nástroj**: [Compiler Explorer](https://godbolt.org/).
> **Postup**: 
    1. Otevřete stránku a v levém okně nechte předvolený jazyk C++ (nebo napište kód: `int square(int num) { return num * num; }`).
    2. V pravém okně se automaticky vygeneruje odpovídající kód v Assembleru (instrukce jako `mov`, `imul`).
    3. Můžete vidět, jak jeden řádek ve vyšším jazyce vyžaduje hned několik instrukcí v nižším jazyce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.4: Otestování příkazového řádku Bash (Doménově orientovaný jazyk)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Práce s jazykem určeným pro skriptování v operačních systémech.
> **Nástroj**: [JDoodle Bash](https://www.jdoodle.com/test-bash-shell-script-online/).
> **Postup**: 
    1. Otevřete online simulátor Bash.
    2. Napište jednoduchý skript pro vypsání textu a obsahu adresáře: `echo "Ahoj z Bashe"` a na další řádek `ls -la`.
    3. Spusťte kód. Vidíte, že tento jazyk je přímo uzpůsoben k práci se systémem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.5: Zkoumání databázového jazyka SQL

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Spustit kód v doménově orientovaném jazyce, který slouží výhradně pro práci s databázemi.
> **Nástroj**: [DB Fiddle](https://www.db-fiddle.com/).
> **Postup**: 
    1. V levém panelu "Schema SQL" vytvořte tabulku: `CREATE TABLE test (id INT, jmeno VARCHAR(10)); INSERT INTO test VALUES (1, 'Karel');`.
    2. V pravém panelu "Query SQL" napište příkaz k vytažení dat: `SELECT * FROM test;`.
    3. Klikněte na "Run" a pozorujte tabulkový výsledek.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 2.6: Vysoká úroveň abstrakce v jazyce Java

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ukázat si kód typického aplikačního vyššího jazyka určeného pro podnikové aplikace s velmi čitelnou syntaxí.
> **Nástroj**: [W3Schools Java Tryit](https://www.w3schools.com/java/tryjava.asp?filename=demo_helloworld).
> **Postup**: 
    1. V editoru si prohlédněte kód. Najdete zde slova z přirozeného jazyka (angličtiny) jako `public`, `class`, `System.out.print`.
    2. Změňte text v uvozovkách na `"Test vyssiho jazyka"`.
    3. Spusťte program. Všimněte si, že na rozdíl od Assembleru programátor vůbec nemusí řešit přidělování paměti nebo registry.

---


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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Vývoj programování, nižší a vyšší programovací jazyky“ a vysvětlete ho na vlastním konkrétním pozorování.

## 3. Princip fungování programu v počítači

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


Kapitola se věnuje cyklu CPU, procesům, operační paměti a vláknům.

### Experiment 3.1: Analýza procesů ve Správci úloh

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vidět rozdíl mezi programem (souborem na disku) a procesem (běžící instancí v paměti).
> **Nástroj**: Správce úloh (Ctrl+Shift+Esc ve Windows).
> **Postup**: 
    1. Otevřete Správce úloh a přejděte na záložku "Podrobnosti" (nebo "Procesy").
    2. Spusťte aplikaci Kalkulačka. Sledujte, jak v seznamu přibyl nový aktivní proces `CalculatorApp.exe`.
    3. Spusťte Kalkulačku podruhé. Uvidíte druhý proces – ze stejného programu na disku běží dvě aktivní instance.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.2: Sledování využití vláken (Multithreading)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit, že jeden proces může obsahovat více vláken sdílejících paměť.
> **Nástroj**: Sledování prostředků (Resource Monitor ve Windows).
> **Postup**: 
    1. Klikněte na Start, napište `resmon` a spusťte jej.
    2. Přejděte na záložku "Procesor".
    3. V tabulce procesů se podívejte do sloupce "Vlákna" (Threads).
    4. Najděte proces webového prohlížeče (např. `chrome.exe` nebo `msedge.exe`) a sledujte, že používá desítky vláken k paralelnímu načítání dat a vykreslování.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.3: Testování cyklu Načti-Dekóduj-Vykonej

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Simulovat krok za krokem základní cyklus práce procesoru CPU.
> **Nástroj**: [CPU Simulator](https://cpusimulator.com/).
> **Postup**: 
    1. Otevřete simulátor v prohlížeči.
    2. Přidejte pár jednoduchých bloků (instrukcí).
    3. Spusťte běh "krok za krokem" (Step-by-step).
    4. Vizuálně sledujte, jak se hodnota z RAM nejprve načte do CPU, procesor pochopí (dekóduje), co má dělat, a teprve poté instrukci vykoná.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.4: Oddělení paměťového prostoru procesů

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pochopit, že operační systém přiděluje procesům vlastní paměťový prostor a navzájem si do něj nesmí zasahovat.
> **Nástroj**: Správce úloh (Záložka Výkon/Paměť).
> **Postup**: 
    1. Otevřete Správce úloh a podívejte se na kartu Paměť.
    2. Spusťte libovolnou náročnější aplikaci (např. prohlížeč s mnoha záložkami).
    3. Sledujte, jak OS dynamicky alokuje paměť tomuto konkrétnímu procesu.
    4. Ukončete proces; OS paměť uvolní (ochrana RAM).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.5: Simulace ukazatelů v paměti (C++)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Prozkoumat funkci "pointerů", které uchovávají adresu do paměti místo samotné hodnoty.
> **Nástroj**: [C++ Tutor](https://pythontutor.com/cpp.html).
> **Postup**: 
    1. Do editoru vložte kód: 
       `int cislo = 10;`
       `int* ukazatel = &cislo;`
    2. Klikněte na "Visualize Execution".
    3. V grafickém znázornění na pravé straně uvidíte, že proměnná `cislo` obsahuje hodnotu 10, ale proměnná `ukazatel` obsahuje paměťovou adresu (šipku ukazující na `cislo`).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 3.6: Ukázka automatické správy paměti (Garbage Collector v Pythonu)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, jak vyšší jazyky skrývají práci s pamětí před programátorem.
> **Nástroj**: Libovolný online Python editor (např. [Programiz](https://www.programiz.com/)).
> **Postup**: 
    1. V editoru napište: 
       `import gc`
       `print("Garbage collector bezi:", gc.isenabled())`
    2. Spusťte program. Vypíše se `True`.
    3. Uvědomte si, že na rozdíl od C++ nemusíte v Pythonu ručně uvolňovat paměť. Virtuální stroj a garbage collector tuto těžkou práci dělají sami.

---


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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Princip fungování programu v počítači“ a vysvětlete ho na vlastním konkrétním pozorování.

## 4. Algoritmizace, možnost zápisu algoritmů

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


Tato kapitola představuje způsoby analýzy problému a vizualizace algoritmů pomocí vývojových diagramů a pseudokódu.

### Experiment 4.1: Kreslení vývojového diagramu online

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Správně poskládat symboly vývojového diagramu pro jednoduchý algoritmus.
> **Nástroj**: [Draw.io](https://app.diagrams.net/).
> **Postup**: 
    1. Zvolte "Create New Diagram" a vyberte "Blank Diagram".
    2. Pomocí menu vlevo ("Flowchart") přetáhněte na plátno tvary: Ovál (Začátek), Paralelogram (Vstup čísla), Obdélník (Výpočet: vynásob 2), Paralelogram (Výstup), Ovál (Konec).
    3. Propojte prvky šipkami určujícími tok řízení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.2: Vizualizace větvení (Rozhodovací bod ve vývojovém diagramu)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Použití kosočtverce pro rozhodnutí (např. sudé/liché číslo).
> **Nástroj**: [Draw.io](https://app.diagrams.net/).
> **Postup**: 
    1. S využitím předchozího diagramu přidejte doprostřed Kosočtverec.
    2. Do kosočtverce napište podmínku: "Je číslo dělitelné 2 beze zbytku?".
    3. Z kosočtverce vyveďte dvě šipky: jednu popsanou "Ano" (vede k operaci pro sudé číslo), druhou "Ne" (vede k operaci pro liché číslo).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.3: Návrh algoritmu zapsaný pomocí Pseudokódu

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Napsat textový algoritmus strukturovaným jazykem (bez nutnosti dodržovat přísnou syntaxi kompilátoru).
> **Nástroj**: Poznámkový blok.
> **Postup**: 
    1. Vymyslete úkol: Nalezení největšího čísla v seznamu o 5 prvcích.
    2. Otevřete textový editor a zapište kroky:
       `ZAČÁTEK`
       `  Vezmi první číslo ze seznamu a ulož ho jako "Maximum".`
       `  PRO každé další číslo v seznamu DĚLEJ:`
       `    POKUD je číslo větší než "Maximum":`
       `      Ulož toto číslo jako nové "Maximum".`
       `  VYPIŠ "Maximum"`
       `KONEC`


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.4: Vizualizace hotového algoritmu krok za krokem

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Sledovat efektivní postup existujícího známého algoritmu na vizuálním grafu.
> **Nástroj**: [VisuAlgo.net](https://visualgo.net/en/sorting).
> **Postup**: 
    1. Otevřete odkaz s vizualizací třídících algoritmů.
    2. Vyberte "Bubble Sort" (jeden z běžných algoritmů zmíněných v textu).
    3. Klikněte na tlačítko "Play" vlevo dole a sledujte, jak animace přesně provádí opakované procházení pole.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.5: Automatické generování diagramu z pseudokódu

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vytvořit vývojový diagram pomocí textového zápisu.
> **Nástroj**: [PlantUML Web](https://www.plantuml.com/plantuml/uml/).
> **Postup**: 
    1. Otevřete generátor PlantUML.
    2. Smažte obsah a vložte následující kód zastupující běh programu:
       `@startuml`
       `start`
       `:Zadej vstup;`
       `if (Je vstup platný?) then (ano)`
       `  :Zpracuj data;`
       `else (ne)`
       `  :Zobraz chybu;`
       `endif`
       `stop`
       `@enduml`
    3. Klikněte na "Submit" a podívejte se na vygenerovaný graf. Tvary přesně odpovídají logice toku řízení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 4.6: Analýza problému myšlenkovou mapou

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vyzkoušet si první krok algoritmizace – analýzu problému a požadavků.
> **Nástroj**: [Miro.com](https://miro.com/) (nebo prostý papír).
> **Postup**: 
    1. Otevřete novou myšlenkovou mapu (nebo nakreslete na papír středový kruh s nápisem "E-shop nákupní košík").
    2. Vyznačte hlavní větve: Vstupy (produkty, ceny), Zpracování (výpočet DPH, slevy), Výstupy (celková částka).
    3. Pro každý uzel dodejte specifické omezení (např. co dělat, když je produkt vyprodán). Tím analyzujete budoucí rozhodovací body algoritmu.

---


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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Algoritmizace, možnost zápisu algoritmů“ a vysvětlete ho na vlastním konkrétním pozorování.

## 5. Základní prvky syntaxe programovacího jazyka

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


Pátá kapitola řeší správný přepis algoritmu do konkrétního jazyka, chyby a debugování.

### Experiment 5.1: Analýza syntaktické chyby

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, jak překladač reaguje na porušení syntaktických pravidel (např. chybějící dvojtečka).
> **Nástroj**: [Online Python Compiler](https://www.online-python.com/).
> **Postup**: 
    1. Vložte vadný kód s porušenou syntaxí (chybí dvojtečka a odsazení):
       `if 5 > 2`
       `print("Vetsi")`
    2. Klikněte na "Run".
    3. V konzoli se objeví hlášení: `SyntaxError`. Překladač detekoval chybu v zápisu a kód vůbec nespustil.
    4. Opravte kód přidáním dvojtečky a mezer (odsazení je v Pythonu určující pro bloky kódu).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.2: Vyvolání běhové chyby (Runtime Error)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Vidět chybu, kterou překladač pustí, ale kód kvůli ní „spadne“ během vykonávání (běhu).
> **Nástroj**: [Online Python Compiler](https://www.online-python.com/).
> **Postup**: 
    1. Napište syntakticky naprosto správný kód:
       `a = 10`
       `b = 0`
       `print(a / b)`
    2. Spusťte program. 
    3. Obdržíte chybovou hlášku podobnou `ZeroDivisionError: division by zero`. Jde o typickou běhovou chybu – dělení nulou.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.3: Sémantická chyba (Logická chyba)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Napsat kód, který je syntakticky správně, nezhavaruje, ale dá špatný (nechtěný) výsledek.
> **Nástroj**: Notepad + Mozeček (jakýkoliv editor).
> **Postup**: 
    1. Úkol: Vypočítej průměr dvou čísel 10 a 20.
    2. Napište v libovolném jazyce výpočet: `prumer = 10 + 20 / 2`.
    3. Kód doběhne v pořádku, ale výsledek bude `20` místo `15`. Jde o logickou/sémantickou chybu, protože jste zapomněli na závorky pro prioritu operací `(10 + 20) / 2`. Tyto chyby překladač neodhalí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.4: Ladění programu pomocí Debuggeru (Krokování)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Použít debugger pro sledování toku hodnot během běhu a hledání sémantických chyb.
> **Nástroj**: [Python Tutor - Debugger](https://pythontutor.com/).
> **Postup**: 
    1. Vložte do Python Tutor kód, který má opakující se cyklus (např. výpočet faktoriálu z textu):
       `faktorial = 1`
       `for i in range(1, 4):`
       `    faktorial = faktorial * i`
    2. Klikněte na "Visualize". 
    3. Každým stiskem "Next" (krokování kódu) pečlivě sledujte v tabulce, jak se po každém průběhu cyklu dynamicky mění hodnota proměnné `faktorial` (nejprve 1, pak 2, pak 6). 


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.5: Logování jako nástroj k odhalení chyby

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Pokud nemáte debugger, použití logování (printů) pomáhá pochopit, co se v programu děje.
> **Nástroj**: Jakýkoliv online editor pro C nebo Python.
> **Postup**: 
    1. Máme komplikovaný kód bez debuggeru:
       `def proved_kalkulaci(x):`
       `    return (x * 5) - 20`
    2. Představte si, že nám kód vrací špatné hodnoty a nevíme proč.
    3. Přidejte kontrolní logovací výpis: 
       `def proved_kalkulaci(x):`
       `    print("Vstupní hodnota do funkce je:", x) # TOTO JE LOGOVÁNÍ`
       `    return (x * 5) - 20`
    4. Výstupní zprávy (logy) pomohou sledovat průběh.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 5.6: Rozdílná syntaxe při deklaraci proměnných (Python vs. C)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: V praxi otestovat převod myšlenky do různých programovacích jazyků s odlišnou syntaxí.
> **Nástroj**: [JDoodle](https://www.jdoodle.com/).
> **Postup**: 
    1. Otevřete záložku s Pythonem. Deklarujte proměnnou (prostým přiřazením): `moje_cislo = 5; print(moje_cislo)`. Funguje ihned.
    2. Otevřete záložku s jazykem C. Zkuste zadat to samé. Kompilátor zahlásí chybu syntaxe.
    3. Opravte kód do správné C syntaxe s použitím datového typu a složených závorek pro funkci main:
       `int main() {`
       `    int moje_cislo = 5;`
       `    printf("%d", moje_cislo);`
       `    return 0;`
       `}`

---


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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Základní prvky syntaxe programovacího jazyka“ a vysvětlete ho na vlastním konkrétním pozorování.

## 6. Efektivita algoritmů a volba řešení

> **🎯 Cíl kapitoly**
>
> Spojujte popsaný postup s příčinou a důsledkem: co systém přijímá, jak to zpracuje a jak poznáte, že výsledek odpovídá modelu.


Tato obsáhlá kapitola vysvětluje Big O notaci, rozdíl mezi konstantní, lineární a kvadratickou náročností, třídění a vyhledávání [21–42].

### Experiment 6.1: Analýza Konstantního času O(1)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ukázat si, že načtení prvku přesně na známé pozici (indexu) trvá stejně dlouho, ať je prvků kolik chce.
> **Nástroj**: Konzole prohlížeče (F12 -> Console).
> **Postup**: 
    1. Vložte do konzole pole o 5 prvcích: `let data = [5, 2, 9, 1, 7];`
    2. Přístup k prvku na druhém indexu: `data;` (Vrátí 30).
    3. Prohlížeč k číslu "skočí" okamžitě. Nezáleží na tom, že by pole `data` mělo milion čísel. Přístup k indexu nezvyšuje náročnost – jde o konstantní čas O(1).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.2: Test Lineárního času O(n)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Zjistit, že u hledání v neuspořádaném seznamu musí program vykonat tolik kroků, kolik je dat.
> **Nástroj**: [Python Online Compiler](https://www.programiz.com/python-programming/online-compiler/).
> **Postup**: 
    1. Vložte cyklus simulující hledání v seznamu:
       `seznam =`
       `kroky = 0`
       `for cislo in seznam:`
       `    kroky = kroky + 1`
       `    if cislo == 3:`
       `        print("Nalezeno za kroků:", kroky)`
    2. Spusťte. Číslo 3 je na konci, smyčka (lineární vyhledávání) se provedla 5x. Počet kontrol roste úměrně s množstvím prvků O(n).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.3: Test Kvadratického času O(n²)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Proč je u vnořených cyklů velký počet položek problém? Otestovat vzoreček n × n.
> **Nástroj**: [Python Online Compiler](https://www.programiz.com/python-programming/online-compiler/).
> **Postup**: 
    1. Vložte kód s vnořeným cyklem:
       `n = 10`
       `pocet_operaci = 0`
       `for i in range(n):`  # Vnější cyklus
       `    for j in range(n):`  # Vnitřní cyklus
       `        pocet_operaci += 1`
       `print("Operací celkem:", pocet_operaci)`
    2. Při `n=10` je operací 100. Změňte proměnnou `n` na 1000 a spusťte kód znovu.
    3. Uvidíte, že z 1000 prvků vzešlo 1 000 000 operací. To je O(n²).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.4: Lineární vs. Binární vyhledávání v praxi

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ukázat si, jak binární vyhledávání O(log n) dramaticky redukuje kroky potřebné k nalezení seřazených dat.
> **Nástroj**: Hra "Hádej číslo" (bez počítače nebo v konzoli).
> **Postup**: 
    1. Poproste kamaráda, ať si myslí číslo od 1 do 100.
    2. *Lineární přístup*: Ptejte se "Je to 1? Je to 2? Je to 3?". Může to trvat až 100 kroků.
    3. *Binární přístup*: Ptejte se tak, ať zahodíte polovinu. "Je to víc než 50?". "Ano". -> "Je to víc než 75?". "Ne". -> "Je to víc než 62?".
    4. Všimněte si, že tímto dělením intervalu dojdete k výsledku maximálně za 7 kroků. Podmínkou ale je, že čísla v intervalu jsou matematicky "seřazená".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.5: Srovnání "Bubble Sortu" a Vestavěného Třídění

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Ověřit si, proč je lepší použít otestovanou vestavěnou knihovnu místo psaní pomalého Bubble Sortu s náročností O(n²).
> **Nástroj**: [Replit Python](https://replit.com/).
> **Postup**: 
    1. Napište do konzole kód pro vestavěné řazení z textu:
       `teploty =`
       `serazeno = sorted(teploty)`
       `print(serazeno)`
    2. Nyní si v mysli vzpomeňte na princip Bubble Sortu, který by stejný úkol prováděl neustálým porovnáváním a prohazováním dvojic dokola. Vestavěná funkce `sorted()` je interně optimalizovaná a běží mnohem rychleji.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz: snímek obrazovky, výpis programu, tabulku výsledků nebo odkaz na vlastní test.
> - Popište přesnou změnu hodnot, výstupu, schématu či chování; nestačí napsat „funguje“.
> - Vysvětlete ji odborným pojmem z kapitoly a doplňte jedno omezení použitého nástroje nebo modelu.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Jiný než očekávaný výsledek je platný výsledek, pokud jej umíte rozebrat.

### Experiment 6.6: Odstranění zbytečných výpočtů (Optimalizace kódu)

> **🧭 Laboratorní postup**
>
> 1. Nejprve napište předpověď: *jaký výsledek očekávám a proč*.
> 2. Postupujte po jednotlivých krocích; po každé podstatné změně se zastavte a zapište, co se skutečně stalo.
> 3. Pracujte pouze s vlastními, testovacími nebo výslovně veřejnými daty. Pokud narazíte na účet, přístupový údaj či cizí systém, experiment zastavte.

> **Cíl**: Demonstrovat zrychlení programu odstraněním "opakovaného provádění stejného výpočtu", což je častá varovná známka neefektivity.
> **Nástroj**: [Python Online Compiler](https://www.programiz.com/python-programming/online-compiler/).
> **Postup**: 
    1. Vložte kód s neefektivním opakováním:
       `def ziskej_konstantu(): return 50 # simulace těžkého výpočtu`
       `data =`
       `for cislo in data:`
       `    vysledek = cislo + ziskej_konstantu()`
       `    print(vysledek)`
    2. Uvědomte si, že funkce `ziskej_konstantu()` se volá pro každé kolo cyklu znovu.
    3. Přesuňte volání funkce ven z cyklu podle textu:
       `hodnota = ziskej_konstantu()`
       `for cislo in data:`
       `    vysledek = cislo + hodnota`
    4. Tato drobná změna zabrání zbytečné námaze počítače a v praxi s mnoha daty by kód masivně zrychlila.

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

> **💬 Reflexe kapitoly:** Vyberte jeden pojem z části „Efektivita algoritmů a volba řešení“ a vysvětlete ho na vlastním konkrétním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| formulovat bezpečný test a předpověď |  |  |
| zaznamenat důkaz výsledku |  |  |
| vysvětlit výsledek odborným pojmem |  |  |
| pojmenovat omezení modelu či nástroje |  |  |
| zachovat ochranu dat a hranice oprávnění |  |  |
