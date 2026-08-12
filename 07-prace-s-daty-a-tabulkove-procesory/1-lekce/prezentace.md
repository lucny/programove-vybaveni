## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Data nezačínají v tabulce**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 1.1 Data nezačínají v tabulce

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
**Jeden záznam, jedna proměnná, jedna hodnota**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 1.2 Jeden záznam, jedna proměnná, jedna hodnota

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
**## 1.3 Sběr dat a neviditelné zkreslení

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
**## 1.4 Metadata jsou návod k použití

Datová sada bez vysvětlení připomíná krabici součástek bez návodu. **Metadata** popisují význam sloupců, jednotky, datové typy, původ, časové období, způsob měření, licenci a případná omezení. Krátký **datový slovník** může například uvést, že `co2_ppm` znamená koncentraci oxidu uhličitého v částech na milion a `obsazenost` počet přítomných osob v okamžiku měření.

Metadata také brání falešně přesné interpretaci. Hodnota zaokrouhlená na celé kilowatthodiny neposkytuje přesnost na tři desetinná místa jen proto, že ji tabulkový procesor tak zobrazí. Podobně potřebujeme vědět, zda čas označuje začátek intervalu, jeho konec, nebo okamžik odečtu. Bez tohoto kontextu můžeme provést technicky bezchybný výpočet a přesto odpovědět na jinou otázku, než jsme zamýšleli.

**Hlavní myšlenka:** Data nejsou neutrální surovina, která se jednoduše „nasype do Excelu“. Jejich význam i omezení vznikají už při formulaci otázky, výběru vzorku, měření a dokumentaci.

# 2. Tabulkový procesor jako datová laboratoř

## 2.1 Buňka má obsah, adresu a zobrazení

Sešit tabulkového procesoru obsahuje jeden nebo více listů a každý list tvoří mřížka řádků, sloupců a buněk. Adresa `B5` označuje průsečík sloupce B a řádku 5. Buňka může obsahovat text, číslo, datum, logickou hodnotu nebo vzorec, jehož výsledek se zobrazuje místo zápisu vzorce.

Zásadní je odlišit **hodnotu od formátu**. Hodnotu `0,25` lze zobrazit jako `25 %`; číslo `1234,5` jako `1 234,50 Kč`; stejné datum jako `12. 10. 2026` nebo `2026-10-12`. Formát mění vzhled, nikoli význam uložené hodnoty. Napíšeme-li však přímo text `1 234 Kč`, program s ním nemusí umět počítat. Barva buňky také není spolehlivým datovým údajem. Pokud červená znamená poruchu senzoru, má existovat samostatný sloupec `stav`, ne pouze ruční obarvení.

Stejně důležité je oddělit **zdrojová data od reportu**. List se sloučenými buňkami, vloženými mezisoučty a několika nadpisovými bloky může vypadat dobře při tisku, ale špatně se filtruje, importuje a automatizuje. Praktický sešit proto často obsahuje samostatný list `data`, kde je čistý obdélník záznamů, list `vypocty` a list `report` určený čtenáři.

## 2.2 Vzorec jako opakovatelný postup

Vzorec obvykle začíná znakem `=` a propojuje konstanty, operátory, odkazy a funkce. Chceme-li z příkonu ve wattech a délky intervalu v hodinách odvodit spotřebu ve watthodinách, můžeme v řádku 2 použít například:

```text
=D2*E2
```

Při zkopírování o řádek níže se odkazy změní na `D3*E3`. Jde o **relativní adresování**: vzorec si zachovává vztah k buňkám ve stejném řádku. Pokud je v buňce `H1` převodní koeficient, který má zůstat pevný, zapíšeme `$H$1`. Znak dolaru uzamkne sloupec i řádek, a vznikne **absolutní odkaz**. Zápisy `$H1` a `H$1` jsou **smíšené odkazy**; uzamykají pouze sloupec nebo pouze řádek. Hodí se například při výpočtech v tabulce sazeb kopírovaných dvěma směry.

