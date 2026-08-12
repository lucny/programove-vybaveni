## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Objekty spolupracují, neexistují izolovaně**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednoduché příklady OOP často ukazují jednu třídu, například `Osoba`, `Auto` nebo `Zvire`. Skutečné programy ale obvykle obsahují větší množství objektů, které spolu nějak souvisejí a předávají si informace.

Představme si jednoduchý program pro školní knihovnu. Můžeme v něm mít například třídy:

- `Kniha`,
- `Ctenar`,
- `Vypujcka`.

Objekt `Kniha` může uchovávat název a autora, objekt `Ctenar` jméno čtenáře a objekt `Vypujcka` může spojovat konkrétní knihu s konkrétním čtenářem.

Například v Pythonu:

```python
class Kniha:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor


class Ctenar:
    def __init__(self, jmeno):
        self.jmeno = jmeno


class Vypujcka:
    def __init__(self, kniha, ctenar):
        self.kniha = kniha
        self.ctenar = ctenar
```

Při vytvoření objektů:

```python
kniha = Kniha("1984", "George Orwell")
ctenar = Ctenar("Jan Novák")
vypujcka = Vypujcka(kniha, ctenar)
```

objekt `Vypujcka` neobsahuje pouze textové kopie názvu knihy a jména čtenáře. Odkazuje na objekty `Kniha` a `Ctenar`, které existují samostatně.

Tím vzniká vztah mezi objekty.

V objektově orientovaném návrhu je proto důležitá nejen otázka:

> Jaké atributy a metody má tato třída?

ale také:

> S jakými dalšími objekty má spolupracovat?

Třídy tak postupně vytvářejí model skutečného problému. Ve školním systému mohou spolupracovat objekty `Student`, `Predmet`, `Ucitel` a `Znamka`; v e-shopu například `Zakaznik`, `Produkt`, `Objednavka` a `Platba`.

OOP proto není pouze způsob, jak rozdělit program do mnoha tříd. Smyslem je rozdělit odpovědnosti mezi objekty tak, aby jejich spolupráce odpovídala problému, který program řeší.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Dědičnost a kompozice: „je“ versus „má“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


V předchozí části jsme dědičnost používali například ve vztahu:

```text
Zvíře
  └── Pes
```

Pes **je zvíře**, proto je dědičnost přirozená.

Ne každý vztah mezi objekty je ale tohoto typu.

Představme si automobil a motor.

Automobil **není motor**. Automobil **má motor**.

Pokud bychom vytvořili:

```text
Motor
  └── Automobil
```

nedával by takový vztah význam.

Vhodnější je vytvořit dvě samostatné třídy:

```python
class Motor:
    def nastartuj(self):
        print("Motor běží.")


class Auto:
    def __init__(self):
        self.motor = Motor()

    def nastartuj(self):
        self.motor.nastartuj()
```

Třída `Auto` zde obsahuje objekt `Motor` a používá jeho funkčnost.

Takovému způsobu skládání objektů se říká **kompozice**.

Rozdíl si můžeme zapamatovat velmi jednoduše:

**dědičnost — „je“**

`Pes je Zvire.`

**kompozice — „má“**

`Auto má Motor.`

Dalším příkladem může být počítač:

```text
Počítač má procesor.
Počítač má paměť.
Počítač má úložiště.
```

Nebudeme tedy vytvářet třídu `Procesor`, ze které by dědil `Pocitac`. Počítač se skládá z dalších objektů.

Kompozice má praktickou výhodu: jednotlivé části lze snadněji měnit.

Například:

```python
class BenzinovyMotor:
    def nastartuj(self):
        print("Startuji benzinový motor.")


class Elektromotor:
    def nastartuj(self):
        print("Aktivuji elektromotor.")
```

Třída automobilu může podle potřeby pracovat s různými typy motoru, aniž bychom museli změnit celý model objektů.

Dědičnost je tedy užitečný mechanismus, ale neměla by být používána automaticky jen proto, že OOP dědičnost nabízí. Mnoho programů je přehlednějších, když jsou větší objekty sestaveny z menších spolupracujících objektů.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Každá třída by měla mít srozumitelnou odpovědnost**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Představme si třídu:

```python
class Student:
    def uloz_do_databaze(self):
        ...

    def vytiskni_vysvedceni(self):
        ...

    def posli_email(self):
        ...

    def vypocitej_statistiku_tridy(self):
        ...

    def vytvor_pdf(self):
        ...
```

Na první pohled může být pohodlné mít všechny operace na jednom místě. Třída `Student` ale postupně začíná řešit ukládání do databáze, tisk, e-mail, statistiku i tvorbu PDF.

Vzniká objekt, který má příliš mnoho různých úkolů.

Jedním ze základních principů dobrého objektového návrhu proto je, že **třída by měla mít jasnou a omezenou odpovědnost**.

Objekt `Student` může například uchovávat informace o studentovi:

```python
class Student:
    def __init__(self, jmeno, trida):
        self.jmeno = jmeno
        self.trida = trida
```

O ukládání se může starat jiný objekt:

```python
class StudentRepository:
    def uloz(self, student):
        ...
```

o vytvoření vysvědčení další:

```python
class GeneratorVysvedceni:
    def vytvor(self, student):
        ...
```

a o odesílání zpráv například:

```python
class EmailService:
    def odesli(self, student, zprava):
        ...
```

Program tak obsahuje více tříd, ale každá z nich má srozumitelnější úkol.

Tento přístup přináší několik výhod. Když se změní způsob odesílání e-mailů, nemusíme zasahovat do třídy `Student`. Pokud chceme změnit formát vysvědčení, upravujeme pouze část odpovědnou za jeho tvorbu.

Neznamená to, že každá metoda musí být ve vlastní třídě. To by vedlo k opačnému extrému. Smyslem je hledat přirozené rozdělení odpovědností.

Dobrou kontrolní otázkou je:

> Dokážu jednou krátkou větou říci, za co tato třída odpovídá?

Pokud odpověď zní například:

> Tato třída ukládá studenty, tiskne dokumenty, posílá e-maily, počítá statistiku a ještě zobrazuje uživatelské rozhraní,

pravděpodobně řeší příliš mnoho věcí najednou.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Od tříd ke struktuře celé aplikace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jakmile program obsahuje desítky nebo stovky tříd, nestačí už pouze správně navrhnout každý jednotlivý objekt. Musíme také rozhodnout, jak budou větší části aplikace uspořádány.

Představme si například program pro správu knihovny.

Jedna část pracuje s daty:

```text
Kniha
Čtenář
Výpůjčka
```

jiná část komunikuje s databází a další zobrazuje informace uživateli.

Je výhodné tyto oblasti úplně nesmíchat.

Například objekt reprezentující knihu by neměl zároveň řešit, jak se vykreslí tlačítko v okně programu:

```python
class Kniha:
    def zobraz_modre_tlacitko(self):
        ...
```

Stejně tak by tlačítko uživatelského rozhraní nemělo obsahovat SQL dotazy pro práci s databází.

Ve větších aplikacích se proto odpovědnosti často rozdělují do **vrstev**.

Jednoduchý model může vypadat:

```text
uživatelské rozhraní
        ↓
aplikační logika
        ↓
data
```

Uživatel například klikne na tlačítko „Půjčit knihu“. Uživatelské rozhraní předá požadavek aplikační části, ta zkontroluje, zda je kniha dostupná, vytvoří výpůjčku a požádá datovou vrstvu o její uložení.

Každá část programu tedy řeší jiný druh problému.

Podobnou myšlenku používá známý vzor **MVC — Model, View, Controller**.

**Model** reprezentuje data a pravidla aplikace.

**View** zajišťuje jejich zobrazení.

**Controller** reaguje na požadavky uživatele a propojuje jednotlivé části.

Velmi zjednodušeně:

```text
uživatel
   ↓
Controller
   ↓
Model
   ↓
View
   ↓
uživatel
```

