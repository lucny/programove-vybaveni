<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Informační a databázové systémy

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


## 1. Informační systémy v digitální době

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

Tato kapitola vysvětluje základní pojmy, rozdíl mezi daty a informacemi a pět klíčových složek informačního systému (lidé, procesy, data, software, infrastruktura). 

### Experiment 1.1: Přeměna dat v informace pomocí kontextu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google Sheets](https://docs.google.com/spreadsheets/) (Free online)
> **Koncept**: Zpracovaná informace jako podklad pro rozhodnutí.
> **Postup**: 
    1. Vytvořte nový sešit a do sloupce A zadejte náhodná čísla (např. 204, 15, 8). Jde o pouhá data bez významu.
    2. Do záhlaví přidejte kontext: "Číslo učebny", "Kapacita", "Volných míst". 
    3. Využijte podmíněné formátování (Zobrazit -> Podmíněné formátování): pokud je "Volných míst" > 0, podbarvěte buňku zeleně.
    4. Sledujte, jak se pouhý údaj vizuálně změnil v informaci použitelnou pro rozhodnutí o rezervaci.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Modelování firemního procesu (Výpůjčka)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Draw.io / diagrams.net](https://app.diagrams.net/) (Open source / Free online)
> **Koncept**: Procesy popisují, co se má stát a v jakém pořadí, včetně výjimek.
> **Postup**: 
    1. Otevřete aplikaci a zvolte "Blank Diagram".
    2. Navrhněte vývojový diagram výpůjčky knihy: Start -> Identifikace čtenáře -> Má dluhy? (Kosočtverec/Rozhodnutí).
    3. Modelujte dvě větve: "Ano" (konec procesu, odmítnutí) a "Ne" (ověření dostupnosti knihy -> výstup).
    4. Ověřte, zda váš model pamatuje na výjimku (např. ztráta knihy).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Tok dat přes API (Získání veřejných dat)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Postman](https://www.postman.com/) (Free online/Desktop)
> **Koncept**: Komunikaci mezi nesouvisejícími systémy umožňuje API (aplikační programové rozhraní).
> **Postup**: 
    1. Zaregistrujte se a vytvořte "New HTTP Request".
    2. Zadejte veřejnou URL adresu (např. `https://api.agify.io?name=jan` pro odhad věku podle jména).
    3. Klikněte na "Send" a prostudujte si odpověď ve formátu JSON (vstup, zpracování, výstup).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Business Intelligence Dashboard

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Tableau Public](https://public.tableau.com/) (Free online)
> **Koncept**: BI převádí provozní data na přehledy podporující rozhodování.
> **Postup**: 
    1. Stáhněte si libovolnou testovací datovou sadu (např. Superstore Sales v Excelu).
    2. Nahrajte ji do Tableau Public přes webové rozhraní.
    3. Přetáhněte "Region" na osu X a "Sales" (Tržby) na osu Y k vytvoření sloupcového grafu.
    4. Sledujte, jak systém automaticky agreguje tisíce transakcí do jednoho manažerského pohledu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Zpětná vazba a uživatelský vstup

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google Forms](https://docs.google.com/forms/) (Free online)
> **Koncept**: Systém musí kontrolovat vstupy, aby technické pravidlo nezkreslilo skutečnost.
> **Postup**: 
    1. Vytvořte formulář pro registraci do fiktivní školy.
    2. U pole "PSČ" nastavte validaci (Response validation): Musí to být číslo a musí mít přesně 5 číslic.
    3. Zkuste zadat zahraniční adresu s písmeny. Všimněte si, jak systém reaguje, a zamyslete se, zda tato kontrola není až příliš "slepá".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Identifikace komponent počítače (Infrastruktura)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Správce úloh (Windows Task Manager - `Ctrl+Shift+Esc`)
> **Koncept**: Technická infrastruktura (koncová zařízení, servery, úložiště, síť).
> **Postup**: 
    1. Otevřete Správce úloh a přejděte na kartu "Výkon" (Performance).
    2. Prozkoumejte vytížení CPU (zpracování), Paměti (krátkodobé úložiště dat) a Sítě (přenos).
    3. Identifikujte aplikace, které tvoří "Software", a zamyslete se nad svou "Lidskou" rolí v tomto lokálním IS.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Informační systémy v digitální době“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Typy informačních systémů

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

Tato kapitola rozděluje systémy na provozní (TPS), manažerské (MIS, DSS) a podnikové či oborové (ERP, CRM, GIS, DMS).

### Experiment 2.1: Transakční zpracování (TPS) v e-shopu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Odoo - Sales](https://www.odoo.com/) (Free tier)
> **Koncept**: TPS zachycuje jednotlivé události (vytvoření objednávky, prodej).
> **Postup**: 
    1. Založte si zkušební účet na Odoo s modulem "Sales".
    2. Vytvořte nového zákazníka a vygenerujte mu cenovou nabídku.
    3. Potvrďte nabídku – sledujte, jak se změní stav na "Prodejní objednávku" (transakce byla zaúčtována).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Řízení vztahů se zákazníky (CRM)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [HubSpot CRM](https://www.hubspot.com/products/crm) (Free online)
> **Koncept**: CRM podporuje vztahy se zákazníky, ukazuje historii komunikace.
> **Postup**: 
    1. Vytvořte bezplatný účet v HubSpotu.
    2. Zadejte "Kontakt" a v jeho profilu uložte simulovanou poznámku ze schůzky a zadejte mu "Úkol" (např. zavolat zítra).
    3. Všimněte si, že kdokoliv jiný z firmy otevře tento profil, přesně ví, jaký je dohodnutý další krok.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Geografický informační systém (GIS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google My Maps](https://www.google.com/maps/d/) (Free online)
> **Koncept**: GIS propojuje data s polohou (objekty, vlastnosti, prostorové vztahy).
> **Postup**: 
    1. Vytvořte novou mapu.
    2. Přidejte 3 body představující pobočky vaší fiktivní firmy (uzly).
    3. Do popisku každého bodu vložte metadata (Počet zaměstnanců, Obrat).
    4. Použijte nástroj "Pravítko" (Ruler) pro optimalizaci vzdálenosti doručení balíku z jedné pobočky do druhé.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Správa dokumentů a verzování (DMS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google Docs](https://docs.google.com/document/) (Free online)
> **Koncept**: DMS eviduje dokument jako řízený objekt s historií verzí a kolaborací.
> **Postup**: 
    1. Vytvořte nový textový dokument a sdílejte ho s kolegou (nebo svým druhým e-mailem).
    2. Napište odstavec textu. Přepněte do režimu "Navrhování" (Suggesting) a text upravte.
    3. Otevřete Historii verzí (`Soubor -> Historie verzí`) a zkuste obnovit starší stav. Tímto se zamezí vzniku "desítek kopií souborů".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Expertní systém (Rozhodovací strom)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Twine](https://twinery.org/) (Open source / Browser)
> **Koncept**: Znalostní systémy používají pravidla "jestliže–pak" pro odvození výsledku.
> **Postup**: 
    1. V prohlížeči otevřete Twine a vytvořte nový příběh (Story).
    2. Napište první blok: "Počítač se nespustí. Svítí kontrolka napájení? [[Ano]] [[Ne]]".
    3. Twine automaticky vytvoří dvě nové větve. Pokračujte k diagnózám (např. "Zkontrolujte kabel" nebo "Chyba základní desky").
    4. Spusťte mód "Play" a proklikejte expertní rozhodování technika.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Systém pro řízení obsahu (CMS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [WordPress.com](https://wordpress.com/) (Free tier)
> **Koncept**: CMS se zaměřuje na publikování obsahu na webu či intranetu.
> **Postup**: 
    1. Založte bezplatný web na WordPressu.
    2. Vytvořte "Příspěvek" (nikoli statickou stránku), přidejte mu štítky a zařaďte ho do kategorie.
    3. Publikujte jej a uvědomte si rozdíl oproti tvorbě čistého HTML: systém se stará o databázi a vzhled, vy jen zadáváte obsah.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Typy informačních systémů“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Životní cyklus informačního systému

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

Tato kapitola prochází fázemi vzniku IS od sběru požadavků přes návrh, testování a nasazení (migrace dat) až po provoz (SaaS, incidenty).

### Experiment 3.1: Evidence požadavků a Kanban

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Trello](https://trello.com/) (Free online)
> **Koncept**: Vymezení cílů a vývoj v iteracích pomocí menších celků.
> **Postup**: 
    1. Založte novou nástěnku (Board) se třemi sloupci: "To Do" (Požadavky), "Doing" (Realizace), "Done" (Nasazeno).
    2. Vytvořte kartu pro funkční požadavek: "Žák musí zjistit, zda je učebna volná".
    3. Přidejte k ní checklist (Testování, Schválení) a zkuste ji plynule přesouvat mezi sloupci.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Tvorba prototypu rozhraní

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Figma](https://www.figma.com/) (Free online)
> **Koncept**: Prototyp může včas odhalit, že uživatelé rozumějí procesu jinak než analytik.
> **Postup**: 
    1. Zaregistrujte se do Figmy a vytvořte nový Design File.
    2. Vložte "Frame" velikosti mobilního telefonu.
    3. Vytvořte tlačítko "Rezervovat" a textové pole.
    4. V záložce "Prototype" propojte tlačítko s druhou obrazovkou (např. "Potvrzení"), abyste nasimulovali chování systému před samotným programováním.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Generování testovacích a migračních dat

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Mockaroo](https://www.mockaroo.com/) (Free online)
> **Koncept**: Úspěšný běžný scénář pro testování nestačí, jsou nutná objemná, chybová nebo migrační data.
> **Postup**: 
    1. Na hlavní stránce definujte strukturu dat (např. ID, Jméno, Email, IP adresa).
    2. U jednoho z polí úmyslně nastavte % "Blank" (Prázdné hodnoty), abyste nasimulovali neúplná data.
    3. Vygenerujte a stáhněte 1000 záznamů v CSV formátu pro potřeby budoucího zátěžového "systémového testování".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Testování přístupnosti (Nefunkční požadavky)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Chrome DevTools (Lighthouse) - součást prohlížeče
> **Koncept**: Mezi nefunkční požadavky patří přístupnost (např. pro lidi s omezením).
> **Postup**: 
    1. Otevřete libovolný web a stiskněte `F12` pro vývojářské nástroje.
    2. Přejděte na záložku "Lighthouse" (příp. "Audits").
    3. Zaškrtněte "Accessibility" (Přístupnost) a spusťte analýzu.
    4. Projděte si výsledek, který upozorňuje například na chybějící popisy obrázků nebo špatný kontrast barev.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Řešení incidentů a dostupnosti

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [UptimeRobot](https://uptimerobot.com/) (Free tier)
> **Koncept**: Provozní správci sledují dostupnost služeb. Incident je narušení služby.
> **Postup**: 
    1. Založte účet a vytvořte "New Monitor".
    2. Zadejte libovolný web, který chcete sledovat (např. váš osobní web).
    3. Nastavte upozornění na e-mail při výpadku (HTTP chyba).
    4. Systém vás upozorní, jakmile nastane incident, jehož „problém“ (příčinu) pak musí řešit podpora.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Průzkum architektury SaaS

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Libovolný SaaS (např. Microsoft 365, Google Workspace, Notion)
> **Koncept**: V modelu SaaS poskytovatel řeší infrastrukturu a zákazník data a účty. Vyžaduje promyšlení "exit strategie".
> **Postup**: 
    1. Přihlaste se do vámi zvoleného SaaS programu.
    2. Běžte do nastavení "Export dat" nebo "Account data".
    3. Prostudujte, v jakém formátu systém umožňuje hromadný export vašich dat (.zip, .csv). Zamyslete se, jak těžká by v praxi byla migrace jinam (exit strategie).

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Životní cyklus informačního systému“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Databáze a hromadné zpracování dat

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

V této sekci zkoumáme oddělení aplikace od dat, hromadné operace (SQL), logický návrh a práci lokálních/serverových databází.

### Experiment 4.1: Vizuální relační modelování (ER diagram)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [dbdiagram.io](https://dbdiagram.io/) (Free online)
> **Koncept**: Relační model vyjadřuje vztahy tabulek pomocí klíčů, odděluje fyzické uložení a logický model.
> **Postup**: 
    1. V editoru napište jednoduchý kód pro tabulky Knihy (ID, Nazev) a Ctenari (ID, Jmeno).
    2. Vytvořte spojovací tabulku Vypujcky (ID_Knihy, ID_Ctenare, Datum).
    3. Nástroj obratem vygeneruje vizuální diagram struktury s vazbami.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Hromadné operace a deklarativní SQL

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DB Fiddle](https://www.db-fiddle.com/) (Free online)
> **Koncept**: Relační zpracování se děje deklarativním jazykem SQL. Síla DB je v hromadném zpracování záznamů jedním příkazem.
> **Postup**: 
    1. Zvolte SQL engine (např. PostgreSQL, jak je zmíněno ve studijních zdrojích).
    2. Vložte testovací data: `CREATE TABLE Zaci (jmeno TEXT, absence INT); INSERT INTO Zaci VALUES ('Jan', 5), ('Eva', 15);`
    3. Vytvořte hromadnou aktualizaci: `UPDATE Zaci SET absence = 0;` a uvědomte si rychlost (ale i riziko chyby), když se operace aplikuje plošně.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Lokální jednomuživatelská databáze

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [DB Browser for SQLite](https://sqlitebrowser.org/) (Open source Windows)
> **Koncept**: SQLite může sloužit jednomu uživateli bez instalace robustního serveru.
> **Postup**: 
    1. Nainstalujte program a vytvořte novou databázi (soubor `.db`).
    2. Naklikejte v grafickém rozhraní strukturu jednoduché tabulky a přidejte pár záznamů.
    3. Zkuste soubor v počítači přesunout nebo smazat – pochopíte tak rozdíl oproti serverové databázi, která data izoluje před přímým přístupem uživatele.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Rozdíl mezi tabulkovým procesorem a databází

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: MS Excel / Google Sheets
> **Koncept**: Tabulkový procesor je výborný pro analytiku malých dat, ale sdílený sešit nenahradí databázi pro souběžný přístup.
> **Postup**: 
    1. Otevřete Google Sheets se simulovanými daty.
    2. Požádejte kolegu, aby upravoval stejnou buňku ve stejném okamžiku.
    3. Porovnejte toto chování s transakční databází, která by pomocí zamykání záznamů (transakcí) zabránila přepsání dat druhé operace ("při prodeji poslední vstupenky").


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Role databázového administrátora (DBA)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Rozhraní Windows (Příkazový řádek) nebo phpMyAdmin (Demo)
> **Koncept**: DBA nenastavuje obsah dat, ale účty, oprávnění a obnovu.
> **Postup**: 
    1. Najděte na internetu volně dostupné demo *phpMyAdmin* (častý správce MySQL).
    2. Podívejte se na záložku "Users" nebo "Privileges".
    3. Zkuste cvičně navrhnout scénář: jaké "Checkboxy" s právy (SELECT - čtení, UPDATE - úprava) by měl mít běžný účetní a jaké externí auditor.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Principy sloupcového a řádkového uložení

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: MS Excel (Kontingenční tabulka)
> **Koncept**: Řádkové uložení se hodí pro čtení celého záznamu, sloupcové zrychluje analytické agregace nad stejným typem hodnoty.
> **Postup**: 
    1. V Excelu vytvořte širokou tabulku (50 řádků, 10 sloupců). To fyzicky odpovídá řádkovému čtení dat.
    2. Vytvořte Kontingenční tabulku a vložte "Tržby" do pole "Hodnoty" (Součet). 
    3. Uvědomte si princip: výpočetní modul teď nemusel načítat jména, data ani kategorie (celé řádky), ale "sáhl" pouze do jediného sloupce čísel.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Databáze a hromadné zpracování dat“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. NoSQL databáze

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

Zde se zaměříme na pochopení čtyř modelů, které řeší takzvanou "polyglot persistence": Dokumentový, Klíč-hodnota, Wide-column a Grafový.

### Experiment 5.1: Modelování v Dokumentové databázi (JSON)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [JSON Editor Online](https://jsoneditoronline.org/) (Free online)
> **Koncept**: Dokumentové databáze (jako MongoDB) ukládají data ve struktuře podobné formátu JSON včetně vnořených objektů a polí.
> **Postup**: 
    1. V editoru vytvořte strukturu `{ "kniha": "Základy IT", "autori": ["Jan", "Petr"], "vydani": {"rok": 2026} }`.
    2. Všimněte si, že autoři jsou "vnořené" pole (array) v jednom dokumentu. Relace není tvořena odkazem do jiné tabulky (nemusíte provádět SQL JOIN), ačkoliv to pro masivně se opakující data nese riziko duplicit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Key-value databáze a mezipaměť

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Chrome DevTools (Local Storage)
> **Koncept**: Databáze typu klíč-hodnota (např. Redis) je vhodná pro rychlé uložení stavu bez složitého vyhledávání.
> **Postup**: 
    1. Otevřete DevTools (`F12`) na libovolném webu a běžte do záložky "Application" (Aplikace).
    2. Najděte "Local Storage". Zde uvidíte jednoduchý pár `Key` (Klíč) a `Value` (Hodnota).
    3. Zkuste si představit serverový Redis: Aplikace zná unikátní klíč "session_123" a okamžitě získá hodnotu přihlášeného uživatele bez prohledávání celé databáze.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Zkoumání vztahů v Grafové databázi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Neo4j Sandbox](https://sandbox.neo4j.com/) (Free online, vyžaduje registraci)
> **Koncept**: Uzly a vztahy jsou základem, tvar cesty a procházení sítě hraje hlavní roli (Kdo zná koho?).
> **Postup**: 
    1. Založte Sandbox a vyberte dataset "Movies".
    2. Spusťte příklad grafového dotazu v jazyce Cypher: `MATCH (p:Person)-[:ACTED_IN]->(m:Movie) RETURN p,m LIMIT 10`
    3. Na obrazovce sledujte interaktivní "uzly" herců a filmů propojené explicitními vztahy.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Wide-column model pro časové řady (Koncept)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Tabulkový procesor (simulace)
> **Koncept**: Nástroje jako Apache Cassandra oddělují data (partitioning) a jsou uzpůsobené častému čtení "měření konkrétního senzoru v konkrétním čase".
> **Postup**: 
    1. V sešitu namodelujte sloupce: `ID_Senzoru`, `Datum_Cas`, `Teplota`.
    2. Seřaďte (Sort) tabulku primárně podle "ID_Senzoru" a sekundárně sestupně podle "Datum_Cas".
    3. To simuluje klíč, který umístí naměřené události jednoho senzoru fyzicky vedle sebe, čímž umožní extrémně rychlé vytažení dat bez ohledu na velikost zbytku tabulky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Distribuované sítě a CAP Teorém

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Chrome DevTools (Network Throttling)
> **Koncept**: Replikace kopíruje data napříč uzly sítě. Když nastane rozpad sítě, řeší to CAP teorém (konzistence vs dostupnost).
> **Postup**: 
    1. Otevřete libovolnou webovou aplikaci tvořící feed (např. sociální síť).
    2. V DevTools na kartě "Network" přepněte na režim "Offline" (Simulace přerušení spojení uzlů).
    3. Zkuste interagovat. Sledujte, jak se systém chová: odmítne operaci, nebo ji dočasně nasimuluje a spoléhá na "výslednou konzistenci" (eventual consistency) po připojení?


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Návrh architektury (Polyglot persistence)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Papír a tužka (nebo Draw.io)
> **Koncept**: Jeden systém může používat relační DB pro výpůjčky, dokumentový pro katalog, key-value pro session a graf pro doporučení (polyglot persistence).
> **Postup**: 
    1. Nakreslete architekturu E-shopu.
    2. Pro "Doporučení přátel" přiřaďte ikonku grafové DB (Neo4j).
    3. Pro "Obsah košíku" přiřaďte key-value úložiště (Redis).
    4. Zvažte úskalí z pohledu administrátora: nutnost zálohovat a synchronizovat více technologií oproti monolitu.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „NoSQL databáze“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Big data a datové sklady

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.

Závěrečná kapitola probírá obrovské a rychlé toky dat ("V" charakteristiky), budování datových skladů (DWH), transformace (ETL), agregaci (OLAP), dolování dat a analytickou bezpečnost.

### Experiment 6.1: Proces ETL (Extrakce, Transformace, Načtení)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Excel (Power Query)
> **Koncept**: Data se extrahují z různých zdrojů (E), vyčistí a sjednotí (T) a následně načtou do analytického úložiště (L).
> **Postup**: 
    1. Načtěte do Excelu rozbitý CSV soubor (`Data -> Z textu/CSV`).
    2. Klikněte na "Transformovat data" – otevře se Power Query.
    3. Proveďte transformaci: slučte jméno a příjmení do jednoho sloupce, odstraňte prázdné řádky, nahraďte desetinné tečky čárkami.
    4. Klikněte na "Zavřít a načíst" (Load do skladu).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: OLAP a Drill-down pohled

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: MS Excel (Pivot Tables s hierarchií)
> **Koncept**: OLAP systémy čtou velká historická data, seskupují je a dovolují rozpad ze souhrnu do detailu (drill-down).
> **Postup**: 
    1. Vytvořte data s hierarchií dimenzí (Rok -> Měsíc -> Produkt -> Tržba). 
    2. Vložte do Kontingenční tabulky Rok a Měsíc do sekce "Řádky".
    3. Použijte znaménka plus a minus vedle roků pro rozbalování a sbalování (roll-up) dat, čímž simulujete chování komplexní OLAP kostky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Dolování dat (Hledání shluků)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Orange Data Mining](https://orangedatamining.com/) (Open source Windows)
> **Koncept**: Dolování dat (Data mining) znamená použití statistických metod a strojového učení pro nalezení vzorů ve velkých datech.
> **Postup**: 
    1. Stáhněte si aplikaci.
    2. Vizuálně vytvořte spojení nodu "File" (vyberte přednastavená data) k nodu "Scatter Plot".
    3. Nástroj vykreslí graf, kde na pozadí shlukuje (klastruje) případy se stejnými vlastnostmi.
    4. Uvědomte si, že nalezený matematický vzor nemusí automaticky znamenat trvalou příčinnou souvislost.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Dávkové vs. Proudové zpracování (Stream)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Google Trends](https://trends.google.com/trends/) (Free online)
> **Koncept**: Oproti pomalým nočním dávkám (batch) zpracovává systém proudová data průběžně a detekuje trendy.
> **Postup**: 
    1. Otevřete Google Trends a vložte libovolný globální výraz.
    2. Zkuste si přepnout filtry na vyhledávání za posledních "7 dní" a "poslední hodinu".
    3. Sledujte "Velocity" (rychlost vzniku dat) u real-time přehledu, kde se miliardy událostí hodnotí průběžně jako proudové zpracování (stream processing).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Zásahy do soukromí a anonymizace

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Libovolný textový editor s funkcí Najít a Nahradit (nebo Python)
> **Koncept**: Nahrazením identifikátorů (Pseudonymizace) může zůstat možnost zpětného spojení.
> **Postup**: 
    1. Napište odstavec s citlivými údaji: "Jan Novák (obor IT) navštěvuje lékaře 5x ročně."
    2. Nahraďte jméno ID kódem: "Pacient #1 (obor IT) navštěvuje lékaře..."
    3. Cvičení k zamyšlení: Pokud se propojí takto "anonymizovaná" tabulka s tabulkou z LinkedIn profilů (kde je v IT z dané školy jen jeden člověk), došlo k narušení soukromí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Riziko algoritmického zkreslení a AI biasu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Rozhovor s jakýmkoliv modelem umělé inteligence (např. ChatGPT/Gemini)
> **Koncept**: Profilování a historická data mohou obsahovat nerovné zacházení. Model ho může opakovat bez použití explicitně citlivého údaje.
> **Postup**: 
    1. Zeptejte se modelu, ať vám napíše "seznam 5 profesí typických pro muže a 5 profesí typických pro ženy v roce 1950".
    2. Zeptejte se znovu pro rok 2024.
    3. Reflektujte s pomocí učebního textu: Pokud byste tato historická či nevyvážená tréninková data použili pro screening životopisů na manažerskou pozici, model může na pozadí diskriminovat a vyžadovat lidský přezkum (algoritmický bias).

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Big data a datové sklady“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
