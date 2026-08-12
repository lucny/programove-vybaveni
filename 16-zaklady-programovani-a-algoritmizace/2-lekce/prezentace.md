## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Historický vývoj programování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Počátky programování úzce souvisí s vývojem výpočetní techniky. První počítače byly konstruovány pro řešení konkrétních výpočetních úloh a jejich programování bylo velmi složité a časově náročné. Například první programy pro počítač ENIAC byly zadávány pomocí přepínačů a kabelů. V nejranějších fázích se programy zapisovaly přímo ve strojovém kódu, tedy jako posloupnosti nul a jedniček. Tento způsob programování byl velmi nepřehledný, náchylný k chybám a silně závislý na konkrétním typu procesoru. Postupně vznikly assemblerové jazyky, které umožnily zapisovat strojové instrukce pomocí symbolických názvů (mnemotechnických zkratek). Přesto zůstávalo programování stále úzce svázané s konkrétním hardwarem. S rozvojem výpočetní techniky a rostoucí složitostí programů začaly vznikat vyšší programovací jazyky, které se snažily přiblížit způsob zápisu lidskému myšlení. Tyto jazyky umožnily:

- zvyšovat produktivitu programátorů,
- psát přehlednější a lépe udržovatelný kód,
- vytvářet přenositelnější programy. Mezi historicky významné vyšší programovací jazyky patří například Fortran, CO-
BOL, Pascal nebo C. Tyto jazyky položily základy moderního programování a mnohé jejich principy se používají dodnes.

## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Co je rastrová grafika?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Rastrový obraz je tvořen **pravidelnou mřížkou obrazových bodů — pixelů**. Každý pixel nese číselnou informaci o své barvě, případně také o průhlednosti. Když jsou pixely dostatečně malé a zobrazujeme obraz z běžné vzdálenosti, lidské oko je přestane vnímat jako samostatné čtverečky a spojí je do souvislé fotografie, kresby nebo textury.

Tento princip je velmi odlišný od vektorové grafiky. Vektorový obrázek popisuje objekty matematicky: například „nakresli kružnici s tímto středem a poloměrem“. Rastrový obrázek naproti tomu říká: „na této pozici je pixel s takovou barvou, vedle něj další pixel s jinou barvou“.

Proto se rastrová grafika výborně hodí tam, kde má obraz obsahovat velké množství jemných barevných a jasových změn — především u **digitální fotografie**, digitální malby, textur, naskenovaných dokumentů, obrazových efektů nebo výsledků renderingu.

Její hlavní omezení vychází ze stejného principu. Rastrový obraz má konečný počet vzorků. Když jej výrazně zvětšíme, původní pixely nestačí a program musí vytvořit nové hodnoty. Nemůže však objevit detail, který ve zdrojovém obrazu nikdy nebyl zachycen.

Klasické zvětšení proto vede k měkkému obrazu nebo k viditelné pixelizaci. Moderní algoritmy a AI super-resolution mohou chybějící strukturu **odhadovat**, ale to neznamená, že rekonstruují původní scénu s jistotou. Část detailů může být synteticky vytvořená.

Rastrový princip používají také obrazovky. Monitor má fyzickou mřížku obrazových prvků, ale jeden pixel obrázku nemusí vždy přesně odpovídat jednomu fyzickému pixelu displeje. Operační systém, prohlížeč nebo grafická aplikace může obraz škálovat podle hustoty displeje a nastaveného měřítka.

**Příklad z praxe.** Fotografie o rozměrech `4000 × 3000 px` obsahuje 12 milionů pixelů. To odpovídá 12 megapixelům. Pokud ji zobrazíme na monitoru 1920 × 1080, musí být zmenšena — monitor nemá dost fyzických pixelů, aby ukázal všechny obrazové vzorky současně v poměru 1 : 1.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rozměry obrazu, rozlišení a megapixely**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Slovo **rozlišení** se používá v několika významech a právě proto často vzniká zmatek.

U digitálního obrázku je nejpřesnější nejprve uvést jeho **pixelové rozměry**:

`šířka × výška`

Například:

`1920 × 1080 px`

Takový obraz obsahuje:

`1920 × 1080 = 2 073 600 pixelů`

tedy přibližně 2,07 megapixelu.

Fotografie `6000 × 4000 px` obsahuje 24 milionů pixelů, tedy přibližně 24 Mpx.

