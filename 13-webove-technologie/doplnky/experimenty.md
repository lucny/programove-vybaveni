<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Webové technologie a webové aplikace

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


## 1. Klient, server, frontend a backend

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato sada experimentů vám pomůže pochopit, jak probíhá komunikace v síti, protože web je založen na komunikaci mezi programy, kdy klient požaduje službu a server na ni odpovídá.

### Experiment 1.1: Sledování řetězce HTTP požadavků

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Vývojářské nástroje prohlížeče (F12) – záložka **Network** (Síť).
*Postup:*
1. Otevřete libovolný web (např. Wikipedii) a stiskněte F12.
2. Přejděte na záložku *Network* a obnovte stránku (F5).
3. Pozorujte, že na jeden zadaný odkaz prohlížeč odeslal desítky dalších požadavků (CSS, obrázky, skripty).
4. Klikněte na první dokument v seznamu a prohlédněte si záložku *Headers* (Hlavičky), kde uvidíte metody požadavků a stavové kódy.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Zobrazení fyzického umístění serveru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [DNS Checker](https://dnschecker.org/) a [IP Location](https://www.iplocation.net/).
*Postup:*
1. Zadejte oblíbenou adresu (např. `seznam.cz`) do DNS Checkeru a zjistěte její IP adresu (A záznam).
2. Zkopírujte získanou IP adresu do nástroje IP Location.
3. Prozkoumejte, kde se fyzicky nachází počítače (servery), které vrací HTTP odpovědi do vašeho prohlížeče.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Testování rychlosti a zátěže (Throttling)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Vývojářské nástroje prohlížeče (F12) – Network.
*Postup:*
1. Otevřete bohatý zpravodajský portál a zapněte DevTools.
2. V záložce *Network* najděte roletku "No throttling" a změňte ji na "Slow 3G".
3. Obnovte stránku. Sledujte, jak se frontendová část (vzhled, obrázky) postupně skládá, a uvědomte si, jakou práci musí prohlížeč při slabším spojení odvádět.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Vytvoření vlastního statického serveru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Příkazový řádek Windows (CMD) + instalovaný [Python](https://www.python.org/) (součástí mnoha distribucí).
*Postup:*
1. Vytvořte si složku a v ní jednoduchý soubor `index.html` s textem `<h1>Ahoj ze serveru</h1>`.
2. Otevřete v této složce příkazový řádek.
3. Spusťte příkaz `python -m http.server 8000`.
4. V prohlížeči jděte na `http://localhost:8000`. Právě jste spustili program, který poskytuje statické soubory.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Identifikace serverových technologií

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Netcraft Site Report](https://sitereport.netcraft.com/).
*Postup:*
1. Zadejte adresu vašeho oblíbeného webu.
2. V sekci *Hosting History* nebo *Network* vyhledejte položku "Web server".
3. Zjistíte tak, zda web pohání Nginx, Apache HTTP Server nebo Microsoft IIS.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Komunikace přes "surovou" příkazovou řádku

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Příkaz `curl` (vestavěný ve Windows 10/11 i macOS).
*Postup:*
1. Otevřete příkazový řádek (CMD/PowerShell).
2. Zadejte `curl -I https://www.google.com`.
3. Přepínač `-I` vrátí pouze HTTP hlavičky odpovědi (bez těla HTML). Prohlédněte si, jaká čistá data dostává klient (prohlížeč) od serveru před tím, než z nich složí rozhraní.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Klient, server, frontend a backend“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. JavaScript: jazyk pro web

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Následující experimenty prozkoumají základní dynamické typování a specifika jazyka JavaScript přímo ve vašem prohlížeči, jelikož JavaScript je dynamicky typovaný jazyk a proměnná může během běhu programu měnit svůj typ.

### Experiment 2.1: Blokový scope (rozsah platnosti) v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče (F12 -> Console) nebo [JSFiddle](https://jsfiddle.net/).
*Postup:*
1. Napište blok kódu: `{ let x = 10; var y = 20; }`.
2. Zkuste vypsat `console.log(y);` – hodnota 20 se vypíše, protože starší `var` má funkční scope a blok `{}` ho nezastaví.
3. Zkuste `console.log(x);` – prohlížeč vyhodí chybu, protože `let` má blokový scope.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Testování plovoucí řádové čárky (IEEE 754)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Do konzole zadejte `0.1 + 0.2`.
2. Zjistíte, že výsledek není `0.3`, ale `0.30000000000000004`.
3. Ověříte si tím důsledek binární reprezentace desetinných čísel.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Operátory a volná vs. striktní rovnost

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Zadejte `1 == "1"`. Výsledek bude `true`, protože operátor `==` převede typy.
2. Zadejte `1 === "1"`. Výsledek bude `false`, což dokazuje užitečnost striktní rovnosti, která porovnává hodnotu bez implicitní konverze.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Zvláštnosti datových typů a NaN

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Zkuste vynásobit text číslem: `"Ahoj" * 5`.
2. Výsledkem bude `NaN` (Not-a-Number), což značí, že číselná operace nedala použitelný výsledek.
3. Pomocí příkazu `typeof NaN` zjistíte paradox JavaScriptu – typ této hodnoty je `number`.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Zkoumání mutability objektů při použití `const`

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Definujte konstantní objekt: `const auto = { barva: "červená" };`.
2. Pokuste se přiřadit celou novou hodnotu: `auto = { barva: "modrá" };`. Dostanete chybu.
3. Pokuste se ale změnit vnitřní vlastnost: `auto.barva = "modrá";`. Změna projde. U objektu použití `const` nezmrazí jeho obsah, pouze samotnou vazbu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Callbacky a Arrow funkce

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [JSFiddle](https://jsfiddle.net/)
*Postup:*
1. Do JavaScriptového okna vložte kód s polem a zkrácenou arrow funkcí:
   `let cisla =;`
   `let dvojnasobky = cisla.map(n => n * 2);`
   `console.log(dvojnasobky);`
2. Otevřete konzoli ve spodní části nástroje a podívejte se, jak se funkce předaná jako argument postarala o transformaci pole.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „JavaScript: jazyk pro web“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Propojení JavaScriptu s webovou stránkou

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Web API zprostředkovává vazbu mezi JavaScriptem a prohlížečem. Tyto úkoly ilustrují manipulaci se strukturou a událostmi dokumentu.

### Experiment 3.1: Iluze zdrojového HTML a upraveného DOMu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Libovolný web (např. zprávy) + Vývojářské nástroje (Elements vs. Zobrazit zdrojový kód).
*Postup:*
1. Klikněte pravým tlačítkem na stránku a zvolte "Zobrazit zdrojový kód stránky" (View Page Source). Uvidíte původní HTML odeslané ze serveru.
2. Nyní zmáčkněte F12 a podívejte se na záložku *Elements*. Uvidíte obrovské množství elementů navíc. JavaScript totiž DOM po načtení mění, aniž by přepsal HTML na serveru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Destrukce webu přes DOM API (textContent a innerHTML)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče na oblíbeném webu.
*Postup:*
1. Na libovolné stránce jděte do konzole a zadejte `document.body.innerHTML = "<h1>HACKED</h1>";`. Celý web zmizí a bude nahrazen nadpisem, protože `innerHTML` interpretuje text jako HTML.
2. Obnovte stránku (F5) a zkuste `document.body.textContent = "<h1>HACKED</h1>";`. Místo velkého nadpisu uvidíte vypsané tagy, protože se vkládá obyčejný text.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Využití BOM: Objekt location

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Zadejte `location.hostname`. Získáte doménu, na které se aktuálně nacházíte.
2. Zadejte `location.assign("https://google.com")`. Okamžitě dojde k přesměrování. Tyto objekty pro práci s prohlížečem (BOM) se netýkají přímo HTML stránky, ale kontextu okna.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Interaktivní web: Nasazení Event Listeneru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [CodePen](https://codepen.io/)
*Postup:*
1. V okně HTML vytvořte tlačítko: `<button id="btn">Klikni</button>`.
2. V okně JS přidejte naslouchač: 
   `document.getElementById("btn").addEventListener("click", () => { alert("Kliknuto!"); });`
3. Vyzkoušejte kliknutí. Stránka reaguje, událost oznamuje, že uživatel klikl.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Bublání událostí (Event Delegation)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [CodePen](https://codepen.io/)
*Postup:*
1. Do HTML dejte seznam: `<ul id="seznam"><li>A</li><li>B</li></ul>`.
2. Do JS dejte: `document.getElementById("seznam").addEventListener("click", (event) => { alert(event.target.textContent); });`
3. Klikněte na konkrétní položku. Událost probublá z `<li>` k rodiči `<ul>` a `event.target` ukáže, na který přesně element jste klikli. Tento přístup zachytávání se nazývá event delegation.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Generování elementů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče.
*Postup:*
1. Napište příkaz: `let div = document.createElement("div");`.
2. Přidejte mu text: `div.textContent = "Nový obsah!";`.
3. Vložte ho na stránku: `document.body.appendChild(div);`.
4. Skrolujte dolů a uvidíte nově přidaný element. Změna se projeví při vykreslení bez obnovení stránky ze serveru.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Propojení JavaScriptu s webovou stránkou“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Node.js a JavaScript na serveru

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Node.js doplňuje engine V8 o rozhraní pro práci s filesystémem, sítěmi a procesy OS.

### Experiment 4.1: Rychlé spuštění Node.js online (bez instalace)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Glitch](https://glitch.com/) nebo [Replit](https://replit.com/).
*Postup:*
1. Na Glitchi vytvořte nový projekt typu "glitch-hello-node".
2. Prozkoumejte, že máte k dispozici logiku běžící na serveru, a podívejte se na výpisy v sekci "Logs". Oproti prohlížeči tu máte například modul pro soubory.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Asynchronní I/O operace

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Glitch](https://glitch.com/) - konzole (Terminal).
*Postup:*
1. V Terminálu vytvořte skript `touch test.js`.
2. Otevřete ho a vložte asynchronní čekání, které ukazuje princip event loopu:
   `console.log("Start");`
   `setTimeout(() => console.log("Čekání"), 2000);`
   `console.log("Konec");`
3. Spusťte přes `node test.js`. Uvidíte pořadí Start -> Konec -> Čekání. Asynchronní přístup totiž operaci zahájí a čeká neblokujícím způsobem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Mapa balíčků NPM (Závislosti)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [NPM Graph](https://npmgraph.js.org/).
*Postup:*
1. Jděte na NPM Graph a napište známý balíček, např. `express`.
2. Prozkoumejte pavučinu závislostí. Uvědomte si, že externí balíček je cizí kód, který se stává součástí vašeho projektu díky správci závislostí `npm`.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Vytvoření základní Express.js routy

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Glitch](https://glitch.com/) (projekt Node).
*Postup:*
1. Otevřete soubor `server.js`.
2. Napište novou obslužnou cestu (routu):
   `app.get("/moje-cesta", (req, res) => { res.send("Našel jsi mě!"); });`.
3. Klikněte na *Preview* a za URL doplňte `/moje-cesta`. Routing rozhodl, která část programu požadavek obsloužila.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Zápis do lokálního JSON souboru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Glitch](https://glitch.com/)
*Postup:*
1. Využijte modul pro souborový systém: `const fs = require('fs');`.
2. Spusťte ve skriptu: `fs.writeFileSync('data.json', JSON.stringify({ a: 1 }));`.
3. V editoru se vám po obnovení objeví soubor `data.json`. Pro ukládání nastavení je to přiměřené, na rozdíl od tisíců uživatelských dat, kde by byla vhodnější databáze.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Šablonovací systémy na backendu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Glitch](https://glitch.com/) (připravený Node.js s EJS).
*Postup:*
1. Nainstalujte šablonu v terminálu: `npm install ejs`.
2. Nastavte v Expressu generování: `app.set('view engine', 'ejs');`
3. Vytvořte soubor `views/index.ejs` obsahující strukturu `<h1>Ahoj <%= jmeno %></h1>`.
4. V server.js pošlete data: `res.render('index', { jmeno: 'Studente' });`. Server sestaví finální HTML dříve, než jej odešle.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Node.js a JavaScript na serveru“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Webové API a AJAX

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tyto úkoly učí pracovat s cizími zdroji bez stahování nových HTML stránek a prozkoumávat REST architekturu.

### Experiment 5.1: Zavolání API přes Fetch a vytažení dat

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče + [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
*Postup:*
1. Zadejte asynchronní požadavek: 
   `fetch('https://jsonplaceholder.typicode.com/users/1').then(res => res.json()).then(data => console.log(data.name));`
2. Pozorujte, že získáte výpis uživatele z externího API (např. Leanne Graham). Pro starší kód se dříve používal XMLHttpRequest, dnes vede moderní Fetch API.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Orientace v parametrech cesty a dotazu (Query/Path Params)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Webový prohlížeč + [Star Wars API (SWAPI)](https://swapi.dev/).
*Postup:*
1. Do URL řádku zadejte `https://swapi.dev/api/people/1/`. `1` je *path parameter*, určuje zdroj Luke Skywalker.
2. Nyní zkuste filtrovat v jiném API (např. `https://jsonplaceholder.typicode.com/posts?userId=1`). `?userId=1` funguje jako *query parameter* pro filtraci odpovědi.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Odeslání dat přes POST a čtení stavových kódů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče + [Webhook.site](https://webhook.site/).
*Postup:*
1. Otevřete Webhook.site a zkopírujte vaši unikátní URL.
2. V prohlížeči proveďte POST: 
   `fetch('VAŠE_URL', { method: 'POST', body: JSON.stringify({tajemstvi: '123'}) });`.
3. Na kartě Webhooku se okamžitě zobrazí přijatá data se stavovým kódem 200.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Interakce přes WebSocket

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole + [PieSocket Tester](https://www.piesocket.com/websocket-tester).
*Postup:*
1. Otevřete konzoli a připojte se ke zkušebnímu veřejnému soketu:
   `let ws = new WebSocket("wss://echo.websocket.events");`.
2. Definujte reakci: `ws.onmessage = (event) => console.log(event.data);`.
3. Pošlete zprávu: `ws.send("Testovací zpráva pro server");`.
4. Dostanete ji okamžitě zpět bez HTTP žádosti – komunikační kanál je obousměrný.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Zkoumání CORS restrikcí

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* Konzole prohlížeče (otevřená např. na seznam.cz).
*Postup:*
1. Zkuste si z cizí domény přečíst lokální služby Google nebo jiného API bez hlaviček. V záložce konzole si vygenerujte nesprávný request.
2. Výsledkem bude červená chyba obsahující výraz **CORS Policy**. Prohlížeč totiž uplatňuje pravidla CORS určující, zda smí skript z jednoho originu číst odpověď cizí služby.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Sestavení dat z GraphQL API

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Rick and Morty GraphQL API](https://rickandmortyapi.com/graphql).
*Postup:*
1. Jděte na uvedenou adresu a do levého okna napište dotaz definující přesná pole:
   `query { character(id: 1) { name, species } }`
2. Stiskněte Play. Oproti RESTu se vám vrátil JSON obsahující pouze to, co jste specifikovali, což je hlavní výhoda flexibility GraphQL klienta.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Webové API a AJAX“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Knihovny a frameworky

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Moderní nástroje přidávají abstrakci nad základními technologiemi a zjednodušují práci na složitých projektech.

### Experiment 6.1: Přidání knihovny z CDN do projektu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [CodePen](https://codepen.io/) + [Chart.js CDN](https://cdnjs.com/libraries/Chart.js).
*Postup:*
1. V CodePenu otevřete nastavení okna HTML a vložte odkaz na CDN skript knihovny Chart.js.
2. Do HTML vložte `<canvas id="myChart"></canvas>`.
3. Do JS vložte malý kód z dokumentace Chart.js a vygenerujte během okamžiku hezký vizuální graf. Nemuseli jste znovu implementovat zobrazení os a animace.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Vytvoření layoutu pomocí Utility tříd (Tailwind CSS)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Tailwind Play](https://play.tailwindcss.com/).
*Postup:*
1. Smažte stávající kód.
2. Vložte `<div class="bg-blue-500 text-white p-4 rounded-lg shadow-md hover:bg-blue-600 cursor-pointer">Tlačítko</div>`.
3. Místo psaní odděleného CSS skládáte vzhled z malých utility tříd přímo v HTML.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Simulace WebAssembly (Wasm)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [WasmFiddle](https://wasdk.github.io/WasmFiddle/) nebo konzole.
*Postup:*
1. V okně jazyka C vytvořte jednoduchou matematickou funkci (např. sečtení dvou hodnot).
2. Nechte nástroj funkci přeložit (transkompilovat/build). Nástroj vygeneruje binární formát WebAssembly a obalující JavaScript (spojovací jazyk), který modul vykonává blízko nativní rychlosti mimo tradiční sandbox.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Organizace podle komponentního frontendu (React)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [CodeSandbox - React Template](https://codesandbox.io/s/react-new).
*Postup:*
1. Otevřete šablonu. Uvidíte soubor `App.js`.
2. Zkuste si vytvořit izolovanou funkci `function Tlacitko() { return <button>Ahoj</button>; }`.
3. Vložte tag `<Tlacitko />` do hlavičky hlavní aplikace. Uvědomte si, že rozhraní neděláte jako obrovské HTML, ale strom vnořených opakovatelných komponent, jaké využívá React či Vue.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Ochrana před chybami pomocí statických typů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [TypeScript Playground](https://www.typescriptlang.org/play).
*Postup:*
1. Napište funkci: `function secti(a: number, b: number) { return a + b; }`
2. Zkuste ji zavolat špatně: `secti(5, "10");`.
3. Nástroj okamžitě podtrhne chybné volání červeně díky typovým informacím, ačkoli na pravé straně obrazovky z kódu transkompiluje klasický JS soubor pro prohlížeč.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Formátování a analýza kódu na pozadí

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

*Nástroj:* [Prettier Playground](https://prettier.io/playground/).
*Postup:*
1. Do okna napište absolutně nečitelně formátovaný, ale validní JavaScriptový kód s různými uvozovkami, odsazeními a zbytečnými mezerami.
2. Sledujte okno výsledku. Prettier provádí unifikaci formátování (často společně s ESLint analýzou) zcela automaticky, což je základem mnoha vývojářských toolchainů.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Knihovny a frameworky“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
