# Datové struktury a soubory

## 1. Strukturované datové typy a ukazatele

### 1.1 Strukturované datové typy

Skalární datové typy reprezentují jednotlivé hodnoty, například celá čísla (int), desetinná čísla (float) nebo znaky (char). Každá proměnná skalárního typu obsahuje právě jednu hodnotu.

Pojem ”skalární”pochází z matematiky a znamená ”jednoduchý”nebo ”nekompozitní”. Skalární datové typy jsou základními stavebními kameny pro vytváření složitějších datových struktur. Věk je skalární datový typ, protože představuje jednu hodnotu (například 25). Teplota je skalární datový typ, protože představuje jednu hodnotu (například 36.5 °C).

Opakem skalárních datových typů jsou strukturované datové typy, které mohou obsahovat více hodnot uspořádaných podle určitého pravidla. Strukturované datové typy umožňují ukládat více hodnot uspořádaných podle určitého pravidla. Strukturované typy poskytují způsob organizace dat do logických celků, což zjednodušuje práci se složitějšími datovými strukturami.

Příklady z reálného světa: Osoba může být strukturovaný datový typ, který obsahuje atributy jako jmeno , vek , mesto . Každý atribut představuje jednu vlastnost osoby, a všechny tyto vlastnosti dohromady tvoří komplexní datovou strukturu.

Základní typy strukturovaných dat zahrnují:

- pole – uspořádaná kolekce prvků stejného typu,
- záznamy (struktury) – kolekce prvků různých typů,
- seznamy – dynamické kolekce prvků,
- slovníky – kolekce párů klíč-hodnota.

### 1.2 Pole jako základní datová struktura

Pole je základní strukturovaný datový typ, který uchovává pevný počet prvků stejného typu uspořádaných v posloupnosti. Každý prvek pole je přístupný pomocí indexu, což je číselná pozice prvku v poli. Vlastnosti pole:

- všechny prvky mají stejný datový typ,
- prvky jsou uloženy v paměti za sebou,
- přístup k prvkům je rychlý díky indexování,
- velikost pole je obvykle stanovena při vytvoření. Indexování v poli:
- v jazycích C a C++ se indexuje od nuly,
- první prvek má index 0 , druhý index 1 atd.
- přístup k prvku se provádí pomocí hranatých závorek, například pole[0] pro první prvek.

> **Poznámka**
>
> V Pythonu tradiční pole nahrazují seznamy ( list ), které jsou dynamické a mohou obsahovat prvky různých typů, ale základní princip indexování zůstává stejný. Pole v Pythonu lze simulovat pomocí modulu array , který poskytuje efektivní pole pro základní datové typy.

Příklad v Pythonu s modulem array :

```
import array
# Vytvoreni pole celych cisel
cisla = array . array ('i', [10 , 20, 30, 40, 50])
print (cisla [0]) # Vystup : 10
```

Schematické znázornění pole:

Index: 0 1 2 3 4 Hodnota: [10] [20] [30] [40] [50] ^

```text
|
```

adresa v paměti

### 1.3 Statické pole

Statické pole má velikost pevně stanovenou při deklaraci a nelze ji během běhu programu změnit. Paměť pro statické pole je alokována při vytvoření proměnné. Příklad v jazyce C:

```
int cisla [5]; // Pole s 5 prvky typu int
cisla [0] = 10;
cisla [1] = 20;
cisla [2] = 30;

// Inicializace pri deklaraci

int hodnoty [5] = {10 , 20, 30, 40, 50};
```

### 1.4 Dynamické pole

Dynamické pole umožňuje měnit svou velikost během běhu programu. Paměť se alokuje dynamicky podle potřeby, což poskytuje větší flexibilitu při práci s daty neznámého rozsahu. V jazyce C se dynamická alokace provádí pomocí funkcí malloc a free :

```
# include <stdlib .h>
int *pole;
int velikost = 5;
```

```
// Dynamicka alokace pameti
pole = (int *) malloc ( velikost * sizeof (int));
```