Počet megapixelů však sám o sobě neurčuje kvalitu fotografie. Dva fotoaparáty mohou mít stejný počet pixelů a přitom velmi odlišnou kvalitu výsledku kvůli rozdílné velikosti snímače, objektivu, šumu, dynamickému rozsahu, zpracování nebo kvalitě zaostření.

Stejně tak více pixelů není vždy prakticky přínosných. Pokud bude výsledná fotografie zobrazena pouze jako malý náhled na webu, extrémně vysoké rozlišení znamená hlavně větší datový objem a delší zpracování.

Rozlišení proto musíme vždy vztahovat k účelu:

- zobrazení na obrazovce,
- tisk,
- další ořez,
- archivace,
- strojové zpracování,
- publikace na webu.

Důležité je také rozlišit **ořez** a **změnu velikosti**. Ořez odstraní část obrazu a ponechá zbývající pixely beze změny. Zmenšení nebo zvětšení naproti tomu mění počet pixelů a vyžaduje přepočet obrazových dat.

**Příklad.** Máme fotografii `6000 × 4000 px` a vyřízneme prostřední čtvrtinu plochy. Výsledný obraz může mít zhruba `3000 × 2000 px`. Nezhoršili jsme kvalitu jednotlivých zbývajících pixelů, ale ztratili jsme část původního záběru a tím také část celkového rozlišení.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**PPI, DPI a proč „72 DPI pro web“ nedává smysl**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jedním z nejodolnějších grafických mýtů je tvrzení, že „obrázek na web musí mít 72 DPI“. Pro digitální zobrazení je to zavádějící.

**PPI — pixels per inch** vyjadřuje počet pixelů na jeden palec výsledné fyzické délky. Je důležitý například tehdy, když chceme určit, jak velký bude obrázek při tisku.

**DPI — dots per inch** označuje počet tiskových bodů, které dokáže tiskové zařízení umístit na palec. Tiskárna může pro reprodukci jednoho obrazového pixelu použít několik tiskových bodů různých barev. DPI tiskárny tedy není totéž co PPI obrázku.

Na běžném webu rozhodují především **pixelové rozměry obrázku a způsob jeho zobrazení v CSS**. Metadata „72 PPI“ nebo „300 PPI“ sama o sobě nezmění počet pixelů, které má prohlížeč k dispozici.

Soubor `1200 × 800 px` je pro web stále `1200 × 800 px`, ať v metadatech uvedeme 72 PPI, 96 PPI nebo 300 PPI.

PPI začne být zásadní při převodu do fyzické velikosti.

Máme například obraz široký 3000 pixelů. Při tisku na 300 PPI bude jeho šířka:

`3000 / 300 = 10 palců`

tedy přibližně 25,4 cm.

Při 150 PPI by byl stejně velký soubor vytištěn na dvojnásobnou fyzickou šířku, ale s menší hustotou obrazových vzorků.

Ani známých 300 PPI však není univerzální magická hranice. Vhodná hodnota závisí na tiskové technologii, pozorovací vzdálenosti, typu obrazu a požadované kvalitě. Velkoplošný plakát sledovaný z několika metrů nepotřebuje stejnou PPI jako kvalitní fotografie držená v ruce.

**Hlavní myšlenka:** pro obrazovku uvažujeme hlavně o pixelech; pro tisk musíme propojit pixelové rozměry s fyzickou velikostí. DPI je vlastnost tiskového zařízení, PPI vlastnost pixelové hustoty obrazu nebo displeje.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Barevná hloubka: kolik hodnot může pixel mít?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Pixel nemusí být pouze „barevný bod“. Aby počítač věděl, jakou barvu zobrazit, musí být tato barva popsána čísly.

U běžného obrazu RGB se často používá **8 bitů na jeden barevný kanál**. Máme tři kanály:

- R — red,
- G — green,
- B — blue.

Každý kanál může mít `2^8 = 256` hodnot, typicky 0 až 255.

Celkový počet možných kombinací je:

`256 × 256 × 256 = 16 777 216`

Proto se běžnému osmibitovému RGB obrazu říká také **24bitová barva** — tři kanály po osmi bitech.

Pokud přidáme osmibitový alfa kanál pro průhlednost, může jeden pixel používat 32 bitů:

`8 + 8 + 8 + 8`

Je však důležité uvědomit si, že pojem „32bitový obraz“ může v různých programech znamenat něco jiného. Profesionální grafika například používá 16 nebo 32 bitů **na kanál**, často v plovoucí řádové reprezentaci. Proto musíme vždy sledovat konkrétní kontext.

Vyšší bitová hloubka je významná při úpravách. Osmibitový kanál má 256 úrovní. Šestnáctibitové zpracování poskytuje mnohem jemnější odstupňování, takže při výrazných korekcích jasu a barev vzniká menší riziko viditelných přechodových pásů — **bandingu**.

To neznamená, že monitor musí dokázat zobrazit všechny interní hodnoty. Vyšší bitová hloubka může sloužit jako rezerva během výpočtů a editace.

**Příklad.** Když velmi zesvětlíme tmavou část osmibitové fotografie, začneme roztahovat malý počet původních tónových úrovní přes velký rozsah. V šestnáctibitovém pracovním obrazu máme pro úpravy výrazně více mezistupňů.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Alfa kanál a průhlednost**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

RGB popisuje barevnou složku pixelu. Pro skládání více obrazů však často potřebujeme vědět také, **nakolik má být daný pixel viditelný**.

K tomu slouží **alfa kanál**.

Hodnota alfa může například říkat:

- 0 % — úplně průhledný pixel,
- 50 % — částečně průhledný,
- 100 % — zcela neprůhledný.

Průhlednost je zásadní pro ikony, vrstvenou grafiku, kompozice, stíny, uživatelská rozhraní a maskování.

Je vhodné rozlišit **průhlednost a barvu**. Pixel může mít uložené RGB hodnoty i tehdy, když je jeho alfa nulová a při běžném zobrazení není vidět.

Při skládání vrstev pak grafický systém vypočítává výslednou barvu podle barev horní a spodní vrstvy a hodnoty alfa.

Existují také dvě běžné technické reprezentace: **straight alpha** a **premultiplied alpha**. Pro základní výuku není nutné počítat jejich vzorce, ale vysvětlují, proč se při špatném exportu nebo kombinaci nástrojů někdy kolem průhledných objektů objeví tmavé nebo světlé okraje.

Ne každý obrazový formát průhlednost podporuje. JPEG běžný alfa kanál nemá, zatímco PNG, WebP nebo AVIF mohou průhlednost uchovávat.

**Hlavní myšlenka první lekce:** rastrový obraz je diskrétní vzorek vizuální informace. K jeho správnému popisu nestačí vědět jen „kolik má megapixelů“. Důležitá je také bitová hloubka, barevná reprezentace, případná průhlednost a způsob, jakým obraz převádíme na fyzickou velikost.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Nižší a vyšší programovací jazyky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Programovací jazyky lze rozdělit podle úrovně abstrakce na nižší a vyšší. Nižší programovací jazyky jsou velmi blízké hardwaru a umožňují přímou kontrolu nad chodem počítače. V současnosti se používají méně často, ale stále jsou důležité pro specifické úlohy, jako je vývoj operačních systémů, ovladačů nebo vestavěných systémů. Typické vlastnosti:

- silná vazba na konkrétní procesor nebo architekturu,
- vysoký výkon a efektivita,
- složitější zápis a horší čitelnost kódu. Příklady nižších jazyků:
- strojový jazyk – přímý binární kód vykonávaný procesorem,
- assembler – jazyk blízký strojovému kódu, jedna instrukce odpovídá jedné strojové instrukci, ale oproti strojovému kódu používá symbolické názvy pro instrukce a adresy. Ukázka assemblerového kódu (pro x86 architekturu):
```
MOV AX , 5          ; Nacti hodnotu 5 do registru AX
ADD AX , 10         ; Pricti hodnotu 10 k registru AX
MOV BX , AX         ; Presun hodnotu z registru AX do registru BX
```

Vyšší programovací jazyky. Instrukce v těchto jazycích jsou blíže přirozenému jazyku (například angličtině), což usnadňuje jejich pochopení a použití. Umožňují psát kód, který je srozumitelnější a snadněji udržovatelný, protože abstrahují detaily hardwaru a v jedné instrukci mohou zahrnovat více operací. Typické vlastnosti:

- lepší čitelnost a srozumitelnost kódu,
- vyšší produktivita při vývoji,
- větší přenositelnost programů mezi platformami. Příklady vyšších jazyků:
- C, C++,
- Java,
- Python,
- JavaScript. Rozdělení na nižší a vyšší jazyky není zcela striktní. Některé jazyky (např. C nebo
C++) stojí na pomezí obou kategorií – umožňují práci blízkou hardwaru, ale zároveň poskytují prvky vyšší úrovně.

## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Co je rastrová grafika?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Rastrový obraz je tvořen **pravidelnou mřížkou obrazových bodů — pixelů**. Každý pixel nese číselnou informaci o své barvě, případně také o průhlednosti. Když jsou pixely dostatečně malé a zobrazujeme obraz z běžné vzdálenosti, lidské oko je přestane vnímat jako samostatné čtverečky a spojí je do souvislé fotografie, kresby nebo textury.

Tento princip je velmi odlišný od vektorové grafiky. Vektorový obrázek popisuje objekty matematicky: například „nakresli kružnici s tímto středem a poloměrem“. Rastrový obrázek naproti tomu říká: „na této pozici je pixel s takovou barvou, vedle něj další pixel s jinou barvou“.

Proto se rastrová grafika výborně hodí tam, kde má obraz obsahovat velké množství jemných barevných a jasových změn — především u **digitální fotografie**, digitální malby, textur, naskenovaných dokumentů, obrazových efektů nebo výsledků renderingu.

Její hlavní omezení vychází ze stejného principu. Rastrový obraz má konečný počet vzorků. Když jej výrazně zvětšíme, původní pixely nestačí a program musí vytvořit nové hodnoty. Nemůže však objevit detail, který ve zdrojovém obrazu nikdy nebyl zachycen.

Klasické zvětšení proto vede k měkkému obrazu nebo k viditelné pixelizaci. Moderní algoritmy a AI super-resolution mohou chybějící strukturu **odhadovat**, ale to neznamená, že rekonstruují původní scénu s jistotou. Část detailů může být synteticky vytvořená.

Rastrový princip používají také obrazovky. Monitor má fyzickou mřížku obrazových prvků, ale jeden pixel obrázku nemusí vždy přesně odpovídat jednomu fyzickému pixelu displeje. Operační systém, prohlížeč nebo grafická aplikace může obraz škálovat podle hustoty displeje a nastaveného měřítka.

**Příklad z praxe.** Fotografie o rozměrech `4000 × 3000 px` obsahuje 12 milionů pixelů. To odpovídá 12 megapixelům. Pokud ji zobrazíme na monitoru 1920 × 1080, musí být zmenšena — monitor nemá dost fyzických pixelů, aby ukázal všechny obrazové vzorky současně v poměru 1 : 1.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rozměry obrazu, rozlišení a megapixely**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Slovo **rozlišení** se používá v několika významech a právě proto často vzniká zmatek.

U digitálního obrázku je nejpřesnější nejprve uvést jeho **pixelové rozměry**:

`šířka × výška`

Například:

`1920 × 1080 px`

Takový obraz obsahuje:

`1920 × 1080 = 2 073 600 pixelů`

tedy přibližně 2,07 megapixelu.

Fotografie `6000 × 4000 px` obsahuje 24 milionů pixelů, tedy přibližně 24 Mpx.

Počet megapixelů však sám o sobě neurčuje kvalitu fotografie. Dva fotoaparáty mohou mít stejný počet pixelů a přitom velmi odlišnou kvalitu výsledku kvůli rozdílné velikosti snímače, objektivu, šumu, dynamickému rozsahu, zpracování nebo kvalitě zaostření.

Stejně tak více pixelů není vždy prakticky přínosných. Pokud bude výsledná fotografie zobrazena pouze jako malý náhled na webu, extrémně vysoké rozlišení znamená hlavně větší datový objem a delší zpracování.

Rozlišení proto musíme vždy vztahovat k účelu:

- zobrazení na obrazovce,
- tisk,
- další ořez,
- archivace,
- strojové zpracování,
- publikace na webu.

Důležité je také rozlišit **ořez** a **změnu velikosti**. Ořez odstraní část obrazu a ponechá zbývající pixely beze změny. Zmenšení nebo zvětšení naproti tomu mění počet pixelů a vyžaduje přepočet obrazových dat.