Dobře navržený vzorec není jen kratší cesta k číslu. Je to viditelný, opakovatelný postup. Ručně zapsaná hodnota `326` neprozradí, jak vznikla. Vzorec `=SUMA(F2:F25)` nebo v anglickém prostředí `=SUM(F2:F25)` lze zkontrolovat a po změně vstupů se přepočítá. Názvy funkcí a oddělovače argumentů se mohou lišit podle programu a jazykového nastavení, princip však zůstává stejný.

## 2.3 Několik funkcí, které řeší většinu prvních úloh

Funkce je hotový výpočet s očekávanými vstupy. Pro začátek je užitečnější důkladně pochopit několik reprezentativních funkcí než se učit dlouhý katalog. `SUM` sčítá, `AVERAGE` počítá průměr, `MIN` a `MAX` hledají krajní hodnoty a `COUNT` počítá číselné buňky. Podmíněné varianty `SUMIFS`, `COUNTIFS` nebo `AVERAGEIFS` umožní pracovat jen s řádky, které splňují zadané podmínky — například vypočítat průměrnou teplotu v učebně A203 během vyučování.

Logická funkce `IF` rozhoduje mezi dvěma výsledky. V projektu můžeme vytvořit kontrolní sloupec:

```text
=IF(C2>35;"zkontrolovat";"v mezích")
```

Takový test neříká, že každá teplota nad 35 °C je automaticky chybná. Označuje záznam k prověření. Funkce pro vyhledávání, například `XLOOKUP`, dokáže podle `ucebna_id` doplnit patro nebo typ místnosti z jiné tabulky. Textové funkce pomohou odstranit přebytečné mezery či rozdělit složený údaj a funkce pro datum umožní odvodit hodinu, den v týdnu nebo měsíc.

Ve větších seznamech bývá výhodné převést oblast na pojmenovanou tabulku. **Strukturované odkazy** pak místo `C2:C5000` používají názvy tabulky a sloupce a při přidání řádků se rozsah automaticky přizpůsobí. Vzorec je čitelnější a méně závislý na aktuální poloze dat.

## 2.4 Filtr, řazení a kontingenční tabulka

Řazení mění pořadí řádků, filtrování dočasně skrývá ty, které nesplňují podmínku. Obojí je jednoduché, ale může být zrádné. Seřadíme-li jen jeden sloupec místo celé tabulky, oddělíme teploty od časů a učeben, k nimž patří. Filtr zase nemaže data; pouze mění aktuální pohled. Výpočet proto musí respektovat, zda má zahrnout všechny řádky, nebo jen viditelné.

**Kontingenční tabulka — pivot table** vytváří agregovaný pohled nad zdrojem. Z tisíců pětiminutových záznamů může během chvíle ukázat průměrnou teplotu podle učebny a hodiny nebo nejvyšší koncentraci CO₂ podle dnů v týdnu. Přesouváním polí mezi řádky, sloupce, hodnoty a filtry měníme otázku, nikoli původní data. Právě proto je kontingenční tabulka výborným modelem analytického myšlení: jedna datová sada může poskytovat více pohledů, ale každý z nich musí mít jasně určenou agregační funkci.

## 2.5 CSV, XLSX a JSON nejsou totéž

Formát **XLSX** uchovává sešit s více listy, vzorci, styly a grafy. Hodí se pro práci člověka v tabulkovém procesoru, ale jeho bohatost komplikuje automatickou výměnu. **CSV — comma-separated values** je naproti tomu prostý text s řádky a oddělenými poli. Nepřenáší vzorce, barvy ani spolehlivý popis datových typů. Při importu proto záleží na oddělovači, kódování, desetinném znaménku a formátu data. V českých souborech se často používá středník, protože čárka slouží jako desetinný oddělovač.

**JSON — JavaScript Object Notation** umí vyjádřit vnořené objekty a seznamy, a proto se s ním často setkáme u webových API. Tabulková analýza však nejlépe pracuje s plochou strukturou, takže hierarchický JSON je obvykle nutné při importu rozbalit do řádků a sloupců. Volba formátu tedy není soutěž o „nejlepší příponu“. Záleží na tom, zda potřebujeme uchovat prezentaci sešitu, jednoduše vyměnit tabulková data, nebo přenést složitější strukturu mezi programy.