MVC není univerzální návod pro každý program a existuje řada jiných architektonických přístupů. Pro základní pochopení OOP je ale užitečné, protože ukazuje, že rozdělování odpovědností nekončí u jednotlivých tříd.

Stejný princip pokračuje i na vyšší úrovni:

**program → části systému → třídy → objekty → jejich spolupráce**

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Návrhové vzory: osvědčená řešení opakujících se problémů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při vývoji větších programů se často opakují podobné problémy. Například potřebujeme oddělit vytváření objektu od jeho použití nebo zajistit, aby více objektů reagovalo na změnu stavu jiného objektu.

Programátoři si postupně všimli, že pro podobné situace existují opakovaně použitelné způsoby návrhu. Tyto obecné postupy se označují jako **návrhové vzory — design patterns**.

Návrhový vzor není hotový kus programu ani knihovna, kterou pouze vložíme do projektu. Je to spíše popis osvědčeného uspořádání tříd a jejich spolupráce pro určitý typ problému.

Můžeme si to představit podobně jako stavební plán. Neříká přesně, z jakých cihel musí být konkrétní dům postaven, ale ukazuje ověřený způsob, jak například navrhnout schodiště nebo rozdělit místnosti.

Jedním z jednoduchých příkladů je vzor **Observer — pozorovatel**. Představme si aplikaci, ve které se po změně dat musí aktualizovat několik částí uživatelského rozhraní. Místo toho, aby objekt s daty přímo znal všechny konkrétní části rozhraní, umožní ostatním objektům přihlásit se k odběru změn. Když se stav změní, upozorní všechny registrované pozorovatele.

Jiným příkladem je **Factory — továrna**, která odděluje vytváření objektů od kódu, který je používá. Program například požádá o vytvoření určitého typu dokumentu, aniž by musel znát všechny podrobnosti konstrukce konkrétní třídy.

Návrhových vzorů existuje mnoho, ale není cílem učit se jejich názvy zpaměti. Důležitější je pochopit jejich smysl:

**opakující se návrhový problém → známý princip řešení → přizpůsobení konkrétnímu programu**

Návrhové vzory také nejsou pravidla, která je nutné používat za každou cenu. Pokud je problém jednoduchý, může být přímé řešení lepší než zbytečně složitá architektura vytvořená jen proto, aby v programu byl „nějaký pattern“.

Pro základní orientaci stačí vědět, že návrhové vzory dávají programátorům společný slovník pro popis osvědčených způsobů spolupráce objektů. Když například vývojář řekne, že určitá část programu používá Observer nebo Factory, zkušený kolega má přibližnou představu, jak jsou dané objekty uspořádány.

# Závěrečné propojení

Základní mechanismy objektově orientovaného programování umožňují vytvářet třídy, objekty, skrývat jejich vnitřní stav, využívat dědičnost, polymorfismus, abstraktní třídy a rozhraní. Samotná znalost těchto mechanismů ale ještě nezaručuje dobře navržený program.

Při návrhu objektového řešení je vhodné uvažovat v několika krocích:

**Jaké objekty v problému existují?**

**Jakou odpovědnost má každý z nich?**

**Jaké vztahy mezi nimi vznikají?**

**Jde o vztah „je“, nebo „má“?**

**Jak spolu budou jednotlivé části programu komunikovat?**

Dědičnost vyjadřuje především vztah specializace, například `Pes je Zvire`. Kompozice skládá složitější objekt z dalších objektů, například `Auto má Motor`. Dobře navržená třída má srozumitelnou odpovědnost a ve větší aplikaci se třídy seskupují do částí, které oddělují například práci s daty, aplikační logiku a uživatelské rozhraní.

Návrhové vzory pak nabízejí obecně známé a osvědčené způsoby, jak některé opakující se problémy spolupráce objektů řešit.

Celou cestu od jednoduchého objektu k aplikaci lze proto shrnout:

**třída → objekt → vztahy mezi objekty → spolupráce → návrhové vzory → struktura aplikace**

Právě zde se OOP mění z pouhé znalosti syntaxe tříd na způsob uvažování o návrhu programu.

***
