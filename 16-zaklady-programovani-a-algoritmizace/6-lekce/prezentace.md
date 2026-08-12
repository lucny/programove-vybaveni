## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Správné řešení nemusí být dobré řešení**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při programování je nejdůležitější, aby program dával správný výsledek. Tím ale práce programátora často nekončí. Stejný problém totiž můžeme vyřešit několika různými způsoby a některé z nich mohou být výrazně rychlejší, úspornější nebo jednodušší.

Představme si například seznam tisíce jmen, ve kterém chceme najít konkrétní osobu. Nejjednodušší postup je začít od prvního jména a postupně kontrolovat jedno po druhém, dokud hledané jméno nenajdeme.

Takový algoritmus je správný. Pokud ale máme seznam milionu položek a vyhledávání provádíme mnohokrát za sekundu, může být příliš pomalý.

Programátor proto obvykle řeší dvě různé otázky:

1. **Funguje algoritmus správně?**
2. **Je jeho způsob řešení dostatečně efektivní?**

Efektivita neznamená pouze rychlost. Program může například pracovat velmi rychle, ale spotřebovávat příliš mnoho paměti. Jiný může být o něco pomalejší, ale výrazně jednodušší a spolehlivější.

V praxi proto často hledáme rozumný kompromis mezi několika vlastnostmi:

- rychlostí,
- spotřebou paměti,
- jednoduchostí,
- čitelností,
- snadností údržby.

U malého školního programu bývá nejlepší jednoduché a přehledné řešení. U rozsáhlé aplikace, která zpracovává miliony položek, už může mít volba algoritmu zásadní význam.

Příklad:

Máme seznam 20 čísel a chceme zjistit největší hodnotu.

Nejjednodušší postup je projít seznam od začátku do konce a průběžně si pamatovat největší nalezené číslo.

```python
cisla = [8, 3, 15, 4, 12]

maximum = cisla[0]

for cislo in cisla:
    if cislo > maximum:
        maximum = cislo

print(maximum)
```

Takový algoritmus je jednoduchý, přehledný a zároveň efektivní. Nemusíme čísla nejprve třídit, protože ke zjištění maxima stačí jediný průchod seznamem.

To je dobrý příklad situace, kdy lepší algoritmus nemusí znamenat složitější algoritmus.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak přibližně měřit náročnost algoritmu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Když chceme porovnat dva algoritmy, nestačí pouze spustit oba programy a změřit čas stopkami. Výsledek by totiž závisel na konkrétním počítači, rychlosti procesoru, momentálním zatížení systému i použitém programovacím jazyce.

Mnohem užitečnější je sledovat, jak se počet potřebných operací mění s velikostí vstupních dat.

Představme si dvě situace.

V první hledáme číslo v neuspořádaném seznamu:

```python
for cislo in seznam:
    if cislo == hledane:
        print("Nalezeno")
        break
```

Pokud má seznam deset prvků, může být potřeba zkontrolovat až deset hodnot.

Pokud má seznam tisíc prvků, může být potřeba zkontrolovat až tisíc hodnot.

Pokud má seznam milion prvků, může být potřeba zkontrolovat až milion hodnot.

Počet operací tedy roste přibližně stejně rychle jako počet prvků.

To je důležitější informace než údaj „program běžel 0,002 sekundy“.

U některých algoritmů roste počet operací rychleji.

Představme si například, že chceme porovnat každý prvek seznamu se všemi ostatními:

```python
for a in seznam:
    for b in seznam:
        print(a, b)
```

Pro deset prvků vznikne přibližně sto dvojic.

Pro sto prvků už deset tisíc.

Pro tisíc prvků milion.

Právě zde se ukazuje, proč mohou být dva programy na malých datech stejně rychlé, ale při větších datech se jeden z nich začne dramaticky zpomalovat.

Programátoři proto při hodnocení algoritmu často sledují hlavně dvě věci:

**časovou náročnost** — kolik práce musí program vykonat,

**paměťovou náročnost** — kolik dodatečné paměti při tom potřebuje.