**Hlavní myšlenka:** Tabulkový procesor je silný tehdy, když oddělujeme hodnotu od vzhledu, zdroj od výstupu a ruční zásah od opakovatelného vzorce. Správná struktura dělá sešit spolehlivějším než další efektní funkce.

# 3. Čištění a transformace: práce, kterou výsledek skrývá

## 3.1 Když počítač nevidí to, co člověk

Člověk snadno pozná, že `A203`, `a203` a `A203 ` pravděpodobně označují stejnou učebnu. Program může vidět tři různé texty. Podobně hodnoty `22,4`, `22.4` a `22,4 °C` mohou po importu skončit jako směs čísel a textu. **Čištění dat — data cleaning** převádí takové nepravidelnosti do konzistentní podoby, aniž by se ztratil jejich význam.

Nejprve je vhodné vytvořit profil dat: zkontrolovat počet řádků, datové typy, minimum a maximum, chybějící hodnoty, nečekané kategorie a duplicity. V našem projektu bude teplota 215 °C nápadná už při pohledu na maximum. Hodnota `-5 °C` v nevytápěné venkovní stanici může být správná, v obsazené učebně vyžaduje kontrolu. Číselná hranice sama o sobě nestačí; vždy potřebujeme věcný kontext.

Čištění není kosmetická příprava před „skutečnou“ analýzou. Rozhodnutí, zda hodnotu opravit, vynechat nebo ponechat, přímo ovlivňuje výsledek. Proto musí být změny dohledatelné.

## 3.2 Prázdná buňka není nula a dvojitý řádek nemusí být duplicita

Chybějící údaj může znamenat poruchu senzoru, neprovedené měření, odmítnutou odpověď nebo vlastnost, která pro daný záznam neexistuje. Nula je naproti tomu platná hodnota. Nahradíme-li každý výpadek měření nulou, vytvoříme v časové řadě umělé propady a snížíme průměr. Nejdříve je proto nutné rozlišit důvod chybění.

Podle účelu můžeme záznam vynechat, chybějící hodnotu ponechat, nebo ji odhadnout — provést **imputaci**. Odhad mediánem či sousední hodnotou může být užitečný, ale není to obnovené měření. Musí být označen a jeho vliv na závěr posouzen. U krátkého výpadku senzoru lze například zobrazit graf s odhadnutým bodem, ale pro vyhodnocení překročení bezpečnostní meze by bylo nepoctivé tvářit se, že bod skutečně existuje.

Stejnou opatrnost vyžadují duplicity. Dva totožné řádky mohou vzniknout dvojím importem, ale také dvěma skutečnými událostmi. O duplicitě rozhoduje klíč, tedy údaj nebo kombinace údajů, které mají být jedinečné. U měření to může být spojení `senzor_id + cas`; u objednávky `objednavka_id`. Odstranění „stejných řádků“ bez pochopení významu může smazat platná data.

## 3.3 Jednotky, kategorie a odlehlé hodnoty

Jedna tabulka může obsahovat energii ve watthodinách i kilowatthodinách, délku v metrech i centimetrech nebo cenu v různých měnách. Před porovnáním je nutné převést hodnoty na společnou jednotku a původní jednotku zdokumentovat. Stejně nebezpečné jsou nejednoznačné datumové zápisy: `03/04/2026` může znamenat 3. dubna i 4. března. Pro přenos dat je užitečný jednoznačný zápis `2026-04-03`.

Kategorie se sjednocují pomocí mapování. Hodnoty `lab`, `laboratoř` a `PC učebna` nemají být mechanicky sloučeny jen proto, že vypadají příbuzně; nejdříve musíme určit, zda opravdu znamenají stejný typ místnosti. Dobrá mapovací tabulka uchovává původní hodnotu i výslednou kategorii, takže je změna kontrolovatelná.