```
// Pouziti pole
pole [0] = 10;
pole [1] = 20;
```

```
// Uvolneni pameti
free(pole);
```

V Pythonu jsou seznamy (list) dynamické automaticky:

```
cisla = [] # Prazdny seznam
cisla. append (10) # Pridani prvku
cisla. append (20)
cisla. append (30)
# Seznam automaticky roste podle potreby
```

### 1.5 Ukazatele a pole

Ukazatel je proměnná, která uchovává adresu v paměti, kde je uložena jiná hodnota. Ukazatele jsou klíčové při práci s dynamickými datovými strukturami. V jazyce C existuje úzký vztah mezi poli a ukazateli:

```
int pole [5] = {10 , 20, 30, 40, 50};
int * ukazatel = pole; // Ukazatel na prvni prvek
```

```
// Pristup pomoci ukazatele
printf ("%d\n", * ukazatel );     // Vystup : 10
printf ("%d\n", *( ukazatel + 1)); // Vystup : 20
```

Název pole v jazyce C funguje jako ukazatel na jeho první prvek. To umožňuje efektivní práci s pamětí, ale vyžaduje opatrnost při manipulaci.

### 1.6 Matice (vícerozměrná pole)

Matice je vícerozměrné pole, nejčastěji dvourozměrné, které lze chápat jako tabulku hodnot s řádky a sloupci. Příklad v jazyce C:

```
int matice [3][4];       // Matice 3 radky x 4 sloupce
```

```
// Inicializace
int cisla [2][3] = {
{1, 2, 3},
{4, 5, 6}
};
```

```
// Pristup k prvkum
cisla [0][0] = 10; // Prvni radek , prvni sloupec
cisla [1][2] = 60; // Druhy radek , treti sloupec
```

Příklad v Pythonu:

```
# Vnorene seznamy jako matice
matice = [
[1, 2, 3],
[4, 5, 6]
]
```

```
# Pristup k prvkum
matice [0][0] = 10 # Prvni radek , prvni sloupec
matice [1][2] = 60 # Druhy radek , treti sloupec
```

Schematické znázornění matice:

sloupec 0 sloupec 1 sloupec 2 řádek 0 [1] [2] [3] řádek 1 [4] [5] [6]

Matice se používají v mnoha oblastech, například při reprezentaci obrazu, řešení soustav rovnic, grafice nebo zpracování tabulkových dat.

## 2. Znakové řetězce

### 2.1 Znakové řetězce jako datový typ

Znakový řetězec (string) je posloupnost znaků reprezentující text. Řetězce patří mezi nejpoužívanější datové typy, protože většina programů pracuje s textovými daty. Reprezentace řetězců se liší mezi programovacími jazyky:

- v jazyce C je řetězec pole znaků ukončené speciálním znakem,
- v Pythonu je řetězec samostatný datový typ s mnoha vestavěnými metodami.

### 2.2 Řetězce v jazyce C

V jazyce C je řetězec implementován jako pole znaků typu char , které je ukončeno nulovým znakem '\0' . Tento ukončující znak signalizuje konec řetězce a umožňuje funkcím určit délku řetězce. Příklad:

```
char pozdrav [6] = {'A', 'h', 'o', 'j', '!', '\0 '};
```

```
// Zkraceny zapis ukoncovaci znak se prida automaticky
char text [] = "Ahoj!";
```

Reprezentace v paměti:

Index: 0 1 2 3 4 5 Znak: 'A' 'h' 'o' 'j' '!' '\0'

Práce s řetězci v jazyce C vyžaduje použití funkcí ze standardní knihovny <string.h> :

```
# include <string .h>
# include <stdio .h>
```

```
char text1 [20] = "Ahoj";
char text2 [20] = " svete";
```

```
// Delka retezce
int delka = strlen ( text1 );      // Vysledek : 4
```

```
// Kopirovani retezce
strcpy (text1 , "Novy text");
```

