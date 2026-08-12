# Rastrová grafika a digitální fotografie

## Modernizovaný výukový text pro studenty informačních technologií

> Digitální obraz vypadá na monitoru samozřejmě: fotografie je ostrá, barvy působí přirozeně a při přiblížení vidíme stále další detaily. Ve skutečnosti je však každý takový obraz výsledkem dlouhého řetězce rozhodnutí. Kolik pixelů použijeme? Jak přesně zapíšeme jejich barvy? Jaký barevný prostor zvolíme? Co udělá fotoaparát se světlem dopadajícím na snímač? A co se stane s obrazem při úpravě, kompresi, tisku nebo generativním zásahu AI?

Tento text modernizuje původní výukový materiál **Rastrová grafika a digitální fotografie**. Zachovává jeho základní tematickou osu — princip rastrového obrazu, obrazové formáty, barvy, nástroje rastrových editorů a digitální fotografii — ale rozděluje ji do šesti ucelených lekcí a na řadě míst zpřesňuje terminologii. Doplňuje také témata, která jsou pro současnou praxi zásadní: rozdíl mezi PPI a DPI, resampling, moderní formáty WebP a AVIF, barevné prostory a ICC profily, histogram, nedestruktivní workflow, computational photography, skutečný význam ISO, RAW workflow, export pro web a tisk i nové nástroje založené na umělé inteligenci.

Text je psán jako souvislý výklad, nikoli jako seznam hesel. Jednotlivé podkapitoly používají konkrétní příklady, srovnání a názorné analogie, aby byly vhodné nejen pro samostatné studium, ale později také jako podklad pro komentované prezentace a krátké podcastové minipořady.

---

# 1. Rastrový obraz: svět složený z pixelů

## 1.1 Co je rastrová grafika?

Rastrový obraz je tvořen **pravidelnou mřížkou obrazových bodů — pixelů**. Každý pixel nese číselnou informaci o své barvě, případně také o průhlednosti. Když jsou pixely dostatečně malé a zobrazujeme obraz z běžné vzdálenosti, lidské oko je přestane vnímat jako samostatné čtverečky a spojí je do souvislé fotografie, kresby nebo textury.

Tento princip je velmi odlišný od vektorové grafiky. Vektorový obrázek popisuje objekty matematicky: například „nakresli kružnici s tímto středem a poloměrem“. Rastrový obrázek naproti tomu říká: „na této pozici je pixel s takovou barvou, vedle něj další pixel s jinou barvou“.

Proto se rastrová grafika výborně hodí tam, kde má obraz obsahovat velké množství jemných barevných a jasových změn — především u **digitální fotografie**, digitální malby, textur, naskenovaných dokumentů, obrazových efektů nebo výsledků renderingu.

Její hlavní omezení vychází ze stejného principu. Rastrový obraz má konečný počet vzorků. Když jej výrazně zvětšíme, původní pixely nestačí a program musí vytvořit nové hodnoty. Nemůže však objevit detail, který ve zdrojovém obrazu nikdy nebyl zachycen.

Klasické zvětšení proto vede k měkkému obrazu nebo k viditelné pixelizaci. Moderní algoritmy a AI super-resolution mohou chybějící strukturu **odhadovat**, ale to neznamená, že rekonstruují původní scénu s jistotou. Část detailů může být synteticky vytvořená.

Rastrový princip používají také obrazovky. Monitor má fyzickou mřížku obrazových prvků, ale jeden pixel obrázku nemusí vždy přesně odpovídat jednomu fyzickému pixelu displeje. Operační systém, prohlížeč nebo grafická aplikace může obraz škálovat podle hustoty displeje a nastaveného měřítka.

**Příklad z praxe.** Fotografie o rozměrech `4000 × 3000 px` obsahuje 12 milionů pixelů. To odpovídá 12 megapixelům. Pokud ji zobrazíme na monitoru 1920 × 1080, musí být zmenšena — monitor nemá dost fyzických pixelů, aby ukázal všechny obrazové vzorky současně v poměru 1 : 1.

---

## 1.2 Rozměry obrazu, rozlišení a megapixely

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

---

## 1.3 PPI, DPI a proč „72 DPI pro web“ nedává smysl

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

---

## 1.4 Barevná hloubka: kolik hodnot může pixel mít?

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

---

## 1.5 Alfa kanál a průhlednost

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

---

# 2. Obrazové formáty, velikost a komprese

## 2.1 Co vlastně znamená obrazový formát?

Dva soubory mohou zobrazovat stejnou fotografii, ale uvnitř být strukturovány úplně jinak. Jeden může používat JPEG, druhý PNG a třetí AVIF. Rozdíl není jen v příponě.

**Obrazový formát** definuje, jak jsou pixelová data, metadata a další informace v souboru uspořádány a případně komprimovány.

Formát může rozhodovat například o tom:

- zda je komprese ztrátová nebo bezeztrátová,
- zda lze uložit alfa kanál,
- jaká bitová hloubka je podporována,
- zda lze ukládat metadata,
- zda formát podporuje animaci,
- zda umí pracovat s více vrstvami nebo stránkami.

Je také užitečné odlišit **formát pro výměnu výsledného obrazu** a **pracovní formát editoru**.

JPEG je typický distribuční formát fotografie. PSD nebo XCF naproti tomu mohou uchovávat vrstvy, masky a další stav rozpracovaného dokumentu. Takový soubor není jen „obrázek“, ale projekt.

Některé formáty jsou velmi jednoduché, jiné fungují jako kontejnery a mohou podporovat několik způsobů komprese.

Proto nelze spolehlivě rozdělit formáty na dvě jednoduché skupiny „tento je vždy bezeztrátový, tento vždy ztrátový“. TIFF například může používat různé kompresní metody. WebP a AVIF mají ztrátové i bezeztrátové režimy.

Při výběru formátu se proto ptáme:

**Co je důležitější — maximální kvalita, malá velikost, editovatelnost, průhlednost, kompatibilita nebo rychlost?**

---

## 2.2 JPEG: proč fotografie může být malá

