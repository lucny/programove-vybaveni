## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Význam strukturovaných datových formátů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při ukládání a přenosu dat mezi programy nebo systémy je důležité používat standardizované formáty, které zajistí:

- přenositelnost – data lze sdílet mezi různými programy a platformami,
- čitelnost – strukturovaná data jsou srozumitelnější,
- parsovatelnost – programy mohou data snadno načíst a zpracovat,
- interoperabilitu – různé systémy mohou spolupracovat.

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

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**CSV (Comma-Separated Values)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


CSV je jednoduchý textový formát pro ukládání tabulkových dat. Každý řádek souboru odpovídá jednomu záznamu a hodnoty jsou odděleny čárkami (nebo jinými oddělovači). Příklad CSV souboru:

jmeno,vek,mesto Alice,25,Praha Jan,30,Brno Ludmila,22,Ostrava

Vlastnosti CSV:

- jednoduchost – snadné vytvoření i ruční editace,
- kompaktnost – malá velikost souborů,
- široká podpora – většina nástrojů CSV podporuje,
- omezení – obtížné ukládání hierarchických nebo vnořených dat. Práce s CSV v Pythonu:
## 1. import csv

```
# Cteni CSV
with open("data.csv", "r", encoding ="utf -8") as soubor :
ctenar = csv. reader ( soubor )
hlavicka = next( ctenar ) # Prvni radek
for radek in ctenar :
print ( radek ) # [' Alice ', '25', 'Praha ']
```

```
# Zapis CSV
with open(" vystup .csv", "w", newline ="", encoding ="utf -8") as
```

soubor :

```
zapisovac = csv. writer ( soubor )
zapisovac . writerow ([" jmeno", "vek", "mesto "])
zapisovac . writerow ([" David", "28", "ňPlze"])
```

CSV se používá pro:

- export dat z tabulkových procesorů,
- výměnu dat mezi databázemi,
- statistické zpracování dat,
- logy a reporty.

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

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**XML (eXtensible Markup Language)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


XML je značkovací jazyk určený pro strukturované ukládání dat. Používá značky (tagy) pro definování hierarchie a struktury dat. Příklad XML souboru:

```
<?xml version ="1.0" encoding ="UTF -8"?>
<osoby >
<osoba >
<jmeno >Alice </ jmeno >
<vek >25 </vek >
<mesto >Praha </ mesto >
</osoba >
<osoba >
<jmeno >Jan </ jmeno >
<vek >30 </vek >
<mesto >Brno </ mesto >
</osoba >
</osoby >
```

Vlastnosti XML:

- hierarchická struktura – stromová organizace dat,
- samodokumentující – názvy tagů popisují obsah,
- rozšiřitelnost – možnost definovat vlastní tagy,
- validace – lze ověřit strukturu pomocí schémat,
- rozvláčnost – větší velikost souborů kvůli opakujícím se tagům. XML se používá pro:
- konfigurační soubory,
- výměnu dat mezi systémy (SOAP webové služby),
- reprezentaci dokumentů (Office Open XML),
- ukládání komplexních datových struktur.

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

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**JSON (JavaScript Object Notation)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


JSON je lehký textový formát pro výměnu dat založený na syntaxi JavaScriptu. Je čitelnější a kompaktnější než XML. Příklad JSON souboru:

```
{
"osoby ": [
{
" jmeno ": " Alice ",
"vek": 25,
" mesto ": " Praha "
},
{
" jmeno ": "Jan",
"vek": 30,
" mesto ": "Brno"
}
]
}
```

Vlastnosti JSON:

- jednoduchost – snadno čitelný i zapisovatelný,
- kompaktnost – menší velikost než XML,
- nativní podpora – přímo podporován v JavaScriptu,
- omezené datové typy – čísla, řetězce, objekty, pole, boolean, null. Práce s JSON v Pythonu:
## 1. import json

```
# Nacteni JSON
with open("data.json", "r", encoding ="utf -8") as soubor :
data = json.load( soubor )
print (data["osoby "][0][ "jmeno "]) # Alice
```

```
# Zapis JSON
data = {
"osoby ": [
{"jmeno ": " Ludmila ", "vek": 22, "mesto ": " Ostrava "}
]
}
with open(" vystup .json", "w", encoding ="utf -8") as soubor :
json.dump(data , soubor , indent =2, ensure_ascii = False )
```

JSON se používá pro:

- RESTful API komunikaci,
- konfigurační soubory,
- ukládání strukturovaných dat,
- výměnu dat mezi webovými aplikacemi.

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

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**YAML (YAML Ain’t Markup Language)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


YAML je lidsky čitelný formát pro serializaci dat. Klade důraz na jednoduchost a čitelnost, používá odsazení místo složených závorek. Příklad YAML souboru:

osoby: - jmeno: Alice vek: 25 mesto: Praha - jmeno: Jan vek: 30 mesto: Brno

Vlastnosti YAML:

- čitelnost – velmi přehledný pro člověka,
- minimalistický – méně syntaktických značek,
- podpora komentářů – označeny # ,
- citlivost na odsazení – struktura je určena odsazením. YAML se používá pro:
- konfigurační soubory (Docker, Kubernetes),
- definice CI/CD pipeline,
- nastavení aplikací,
- dokumentaci struktury dat.

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

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Srovnání formátů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Formát Čitelnost Velikost Složitost Typické využití CSV Vysoká Malá Nízká Tabulková data XML Střední Velká Vysoká Dokumenty, komplexní struktury JSON Vysoká Střední Střední Web API, konfigurace YAML Velmi vysoká Střední Střední Konfigurace, DevOps

Volba formátu závisí na konkrétních požadavcích projektu:

- CSV pro jednoduché tabulkové exporty,
- JSON pro moderní webové API,
- XML pro komplexní dokumenty a legacy systémy,
- YAML pro čitelné konfigurační soubory.

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