```
// Spojeni retezcu
strcat (text1 , text2 );     // text1 = "Novy text svete"
```

```
// Porovnani retezcu
int vysledek = strcmp (text1 , text2 );            // 0 = stejne , <0 nebo >0 = ruzne
```

Základní funkce pro práce s řetězci v C:

- strlen(str) – vrací délku řetězce,
- strcpy(dest, src) – kopíruje řetězec,
- strcat(dest, src) – připojuje řetězec,
- strcmp(str1, str2) – porovnává řetězce,
- strchr(str, ch) – hledá znak v řetězci.

### 2.3 Řetězce v Pythonu

V Pythonu je řetězec objektem typu str , který poskytuje mnoho vestavěných metod pro manipulaci s textem. Řetězce v Pythonu jsou neměnné (immutable) – jakmile jsou vytvořeny, nelze změnit jejich obsah, ale lze vytvořit nové řetězce. Příklad:

```
text = "Ahoj!"
dalsi_text = 'Python '
```

```
# Spojeni retezcu
spojen = text + " " + dalsi_text               # "Ahoj! Python "
```

```
# Delka retezce
delka = len(text)      # 5
```

```
# Pristup k znakum pomoci indexu
prvni_znak = text [0] # 'A'
posledni_znak = text [ -1] # '!'
```

```
# Vyriznuti podretezce ( slicing )
cast = text [0:4] # "Ahoj"
```

Základní metody pro práci s řetězci v Pythonu:

```
text = "Ahoj Svete"
```

```
# Prevod na velka /mala pismena
velky = text. upper ()    # "AHOJ SVETE "
maly = text. lower ()     # "ahoj svete "
```

```
# Hledani podretezce
pozice = text.find("Svete ")        # 5
obsahuje = "Svete " in text         # True
```

```
# Rozdeleni retezce
slova = text. split (" ")    # [" Ahoj", " Svete "]
```

```
# Nahrazeni podretezce
novy = text. replace ("Ahoj", " Nazdar ")      # " Nazdar Svete "
```

```
# Odstraneni bilych znaku
text2 = " text "
cisteny = text2 . strip () # "text"
```

### 2.4 Srovnání práce s řetězci

Hlavní rozdíly mezi jazyky C a Python:

Aspekt C Python Reprezentace Pole znaků s '\0' Objekt typu str Měnitelnost Měnitelné Neměnné Délka Musí se vypočítat (strlen) Vestavěná funkce len() Spojení strcat() Operátor + Bezpečnost Riziko přetečení bufferu Automatická správa paměti

Python nabízí pohodlnější a bezpečnější práci s řetězci díky vysokoúrovňovým abstrakcím, zatímco C poskytuje větší kontrolu nad pamětí, ale vyžaduje opatrnější přístup.

## 3. Regulární výrazy a jejich využití při práci s textem

### 3.1 Princip regulárních výrazů

Regulární výraz (regular expression, regex) je vzor definující množinu řetězců. Regulární výrazy poskytují mocný nástroj pro vyhledávání, ověřování a manipulaci s textem na základě definovaných pravidel. Regulární výrazy umožňují:

- vyhledávat řetězce odpovídající danému vzoru,
- ověřovat správnost formátu dat (validace),
- extrahovat části textu,
- nahrazovat text podle vzoru.

### 3.2 Základní konstrukce regulárních výrazů

Regulární výrazy používají speciální znaky a konstrukce pro definování vzorů: Literály – běžné znaky odpovídají samy sobě:

- abc – odpovídá řetězci ”abc” Metaznaky – speciální znaky s významem:
- . – jakýkoliv znak
- ̂ – začátek řetězce
- $ – konec řetězce
- * – 0 nebo více opakování
- + – 1 nebo více opakování
- ? – 0 nebo 1 výskyt
- | – alternativa (nebo)

Třídy znaků – definují množinu znaků:

- [abc] – znak a, b nebo c
- [0-9] – jakákoliv číslice
- [a-z] – jakékoli malé písmeno
- \d – číslice (digit)
- \w – alfanumerický znak
- \s – bílý znak (mezera, tabulátor)