JPEG patří k nejrozšířenějším formátům digitální fotografie. Jeho síla spočívá v tom, že dokáže obraz výrazně zmenšit za cenu řízené ztráty informace.

JPEG typicky využívá několik kroků. Obraz se transformuje do reprezentace, kde lze oddělit jasovou a barevnou informaci. Lidské vidění je citlivější na některé jasové detaily než na jemné barevné změny, takže lze barevná data často redukovat více.

Obraz se dále zpracovává po blocích a pomocí diskrétní kosinové transformace se prostorová informace převádí na frekvenční složky. Následuje kvantování, při kterém se méně významné hodnoty zjednoduší nebo odstraní.

Právě zde vzniká ztráta.

Při mírné kompresi může být vizuálně téměř nepostřehnutelná. Při silné kompresi se objeví typické artefakty:

- blokování,
- kroužkování kolem hran,
- ztráta jemných textur,
- barevné rozmazání.

JPEG je výborný pro fotografie, ale méně vhodný pro grafiku s velmi ostrými hranami, drobným textem nebo průhledností.

Důležitá je také zásada **opakovaného ukládání**. Když JPEG otevřeme, upravíme a znovu uložíme jako JPEG, proběhne další ztrátová komprese. Při mnoha cyklech se artefakty mohou kumulovat.

Proto je vhodné uchovávat kvalitní zdroj nebo pracovní soubor a JPEG vytvářet jako exportní verzi.

---

## 2.3 PNG, GIF, TIFF a pracovní formáty

**PNG** používá bezeztrátovou kompresi a velmi dobře se hodí pro snímky obrazovky, diagramy, grafiku s ostrými hranami a průhledné prvky.

U fotografie bývá PNG často výrazně větší než kvalitní JPEG nebo moderní ztrátové formáty, protože se snaží zachovat každý pixel přesně.

**GIF** používá paletu maximálně 256 barev na jeden snímek. Jeho hlavní dnešní význam souvisí s jednoduchými animacemi a historickou kompatibilitou. Pro moderní fotografii není efektivní.

GIF používá bezeztrátovou kompresi LZW, ale omezení palety může při převodu plnobarevného obrazu způsobit výraznou ztrátu barev. Označit jej pouze jako „bezeztrátový formát“ proto nevystihuje celý praktický problém.

**TIFF** je flexibilní formát používaný například v prepressu, archivaci a profesionálním obrazovém workflow. Může ukládat data s různou bitovou hloubkou a používat několik kompresních metod. Není tedy správné chápat TIFF jako jeden konkrétní typ „velkého nekomprimovaného obrázku“.

**BMP** je tradiční bitmapový formát spojený především s prostředím Windows. Často se používá bez účinné komprese, ale specifikace umožňuje více variant. Dnes se pro běžnou distribuci používá méně.

**PSD** je pracovní formát Adobe Photoshopu. Dokáže uchovávat vrstvy, masky, text, efekty a další editační informace. Jeho účelem není být univerzálním výsledným webovým formátem.

Podobnou roli má například XCF v GIMPu nebo interní dokumentové formáty dalších editorů.

**Praktické pravidlo:** pracovní soubor má uchovat maximum informací potřebných pro další úpravy; exportní soubor má být optimalizován pro konkrétní způsob použití.

---

## 2.4 WebP, AVIF a moderní webová grafika

Webové stránky musí řešit zvláštní kompromis. Obraz má být kvalitní, ale zároveň se musí rychle stáhnout přes mobilní síť a neměl by zbytečně zatěžovat server ani zařízení.

Moderní formáty proto hledají lepší poměr mezi kvalitou a velikostí.

**WebP** podporuje ztrátovou i bezeztrátovou kompresi, průhlednost a animaci. Díky široké podpoře je dnes běžnou volbou pro webovou grafiku a fotografie.

**AVIF** vychází z obrazové komprese související s video kodekem AV1. Dokáže při vhodném obsahu dosahovat velmi dobré kompresní účinnosti, podporuje průhlednost, HDR a vyšší bitové hloubky. Kódování ale může být výpočetně náročnější.

Starší **JPEG 2000** přinesl řadu zajímavých technických vlastností a může pracovat se ztrátovou i bezeztrátovou kompresí, ale na běžném webu nikdy nezískal tak univerzální podporu jako klasický JPEG.

Moderní web navíc neřeší jen formát. Používá **responsive images** a více velikostních variant. Prohlížeč může podle velikosti displeje a hustoty pixelů stáhnout vhodnější soubor.

Nemá smysl posílat mobilnímu telefonu fotografii širokou 6000 px, pokud bude zobrazena v boxu o šířce 400 CSS pixelů.

Optimalizace proto kombinuje:

- vhodné rozměry,
- vhodný formát,
- správnou kvalitu komprese,
- lazy loading,
- případně více variant obrazu.

**Hlavní myšlenka:** efektivní webový obraz není „JPEG na 72 DPI“. Je to správně zvolená kombinace pixelových rozměrů, formátu, komprese a způsobu doručení.

---

## 2.5 Velikost obrazových dat a jednoduchý výpočet

Nekomprimovaný rastrový obraz může být velmi velký.

Pro jednoduchý RGB obraz můžeme přibližně vypočítat datový objem:

**šířka × výška × počet kanálů × bitů na kanál**

Například obraz:

`4000 × 3000 px`

se třemi osmibitovými kanály RGB má:

`4000 × 3000 × 3 × 8 = 288 000 000 bitů`

tedy:

`36 000 000 bajtů`

přibližně 36 MB v desítkovém vyjádření, bez započtení hlaviček a dalších metadat.

Když přidáme alfa kanál, objem surových pixelových dat vzroste.

Pokud pracujeme se 16 bity na kanál, velikost se oproti osmibitovému obrazu při stejném počtu kanálů přibližně zdvojnásobí.

Skutečný soubor však může být díky kompresi mnohem menší. JPEG fotografie 4000 × 3000 px může mít několik megabajtů, podle obsahu a nastavené kvality.

