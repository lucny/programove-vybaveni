# Základy programování a algoritmizace

# 1. Základní pojmy z programování

## 1.1 Počítačový program

Program v obecném smyslu je scénář kroků (instrukcí), které vedou k dosažení určitého cíle.

> **Příklad**
>
> Například program poznávacího výletu může obsahovat kroky jako: vstát, nasnídat se, sbalit si věci, vyrazit na autobusové nádraží, nastoupit do autobusu a dorazit do cíle.

Počítačový program je soubor instrukcí sestavených tak, aby je mohl vykonat počítač, konkrétně procesor. Tyto instrukce jsou napsány v programovacím jazyce (tzv. zdrojový kód), který je srozumitelný pro člověka, ale musí být přeložen do strojového jazyka (binárního kódu), kterému rozumí procesor. Většina programů je určena k řešení konkrétního problému nebo úkolu, například:

- zpracování dat,
- řízení hardwaru,
- komunikaci s uživatelem,
- provádění výpočtů.
> **Příklad**
>
> Příkladem jednoduchého programu může být kalkulačka, která přijímá vstupy zadané uživatelem, provádí výpočty podle určitého algoritmu a zobrazuje výstupy.

## 1.2 Algoritmus

Algoritmus je přesný a konečný postup řešení určitého problému nebo úkolu, který je popsán pomocí jednotlivých kroků (instrukcí).

> **Poznámka**
>
> Slovo algoritmus pochází z latinského přepisu jména perského matematika al-Chvárizmího (9. století).

Algoritmy mohou být vyjádřeny různými způsoby, například:

- přirozeným jazykem,
- vývojovým diagramem,
- pseudokódem. Obecně můžeme za algoritmus považovat jakýkoliv postup, který splňuje následující
kritéria:

- Konečnost – algoritmus má jasně definovaný začátek a konec.
- Definovanost – každý krok algoritmu je jednoznačně určen.
- Vstupy – algoritmus může pracovat se vstupními daty.
- Výstupy – algoritmus produkuje výsledky své činnosti.
> **Příklad**
>
> Mini příklad algoritmu (bez programování): „Uvař čaj”

- Nalij vodu do konvice.
- Zapni konvici.
- Do hrnku dej sáček.
- Zalij vroucí vodou.
- Počkej 3–5 minut.
- Vyjmi sáček.

## 1.3 Programovací jazyk

Přirozený jazyk je jazyk, kterým lidé běžně komunikují (např. čeština, angličtina). Tyto jazyky jsou však pro počítače příliš složité a nejednoznačné. Programovací jazyk je formální jazyk určený k psaní počítačových programů. Umožňuje programátorům komunikovat s počítačem a vyjadřovat algoritmy a logiku pomocí přesně definovaných instrukcí. Každý programovací jazyk má:

- syntaxi – pravidla zápisu příkazů,
- sémantiku – význam jednotlivých příkazů. Existuje mnoho různých programovacích jazyků, které se liší svým určením a oblastí
použití, například:

- webový vývoj – JavaScript (HTML a CSS jako doplňkové jazyky),
- vědecké výpočty a data – Python, R,
- systémové programování – C, C++,
- mobilní aplikace – Swift, Kotlin.
> **Poznámka**
>
> HTML a CSS nejsou plnohodnotné programovací jazyky, ale značkovací a stylovací jazyky, které se používají společně s programovacími jazyky při tvorbě webových stránek.

## 1.4 Překladače

Počítač neumí přímo vykonávat programy napsané ve vyšších programovacích jazycích, proto je potřeba je přeložit do strojového jazyka (binárního kódu). Tento proces se nazývá překlad a provádějí jej speciální programy nazývané překladače.

Rozlišujeme dva základní typy překladačů:

- Kompilátor Překládá celý zdrojový kód najednou do strojového kódu, který je uložen jako samostatný spustitelný soubor. Příklady kompilovaných jazyků: C, C++, Go.
- Interpret Překládá a zároveň vykonává zdrojový kód řádek po řádku během běhu programu. Příklady interpretovaných jazyků: Python, JavaScript, Ruby. Moderní programovací jazyky často kombinují oba přístupy. Například:
- Java se kompiluje do tzv. bytecode, který je následně vykonáván virtuálním strojem JVM.
- Python může zdrojový kód převést do bytecode, který následně vykonává virtuální stroj interpretu Pythonu. Bytecode představuje mezikrok mezi zdrojovým kódem a strojovým kódem. Umožňuje lepší přenositelnost programů mezi různými platformami, protože bytecode lze spustit
na libovolném zařízení s odpovídajícím interpretem nebo virtuálním strojem.