Kvantifikátory – určují počet opakování:

- {n} – přesně n opakování
- {n,} – n nebo více opakování
- {n,m} – mezi n a m opakování

### 3.3 Použití regulárních výrazů v Pythonu

Python poskytuje modul re pro práci s regulárními výrazy:

```
import re
text = " Kontakt : email@example .com , telefon : 123 -456 -789"
```

```
# Vyhledani emailove adresy
email_vzor = r'\w+@\w+\.\w+'
email = re. search ( email_vzor , text)
if email :
print ( email . group ()) # Vystup : email@example .com
```

```
# Vyhledani vsech cislic
cisla = re. findall (r'\d+', text)
print (cisla ) # ['123', '456', '789 ']
```

```
# Kontrola formatu
telefon = "123 -456 -789"
vzor_telefonu = r'^\d{3} -\d{3} -\d{3}$'
if re.match ( vzor_telefonu , telefon ):
print (" Platné telefonn í číslo")
```

Běžné operace s regulárními výrazy:

```
# Hledani prvniho vyskytu
vysledek = re. search (vzor , text)
```

```
# Hledani vsech vyskytu
vse = re. findall (vzor , text)
```

```
# Kontrola od zacatku retezce
shoda = re. match (vzor , text)
```

```
# Nahrazeni podle vzoru
novy_text = re.sub(vzor , nahrada , text)
```

### 3.4 Praktické příklady

Validace emailové adresy:

```
email_vzor = r'^[a-zA -Z0 -9._%+ -]+@[a-zA -Z0 -9. -]+\.[a-zA -Z]{2 ,}$'
email = " uzivatel@example .com"
```

```
if re.match ( email_vzor , email ):
print (" Platný email ")
```

Extrakce dat z textu:

```
text = "Datum : 15.01.2026 , cena: 1500 čK"
datum = re. search (r'\d {2}\.\ d {2}\.\ d{4} ', text)
cena = re. search (r'\d+', text)
print (datum . group ()) # 15.01.2026
```

Nahrazení citlivých dat:

```
text = "Číslo karty : 1234-5678-9012-3456"
anonymizovano = re.sub(r'\d{4} -\d{4} -\d{4} -\d{4} ', 'XXXX-XXXX-XXXX-XXXX ', text)
print ( anonymizovano ) # Cislo karty : XXXX -XXXX -XXXX -XXXX
```

### 3.5 Oblasti využití

Regulární výrazy se používají v mnoha oblastech:

- validace vstupů – ověření formátu emailů, telefonních čísel, hesel,
- zpracování logů – extrakce informací ze souborů protokolů,
- čištění dat – odstranění nechtěných znaků nebo normalizace formátu,
- vyhledávání v textu – pokročilé hledání v editorech a nástrojích,
- web scraping – extrakce dat z HTML stránek. Regulární výrazy jsou mocný nástroj, ale jejich složitost může činit kód méně čitelným.

Proto je důležité používat je uvážlivě a dokumentovat složitější vzory.

## 4. Datov0 soubory a jejich význam v programování

### 4.1 Význam souborů v programování

Soubor je pojmenovaná oblast na trvalém úložišti (disk, USB), která uchovává data. Soubory umožňují programům:

- uchovávat data i po ukončení programu,
- sdílet data mezi různými programy,
- zpracovávat velké objemy dat, které by se nevešly do paměti najednou,
- vytvářet trvalé záznamy a logy.

### 4.2 Textové a binární soubory

Textové soubory obsahují data reprezentovaná jako znaky čitelné člověkem. Každý řádek je obvykle ukončen speciálním znakem pro nový řádek. Textové soubory lze otevřít a číst v běžném textovém editoru. Příklady textových souborů:

- .txt – prostý text,
- .csv – tabulková data oddělená čárkami,
- .html , .xml , .json – strukturované textové formáty. 

