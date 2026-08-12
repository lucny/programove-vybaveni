# Vektorová grafika

## Modernizovaný výukový text pro studenty informačních technologií

> Vektorový obrázek není složený z milionů barevných bodů. Je to spíše přesný recept: tady začíná křivka, tudy vede, zde se uzavírá, tuto část vyplň modrou barvou a celý tvar otoč o třicet stupňů. Stejný princip pak můžeme rozšířit od jednoduchého loga přes technický výkres až k trojrozměrnému modelu budovy, animované scéně nebo objektu rozšířené reality.

Tento text modernizuje původní výukový materiál **Vektorová grafika**. Zachovává jeho hlavní tematickou osu — princip vektorového obrazu, práci s křivkami a transformacemi, CAD, 3D modelování, realistickou vizualizaci a virtuální či rozšířenou realitu — ale jednotlivé části spojuje do šesti didakticky navazujících lekcí. Na několika místech zpřesňuje tradiční výklad a doplňuje témata, která jsou dnes pro praxi důležitá: SVG jako programovatelnou webovou grafiku, transformační matice, přesnou práci s Bézierovými křivkami, parametrický CAD, rozdíl mezi polygonálními sítěmi a NURBS, PBR materiály, princip ray tracingu a path tracingu, herní real-time rendering, rigging, motion capture, OpenXR, WebXR, inside-out tracking, SLAM a smíšenou realitu.

Text je psán jako souvislý výklad. Jednotlivé kapitoly proto nejsou jen seznamem definic, ale snaží se ukázat, proč daný princip vznikl, kde se používá a jak souvisí s dalšími oblastmi informatiky. Může tak sloužit jako podklad pro studium, komentovanou prezentaci i pozdější podcastové minipořady.

---

# 1. Principy vektorové grafiky

## 1.1 Obraz jako popis objektů místo mřížky pixelů

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

---

## 1.2 Souřadnicový systém, body a cesty

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

---

## 1.3 Vektorová grafika a rasterizace

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

---

## 1.4 Vektorizace: jak z pixelů vznikne geometrie

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

---

## 1.5 Kde se vektorová grafika používá

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

---

## 1.6 Vektorové formáty: SVG, PDF, AI, EPS a DXF

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

# 2. Přesné kreslení a práce s vektorovými objekty

## 2.1 Mřížky, vodítka, snapping a zarovnání

Vektorová grafika se často používá právě tam, kde je důležitá přesnost.

Editor proto nabízí **mřížku**, vodicí linie a různé režimy přichytávání — snapping.

Objekt lze přichytit například:

- k mřížce,
- k hraně jiného objektu,
- ke středu,
- ke koncovému bodu,
- k průsečíku,
- k vodicí linii.

To je mimořádně užitečné při tvorbě ikon, technických diagramů nebo opakujících se prvků.

Důležitou roli hraje také **zarovnání a distribuce**.

Můžeme říci:

- zarovnej všechny objekty na levou hranu,
- vycentruj je,
- rozmísti je se stejnými rozestupy.

Pro přesnou práci je to spolehlivější než posouvání objektů „od oka“.

Při návrhu rozhraní se navíc pracuje s konstrukčními systémy, například osmibodovou mřížkou nebo modulárními layouty. Vektorový editor tak není jen kreslicí nástroj, ale prostředí pro práci s geometrickými vztahy.

---

## 2.2 Bézierovy křivky: jak dvěma úchyty řídíme hladký tvar

Bézierovy křivky jsou jedním ze základních nástrojů vektorové grafiky, typografie i počítačového designu.

Nejčastěji se setkáme s **kubickou Bézierovou křivkou**, která je definována čtyřmi body:

- počáteční bod,
- první řídicí bod,
- druhý řídicí bod,
- koncový bod.

Řídicí body obvykle neleží přímo na výsledné křivce. Ovlivňují její směr a zakřivení.

V editoru je často vidíme jako **handles — úchyty** vycházející z uzlu.

Když jsou úchyty na obou stranách uzlu v jedné přímce, lze vytvořit hladké pokračování křivky. Pokud jejich směry oddělíme, vznikne ostrý roh.

Existují také **kvadratické Bézierovy křivky**, které mají jeden řídicí bod mezi počátečním a koncovým bodem. Používají se například v některých fontových technologiích.

Dobrá křivka neznamená „co nejvíce bodů“. Naopak. Příliš mnoho uzlů často vede k nerovnostem a obtížné editaci.

Profesionální kreslení se snaží popsat tvar **co nejjednodušší geometrií, která vystihuje požadovaný průběh**.

Při trasování loga tak může být ručně vytvořená křivka s několika dobře umístěnými body kvalitnější než automatický výsledek s desítkami uzlů.

---

## 2.3 B-spline a NURBS: když potřebujeme více lokální kontroly

Bézierovy křivky nejsou jediný způsob popisu hladké geometrie.

V CAD a 3D modelování se často používají **B-spline** a **NURBS** křivky.

B-spline umožňuje vytvořit hladký tvar řízený více kontrolními body. Její důležitou vlastností je **lokální kontrola**: změna jednoho kontrolního bodu může ovlivnit jen část křivky, nikoli nutně celý tvar.

NURBS znamená **Non-Uniform Rational B-Spline**.