# 2. Vývoj programování, nižší a vyšší programovací jazyky

## 2.1 Historický vývoj programování

Počátky programování úzce souvisí s vývojem výpočetní techniky. První počítače byly konstruovány pro řešení konkrétních výpočetních úloh a jejich programování bylo velmi složité a časově náročné. Například první programy pro počítač ENIAC byly zadávány pomocí přepínačů a kabelů. V nejranějších fázích se programy zapisovaly přímo ve strojovém kódu, tedy jako posloupnosti nul a jedniček. Tento způsob programování byl velmi nepřehledný, náchylný k chybám a silně závislý na konkrétním typu procesoru. Postupně vznikly assemblerové jazyky, které umožnily zapisovat strojové instrukce pomocí symbolických názvů (mnemotechnických zkratek). Přesto zůstávalo programování stále úzce svázané s konkrétním hardwarem. S rozvojem výpočetní techniky a rostoucí složitostí programů začaly vznikat vyšší programovací jazyky, které se snažily přiblížit způsob zápisu lidskému myšlení. Tyto jazyky umožnily:

- zvyšovat produktivitu programátorů,
- psát přehlednější a lépe udržovatelný kód,
- vytvářet přenositelnější programy. Mezi historicky významné vyšší programovací jazyky patří například Fortran, COBOL, Pascal nebo C. Tyto jazyky položily základy moderního programování a mnohé jejich principy se používají dodnes.

## 2.2 Nižší a vyšší programovací jazyky

Programovací jazyky lze rozdělit podle úrovně abstrakce na nižší a vyšší. Nižší programovací jazyky jsou velmi blízké hardwaru a umožňují přímou kontrolu nad chodem počítače. V současnosti se používají méně často, ale stále jsou důležité pro specifické úlohy, jako je vývoj operačních systémů, ovladačů nebo vestavěných systémů. Typické vlastnosti:

- silná vazba na konkrétní procesor nebo architekturu,
- vysoký výkon a efektivita,
- složitější zápis a horší čitelnost kódu. Příklady nižších jazyků:
- strojový jazyk – přímý binární kód vykonávaný procesorem,
- assembler – jazyk blízký strojovému kódu, jedna instrukce odpovídá jedné strojové instrukci, ale oproti strojovému kódu používá symbolické názvy pro instrukce a adresy. Ukázka assemblerového kódu (pro x86 architekturu):
```asm
MOV AX, 5           ; Načti hodnotu 5 do registru AX
ADD AX, 10          ; Přičti hodnotu 10 k registru AX
MOV BX, AX          ; Přesuň hodnotu z registru AX do registru BX
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

## 2.3 Typy moderních programovacích jazyků

Moderní programovací jazyky lze rozdělit podle různých hledisek. Jedním z nejpoužívanějších je rozdělení podle oblasti použití, dalším kritériem může být paradigma programování (procedurální, objektově orientované, funkcionální, logické), použitá syntaktická struktura (blokové jazyky, značkovací jazyky), případně úroveň abstrakce (nízkoúrovňové vs. vysokoúrovňové jazyky).

- Programovací jazyky pro webový vývoj – JavaScript – klientská i serverová část webu, – PHP – serverové webové aplikace, – Python – backend, webové frameworky.
- Programovací jazyky pro aplikační a systémový vývoj – C, C++ – systémový software, ovladače, herní enginy, – Java, C# – desktopové a podnikové aplikace, – Rust – systémové programování s důrazem na bezpečnost.
- Programovací jazyky pro mobilní aplikace – Swift – aplikace pro iOS, – Kotlin – aplikace pro Android.
- Programovací jazyky pro vědecké výpočty a práci s daty – Python – analýza dat, umělá inteligence, – R – statistika a datová analýza.
- Speciální a doménově orientované jazyky – SQL – práce s databázemi, – Bash – skriptování v operačních systémech. Výběr programovacího jazyka závisí na konkrétním účelu použití, požadavcích na výkon, přenositelnost, bezpečnost a také na zkušenostech vývojáře nebo vývojového týmu.

# 3. Princip fungování programu v počítači

## 3.1 Princip fungování programu v počítači

Počítač vykonává programy pomocí procesoru (CPU), který postupně zpracovává jednotlivé instrukce. Aby bylo možné program spustit, musí být jeho instrukce: 1. načteny z úložiště (např. disk), 2. umístěny do operační paměti (RAM), 3. postupně vykonávány procesorem.

Procesor pracuje v cyklu, který se často označuje jako cyklus načti – dekóduj – vykonej:

- načti instrukci z paměti,
- dekóduj instrukci (zjisti, co má procesor udělat),
- vykonej instrukci (výpočet, práce s pamětí, skok v programu).
Operační systém přitom zajišťuje:

- spouštění programů,
- přidělování systémových prostředků (čas procesoru, paměť),
- komunikaci mezi hardwarem a softwarem. Program tedy nikdy neběží „sám o sobě”, ale vždy za asistence operačního systému.

## 3.2 Program a proces, multitasking a multithreading

Program je pasivní entita – jedná se o soubor instrukcí uložený na disku (např. soubor `.exe`, `.py` nebo `.jar`). Proces je aktivní instance programu, která právě běží v paměti a je vykonávána procesorem.

Rozdíl mezi programem a procesem lze přirovnat k vaření podle receptu:

- program je jako „recept”,
- proces je jako „vaření podle receptu”.
Multitasking označuje schopnost operačního systému současně spravovat více procesů. Ve skutečnosti procesor velmi rychle přepíná mezi jednotlivými procesy, čímž vytváří dojem, že běží současně. Multithreading znamená, že jeden proces může obsahovat více vláken (threads). Vlákno je menší jednotka vykonávání uvnitř procesu.

> **Příklad**
>
> Grafické aplikace často využívají multithreading k oddělení vykreslování uživatelského rozhraní od zpracování dat na pozadí. Síťové servery mohou používat více vláken k obsluze současných požadavků od různých uživatelů.

Vlastnosti vláken:

- vlákna jednoho procesu sdílejí paměť,
- umožňují paralelní zpracování úloh,
- zvyšují efektivitu využití vícejádrových procesorů. Příklad:
- webový prohlížeč může mít jedno vlákno pro vykreslování stránky,
- jiné vlákno pro načítání dat,
- další vlákno pro reakce na vstupy uživatele.

## 3.3 Využití paměti, ukazatele

Během běhu programu jsou data a instrukce uloženy v operační paměti (RAM). Paměť je rozdělena na malé adresovatelné jednotky, z nichž každá má svou adresu. Program při běhu typicky pracuje s:

- pamětí pro kód programu,
- pamětí pro proměnné a data,
- pamětí pro dočasné výpočty. Operační systém zajišťuje, aby jednotlivé procesy:
- měly přidělen vlastní paměťový prostor,
- nemohly nelegálně přistupovat k paměti jiných procesů. Ukazatel (pointer) je proměnná, která neuchovává přímo hodnotu, ale adresu
v paměti, kde je hodnota uložena. Ukazatele se používají zejména:

- při efektivní práci s pamětí,
- při dynamické alokaci paměti,
- při práci s většími datovými strukturami. Ukazatele jsou typické především pro nižší a systémové programovací jazyky (např.
C, C++). Ve vyšších programovacích jazycích (např. Python, Java) jsou detaily práce s pamětí většinou skryty před programátorem a spravuje je automaticky běhové prostředí (garbage collector) nebo virtuální stroj, což zjednodušuje vývoj, ale může omezit kontrolu nad výkonem a využitím paměti.

# 4. Algoritmizace, možnost zápisu algoritmů

## 4.1 Algoritmizace

Algoritmizace je proces navrhování a vytváření algoritmů pro řešení konkrétních problémů nebo úkolů. Cílem algoritmizace je vytvořit jasný, přesný a efektivní postup, který lze následně implementovat v programovacím jazyce. Algoritmizace zahrnuje několik kroků: 1. Analýza problému – pochopení požadavků a cílů. 2. Návrh algoritmu – vytvoření kroků a logiky řešení. 3. Zápis algoritmu – vyjádření algoritmu pomocí vhodného zápisu (pseudokód, vývojový diagram). 4. Testování a optimalizace – ověření správnosti a efektivity algoritmu. Existuje řada ustálených algoritmů pro běžné úlohy, jako jsou třídění (např. bubble sort, quicksort), vyhledávání (např. binární vyhledávání) nebo grafové algoritmy (např. Dijkstrův algoritmus).

## 4.2 Způsoby zápisu algoritmů

Algoritmy lze zapsat různými způsoby, které usnadňují jejich pochopení a implementaci:

- Pseudokód – textový zápis algoritmu, který používá strukturovaný jazyk podobný programovacím jazykům, ale bez striktních pravidel syntaxe. Pseudokód je snadno čitelný a slouží jako most mezi myšlením a kódováním. Příklad pseudokódu pro výpočet faktoriálu:
```text
Funkce Faktorial(n)
    Pokud n == 0 nebo n == 1 pak
        Návrat 1
    Jinak
        Návrat n * Faktorial(n - 1)
