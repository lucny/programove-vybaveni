<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: HTML, CSS a tvorba webu

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


*Poznámka: Konkrétní programy a online aplikace použité v těchto experimentech pocházejí z mých externích znalostí (na základě naší předchozí konverzace) a můžete si jejich vlastnosti nezávisle ověřit. Teoretické principy, které těmito nástroji testujeme, vycházejí přímo z poskytnutého studijního textu.*

## 1. HTML jako strukturovaný dokument

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 1.1: Od prostého textu k DOMu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Minimální dokument lze napsat v obyčejném textovém editoru a otevřít bez kompilátoru, přičemž prohlížeč z něj rovnou sestaví dokumentový strom.
> **Nástroj**: Poznámkový blok (součást Windows) a libovolný webový prohlížeč.
> **Postup**: 
  1. Otevřete program Poznámkový blok.
  2. Napište jednoduchý text: `<h1>Můj první test</h1> <p>Toto je zkušební odstavec.</p>`.
  3. Zvolte *Soubor > Uložit jako*, do názvu napište `test.html` a typ souboru změňte na "Všechny soubory".
  4. Na soubor dvakrát klikněte. Prohlížeč jej okamžitě vykreslí jako strukturovaný dokument.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Automatická oprava překřížených značek

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Pokud se značky nesprávně překříží, prohlížeč se snaží zápis opravit podle standardních pravidel parseru, výsledný strom však nemusí odpovídat představě autora.
> **Nástroj**: [Live DOM Viewer](https://software.hixie.ch/utilities/js/live-dom-viewer/)
> **Postup**: 
  1. Otevřete aplikaci Live DOM Viewer.
  2. Do horního pole (Markup) záměrně napište chybný kód: `<b>tučný <i>a kurzíva</b> jen kurzíva</i>`.
  3. V dolní části sledujte interaktivní DOM strom. Všimněte si, jak si prohlížeč vnitřně HTML přepsal a rozdvojil element `<i>`, aby logiku stromu opravil.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Anatomie HTML kostry a prázdné elementy (void elements)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Moderní dokument začíná deklarací `<!doctype html>`, obsahuje `<head>`, `<body>` a některé elementy nemají koncovou značku.
> **Nástroj**: [CodePen](https://codepen.io/)
> **Postup**: 
  1. Založte si nový "Pen" (pískoviště) na CodePenu.
  2. Do HTML panelu vložte standardní kostru `<html><head><meta charset="utf-8"></head><body></body></html>`.
  3. Do těla `body` vložte text rozdělený značkou `<br>`. Všimněte si, že moderní HTML nevyžaduje lomítko (`<br />`).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Validace kódu a její limity

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Validátor dokáže odhalit nepovolený atribut nebo chybějící povinnou část. Validní stránka však stále může být nepřístupná nebo pomalá.
> **Nástroj**: [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)
> **Postup**: 
  1. Přejděte na záložku *Validate by Direct Input*.
  2. Vložte čisté HTML: `<!doctype html><title>Test</title><img src="test.jpg">`.
  3. Klikněte na Check. Validátor nahlásí chybu: chybějící atribut `alt`.
  4. Opravte na `alt=""` a ověřte zelený výsledek.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Zápis speciálních znaků pomocí entit

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Znaky se speciálním významem (např. `<`) nebo nedosažitelné na klávesnici lze zapsat pomocí znakových odkazů a entit.
> **Nástroj**: [Toptal HTML Arrows](https://www.toptal.com/designers/htmlarrows/)
> **Postup**: 
  1. Nalezněte si v nástroji kód pro znak menší než (`<`) nebo symbol autorského práva (©).
  2. V běžném editoru napište `10 &lt; 20`. Prohlížeč to bezpečně vykreslí jako "10 < 20", aniž by text interpretoval jako začátek značky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Analýza hierarchie outlinerem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Podstatná je srozumitelná struktura a správné nadpisy, nikoliv seznam kouzelných slov v meta značce `keywords`.
> **Nástroj**: [HTML5 Outliner](https://gsnedders.html5.org/outliner/)
> **Postup**: 
  1. Vytvořte kód dokumentu pouze z nadpisů `<h2>` a podnadpisů `<h4>`, schválně přeskočte `<h3>`.
  2. Vložte jej do Outlineru.
  3. Prohlédněte si vygenerovanou osnovu, která jasně vizualizuje mezeru v logice struktury vašeho dokumentu.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „HTML jako strukturovaný dokument“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Sémantická struktura, odkazy, média a formuláře

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 2.1: Nadpis není „větší text“

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Nadpisy `h1` až `h6` vytvářejí hierarchii dokumentu a jejich hlavní úlohou není určovat velikost písma.
> **Nástroj**: [Rozšíření HeadingsMap](https://chrome.google.com/webstore/detail/headingsmap/flbjommegcjonpdmenkdiocclhjacmbi)
> **Postup**: 
  1. Nainstalujte si rozšíření do prohlížeče Chrome nebo Firefox.
  2. Otevřete libovolný zpravodajský článek na internetu.
  3. Klikněte na ikonu rozšíření. Objeví se postranní panel, který ukáže sémantický strom nadpisů, díky němuž lze obsah pochopit bez ohledu na jeho CSS velikosti.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Zneužití vs. správné použití tabulek

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Tabulky patří k tabulkovým datům (elementy `caption`, `th`), nikoliv k tvorbě layoutu, k čemuž se zneužívaly v počátcích webdesignu.
> **Nástroj**: [TablesGenerator](https://www.tablesgenerator.com/html_tables)
> **Postup**: 
  1. V online generátoru si vizuálně naklikejte jednoduchý rozvrh hodin s hlavičkami dnů.
  2. Vygenerujte HTML.
  3. Prostudujte kód a zjistěte, jak nástroj oddělil sémanticky hlavičku tabulky (`<thead>` a `<th>`) od jejích datových buněk.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Propojení prvku Label s formulářem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Důležitá je vazba `label` na konkrétní ovládací prvek pomocí atributů, placeholder jako náhrada nestačí.
> **Nástroj**: [JSFiddle](https://jsfiddle.net/)
> **Postup**: 
  1. Vložte do HTML okna pole s id: `<input type="text" id="jmeno">`.
  2. Nad něj vložte `<label for="jmeno">Vaše jméno</label>`.
  3. Klikněte na text "Vaše jméno" ve výsledku. Fokus se okamžitě, přístupně přesune do vstupního pole.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Funkční backend zdarma

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Serverová aplikace musí data z formuláře ověřit, protože HTML formulář je pouze rozhraním klienta.
> **Nástroj**: [Formspree](https://formspree.io/)
> **Postup**: 
  1. Registrujte se a získejte zdarma endpoint URL.
  2. Nastavte tuto URL do atributu `action` formuláře: `<form action="VASE_URL" method="POST">`.
  3. Otevřete soubor v prohlížeči, vyplňte data a klikněte na odeslat. Data bezpečně dorazí na server Formspree.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Responzivní komprese obrázků

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Moderní web nabízí obrazové formáty jako AVIF nebo WebP a bere ohled na datový objem.
> **Nástroj**: [Squoosh](https://squoosh.app/)
> **Postup**: 
  1. Přetáhněte velkou (MB) fotografii ze svého počítače do Squoosh.
  2. Zvolte kompresi do formátu WebP.
  3. Posuvníkem porovnejte vizuální kvalitu (zůstává téměř shodná) a sledujte dramatický úbytek objemu dat (často v desítkách procent).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Cesty v odkazech a mrtvé linky

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Relativní odkazy se vyhodnocují vůči umístění souboru, např. zápis `../` znamená „o adresář výše“.
> **Nástroj**: [W3C Link Checker](https://validator.w3.org/checklink)
> **Postup**: 
  1. Vytvořte si HTML s několika odkazy. U jednoho zadejte schválně špatně zapsanou doménu, např. `href="https://google.comm"`.
  2. Zveřejněte (např. přes Glitch) nebo analyzujte lokálně, máte-li veřejnou URL.
  3. Nástroj odhalí a barevně zvýrazní, kam vedou "mrtvé" cesty a jaké HTTP chyby vrací servery.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Sémantická struktura, odkazy, média a formuláře“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. CSS: kaskáda, selektory a box model

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 3.1: Rozměry prvků přes Box model

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Výchozí CSS box model skládá rozměr z obsahu, paddingu, borderu a vnějšího marginu. U `box-sizing: border-box` se padding počítá do šířky.
> **Nástroj**: [CSS Peeper](https://csspeeper.com/) (nebo DevTools)
> **Postup**: 
  1. Nainstalujte CSS Peeper.
  2. Otevřete libovolný web, aktivujte Peeper a klikněte na vybrané tlačítko.
  3. Nástroj vám okamžitě ukáže grafické složení rozměrů v barvách: modrý content, zelený padding, oranžový margin, což přesně odpovídá logice z kapitoly.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Matematika specifity v kaskádě

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Kaskáda zohledňuje specificitu selektoru. Spor nevyhrává vždy to poslední zapsané pravidlo.
> **Nástroj**: [Specificity Calculator](https://specificity.keegan.st/)
> **Postup**: 
  1. Vložte selektor `#hlavni .odstavec` do levého sloupce.
  2. Vložte divočejší selektor `body div main p.odstavec:hover` do pravého sloupce.
  3. Kalkulačka vám ukáže bodové hodnocení (např. 1-1-0 proti 0-2-3) a matematicky potvrdí, že selektor s ID jasně vítězí, i když je kratší.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Hierarchické vztahy a selektory

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Kombinátory popisují vztahy; např. přímý potomek nebo selekce pomocí pseudotříd jako `:first-child`.
> **Nástroj**: [CSS Diner](https://flukeout.github.io/)
> **Postup**: 
  1. Otevřete online výukovou hru.
  2. Řešte úkoly formou psaní selektorů, které míří na "talíře" a "jablka" na stole.
  3. Postupte až k levelům, kde se využívají znaky jako `>` a `+`, čímž se interaktivně naučíte rodinným vztahům elementů.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Vizuální detekce fokusu pro klávesnici

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Člověk používající klávesnici potřebuje bezpodmínečně vidět viditelný fokus (`:focus-visible`), designové odstranění obrysu stránku ničí.
> **Nástroj**: [VisBug](https://visbug.web.app/)
> **Postup**: 
  1. Spusťte rozšíření VisBug nad komerční webovou stránkou.
  2. Z nabídky zvolte nástroj *Inspect State* (zkoumání stavů).
  3. Najeďte na odkaz a ručně mu vynuťte stav `:focus-visible`. Ihned se vizualizuje kroužek/rámeček, který web výchozím způsobem pro klávesnici definuje.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Dědičnost custom properties (proměnných)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Custom properties (`--promenna`) fungují jako kaskádové proměnné, které dědí hodnoty a ulehčují centrální správu.
> **Nástroj**: [Keyframes.app - Variables](https://keyframes.app/)
> **Postup**: 
  1. Vytvořte si prázdný projekt a do kořene `:root` definujte `--hlavni-barva: blue;`.
  2. Nastavte nadpisům a odkazům barvu pomocí `color: var(--hlavni-barva)`.
  3. Poté změňte proměnnou v `:root` na červenou a sledujte, jak kaskádově celý dokument okamžitě přebarví prvky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Relativní jednotky místo pixelů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Jednotka `px` je referenční a hodí se na rámečky, ale pro typografii jsou vhodnější kontextové hodnoty jako `rem` a `em`.
> **Nástroj**: [Utopia (Fluid Typography)](https://utopia.fyi/)
> **Postup**: 
  1. V nástroji vygenerujte škálu písma odstupňovanou pomocí relativních jednotek `rem`.
  2. Zkoumejte vygenerovaný kód CSS, ve kterém se matematicky propojuje funkce `clamp()` s viewportovými šířkami, aby nadpis rostl rozumně.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „CSS: kaskáda, selektory a box model“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Layout: od normálního toku k Flexboxu a Gridu

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 4.1: Flexbox v jednom směru

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Flexbox se hodí tam, kde se prvky organizují v jednom směru a rozdělují volný prostor bez ručního počítání.
> **Nástroj**: [Flexbox Froggy](https://flexboxfroggy.com/)
> **Postup**: 
  1. Nastartujte online aplikaci.
  2. Pomocí vlastností `justify-content` a `align-items` rozmístěte žáby na správné lekníny podél hlavní a příčné osy.
  3. Dokončením prvních 5 kol získáte základní mentální model pro zarovnávání menu a tlačítek.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Responzivní dvourozměrný CSS Grid

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: CSS Grid umí definovat dvourozměrné řádky i sloupce; responzivita může vzniknout i bez úprav na pevných breakpointech např. přes `repeat(auto-fit...)`.
> **Nástroj**: [Grid Garden](https://cssgridgarden.com/)
> **Postup**: 
  1. Na podobném principu jako Flexbox Froggy sázejte interaktivně mrkev do mřížky.
  2. Trénujte přesné alokování ploch pro komponenty (např. roztažení mrkve na víc sloupců).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Vizuální návrh layoutu přesahující Grid

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Dobrý layout kombinuje Grid pro hlavní kostru a Flexbox pro drobnější zarovnání prvků.
> **Nástroj**: [Layoutit Grid](https://grid.layoutit.com/)
> **Postup**: 
  1. V prázdné pracovní ploše si navrhněte klasické rozložení (Hlavička, Postranní panel, Hlavní obsah, Patička).
  2. Pomocí myši upravujte zlomkové podíly plochy (`fr`).
  3. Nástroj automaticky exportuje kód HTML a přesný obal CSS Gridu, na kterém uvidíte, jak se vyznačené oblasti definují vlastností `grid-template-areas`.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Opuštění pixel-perfect layoutu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Pozicování absolutními souřadnicemi se rozpadne, když se změní font nebo zařízení.
> **Nástroj**: [Interactive CSS Positioning Sandbox](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning)
> **Postup**: 
  1. Otevřete libovolný CodePen s textem a jedním odstavcem nastaveným na `position: absolute; top: 50px;`.
  2. Zvětšete v prohlížeči písmo (Ctrl/Cmd + Plus).
  3. Sledujte, jak se absolutně ukotvený rámeček drasticky překryje s ostatním zvětšeným obsahem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Plynulé kontinuum šířky

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Responzivní web není o návrhu pro „mobil, tablet, desktop“, ale chová se jako plynulé kontinuum velikostí.
> **Nástroj**: [Responsively App](https://responsively.app/)
> **Postup**: 
  1. Stáhněte a spusťte tento open-source prohlížeč.
  2. Vložte adresu svého oblíbeného webu.
  3. Aplikace web naráz vykreslí vedle sebe na simulátoru iPhonu, iPadu i obřího 4K displeje. Jakmile začnete scrollovat, scrollovaní probíhá synchronně ve všech náhledech.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Nevyzpytatelný viewport

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Okno může mít libovolnou šířku a layout musí odolat i nečekané šířce obrazovky.
> **Nástroj**: [ish.](https://bradfrost.com/demo/ish/)
> **Postup**: 
  1. Otevřete aplikaci.
  2. V horním menu klikněte na velikost "Random" (nebo "Disco").
  3. Okno začne náhodně roztahovat a smršťovat vloženou stránku, čímž simuluje nejbláznivější reálné možnosti zobrazení bez fixních velikostí.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Layout: od normálního toku k Flexboxu a Gridu“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Webdesign, přístupnost a výkon

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 5.1: Vizualizace střídmé hierarchie

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Vizuální hierarchii utváří mimo jiné velikost a proporce; web nepotřebuje mnoho barev, aby vedl pozornost.
> **Nástroj**: [Type Scale](https://typescale.com/)
> **Postup**: 
  1. Vyberte matematickou proporci (např. *Perfect Fourth*).
  2. Nástroj vytvoří harmonický rozdíl mezi velikostí pro nadpis H1 a běžný odstavec, který můžete zkopírovat do vlastního CSS pro zachování profesionální struktury.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Měření použitelného kontrastu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Web musí být ovladatelný a obsah vnímatelný pro uživatele např. venku s odlesky, kontrast je nedílnou součástí designu.
> **Nástroj**: [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
> **Postup**: 
  1. Otevřete tento ověřovací nástroj.
  2. Napište hexadecimální kód barvy vašeho textu (např. světle šedá `#999999`) a pozadí (`#ffffff`).
  3. Nástroj nahlásí, že barvy v testech standardu WCAG propadly, čímž potvrdí, že text bude špatně čitelný. Ztmavujte posuvník, dokud se nezobrazí "Pass".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Vnímání barev a informací

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Člověk může hůře rozlišovat barvy a informace nikdy nesmí být sdělena pouze barvou.
> **Nástroj**: [Color Oracle](https://colororacle.org/)
> **Postup**: 
  1. Stáhněte si tento bezplatný systémový filtr.
  2. Spusťte filtr "Deuteranopia" (běžná porucha vnímání zelené a červené).
  3. Podívejte se na semafor nebo na graf a všimněte si, že pokud neexistoval textový popis (tzv. alternativní text), význam grafiky se zcela smazal.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Analýza reálného výkonu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Výkon ovlivňuje kvalitu a použitelnost webu, například nezodpovědné množství fontů a datově těžké obrázky blokují vykreslení stránky.
> **Nástroj**: [WebPageTest](https://www.webpagetest.org/)
> **Postup**: 
  1. Zadejte URL adresu testovaného webu.
  2. Zvolte připojení "3G Fast" a spusťte test.
  3. Ve výsledném kaskádovém grafu ("Waterfall") prozkoumejte, který masivní skript nebo nenaškálovaný obrázek blokoval načtení HTML dokumentu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Zážitek s motorickým omezením

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Ovládání zůstává použitelné pro lidi s různými schopnostmi, například s třesem rukou.
> **Nástroj**: [Rozšíření Funkify](https://www.funkify.org/)
> **Postup**: 
  1. Nainstalujte do prohlížeče doplňkovou laboratoř Funkify.
  2. Zapněte osobnost "Trembling Trevor".
  3. Vaše myš se na obrazovce začne viditelně a nečekaně třást. Následně se v tomto režimu pokuste odeslat složitý dotazník obsahující drobná HTML políčka.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Minimalizace zátěže u fontů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Stahování nepoužitých řezů velké rodiny fontů přidává stovky kilobajtů dat k výkonu webu.
> **Nástroj**: [Wakamai Fondue](https://wakamaifondue.com/)
> **Postup**: 
  1. Najděte na disku libovolný font (např. ve formátu `.ttf`).
  2. Přetáhněte jej do okna Wakamai Fondue.
  3. Nástroj spočítá, kolik jazyků, symbolů a zbytečných historických ligatur font obsahuje, a ukáže možnosti, jak jej ořezat jen na znaky, které váš web vyžaduje.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Webdesign, přístupnost a výkon“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Od zdrojového souboru k publikovanému webu

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


### Experiment 6.1: Rozdíl mezi lokální cestou a webovým serverem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Odkazy by neměly obsahovat lokální cestu (`C:\Users\...`), jinak se na serveru web rozbije.
> **Nástroj**: [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) (doplněk VS Code)
> **Postup**: 
  1. Pokud píšete kód ve VS Code, dvojitým kliknutím na HTML otevřete soubor z disku přes `file:///C:/`.
  2. Nainstalujte Live Server, klikněte na "Go Live" a otevřete soubor přes `http://127.0.0.1`.
  3. Nyní víte, že obrázky volané s absolutním lomítkem `<img src="/images/x.png">` fungují na serveru správně, ale přes souborový protokol selžou.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Diagnostická laboratoř a kaskáda v DevTools

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Nástroje prohlížeče ukazují přeškrtnutá pravidla, která prohrála v kaskádě, což mění CSS z magie na predikovatelný systém.
> **Nástroj**: Vývojářské nástroje v prohlížeči (DevTools - F12)
> **Postup**: 
  1. Na libovolné stránce zmáčkněte `F12`.
  2. Pomocí inspektoru (ikona kurzoru) klikněte na hlavní nadpis.
  3. V záložce *Styles* hledejte přeškrtnutá písma – uvidíte, jak postupně silnější selektory nebo stylování přepsaly starší, slabší pravidla kaskády.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Web degradovaný na prostý text

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: I když se CSS nenačte (nebo selže spojení), dobře napsané sémantické HTML musí zůstat plně srozumitelným dokumentem.
> **Nástroj**: [Lynx Viewer](https://lynx.invisible-island.net/) (nebo online textový simulátor)
> **Postup**: 
  1. Vložte odkaz na svůj graficky moderní projekt do textového emulátoru.
  2. Analyzujte strukturu v holém textu bez CSS a JavaScriptu – ověřte, že navigační menu je stále seznam položek a články tvoří logicky seřazenou strukturu dokumentu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Automatizovaný audit (CI princip)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Před publikací se hodí ověřit přístupnost, výkon a best-practices sadou kontrol.
> **Nástroj**: Lighthouse (integrován v Chrome DevTools)
> **Postup**: 
  1. Otevřete projekt v Google Chrome.
  2. Zmáčkněte `F12`, vyberte záložku *Lighthouse* a dejte spustit *Analyze page load*.
  3. Počkejte na vygenerování zprávy. Obdržíte skóre na škále 0-100 ve výkonu, dostupnosti a doporučeních a získáte přesný checklist kroků k okamžité nápravě případných prohřešků kódu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Bezbolestný statický deployment

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Malý statický web (HTML, CSS a obrázky) nevyžaduje obří dynamický hosting, stačí ho přesunout jako publikovaný statický soubor.
> **Nástroj**: [Netlify Drop](https://app.netlify.com/drop)
> **Postup**: 
  1. Připravte si složku obsahující `index.html` a vedle něj složku stylů.
  2. Otevřete prohlížeč a složku přetáhněte fyzicky na plochu aplikace Netlify Drop.
  3. Během minuty dojde k bezplatnému nasazení (deploy) do sítě a vy získáte veřejnou URL, aniž byste použili FTP či programovali server.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Pořádek v kódu pomocí formátovače

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Koncept**: Cílem projektu není funkční shluk značek, ale systémová struktura oddělení prezentace, která jde dlouhodobě udržovat týmem vývojářů.
> **Nástroj**: [Prettier](https://prettier.io/)
> **Postup**: 
  1. Otevřete online pískoviště (Playground) nástroje Prettier.
  2. Vložte ošklivě poslepovaný, chaoticky odsazený HTML kód, kde chybí občas odřádkování.
  3. Prettier kód bleskově analyzuje a přeformátuje, čímž dává praxi tvrzení z textu, že webové technologie vyžadují kulturu zápisu pro lidské správce.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Od zdrojového souboru k publikovanému webu“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
