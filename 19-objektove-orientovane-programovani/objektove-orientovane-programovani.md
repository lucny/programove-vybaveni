# Objektově orientované programování

## 1. Důvody vzniku OOP a jeho principy

### 1.1 Vznik objektově orientovaného programování

Procedurální programování, které řeší problémy postupným vykonáváním posloupnosti instrukcí, se ukázalo být nedostatečné pro vývoj rozsáhlých a složitých aplikací. S rostoucí velikostí programů se objevily zásadní problémy:

- Obtížná údržba – ”spaghetti”kód s mnohými vzájemnými vazbami a globálními proměnnými se stává nepřehledným a nebezpečným na úpravy.
- Opakování kódu – stejné postupy se často píší znovu místo jejich opakovaného využití.
- Špatná organizace – chybí jasná struktura a logická hierarchie v programu.
- Náchylnost na chyby – změny v jedné části kódu neočekávaně ovlivňují jiné části. Tyto problémy vedly v 70. a 80. letech 20. století ke vzniku objektově orientovaného
programování (OOP), které nabízí fundamentálně odlišný přístup: místo soustředění se na procedury a datové struktury se program modeluje pomocí objektů, které kombinují data a operace nad nimi v jeden celek.

### 1.2 Základní pojmy OOP

Třída je abstraktní předpis (šablona, plán) definující, jaké vlastnosti a chování mají objekty daného typu. Třída určuje:

- jaké atributy (data, vlastnosti) budou objekty obsahovat,
- jaké metody (operace, chování) budou objekty vykonávat. Třída sama o sobě není entita existující v paměti, je pouze definicí. Objekt je konkrétní instance třídy vzniklá v paměti počítače. Objekt obsahuje
skutečné hodnoty atributů a může vykonávat metody definované v třídě. Stejně jako lze mít mnoho instancí stejného programu spuštěno současně, lze vytvořit z jedné třídy mnoho objektů.

Příklad z reálného světa: Třída Automobil by mohla definovat atributy jako barva , rychlost , množství_paliva a metody jako akcelerace() , brzdění() , doplnění_paliva() . Konkrétní automobil značky Škoda Octavia s červenou barvou a plnou nádrží by byl objektem třídy Automobil .

### 1.3 Využití OOP v praxi

Objektově orientované programování se uplatňuje v mnoha oblastech:

- Desktopové a webové aplikace – objekty reprezentují prvky uživatelského rozhraní, formuláře, data z databází.
- Počítačové hry – objekty reprezentují postavy, předměty, nepřátele, prostředí; jejich interakce se řídí zapsaným chováním.
- Simulace a vědecké výpočty – objekty modelují fyzické entity a jejich interakce.
- Informační systémy – objekty reprezentují záznamy o zákaznících, výrobcích, transakcích.
- Grafika a vizualizace – objekty reprezentují geometrické tvary, kameru, osvětlení. OOP je převažujícím paradigmatem v moderním softwarovém inženýrství, neboť přináší lepší organizaci, bezpečnost a znovupoužitelnost kódu.

## 2. Třídy a objekty

### 2.1 Struktura třídy

Třída jako základní stavební jednotka OOP obsahuje několik klíčových prvků:

- atributy (data) – proměnné uchovávající stav objektu,
- metody (funkce) – procedury provádějící operace nad daty,
- konstruktor – speciální metoda volaná při vytváření objektu,
- destruktor – speciální metoda volaná při zrušení objektu. Příklad deklarace třídy v C++:

```
class Osoba {
private :
int vek;                // Privatni atribut
string jmeno ;          // Privatni atribut
```

```
public :
// Konstruktor
Osoba ( string j, int v) {
jmeno = j;
vek = v;
}
```

```
// Metoda
void predstaveni () {
cout << " Jmenuju se " << jmeno << ", je mi " << vek << " let." << endl;
}
```


```
// Destruktor
~Osoba () {
cout << " Osoba " << jmeno << " je zrusena ." << endl;
}
};
```