**Příklad.** Máme fotografii `6000 × 4000 px` a vyřízneme prostřední čtvrtinu plochy. Výsledný obraz může mít zhruba `3000 × 2000 px`. Nezhoršili jsme kvalitu jednotlivých zbývajících pixelů, ale ztratili jsme část původního záběru a tím také část celkového rozlišení.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**PPI, DPI a proč „72 DPI pro web“ nedává smysl**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jedním z nejodolnějších grafických mýtů je tvrzení, že „obrázek na web musí mít 72 DPI“. Pro digitální zobrazení je to zavádějící.

**PPI — pixels per inch** vyjadřuje počet pixelů na jeden palec výsledné fyzické délky. Je důležitý například tehdy, když chceme určit, jak velký bude obrázek při tisku.

**DPI — dots per inch** označuje počet tiskových bodů, které dokáže tiskové zařízení umístit na palec. Tiskárna může pro reprodukci jednoho obrazového pixelu použít několik tiskových bodů různých barev. DPI tiskárny tedy není totéž co PPI obrázku.

Na běžném webu rozhodují především **pixelové rozměry obrázku a způsob jeho zobrazení v CSS**. Metadata „72 PPI“ nebo „300 PPI“ sama o sobě nezmění počet pixelů, které má prohlížeč k dispozici.

Soubor `1200 × 800 px` je pro web stále `1200 × 800 px`, ať v metadatech uvedeme 72 PPI, 96 PPI nebo 300 PPI.

PPI začne být zásadní při převodu do fyzické velikosti.

Máme například obraz široký 3000 pixelů. Při tisku na 300 PPI bude jeho šířka:

`3000 / 300 = 10 palců`

tedy přibližně 25,4 cm.

Při 150 PPI by byl stejně velký soubor vytištěn na dvojnásobnou fyzickou šířku, ale s menší hustotou obrazových vzorků.

Ani známých 300 PPI však není univerzální magická hranice. Vhodná hodnota závisí na tiskové technologii, pozorovací vzdálenosti, typu obrazu a požadované kvalitě. Velkoplošný plakát sledovaný z několika metrů nepotřebuje stejnou PPI jako kvalitní fotografie držená v ruce.

**Hlavní myšlenka:** pro obrazovku uvažujeme hlavně o pixelech; pro tisk musíme propojit pixelové rozměry s fyzickou velikostí. DPI je vlastnost tiskového zařízení, PPI vlastnost pixelové hustoty obrazu nebo displeje.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Barevná hloubka: kolik hodnot může pixel mít?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Pixel nemusí být pouze „barevný bod“. Aby počítač věděl, jakou barvu zobrazit, musí být tato barva popsána čísly.

U běžného obrazu RGB se často používá **8 bitů na jeden barevný kanál**. Máme tři kanály:

- R — red,
- G — green,
- B — blue.

Každý kanál může mít `2^8 = 256` hodnot, typicky 0 až 255.

Celkový počet možných kombinací je:

`256 × 256 × 256 = 16 777 216`

Proto se běžnému osmibitovému RGB obrazu říká také **24bitová barva** — tři kanály po osmi bitech.

Pokud přidáme osmibitový alfa kanál pro průhlednost, může jeden pixel používat 32 bitů:

`8 + 8 + 8 + 8`

Je však důležité uvědomit si, že pojem „32bitový obraz“ může v různých programech znamenat něco jiného. Profesionální grafika například používá 16 nebo 32 bitů **na kanál**, často v plovoucí řádové reprezentaci. Proto musíme vždy sledovat konkrétní kontext.

Vyšší bitová hloubka je významná při úpravách. Osmibitový kanál má 256 úrovní. Šestnáctibitové zpracování poskytuje mnohem jemnější odstupňování, takže při výrazných korekcích jasu a barev vzniká menší riziko viditelných přechodových pásů — **bandingu**.

To neznamená, že monitor musí dokázat zobrazit všechny interní hodnoty. Vyšší bitová hloubka může sloužit jako rezerva během výpočtů a editace.

**Příklad.** Když velmi zesvětlíme tmavou část osmibitové fotografie, začneme roztahovat malý počet původních tónových úrovní přes velký rozsah. V šestnáctibitovém pracovním obrazu máme pro úpravy výrazně více mezistupňů.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Alfa kanál a průhlednost**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