Binární soubory obsahují data v binární podobě, která není přímo čitelná člověkem.
Jsou efektivnější pro ukládání velkých objemů dat nebo složitých struktur. 

Příklady binárních souborů:

- .exe – spustitelné soubory,
- .jpg , .png – obrázky,
- .mp3 , .wav – zvukové soubory,
- .bin , .dat – obecná binární data.

### 4.3 Základní operace se soubory

Práce se soubory typicky zahrnuje čtyři základní kroky: 1. Otevření souboru – vytvoření spojení mezi programem a souborem. 2. Čtení nebo zápis – manipulace s daty. 3. Zpracování dat – operace s načtenými daty. 4. Uzavření souboru – uvolnění prostředků.

### 4.4 Práce se soubory v jazyce C

V jazyce C se používají souborové ukazatele typu FILE* pro práci se soubory. Hlavičkový soubor <stdio.h> obsahuje funkce pro vstup a výstup.

Otevření souboru:

```
# include <stdio .h>
FILE * soubor ;
soubor = fopen ("data.txt", "r");            // "r" = cteni
```

```
if ( soubor == NULL) {
printf ("Chyba řpi otevírání souboru \n");
return 1;
}
```

Režimy otevření souboru:

- "r" – čtení (soubor musí existovat),
- "w" – zápis (vytvoří nový nebo přepíše existující),
- "a" – připojení (zápis na konec souboru),
- "r+" – čtení i zápis.

Čtení ze souboru:

```
char radek [100];

// Cteni radku
while ( fgets (radek , 100 , soubor ) != NULL) {
printf ("%s", radek );
}
```

```
// Cteni jednotlivych znaku
int znak;
while (( znak = fgetc ( soubor )) != EOF) {
putchar (znak);
}
```

Zápis do souboru:

```
FILE * soubor = fopen (" vystup .txt", "w");
fprintf (soubor , "Text: %s\n", "Ahoj");
fprintf (soubor , "Číslo: %d\n", 42);
```

Uzavření souboru:

```
fclose ( soubor );      // Dulezite pro uvolneni prostredku
```

### 4.5 Práce se soubory v Pythonu

Python poskytuje vestavěné funkce pro práci se soubory a doporučuje použít kontextový manažer (with), který automaticky uzavře soubor. Čtení ze souboru:

```
# Bezpecny zpusob - automaticke uzavreni
with open("data.txt", "r", encoding ="utf -8") as soubor :
obsah = soubor .read () # Cely obsah
print ( obsah )
```

```
# Cteni po radcich
with open("data.txt", "r", encoding ="utf -8") as soubor :
for radek in soubor :
print ( radek . strip ()) # strip () odstrani \n
```

```
# Nacteni vsech radku do seznamu
with open("data.txt", "r", encoding ="utf -8") as soubor :
radky = soubor . readlines ()
```

Zápis do souboru:

```
# Zapis prepise existujici soubor
with open(" vystup .txt", "w", encoding ="utf -8") as soubor :
soubor . write ("První řádek\n")
soubor . write ("Druhý řádek\n")
```

```
# Pripojeni na konec souboru
with open(" vystup .txt", "a", encoding ="utf -8") as soubor :
soubor . write ("šDalí řádek\n")
```

Režimy otevření v Pythonu:

- "r" – čtení (výchozí),
- "w" – zápis (přepíše existující),
- "a" – připojení,
- "r+" – čtení i zápis,
- "b" – binární režim (např. "rb" , "wb" ).

### 4.6 Srovnání práce se soubory

Aspekt C Python Otevření fopen() open() Čtení fgets() , fgetc() read() , readline() Zápis fprintf() , fputc() write() Uzavření Manuální fclose() Automatické s with Bezpečnost Vyžaduje kontrolu Jednodušší správa chyb

Python nabízí pohodlnější a bezpečnější práci se soubory díky automatické správě prostředků, zatímco C poskytuje nižší úroveň kontroly.

## 5. Nejpoužívanější typy datových formátů

### 5.1 Význam strukturovaných datových formátů