**Odlehlá hodnota — outlier** je výrazně vzdálená ostatním. Může být chybou, ale také nejdůležitějším zjištěním v celé sadě. Teplota 215 °C patrně vznikla posunutou desetinnou čárkou; prudký nárůst CO₂ během plně obsazené hodiny může být reálným signálem nedostatečného větrání. Odlehlé hodnoty lze hledat pomocí grafu, kvartilů, směrodatné odchylky nebo věcných mezí, ale žádná metoda sama nerozhodne, zda je máme odstranit.

## 3.4 Transformace vytváří proměnné, které umíme analyzovat

Čistá data ještě nemusí být ve tvaru vhodném pro otázku. Z časové značky můžeme odvodit hodinu, den v týdnu nebo měsíc; z příkonu a délky intervalu spotřebu; z počtu přítomných a objemu místnosti relativní obsazenost. Tak vznikají **odvozené proměnné**. Jejich vzorec musí být popsán, protože výsledek závisí na přijatých definicích.

Transformace může také rozdělit složený text, spojit dvě tabulky podle identifikátoru, převést širokou tabulku do dlouhého tvaru nebo agregovat minutová měření na hodinové hodnoty. Spojení podle jména je rizikové, protože dva lidé či objekty mohou mít stejný název. Stabilní jednoznačný identifikátor, například `ucebna_id`, omezuje nechtěná spojení. Tento princip už připomíná databázi: tabulkový procesor může obsahovat několik souvisejících tabulek, ale vztahy mezi nimi musí být jednoznačné.

## 3.5 Raw data se nepřepisují

Představme si, že každý týden stáhneme nový soubor, ručně odstraníme sloupce, opravíme data a přebarvíme výjimky. Při třetím týdnu už si nemusíme pamatovat přesné pořadí kroků. Nástroje jako Power Query nebo skript dokážou import a transformaci uložit jako opakovatelný postup. Obecný řetězec se označuje **ETL — Extract, Transform, Load**, tedy získat, transformovat a načíst data do cílového místa.

Bez ohledu na nástroj je vhodné zachovat **raw data — původní surová data** beze změny. Vedle nich vznikne vyčištěná verze a nad ní analýza. Jednoduchý projekt může mít složky `raw`, `clean`, `analysis` a soubor `README.md`, který vysvětlí původ, význam sloupců a provedené kroky. Pokud později zjistíme chybný převod jednotek, můžeme postup opravit a spustit znovu. U ručně přepsaného jediného souboru už původní hodnoty neobnovíme.

**Hlavní myšlenka:** Čištění není mazání všeho neobvyklého. Je to zdokumentované rozhodování o chybějících hodnotách, jednotkách, kategoriích a výjimkách tak, aby byl výsledek správný i opakovatelný.

# 4. Od souhrnu ke statistickému uvažování

## 4.1 Agregace odpovídá na otázku — a část detailu zahazuje

Tisíce pětiminutových měření nelze smysluplně číst řádek po řádku. **Agregace** je převádí na menší počet souhrnů: průměrnou teplotu podle učebny, nejvyšší CO₂ během hodiny nebo celkovou spotřebu za den. Každé shrnutí však něco ztrácí. Denní průměr může skrýt krátký, ale výrazný výkyv; součet spotřeby neukáže, kdy nastala odběrová špička.

Volba agregační funkce proto vychází z otázky. Pro celkovou energii použijeme součet, pro typickou teplotu střední hodnotu, pro překročení limitu maximum a pro počet měření počet záznamů. Počet řádků přitom není vždy počet objektů: jeden senzor vytváří mnoho měření a jedna učebna se opakuje v celé časové řadě.

## 4.2 Průměr bez rozdělení může lhát

Pět hodnot `20, 21, 22, 23, 34` má průměr 24, ale čtyři z pěti měření leží níže. **Aritmetický průměr** využívá všechny hodnoty a citlivě reaguje na extrémy. **Medián** je prostřední seřazená hodnota a bývá stabilnější u šikmých rozdělení. **Modus** označuje nejčastější hodnotu nebo kategorii. Ani jedna míra není obecně nejlepší; každá odpovídá na trochu jinou otázku.