Racionální forma používá váhy kontrolních bodů a umožňuje přesně reprezentovat také některé geometrické tvary, například kružnice a kuželosečky.

Není vhodné říkat, že B-spline je jednoduše „přesnější než Bézier“. Oba modely jsou matematicky velmi schopné. Liší se především způsobem parametrizace, lokální kontroly a vhodností pro konkrétní úlohu.

V ilustraci a typografii je Bézierova křivka velmi praktická. V průmyslovém návrhu složitých hladkých ploch se často používají NURBS.

---

## 2.4 Boolean operace: geometrická logika

Mnoho složitých tvarů nemusíme kreslit ručně. Můžeme je sestavit ze základních objektů pomocí **boolean operací**.

Typické operace jsou:

- union — sjednocení,
- intersection — průnik,
- difference — rozdíl,
- exclusive or — výlučný rozdíl.

Představme si dva překrývající se kruhy.

Sjednocení vytvoří jeden společný tvar.

Průnik ponechá pouze oblast, kterou mají kruhy společnou.

Rozdíl odečte jeden objekt od druhého.

Tento princip se používá v logotypech, ikonách, CAD modelování i 3D grafice.

Důležité je rozlišit **skupinu objektů** a **skutečné geometrické spojení**. Když dva kruhy pouze seskupíme, stále existují jako dva samostatné objekty. Boolean union může vytvořit jednu výslednou cestu.

Některé editory navíc podporují „živé“ nebo nedestruktivní boolean operace, které lze později změnit bez ztráty původních objektů.

---

## 2.5 Transformace: posun, rotace, měřítko a zkosení

Transformace mění polohu nebo tvar objektu bez ruční editace jednotlivých bodů.

Základní operace jsou:

- posun,
- rotace,
- změna měřítka,
- zrcadlení,
- zkosení.

V počítačové grafice lze tyto operace zapisovat pomocí **transformačních matic**.

Pro studenta je důležitá hlavně myšlenka, že transformace lze skládat.

Například:

1. otoč objekt,
2. zmenši ho,
3. posuň doprava.

Pořadí může ovlivnit výsledek.

Rotace kolem počátku souřadnicového systému není totéž jako rotace kolem středu objektu. Program proto často provádí pomocné posuny do a z požadovaného středu transformace.

Ve vektorové grafice mají transformace velkou výhodu: mění geometrické parametry a výsledek lze znovu rasterizovat v aktuální kvalitě.

Pokud ale vektorový dokument obsahuje rastrový obrázek, jeho zvětšování stále podléhá omezením rastrových dat.

---

## 2.6 Obrys, výplň, gradient a pořadí objektů

Geometrie určuje tvar, ale vzhled vzniká až pomocí stylu.

**Stroke — obrys** může mít:

- barvu,
- tloušťku,
- typ čáry,
- styl zakončení,
- způsob spojení segmentů.

**Fill — výplň** může být:

- jednobarevná,
- gradientní,
- vzorová,
- obrazová.

Gradient vytváří plynulý přechod mezi barvami. Může být lineární, radiální nebo podle možností editoru i složitější.

Důležité je také **pořadí kreslení**. Vektorový dokument je často zásobník objektů. Co se vykreslí později, může překrýt předchozí prvky.

Proto editory používají operace typu:

- bring to front,
- send to back,
- move forward,
- move backward.

U SVG pořadí často odpovídá pořadí elementů v dokumentu.

Vzhled objektu tak vzniká kombinací geometrie, stylu a jeho vztahu k ostatním objektům.

---

## 2.7 Text a typografie ve vektorové grafice

Text je zvláštní vektorový objekt.

Dokud zůstává textem, uchovává:

- znakovou informaci,
- font,
- velikost,
- řez,
- proklad,
- další typografické vlastnosti.

To je výhodné pro editaci a přístupnost.

Při převodu **textu na křivky** se jednotlivé znaky změní na geometrické obrysy. Dokument už nepotřebuje původní font pro vykreslení těchto znaků.

To může být užitečné při exportu loga nebo výrobních podkladů, ale ztrácíme možnost text běžně editovat, kopírovat nebo interpretovat jako skutečné znaky.

Proto není vhodné převádět veškerý text na křivky automaticky.

Moderní PDF a jiné formáty umějí fonty vkládat nebo subsetovat, takže lze často zachovat skutečný text.

**Hlavní myšlenka druhé lekce:** přesná vektorová práce nevzniká ručním „trefováním“ objektů. Používá souřadnice, snapping, matematicky definované křivky, logické operace, transformace a strukturovaný text.

---

# 3. Technické kreslení a CAD

## 3.1 Co je CAD a proč není jen digitální rýsovací prkno

**CAD — Computer-Aided Design** označuje počítačovou podporu návrhu.

První CAD systémy často připomínaly elektronické rýsovací prkno: čáry, kružnice, kóty a vrstvy byly vytvářeny přesněji než ručně.

Moderní CAD ale sahá mnohem dál.

Umožňuje vytvářet:

- 2D technické výkresy,
- 3D tělesa,
- sestavy,
- parametrické modely,
- výrobní dokumentaci,
- technické analýzy,
- vizualizace.

Zásadní rozdíl oproti běžnému grafickému editoru spočívá ve významu geometrie.

