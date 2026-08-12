## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Strukturované datové typy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Skalární datové typy reprezentují jednotlivé hodnoty, například celá čísla (int), desetinná čísla (float) nebo znaky (char). Každá proměnná skalárního typu obsahuje právě jednu hodnotu.

Pojem ”skalární”pochází z matematiky a znamená ”jednoduchý”nebo ”nekompozitní”. Skalární datové typy jsou základními stavebními kameny pro vytváření složitějších datových struktur. Věk je skalární datový typ, protože představuje jednu hodnotu (například 25). Teplota je skalární datový typ, protože představuje jednu hodnotu (například 36.5 °C).

Opakem skalárních datových typů jsou strukturované datové typy, které mohou obsahovat více hodnot uspořádaných podle určitého pravidla. Strukturované datové typy umožňují ukládat více hodnot uspořádaných podle určitého pravidla. Strukturované typy poskytují způsob organizace dat do logických celků, což zjednodušuje práci se složitějšími datovými strukturami.

Příklady z reálného světa: Osoba může být strukturovaný datový typ, který obsahuje atributy jako jmeno , vek , mesto . Každý atribut představuje jednu vlastnost osoby, a všechny tyto vlastnosti dohromady tvoří komplexní datovou strukturu.

Základní typy strukturovaných dat zahrnují:

- pole – uspořádaná kolekce prvků stejného typu,
- záznamy (struktury) – kolekce prvků různých typů,
- seznamy – dynamické kolekce prvků,
- slovníky – kolekce párů klíč-hodnota.

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

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Pole jako základní datová struktura**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Pole je základní strukturovaný datový typ, který uchovává pevný počet prvků stejného typu uspořádaných v posloupnosti. Každý prvek pole je přístupný pomocí indexu, což je číselná pozice prvku v poli. Vlastnosti pole:

- všechny prvky mají stejný datový typ,
- prvky jsou uloženy v paměti za sebou,
- přístup k prvkům je rychlý díky indexování,
- velikost pole je obvykle stanovena při vytvoření. Indexování v poli:
- v jazycích C a C++ se indexuje od nuly,
- první prvek má index 0 , druhý index 1 atd.
- přístup k prvku se provádí pomocí hranatých závorek, například pole[0] pro první prvek.
> **Poznámka**
>
> V Pythonu tradiční pole nahrazují seznamy ( list ), které jsou dynamické a mohou obsahovat prvky různých typů, ale základní princip indexování zůstává stejný. Pole v Pythonu lze simulovat pomocí modulu array , který poskytuje efektivní pole pro základní datové typy.

Příklad v Pythonu s modulem array :

```
import array
# Vytvoreni pole celych cisel
cisla = array . array ('i', [10 , 20, 30, 40, 50])
print (cisla [0]) # Vystup : 10
```

Schematické znázornění pole:

Index: 0 1 2 3 4 Hodnota: [10] [20] [30] [40] [50] ^

```text
|
```

adresa v paměti

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

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Statické pole**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Statické pole má velikost pevně stanovenou při deklaraci a nelze ji během běhu programu změnit. Paměť pro statické pole je alokována při vytvoření proměnné. Příklad v jazyce C:

```
int cisla [5]; // Pole s 5 prvky typu int
cisla [0] = 10;
cisla [1] = 20;
cisla [2] = 30;
```

## 6. // Inicializace pri deklaraci

## 7. int hodnoty [5] = {10 , 20, 30, 40, 50};

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

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Dynamické pole**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Dynamické pole umožňuje měnit svou velikost během běhu programu. Paměť se alokuje dynamicky podle potřeby, což poskytuje větší flexibilitu při práci s daty neznámého rozsahu. V jazyce C se dynamická alokace provádí pomocí funkcí malloc a free :

## 1. # include <stdlib .h>

```
int *pole;
int velikost = 5;
```

## 6. // Dynamicka alokace pameti

## 7. pole = (int *) malloc ( velikost * sizeof (int));

## 9. // Pouziti pole

```
pole [0] = 10;
pole [1] = 20;
```

## 13. // Uvolneni pameti

## 14. free(pole);

V Pythonu jsou seznamy (list) dynamické automaticky:

```
cisla = [] # Prazdny seznam
cisla. append (10) # Pridani prvku
cisla. append (20)
cisla. append (30)
```

## 6. # Seznam automaticky roste podle potreby

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

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Ukazatele a pole**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Ukazatel je proměnná, která uchovává adresu v paměti, kde je uložena jiná hodnota. Ukazatele jsou klíčové při práci s dynamickými datovými strukturami. V jazyce C existuje úzký vztah mezi poli a ukazateli:

```
int pole [5] = {10 , 20, 30, 40, 50};
int * ukazatel = pole; // Ukazatel na prvni prvek
```

## 4. // Pristup pomoci ukazatele

```
printf ("%d\n", * ukazatel );     // Vystup : 10
printf ("%d\n", *( ukazatel + 1)); // Vystup : 20
```

Název pole v jazyce C funguje jako ukazatel na jeho první prvek. To umožňuje efektivní práci s pamětí, ale vyžaduje opatrnost při manipulaci.

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

## Snímek 1.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Matice (vícerozměrná pole)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Matice je vícerozměrné pole, nejčastěji dvourozměrné, které lze chápat jako tabulku hodnot s řádky a sloupci. Příklad v jazyce C:

## 1. int matice [3][4];       // Matice 3 radky x 4 sloupce

## 3. // Inicializace

```
int cisla [2][3] = {
{1, 2, 3},
{4, 5, 6}
};
```

## 9. // Pristup k prvkum

```
cisla [0][0] = 10; // Prvni radek , prvni sloupec
cisla [1][2] = 60; // Druhy radek , treti sloupec
```

Příklad v Pythonu:

```
# Vnorene seznamy jako matice
matice = [
[1, 2, 3],
[4, 5, 6]
]
```

```
# Pristup k prvkum
matice [0][0] = 10 # Prvni radek , prvni sloupec
matice [1][2] = 60 # Druhy radek , treti sloupec
```

Schematické znázornění matice:

sloupec 0 sloupec 1 sloupec 2 řádek 0 [1] [2] [3] řádek 1 [4] [5] [6]

Matice se používají v mnoha oblastech, například při reprezentaci obrazu, řešení soustav rovnic, grafice nebo zpracování tabulkových dat.

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