Pro běžnou programátorskou praxi není nutné vždy provádět přesné matematické výpočty. Často stačí umět rozpoznat, zda algoritmus prochází data jednou, několikrát, nebo například používá vnořené cykly.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Co znamená O(1), O(n) a O(n²)**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Pro přibližný popis růstu náročnosti se používá takzvaná **asymptotická složitost**, obvykle zapisovaná pomocí symbolu **O**.

Není potřeba chápat tento zápis jako přesný výpočet času. Vyjadřuje především, jak se množství práce mění při zvětšování vstupu.

### Konstantní čas — O(1)

Představme si pole:

```python
cisla = [10, 20, 30, 40, 50]
print(cisla[3])
```

Chceme-li získat prvek na známé pozici, program se k němu může dostat přímo.

Je téměř jedno, zda pole obsahuje deset prvků nebo milion. Pokud známe index, přístup k jednomu konkrétnímu prvku trvá přibližně stejně dlouho.

Tomuto typu operace říkáme **O(1)**.

Neznamená to, že operace trvá přesně jednu instrukci. Znamená to, že její náročnost se zásadně nezvětšuje s počtem prvků.

### Lineární čas — O(n)

Při hledání hodnoty v neuspořádaném seznamu můžeme být nuceni projít všechny prvky:

```python
for cislo in seznam:
    if cislo == hledane:
        break
```

Čím více prvků máme, tím více kontrol může být potřeba.

Pro 100 položek maximálně přibližně 100 kontrol, pro 10 000 položek přibližně 10 000.

Takové chování označujeme jako **O(n)**.

### Kvadratický čas — O(n²)

U vnořených cyklů může počet operací růst mnohem rychleji:

```python
for a in seznam:
    for b in seznam:
        print(a, b)
```

Máme-li `n` prvků, vnější cyklus proběhne `n`krát a při každém průchodu proběhne vnitřní cyklus také `n`krát.

Celkem tedy přibližně:

`n × n = n²`

Takový algoritmus označujeme jako **O(n²)**.

Rozdíl se nejlépe ukáže na větších datech:

| Počet prvků | O(n) | O(n²) |
|---:|---:|---:|
| 10 | 10 | 100 |
| 100 | 100 | 10 000 |
| 1 000 | 1 000 | 1 000 000 |
| 10 000 | 10 000 | 100 000 000 |

To vysvětluje, proč může program fungovat bez problémů při testu na deseti položkách, ale při zpracování skutečných dat být nepoužitelně pomalý.

Pro základní představu stačí pamatovat:

**O(1)** — množství práce se prakticky nemění,

**O(n)** — práce roste přibližně stejně jako množství dat,

**O(n²)** — práce roste velmi rychle, často kvůli vnořeným průchodům stejnými daty.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Lineární a binární vyhledávání**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Velmi názorným příkladem rozdílu mezi algoritmy je hledání určité hodnoty.

Představme si telefonní seznam seřazený podle příjmení.

Mohli bychom začít od první stránky a číst všechna jména jedno po druhém. To by odpovídalo **lineárnímu vyhledávání**.

Pokud hledáme jméno „Novák“, intuitivně ale otevřeme seznam přibližně uprostřed. Jestliže tam vidíme jména začínající na P, víme, že Novák musí být dříve. Z poloviny seznamu tedy okamžitě můžeme polovinu možností zahodit.

Stejný princip používá **binární vyhledávání**.

Mějme seřazený seznam:

```text
3  7  11  18  24  31  42  56  70
```

Hledáme číslo `31`.

Nejprve se podíváme doprostřed:

```text
3  7  11  18  [24]  31  42  56  70
```

31 je větší než 24, takže levou polovinu už nemusíme kontrolovat.

Zbývá:

```text
31  42  56  70
```

Opět zvolíme střední oblast a pokračujeme, dokud hodnotu nenajdeme.

Velká výhoda spočívá v tom, že při každém kroku zahodíme přibližně polovinu zbývajících možností.

U milionu seřazených položek nemusí binární vyhledávání projít milion hodnot. Stačí přibližně několik desítek kroků.