Velikost ovlivňuje také charakter obrazu. Jednolitá grafika může být pro bezeztrátovou kompresi velmi snadná, zatímco obraz plný šumu a náhodných detailů se komprimuje hůře.

To vysvětluje, proč fotografický šum nezhoršuje jen vzhled snímku, ale často také zvyšuje výslednou velikost komprimovaného souboru — náhodný obraz se obtížněji předvídá.

---

## 2.6 Resampling: co se děje při změně rozměrů

Když měníme pixelové rozměry rastrového obrazu, musí editor přepočítat hodnoty pixelů. Tento proces se nazývá **resampling**.

Při zmenšování musí více původních pixelů přispět k menšímu počtu výsledných pixelů. Algoritmus rozhoduje, jak jejich hodnoty zkombinuje.

Při zvětšování naopak vznikají nové pixely, jejichž hodnoty je nutné odhadnout.

Klasické interpolační metody zahrnují například:

- nearest neighbour,
- bilinear,
- bicubic,
- Lanczos.

**Nearest neighbour** pouze kopíruje nejbližší hodnotu. Je vhodný pro pixel art, protože zachovává tvrdé hrany původních pixelů.

**Bilineární a bikubická interpolace** vytvářejí plynulejší přechody a hodí se pro běžnou fotografii.

Moderní editory nabízejí také AI zvětšování. Neuronová síť odhaduje pravděpodobné textury a detaily na základě naučených vzorů.

Je důležité správně interpretovat výsledek. AI může vytvořit obraz, který působí detailněji, ale nové jemné struktury nemusí být věrným záznamem původní reality.

Proto není vhodné používat generativní upscaling jako důkazní rekonstrukci detailu například ve forenzní nebo vědecké analýze bez jasného označení metody.

**Hlavní myšlenka druhé lekce:** formát a komprese určují, jak jsou obrazová data uložena; resampling mění samotnou mřížku pixelů. Tyto operace řeší odlišné problémy a mají odlišný dopad na kvalitu.

---

# 3. Barva: od lidského oka k číslům v počítači

## 3.1 Barva není vlastnost pixelu sama o sobě

Když řekneme, že objekt je „červený“, zní to jako jednoduchá fyzikální vlastnost. Ve skutečnosti je barva výsledkem interakce světla, materiálu, oka a mozku.

Viditelné světlo obsahuje různé vlnové délky. Povrch část světla absorbuje a část odráží. Do oka dopadá světelný signál, který zpracovává sítnice a následně nervový systém.

Lidské barevné vidění využívá především tři typy čípků označovaných **S, M a L** podle toho, na jaké oblasti spektra jsou nejcitlivější. Jejich citlivosti se výrazně překrývají.

Není proto úplně přesné říkat, že máme jednoduché „červené, zelené a modré čípky“. RGB je velmi užitečný technický model pro reprodukci barev, ale fyziologie oka je složitější.

Stejný fyzikální podnět může navíc vypadat různě podle okolí. Barvu ovlivňuje adaptace na osvětlení, kontrast se sousedními barvami i vlastnosti konkrétního pozorovatele.

Existují také různé typy poruch barevného vidění. Proto není bezpečné v informační grafice používat barvu jako jediný nositel významu — například „červené je špatně, zelené dobře“ bez dalších symbolů nebo textu.

Barva v počítači je tedy **modelovaná číselná reprezentace**, která se snaží dosáhnout předvídatelného vizuálního výsledku. Není to totéž co absolutní fyzikální popis lidského vjemu.

---

## 3.2 RGB: jak obrazovka skládá světlo

RGB je **aditivní barevný model** založený na třech složkách:

- red,
- green,
- blue.

Začínáme od tmy a přidáváme světlo.

Pokud mají všechny tři složky nulovou hodnotu, dostaneme černou. Pokud jsou všechny na maximu, výsledkem je v daném RGB prostoru bílá.

V osmibitovém RGB zápisu například:

`R = 255, G = 0, B = 0`

znamená maximální červenou složku a nulové zelenou a modrou.

`R = 255, G = 255, B = 255`

představuje bílou.

Když mají všechny tři kanály stejnou hodnotu, vzniká neutrální odstín šedé:

`R = G = B`

To je přesnější formulace než tvrdit, že neutrální barvy „neobsahují pigment“. Pigmenty se týkají fyzických materiálů a tisku; RGB obraz na monitoru pracuje se světlem.

RGB však není jediný konkrétní barevný prostor. Číselná trojice `(200, 30, 30)` nemá úplně jednoznačný fyzikální význam, dokud nevíme, v jakém **barevném prostoru** je interpretována.

Nejčastěji se setkáme s:

- sRGB,
- Display P3,
- Adobe RGB.

Každý má definované primární barvy, bílý bod a převodní charakteristiku.

Proto může stejná trojice čísel v různých barevných prostorech odpovídat mírně jiné skutečné barvě.

---

## 3.3 CMYK a proč tisk není obrácený monitor

Tiskárna nevyzařuje světlo jako monitor. Barvu vytváří inkousty nebo tonery, které část dopadajícího světla absorbují a část odrážejí.

Proto se v polygrafii používá **subtraktivní model**.

Základní složky jsou:

- C — cyan,
- M — magenta,
- Y — yellow,
- K — black.

Teoreticky by kombinace azurové, purpurové a žluté mohla vytvářet velmi tmavou barvu. V praktickém tisku se používá samostatná černá složka K kvůli kvalitě, neutralitě, ekonomice a reprodukci detailu.

CMYK není jeden univerzální barevný prostor. Výsledek závisí na konkrétním tiskařském procesu, inkoustech, papíru a profilu.

Proto nestačí vzít obrázek v RGB a prostě „přepnout režim CMYK“. Profesionální převod musí zohlednit cílovou tiskovou podmínku.

Některé syté barvy zobrazitelné na moderním monitoru nelze danou tiskovou technologií reprodukovat. Tyto barvy leží **mimo gamut** tiskového zařízení.

A naopak některé tiskové kombinace mohou mít charakter, který běžný displej přesně nenapodobí.