Čára v ilustraci může být jen vizuální prvek. Čára v technickém výkresu může reprezentovat přesně definovanou hranu součásti o délce 42 mm.

CAD proto pracuje s jednotkami, vazbami, tolerancemi a konstrukční logikou.

Používá se například ve:

- strojírenství,
- architektuře,
- stavebnictví,
- elektrotechnice,
- produktovém designu,
- automobilovém a leteckém průmyslu.

---

## 3.2 Parametrický model: konstrukce, která zná své vztahy

Tradiční kresba obsahuje geometrii. **Parametrický CAD model** navíc obsahuje vztahy.

Představme si obdélník.

Můžeme mu určit:

- šířka = 80 mm,
- výška = 40 mm,
- protilehlé strany jsou rovnoběžné,
- sousední strany jsou kolmé.

Do středu přidáme otvor a řekneme:

- průměr = 10 mm,
- střed otvoru leží na středu obdélníku.

Když později změníme šířku obdélníku na 100 mm, správně vytvořený model přepočítá pozici otvoru.

To je zásadní rozdíl mezi „nakreslenou geometrií“ a **modelem konstrukčního záměru**.

Parametry mohou být propojeny rovnicemi. Například:

`šířka = 2 × výška`

Model pak není jen výsledný tvar, ale systém závislostí.

Tato logika umožňuje vytvářet celé rodiny výrobků různých velikostí ze stejného konstrukčního základu.

---

## 3.3 Sketch, constraints a tvorba 3D tělesa

V parametrickém strojírenském CAD workflow často začínáme **skicou — sketch**.

Skica obsahuje 2D geometrii:

- čáry,
- oblouky,
- kružnice,
- body.

Na geometrii aplikujeme **constraints — vazby**.

Mohou určovat:

- vodorovnost,
- svislost,
- rovnoběžnost,
- kolmost,
- soustřednost,
- shodnost,
- vzdálenost,
- úhel.

Dobře definovaná skica má takový počet vazeb a rozměrů, aby se nechovala nečekaně.

Ze skici pak lze vytvořit 3D těleso například operací:

- extrude — vysunutí,
- revolve — rotace profilu,
- sweep — tažení profilu po dráze,
- loft — přechod mezi profily.

Další operace mohou přidat otvor, zaoblení, sražení hrany nebo skořepinu.

Výsledný model často uchovává **historii konstrukčních operací**. Když změníme první rozměr, software přepočítá následné kroky.

To je velmi mocný, ale někdy i křehký systém. Nevhodně navázané operace mohou po velké změně vstupní geometrie selhat.

---

## 3.4 Technický výkres, kóty a tolerance

3D model sám o sobě nemusí být dostatečným výrobním dokumentem.

Technický výkres musí sdělit, co se má vyrobit a s jakou přesností.

Používá:

- pohledy,
- řezy,
- kóty,
- šrafování,
- značky,
- tolerance,
- informace o materiálu a povrchu.

**Kóta** není jen grafická čára s číslem. Vyjadřuje požadovaný rozměr.

V reálné výrobě nelze většinu rozměrů vytvořit absolutně přesně. Proto se používají **tolerance**, které určují přijatelný rozsah.

Například:

`20,00 ± 0,05 mm`

znamená jiný výrobní požadavek než neurčitě napsané „asi 20 mm“.

Pokročilé výkresy používají také geometrické tolerance a standardizované značky.

Technické kreslení je proto jazyk s přesnými pravidly. Cílem není esteticky pěkná ilustrace, ale **jednoznačná technická komunikace**.

---

## 3.5 Vrstvy, bloky a knihovny objektů

Ve 2D CAD systémech se používají **layers — hladiny**.

Na oddělených hladinách mohou být například:

- nosné konstrukce,
- elektroinstalace,
- kóty,
- text,
- skryté čáry.

Hladinu lze skrýt, uzamknout nebo nastavit její styl.

Dalším důležitým prvkem jsou **bloky**.

Blok sdružuje několik geometrických prvků do opakovatelně použitelné definice. Může představovat například:

- dveře,
- šroub,
- elektrickou zásuvku,
- značku,
- nábytkový prvek.

Pokud systém používá instancování, změna definice může aktualizovat mnoho výskytů.

To je informaticky zajímavý princip: místo mnoha nezávislých kopií uchováváme **jednu definici a odkazy na její instance**.

Stejnou myšlenku najdeme v programování, databázích, 3D grafice i herních enginech.

---

## 3.6 CAD, CAE a CAM

CAD není celý digitální výrobní řetězec.

**CAD** se soustředí na návrh a model.

**CAE — Computer-Aided Engineering** zahrnuje inženýrské analýzy a simulace, například:

- pevnostní výpočty,
- proudění tekutin,
- tepelnou analýzu,
- dynamiku.

**CAM — Computer-Aided Manufacturing** připravuje výrobní postup a strojové dráhy.

U CNC frézování CAM řeší například:

- výběr nástroje,
- strategii obrábění,
- rychlosti,
- posuvy,
- bezpečné nájezdy,
- generování strojového programu.

Výsledkem může být G-code, ale konkrétní stroje a výrobní procesy používají různé řídicí formáty a postprocesory.

