## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Datová struktura není jen „místo pro data“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při programování nestačí rozhodnout, **jaká data chceme uložit**. Stejně důležité je, **jak s nimi budeme pracovat**.

Představme si například seznam návštěvníků školní akce. Pokud potřebujeme pouze postupně projít všechna jména, postačí jednoduchý seznam. Pokud ale chceme velmi často zjišťovat, zda se konkrétní člověk už zaregistroval, může být vhodnější jiná datová struktura.

Datová struktura tedy určuje nejen způsob uložení hodnot, ale také to, jak snadno lze provádět určité operace: vyhledat položku, přidat novou, odebrat starou nebo procházet data v určitém pořadí.

V předchozí části jsme se setkali s **polem**, kde jsou prvky uspořádány za sebou a přistupujeme k nim pomocí indexu. To je velmi vhodné například tehdy, když chceme rychle získat „pátou položku“. Pro jiné úlohy však existují vhodnější struktury.

Můžeme si to představit podobně jako různé způsoby ukládání věcí. Knihy ukládáme jinak než zákazníky čekající u pokladny a jinak než kontakty v telefonním seznamu. Ve všech případech ukládáme nějaké položky, ale způsob jejich organizace odpovídá tomu, co s nimi potřebujeme dělat.

Základní otázka při volbě datové struktury proto zní:

> Které operace budu s daty provádět nejčastěji?

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Seznam, zásobník a fronta**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednou z nejjednodušších struktur je **seznam — list**. Obsahuje posloupnost prvků a na rozdíl od klasického statického pole může být v mnoha programovacích jazycích snadno rozšiřován nebo zkracován.

V Pythonu je seznam základním vestavěným typem:

```python
studenti = ["Anna", "Petr", "Lucie"]

studenti.append("Jan")
studenti.remove("Petr")

print(studenti)
```

Výsledkem bude:

```text
['Anna', 'Lucie', 'Jan']
```

Ze seznamu lze vytvořit i struktury, které omezují pořadí přidávání a odebírání položek.

### Zásobník

**Zásobník — stack** pracuje podle principu:

**LIFO — Last In, First Out**

tedy „poslední dovnitř, první ven“.

Představme si hromádku talířů. Nový talíř položíme nahoru a také jej jako první odebereme.

```text
      [C] ← odebereme jako první
      [B]
      [A]
```

Zásobník se používá například při ukládání historie operací pro funkci **Zpět**, při vyhodnocování výrazů nebo při volání funkcí.

V Pythonu jej můžeme jednoduše simulovat seznamem:

```python
historie = []

historie.append("napsat text")
historie.append("vložit obrázek")
historie.append("změnit nadpis")

posledni = historie.pop()

print(posledni)
```

Výstup:

```text
změnit nadpis
```

### Fronta

**Fronta — queue** používá opačný princip:

**FIFO — First In, First Out**

tedy „první dovnitř, první ven“.

Je podobná skutečné frontě lidí. Ten, kdo přišel první, je také první obsloužen.

```text
vstup → [Anna] [Petr] [Lucie] → obsluha
```

Frontu lze použít například pro tiskové úlohy, požadavky na server nebo úkoly čekající na zpracování.

Rozdíl mezi zásobníkem a frontou je tedy především v pořadí:

**zásobník:** poslední přidaný prvek odchází první,

**fronta:** první přidaný prvek odchází první.

Stejná data tak můžeme organizovat různými způsoby podle toho, jaké chování potřebujeme.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Množina a slovník: když potřebujeme rychle hledat**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Představme si program, který eviduje registrační čísla účastníků:

```python
registrace = [105, 203, 417, 562, 814]
```

Pokud chceme zjistit, zda se číslo `417` v seznamu nachází, můžeme seznam procházet, dokud jej nenajdeme.

U několika položek je to bezvýznamný rozdíl. U statisíců záznamů však může být výhodnější použít strukturu navrženou právě pro rychlé vyhledávání.

### Množina

**Množina — set** uchovává unikátní hodnoty. Jeden prvek se v ní nemůže vyskytovat několikrát.

```python
registrovani = {105, 203, 417, 562, 814}

if 417 in registrovani:
    print("Účastník je registrován.")
```

Množina se hodí například tehdy, když potřebujeme zjišťovat:

- zda už určitá hodnota existuje,
- které hodnoty jsou unikátní,
- které prvky mají dvě skupiny společné.

Například:

```python
trida_a = {"Anna", "Jan", "Eva"}
trida_b = {"Petr", "Eva", "Jan"}

spolecni = trida_a & trida_b

print(spolecni)
```

Výsledkem budou jména, která se vyskytují v obou množinách.

### Slovník

**Slovník — dictionary** ukládá dvojice:

**klíč → hodnota**

Například:

```python
student = {
    "jmeno": "Anna Nováková",
    "trida": "3A",
    "vek": 17
}
```

Hodnotu získáme pomocí jejího klíče:

```python
print(student["trida"])
```

Slovník tedy můžeme chápat podobně jako skutečný slovník: nehledáme „pátou položku“, ale hodnotu označenou určitým klíčem.

Jiným příkladem může být počet bodů:

```python
body = {
    "Anna": 25,
    "Petr": 18,
    "Lucie": 31
}

print(body["Lucie"])
```

Podobné struktury jsou velmi časté v databázích, webových aplikacích i při práci s formátem JSON.

