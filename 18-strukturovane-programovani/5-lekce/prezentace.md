## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Modularita a její přínosy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


S růstem velikosti a složitosti programů se stává nezbytné rozdělit kód do více samostatných částí. Modularita je princip členění programu na menší, logicky související celky nazývané moduly. Modularita přináší několik zásadních výhod:

- Lepší organizace – kód je strukturovaný podle funkčnosti.
- Znovupoužitelnost – moduly lze používat v různých projektech.
- Týmová spolupráce – různí vývojáři mohou pracovat na různých modulech současně.
- Snadnější údržba – změny v jednom modulu neovlivňují ostatní.
- Testování – jednotlivé moduly lze testovat nezávisle.

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
**Programové knihovny**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Knihovna je kolekce předpřipravených funkcí, tříd a dalších programových konstrukcí, které řeší běžné úlohy. Knihovny umožňují programátorům využívat již napsaný a otestovaný kód místo opětovného vymýšlení a implementace základních funkcionalit. Rozlišujeme: Standardní knihovny – dodávány společně s programovacím jazykem a poskytují základní funkcionalitu, například:

- práce s řetězci,
- matematické funkce,
- vstup a výstup,
- práce se soubory. Externí knihovny – vytvářené třetími stranami pro specifické účely, například:
- grafické knihovny,
- síťové knihovny,
- knihovny pro zpracování dat. V jazyce Python se knihovny připojují pomocí příkazu import , v jazyce C pomocí
direktivy preprocesoru #include . Příklad použití standardní knihovny v jazyce C:

```
# include <stdio .h>
# include <math.h>
```

```
int main () {
double vysledek = sqrt (16.0) ;         // Odmocnina
```

```
printf ("%.1f\n", vysledek );       // Vystup : 4.0
return 0;
}
```

Příklad použití standardní knihovny v Pythonu:

## 1. import math

```
vysledek = math.sqrt (16) # Odmocnina
print ( vysledek ) # Vystup : 4.0
```

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
**Hlavičkové soubory v jazyce C**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Hlavičkový soubor (header file) je soubor s příponou .h , který obsahuje deklarace funkcí, datových typů, konstant a dalších konstruktů, které mají být sdíleny mezi různými částmi programu. Hlavičkové soubory plní dvě základní role:

- Rozhraní – definují, jaké funkce a datové struktury jsou dostupné,
- Deklarace – oddělují deklaraci funkcí od jejich implementace. Typická struktura programu v jazyce C:
hlavickovy_soubor.h - deklarace funkcí a typů zdrojovy_soubor.c - implementace funkcí hlavni_program.c - hlavní program využívající funkce

Standardní hlavičkové soubory jsou součástí standardní knihovny jazyka C a poskytují základní funkcionalitu:

- <stdio.h> – vstup a výstup (např. printf , scanf ),
- <math.h> – matematické funkce (např. sqrt , sin , cos ),
- <string.h> – práce s řetězci (např. strlen , strcpy ),
- <stdlib.h> – obecné funkce (např. malloc , free , rand ).
Standardní hlavičkové soubory se vkládají pomocí lomených závorek:

```
# include <stdio .h>
# include <math.h>
```

Uživatelské hlavičkové soubory jsou vytvářeny programátorem pro vlastní projekty. Umožňují rozdělit kód do logických celků a znovupoužití funkcí v různých částech programu. Uživatelské hlavičkové soubory se vkládají pomocí uvozovek:

## 1. # include " moje_funkce .h"

Příklad uživatelského hlavičkového souboru matematika.h :

```
# ifndef MATEMATIKA_H
# define MATEMATIKA_H
```

```
int secti (int a, int b);
int odecti (int a, int b);
```

## 7. #endif

Příklad implementace v souboru matematika.c :

## 1. # include " matematika .h"

```
int secti (int a, int b) {
return a + b;
}
```

```
int odecti (int a, int b) {
return a - b;
}
```

Použití v hlavním programu:

```
# include <stdio .h>
# include " matematika .h"
```

```
int main () {
int vysledek = secti (10 , 5);
printf ("Vý sledek : %d\n", vysledek );      // Vystup : 15
return 0;
}
```

Direktivy #ifndef , #define a #endif tvoří tzv. include guard (ochranu proti vícenásobnému zahrnutí), který zajišťuje, že hlavičkový soubor bude do programu vložen pouze jednou, i když je k němu odkazováno z více míst.

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
**Moduly v jazyce Python**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


V Pythonu se modularita realizuje pomocí modulů. Modul je jednoduše soubor s příponou .py obsahující definice funkcí, tříd a proměnných. Příklad modulu matematika.py :

```
def secti (a, b):
return a + b
```

```
def odecti (a, b):
return a - b
```

Použití modulu v jiném souboru:

## 1. import matematika

```
vysledek = matematika . secti (10 , 5)
print (f"Vý sledek : { vysledek }") # Vystup : 15
```

Alternativně lze importovat pouze konkrétní funkce:

## 1. from matematika import secti

```
vysledek = secti (10 , 5)
print (f"Vý sledek : { vysledek }")    # Vystup : 15
```

Modularita je klíčovým principem moderního programování a její správné využití výrazně zvyšuje kvalitu a udržovatelnost softwarových projektů.

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