Příklad deklarace třídy v Pythonu:

```
class Osoba :
def __init__ (self , jmeno , vek):    # Konstruktor
self. jmeno = jmeno
self.vek = vek
```

```
def predstaveni (self): # Metoda
print (f" Jmenuju se {self. jmeno }, je mi {self.vek} let.")
```

```
def __del__ (self): # Destruktor
print (f"Osoba {self.jmeno } je zrusena .")
```

### 2.2 Atributy a metody

Atributy jsou proměnné, které uchovávají data objektu. Každý objekt má svou vlastní sadu hodnot atributů. Metody jsou funkce definované v třídě, které mohou pracovat s atributy objektu a provádět operace. Při volání metody musíme metodu volat na konkrétním objektu. Příklad v C++:

```
Osoba osoba (" Alice", 25);
osoba. predstaveni (); // Volani metody na objektu
cout << osoba .vek; // Pristup k atributu
```

Příklad v Pythonu:

```
osoba = Osoba (" Alice", 25)
osoba. predstaveni () # Volani metody na objektu
print (osoba .vek)     # Pristup k atributu
```

### 2.3 Konstruktor a destruktor

Konstruktor je speciální metoda, která se automaticky volá ve chvíli, kdy je objekt vytvářen. Slouží k inicializaci atributů objektu.

- V C++ má konstruktor stejné jméno jako třída a nemá návratový typ,
- v Pythonu je to metoda pojmenovaná __init__ . Konstruktor přijímá parametry, které určují počáteční hodnoty atributů: Příklad volání konstruktoru v C++:

```
Osoba osoba ("Bob", 30);      // Volani konstruktoru
```

Příklad volání konstruktoru v Pythonu:

```
osoba = Osoba ("Bob", 30)      # Volani konstruktoru
```

Destruktor je speciální metoda volaná, když se objekt maže z paměti. Slouží k uvolnění prostředků (soubory, paměť) a čistění před zničením objektu.

- V C++ je destruktor pojmenován vlnkou ~ před jménem třídy,
- v Pythonu je to metoda __del__ . Je však méně používaný, protože Python má automatickou správu paměti. Příklad destruktoru v C++:

```
~Osoba () {
// Uvolneni prostredku
}
```

Příklad destruktoru v Pythonu:

```
def __del__ (self):
# Uvolneni prostredku
pass
```

### 2.4 Instanční a třídní prvky

Instanční atributy a metody patří konkrétnímu objektu. Každá instance má vlastní hodnoty instančních atributů.

```
class Ucet {
private :
double zustatek ;      // Instancni atribut
};
```

Objekty se vytvářejí instancování třídy:

```
Ucet ucet1 (1000) ;     // Prvni instance se zustatkem 1000
Ucet ucet2 (500) ;      // Druha instance se zustatkem 500
```

Třídní (statické) prvky jsou sdíleny všemi instancemi třídy. Existují pouze jednou, bez ohledu na počet vytvořených objektů. Příklad v C++:

```
class Ucet {
private :
double zustatek ;
static int pocet_uctu ;        // Tridni atribut
```

```
public :
Ucet( double z) : zustatek (z) {
pocet_uctu ++; // Pocet uctu se zvysi
}
```

```
static int getPocetUctu () {          // Tridni metoda
return pocet_uctu ;
}
};
int Ucet :: pocet_uctu = 0;       // Inicializace tridniho atributu
```

Příklad v Pythonu:

```
class Ucet:
pocet_uctu = 0       # Tridni atribut
```

```
def __init__ (self , zustatek ):
self. zustatek = zustatek
Ucet. pocet_uctu += 1
```

```
@classmethod
def get_pocet_uctu (cls): # Tridni metoda
return cls. pocet_uctu
```

### 2.5 Princip zapouzdření

Zapouzdření (encapsulation) je princip skrývání interního stavu objektu a řízení přístupu k němu. Objekty poskytují veřejné rozhraní (veřejné metody), zatímco interní implementace zůstává skryta.