RGB popisuje barevnou složku pixelu. Pro skládání více obrazů však často potřebujeme vědět také, **nakolik má být daný pixel viditelný**.

K tomu slouží **alfa kanál**.

Hodnota alfa může například říkat:

- 0 % — úplně průhledný pixel,
- 50 % — částečně průhledný,
- 100 % — zcela neprůhledný.

Průhlednost je zásadní pro ikony, vrstvenou grafiku, kompozice, stíny, uživatelská rozhraní a maskování.

Je vhodné rozlišit **průhlednost a barvu**. Pixel může mít uložené RGB hodnoty i tehdy, když je jeho alfa nulová a při běžném zobrazení není vidět.

Při skládání vrstev pak grafický systém vypočítává výslednou barvu podle barev horní a spodní vrstvy a hodnoty alfa.

Existují také dvě běžné technické reprezentace: **straight alpha** a **premultiplied alpha**. Pro základní výuku není nutné počítat jejich vzorce, ale vysvětlují, proč se při špatném exportu nebo kombinaci nástrojů někdy kolem průhledných objektů objeví tmavé nebo světlé okraje.

Ne každý obrazový formát průhlednost podporuje. JPEG běžný alfa kanál nemá, zatímco PNG, WebP nebo AVIF mohou průhlednost uchovávat.

**Hlavní myšlenka první lekce:** rastrový obraz je diskrétní vzorek vizuální informace. K jeho správnému popisu nestačí vědět jen „kolik má megapixelů“. Důležitá je také bitová hloubka, barevná reprezentace, případná průhlednost a způsob, jakým obraz převádíme na fyzickou velikost.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Typy moderních programovacích jazyků**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Moderní programovací jazyky lze rozdělit podle různých hledisek. Jedním z nejpoužívanějších je rozdělení podle oblasti použití, dalším kritériem může být paradigma programování (procedurální, objektově orientované, funkcionální, logické), použitá syntaktická struktura (blokové jazyky, značkovací jazyky), případně úroveň abstrakce (nízkoúrovňové vs. vysokoúrovňové jazyky).

- Programovací jazyky pro webový vývoj – JavaScript – klientská i serverová část webu, – PHP – serverové webové aplikace, – Python – backend, webové frameworky.
- Programovací jazyky pro aplikační a systémový vývoj – C, C++ – systémový software, ovladače, herní enginy, – Java, C# – desktopové a podnikové aplikace, – Rust – systémové programování s důrazem na bezpečnost.
- Programovací jazyky pro mobilní aplikace – Swift – aplikace pro iOS, – Kotlin – aplikace pro Android.
- Programovací jazyky pro vědecké výpočty a práci s daty – Python – analýza dat, umělá inteligence, – R – statistika a datová analýza.
- Speciální a doménově orientované jazyky – SQL – práce s databázemi, – Bash – skriptování v operačních systémech. Výběr programovacího jazyka závisí na konkrétním účelu použití, požadavcích na výkon, přenositelnost, bezpečnost a také na zkušenostech vývojáře nebo vývojového týmu.

## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Co je rastrová grafika?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Rastrový obraz je tvořen **pravidelnou mřížkou obrazových bodů — pixelů**. Každý pixel nese číselnou informaci o své barvě, případně také o průhlednosti. Když jsou pixely dostatečně malé a zobrazujeme obraz z běžné vzdálenosti, lidské oko je přestane vnímat jako samostatné čtverečky a spojí je do souvislé fotografie, kresby nebo textury.

Tento princip je velmi odlišný od vektorové grafiky. Vektorový obrázek popisuje objekty matematicky: například „nakresli kružnici s tímto středem a poloměrem“. Rastrový obrázek naproti tomu říká: „na této pozici je pixel s takovou barvou, vedle něj další pixel s jinou barvou“.

Proto se rastrová grafika výborně hodí tam, kde má obraz obsahovat velké množství jemných barevných a jasových změn — především u **digitální fotografie**, digitální malby, textur, naskenovaných dokumentů, obrazových efektů nebo výsledků renderingu.

Její hlavní omezení vychází ze stejného principu. Rastrový obraz má konečný počet vzorků. Když jej výrazně zvětšíme, původní pixely nestačí a program musí vytvořit nové hodnoty. Nemůže však objevit detail, který ve zdrojovém obrazu nikdy nebyl zachycen.