U 3D tisku se obvykle používá **slicer**. Ten převede 3D model na vrstvy a vytvoří dráhy tiskové hlavy. Výstupem u mnoha FDM tiskáren bývá G-code.

Je však zjednodušující říci, že každý 3D tisk „je CAM a vždy generuje stejný G-code“. Výrobní technologie a řídicí řetězce se liší.

---

## 3.7 CAD software a otevřené formáty

Mezi známé CAD systémy patří:

- AutoCAD,
- Autodesk Fusion,
- SolidWorks,
- CATIA,
- Siemens NX,
- FreeCAD.

Každý je zaměřen trochu jinak.

AutoCAD má silnou tradici v 2D technickém kreslení a obecné CAD práci.

SolidWorks je výrazně zaměřen na parametrické strojírenské modelování a sestavy.

CATIA a Siemens NX se používají v rozsáhlém průmyslovém návrhu.

Autodesk Fusion propojuje CAD, CAM a další cloudové workflow.

FreeCAD je open-source parametrický CAD.

Velkým problémem CAD je **výměna dat**.

Vedle proprietárních formátů se používají například:

- DXF,
- STEP,
- IGES,
- STL,
- 3MF.

Tyto formáty ale přenášejí odlišnou úroveň informace.

STL typicky uchovává hlavně triangulovaný povrch. Neobsahuje plnou historii parametrického CAD modelu.

STEP dokáže přenášet bohatší geometrickou a produktovou informaci.

Při exportu proto musíme vědět, co potřebuje příjemce: vizuální síť, přesnou geometrii, výrobní model nebo editovatelnou konstrukční historii.

**Hlavní myšlenka třetí lekce:** CAD není jen přesné kreslení. Moderní CAD model uchovává konstrukční vztahy a tvoří základ digitálního řetězce od návrhu přes simulaci až po výrobu.

---

# 4. Trojrozměrné modelování a digitální scéna

## 4.1 3D scéna: více než samotný model

Když se řekne 3D grafika, mnoho lidí si představí trojrozměrný model. Výsledný obraz ale vzniká z celé **scény**.

Scéna může obsahovat:

- geometrické objekty,
- materiály,
- textury,
- světla,
- kamery,
- animace,
- částicové systémy,
- fyzikální simulace.

Model je tedy jen jedna část.

Aby byl šedý model auta viditelný jako realistický automobil, potřebujeme určit, jak jeho lak reaguje na světlo, jaké je okolní prostředí, odkud se na něj dívá kamera a jak se vypočítají odrazy.

Moderní 3D software proto připomíná kombinaci:

- modelářské dílny,
- fotografického studia,
- filmového animačního pracoviště,
- fyzikálního simulátoru.

---

## 4.2 Polygonální síť: vrcholy, hrany a plochy

Nejběžnější reprezentací v real-time grafice a mnoha 3D programech je **polygonální mesh — síť**.

Je tvořena:

- vertices — vrcholy,
- edges — hranami,
- faces — plochami.

Grafická karta nakonec velmi často pracuje s **trojúhelníky**, protože trojúhelník vždy leží v jedné rovině a jeho rasterizace je dobře definovaná.

Model může být při práci vytvořen z čtyřúhelníků nebo složitějších polygonů, ale při renderování se obvykle trianguluje.

Důležitá je **topologie** — způsob, jak jsou vrcholy a hrany propojeny.

Dobrá topologie je zásadní například pro animaci postavy. Síť kolem lokte musí být navržena tak, aby se při ohnutí deformovala přirozeně.

Počet polygonů ovlivňuje detail i výpočetní náročnost. Filmový model může mít miliony polygonů, real-time hra musí hlídat výkon.

Moderní systémy umějí pracovat s velmi vysokou geometrickou složitostí, ale optimalizace stále zůstává důležitou součástí grafiky.

---

## 4.3 NURBS, subdivision a sculpting

Polygonální modelování není jediný přístup.

**NURBS modelování** používá matematické křivky a plochy. Je velmi vhodné pro hladké technické povrchy, například karoserie automobilu nebo průmyslový design.

**Subdivision surface** začíná z relativně hrubé polygonální sítě a matematicky vytváří hladší povrch. Modelář tak může ovládat velký tvar pomocí menšího počtu základních polygonů.

**Sculpting** napodobuje digitální sochařství. Uživatel pomocí virtuálních štětců tlačí, vyhlazuje nebo vytahuje povrch.

Používá se například pro:

- postavy,
- organické modely,
- tváře,
- fantastické bytosti,
- jemné povrchové detaily.

V profesionálním workflow se metody často kombinují.

Postava může vzniknout sculptingem ve vysokém detailu. Potom se vytvoří jednodušší topologie vhodná pro animaci — **retopology** — a jemné detaily se přenesou do normálových nebo displacement map.

Neexistuje tedy jediný „správný“ způsob 3D modelování. Volba závisí na tom, zda připravujeme technický díl, filmovou postavu, herní prostředí nebo model pro 3D tisk.

---

## 4.4 UV mapping a textury

3D geometrie určuje tvar, ale povrch potřebuje další informace.

**UV mapping** převádí povrch 3D modelu do 2D souřadnicové mapy.

Můžeme si to představit podobně jako rozložení papírového modelu krabice na rovinu.

Na tento 2D „střih“ lze položit texturu.