Příklady: Bankovní účet by měl skrýt svůj zůstatek a umožnit přístup pouze prostřednictvím metod pro vklad, výběr a kontrolu zůstatku. Automobil by měl skrýt své vnitřní mechanismy a umožnit ovládání pouze přes metody jako start() , stop() , accelerate() .

Zapouzdření zajišťuje:

- Bezpečnost – data nelze nechtěně změnit přímým přístupem.
- Kontrolu – všechny změny dat procházejí skrze metody, které mohou ověřit validitu.
- Flexibilitu – interní reprezentaci lze změnit bez ovlivnění zbytku programu. Jazyk C++ poskytuje tři úrovně viditelnosti:
- public – přístupné zvenčí,
- protected – přístupné jen z třídy a jejích potomků,
- private – přístupné pouze z třídy samotné. Privátní atributy a metody jsou přístupné pouze z metod třídy, což umožňuje skrýt
vnitřní stav objektu. Přístupové metody se obvykle nazývají gettery (slouží k získání hodnoty) a settery (slouží k nastavení hodnoty) a umožňují kontrolovat přístup k atributům. Příkladem getteru a setteru v C++:

```
class Auto {
private :
int rychlost ;
public :
int getRychlost () { // Getter
return rychlost ;
}
void setRychlost (int r) { // Setter
if (r >= 0) {
rychlost = r;
}
}
};
```

V Pythonu není zapouzdření striktně vynuceno, ale konvenčně se private prvky označují podtržítkem:

```
class Auto:
def __init__ (self , rychlost ):
self. _rychlost = rychlost       # Konvencne privatni
```

```
def get_rychlost (self): # Getter
return self. _rychlost
```

```
def set_rychlost (self , r):     # Setter
if r >= 0:
self. _rychlost = r
```

Modernějším přístupem v Pythonu je použití dekorátorů @property pro vytvoření getterů a setterů:

```
class Auto:
def __init__ (self , rychlost ):
self. _rychlost = rychlost

@property
def rychlost (self): # Getter
return self. _rychlost
```

## 9. @rychlost . setter

```
def rychlost (self , r): # Setter
if r >= 0:
self. _rychlost = r
```

Zapouzdření je jedním z pilířů OOP a umožňuje vytváření robustních a bezpečných aplikací.

## 3. Dědičnost a polymorfismus

### 3.1 Princip dědičnosti

Dědičnost je mechanismus, kterým nová třída (odvozená třída, potomek) zdědí vlastnosti a chování z již existující třídy (základní třída, rodič). Dědičnost umožňuje vytvářet hierarchie tříd a znovu používat kód. Základní třída (rodičovská třída) obsahuje obecné vlastnosti a metody, které jsou společné pro skupinu objektů. Odvozená třída zdědí všechny veřejné a chráněné prvky základní třídy a může je rozšířit novými atributy a metodami.

Příklady z reálného světa: Zvíře je rodičovská třída, Pes nebo Kočka jsou odvozené třídy (potomci). Auto je rodičovská třída, OsobníAuto nebo NákladníAuto jsou odvozené třídy (potomci).

Při dědičnosti může odvozená třída přidat nové metody a atributy, které nejsou v základní třídě, a také může překrýt (override) metody základní třídy, aby poskytla specifické chování. Příklad v C++:

```
// Zakladni trida ( rodicovska trida )
class Zvire {
protected :
string jmeno ;

public:
Zvire ( string j) : jmeno (j) {}

void zvuk () {
cout << jmeno << " vydava zvuk." << endl;
}
};
```

```
// Odvozen a trida ( potomek )
class Pes : public Zvire {
public :
Pes( string j) : Zvire (j) {}
void zvuk () { // Prekryti metody
cout << jmeno << " šětká." << endl;
}
};
```

Příklad v Pythonu:

```
# Zakladni trida ( rodicovska trida)
class Zvire :
def __init__ (self , jmeno ):
self. jmeno = jmeno
```

```
def zvuk(self):
print (f"{self.jmeno } vydava zvuk.")
```

```
# Odvozen a trida ( potomek )
class Pes( Zvire ): # Dedi z Zvire
def zvuk(self): # Prekryti metody
print (f"{self.jmeno } šětká.")
```

V obou příkladech Pes dědí z Zvire a přepisuje metodu zvuk() , aby poskytla specifické chování pro psy.

> **Poznámka**
>
> V některých jazycích je možné dědit z více tříd (vícenásobná dědičnost), což umožňuje kombinovat chování z různých zdrojů, ale může také vést k problémům s konflikty metod (např. v C++).

### 3.2 Polymorfismus a přetěžování metod

Polymorfismus (mnohočetnost forem) umožňuje objektům různých typů reagovat na stejný příkaz různě. Stejné volání metody se chová odlišně v závislosti na typu objektu.

Příklady z reálného světa: Když řeknete ”zvuk”, pes může štěkat, kočka může mňoukat, a pták může zpívat. Všechny tyto objekty reagují na stejnou metodu zvuk() , ale chovají se odlišně.

Příklad v C++:

```
Zvire* zvire1 = new      Zvire ("Zvíře");
Zvire* zvire2 = new      Pes("Rex");
zvire1 ->zvuk (); //     Vystup : Zvire vydava zvuk.
zvire2 ->zvuk (); //     Vystup : Rex steka .
delete zvire1 ;
delete zvire2 ;
```

Příklad v Pythonu:

```
zvire1 = Zvire ("Zvíře")
zvire2 = Pes("Rex")
```

```
zvire1 .zvuk ()   # Vystup : Zvire vydava zvuk.
zvire2 .zvuk ()   # Vystup : Rex steka.
```

Ačkoliv se obě volání jmenují zvuk() , chování se liší – to je polymorfismus. Přetěžování metod znamená, že metoda se stejným jménem může v jedné třídě existovat s různými parametry (různými typy nebo počtem argumentů). Přetěžování umožňuje definovat více verzí stejné metody pro různé situace. Příklad v C++:

```
class Kalkulator {
public :
int secti (int a, int b) {
return a + b;
}
```

```
double secti ( double a, double b) {          // Pretezovani
return a + b;
}
};
```

Příklad volání přetížených metod:

```
Kalkulator k;
cout << k. secti (3, 4);              // Vola int verzi
cout << k. secti (3.5 , 4.2);       // Vola double verzi
```

V Pythonu není přetěžování metod podporováno jako v jazyce C++, ale lze jej simulovat pomocí výchozích parametrů nebo proměnného počtu argumentů:

```
class Kalkulator :
def secti (self , a, b=None , c=None):
if c is not None:
return a + b + c
elif b is not None:
return a + b
else:
return a
```

### 3.3 Opětovné použití kódu

Dědičnost a polymorfismus umožňují výrazně snížit opakování kódu:

- společný kód se napíše jednou v základní třídě,
- odvozené třídy jej zdědí a nemusí jej psát znovu,
- specializace se provádí překrytím metod. Tento přístup vede k:
- menšímu množství kódu,
- snadnější údržbě – změna v základní třídě se automaticky promítne do všech potomků,
- lepší organizaci – třídy jsou logicky hierarchicky uspořádány. Příklad hierarchie tříd v OOP:

Vozidlo (základní třída) ��� Auto ��� OsobníAuto ��� NákladníAuto ��� Motocykl

Všechny třídy mohou dědit například metodu urychlit() z Vozidla , ale každá ji může implementovat jinak.

## 4. Vytváření objektů, možnosti práce s objekty a s pamětí v různých jazycích

### 4.1 Vznik objektu v paměti

