## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Obraz jako popis objektů místo mřížky pixelů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Rastrový obraz říká přibližně: „na souřadnici x, y je pixel této barvy“. Vektorový obraz postupuje jinak. Popisuje **geometrické objekty** a jejich vlastnosti.

Místo tisíců pixelů kružnice může obsahovat informaci:

- střed je v bodě `(100, 100)`,
- poloměr je `50`,
- obrys je černý,
- výplň je modrá,
- tloušťka obrysu je `2`.

Program při zobrazení tento matematický popis převede na pixely aktuálního zařízení.

Vektorové objekty mohou být tvořeny například:

- body,
- úsečkami,
- obdélníky,
- elipsami,
- mnohoúhelníky,
- křivkami,
- textem,
- složenými cestami.

Kromě geometrie mají také **atributy vzhledu**:

- výplň,
- obrys,
- barvu,
- průhlednost,
- gradient,
- vzorek,
- tloušťku a styl čáry.

Velkou výhodou je, že objekt zůstává samostatně editovatelný. Můžeme změnit barvu jedné hvězdy nebo polohu jednoho bodu křivky, aniž bychom museli přemalovávat okolní obraz.

Vektorová grafika je proto ideální pro loga, ikony, schémata, mapy, diagramy, typografii a technické výkresy.

Často se říká, že vektorový obraz je „bezeztrátově škálovatelný“. Přesnější je říci, že **geometrický popis není svázán s pevnou mřížkou pixelů**. Objekt lze přepočítat na jinou velikost bez klasické pixelizace.

To ale neznamená, že každý vektorový dokument lze libovolně zvětšovat bez jakéhokoli praktického problému. Dokument může obsahovat vložené rastrové obrázky, efekty s pevnou rastrovou velikostí, nevhodně nastavené tloušťky čar nebo font, který není k dispozici.

Dalším často uváděným tvrzením je, že vektorová grafika má vždy menší soubor. To platí pro jednoduché tvary, ale složitá ilustrace s miliony uzlů může být objemnější než dobře komprimovaný rastrový obraz.

**Hlavní myšlenka:** vektorová grafika neukládá hotový obraz po pixelech, ale strukturovaný popis objektů, který lze znovu vykreslit v libovolném vhodném rozlišení.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Souřadnicový systém, body a cesty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Aby bylo možné objekty popsat přesně, používá vektorová grafika **souřadnicový systém**.

Každý bod má souřadnice, například:

`(x, y)`

V běžné matematice roste osa y směrem nahoru. V mnoha grafických a webových systémech ale začíná počátek v levém horním rohu a y roste směrem dolů.

Proto je při programování grafiky důležité vědět, jakou konvenci dané prostředí používá.

Složitější objekt lze popsat jako **cestu — path**. Cesta může obsahovat příkazy typu:

- přesun na bod,
- nakreslení úsečky,
- nakreslení křivky,
- uzavření tvaru.

V SVG například může cesta obsahovat příkazy `M`, `L`, `C` a `Z`.

Zjednodušený zápis:

`M 10 10 L 100 10 L 100 100 Z`

znamená: začni v bodě, nakresli dvě úsečky a cestu uzavři.

Velkou výhodou takového modelu je, že tvar není anonymní skupina pixelů. Program „ví“, že jde o samostatnou cestu, kterou lze posunout, vyplnit, duplikovat nebo použít jako masku.

Při práci s vektorovou grafikou se proto často setkáváme s pojmy:

- **anchor point / uzel** — bod definující část geometrie,
- **segment** — úsek mezi uzly,
- **path** — jedna či více navazujících částí cesty,
- **subpath** — samostatná část složené cesty.

U uzavřených cest lze aplikovat výplň. U otevřených cest se obvykle pracuje hlavně s obrysem.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vektorová grafika a rasterizace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Monitor je tvořen fyzickými pixely. Tiskárna vytváří drobné tiskové body. Vektorový objekt proto musí být při skutečném zobrazení nakonec převeden do rastrové podoby.

Tento proces se nazývá **rasterizace**.

Grafický systém vezme matematický popis objektu a rozhodne, které pixely výsledné obrazovky mají být jakou barvou.

Největší problém vzniká na hranách.

Představme si černou diagonální čáru. Na čtvercové mřížce pixelů nelze vytvořit dokonale hladkou geometrickou hranu. Bez dalších úprav by vznikly viditelné „schody“ — **aliasing**.

Proto se používá **antialiasing**. Hraniční pixely dostanou mezilehlé barvy nebo průhlednost podle toho, jak velkou část pixelu geometrický objekt pokrývá.

Výsledek pak působí hladší.

Antialiasing není totéž co **dithering**.