Písmena U a V se používají proto, že X, Y a Z už tradičně označují prostorové souřadnice.

Textura nemusí znamenat jen barevnou fotografii povrchu. Moderní materiál může používat několik map:

- base color,
- roughness,
- metallic,
- normal,
- displacement,
- ambient occlusion.

Normálová mapa například vytváří dojem drobných nerovností změnou orientace povrchových normál bez toho, aby skutečně přidala odpovídající polygonální geometrii.

Displacement může naopak geometrický povrch skutečně posouvat.

Textury lze také generovat **procedurálně** pomocí matematických funkcí a uzlových systémů. Tím lze vytvářet například dřevo, kámen, mraky nebo šum bez klasického obrazového souboru.

---

## 4.5 PBR materiály: jak povrch reaguje na světlo

Moderní real-time i filmová grafika často používá **PBR — Physically Based Rendering**.

Cílem není dokonale simulovat veškerou fyziku světla, ale používat materiálový model, který se chová konzistentněji a fyzikálně uvěřitelně v různých světelných podmínkách.

Častý workflow používá parametry:

- base color,
- metallic,
- roughness.

**Metallic** určuje, zda se materiál chová více jako kov nebo dielektrikum.

**Roughness** ovlivňuje mikrostrukturu povrchu a tím ostrost odrazů.

Hladký lak může mít ostré odlesky, hrubý povrch rozptýlené.

Základem je **BRDF — Bidirectional Reflectance Distribution Function**, matematický model popisující, jak se světlo odráží podle směru dopadu a pozorování.

Student nemusí počítat BRDF integrály, ale měl by pochopit, že materiál není jen „barva objektu“.

Stejná šedá barva může vypadat jako:

- kov,
- plast,
- guma,
- keramika,

podle způsobu interakce se světlem.

---

## 4.6 Kamera, projekce a perspektiva

3D scéna se musí převést na 2D obraz.

K tomu slouží virtuální kamera.

**Perspektivní projekce** napodobuje běžnou kameru: vzdálené objekty se jeví menší.

**Ortografická projekce** zachovává měřítko nezávisle na vzdálenosti. Používá se v technických pohledech a některých stylizovaných hrách.

Kamera má parametry podobné fotografii:

- pozice,
- směr,
- zorné pole,
- clipping planes,
- někdy fyzicky modelovanou ohniskovou vzdálenost a clonu.

Při renderování architektury nebo filmu se proto znalosti digitální fotografie přímo propojují s 3D grafikou.

Virtuální kamera může simulovat:

- hloubku ostrosti,
- motion blur,
- zkreslení objektivu,
- expozici.

Rozdíl je v tom, že virtuální scéna dovoluje téměř úplnou kontrolu nad prostředím.

---

## 4.7 Světla a prostředí

Bez světla není vidět materiál ani tvar.

3D programy poskytují různé typy světel:

- point light,
- spot light,
- directional light,
- area light,
- environment lighting.

Jednoduché **point light** vyzařuje z bodu.

**Directional light** napodobuje velmi vzdálený zdroj, typicky slunce, takže paprsky mají přibližně stejný směr.

**Area light** má nenulovou plochu a vytváří měkčí stíny.

Moderní scény často používají **HDRI environment maps** jako zdroj okolního osvětlení a odrazů.

Historický pojem „ambient light“ jako jednoduché rovnoměrné přisvícení je užitečný pro základní model, ale fyzikálně realističtější rendering se snaží světlo od prostředí a nepřímé odrazy vypočítat skutečněji.

**Hlavní myšlenka čtvrté lekce:** 3D grafika není jen tvorba geometrie. Výsledný obraz vzniká kombinací modelu, topologie, materiálů, textur, kamery a osvětlení.

---

# 5. Rendering a animace

## 5.1 Rendering: cesta od scény k výslednému obrazu

**Rendering** je výpočet výsledného 2D obrazu z popisu 3D scény.

Program musí rozhodnout například:

- které objekty kamera vidí,
- jakou barvu má každý bod povrchu,
- zda je ve stínu,
- co se v něm odráží,
- jak na něj dopadá nepřímé světlo.

U real-time aplikace musí celý proces proběhnout desítky nebo stovkykrát za sekundu.

U filmového renderingu může jediný snímek trvat minuty nebo hodiny, pokud je prioritou maximální kvalita.

Existují proto různé renderovací přístupy.

Nejznámější jsou:

- rasterizace,
- ray tracing,
- path tracing.

Moderní enginy je často kombinují.

---

## 5.2 Rasterizace v 3D grafice

3D rasterizace převádí geometrické trojúhelníky na fragmenty a pixely obrazovky.

Zjednodušeně:

1. vrcholy modelu se transformují do prostoru kamery,
2. geometrie se promítne na 2D plochu,
3. trojúhelníky se rasterizují,
4. shader vypočítá vlastnosti pixelů.

Grafické procesory jsou pro tento proces extrémně optimalizované.

Proto rasterizace dlouho dominovala real-time grafice.

Realistické stíny, odrazy a nepřímé světlo se v klasické rasterizační pipeline často řeší pomocí aproximací:

- shadow maps,
- reflection probes,
- screen-space reflections,
- baked lightmaps.

Výsledek může být velmi přesvědčivý, ale některé efekty selhávají v případech, které aproximace nepokrývá.