Klasické zvětšení proto vede k měkkému obrazu nebo k viditelné pixelizaci. Moderní algoritmy a AI super-resolution mohou chybějící strukturu **odhadovat**, ale to neznamená, že rekonstruují původní scénu s jistotou. Část detailů může být synteticky vytvořená.

Rastrový princip používají také obrazovky. Monitor má fyzickou mřížku obrazových prvků, ale jeden pixel obrázku nemusí vždy přesně odpovídat jednomu fyzickému pixelu displeje. Operační systém, prohlížeč nebo grafická aplikace může obraz škálovat podle hustoty displeje a nastaveného měřítka.

**Příklad z praxe.** Fotografie o rozměrech `4000 × 3000 px` obsahuje 12 milionů pixelů. To odpovídá 12 megapixelům. Pokud ji zobrazíme na monitoru 1920 × 1080, musí být zmenšena — monitor nemá dost fyzických pixelů, aby ukázal všechny obrazové vzorky současně v poměru 1 : 1.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rozměry obrazu, rozlišení a megapixely**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Slovo **rozlišení** se používá v několika významech a právě proto často vzniká zmatek.

U digitálního obrázku je nejpřesnější nejprve uvést jeho **pixelové rozměry**:

`šířka × výška`

Například:

`1920 × 1080 px`

Takový obraz obsahuje:

`1920 × 1080 = 2 073 600 pixelů`

tedy přibližně 2,07 megapixelu.

Fotografie `6000 × 4000 px` obsahuje 24 milionů pixelů, tedy přibližně 24 Mpx.

Počet megapixelů však sám o sobě neurčuje kvalitu fotografie. Dva fotoaparáty mohou mít stejný počet pixelů a přitom velmi odlišnou kvalitu výsledku kvůli rozdílné velikosti snímače, objektivu, šumu, dynamickému rozsahu, zpracování nebo kvalitě zaostření.

Stejně tak více pixelů není vždy prakticky přínosných. Pokud bude výsledná fotografie zobrazena pouze jako malý náhled na webu, extrémně vysoké rozlišení znamená hlavně větší datový objem a delší zpracování.

Rozlišení proto musíme vždy vztahovat k účelu:

- zobrazení na obrazovce,
- tisk,
- další ořez,
- archivace,
- strojové zpracování,
- publikace na webu.

Důležité je také rozlišit **ořez** a **změnu velikosti**. Ořez odstraní část obrazu a ponechá zbývající pixely beze změny. Zmenšení nebo zvětšení naproti tomu mění počet pixelů a vyžaduje přepočet obrazových dat.

**Příklad.** Máme fotografii `6000 × 4000 px` a vyřízneme prostřední čtvrtinu plochy. Výsledný obraz může mít zhruba `3000 × 2000 px`. Nezhoršili jsme kvalitu jednotlivých zbývajících pixelů, ale ztratili jsme část původního záběru a tím také část celkového rozlišení.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**PPI, DPI a proč „72 DPI pro web“ nedává smysl**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jedním z nejodolnějších grafických mýtů je tvrzení, že „obrázek na web musí mít 72 DPI“. Pro digitální zobrazení je to zavádějící.

**PPI — pixels per inch** vyjadřuje počet pixelů na jeden palec výsledné fyzické délky. Je důležitý například tehdy, když chceme určit, jak velký bude obrázek při tisku.

**DPI — dots per inch** označuje počet tiskových bodů, které dokáže tiskové zařízení umístit na palec. Tiskárna může pro reprodukci jednoho obrazového pixelu použít několik tiskových bodů různých barev. DPI tiskárny tedy není totéž co PPI obrázku.

Na běžném webu rozhodují především **pixelové rozměry obrázku a způsob jeho zobrazení v CSS**. Metadata „72 PPI“ nebo „300 PPI“ sama o sobě nezmění počet pixelů, které má prohlížeč k dispozici.

Soubor `1200 × 800 px` je pro web stále `1200 × 800 px`, ať v metadatech uvedeme 72 PPI, 96 PPI nebo 300 PPI.

PPI začne být zásadní při převodu do fyzické velikosti.

Máme například obraz široký 3000 pixelů. Při tisku na 300 PPI bude jeho šířka:

`3000 / 300 = 10 palců`

tedy přibližně 25,4 cm.

Při 150 PPI by byl stejně velký soubor vytištěn na dvojnásobnou fyzickou šířku, ale s menší hustotou obrazových vzorků.

Ani známých 300 PPI však není univerzální magická hranice. Vhodná hodnota závisí na tiskové technologii, pozorovací vzdálenosti, typu obrazu a požadované kvalitě. Velkoplošný plakát sledovaný z několika metrů nepotřebuje stejnou PPI jako kvalitní fotografie držená v ruce.

**Hlavní myšlenka:** pro obrazovku uvažujeme hlavně o pixelech; pro tisk musíme propojit pixelové rozměry s fyzickou velikostí. DPI je vlastnost tiskového zařízení, PPI vlastnost pixelové hustoty obrazu nebo displeje.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Barevná hloubka: kolik hodnot může pixel mít?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Pixel nemusí být pouze „barevný bod“. Aby počítač věděl, jakou barvu zobrazit, musí být tato barva popsána čísly.

U běžného obrazu RGB se často používá **8 bitů na jeden barevný kanál**. Máme tři kanály:

- R — red,
- G — green,
- B — blue.

Každý kanál může mít `2^8 = 256` hodnot, typicky 0 až 255.

Celkový počet možných kombinací je:

`256 × 256 × 256 = 16 777 216`

Proto se běžnému osmibitovému RGB obrazu říká také **24bitová barva** — tři kanály po osmi bitech.

Pokud přidáme osmibitový alfa kanál pro průhlednost, může jeden pixel používat 32 bitů:

`8 + 8 + 8 + 8`

Je však důležité uvědomit si, že pojem „32bitový obraz“ může v různých programech znamenat něco jiného. Profesionální grafika například používá 16 nebo 32 bitů **na kanál**, často v plovoucí řádové reprezentaci. Proto musíme vždy sledovat konkrétní kontext.

Vyšší bitová hloubka je významná při úpravách. Osmibitový kanál má 256 úrovní. Šestnáctibitové zpracování poskytuje mnohem jemnější odstupňování, takže při výrazných korekcích jasu a barev vzniká menší riziko viditelných přechodových pásů — **bandingu**.

To neznamená, že monitor musí dokázat zobrazit všechny interní hodnoty. Vyšší bitová hloubka může sloužit jako rezerva během výpočtů a editace.

**Příklad.** Když velmi zesvětlíme tmavou část osmibitové fotografie, začneme roztahovat malý počet původních tónových úrovní přes velký rozsah. V šestnáctibitovém pracovním obrazu máme pro úpravy výrazně více mezistupňů.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Alfa kanál a průhlednost**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

RGB popisuje barevnou složku pixelu. Pro skládání více obrazů však často potřebujeme vědět také, **nakolik má být daný pixel viditelný**.

K tomu slouží **alfa kanál**.

Hodnota alfa může například říkat:

- 0 % — úplně průhledný pixel,
- 50 % — částečně průhledný,
- 100 % — zcela neprůhledný.

Průhlednost je zásadní pro ikony, vrstvenou grafiku, kompozice, stíny, uživatelská rozhraní a maskování.

Je vhodné rozlišit **průhlednost a barvu**. Pixel může mít uložené RGB hodnoty i tehdy, když je jeho alfa nulová a při běžném zobrazení není vidět.

Při skládání vrstev pak grafický systém vypočítává výslednou barvu podle barev horní a spodní vrstvy a hodnoty alfa.

Existují také dvě běžné technické reprezentace: **straight alpha** a **premultiplied alpha**. Pro základní výuku není nutné počítat jejich vzorce, ale vysvětlují, proč se při špatném exportu nebo kombinaci nástrojů někdy kolem průhledných objektů objeví tmavé nebo světlé okraje.

Ne každý obrazový formát průhlednost podporuje. JPEG běžný alfa kanál nemá, zatímco PNG, WebP nebo AVIF mohou průhlednost uchovávat.

**Hlavní myšlenka první lekce:** rastrový obraz je diskrétní vzorek vizuální informace. K jeho správnému popisu nestačí vědět jen „kolik má megapixelů“. Důležitá je také bitová hloubka, barevná reprezentace, případná průhlednost a způsob, jakým obraz převádíme na fyzickou velikost.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