Při přípravě pro tisk proto používáme správu barev, profily a někdy **soft proofing** — simulaci tiskového výsledku na kalibrovaném monitoru.

---

## 3.4 HSL, HSV/HSB a proč jsou pohodlné pro člověka

RGB je vhodný pro technickou reprezentaci displejového obrazu, ale člověk často chce říci:

„udělej barvu trochu méně sytou“

nebo:

„posuň odstín směrem k oranžové“.

Proto se používají modely jako **HSL** nebo **HSV/HSB**.

Typicky pracují s veličinami:

- hue — odstín,
- saturation — sytost,
- lightness nebo value/brightness — světlost či jasová veličina podle modelu.

Tyto modely jsou intuitivnější pro výběr a úpravu barev. Barevný kruh umožní snadno měnit odstín a samostatný posuvník sytost.

Je však důležité nepovažovat HSL nebo HSV za přesný model lidského barevného vnímání. Nejsou **perceptuálně uniformní**: stejná číselná změna v různých částech prostoru nemusí působit stejně výrazně.

Pro odbornou správu barev se používají také modely a prostory jako CIE XYZ nebo CIELAB. Ty umožňují lépe popisovat vztahy mezi zařízeními a vnímáním.

Pro základní rastrovou grafiku ale stačí chápat roli jednotlivých modelů:

- RGB — technická reprezentace pro displeje a obrazová data,
- CMYK — tisková separace,
- HSL/HSV — intuitivní ovládání barev,
- CIE prostory — základ pokročilé správy a měření barev.

---

## 3.5 Gamut, barevný prostor a ICC profil

**Gamut** je rozsah barev, které určitý systém dokáže reprezentovat nebo fyzicky reprodukovat.

Moderní displej s Display P3 může zobrazit některé sytější barvy než tradiční sRGB monitor. Profesionální fotografický monitor může pokrývat velkou část Adobe RGB.

Samotný název barevného prostoru ale ještě neříká, co konkrétní fyzický monitor skutečně umí. Zařízení má vlastní reálné vlastnosti a ty se mohou časem měnit.

Pro převody mezi zařízeními se používá **color management** — správa barev.

Základním nástrojem jsou **ICC profily**, které popisují barevné chování zařízení nebo pracovního prostoru.

Jednoduchý řetězec může být:

**fotoaparát / obraz → pracovní barevný prostor → profil monitoru → vizuální zobrazení**

Při tisku:

**pracovní obraz → profil konkrétní tiskové podmínky → tiskárna + inkoust + papír**

Pokud aplikace správu barev ignoruje nebo chybí profil, mohou se barvy mezi programy a zařízeními výrazně lišit.

Proto se například pro běžný web často používá sRGB. Je relativně konzervativní a široce podporovaný. Moderní web ale umí pracovat i s širšími prostory, pokud je celý řetězec správně spravován.

---

## 3.6 Kalibrace a profilace monitoru

Pojmy **kalibrace** a **profilace** se často zaměňují.

Kalibrace znamená nastavit zařízení do definovaného stavu — například jas, bílý bod nebo tónovou odezvu.

Profilace následně měří, jak se zařízení v tomto stavu skutečně chová, a vytvoří profil, který tuto vlastnost popisuje systému pro správu barev.

Profesionální monitor lze měřit kolorimetrem nebo spektrofotometrem. Software zobrazí sadu známých barevných polí, měřicí zařízení zjistí skutečný výstup a vytvoří korekční data a ICC profil.

Cílem není zajistit, aby monitor „ukazoval absolutní pravdu“. Cílem je dosáhnout **předvídatelného a reprodukovatelného chování**.

Význam má také okolní osvětlení. Fotografie upravovaná na extrémně jasném monitoru v temné místnosti může být při běžném zobrazení nebo tisku příliš tmavá.

Správa barev je tedy celý řetězec od dat přes profily až po fyzické zařízení a podmínky pozorování.

**Hlavní myšlenka třetí lekce:** barva není pouze trojice RGB čísel. Aby byl výsledek předvídatelný, musíme znát barevný prostor, gamut a vlastnosti konkrétního zobrazovacího nebo tiskového zařízení.

---

# 4. Rastrový editor a nedestruktivní práce s obrazem

## 4.1 Výběr, ořez a transformace

Rastrový editor umožňuje měnit obraz na úrovni pixelů, ale zároveň nabízí nástroje, které dovolují pracovat s logickými oblastmi.

**Výběr** určuje, na kterou část obrazu bude operace působit.

Výběr může vzniknout:

- geometricky,
- ručním lasem,
- podle podobnosti barvy,
- podle jasu,
- podle hran,
- automatickou segmentací pomocí AI.

Dřívější „kouzelná hůlka“ porovnávala především podobnost barev. Moderní nástroje dokážou rozpoznat člověka, oblohu, vlasy nebo konkrétní objekt díky strojovému učení.

**Ořez** mění kompozici odstraněním části obrazu. Není to totéž co změna rozlišení. Po ořezu může zůstat každý pixel původní kvality, jen je jich méně.

**Transformace** mění geometrické uspořádání: velikost, rotaci, perspektivu, zkosení nebo deformaci.

Při transformaci rastrové vrstvy se často musí přepočítat pixely, a opakované destruktivní transformace mohou snižovat kvalitu. Proto editory nabízejí nedestruktivní varianty, například smart objects nebo parametrické transformační operace.

---

## 4.2 Vrstvy: digitální obdoba průhledných fólií

Jednou z nejdůležitějších myšlenek moderního grafického editoru jsou **vrstvy**.

Můžeme si je představit jako průhledné fólie položené nad sebou. Na jedné je fotografie, na další text, na další stín a nad nimi barevná korekce.

Výhodou je, že jednotlivé části lze upravovat nezávisle.

Vrstva může mít:

- vlastní obsah,
- průhlednost,
- masku,
- transformaci,
- efekty,
- režim prolnutí.

Pořadí vrstev je důležité. Horní vrstva může zakrývat spodní, ale podle průhlednosti a režimu prolnutí se mohou jejich hodnoty kombinovat.