Dvě učebny navíc mohou mít stejný průměr 22 °C, ale v jedné se teplota drží mezi 21,5 a 22,5 °C, zatímco ve druhé kolísá mezi 17 a 27 °C. Potřebujeme tedy popsat i **variabilitu**. Nejjednodušší je rozpětí `maximum − minimum`, odolnější pohled poskytují kvartily a **IQR — mezikvartilové rozpětí**, tedy rozdíl mezi třetím a prvním kvartilem. **Směrodatná odchylka** vyjadřuje, jak výrazně se hodnoty typicky rozptylují kolem průměru. Její význam je důležitější než ruční odvozování vzorce.

Tvar rozdělení dobře ukáže **histogram**, který číselné hodnoty seskupí do navazujících intervalů. Na rozdíl od běžného sloupcového grafu nezobrazuje samostatné kategorie, ale četnosti částí číselné osy. **Krabicový graf — box plot** zase stručně porovná medián, kvartily, rozsah a možné odlehlé hodnoty několika skupin.

## 4.3 Korelace je vodítko, nikoli rozsudek

Chceme zjistit, zda s rostoucí obsazeností roste i CO₂. Každé měření zobrazíme v **bodovém grafu**: na vodorovné ose bude počet osob, na svislé koncentrace. Pokud mrak bodů stoupá zleva doprava, existuje kladná souvislost. **Korelační koeficient** pro lineární vztah nabývá hodnot od −1 do +1; znaménko popisuje směr a velikost sílu lineární souvislosti.

Ani silná korelace však nedokazuje příčinu. Obsazenost i CO₂ mohou souviset s délkou hodiny a způsobem větrání. Dvě časové řady mohou růst současně pouze proto, že obě sledují dlouhodobý trend. Hodnota blízká nule navíc neznamená, že mezi proměnnými není žádný vztah; může být nelineární nebo skrytý ve skupinách.

Praktický omyl vzniká i při obrácení směru tvrzení. Z dat lze například vyčíst, že vysoké hodnoty CO₂ se častěji objevují v plných místnostech. Nelze z toho bez dalšího experimentu přesně určit, o kolik se hodnota sníží po určité změně větrání. Pozorovací data ukazují souvislosti, zatímco kauzální tvrzení vyžaduje silnější návrh studie a kontrolu dalších vlivů.

## 4.4 Vzorek, nejistota a přiměřená jistota

Každé měření obsahuje náhodnou i systematickou nejistotu. Náhodné výkyvy se při opakování mohou částečně vyrovnat; špatně kalibrovaný senzor však posouvá všechna měření stejným směrem a větší počet řádků tuto chybu neodstraní. Velká datová sada proto není automaticky kvalitní.

Při zobecnění ze vzorku na celou školu se ptáme, zda byly zastoupeny různé budovy, časy a typy výuky. Výsledek založený na dvou učebnách v říjnu nemusí platit v zimě ani v počítačové laboratoři. U grafu lze nejistotu či variabilitu zobrazit chybovými úsečkami, ale legenda musí říci, zda představují směrodatnou odchylku, chybu měření nebo interval spolehlivosti. Stejně vypadající úsečky mohou nést odlišný význam.

Statistické uvažování lze shrnout několika kontrolními otázkami:

1. Jak data vznikla a co v nich chybí?
2. Odpovídá souhrnná statistika položené otázce?
3. Jak rozptýlené a stabilní jsou hodnoty?
4. Nezaměňujeme souvislost za příčinu?
5. Na jakou populaci a období lze závěr rozumně vztáhnout?

**Hlavní myšlenka:** Statistika redukuje složitost, ale nevyrábí jistotu. Každý průměr, korelace i graf musí být čten spolu s rozdělením, původem dat a omezeními vzorku.

# 5. Graf jako odpověď, ne jako dekorace

## 5.1 Typ grafu vybírá otázka

Graf má zrychlit pochopení vztahu, který by se v tabulce hledal obtížně. Pro porovnání učeben podle průměrné spotřeby se hodí **sloupcový nebo pruhový graf**; vodorovné pruhy lépe pojmou delší názvy. Pro vývoj teploty během dne použijeme **spojnicový graf**, protože čas má přirozené pořadí. Pro vztah obsazenosti a CO₂ zvolíme bodový graf a pro rozdělení teplot histogram.

