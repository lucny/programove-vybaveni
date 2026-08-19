<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Vektorová grafika, 3D a XR

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


Tento dokument obsahuje sadu 36 praktických úloh (6 pro každou kapitolu), které vás krok za krokem provedou koncepty vektorové, 3D a prostorové grafiky. Všechny zmíněné nástroje jsou volně dostupné v prohlížeči, jako open-source software, nebo jako mobilní aplikace.

---

## 1. Principy vektorové grafiky

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


V této kapitole si vyzkoušíme rozdíl mezi rastrem a vektorem, prozkoumáme strukturu cesty a proces vektorizace.

### Experiment 1.1: Rastr vs. Vektor v praxi (Photopea vs. Inkscape)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vidět na vlastní oči bezeztrátové škálování nezávislé na mřížce pixelů.
> **Postup**: Otevřete si [Photopea](https://www.photopea.com/) (rastrový editor) a [Inkscape](https://inkscape.org/) (vektorový). V obou nakreslete kružnici o průměru 50 pixelů. Následně v obou programech zvětšete plátno i objekt na 5000 pixelů.
> **Výsledek**: V Photopee uvidíte obrovské, rozmazané „schody“ (aliasing) na hranách. V Inkscape zůstane geometrický popis přesný a kružnice bude dokonale hladká.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Pitva SVG kódu (Boxy SVG)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit, že SVG není jen obrázek, ale strukturovaný XML dokument čitelný člověkem i JavaScriptem.
> **Postup**: V editoru [Boxy SVG](https://boxy-svg.com/) nakreslete jednoduchou cestu (path) pomocí nástroje pero. Klikněte na záložku "Elements" (nebo uložte a otevřete soubor v Poznámkovém bloku).
> **Výsledek**: Uvidíte značku `<path>`, která obsahuje příkazy jako M (přesun na bod), L (čára) a Z (uzavření tvaru).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Vliv datové struktury na velikost (SVGOMG)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Otestovat tvrzení, že vektorová grafika má malou velikost, a zjistit, co ji zvětšuje.
> **Postup**: Stáhněte si z internetu jakékoliv složitější volné SVG logo. Nahrajte ho do online nástroje [SVGOMG](https://jakearchibald.github.io/svgomg/).
> **Výsledek**: Posouváním posuvníku „Precision“ můžete odebírat desetinná místa u souřadnic. Sledujte, jak se mění datový objem souboru a kdy geometrie začne vizuálně degradovat.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Proces vektorizace/trasování (Autotracer.org)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit, jak algoritmus odhaduje geometrii z pixelů a hledá hrany.
> **Postup**: Najděte si černobílou rastrovou (JPG) fotografii s vysokým kontrastem (např. ručně nakreslené logo). Nahrajte ji na [Autotracer.org](https://www.autotracer.org/).
> **Výsledek**: Aplikace vygeneruje vektorové cesty, které zjednoduší původní počet pixelů. Zkuste nahrát běžnou barevnou fotku krajiny – uvidíte, že algoritmus vytvoří obrovské množství objektů a ztratí smysl.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Atributy vzhledu a překrývání (Vecteezy Editor)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyzkoušet si definici výplně a obrysu u uzavřených cest.
> **Postup**: V online editoru [Vecteezy](https://www.vecteezy.com/editor) nakreslete hvězdu a obdélník. U hvězdy nastavte žlutou výplň (fill) a silný červený obrys (stroke). Přesuňte hvězdu přes obdélník.
> **Výsledek**: Jasně uvidíte rozdíl mezi samotnou geometrií určující tvar a aplikovaným stylem. Také uvidíte, že objekty tvoří zásobník překrývajících se prvků.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Konstrukční systémy a UI (Figma)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Ukázat si, jak se vektorové objekty využívají pro návrh rozhraní (UI design).
> **Postup**: Zaregistrujte se do [Figmy](https://www.figma.com/). Vytvořte Frame (plátno reprezentující displej mobilu) a zkuste navrhnout jednoduché tlačítko složené z vektorového obdélníku se zaoblenými rohy a textem.
> **Výsledek**: Pochopíte, že vektorové prostředí neslouží jen k ilustracím, ale k logickému rozmisťování škálovatelných prvků.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Principy vektorové grafiky“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Přesné kreslení a práce s vektorovými objekty

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Zde se zaměříme na křivky, logické spojování tvarů a transformace.

### Experiment 2.1: Zkrocení řídicích bodů (Cubic-bezier.com)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Interaktivně otestovat vliv úchytů (handles) na kubickou Bézierovu křivku.
> **Postup**: Otevřete [Cubic-bezier.com](https://cubic-bezier.com/). Křivka zde řídí rychlost animace. Tahejte za dva barevné řídicí body.
> **Výsledek**: Uvidíte, že tyto body neleží přímo na křivce, ale ovlivňují její směr a zakřivení. Když oddělíte směry úchytů, vznikne ostrý přechod.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Boolean operace v praxi (Tinkercad)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyzkoušet si geometrickou logiku sjednocení, průniku a rozdílu.
> **Postup**: V [Tinkercadu](https://www.tinkercad.com/) vložte do scény červenou krychli. Přes ni částečně položte šedou kouli, u které nastavíte režim "Hole" (díra). Oba objekty vyberte a klikněte na "Group" (Seskupit).
> **Výsledek**: Koule se odečte od krychle. Jedná se o operaci rozdílu (difference). Tuto „nedestruktivní“ operaci lze kdykoliv zrušit.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Transformační matice a jejich skládání (CSSmatic Transform)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit, jak rotace, posun a změna měřítka fungují a proč záleží na jejich pořadí.
> **Postup**: Otevřete si [CSSmatic Transform](https://www.cssmatic.com/box-transform). Pomocí posuvníků zkuste objekt nejdříve otočit o 45 stupňů a pak posunout (translate) na ose X.
> **Výsledek**: Zjistíte, že pokud dojde k rotaci celého souřadnicového systému objektu, posun na ose X se najednou pohybuje po úhlopříčce. Transformační parametry se skládají.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Zarovnávání a snapping (Penpot)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Místo posouvání „od oka“ použít přesné přichytávání a distribuci.
> **Postup**: V open-source editoru [Penpot](https://penpot.app/) nakreslete 5 různých kružnic libovolně rozházených po plátně. Vyberte je všechny najednou a v pravém panelu použijte ikony pro "Align vertical centers" a "Distribute horizontal spacing".
> **Výsledek**: Program všechny objekty přesně vycentruje a rozmístí se stejnými rozestupy bez vaší manuální námahy.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Pořadí kreslení a Z-index (Method Draw)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Prozkoumat logiku překrývání objektů ve vektorovém dokumentu.
> **Postup**: V editoru [Method Draw](https://editor.method.ac/) nakreslete velký červený kruh. Následně přes něj nakreslete menší zelený čtverec. Zelený čtverec kruh částečně překryje.
> **Výsledek**: Využijte tlačítka "Send to back" (přesunout do pozadí) na zelený čtverec. Čtverec zmizí za červeným kruhem, protože vektorový dokument je zásobník na sebe kladených prvků.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Převod textu na křivky (Glyphr Studio)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit, z čeho se skládají fonty a co znamená převedení na obrysy.
> **Postup**: Otevřete [Glyphr Studio](https://glyphrstudio.com/) a vyberte možnost pro tvorbu nového fontu z prázdného plátna. Otevřete znak "A".
> **Výsledek**: Zjistíte, že písmeno není žádný kouzelný text, ale přesně definovaná vektorová cesta s uzly a výplní. Pokud takový tvar upravíte, vytvoříte geometrii, kterou už nelze běžně editovat jako textový dokument.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Přesné kreslení a práce s vektorovými objekty“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. Technické kreslení a CAD

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Vyzkoušíme si přechod od skici k parametrickému modelu, geometrické vazby a přípravu pro CAM/tisk.

### Experiment 3.1: Skica a geometrické vazby (SolveSpace)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vidět rozdíl mezi čarou a plně definovanou skicou s vazbami.
> **Postup**: Spusťte [SolveSpace](https://solvespace.com/). Nakreslete 4 čáry zhruba do tvaru obdélníku. Vůbec se netrefujte do přesných rohů. Následně vyberte sousední čáry a aplikujte vazbu (constraint) "Perpendicular" (kolmost) a "Horizontal/Vertical".
> **Výsledek**: Software čáry sám zdeformuje a "uzamkne" do dokonalého obdélníku. Systém řídí tvary přes logiku, ne přes vizuální přesnost vaší ruky.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Parametrický CAD model (Onshape)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Otestovat historii operací a přepočítání modelu při změně základu.
> **Postup**: V bezplatném [Onshape](https://www.onshape.com/) vytvořte "Sketch", nakreslete kruh a zakótujte jeho průměr (např. 50 mm). Zvolte operaci "Extrude" pro vytlačení do 3D válce (např. 100 mm).
> **Výsledek**: V historii úprav se vraťte do první skici, změňte kótu průměru na 20 mm. Potvrďte. 3D válec se okamžitě přepočítá a zúží. Není to jen vizuální model, je to systém matematických závislostí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Programování geometrie (OpenSCAD)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Demonstrovat tvorbu modelu pomocí textových rovnic a proměnných.
> **Postup**: Otevřete [OpenSCAD](https://openscad.org/) a do editoru zadejte kód: `cube();` a stiskněte F5 pro vyrenderování. Pak si vytvořte proměnnou `sirka = 50;` a změňte kód na `cube([sirka, 30, 40]);`.
> **Výsledek**: Vizuální model se vygeneruje zcela automaticky podle vámi definovaných matematických parametrů, což je esence parametrického řízení modelu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Bloky a instance (Mecabricks)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit princip, že nemusíme ukládat geometrii milionkrát, ale použijeme jednu definici s odkazy.
> **Postup**: V online editoru [Mecabricks](https://www.mecabricks.com/) postavte malou zeď ze stejných kostek 2x4. Každou další kostku vytvoříte duplikací.
> **Výsledek**: Zeď sice vypadá jako hromada geometrie, ale program eviduje na pozadí pouze jednu referenční knihovní definici kostky 2x4 a u instancí si pamatuje pouze jejich pozici a natočení v prostoru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Slicing a příprava na výrobu - CAM (PrusaSlicer / Cura)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Projít CAM procesem, kdy z povrchového modelu (STL) vznikají instrukce pro stroj.
> **Postup**: Stáhněte si bezplatný [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) nebo [UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura). Vložte do něj libovolný STL 3D model. Klikněte na "Slice" (Rozřezat).
> **Výsledek**: V náhledu po vrstvách jasně uvidíte vygenerované dráhy, kudy reálně pojede hlava 3D tiskárny. Vygeneruje se soubor G-code, což už není geometrie, ale seznam fyzických souřadnic a povelů motorům.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Kontrola G-Code drah (NC Viewer)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Přečíst si strojový program.
> **Postup**: Uložte G-code z předchozího experimentu. Otevřete webový simulátor [NC Viewer](https://ncviewer.com/) a soubor do něj nahrajte.
> **Výsledek**: Uvidíte textové příkazy (např. `G1 X10 Y20 E1.5`) a simulátor vám animací přehraje, jak se tyto řádky překládají zpět do pohybu po přesných vektorových drahách.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Technické kreslení a CAD“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Trojrozměrné modelování a digitální scéna

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato část zkoumá polygonální mesh, práci s texturami a PBR materiály, a nasvícení.

### Experiment 4.1: Digitální sochařství a manipulace s meshem (SculptGL)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Zažít rozdíl mezi technickým CAD modelem a organickým sculptingem (socháním).
> **Postup**: Otevřete webový nástroj [SculptGL](https://stephaneginier.com/sculptgl/). Pomocí štětce "Draw" tažením myši deformujte základní hladkou kouli. Zapněte si nahoře zobrazení "Wireframe".
> **Výsledek**: Uvidíte, jak virtuální hmota ve skutečnosti představuje obrovskou hustou síť polygonů (vertices, edges, faces), kterou tahy štětce fyzicky posouvají prostorem.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Inspekce PBR map a topologie (Sketchfab)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Rozložit na prvočinitele strukturu moderního realistického materiálu.
> **Postup**: Běžte na [Sketchfab](https://sketchfab.com/), vyberte jakýkoliv populární realistický model (např. auto, zbraň) a zapněte "Model Inspector" (ikona vrstev vpravo dole).
> **Výsledek**: Přepínejte si zobrazení. Můžete si nechat zobrazit čistě jenom drátěný model (Wireframe) pro ukázku topologie, nebo vyizolovat pouze "Base Color", odlesky (Roughness) či kovovost (Metallic). Uvidíte, že finální render je vrstvený sendvič těchto map.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Procedurální generování textur (Material Maker)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vygenerovat povrch bez klasické fotografie pomocí uzlů.
> **Postup**: V programu [Material Maker](https://www.materialmaker.org/) na plochu vytáhněte uzel "Noise" (šum) a připojte ho rovnou do kanálu "Base color" ve výstupním materiálu. Poté ho napojte přes uzel "Normal map" i do kanálu "Normal".
> **Výsledek**: 3D koule v náhledu získá díky matematické funkci vizuální drsnou hrbolatou strukturu. Normálová mapa změní orientaci světelných odrazů na povrchu bez fyzického zahuštění polygonální geometrie.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Světla a kamery (Spline.design)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Složit 3D scénu a vidět rozdíl mezi perspektivou a ortografií.
> **Postup**: V editoru [Spline](https://spline.design/) vložte do scény 3D objekt. Vyberte objekt kamery a přepněte její projekci z "Perspective" na "Orthographic". Následně přidejte světlo typu "Directional light" (simulace slunce) a jedno "Point light".
> **Výsledek**: Při ortografické projekci zjistíte, že objekt neubíhá do dálky a drží měřítko. Různé typy světel pak naprosto změní náladu scény i tvar vrháných stínů.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Environment Lighting a HDRI (Poly Haven)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Otestovat nepřímé a přirozené osvětlení scény z okolní mapy.
> **Postup**: Na webu [Poly Haven](https://polyhaven.com/) najděte libovolnou mapu z lesa nebo interiéru. Přímo na webu se objeví 3D testovací náhled.
> **Výsledek**: Model nereaguje na jednoduchá bodová světla, ale na celou zmapovanou 360° fotografii. Kovová zrcadlová koule ukáže věrné odrazy prostředí, zatímco matná koule nasaje jemné nepřímé tónování barev (např. zelená z lesa).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: UV Mapping na základních tvarech (Blockbench)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vizualizovat si, jak se 2D textura obaluje na 3D model.
> **Postup**: Otevřete si [Blockbench](https://www.blockbench.net/) (webovou nebo desktop aplikaci). Vytvořte jednoduchou krychli a vpravo rozklikněte panel "UV".
> **Výsledek**: Jasně uvidíte křížový 2D rozklad krychle. Jakmile začnete na tento 2D rozklad kreslit štětcem, barva se bude matematicky mapovat přímo na správné polygony ve 3D prostoru.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Trojrozměrné modelování a digitální scéna“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Rendering a animace

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Zde otestujeme výpočty šíření světla, klíčování pohybu, kostry a částice.

### Experiment 5.1: Sledování paprsků v reálném čase (WebGL Path Tracer)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vidět "path tracing" v akci – postupné zbavování se šumu pomocí vzorkování.
> **Postup**: Otevřete experiment [WebGL Path Tracer](https://madebyevan.com/webgl-path-tracing/) od Evana Wallace. Nechte scénu pár sekund bez pohybu a pak hýbněte kamerou.
> **Výsledek**: Hned po pohybu je obraz velmi hrubý a zrnitý (málo vzorků cest). Jak kamera stojí, program neustále posílá další paprsky (samples) a dopočítává nepřímé odrazy světla (global illumination), čímž obraz vyhlazuje do čistého renderu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Renderování přes matematický kód (Shadertoy)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyzkoušet si rasterizaci a shadery bez klasické polygonální geometrie.
> **Postup**: Otevřete web [Shadertoy](https://www.shadertoy.com/) klikněte na libovolný jednoduchý populární projekt. Uvidíte blok textového kódu.
> **Výsledek**: Pokud v kódu změníte hodnoty určující barvu (`vec3 color = ...`) a kliknete na kompilaci, obraz vlevo se okamžitě překreslí. Program v reálném čase pro každý pixel obrazovky rozhoduje, jakou má mít výslednou barvu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Keyframe animace a časování (Wick Editor)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyrobit pohybovou interpolaci pomocí klíčových snímků.
> **Postup**: Otevřete [Wick Editor](https://www.wickeditor.com/). Na časové ose vytvořte klíčový snímek v čase 0 a nakreslete kruh vlevo. Na snímku 20 přidejte druhý klíčový snímek a posuňte kruh vpravo. Zapněte funkci "Tween" mezi nimi.
> **Výsledek**: Editor plynule dopočítá všechny mezistavy kruhu na pozicích mezi snímky 1 a 19.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Fyzikální pózování přes IK (Cascadeur)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Použít inverzní kinematiku k logickému pozicování postavy.
> **Postup**: V programu [Cascadeur](https://cascadeur.com/) (má free verzi) nahrajte základní humanoidní kostru. Uchopte za virtuální ovladač nohy a posuňte s ním nahoru.
> **Výsledek**: Nemusíte pracně počítat úhel kyčle a kolene. Díky inverzní kinematice (IK) systém sám dopočítá úhly celého řetězce kostí tak, aby chodidlo dosáhlo vaší cílové polohy, čímž zásadně zrychlí proces.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Automatický Rigging a Mocap (Mixamo)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Objevit, jak se z mrtvé polygonální sítě stane animovatelný "rig" ovládaný zachycenými daty.
> **Postup**: Založte si zdarma účet na [Mixamo.com](https://www.mixamo.com/). Vyberte jakoukoliv statickou (T-pose) postavu. Přejděte do sekce "Animations" a aplikujte na ni pohyb (např. běh nebo tanec).
> **Výsledek**: Systém postavě na pozadí vytvořil hierarchickou kostru (bones) a připojil k ní síť pomocí vah (skinning). Aplikovaná animace pochází ze skutečného herce snímaného přes motion capture.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Programování chaosu – částice (Effekseer)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vytvořit oheň pomocí Particle Systému.
> **Postup**: Otevřete open-source nástroj [Effekseer](https://effekseer.github.io/). Přidejte emitor (zdroj) částic a nastavte chování (Behavior) tak, aby částice stoupaly po ose Y nahoru a měnily barvu ze žluté na červenou a nakonec zprůhledněly.
> **Výsledek**: Uvidíte stovky drobných prvků chovajících se jako jedna substance. Nejedná se o ruční animaci každé jiskry, ale o simulaci řízenou vašimi základními pravidly zániku, rychlosti a barvy.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Rendering a animace“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Virtuální, rozšířená a smíšená realita

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Závěrečná část se zaměří na ukotvení do reality (SLAM), 6DoF volnost a moderní AR.

### Experiment 6.1: SLAM v kapse (Polycam / Scaniverse)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Nasnímat prostorovou mapu reálného pokoje a zkoumat orientaci v prostoru.
> **Postup**: Nainstalujte si na telefon aplikaci [Polycam](https://poly.cam/) nebo [Scaniverse](https://scaniverse.com/). Zvolte fotogrammetrický sken a pomocí senzorů/kamery se projděte kolem křesla či celého pokoje.
> **Výsledek**: Telefon pomocí inside-out trackingu a SLAMu (kombinace senzorů a obrazových bodů) neustále odhaduje svou pozici a sestavuje před vašima očima drátěnou mesh mřížku skutečného prostoru, kterou posléze obalí texturou.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: WebXR a 6DoF pohyb (Mozilla Hubs / Spoke)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyzkoušet si navigaci v prostorovém webu.
> **Postup**: Na počítači otevřete jakoukoliv místnost na [Mozilla Hubs](https://hubs.mozilla.com/). Pomocí myši a kláves WSAD se projděte prostředím. Pokud máte headset, vstupte do místnosti v něm.
> **Výsledek**: Zažijete pohyb se 6 stupni volnosti (6DoF) – můžete jít dopředu/dozadu (osa Z), doleva/doprava (X), skákat/krčit se (Y) i rotovat. Vše běží přes webový standard v prohlížeči, aniž byste instalovali herní aplikaci.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Markerless AR - Model-viewer (Mobilní web)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Vyvolat virtuální objekt v reálném obýváku bez použití fyzických značek.
> **Postup**: Na svém telefonu otevřete prohlížeč a vyhledejte stránku s [Google Model-viewer experimenty](https://modelviewer.dev/). Klikněte u zobrazeného předmětu (např. boty) na ikonu AR pro zobrazení ve vašem prostoru.
> **Výsledek**: Prohlížeč aktivuje kameru, najde fyzickou podlahu (rovinu) a ukotví botu přesně na její místo bez nutnosti vytištěného "QR" markeru (markerless). Můžete ji fyzicky obejít.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Face tracking jako kotva (Snap Lens Studio)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Napojit objekt na sledované rysy lidského těla (oči, tvář).
> **Postup**: V programu [Snap Lens Studio](https://ar.snap.com/lens-studio) (na PC) založte projekt z šablony "Face Mesh" nebo "Head Binding". Z webkamery se nahraje váš obličej a na něm se objeví testovací 3D objekt (např. brýle).
> **Výsledek**: Když hýbete hlavou, program v reálném čase analyzuje orientaci (3DoF/6DoF rotaci a posun obličeje) a pevně na obličej aplikuje transformační matici modelu brýlí.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Oživení vizitky přes Marker-based AR (AR.js)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Pochopit historicky spolehlivou metodu AR založenou na známém černobílém obrazci.
> **Postup**: Vyhledejte projekt [AR.js (Hiro marker)](https://ar-js-org.github.io/AR.js-Docs/). Na monitoru či papíře si nechte zobrazit velký čtvercový znak s nápisem "Hiro". Z druhého zařízení namiřte webkameru na tento znak.
> **Výsledek**: Systém znak detekuje s obrovskou jistotou a okamžitě na něj vykreslí 3D těleso. Oproti SLAMu nepotřebuje systém znát hloubku místnosti, orientuje se čistě podle natočení geometrického čtverce na obrazovce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Rychlý prototyp smíšené reality (Vectary)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Cíl**: Dokončit celý řetězec: Geometrie -> Model -> Render -> Prohlížení v AR.
> **Postup**: Vytvořte jednoduchou scénu ve webovém [Vectary](https://www.vectary.com/). V pravém horním menu využijte funkci "WebAR" (ikonka pro generování sdílecího kódu). Program vygeneruje QR kód.
> **Výsledek**: Jakmile tento kód naskenujete telefonem, celý cloudový model se přenese na vaši fyzickou podlahu do rozšířené reality. Osvětlíte si tak napojení veškeré teorie dohromady od křivky až k reálně vnímatelnému 3D prostoru.

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

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Virtuální, rozšířená a smíšená realita“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
