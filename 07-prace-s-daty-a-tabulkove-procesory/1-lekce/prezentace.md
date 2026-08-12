## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Data nezačínají v tabulce**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Škola může položit několik podobně znějících, ale ve skutečnosti odlišných otázek. „Která učebna je nejteplejší?“ vyžaduje porovnání místností. „Kdy je žákům v učebnách nepříjemně?“ přidává čas, obsazenost a možná i dotazníkové hodnocení. „Lze snížit spotřebu bez zhoršení prostředí?“ propojuje údaje o teplotě s energií a způsobem provozu. Každá otázka vede k jinému výběru proměnných i k jinému způsobu analýzy.

Dobrá analytická otázka proto určuje, **co budeme pozorovat**, **které vlastnosti změříme** a **jak poznáme užitečnou odpověď**. V našem projektu může být jedním pozorováním stav jedné učebny v konkrétním čase. Proměnnými budou například identifikátor učebny, datum a čas, teplota, koncentrace oxidu uhličitého, spotřeba energie a počet přítomných osob. Teprve s takovým popisem získá číslo `24,7` význam: nejde jen o hodnotu, ale o teplotu ve stupních Celsia, zaznamenanou určitým senzorem v určité místnosti a čase.

Užitečný mentální model celého tématu je:

**otázka → sběr → kontrola → struktura → analýza → interpretace → rozhodnutí**

Chyba na začátku se přitom nedá zachránit sebelepším grafem. Pokud například změříme každou učebnu jen jednou a v jinou denní dobu, porovnáváme současně místnosti i čas. Z výsledku pak nelze spolehlivě poznat, co způsobilo rozdíl.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
Jeden záznam, jedna proměnná, jedna hodnota
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:

-

Pro analýzu je nejpraktičtější **obdélníková datová tabulka**. Jeden řádek představuje jeden záznam, jeden sloupec jednu proměnnou a jedna buňka jednu hodnotu. Tento způsob uspořádání se často označuje jako **tidy data — uklizená data**.

| cas | ucebna_id | teplota_c | co2_ppm | obsazenost |
|---|---|---:|---:|---:|
| 2026-10-12 08:00 | A203 | 21,8 | 690 | 24 |
| 2026-10-12 08:05 | A203 | 22,1 | 745 | 24 |
| 2026-10-12 08:00 | B105 | 20,9 | 520 | 0 |

Toto pravidlo zní prostě, ale řeší mnoho pozdějších problémů. Zápis `21,8 °C` spojuje hodnotu s jednotkou a může být načten jako text; vhodnější je uložit číslo `21,8` a jednotku popsat v názvu sloupce nebo metadatech. Zápis `23/24` v jediné buňce zase může znamenat obsazenost, školní rok nebo datum. Dvě různá měření vložená do jedné buňky nelze jednoduše filtrovat ani počítat.

Každý sloupec by měl mít také odpovídající **datový typ**. Teplota a spotřeba jsou číselné hodnoty, označení učebny je kategorie, poznámka technika je text a čas měření patří k datu a času. Kategorie mohou být bez pořadí, například typ učebny, nebo uspořádané, například hodnocení „nízké — střední — vysoké“. Čísla zase mohou vyjadřovat počet kusů nebo spojité měření. Rozdíl není jen terminologický: průměr z identifikačních čísel učeben nedává smysl, přestože je program technicky sečíst umí.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Sběr dat a neviditelné zkreslení**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Data mohou vzniknout ručním zápisem, formulářem, senzorem, exportem z databáze, stažením otevřené datové sady nebo dotazem na **API — aplikační programové rozhraní**. Forma získání však sama nezaručuje kvalitu. Automatický senzor může být špatně kalibrovaný, formulář může obsahovat sugestivní otázku a databázový export může vynechat zrušené objednávky.

Pokud se na tepelnou pohodu zeptáme pouze členů ekologického kroužku, nemusí odpovědi zastupovat celou školu. Vzniká **výběrové zkreslení — selection bias**. Podobně zavádějící bude dobrovolný dotazník, který vyplní hlavně lidé s velmi silným názorem. **Vzorek** je použitelný jen tehdy, když rozumně zastupuje populaci, o níž chceme mluvit. Důležitá proto není pouze jeho velikost, ale i způsob výběru a podíl lidí, kteří neodpověděli.

U senzorů je vhodné předem určit měřicí interval, umístění zařízení a kontrolní pravidla. Teploměr nad radiátorem neměří totéž co senzor ve výšce hlavy uprostřed místnosti. Pětiminutový interval může zachytit průběh hodiny, jedna hodnota po obědě nikoli. Kvalita analýzy tak vzniká už při návrhu sběru, nikoli až při výpočtu průměru.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Metadata jsou návod k použití**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Datová sada bez vysvětlení připomíná krabici součástek bez návodu. **Metadata** popisují význam sloupců, jednotky, datové typy, původ, časové období, způsob měření, licenci a případná omezení. Krátký **datový slovník** může například uvést, že `co2_ppm` znamená koncentraci oxidu uhličitého v částech na milion a `obsazenost` počet přítomných osob v okamžiku měření.

Metadata také brání falešně přesné interpretaci. Hodnota zaokrouhlená na celé kilowatthodiny neposkytuje přesnost na tři desetinná místa jen proto, že ji tabulkový procesor tak zobrazí. Podobně potřebujeme vědět, zda čas označuje začátek intervalu, jeho konec, nebo okamžik odečtu. Bez tohoto kontextu můžeme provést technicky bezchybný výpočet a přesto odpovědět na jinou otázku, než jsme zamýšleli.

**Hlavní myšlenka:** Data nejsou neutrální surovina, která se jednoduše „nasype do Excelu“. Jejich význam i omezení vznikají už při formulaci otázky, výběru vzorku, měření a dokumentaci.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