Konec funkce
```

- Vývojový diagram – grafické znázornění algoritmu pomocí symbolů a šipek, které ukazují tok řízení mezi jednotlivými kroky. Vývojové diagramy jsou užitečné pro vizualizaci struktury algoritmu a jeho logiky.

## 4.3 Vývojový diagram

Vývojový diagram (flowchart) používá různé tvary k reprezentaci různých typů operací a rozhodnutí v algoritmu. Přehled symbolů:

- Ovál – začátek/konec
- Obdélník – procesní krok
- Kosočtverec – rozhodovací bod
- Šipky – tok řízení
- Paralelogram – vstup/výstup

Příklad vývojového diagramu pro výpočet faktoriálu:

```text
[Start]
   |
   v
[Zadej n]
   |
   v
[n == 0 nebo n == 1?] -- Ano --> [Návrat 1] --> [Konec]
   |
   Ne
   |
   v
[Faktorial(n - 1)]
   |
   v
[Návrat n * Faktorial(n - 1)]
   |
   v
[Konec]
```

# 5. Základní prvky syntaxe programovacího jazyka

## 5.1 Syntaxe programovacího jazyka

Syntaxe je soubor pravidel, která určují, jak správně psát kód v daném programovacím jazyce. Každý jazyk má svou vlastní syntaxi, která definuje strukturu příkazů, deklaraci proměnných, použití operátorů, tvorbu funkcí a další aspekty programování. Správnost syntaxe lze ověřit pomocí překladače nebo interpretu, který při nalezení chyby obvykle poskytne chybovou zprávu s informací o místě a typu chyby. Důležitou roli hrají také komentáře, které umožňují programátorům přidávat poznámky do kódu bez ovlivnění jeho běhu (např. // Tento radek je komentar v C++ nebo # Tento radek je komentar v Pythonu). Reference na dokumentaci jazyka je klíčová pro pochopení specifických pravidel a konvencí daného jazyka.

## 5.2 Převod algoritmu do zdrojového kódu

Převod algoritmu do zdrojového kódu zahrnuje přepis kroků algoritmu do syntaxe konkrétního programovacího jazyka. Tento proces vyžaduje pochopení jak algoritmu, tak pravidel daného jazyka. Například Python a jazyk C mají odlišnou syntaxi pro deklaraci proměnných a řízení toku. Zatímco v Pythonu se proměnné deklarují jednoduše přiřazením hodnoty (`x = 5`), v C je nutné specifikovat datový typ (`int x = 5;`). V Pythonu se bloky kódu určují odsazením, zatímco v C se používají složené závorky `{}`. Například převod jednoduchého algoritmu pro výpočet faktoriálu do jazyka Python může vypadat takto:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Výstup: 120
```

Stejný algoritmus v jazyce C by vypadal takto:

```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main(void) {
    printf("%d\n", factorial(5));  // Výstup: 120
    return 0;
}
```

## 5.3 Typické chyby a ladění programů

Při psaní kódu se mohou vyskytnout různé typy chyb, které lze rozdělit do několika kategorií:

- Syntaktické chyby – chyby v zápisu kódu, které porušují pravidla syntaxe jazyka (např. chybějící středník, nesprávné odsazení). Tyto chyby jsou obvykle detekovány překladačem nebo interpretem při pokusu o spuštění programu.
- Sémantické chyby – chyby v logice programu, kdy kód dělá něco jiného, než bylo zamýšleno (např. nesprávné podmínky, špatné výpočty). Tyto chyby mohou být obtížnější k odhalení, protože program může běžet bez chybových hlášení, ale výsledky jsou nesprávné.
- Běhové chyby – chyby, které se objevují během vykonávání programu (např. dělení nulou, přístup k neexistujícímu indexu pole). Tyto chyby často vedou k pádu programu nebo neočekávanému chování. Pro ladění programů se používají různé techniky a nástroje:
- Debuggery – specializované nástroje, které umožňují krokování kódu, sledování hodnot proměnných a analýzu toku programu.
- Výpisy (logování) – přidávání výstupních zpráv do kódu pro sledování průběhu programu a hodnot proměnných v různých bodech.
- Jednotkové testy – psaní testovacích případů pro ověření správnosti jednotlivých částí kódu.
- Code reviews – kontrola kódu jinými vývojáři za účelem odhalení chyb a zlepšení kvality kódu. Ladění je klíčovou součástí vývojového procesu a pomáhá zajistit, že program funguje
správně a efektivně.