**Blend modes** neboli režimy prolnutí určují matematický způsob kombinace pixelů vrstev.

Například Multiply typicky ztmavuje, Screen zesvětluje a Overlay kombinuje kontrastnější chování podle vstupních hodnot.

Není nutné znát všechny vzorce, ale je důležité vědět, že režim prolnutí není dekorativní „efekt“. Je to přesně definovaná operace nad hodnotami pixelů.

Vrstvy umožňují zachovat strukturu projektu. Pokud vše předčasně sloučíme do jediného obrazu, přijdeme o možnost pohodlně upravovat části odděleně.

---

## 4.3 Masky: skrýt místo smazat

Klasická guma maže pixely. Pokud později zjistíme, že jsme odstranili příliš mnoho, potřebujeme historii úprav nebo původní soubor.

**Maska vrstvy** řeší problém jinak. Obsah vrstvy zůstává zachovaný, ale maska určuje, kde se má zobrazovat.

Typicky:

- bílá — vrstva je viditelná,
- černá — skrytá,
- odstíny šedé — částečná viditelnost.

Proto je přesnější říci, že maska je **obraz řídící míru účinku nebo viditelnosti**, nikoli nutně pouze černobílý obrázek.

Masky patří k základům **nedestruktivní editace**.

Můžeme například vyříznout člověka z pozadí bez jediného skutečného smazání původních pixelů. Když později objevíme chybu ve vlasech, upravíme masku.

Stejný princip se používá u korekčních vrstev. Můžeme zesvětlit pouze obličej nebo ztmavit oblohu tím, že korekci omezíme maskou.

Moderní editory dokážou masky automaticky generovat pomocí AI segmentace, ale výsledek je stále dobré zkontrolovat. Jemné vlasy, průsvitné objekty, sklo nebo složité hrany mohou být problematické.

---

## 4.4 Nedestruktivní úpravy, adjustment layers a smart objects

Při destruktivní úpravě přepisujeme původní pixely. Pokud například přímo zvýšíme kontrast a soubor uložíme bez zachování předchozího stavu, původní informace může být ztracena.

Moderní workflow proto používá **nedestruktivní úpravy**.

Patří sem:

- korekční vrstvy,
- masky,
- smart objects,
- parametrické RAW úpravy,
- nedestruktivní filtry,
- virtuální kopie.

**Adjustment layer** neobsahuje klasický obraz. Uchovává instrukci typu „změň křivku tónů“ a aplikuje ji na vrstvy pod sebou.

Výhoda je zásadní: parametry lze kdykoli změnit, vypnout nebo omezit maskou.

**Smart object** může uchovávat původní zdroj tak, aby opakované transformace a některé filtry nemusely pokaždé trvale přepočítávat a zhoršovat původní obsah.

Programy pro RAW workflow, například Lightroom nebo darktable, pracují ještě jinak. Zdrojový RAW soubor běžně nemění. Ukládají seznam úprav a výsledný obraz se přepočítává až při náhledu nebo exportu.

To je důležitá obecná myšlenka:

**editovat obraz nemusí znamenat přepisovat obrazová data; můžeme ukládat recept na jejich zobrazení.**

---

## 4.5 Histogram, úrovně a křivky

Histogram je graf, který ukazuje rozložení tónových hodnot v obrazu.

Na vodorovné ose jsou typicky hodnoty od tmavých po světlé, na svislé počet pixelů.

Histogram neříká, zda je fotografie „dobrá“. Je to diagnostický nástroj.

Pokud se velká část hodnot natlačí na úplný pravý okraj, může dojít k **clippingu světel** — různé velmi světlé hodnoty se sloučí do maxima a detail se ztratí.

Podobně může vzniknout clipping ve stínech.

Nástroj **Levels** umožňuje nastavit černý bod, bílý bod a střední tóny.

**Curves** jsou flexibilnější. Křivka mapuje vstupní jasové hodnoty na výstupní. Typická jemná S-křivka zvýší kontrast tím, že ztmaví část stínů a zesvětlí část světel.

Křivky lze používat také po jednotlivých barevných kanálech a tím ovlivňovat barevné vyvážení.

Při korekcích je důležité sledovat, zda nevytváříme clipping a zda výsledný obraz stále odpovídá zamýšlenému účelu.

---

## 4.6 Filtry, retuš a AI nástroje

Filtr je operace, která vypočítává nové hodnoty pixelů podle určitého algoritmu.

Může provádět například:

- rozostření,
- doostření,
- redukci šumu,
- detekci hran,
- změnu barev,
- geometrické zkreslení.

Doostření ve skutečnosti „neobjevuje ostrý detail“. Zvyšuje lokální kontrast kolem hran, takže obraz působí ostřeji.

Podobně redukce šumu hledá kompromis mezi odstraněním náhodných změn a zachováním jemných detailů.

Retušovací nástroje jako **clone stamp** kopírují obrazovou strukturu z jedné oblasti do druhé. Healing nástroje se snaží navíc přizpůsobit tón a texturu okolí.

Moderní AI editory jdou dál. Umějí:

- automaticky vybrat objekt,
- odstranit pozadí,
- rekonstruovat poškozené oblasti,
- redukovat šum,
- zvětšovat obraz,
- generativně doplnit obsah mimo původní záběr.

Zásadní je odlišit **restauraci nebo korekci** od **syntézy nového obsahu**.

Když AI generativně doplní část fotografie, nevytahuje skrytá původní data ze souboru. Vytváří pravděpodobný obraz na základě modelu a okolního kontextu.

To je přijatelné v kreativní grafice, ale musí být velmi opatrně používáno v dokumentární, vědecké nebo forenzní fotografii.

**Hlavní myšlenka čtvrté lekce:** kvalitní editor není jen sada efektů. Je to systém pro řízené, pokud možno nedestruktivní transformace obrazových dat, který umožňuje oddělit obsah, maskování, korekce a výsledný export.

---

# 5. Digitální fotoaparát: jak se světlo mění na data

## 5.1 Od objektivu k digitálnímu obrazu

Digitální fotografie začíná světlem odraženým od scény.