Výsečový graf může přehledně ukázat několik částí jednoho celku, pokud opravdu dávají 100 %. Při mnoha podobných podílech však člověk porovnává úhly hůře než délky, takže pruhový graf bývá čitelnější. Trojrozměrný efekt nepřidává další informaci; perspektiva naopak může velikosti zkreslit.

Spojnice v grafu také nese význam. U časové řady naznačuje průběh mezi okamžiky. Spojíme-li však body různých nesouvisejících učeben jen proto, že stojí vedle sebe v tabulce, vytvoříme vztah, který v datech neexistuje.

## 5.2 Čitelnost vzniká výběrem, ne zdobením

Dobrý graf má sdělný název, popsané osy, jednotky, rozumnou stupnici a jen tolik barev, kolik je potřeba k rozlišení významu. Název „Vývoj teploty v A203 během výuky“ je užitečnější než „Graf 1“. Pokud barva označuje učebnu, musí být použita konzistentně. Pokud zvýrazňuje jedinou důležitou výjimku, ostatní prvky mohou ustoupit do neutrálního odstínu.

U časové řady je důležité zachovat skutečné rozestupy. Hodnoty z ledna, února a června nemají ležet ve stejných vzdálenostech, jako by šlo o tři po sobě jdoucí měsíce. Velké množství popisků, mřížek a desetinných míst může zastínit hlavní sdělení. Zjednodušení však nesmí skrýt důležitou nejistotu nebo část dat.

**Dashboard** spojuje několik grafů a ukazatelů pro konkrétní rozhodnutí. Energetický přehled školy může ukázat dnešní spotřebu, vývoj za měsíc, největší odběr a porovnání budov. Není to nástěnka pro všechny dostupné grafy. Každý prvek má podporovat otázku člověka, který podle přehledu jedná.

## 5.3 Pravdivá data lze zobrazit zavádějícím způsobem

Rozdíl mezi 21,8 a 22,0 °C může vypadat dramaticky, pokud svislá osa začíná na 21,7. U sloupcového grafu, kde délka sloupce vyjadřuje velikost, je počátek na nule obvykle důležitý. U spojnicového grafu nemusí být nulový počátek vždy praktický, ale zvolený rozsah má být zřetelný a nesmí vytvářet falešné drama.

Výsledek lze ovlivnit také výběrem období, neobvyklým poměrem stran nebo dvojitou osou y. Dvě nesouvisející řady lze pomocí různých měřítek zarovnat tak, že působí téměř totožně. Graf přitom může obsahovat pouze pravdivá čísla. Manipulace vzniká způsobem výběru a zobrazení.

Před zveřejněním je proto užitečné provést jednoduchý test: porozuměl by čtenář měřítku, jednotkám a výběru dat bez ústního vysvětlení? Vidí také výjimky a nejistotu, které by mohly změnit závěr? Graf je zhuštěný argument a autor odpovídá za to, zda je poctivý.

## 5.4 Od analýzy k rozhodnutí

Výsledek projektu nemá znít „průměrná teplota byla 22,6 °C“. Smysluplná interpretace propojí číslo s otázkou, kontextem a omezeními: například „Učebna A203 měla během posledních dvou vyučovacích hodin podobnou teplotu jako ostatní místnosti, ale při vysoké obsazenosti v ní CO₂ rostlo rychleji. Data pocházejí ze tří říjnových týdnů, proto nepopisují zimní provoz.“

Takové sdělení odděluje **zjištění**, **možné vysvětlení** a **doporučení**. Zjištěním je pozorovaný růst. Vysvětlením může být nedostatečné větrání, ale je třeba jej ověřit. Doporučením může být kontrolované porovnání dvou režimů větrání a nové měření. Dobrá analýza tedy často nekončí definitivní odpovědí, ale přesnější další otázkou.

**Hlavní myšlenka:** Graf není ozdoba tabulky. Je to volba, co čtenář uvidí jako první, a proto musí odpovídat otázce, zachovat měřítko a otevřeně ukázat omezení výsledku.

# 6. Trend, predikce a odpovědný datový workflow

## 6.1 Model je užitečné zjednodušení