---

## 5.3 Ray tracing a cesta paprsku

**Ray tracing** sleduje virtuální paprsky a jejich průsečíky se scénou.

Často se vysvětluje, že „simuluje cestu světla od zdroje“. V klasickém počítačovém ray tracingu se však prakticky často postupuje opačně: primární paprsek vysíláme **z kamery do scény**, protože nás zajímají pouze cesty, které mohou přispět do výsledného pixelu.

Po zásahu povrchu lze vyslat další paprsky:

- ke světlu kvůli stínu,
- ve směru odrazu,
- ve směru lomu.

Tím lze přirozeněji vypočítat odrazy a průhlednost než pomocí mnoha rasterizačních triků.

Ray tracing je výpočetně náročný, ale moderní GPU mají specializovaný hardware pro akceleraci průsečíků paprsků s geometrií.

Proto se dnes používá také v real-time hrách, často v hybridní kombinaci s rasterizací.

---

## 5.4 Path tracing a global illumination

**Path tracing** je Monte Carlo metoda pro simulaci transportu světla.

Z kamery vysílá paprsky do scény a při každém zásahu náhodně vzorkuje možné další směry. Mnoho takových cest postupně odhaduje světelný příspěvek.

Díky tomu může přirozeně zahrnout:

- přímé světlo,
- nepřímé odrazy,
- měkké stíny,
- color bleeding,
- vícečetné odrazy.

Výsledný obraz je zpočátku zašuměný. S rostoucím počtem vzorků se odhad zpřesňuje.

Moderní renderer může použít **denoising**, který pomáhá z menšího počtu vzorků rekonstruovat čistší obraz.

**Global illumination** není jedna konkrétní kombinace ray tracingu a radiosity. Je to obecný pojem pro techniky, které počítají také **nepřímé osvětlení**, tedy světlo odražené mezi povrchy.

Path tracing je jednou z metod global illumination.

**Radiosity** je historicky významná metoda vhodná především pro difuzní výměnu energie mezi plochami.

---

## 5.5 Ambient occlusion a proč roh bývá tmavší

**Ambient occlusion — AO** odhaduje, jak moc je určitý bod povrchu „zakrytý“ okolní geometrií.

Roh místnosti, škvíra nebo místo, kde se dva objekty téměř dotýkají, má menší přístup k okolnímu světlu než volně vystavená plocha.

AO proto vytváří jemné kontaktní stíny, které pomáhají číst tvar.

Nejde ale o kompletní fyzikální osvětlení. Je to aproximace viditelnosti okolní hemisféry.

V real-time grafice existují screen-space varianty jako SSAO, které pracují pouze s informacemi aktuálně viditelnými na obrazovce.

Výsledek je rychlý, ale může mít artefakty.

AO se často používá jako jedna součást širšího PBR a global illumination workflow.

---

## 5.6 Keyframe animace a interpolace

Animace znamená změnu vlastností v čase.

V **keyframe animaci** animátor nastaví hodnoty v určitých klíčových okamžicích.

Například:

čas 0 s → objekt je vlevo,

čas 2 s → objekt je vpravo.

Program vypočítá mezilehlé stavy pomocí interpolace.

Animovat lze:

- pozici,
- rotaci,
- měřítko,
- barvu,
- intenzitu světla,
- parametry materiálu,
- tvar objektu.

Interpolace nemusí být lineární. Křivky v animačním editoru umožňují vytvářet zrychlení, zpomalení a přirozené časování.

Právě timing a spacing jsou zásadní pro dojem pohybu. Technicky správná interpolace může působit roboticky, pokud nerespektuje principy animace.

---

## 5.7 Rigging, skinning a animace postavy

Složitou postavu nechceme animovat posouváním tisíců vrcholů.

Proto se vytváří **rig — kostra a řídicí systém**.

Kostru tvoří hierarchie bones.

Například pohyb předloktí závisí na lokti, pohyb ruky na předloktí a podobně.

Síť postavy se ke kostře připojí pomocí **skinningu**. Jednotlivé vrcholy mohou být ovlivňovány několika kostmi s různými vahami.

Pokud je skinning špatně nastaven, při ohnutí lokte nebo kolena vzniknou nepřirozené deformace.

Animátor často nepohybuje kostmi přímo, ale používá ovládací prvky a **inverse kinematics — IK**.

U IK například určí pozici chodidla a systém dopočítá potřebné úhly nohy.

To je výhodné při kontaktu postavy se zemí nebo objektem.

---

## 5.8 Motion capture a particle systems

**Motion capture** zaznamenává pohyb skutečného člověka nebo objektu a převádí jej na animační data.

Systém může používat:

- optické markery,
- inerciální senzory,
- kamery bez markerů,
- kombinované metody.

Data z motion capture obvykle nejsou hotová animace. Je potřeba je vyčistit, přizpůsobit virtuální postavě a ručně upravit.

Podobně **particle system** není jen „animace kouře“.

Částicový systém vytváří mnoho jednoduchých prvků, jejichž vznik, pohyb a zánik řídí pravidla.

Používá se pro:

- jiskry,
- déšť,
- prach,
- kouř,
- magické efekty,
- hejna.

Moderní kouř a kapaliny ale mohou využívat i komplexní fyzikální simulace, kde částice tvoří jen jednu část systému.