Objektiv světlo soustředí na **snímací čip**. Jednotlivé světlocitlivé prvky převádějí dopadající fotony na elektrický náboj. Elektronika hodnoty přečte, převede na čísla a obrazový procesor z nich sestaví fotografii.

Moderní fotoaparáty používají především **CMOS snímače**. CCD byly historicky významné a stále mají specializované použití, ale v běžné současné fotografii CMOS dominuje.

Snímač je tvořen mřížkou fotosenzorů. Jeden fotosenzor sám o sobě typicky měří především množství dopadajícího světla, nikoli kompletní RGB barvu.

Proto se nad snímač často umisťuje **color filter array**, nejznámější je Bayerova maska. Jednotlivé pozice propouštějí převážně červenou, zelenou nebo modrou část spektra.

Typický Bayerův vzor má dvakrát více zelených filtrů než červených nebo modrých, což souvisí mimo jiné s citlivostí lidského vidění na jasovou informaci.

Výsledkem snímání tedy není hotová plnobarevná mřížka RGB pixelů. Software musí chybějící barevné složky dopočítat z okolních hodnot procesem nazývaným **demosaicing**.

Digitální fotografie je proto výsledkem měření i výpočtu.

---

## 5.2 Velikost snímače, pixelů a dynamický rozsah

Megapixely říkají, kolik obrazových vzorků výstup obsahuje. Neříkají ale všechno o snímači.

Velký snímač může při podobném počtu pixelů používat větší fotosenzorové oblasti, které za daných podmínek zachytí více fotonů. To může pomoci poměru signálu k šumu.

Kvalitu ovlivňuje mnoho faktorů:

- velikost snímače,
- velikost a konstrukce fotodiod,
- účinnost převodu světla,
- elektronický šum,
- A/D převod,
- obrazový procesor,
- objektiv.

Důležitým pojmem je **dynamický rozsah** — rozdíl mezi nejslabším a nejsilnějším signálem, který systém dokáže užitečně zachytit.

Scéna může obsahovat velmi tmavý interiér a současně jasnou oblohu za oknem. Pokud rozdíl překročí možnosti snímače a zvoleného záznamu, některé části budou bez detailu ve stínech nebo přepálené ve světlech.

Moderní fotoaparáty a telefony proto používají víceexpozicové HDR techniky. Pořídí několik různých měření a výpočetně je spojí.

To opět ukazuje, že „fotografie“ nemusí být jediný okamžik jednoho fyzického senzoru. V computational photography může být výsledkem kombinace mnoha snímků a algoritmů.

---

## 5.3 Objektiv, ohnisková vzdálenost a úhel záběru

Objektiv není jen „sklo před senzorem“. Je to optický systém, který zásadně ovlivňuje obraz.

**Ohnisková vzdálenost** se udává v milimetrech a spolu s velikostí snímače určuje **úhel záběru**.

Proto není přesné říci, že například 50 mm vždy znamená stejný záběr. Objektiv 50 mm na full-frame fotoaparátu a na menším APS-C snímači poskytne jiný úhel záběru.

Pro srovnávání se používá **ekvivalentní ohnisková vzdálenost vůči full frame**.

Širokoúhlý objektiv zachytí větší část scény. Teleobjektiv užší část a umožní vzdálený objekt zobrazit větší v rámci snímku.

Perspektivu však neurčuje ohnisková vzdálenost sama o sobě. Perspektivní vztahy určuje především **pozice fotoaparátu vůči scéně**. Ohnisko nás často přiměje změnit vzdálenost od objektu, a tím perspektivu nepřímo ovlivní.

Objektiv může mít také optické vady:

- vinětaci,
- chromatickou aberaci,
- soudkovité nebo poduškovité zkreslení,
- neostrost v rozích,
- flare.

Mnoho z nich lze částečně korigovat softwarově podle profilu objektivu.

---

## 5.4 Clona a hloubka ostrosti

**Clona** reguluje velikost otvoru v objektivu, kterým prochází světlo.

Vyjadřuje se pomocí **f-čísla**, například:

`f/1.8`, `f/2.8`, `f/5.6`, `f/11`

Nižší f-číslo znamená větší relativní otvor a při stejném čase propustí více světla.

Clona zároveň ovlivňuje **hloubku ostrosti** — rozsah vzdáleností, které vnímáme jako dostatečně ostré.

Větší otvor, například f/1.8, může při stejných ostatních podmínkách vést k menší hloubce ostrosti. To se využívá u portrétů k oddělení člověka od rozostřeného pozadí.

Hloubka ostrosti však nezávisí jen na cloně. Ovlivňuje ji také:

- ohnisková vzdálenost,
- vzdálenost zaostření,
- velikost výsledného zobrazení,
- přijatelný kruh neostrosti.

Ani tvrzení „nižší clona = vždy rozmazané pozadí“ proto není úplné.

Při velmi malém otvoru může navíc dojít k výraznější **difrakci**, která omezí ostrost. Clonu tedy nevolíme jen podle množství světla, ale i podle požadovaného charakteru obrazu a vlastností objektivu.

---

## 5.5 Čas závěrky a pohyb

**Čas závěrky** určuje, jak dlouho snímač sbírá světlo pro jednu expozici.

Například:

`1/1000 s`

je velmi krátký čas a může „zmrazit“ rychlý pohyb.

`1/15 s`

je mnohem delší a pohybující se objekt může být rozmazaný.

Delší čas zároveň zvyšuje riziko rozmazání způsobeného pohybem samotného fotoaparátu.

Proto fotografové při dlouhých časech používají stativ nebo stabilizaci.

Pohybové rozmazání ale není vždy chyba. Ve sportovní fotografii může panning zachovat relativně ostrý pohybující se objekt a rozmazat pozadí tak, že obraz působí dynamicky.

Dlouhá expozice dokáže proměnit tekoucí vodu v hladkou strukturu nebo zaznamenat světelné stopy aut.

Čas závěrky tedy není jen technická veličina „pro správný jas“. Je to kreativní nástroj, který rozhoduje, jak bude fotografie reprezentovat čas a pohyb.

