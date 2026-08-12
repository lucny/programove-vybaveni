## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Výběr, ořez a transformace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vrstvy: digitální obdoba průhledných fólií**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Masky: skrýt místo smazat**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Nedestruktivní úpravy, adjustment layers a smart objects**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Histogram, úrovně a křivky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Histogram je graf, který ukazuje rozložení tónových hodnot v obrazu.

Na vodorovné ose jsou typicky hodnoty od tmavých po světlé, na svislé počet pixelů.

Histogram neříká, zda je fotografie „dobrá“. Je to diagnostický nástroj.

Pokud se velká část hodnot natlačí na úplný pravý okraj, může dojít k **clippingu světel** — různé velmi světlé hodnoty se sloučí do maxima a detail se ztratí.

Podobně může vzniknout clipping ve stínech.

Nástroj **Levels** umožňuje nastavit černý bod, bílý bod a střední tóny.

**Curves** jsou flexibilnější. Křivka mapuje vstupní jasové hodnoty na výstupní. Typická jemná S-křivka zvýší kontrast tím, že ztmaví část stínů a zesvětlí část světel.

Křivky lze používat také po jednotlivých barevných kanálech a tím ovlivňovat barevné vyvážení.

Při korekcích je důležité sledovat, zda nevytváříme clipping a zda výsledný obraz stále odpovídá zamýšlenému účelu.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Filtry, retuš a AI nástroje**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