# 6. Efektivita algoritmů a volba řešení

## 6.1 Správné řešení nemusí být dobré řešení

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

## 6.2 Jak přibližně měřit náročnost algoritmu

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

## 6.3 Co znamená O(1), O(n) a O(n²)

Pro přibližný popis růstu náročnosti se používá takzvaná **asymptotická složitost**, obvykle zapisovaná pomocí symbolu **O**.

Není potřeba chápat tento zápis jako přesný výpočet času. Vyjadřuje především, jak se množství práce mění při zvětšování vstupu.

**Konstantní čas — O(1)**

Představme si pole:

```python
cisla = [10, 20, 30, 40, 50]
print(cisla[3])
```

Chceme-li získat prvek na známé pozici, program se k němu může dostat přímo.

Je téměř jedno, zda pole obsahuje deset prvků nebo milion. Pokud známe index, přístup k jednomu konkrétnímu prvku trvá přibližně stejně dlouho.

Tomuto typu operace říkáme **O(1)**.

Neznamená to, že operace trvá přesně jednu instrukci. Znamená to, že její náročnost se zásadně nezvětšuje s počtem prvků.

**Lineární čas — O(n)**

Při hledání hodnoty v neuspořádaném seznamu můžeme být nuceni projít všechny prvky:

```python
for cislo in seznam:
    if cislo == hledane:
        break
```

Čím více prvků máme, tím více kontrol může být potřeba.

Pro 100 položek maximálně přibližně 100 kontrol, pro 10 000 položek přibližně 10 000.

Takové chování označujeme jako **O(n)**.

**Kvadratický čas — O(n²)**

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

## 6.4 Lineární a binární vyhledávání

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

## 6.5 Třídění jako příklad různě dobrých algoritmů

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

## 6.6 Rychlost není jediným kritériem

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

**Rychlost versus paměť**

Někdy lze výpočet urychlit tím, že si předem uložíme další data.

Například internetový obchod může mít informace o milionech výrobků. Místo toho, aby při každém hledání procházel všechny položky, může používat speciální index.

Vyhledávání je potom rychlejší, ale index zabírá další místo.

Podobný princip využívají databáze i vyhledávače.

**Příprava versus opakované použití**

Představme si seznam milionu čísel.

Pokud v něm chceme najít jednu jedinou hodnotu, nemusí mít smysl celý seznam nejprve třídit.

Pokud v něm ale budeme vyhledávat tisíckrát, může se vyplatit seznam jednou seřadit a potom používat binární vyhledávání.

Jinými slovy:

**někdy investujeme více práce na začátku, abychom pozdější operace výrazně urychlili.**

Takový kompromis se v informatice objevuje velmi často.

## 6.7 Jak poznat zbytečně pomalý program

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

## 6.8 Teorie a skutečný výkon programu

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

# Závěrečné propojení

Algoritmus není pouze postup, který vede ke správnému výsledku. Při skutečném programování nás zajímá také to, kolik práce musí počítač vykonat a jak se tato práce změní při větším množství dat.

Jednoduchý mentální model může vypadat takto:

**problém → návrh algoritmu → správnost → náročnost → implementace → měření → případné zlepšení**

U malých úloh bývá často nejlepší jednoduché a čitelné řešení. S rostoucím množstvím dat ale může volba algoritmu rozhodnout o tom, zda program dokončí úlohu za zlomek sekundy, několik minut, nebo prakticky nikdy.

Nejdůležitější proto není umět zpaměti seznam složitostí různých algoritmů. Podstatné je naučit se klást otázku:

**Jak se bude množství práce měnit, když bude vstupních dat desetkrát, tisíckrát nebo milionkrát více?**

Právě tato otázka vede od pouhého psaní programů k algoritmickému uvažování.