---

## 5.6 ISO: jas fotografie není totéž co množství světla

Ve výukových materiálech se často říká:

> „ISO je citlivost snímače.“

Pro základní fotografickou praxi je to užitečná zkratka, ale u digitálního snímače technicky zjednodušuje situaci.

Fyzické množství světla zachyceného snímačem je určeno především:

- clonou,
- časem expozice,
- jasem scény.

Změna ISO sama o sobě nepřidá na snímač další fotony.

ISO u digitálního fotoaparátu souvisí s tím, jak fotoaparát mapuje a zesiluje elektrický signál do výsledných obrazových hodnot a jaký expoziční režim očekává.

Vyšší ISO umožní vytvořit světleji vypadající výsledek při menším množství zachyceného světla, ale šum se stane viditelnější. Hlavním problémem často není, že by ISO „vytvářelo šum z ničeho“, ale že pracujeme se slabším světelným signálem a horším poměrem signálu k šumu.

Proto je důležité rozlišit:

**expozici** — množství světla zachyceného snímačem,

a

**výsledný jas obrazu** — ten může ovlivnit také ISO a následné zpracování.

Klasický **expoziční trojúhelník** je stále velmi užitečná didaktická pomůcka, pokud si uvědomíme, že všechny tři parametry nemají fyzikálně totožnou roli.

---

## 5.7 Computational photography: fotoaparát jako výpočetní systém

Moderní smartphone často používá malý snímač a miniaturní objektiv, přesto dokáže vytvořit působivý snímek za špatného světla.

Důvodem je **computational photography**.

Telefon může ještě před stisknutím spouště průběžně ukládat snímky do vyrovnávací paměti. Při pořízení fotografie může spojit několik expozic, zarovnat je, potlačit šum a zvýšit dynamický rozsah.

Portrétní režim může odhadnout hloubkovou mapu a synteticky rozostřit pozadí.

Noční režim může spojovat několik snímků pořízených během delšího intervalu.

AI může rozpoznat scénu, obličej, oblohu nebo text a aplikovat lokálně odlišné úpravy.

Výsledná fotografie tedy stále vychází ze světla zachyceného kamerou, ale mezi senzorem a výsledným JPEGem probíhá stále větší množství výpočetního zpracování.

Tím se hranice mezi fotografií a počítačovou grafikou částečně stírá.

**Hlavní myšlenka páté lekce:** digitální fotoaparát není jen elektronická obdoba filmu. Je to měřicí a výpočetní systém, ve kterém optika, snímač a software společně vytvářejí výsledný obraz.

---

# 6. Zpracování, publikace a důvěryhodnost digitální fotografie

## 6.1 RAW není „hotová fotografie“

RAW se často popisuje jako „nezpracovaná fotografie obsahující všechna data ze snímače“. To vystihuje jeho účel, ale technicky je vhodné formulaci zpřesnit.

RAW soubor obvykle obsahuje data blízká původním měřením snímače spolu s rozsáhlými metadaty. Může být bezeztrátově nebo někdy i ztrátově komprimován a fotoaparát na data může aplikovat určité korekce už před uložením.

Navíc nejde o jeden univerzální formát. Výrobci používají například:

- CR3,
- NEF,
- ARW,
- RAF,

a existuje také otevřeněji specifikovaný DNG.

RAW obvykle neobsahuje jen „hotové RGB pixely“. U Bayerova snímače je nutné provést demosaicing, vyvážení bílé, tónové mapování, převod barev a další operace.

Proto může stejný RAW soubor v různých programech vypadat trochu jinak.

JPEG vytvořený přímo fotoaparátem už prošel celou interní obrazovou pipeline:

**snímač → demosaicing → white balance → redukce šumu → doostření → tónová křivka → barvy → komprese JPEG**

RAW dává fotografovi větší kontrolu nad tímto zpracováním později.

---

## 6.2 Vyvážení bílé a barevná teplota

Lidský mozek se dokáže výrazně přizpůsobit barvě osvětlení. Bílý papír vnímáme jako relativně bílý pod denním světlem i pod teplou žárovkou.

Fotoaparát musí tuto adaptaci napodobit.

**White balance** neboli vyvážení bílé upravuje vztah barevných kanálů tak, aby neutrální objekty působily neutrálně nebo aby fotografie měla zamýšlený barevný charakter.

Osvětlení se často zjednodušeně popisuje pomocí **correlated color temperature** v kelvinech.

Nižší teploty odpovídají tepleji působícímu světlu, vyšší hodnoty modřejšímu dennímu světlu.

Vyvážení bílé však není jen jediný posuvník teploty. Některé zdroje světla mají také zelený nebo purpurový posun a složité spektrum.

RAW poskytuje při korekci bílé výraznou výhodu, protože původní měření kanálů zůstává zachováno. U silně zpracovaného JPEG je prostor pro extrémní opravy menší.

Správná bílá navíc nemusí být vždy kreativním cílem. Fotograf může záměrně zachovat teplou atmosféru západu slunce místo dokonale neutrálního výsledku.

---

## 6.3 Expozice, stíny, světla a lokální kontrast

Postprodukce nezačíná efektem. Nejprve potřebujeme správně rozdělit tónové hodnoty.

Základní úpravy typicky zahrnují:

- celkový jas,
- kontrast,
- černý a bílý bod,
- stíny,
- světla,
- lokální kontrast.

Korekce nemůže vždy obnovit informaci, která při snímání nebyla zachycena. Pokud je část obrazu skutečně saturována na maximum ve všech relevantních kanálech, detail ve světlech může být nenávratně pryč.

RAW ale často uchovává větší tónovou rezervu než výsledný osmibitový JPEG, takže některé zdánlivě přepálené nebo tmavé oblasti lze při zpracování zachránit.

Velmi výrazné vytahování stínů může zvýraznit šum.

Proto je postprodukce vždy práce s kompromisem: snažíme se využít dostupný dynamický rozsah, aniž bychom vytvářeli nepřirozený obraz nebo technické artefakty.