**Hlavní myšlenka páté lekce:** rendering řeší, jak ze scény vznikne obraz, zatímco animace určuje, jak se scéna mění v čase. Realistický výsledek často kombinuje fyzikální modely, aproximace, výtvarné rozhodování a vysoký výpočetní výkon.

---

# 6. Virtuální, rozšířená a smíšená realita

## 6.1 XR jako společná rodina technologií

Pojmy VR a AR se často učí odděleně. Dnes je užitečné používat širší pojem **XR — Extended Reality** jako společnou rodinu technologií.

Patří sem:

- VR — virtual reality,
- AR — augmented reality,
- MR — mixed reality.

Hranice mezi nimi se mohou překrývat.

**Virtuální realita** nahrazuje většinu běžného vizuálního vjemu digitálním prostředím.

Toto prostředí nemusí být „něco, co ve skutečnosti neexistuje“. Může jít také o digitální rekonstrukci skutečného místa, simulátor kokpitu nebo stereoskopické 360° video.

**Rozšířená realita** přidává digitální obsah k pohledu na reálné prostředí.

**Mixed reality** zdůrazňuje, že digitální objekty jsou prostorově ukotvené a mohou reagovat na geometrii skutečného prostředí.

Moderní headset s kamerovým passthrough může během jedné aplikace plynule přecházet mezi plně virtuálním a kombinovaným prostředím.

Proto není vždy užitečné hledat ostrou hranici mezi všemi marketingovými názvy. Důležitější je technický způsob zobrazení, sledování a interakce.

---

## 6.2 Headset: displej, optika a stereoskopie

VR headset musí vytvořit přesvědčivý obraz pro každé oko.

Používá:

- jeden nebo více displejů,
- optiku,
- senzory pohybu,
- často kamery pro tracking.

Každé oko dostává mírně odlišný obraz, čímž vzniká **stereoskopická disparita** a pocit hloubky.

Optika umožňuje oku zaostřit na displej umístěný velmi blízko obličeje a zároveň vytváří široké zorné pole.

Důležité parametry headsetu jsou například:

- rozlišení,
- field of view,
- refresh rate,
- hmotnost,
- kvalita čoček,
- motion-to-photon latency.

Samotné rozlišení displeje nevystihuje ostrost. Záleží také na zorném poli a optické kvalitě.

Používá se například veličina **pixels per degree**, která lépe souvisí s tím, kolik pixelů připadá na část zorného pole.

---

## 6.3 3DoF a 6DoF: jak systém ví, kde máme hlavu

Pro kvalitní prostorový zážitek musí headset znát polohu a orientaci uživatele.

**3DoF — three degrees of freedom** sleduje rotaci:

- pitch,
- yaw,
- roll.

Uživatel se může rozhlížet, ale systém přesně neví, že se fyzicky posunul dopředu nebo do strany.

**6DoF — six degrees of freedom** přidává tři translační osy:

- x,
- y,
- z.

Headset tak sleduje rotaci i polohu v prostoru.

Moderní standalone VR používá často **inside-out tracking**. Kamery na headsetu sledují okolní prostředí a společně s inerciálními senzory odhadují pohyb zařízení.

Starší nebo specializované systémy mohou používat externí základnové stanice či kamery.

Stejný problém musí řešit také ovladače a ruce uživatele.

---

## 6.4 SLAM, prostorová mapa a AR

Aby digitální objekt zůstal například na skutečném stole, systém musí rozumět pohybu kamery i okolní geometrii.

Jednou ze zásadních technologií je **SLAM — Simultaneous Localization and Mapping**.

Systém současně:

- odhaduje vlastní polohu,
- vytváří mapu okolí.

Používá obrazové body, inerciální senzory a někdy hloubková data.

AR systém může detekovat:

- roviny,
- stěny,
- podlahu,
- objekty,
- prostorové body.

Starší AR aplikace často používaly **markery** — známé obrazce, jejichž polohu bylo snadné rozpoznat.

Marker-based AR je stále užitečná, ale moderní systémy dokážou pracovat také **markerless** pomocí SLAM, image tracking nebo geolokace.

To umožňuje postavit virtuální židli na skutečnou podlahu bez vytištěné značky.

---

## 6.5 Interakce: ovladače, ruce, oči a hlas

Prostorová aplikace potřebuje nový způsob ovládání.

Myš a klávesnice nejsou vždy vhodné pro prostředí, ve kterém se uživatel otáčí a pracuje rukama.

VR systémy proto používají:

- tracked controllers,
- hand tracking,
- eye tracking,
- voice input,
- haptiku.

**Hand tracking** se snaží z kamer rekonstruovat polohu prstů.

**Eye tracking** zjišťuje, kam se uživatel dívá. Může pomoci při výběru objektů nebo při technice **foveated rendering**.

Foveated rendering využívá skutečnosti, že lidské oko má nejvyšší ostrost ve foveální oblasti. Systém může renderovat vysoký detail především tam, kam se uživatel právě dívá, a periferní obraz zjednodušit.

Haptika poskytuje fyzickou zpětnou vazbu. Běžné ovladače používají vibrace, pokročilé systémy mohou simulovat odpor nebo tlak.