Časová řada může obsahovat dlouhodobý **trend**, pravidelnou **sezónnost** a krátkodobý šum. Spotřeba školy se mění s venkovní teplotou, rozvrhem, víkendy i prázdninami. Porovnání prosince s lednem proto nemusí dokazovat nový trend; může zachycovat běžný roční rytmus. U sezónních dat bývá výstižnější porovnat stejné období různých let.

Kolísavý průběh lze vyhladit **klouzavým průměrem**, který pro každý bod počítá průměr z několika sousedních období. Delší okno ukáže hladší trend, ale skryje více krátkých změn a reaguje se zpožděním. Ani vyhlazená křivka není „pravá hodnota“; je to další pohled na tatáž data.

Jednoduchá **lineární regrese** popisuje vztah přímkou `y = ax + b`. Koeficient `a` vyjadřuje sklon a `b` průsečík s osou. Model může například odhadovat spotřebu z venkovní teploty. Hodnota **R² — koeficient determinace** popisuje, jakou část variability sledovaných dat model zachycuje. Vysoké R² však nedokazuje příčinu ani nezaručuje úspěch v budoucnosti. Model může přesně vystihnout minulost a selhat po změně režimu vytápění.

## 6.2 Predikce není věštění

Použijeme-li model uvnitř rozsahu známých hodnot, mluvíme o **interpolaci**. Odhad mimo tento rozsah je **extrapolace** a bývá mnohem riskantnější. Vztah pozorovaný při venkovních teplotách od −5 do 15 °C nemusí pokračovat při −25 °C. Matematická přímka pokračuje bez váhání, i když se chování budovy nebo topného systému dávno změnilo.

Pro poctivé ověření predikce nestačí zjistit, jak dobře model popisuje data, na nichž vznikl. Část záznamů použijeme jako **trénovací data** pro nastavení modelu a jinou část jako **testovací data** pro kontrolu na dosud neviděných případech. Je to podobné jako učení na známé sadě otázek: bez nového testu nepoznáme, zda člověk pochopil princip, nebo si zapamatoval odpovědi.

Když je model příliš přizpůsoben detailům trénovací sady a na nových datech selhává, jde o **přeučení — overfitting**. U časových řad navíc nesmíme náhodně promíchat budoucí záznamy do tréninku a minulost ponechat pro test; model by získal informaci, kterou v okamžiku skutečné predikce nemá. Nejdůležitější otázka nakonec nezní „Jak složitý model umíme vytvořit?“, ale „Je jeho chyba dost malá pro rozhodnutí, které na něm chceme založit?“

## 6.3 Kdy tabulka přestává stačit

Tabulkový procesor je výborný pro průzkum, výpočty a komunikaci menších až středních datových úloh. S rostoucím objemem, počtem zdrojů a požadavkem na opakování však roste riziko ručních chyb. Databáze lépe spravuje sdílená strukturovaná data a vztahy, Power Query opakuje importní a transformační kroky a jazyky jako Python s knihovnou pandas umožňují zpracovat více souborů, verzovat postup a vytvářet složitější analýzy.

Nejde o soutěž nástrojů. Praktický workflow může začít rychlým průzkumem CSV v tabulkovém procesoru, pokračovat automatizovaným čištěním a skončit přehledným reportem opět v sešitu. Přechod k jinému nástroji dává smysl tehdy, když ruční postup přestává být kontrolovatelný, opakovatelný nebo dostatečně výkonný.

## 6.4 AI asistent musí ukázat práci

AI může navrhnout vzorec, vysvětlit chybu, vytvořit skript, shrnout tabulku nebo doporučit graf. Tím zrychluje práci, ale nemá přístup k žádné skryté „správné odpovědi“. Může zaměnit význam sloupce, použít chybný rozsah, přehlédnout výběrové zkreslení nebo přesvědčivě tvrdit kauzalitu z pouhé korelace.