Lokální korekce umožňují zasáhnout jen určitou část snímku pomocí masek, přechodů nebo AI výběru objektů.

Moderní workflow tak spojuje principy fotografie a rastrového editoru.

---

## 6.4 Redukce šumu, doostření a korekce objektivu

Digitální fotografie může obsahovat několik druhů šumu a technických nedokonalostí.

**Redukce šumu** se snaží odlišit náhodnou složku od skutečné obrazové textury. Příliš agresivní nastavení však může odstranit jemné detaily a vytvořit „plastický“ vzhled.

Moderní AI denoise modely dokážou využít naučené struktury a často poskytují velmi dobré výsledky. Stále ale pracují s odhadem a mohou obraz interpretovat chybně.

**Doostření** zvýrazňuje přechody a lokální kontrast. Může kompenzovat část měkkosti optiky, demosaicingu nebo změny velikosti.

Doostření ale neumí vrátit skutečný detail z fotografie silně rozostřené chybným zaostřením.

Korekce objektivu může opravit:

- geometrické zkreslení,
- vinětaci,
- chromatickou aberaci.

Program často používá databázi profilů konkrétních objektivů a hodnoty ohniskové vzdálenosti či clony z EXIF metadat.

U některých moderních fotoaparátů je softwarová korekce součástí celkového návrhu objektivu a může probíhat automaticky.

---

## 6.5 Metadata, EXIF a správa fotografií

Digitální fotografie není jen obrazová matice. Soubor může obsahovat rozsáhlá metadata.

**EXIF** typicky uchovává například:

- datum a čas,
- model fotoaparátu,
- objektiv,
- ohniskovou vzdálenost,
- clonu,
- čas závěrky,
- ISO,
- někdy GPS polohu.

Další metadata mohou obsahovat autora, copyright, popis, klíčová slova nebo hodnocení.

Tyto údaje jsou velmi užitečné při organizaci fotografického archivu. Programy jako Lightroom nebo darktable umožňují spravovat tisíce snímků pomocí katalogu, metadat a nedestruktivních úprav.

Metadata mají ale také **soukromou stránku**. Fotografie z telefonu může obsahovat přesnou polohu domova nebo školy.

Před zveřejněním citlivého snímku je proto vhodné vědět, jaká metadata služba zachovává a co případně odstranit.

Je také důležité vědět, že metadata lze změnit. EXIF není kryptografický důkaz autenticity fotografie.

---

## 6.6 Export pro web, tisk a archiv

Jeden pracovní obraz může potřebovat několik různých výstupů.

### Pro web

Potřebujeme:

- přiměřené pixelové rozměry,
- účinnou kompresi,
- vhodný barevný prostor,
- kompatibilní formát,
- rozumnou velikost souboru.

Typickou volbou může být JPEG, WebP nebo AVIF podle požadavků.

### Pro tisk

Musíme řešit:

- fyzickou velikost,
- potřebnou PPI,
- barevný management,
- profil tiskové podmínky,
- způsob doostření pro výstup.

### Pro archiv

Cílem může být zachovat:

- originální RAW,
- pracovní projekt,
- kvalitní export,
- metadata,
- zálohu na více místech.

Není vhodné uchovávat jedinou malou JPEG verzi jako jediný „originál“, pokud můžeme potřebovat budoucí přepracování.

Souborové názvy, katalogizace a zálohování jsou součástí fotografického workflow stejně jako samotná retuš.

---

## 6.7 AI, syntetický obraz a otázka důvěryhodnosti

Generativní AI zásadně změnila vztah mezi fotografií a obrazem.

Dříve bylo samozřejmě možné fotografii retušovat nebo montovat, ale dnešní model dokáže během sekund vytvořit realistický člověk, prostředí nebo událost, která nikdy neexistovala.

To klade nové nároky na informační gramotnost.

Samotný realistický vzhled už není dostatečným důkazem, že obraz zachycuje skutečnou událost.

Stejně tak automatické „AI detektory“ nejsou neomylné.

Při ověřování digitálního obrazu je proto důležitější sledovat:

- původ souboru,
- kontext publikace,
- důvěryhodnost zdroje,
- navazující záběry,
- nezávislá potvrzení,
- metadata a provenance,
- případné kryptografické údaje o původu.

Vznikají také standardy pro **Content Credentials / C2PA**, které se snaží k obsahu připojovat ověřitelné informace o jeho původu a historii úprav. Ani takový systém ale není univerzálním „detektorem pravdy“ — dokáže doložit určitou historii, pokud celý řetězec podporuje potřebné mechanismy.

V kreativní práci je generativní AI mocný nástroj. V dokumentární fotografii je však důležité transparentně odlišit korekci skutečně zachyceného obrazu od generování nového obsahu.

---

# Závěrečné propojení kurzu

Rastrová grafika a digitální fotografie tvoří jeden souvislý řetězec.

Na začátku je světlo a fyzická scéna. Objektiv vytváří obraz na snímači, fotosenzory převádějí světlo na elektrický signál a A/D převodník jej mění na čísla.

Obrazový procesor a software z naměřených hodnot rekonstruují rastrový obraz:

**světlo → objektiv → snímač → elektrický signál → digitální vzorky → demosaicing → rastrový obraz**

Potom přichází další vrstva:

**pixely → barevný prostor → vrstvy a masky → korekce → komprese → export**

A nakonec uživatelská situace:

**web / tisk / archiv / analýza / další editace**

Každá fáze ovlivňuje výsledek. Vyšší počet megapixelů nepomůže špatně zaostřené fotografii. Správný monitor nezachrání obraz uložený v nevhodném formátu. Bezeztrátový PNG nezíská zpět detail, který se ztratil při silné JPEG kompresi. A generativní AI může vytvořit přesvědčivý detail, ale nemůže zaručit, že tento detail v původní scéně skutečně existoval.

Celý tematický okruh proto není jen „ovládání Photoshopu“ nebo „nastavení fotoaparátu“. Je to studium toho, **jak se vizuální informace měří, reprezentuje, interpretuje, upravuje a nakonec znovu převádí do obrazu, který vidí člověk**.