Přirozená interakce ale není automaticky jednoduchá. Virtuální tlačítko bez fyzického odporu může být méně přesné než skutečné tlačítko. Design XR proto musí respektovat ergonomii a omezení lidského těla.

---

## 6.6 Latence, obnovovací frekvence a cybersickness

Ve VR je velmi citlivý vztah mezi pohybem hlavy a změnou obrazu.

Když uživatel otočí hlavu, systém musí:

1. pohyb změřit,
2. aktualizovat pozici kamery,
3. vyrenderovat nový obraz,
4. zobrazit jej.

Celkové zpoždění se často označuje jako **motion-to-photon latency**.

Pokud je příliš vysoké, vizuální informace neodpovídá vestibulárnímu vjemu pohybu.

To může přispět k **cybersickness** — nevolnosti, dezorientaci nebo únavě.

Důležitá je také stabilní obnovovací frekvence. Kolísající frame rate může být ve VR výrazně nepříjemnější než na běžném monitoru.

Designéři proto řeší:

- vysoký a stabilní výkon,
- nízkou latenci,
- předvídání pohybu,
- reprojekci,
- vhodný způsob virtuální lokomoce.

Teleportace může být méně realistická než plynulá chůze joystickem, ale pro některé uživatele je mnohem komfortnější.

---

## 6.7 VR, AR a MR v praxi

XR technologie nejsou jen herní zařízení.

### Výuka a školení

Lze simulovat situace, které jsou:

- drahé,
- nebezpečné,
- vzácné,
- obtížně dostupné.

Student může například trénovat práci s průmyslovým strojem nebo projít virtuální laboratoř.

### Průmysl

AR může zobrazit pracovníkovi montážní instrukce přímo nad skutečým zařízením.

MR lze využít při vzdálené spolupráci, kdy odborník vidí prostorovou situaci technika v terénu.

### Architektura a design

Virtuální model budovy lze procházet ještě před stavbou.

AR umožní umístit budoucí nábytek nebo zařízení do skutečné místnosti.

### Zdravotnictví

Používají se tréninkové simulace, vizualizace anatomie, rehabilitační aplikace nebo prostorová navigace.

### Kultura

Muzea mohou kombinovat fyzické exponáty s prostorovými digitálními vrstvami.

Přínos ale vždy závisí na tom, zda prostorová technologie skutečně řeší problém. Použití headsetu jen proto, že „VR je moderní“, může uživatelský zážitek naopak zhoršit.

---

## 6.8 Unity, Unreal Engine, OpenXR, WebXR a A-Frame

Pro vývoj XR aplikací se používají herní enginy a specializovaná API.

**Unity** je široce používaný engine pro interaktivní 3D aplikace, mobilní AR i VR.

**Unreal Engine** nabízí pokročilé real-time renderování a je silně využíván v hrách, vizualizaci a virtuální produkci.

Důležitým standardem je **OpenXR**, který vytváří společné API pro různé XR headsety a platformy. Vývojář tak nemusí každé zařízení obsluhovat úplně jiným rozhraním.

Pro web existuje **WebXR Device API**.

Umožňuje webové aplikaci přistupovat k XR relaci přímo v kompatibilním prohlížeči.

**A-Frame** je framework založený na HTML-like deklarativním zápisu, který usnadňuje tvorbu 3D a WebXR scén.

Například jednoduchá webová scéna může být popsána několika elementy místo rozsáhlého nízkoúrovňového WebGL kódu.

Vedle toho existují knihovny jako Three.js a Babylon.js, které lze použít také pro prostorovou grafiku a WebXR.

Vývoj XR proto propojuje témata celého okruhu:

- vektorovou matematiku,
- 3D geometrii,
- materiály,
- rendering,
- animaci,
- senzory,
- uživatelské rozhraní.

**Hlavní myšlenka šesté lekce:** XR není jen „3D obraz v brýlích“. Fungující prostorový systém musí v reálném čase spojit 3D scénu, tracking, senzory, rendering, optiku a interakci člověka se systémem.

---

# Závěrečné propojení kurzu

Vektorová grafika začíná jednoduchou myšlenkou: obraz nemusíme ukládat jako mřížku pixelů. Můžeme uložit **strukturu a vztahy**.

Z bodů vznikají křivky a tvary:

**bod → segment → křivka → objekt → ilustrace**

Stejnou myšlenku lze rozšířit do technického návrhu:

**skica → vazby → parametrický model → technický výkres → výroba**

A dále do 3D grafiky:

**geometrie → materiál → textura → světlo → kamera → rendering**

Když přidáme čas:

**3D scéna → rig → animace → simulace → obrazová sekvence**

A když k obrazu přidáme tracking skutečného uživatele a prostorovou interakci:

**3D scéna → real-time rendering → headset → tracking → XR prostředí**

Celý tematický okruh tak není souborem nesouvisejících programů typu Illustrator, AutoCAD, Blender a Unity. Všechny stojí na příbuzné informatické myšlence: **digitální svět lze popsat pomocí objektů, jejich parametrů, vztahů a transformací a z tohoto modelu potom vypočítat konkrétní obraz nebo fyzický výstup**.

Právě proto je vektorová grafika důležitým mostem mezi běžnou 2D grafikou, technickým návrhem, 3D modelováním, animací a prostorovými technologiemi budoucnosti.