Dithering řeší jiný problém: jak vizuálně napodobit barvy nebo tóny, které nejsou přímo dostupné v omezené paletě nebo bitové hloubce. Používá prostorové rozložení dostupných hodnot tak, aby oko vnímalo mezitón.

Například černobílá tiskárna může pomocí různě hustých vzorů černých bodů vytvořit dojem šedé.

Rasterizace tedy řeší převod geometrie na pixely, antialiasing vyhlazení hran a dithering omezený počet dostupných tónů či barev.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vektorizace: jak z pixelů vznikne geometrie**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Opačný proces se nazývá **vektorizace** nebo trasování.

Máme-li například naskenované černobílé logo, můžeme se pokusit najít jeho hranice a převést je na křivky.

Automatický algoritmus typicky:

1. analyzuje rastrový obraz,
2. hledá oblasti podobné barvy nebo hrany,
3. odhaduje jejich geometrický tvar,
4. vytváří vektorové cesty,
5. zjednodušuje počet uzlů.

Při jednoduchém logu může být výsledek velmi dobrý. U fotografie plné textur, šumu a jemných barevných přechodů by vzniklo obrovské množství objektů a výsledek by ztratil smysl.

Vektorizace proto není univerzální způsob „zlepšení kvality fotografie“. Je vhodná tam, kde původní obraz skutečně reprezentuje jednoduchou geometrii.

Typické použití:

- digitalizace starého loga,
- převod mapových podkladů,
- technické náčrty,
- historické ornamenty,
- ručně kreslené ikony.

Dnes se při vektorizaci používá také strojové učení. AI může lépe rozpoznat, co je pravděpodobně text, symbol nebo pravidelný objekt. Stále ale vytváří **interpretaci původního rastru**, nikoli dokonale obnovuje ztracenou původní geometrii.

U důležité grafiky bývá často nejlepší kombinace: automatické trasování jako základ a následná ruční oprava uzlů a křivek.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kde se vektorová grafika používá**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Nejznámější aplikací jsou **loga a ikony**. Značka musí fungovat na vizitce i na fasádě budovy, proto je výhodné uchovávat její geometrii nezávisle na rozlišení.

Podobně funguje **typografie**. Moderní fonty obvykle popisují tvary znaků pomocí křivek. Díky tomu může stejné písmo vypadat ostře na malém displeji i při velkoformátovém tisku.

Vektorový princip je klíčový také v:

- technických schématech,
- mapách,
- infografikách,
- UI designu,
- ilustracích,
- laserovém řezání,
- plotrech,
- CAD systémech.

Na webu hraje důležitou roli **SVG**. Není to jen obrázkový formát. Je to strukturovaný XML dokument, jehož objekty lze stylovat pomocí CSS, měnit JavaScriptem a animovat.

Jedno SVG tak může být současně obraz, datová struktura i součást interaktivního uživatelského rozhraní.

**Příklad.** Mapa metra v SVG může obsahovat každou linku a stanici jako samostatný objekt. Po kliknutí lze JavaScriptem zvýraznit konkrétní trasu, zobrazit informace o stanici nebo animovat průjezd vlaku.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vektorové formáty: SVG, PDF, AI, EPS a DXF**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Různé oblasti používají různé formáty.

### SVG — Scalable Vector Graphics

SVG je otevřený webový standard založený na XML. Umí popisovat:

- cesty,
- základní geometrické tvary,
- text,
- gradienty,
- masky,
- filtry,
- transformace,
- vložené rastrové obrazy.

Díky `viewBox` může být grafika škálována do různých velikostí.

SVG se hodí pro webové ikony, diagramy, loga a interaktivní grafiku.

### PDF

PDF není čistě vektorový formát. Dokument může obsahovat vektorovou grafiku, text i rastrové obrazy. Díky tomu je velmi vhodný pro tisk a výměnu dokumentů.

### AI

AI je pracovní formát aplikace Adobe Illustrator. Může uchovávat strukturu dokumentu a editovatelné prvky. Pro dlouhodobou otevřenou výměnu dat však bývá vhodnější standardizovaný formát, pokud zachová potřebné vlastnosti.

### EPS

EPS je historicky důležitý formát založený na PostScriptu. Dlouho se používal při přenosu vektorové grafiky do sazby a tisku. V moderních workflow jej často nahrazují PDF a SVG.

### DXF

DXF je výměnný formát spojený s CAD systémy. Slouží hlavně pro přenos geometrických dat mezi technickými aplikacemi.

Při převodu mezi formáty se nemusí zachovat všechny vlastnosti. Některý formát například neumí efekty, vrstvy nebo typ objektu používaný zdrojovou aplikací.

**Hlavní myšlenka první lekce:** vektorový dokument je strukturovaný geometrický model. Při zobrazení se rasterizuje, při vektorizaci naopak odhadujeme geometrii z pixelů a jednotlivé formáty zachovávají různé části struktury.

---
---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