Při ukládání a přenosu dat mezi programy nebo systémy je důležité používat standardizované formáty, které zajistí:

- přenositelnost – data lze sdílet mezi různými programy a platformami,
- čitelnost – strukturovaná data jsou srozumitelnější,
- parsovatelnost – programy mohou data snadno načíst a zpracovat,
- interoperabilitu – různé systémy mohou spolupracovat.

### 5.2 CSV (Comma-Separated Values)

CSV je jednoduchý textový formát pro ukládání tabulkových dat. Každý řádek souboru odpovídá jednomu záznamu a hodnoty jsou odděleny čárkami (nebo jinými oddělovači). Příklad CSV souboru:

jmeno,vek,mesto Alice,25,Praha Jan,30,Brno Ludmila,22,Ostrava

Vlastnosti CSV:

- jednoduchost – snadné vytvoření i ruční editace,
- kompaktnost – malá velikost souborů,
- široká podpora – většina nástrojů CSV podporuje,
- omezení – obtížné ukládání hierarchických nebo vnořených dat. Práce s CSV v Pythonu:

```
import csv

# Cteni CSV
with open("data.csv", "r", encoding ="utf -8") as soubor :
ctenar = csv. reader ( soubor )
hlavicka = next( ctenar ) # Prvni radek
for radek in ctenar :
print ( radek ) # [' Alice ', '25', 'Praha ']
```

```
# Zapis CSV
with open(" vystup .csv", "w", newline ="", encoding ="utf -8") as
```

soubor :

```
zapisovac = csv. writer ( soubor )
zapisovac . writerow ([" jmeno", "vek", "mesto "])
zapisovac . writerow ([" David", "28", "ňPlze"])
```

CSV se používá pro:

- export dat z tabulkových procesorů,
- výměnu dat mezi databázemi,
- statistické zpracování dat,
- logy a reporty.

### 5.3 XML (eXtensible Markup Language)

XML je značkovací jazyk určený pro strukturované ukládání dat. Používá značky (tagy) pro definování hierarchie a struktury dat. Příklad XML souboru:

```
<?xml version ="1.0" encoding ="UTF -8"?>
<osoby >
<osoba >
<jmeno >Alice </ jmeno >
<vek >25 </vek >
<mesto >Praha </ mesto >
</osoba >
<osoba >
<jmeno >Jan </ jmeno >
<vek >30 </vek >
<mesto >Brno </ mesto >
</osoba >
</osoby >
```

Vlastnosti XML:

- hierarchická struktura – stromová organizace dat,
- samodokumentující – názvy tagů popisují obsah,
- rozšiřitelnost – možnost definovat vlastní tagy,
- validace – lze ověřit strukturu pomocí schémat,
- rozvláčnost – větší velikost souborů kvůli opakujícím se tagům. XML se používá pro:
- konfigurační soubory,
- výměnu dat mezi systémy (SOAP webové služby),
- reprezentaci dokumentů (Office Open XML),
- ukládání komplexních datových struktur.

### 5.4 JSON (JavaScript Object Notation)

JSON je lehký textový formát pro výměnu dat založený na syntaxi JavaScriptu. Je čitelnější a kompaktnější než XML. Příklad JSON souboru:

```
{
"osoby ": [
{
" jmeno ": " Alice ",
"vek": 25,
" mesto ": " Praha "
},
{
" jmeno ": "Jan",
"vek": 30,
" mesto ": "Brno"
}
]
}
```

Vlastnosti JSON:

- jednoduchost – snadno čitelný i zapisovatelný,
- kompaktnost – menší velikost než XML,
- nativní podpora – přímo podporován v JavaScriptu,
- omezené datové typy – čísla, řetězce, objekty, pole, boolean, null. Práce s JSON v Pythonu:

```
import json
# Nacteni JSON
with open("data.json", "r", encoding ="utf -8") as soubor :
data = json.load( soubor )
print (data["osoby "][0][ "jmeno "]) # Alice
```