Množiny a slovníky bývají uvnitř často založeny na principu **hashování**. Z klíče se vypočítá pomocná číselná hodnota, která umožní rychle určit, kde mají být data hledána. Pro základní pochopení není nutné znát přesný algoritmus hashovací funkce. Podstatné je, že program obvykle nemusí při každém hledání postupně porovnávat všechny položky.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Stromy a grafy: když data vytvářejí vztahy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Ne všechna data lze přirozeně uspořádat do jedné řady.

Představme si strukturu adresářů:

```text
skola
├── studenti
│   ├── prvni_rocnik
│   └── druhy_rocnik
└── ucitele
    ├── informatika
    └── matematika
```

Taková struktura připomíná strom.

**Strom — tree** je datová struktura složená z uzlů, mezi kterými existují vztahy nadřazenosti a podřazenosti. Výchozí uzel se nazývá **kořen — root**, další uzly mohou mít své potomky.

Stromovou strukturu najdeme například v:

- adresářích souborového systému,
- organizační struktuře firmy,
- rodokmenu,
- HTML dokumentu reprezentovaném pomocí DOM,
- některých vyhledávacích strukturách.

Zvláštním případem je **binární strom**, ve kterém může mít uzel nejvýše dva potomky. Některé binární stromy lze uspořádat tak, aby umožňovaly efektivní vyhledávání hodnot.

Existují však také problémy, které už nemají přirozenou stromovou hierarchii.

Představme si síť měst:

```text
Opava ─ Ostrava
  │       │
Krnov ─ Bruntál
```

Jedno město může být spojeno s několika dalšími a neexistuje zde jediný přirozený „kořen“.

Takovou strukturu označujeme jako **graf — graph**.

Graf se skládá z **vrcholů** a **hran**, které vyjadřují vztahy mezi nimi.

Vrchol může představovat město a hrana silnici. V sociální síti může vrchol představovat uživatele a hrana jejich spojení. V počítačové síti mohou vrcholy představovat zařízení a hrany komunikační linky.

Grafy se proto používají například při:

- hledání trasy v navigaci,
- modelování počítačových sítí,
- analýze sociálních sítí,
- plánování dopravy,
- hledání vazeb mezi objekty.

Strom a graf nejsou pouze složitější varianty seznamu. Umožňují reprezentovat **vztahy mezi daty**, které by se v jednoduché posloupnosti popisovaly velmi obtížně.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak vybrat vhodnou datovou strukturu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Neexistuje jedna datová struktura, která by byla nejlepší pro všechny situace.

Představme si několik různých problémů.

Chceme uložit naměřené teploty v pořadí, v jakém vznikly. Přirozenou volbou je seznam nebo pole.

Chceme implementovat funkci „Zpět“ v editoru. Hodí se zásobník.

Chceme zpracovávat požadavky v pořadí jejich příchodu. Hodí se fronta.

Chceme rychle zjistit, zda už bylo určité ID použito. Vhodná může být množina.

Chceme ke jménu studenta rychle přiřadit počet bodů. Přirozený je slovník.

Chceme reprezentovat strukturu složek. Hodí se strom.

Chceme hledat trasu mezi městy. Potřebujeme graf.

Lze si tedy vytvořit jednoduchý přehled:

| Potřeba | Vhodná struktura |
|---|---|
| hodnoty v pořadí | pole nebo seznam |
| poslední vložená položka jako první | zásobník |
| položky zpracované v pořadí příchodu | fronta |
| unikátní hodnoty a rychlé ověření existence | množina |
| vztah klíč → hodnota | slovník |
| hierarchie | strom |
| obecná síť vztahů | graf |

Tato tabulka není absolutním pravidlem. Skutečné programy často kombinují několik struktur a jednotlivé programovací jazyky je mohou implementovat odlišně.

Důležitější než jejich názvy je základní princip:

> Datovou strukturu volíme podle operací, které chceme s daty provádět.

Stejný soubor dat můžeme někdy uložit několika způsoby, ale volba struktury ovlivní jednoduchost programu i jeho rychlost.

Například seznam uživatelů je vhodný pro postupné procházení. Pokud však potřebujeme tisíckrát za sekundu zjišťovat, zda určité uživatelské ID existuje, může být vhodnější množina nebo slovník.

Volba datové struktury je proto součástí samotného návrhu algoritmu.

# Závěrečné propojení

V předchozích částech jsme pracovali s poli, maticemi, řetězci, soubory a strukturovanými datovými formáty. Další datové struktury ukazují, že způsob organizace dat závisí především na tom, jak s nimi chceme pracovat.

Základní souvislost můžeme shrnout:

**data → požadované operace → vhodná datová struktura → algoritmus**

Seznam zachovává posloupnost, zásobník a fronta určují pořadí zpracování, množina pomáhá pracovat s unikátními hodnotami, slovník propojuje klíče s hodnotami a stromy či grafy zachycují složitější vztahy mezi objekty.

Nejdůležitější proto není naučit se zpaměti co nejvíce názvů datových struktur. Podstatné je umět se při návrhu programu zeptat:

**Potřebuji data hlavně procházet, vyhledávat, přidávat, odebírat, nebo mezi nimi zachytit vztahy?**

Právě odpověď na tuto otázku často rozhoduje o tom, jaká datová struktura je pro daný problém nejvhodnější.

***