Tento způsob chování se označuje jako **O(log n)**.

Pro středoškolskou úroveň není důležité počítat logaritmy. Podstatná je myšlenka:

**lineární vyhledávání zmenšuje problém po jedné položce, zatímco binární vyhledávání jej zmenšuje přibližně na polovinu.**

Binární vyhledávání má ale jednu zásadní podmínku: data musí být **seřazená**.

To ukazuje důležitou vlastnost algoritmů — rychlejší řešení často vyžaduje nějakou přípravu nebo splnění určité podmínky.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Třídění jako příklad různě dobrých algoritmů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Třídění znamená uspořádání hodnot podle určitého pravidla, například od nejmenšího po největší.

Jedním z nejjednodušších třídicích algoritmů je **bubble sort**.

Jeho princip můžeme přirovnat k tomu, že opakovaně procházíme řadu čísel a porovnáváme sousední dvojice. Pokud jsou ve špatném pořadí, prohodíme je.

Například:

```text
5  2  8  1
```

Porovnáme 5 a 2:

```text
2  5  8  1
```

Porovnáme 5 a 8 — jsou správně.

Porovnáme 8 a 1:

```text
2  5  1  8
```

Největší číslo se tak během jednoho průchodu postupně „posune“ doprava. Celý postup je nutné několikrát opakovat.

Bubble sort je výborný pro pochopení principu třídění, protože je jednoduchý. U velkých seznamů ale není příliš efektivní.

Jeho typická časová náročnost je přibližně **O(n²)**.

Moderní programovací jazyky proto používají mnohem promyšlenější třídicí algoritmy.

Například v Pythonu běžně stačí:

```python
cisla = [5, 2, 8, 1]
cisla.sort()

print(cisla)
```

Výstup:

```text
[1, 2, 5, 8]
```

Programátor přitom nemusí implementovat vlastní třídicí algoritmus. Vestavěná funkce používá velmi účinné řešení.

To přináší důležitou praktickou zásadu:

**Pokud programovací jazyk nebo kvalitní knihovna nabízí dobře otestovaný algoritmus, bývá lepší jej použít než vytvářet vlastní verzi bez důvodu.**

Znalost jednoduchých třídicích algoritmů je ale stále důležitá, protože na nich lze dobře pochopit způsob práce algoritmu a rozdíly v efektivitě.

***

## Snímek 6.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rychlost není jediným kritériem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při výběru algoritmu bychom neměli automaticky hledat pouze nejrychlejší možné řešení.

Představme si program, který jednou za den zpracuje seznam třiceti studentů. Rozdíl mezi algoritmem, který úlohu dokončí za jednu tisícinu sekundy, a algoritmem, který ji dokončí za deset tisícin sekundy, není prakticky důležitý.

Pokud je druhé řešení výrazně jednodušší a přehlednější, může být dokonce lepší.

Naopak u internetové služby, která zpracovává miliony požadavků, může být i malé zrychlení velmi významné.

Programátor proto musí zohlednit kontext.

### Čitelnost versus rychlost

Velmi optimalizovaný kód může být obtížně pochopitelný.

```python
vysledek = sum(x*x for x in data if x > 0)
```

Pro zkušeného programátora může být zápis přehledný, ale začátečník může lépe chápat rozepsanou variantu:

```python
vysledek = 0

for x in data:
    if x > 0:
        vysledek = vysledek + x * x
```

Pokud obě řešení dostatečně rychle splní požadovaný úkol, může být důležitější zvolit kód, kterému tým dobře rozumí.

### Rychlost versus paměť

Někdy lze výpočet urychlit tím, že si předem uložíme další data.

Například internetový obchod může mít informace o milionech výrobků. Místo toho, aby při každém hledání procházel všechny položky, může používat speciální index.

Vyhledávání je potom rychlejší, ale index zabírá další místo.

Podobný princip využívají databáze i vyhledávače.

### Příprava versus opakované použití

Představme si seznam milionu čísel.