Když se vytváří objekt, dochází k několika procesům: 1. přidělení paměti – operační systém přidělí potřebné místo v paměti, 2. inicializace – konstruktor inicializuje atributy objektu, 3. reference – objekt je dostupný skrze proměnnou (referenci nebo ukazatel). V C++ se objekt vytváří dvěma způsoby:

```
// Vytvoreni na zasobniku ( stack)
Osoba osoba1 ("Alice ", 25);
```

```
// řVytvoen í na ěhald (heap) –ž vyaduje ukazatel
Osoba * osoba2 = new Osoba ("Bob", 30);
```

Objekt na zásobníku se automaticky zruší, když opustí svůj obor platnosti. Objekt na haldě zůstává, dokud není explicitně zrušen pomocí delete :

```
delete osoba2 ;     // Uvolneni pameti
```

Rozdíl mezi stackem (zásobník) a heapem (halda): Stack – rychlejší, ale omezený velikostí a životností (objekt existuje pouze v rámci bloku kódu). Heap – pomalejší, ale flexibilnější (objekt může existovat, dokud není explicitně zrušen).

V Pythonu se objekty vždy vytváření na haldě a proměnné jsou pouze odkazy na tyto objekty:

```
osoba1 = Osoba ("Alice ", 25)        # Automaticky na halde
osoba2 = Osoba ("Bob", 30)
```

Díky automatické správě paměti v Pythonu se programátor nemusí starat o přidělování a uvolňování paměti.

### 4.2 Hodnota vs. reference

V C++ rozlišujeme:

- hodnotový přístup – proměnná obsahuje přímo hodnotu objektu, kopíruje se celý obsah,
- referenční přístup – proměnná obsahuje adresu objektu v paměti, nekopíruje se. 

Příklad:

```
Osoba osoba1 ("Alice ", 25);
Osoba osoba2 = osoba1 ; // Hodnotov ý řpístup – kopie
osoba2 . jmeno = " Alice2 "; // osoba1 se nezmeni
```

```
Osoba *ptr1 = & osoba1 ; // čReferenn í řpístup – adresa objektu
Osoba *ptr2 = ptr1;        // ptr2 ukazuje na stejny objekt
ptr2 ->jmeno = " Alice3 "; // osoba1 se zmeni
```

V Pythonu jsou všechny objekty referenční (vždy se předává odkaz):

```
osoba1 = Osoba ("Alice ", 25)
osoba2 = osoba1 # Odkaz na stejny objekt
osoba2 . jmeno = " Alice2 " # osoba1 se take zmeni
```

### 4.3 Správa paměti

C++ – Explicitní správa V C++ programátor sám odpovídá za přidělení a uvolnění paměti. Objekty na haldě se vytváří pomocí new a ruší pomocí delete :

```
Osoba * osoba = new Osoba ("Alice ", 25);
// Pouziti objektu
delete osoba ; // Manualni uvolneni
```

Zapomenutí delete vede k úniku paměti (memory leak), kdy paměť zůstává obsazena zbytečně. K automatizaci správy paměti se v moderním C++ používají inteligentní ukazatele:

```
std :: unique_ptr <Osoba > osoba (new Osoba ("Alice ", 25));
// Pamet se automaticky uvolni , kdyz unique_ptr opusti obor
```

Python – Automatická správa Python automaticky spravuje paměť pomocí garbage collectoru, který sleduje, které objekty jsou ještě používány. Jakmile se objekt přestane používat, je automaticky odstraněn:

```
osoba = Osoba (" Alice", 25)
# Python automaticky uvolni pamet , kdyz osoba uz neni potreba
```

Programátor se nemusí starat o delete či free .

### 4.4 Zrušení objektu a destruktor

Destruktor se volá automaticky, když se objekt maže. V C++ se volá při delete nebo když objekt opustí obor:

```
{
Osoba osoba (" Alice", 25);
// destruktor se vola na konci bloku
}
```

V Pythonu se destruktor volá, když garbage collector detekuje, že objekt není už nikde referován. Je však důležité poznamenat, že v Pythonu není zaručeno, kdy přesně se destruktor __del__ zavolá, protože závisí na implementaci garbage collectoru.

