## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rekurze: když funkce volá sama sebe**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


V předchozích částech jsme opakování řešili především pomocí cyklů. Některé problémy však lze přirozeně popsat jiným způsobem: pomocí **rekurze**. Rekurzivní funkce je funkce, která při svém běhu zavolá sama sebe, obvykle s jednodušší verzí původního problému.

Klasickým příkladem je faktoriál. Pro číslo 5 platí:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

Stejný výpočet ale můžeme vyjádřit také postupně:

`5! = 5 × 4!`  
`4! = 4 × 3!`  
`3! = 3 × 2!`

až dojdeme k jednoduchému případu `1! = 1`.

V Pythonu lze tento princip zapsat:

```python
def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)

print(faktorial(5))
```

Výsledkem je `120`.

Každá rekurzivní funkce potřebuje dvě důležité části. **Ukončovací podmínka** určuje případ, který už dokážeme vyřešit přímo, a rekurzivní krok převádí původní problém na jednodušší problém stejného typu. Bez ukončovací podmínky by funkce volala sama sebe stále znovu a program by skončil chybou.

Rekurze není náhradou každého cyklu. Například jednoduché vypsání čísel od 1 do 100 je přirozenější řešit cyklem. Rekurze se hodí především pro problémy, které samy obsahují menší problémy stejného druhu.

Dobrým příkladem je struktura složek:

```text
dokumenty
├── skola
│   ├── matematika
│   └── informatika
└── osobni
    └── fotografie
```

Chceme-li projít celý adresář, můžeme pro každou nalezenou podsložku zopakovat stejný postup. Podobnou strukturu mají například rodokmeny, organizační hierarchie nebo stromové datové struktury.

Při návrhu rekurze je proto užitečné položit si dvě jednoduché otázky:

**Kdy se funkce zastaví?**

**Je při každém dalším volání problém skutečně jednodušší?**

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rekurze a iterace: dvě cesty ke stejnému výsledku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Mnoho úloh lze vyřešit jak rekurzivně, tak pomocí cyklu. Faktoriál můžeme například napsat také takto:

```python
def faktorial(n):
    vysledek = 1

    for cislo in range(2, n + 1):
        vysledek *= cislo

    return vysledek
```

Výsledek je stejný jako u rekurzivní varianty.

První řešení používá **iteraci**, tedy opakování pomocí cyklu. Druhé řešení používá rekurzivní volání funkce.

U jednoduchého opakování bývá cyklus obvykle přímočařejší. Rekurze je výhodná hlavně tehdy, když odpovídá samotné povaze problému. Například při procházení stromové struktury je přirozené zpracovat jeden uzel a stejným postupem pokračovat v jeho potomcích.

Nemá proto smysl rozhodovat podle pravidla „rekurze je pokročilejší, takže je lepší“. Vhodnější otázka zní:

> Který způsob vyjadřuje řešení tohoto konkrétního problému jednodušeji a srozumitelněji?

Pro běžné opakování je často vhodnější cyklus. Pro hierarchicky uspořádané problémy může být rekurze výrazně přirozenější.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Výjimky: když operaci nelze dokončit běžným způsobem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Program nepracuje vždy s ideálními vstupy. Uživatel může zadat text tam, kde očekáváme číslo, soubor nemusí existovat nebo může nastat jiná situace, která znemožní pokračovat běžným způsobem.

Například:

```python
vek = int(input("Zadejte věk: "))
```

funguje, pokud uživatel zadá:

```text
18
```

Pokud ale napíše:

```text
osmnáct
```

nelze text převést na celé číslo a Python vyvolá **výjimku — exception**.

Výjimka oznamuje, že při provádění určité operace nastal problém. Pokud ji program nijak neošetří, běh programu zpravidla skončí chybovým hlášením.

Pokud s takovou situací počítáme, můžeme ji zachytit:

```python
try:
    vek = int(input("Zadejte věk: "))
    print(f"Za rok vám bude {vek + 1}.")
except ValueError:
    print("Věk musí být zadán jako celé číslo.")
```

Kód v bloku `try` se program pokusí normálně vykonat. Pokud při převodu vznikne `ValueError`, pokračuje blokem `except`.

Stejný princip lze použít například při práci se souborem:

```python
try:
    with open("data.txt", "r", encoding="utf-8") as soubor:
        obsah = soubor.read()
except FileNotFoundError:
    print("Soubor nebyl nalezen.")
```

Výjimka tedy umožňuje oddělit **běžný průběh programu** od řešení situace, kdy určitou operaci nelze dokončit.

Není ale vhodné bez rozmyslu skrýt každou možnou chybu:

```python
try:
    neco_proved()
except:
    pass
```

Takový program může skutečný problém pouze zatajit. Je lepší zachytávat především konkrétní výjimky, se kterými skutečně počítáme a na které umíme vhodně reagovat.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Validace vstupu: je hodnota nejen správného typu, ale také smysluplná?**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Úspěšné načtení hodnoty ještě neznamená, že je vstup správný.

Představme si program:

```python
vek = int(input("Zadejte věk: "))
```

Hodnota `25` je v pořádku. Hodnota `-300` je ale také platné celé číslo, přestože jako věk člověka nedává smysl.

Proto provádíme **validaci vstupu**, tedy kontrolu, zda data splňují pravidla požadovaná programem.

Například:

```python
try:
    vek = int(input("Zadejte věk: "))

    if 0 <= vek <= 130:
        print("Hodnota byla přijata.")
    else:
        print("Věk není v očekávaném rozsahu.")

except ValueError:
    print("Zadejte celé číslo.")
```

Program zde kontroluje dvě odlišné věci.

Nejprve ověřuje **typ nebo formát vstupu**: lze zadaný text převést na celé číslo?

Potom ověřuje jeho **význam**: leží číslo v rozumném rozsahu?

Podobně můžeme kontrolovat například známku:

```python
if 1 <= znamka <= 5:
    print("Platná známka")
else:
    print("Známka musí být od 1 do 5")
```

nebo nabídnout opakované zadávání, dokud uživatel neposkytne přijatelnou hodnotu:

```python
while True:
    try:
        znamka = int(input("Zadejte známku 1 až 5: "))

        if 1 <= znamka <= 5:
            break

        print("Známka musí být od 1 do 5.")

    except ValueError:
        print("Zadejte celé číslo.")

print(f"Zadána známka {znamka}.")
```

Tento příklad současně propojuje několik principů strukturovaného programování: cyklus řídí opakování, podmínka kontroluje rozsah a výjimka zachytává chybný typ vstupu.

Je užitečné rozlišovat:

**výjimka** — operaci nebylo možné běžným způsobem provést;

**validace** — operaci provést lze, ale výsledek ještě kontrolujeme podle pravidel programu.

Například text `abc` nelze převést na číslo a vznikne výjimka. Hodnotu `-300` na číslo převést lze, ale validace ji odmítne jako nepřijatelný věk.

# Závěrečné propojení

Základní strukturované konstrukce — sekvence, větvení, cykly a funkce — umožňují popsat běžný tok programu. Rekurze přidává možnost řešit problém prostřednictvím jednoduššího problému stejného typu. Výjimky umožňují přehledně zachytit situace, kdy určitou operaci nelze normálně dokončit, a validace kontroluje, zda přijatá data skutečně odpovídají požadavkům programu.

Vztah těchto principů lze shrnout:

**opakování → cyklus nebo rekurze**

**operace → úspěch nebo výjimka**

**vstup → převod → validace → další zpracování**

***