Pokud v něm chceme najít jednu jedinou hodnotu, nemusí mít smysl celý seznam nejprve třídit.

Pokud v něm ale budeme vyhledávat tisíckrát, může se vyplatit seznam jednou seřadit a potom používat binární vyhledávání.

Jinými slovy:

**někdy investujeme více práce na začátku, abychom pozdější operace výrazně urychlili.**

Takový kompromis se v informatice objevuje velmi často.

***

## Snímek 6.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak poznat zbytečně pomalý program**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při běžném programování není nutné u každé funkce počítat složitost pomocí matematických vzorců. Stačí si vytvořit několik praktických návyků.

První varovný signál představují **vnořené cykly nad velkým množstvím dat**.

Například:

```python
for student in studenti:
    for zaznam in vsechny_zaznamy:
        ...
```

Pokud máme deset studentů a sto záznamů, není to problém.

Pokud máme sto tisíc studentů a milion záznamů, situace je úplně jiná.

Druhým varovným signálem je **opakované provádění stejného výpočtu**, jehož výsledek se nemění.

Například:

```python
for x in data:
    prumer = vypocitej_prumer(data)
    ...
```

Pokud `vypocitej_prumer(data)` pokaždé počítá stejnou hodnotu, je zbytečné jej volat při každém průchodu.

Lepší je:

```python
prumer = vypocitej_prumer(data)

for x in data:
    ...
```

Třetím signálem je výběr nevhodné datové struktury.

Pokud například často hledáme, zda určitá hodnota existuje mezi velkým množstvím položek, může být vhodnější použít množinu než obyčejný seznam.

```python
povolena_id = {12, 18, 25, 41}

if id_uzivatele in povolena_id:
    print("Přístup povolen")
```

Vhodný algoritmus a vhodná datová struktura spolu často úzce souvisejí.

Proto se programátor neptá pouze:

> Jak tento úkol naprogramuji?

ale také:

> Jaký způsob reprezentace dat mi tento úkol usnadní?

***

## Snímek 6.8

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Teorie a skutečný výkon programu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Zápis typu O(n) nebo O(n²) je velmi užitečný, ale neříká přesně, jak dlouho bude program běžet.

Dva algoritmy mohou mít stejnou teoretickou složitost a přesto být v praxi různě rychlé.

Výkon ovlivňuje například:

- programovací jazyk,
- použitý překladač nebo interpret,
- rychlost procesoru,
- množství operační paměti,
- způsob uložení dat,
- použité knihovny,
- práce s diskem nebo sítí.

Jedna operace načtení dat z disku může například trvat výrazně déle než mnoho jednoduchých aritmetických operací procesoru.

Proto se při skutečné optimalizaci používá také **měření výkonu**.

Programátor může například zjistit, která část programu zabírá nejvíce času, a zaměřit se právě na ni.

Tomu se říká **profilování — profiling**.

Pro základní programování je ale důležitější jiná zásada:

> Nejprve napiš správný a srozumitelný program. Optimalizuj až tehdy, když víš, že výkon skutečně představuje problém.

Předčasná optimalizace může vést ke složitějšímu kódu bez skutečného přínosu.

## Závěrečné propojení

Algoritmus není pouze postup, který vede ke správnému výsledku. Při skutečném programování nás zajímá také to, kolik práce musí počítač vykonat a jak se tato práce změní při větším množství dat.

Jednoduchý mentální model může vypadat takto:

**problém → návrh algoritmu → správnost → náročnost → implementace → měření → případné zlepšení**

U malých úloh bývá často nejlepší jednoduché a čitelné řešení. S rostoucím množstvím dat ale může volba algoritmu rozhodnout o tom, zda program dokončí úlohu za zlomek sekundy, několik minut, nebo prakticky nikdy.

Nejdůležitější proto není umět zpaměti seznam složitostí různých algoritmů. Podstatné je naučit se klást otázku:

**Jak se bude množství práce měnit, když bude vstupních dat desetkrát, tisíckrát nebo milionkrát více?**

Právě tato otázka vede od pouhého psaní programů k algoritmickému uvažování.

***
