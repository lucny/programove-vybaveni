## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Když počítač nevidí to, co člověk**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
Člověk snadno pozná, že `A203`, `a203` a `A203 ` pravděpodobně označují stejnou učebnu. Program může vidět tři různé texty. Podobně hodnoty `22,4`, `22.4` a `22,4 °C` mohou po importu skončit jako směs čísel a textu. **Čištění dat — data cleaning** převádí takové nepravidelnosti do konzistentní podoby, aniž by se ztratil jejich význam.

Nejprve je vhodné vytvořit profil dat: zkontrolovat počet řádků, datové typy, minimum a maximum, chybějící hodnoty, nečekané kategorie a duplicity. V našem projektu bude teplota 215 °C nápadná už při pohledu na maximum. Hodnota `-5 °C` v nevytápěné venkovní stanici může být správná, v obsazené učebně vyžaduje kontrolu. Číselná hranice sama o sobě nestačí; vždy potřebujeme věcný kontext.

Čištění není kosmetická příprava před „skutečnou“ analýzou. Rozhodnutí, zda hodnotu opravit, vynechat nebo ponechat, přímo ovlivňuje výsledek. Proto musí být změny dohledatelné.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Prázdná buňka není nula a dvojitý řádek nemusí být duplicita**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Chybějící údaj může znamenat poruchu senzoru, neprovedené měření, odmítnutou odpověď nebo vlastnost, která pro daný záznam neexistuje. Nula je naproti tomu platná hodnota. Nahradíme-li každý výpadek měření nulou, vytvoříme v časové řadě umělé propady a snížíme průměr. Nejdříve je proto nutné rozlišit důvod chybění.

Podle účelu můžeme záznam vynechat, chybějící hodnotu ponechat, nebo ji odhadnout — provést **imputaci**. Odhad mediánem či sousední hodnotou může být užitečný, ale není to obnovené měření. Musí být označen a jeho vliv na závěr posouzen. U krátkého výpadku senzoru lze například zobrazit graf s odhadnutým bodem, ale pro vyhodnocení překročení bezpečnostní meze by bylo nepoctivé tvářit se, že bod skutečně existuje.

Stejnou opatrnost vyžadují duplicity. Dva totožné řádky mohou vzniknout dvojím importem, ale také dvěma skutečnými událostmi. O duplicitě rozhoduje klíč, tedy údaj nebo kombinace údajů, které mají být jedinečné. U měření to může být spojení `senzor_id + cas`; u objednávky `objednavka_id`. Odstranění „stejných řádků“ bez pochopení významu může smazat platná data.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jednotky, kategorie a odlehlé hodnoty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jedna tabulka může obsahovat energii ve watthodinách i kilowatthodinách, délku v metrech i centimetrech nebo cenu v různých měnách. Před porovnáním je nutné převést hodnoty na společnou jednotku a původní jednotku zdokumentovat. Stejně nebezpečné jsou nejednoznačné datumové zápisy: `03/04/2026` může znamenat 3. dubna i 4. března. Pro přenos dat je užitečný jednoznačný zápis `2026-04-03`.

Kategorie se sjednocují pomocí mapování. Hodnoty `lab`, `laboratoř` a `PC učebna` nemají být mechanicky sloučeny jen proto, že vypadají příbuzně; nejdříve musíme určit, zda opravdu znamenají stejný typ místnosti. Dobrá mapovací tabulka uchovává původní hodnotu i výslednou kategorii, takže je změna kontrolovatelná.

**Odlehlá hodnota — outlier** je výrazně vzdálená ostatním. Může být chybou, ale také nejdůležitějším zjištěním v celé sadě. Teplota 215 °C patrně vznikla posunutou desetinnou čárkou; prudký nárůst CO₂ během plně obsazené hodiny může být reálným signálem nedostatečného větrání. Odlehlé hodnoty lze hledat pomocí grafu, kvartilů, směrodatné odchylky nebo věcných mezí, ale žádná metoda sama nerozhodne, zda je máme odstranit.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Transformace vytváří proměnné, které umíme analyzovat**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Čistá data ještě nemusí být ve tvaru vhodném pro otázku. Z časové značky můžeme odvodit hodinu, den v týdnu nebo měsíc; z příkonu a délky intervalu spotřebu; z počtu přítomných a objemu místnosti relativní obsazenost. Tak vznikají **odvozené proměnné**. Jejich vzorec musí být popsán, protože výsledek závisí na přijatých definicích.

Transformace může také rozdělit složený text, spojit dvě tabulky podle identifikátoru, převést širokou tabulku do dlouhého tvaru nebo agregovat minutová měření na hodinové hodnoty. Spojení podle jména je rizikové, protože dva lidé či objekty mohou mít stejný název. Stabilní jednoznačný identifikátor, například `ucebna_id`, omezuje nechtěná spojení. Tento princip už připomíná databázi: tabulkový procesor může obsahovat několik souvisejících tabulek, ale vztahy mezi nimi musí být jednoznačné.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 3.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Raw data se nepřepisují**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Představme si, že každý týden stáhneme nový soubor, ručně odstraníme sloupce, opravíme data a přebarvíme výjimky. Při třetím týdnu už si nemusíme pamatovat přesné pořadí kroků. Nástroje jako Power Query nebo skript dokážou import a transformaci uložit jako opakovatelný postup. Obecný řetězec se označuje **ETL — Extract, Transform, Load**, tedy získat, transformovat a načíst data do cílového místa.

Bez ohledu na nástroj je vhodné zachovat **raw data — původní surová data** beze změny. Vedle nich vznikne vyčištěná verze a nad ní analýza. Jednoduchý projekt může mít složky `raw`, `clean`, `analysis` a soubor `README.md`, který vysvětlí původ, význam sloupců a provedené kroky. Pokud později zjistíme chybný převod jednotek, můžeme postup opravit a spustit znovu. U ručně přepsaného jediného souboru už původní hodnoty neobnovíme.

**Hlavní myšlenka:** Čištění není mazání všeho neobvyklého. Je to zdokumentované rozhodování o chybějících hodnotách, jednotkách, kategoriích a výjimkách tak, aby byl výsledek správný i opakovatelný.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