## 5. Další aplikace principů OOP: abstraktní třídy, rozhraní

### 5.1 Abstraktní třídy

Abstraktní třída je třída, kterou nelze bezprostředně instancovat. Slouží jako šablona pro odvozené třídy a definuje společné rozhraní.

Příklady z reálného světa: Zvíře může být abstraktní třída, protože nemůžeme mít konkrétní zvíře bez specifikace druhu. Místo toho můžeme mít odvozené třídy jako Pes , Kočka , které implementují konkrétní chování. Vozidlo může být abstraktní třída, protože nemůžeme mít konkrétní vozidlo bez specifikace typu. Místo toho můžeme mít odvozené třídy jako Auto , Motocykl , které implementují konkrétní chování.

Abstraktní třída obsahuje abstraktní metody – metody bez implementace, které musí být implementovány v odvozených třídách. Příklad v C++:

```
class Zvire { // Abstraktni trida
public :
virtual void zvuk () = 0; // Ciste virtualni – abstraktn í
```

metoda

```
virtual ~ Zvire () {}
};
```

```
class Pes : public Zvire {
public :
void zvuk () { // Povinna implementace
cout << "Šětkání" << endl;
}
};
```

```
// Zvire z; // Chyba – nelze instancovat
Pes p; // OK
```

Příklad v Pythonu s použitím modulu abc :

```
from abc import ABC, abstractmethod
class Zvire (ABC): # Abstraktni trida
@abstractmethod
def zvuk(self): # Abstraktni metoda
  pass
```

```
# z = Zvire () # Chyba
class Pes( Zvire ):
def zvuk(self): # Povinna implementace
  print ("Šětkání")
```

V obou příkladech Zvire je abstraktní třída, která definuje abstraktní metodu zvuk() . Odvozená třída Pes musí tuto metodu implementovat, jinak by také byla abstraktní. Abstraktní třídy vynucují, aby všechny odvozené třídy implementovaly určitá chování.

### 5.2 Rozhraní (Interface)

Rozhraní definuje sadu metod, které třídy musí implementovat.

Příklady z reálného světa: Pohyblivý může být rozhraní, které definuje metody jako pohni_se() , zastav() . Různé třídy jako Auto , Pes , Robot mohou implementovat toto rozhraní a poskytovat vlastní implementaci těchto metod. Rozhraní tak umožňuje různým třídám sdílet společné chování, aniž by musely být ve stejné hierarchii dědičnosti.

V C++ se rozhraní simuluje pomocí abstraktní třídy obsahující pouze abstraktní metody:

```
class Vozidlo { // Rozhrani
public :
virtual void urychlit () = 0;
virtual void zastavit () = 0;
virtual ~ Vozidlo () {}
};
```

```
class Auto : public Vozidlo {
public :
void urychlit () { cout << "Auto akceleruje ." << endl; }
void zastavit () { cout << "Auto brzdí." << endl; }
};
```

V Pythonu se používá abstraktní třída s metodami:

```
from abc import ABC, abstractmethod
class Vozidlo (ABC):
@abstractmethod
def urychlit (self):
pass
```

```
@abstractmethod
def zastavit (self):
pass
```

```
class Auto( Vozidlo ):
def urychlit (self):
print ("Auto akceleruje .")
```

```
def zastavit (self):
print ("Auto brzdí.")
```

Rozhraní zajišťují, že různé třídy disponují jednotným chováním.

## 6 Návrh objektového programu

### 6.1 Objekty spolupracují, neexistují izolovaně

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

## 6.2 Dědičnost a kompozice: „je“ versus „má“

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

### 6.3 Každá třída by měla mít srozumitelnou odpovědnost

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

### 6.4 Od tříd ke struktuře celé aplikace

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

### 6.5 Návrhové vzory: osvědčená řešení opakujících se problémů

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

