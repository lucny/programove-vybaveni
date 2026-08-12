## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Projekt je víc než `index.html`**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednoduchý web může mít jen několik souborů, ale i u něj se vyplatí přehledná struktura:

```text
projekt/
├── index.html
├── kontakt.html
├── styles/
│   └── main.css
├── images/
│   ├── logo.svg
│   └── hero.webp
└── files/
    └── cenik.pdf
```

Názvy souborů je vhodné volit stabilně, bez závislosti na konkrétním počítači. Odkazy v HTML by měly používat webové cesty, ne lokální `C:\Users\...`. Rozdíl se často projeví až při publikaci: stránka, která na autorově počítači „funguje“, může na serveru přijít o obrázky kvůli špatným relativním cestám nebo rozdílu mezi velkými a malými písmeny v názvu souboru.

Pro verzování zdrojového kódu se hodí Git. U textových souborů HTML a CSS dokáže přesně ukázat, který řádek se změnil, a umožní bezpečně experimentovat. Malý statický web lze potom publikovat například na statickém hostingu nebo pomocí služby typu GitHub Pages. Dynamické webové aplikace potřebují další serverovou vrstvu, té se věnuje samostatný okruh.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**DevTools: laboratoř přímo v prohlížeči**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Nástroje pro vývojáře v prohlížeči umožňují prohlížet DOM, měnit CSS za běhu, sledovat box model, simulovat rozměry zařízení a zjišťovat, který styl skutečně vyhrál v kaskádě. To je mnohem účinnější než náhodně přepisovat hodnoty v souboru a znovu načítat stránku.

Typický problém: prvek má `margin`, ale mezera vypadá jinak, než autor čekal. DevTools ukáže výsledné rozměry boxu a seznam všech pravidel, včetně přeškrtnutých deklarací, které prohrály v kaskádě. CSS se tím mění z „magie, která někdy neposlouchá“ na systém, jehož rozhodování lze krok po kroku sledovat.

Stejným způsobem lze kontrolovat přístupnost, síťové požadavky, velikost zdrojů a výkon vykreslování. Prohlížeč je proto nejen cílové prostředí, ale i jeden z nejdůležitějších diagnostických nástrojů webového vývojáře.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Praktický pracovní postup**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při tvorbě nové stránky je výhodné nezačínat barvami. Nejprve si ujasníme obsah a informační strukturu, potom vytvoříme sémantické HTML, ověříme odkazy a základní ovladatelnost bez stylů. Teprve poté přidáme typografii, mezery a layout. Nakonec testujeme responzivitu, přístupnost, výkon a publikovanou verzi.

Tento postup má jednu zajímavou vlastnost: i když CSS selže nebo se nenačte, dobře napsané HTML zůstává srozumitelným dokumentem. A když později změníme design, nemusíme přepisovat obsah každé stránky. Oddělení vrstev tak není jen estetický ideál, ale praktická strategie pro dlouhodobou údržbu.

Před publikací je rozumné projít několik kontrolních otázek: fungují všechny odkazy a formuláře, má stránka správný titulek a jazyk, jsou obrázky optimalizované a mají smysluplné alternativy, lze vše ovládat klávesnicí, neztrácí se obsah při úzkém viewportu a nehlásí validátor nebo konzole zjevné chyby? U většího projektu se část těchto kontrol automatizuje v CI, ale princip zůstává stejný.

# Závěrečné propojení

HTML a CSS řeší dvě odlišné, ale těsně propojené vrstvy webu. HTML odpovídá především na otázku **„co tato část dokumentu znamená?“**, CSS na otázku **„jak má být v daném kontextu prezentována?“**. Když se role zamění, vzniká kód, který je obtížné upravovat a špatně se přizpůsobuje jiným zařízením nebo uživatelům.

Celý proces lze shrnout jako řetězec:

**obsah → sémantická struktura HTML → DOM → kaskáda a layout CSS → vykreslení v prohlížeči → vnímání a ovládání uživatelem**

Moderní webdesign proto není jen znalost značek a barev. Je to schopnost vytvořit dokument, který má smysluplnou strukturu, pružně se rozloží v různém prostoru, zůstává čitelný a ovladatelný a lze jej dlouhodobě udržovat. Flexbox, Grid, container queries nebo nové selektory jsou důležité nástroje, ale stojí na starší a stále platné myšlence: web funguje nejlépe tehdy, když je význam obsahu oddělen od způsobu jeho prezentace.

## Referenční zdroje pro další studium

- WHATWG: HTML Living Standard — https://html.spec.whatwg.org/
- W3C: CSS Snapshot — https://www.w3.org/TR/css-2026/
- MDN Web Docs: HTML a CSS — https://developer.mozilla.org/
- W3C: Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/

***