```
# Zapis JSON
data = {
"osoby ": [
{"jmeno ": " Ludmila ", "vek": 22, "mesto ": " Ostrava "}
]
}
with open(" vystup .json", "w", encoding ="utf -8") as soubor :
json.dump(data , soubor , indent =2, ensure_ascii = False )
```

JSON se používá pro:

- RESTful API komunikaci,
- konfigurační soubory,
- ukládání strukturovaných dat,
- výměnu dat mezi webovými aplikacemi.

### 5.5 YAML (YAML Ain’t Markup Language)

YAML je lidsky čitelný formát pro serializaci dat. Klade důraz na jednoduchost a čitelnost, používá odsazení místo složených závorek. Příklad YAML souboru:

osoby: - jmeno: Alice vek: 25 mesto: Praha - jmeno: Jan vek: 30 mesto: Brno

Vlastnosti YAML:

- čitelnost – velmi přehledný pro člověka,
- minimalistický – méně syntaktických značek,
- podpora komentářů – označeny # ,
- citlivost na odsazení – struktura je určena odsazením. YAML se používá pro:
- konfigurační soubory (Docker, Kubernetes),
- definice CI/CD pipeline,
- nastavení aplikací,
- dokumentaci struktury dat.

### 5.6 Srovnání formátů

Formát Čitelnost Velikost Složitost Typické využití CSV Vysoká Malá Nízká Tabulková data XML Střední Velká Vysoká Dokumenty, komplexní struktury JSON Vysoká Střední Střední Web API, konfigurace YAML Velmi vysoká Střední Střední Konfigurace, DevOps

Volba formátu závisí na konkrétních požadavcích projektu:

- CSV pro jednoduché tabulkové exporty,
- JSON pro moderní webové API,
- XML pro komplexní dokumenty a legacy systémy,
- YAML pro čitelné konfigurační soubory.

## 6. Další datové struktury

### 6.1 Datová struktura není jen „místo pro data“

Při programování nestačí rozhodnout, **jaká data chceme uložit**. Stejně důležité je, **jak s nimi budeme pracovat**.

Představme si například seznam návštěvníků školní akce. Pokud potřebujeme pouze postupně projít všechna jména, postačí jednoduchý seznam. Pokud ale chceme velmi často zjišťovat, zda se konkrétní člověk už zaregistroval, může být vhodnější jiná datová struktura.

Datová struktura tedy určuje nejen způsob uložení hodnot, ale také to, jak snadno lze provádět určité operace: vyhledat položku, přidat novou, odebrat starou nebo procházet data v určitém pořadí.

V předchozí části jsme se setkali s **polem**, kde jsou prvky uspořádány za sebou a přistupujeme k nim pomocí indexu. To je velmi vhodné například tehdy, když chceme rychle získat „pátou položku“. Pro jiné úlohy však existují vhodnější struktury.

Můžeme si to představit podobně jako různé způsoby ukládání věcí. Knihy ukládáme jinak než zákazníky čekající u pokladny a jinak než kontakty v telefonním seznamu. Ve všech případech ukládáme nějaké položky, ale způsob jejich organizace odpovídá tomu, co s nimi potřebujeme dělat.

Základní otázka při volbě datové struktury proto zní:

> Které operace budu s daty provádět nejčastěji?

### 6.2 Seznam, zásobník a fronta

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

### 6.3 Množina a slovník: když potřebujeme rychle hledat

Představme si program, který eviduje registrační čísla účastníků:

```python
registrace = [105, 203, 417, 562, 814]
```

Pokud chceme zjistit, zda se číslo `417` v seznamu nachází, můžeme seznam procházet, dokud jej nenajdeme.

U několika položek je to bezvýznamný rozdíl. U statisíců záznamů však může být výhodnější použít strukturu navrženou právě pro rychlé vyhledávání.

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

## 6.4 Stromy a grafy: když data vytvářejí vztahy

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

## 6.5 Jak vybrat vhodnou datovou strukturu

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