Rozumné použití proto připomíná spolupráci s rychlým, ale ne vždy spolehlivým pomocníkem. Zadání má obsahovat význam dat a očekávaný výsledek. Navržený vzorec otestujeme na několika ručně spočítaných případech, zkontrolujeme chování u prázdných a krajních hodnot a porovnáme souhrny se zdrojem. U skriptu uchováme vstup i kód, aby šel výsledek zopakovat. Citlivá data se do externí AI služby nevkládají bez oprávnění a znalosti podmínek zpracování.

AI tedy nemění základní pravidla datové práce. Naopak zvyšuje cenu porozumění: čím snazší je vytvořit složitě vypadající analýzu, tím důležitější je umět ověřit její vstupy, metodu a závěr.

## 6.5 Soukromí, etika a reprodukovatelnost

Školní data mohou obsahovat jména, výsledky, docházku, polohu nebo jiné osobní údaje. Základním principem je **minimalizace dat**: sbíráme jen údaje skutečně potřebné pro vymezený účel, přístup dáváme jen oprávněným lidem a data neuchováváme déle, než je nutné. Pro analýzu prostředí obvykle nepotřebujeme jména žáků; stačí počet přítomných.

**Pseudonymizace** nahrazuje přímý identifikátor kódem, ale pokud lze člověka znovu určit pomocí odděleného klíče nebo kombinace dalších údajů, stále jde o osobní data. **Anonymizace** má být nevratná v rozumně očekávatelných podmínkách, což je obtížnější, než pouhé smazání sloupce se jménem. Kombinace třídy, věku, času a neobvyklé události může člověka odhalit i bez jména.

Odpovědnost se týká také způsobu použití výsledku. Model založený na minulých datech může přenášet dřívější nerovnosti. Dashboard může skrýt menšinovou skupinu v celkovém průměru. Automatické rozhodnutí proto potřebuje lidskou kontrolu, možnost zpochybnění a dokumentaci toho, z jakých dat vzniklo.

Dobře odevzdaný datový projekt neobsahuje jen finální graf. Uchovává původní data, vyčištěnou verzi, vzorce nebo skript, popis proměnných a stručný `README`, který vysvětlí postup, rozhodnutí při čištění a omezení. Jiný člověk by měl být schopen zjistit, odkud výsledek pochází, a analýzu v rozumné míře zopakovat. **Reprodukovatelnost** není administrativní přítěž; je to praktická ochrana proti vlastním omylům.

**Hlavní myšlenka:** Predikce je podmíněný odhad, nikoli věštba. Odpovědný workflow odděluje data, postup a výstup, testuje model na nových případech, chrání soukromí a ponechává člověku kontrolu nad závěrem.

# Závěrečné propojení

Příběh školních učeben ukazuje, proč práce s daty není posloupnost izolovaných funkcí. Otázka rozhodne, co budeme měřit. Způsob měření určí, jaké zkreslení může vzniknout. Struktura tabulky ovlivní, zda lze data spolehlivě filtrovat a spojovat. Čištění změní, které záznamy vstoupí do analýzy. Statistická metoda určí, co ze složitosti zachováme, a graf rozhodne, co uvidí příjemce jako první. Predikce pak přidá předpoklad, že určitá část minulého vztahu bude platit i dál.

Celý proces lze shrnout dvěma propojenými řetězci:

**otázka → sběr → metadata → struktura → čištění → analýza → vizualizace → interpretace**

**trend → model → test → predikce → rozhodnutí → nové měření**

Druhý řetězec nekončí definitivní pravdou, ale návratem k datům. Po změně větrání nebo vytápění znovu měříme, porovnáme očekávání se skutečností a model opravíme. Datová práce je proto cyklus učení.

Tabulkový procesor v něm zůstává první praktickou laboratoří. Učí přesně formulovat vztahy pomocí vzorců, oddělit hodnotu od zobrazení, změnit pohled bez přepisování zdroje a rychle prověřit hypotézu. Jakmile však data přerostou možnosti ruční kontroly, stejný mentální model pokračuje v databázích, transformačních nástrojích, programování i strojovém učení.

Nejcennější dovedností tedy není zapamatovat si všechny funkce. Je to schopnost položit dobrou otázku, poznat omezení dat, vytvořit kontrolovatelný postup a tvrdit jen to, co výsledek opravdu podporuje.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
