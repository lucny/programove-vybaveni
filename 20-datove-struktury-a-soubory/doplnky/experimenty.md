# Experimenty

## 1. Strukturované datové typy a ukazatele
Tato kapitola vysvětluje pole, matice a ukazatele v jazycích C a Python. Následující experimenty vám pomohou tyto struktury vizualizovat v paměti.

**1. Sledování indexování pole krok za krokem**
*   **Nástroj:** [Python Tutor (Python režim)](https://pythontutor.com/)
*   **Postup:**
    1. Otevřete Python Tutor a zvolte jazyk Python.
    2. Vložte kód tvořící jednoduchý seznam: `moje_pole =`.
    3. Na další řádek přidejte `print(moje_pole)`.
    4. Klikněte na "Visualize Execution". Pomocí tlačítka "Next" krokujte program a na pravé obrazovce sledujte, jak se pole vytvoří a jak Python přistupuje k indexu 2.

**2. Vizualizace alokace pole v paměti jazyka C**
*   **Nástroj:** [Python Tutor (C režim)](https://pythontutor.com/c.html)
*   **Postup:**
    1. Přepněte prostředí na jazyk C.
    2. Napište krátký kód: `int main() { int pole = {10, 20, 30, 40, 50}; return 0; }`.
    3. Spusťte vizualizaci. V grafickém zobrazení paměti uvidíte, jak se prvky pole ukládají striktně za sebou.

**3. Simulace dynamické alokace a memory leaku v C**
*   **Nástroj:** [OnlineGDB (C Compiler)](https://www.onlinegdb.com/online_c_compiler)
*   **Postup:**
    1. V editoru vytvořte kód používající `malloc` k alokaci dynamického pole.
    2. Úmyslně na konec kódu nepřidejte funkci `free()` a program spusťte.
    3. Zamyslete se nad tím, co se stane v operačním systému. Následně kód opravte doplněním `free(ukazatel)` pro správné uvolnění paměti.

**4. Vícerozměrné pole jako matice**
*   **Nástroj:** MS Excel, Calc nebo [Google Sheets](https://docs.google.com/spreadsheets/)
*   **Postup:**
    1. Otevřete prázdnou tabulku. Tabulka je přirozenou reprezentací 2D matice.
    2. Do buněk A1 až C2 vepište čísla (vytvoříte matici 2x3 – 2 řádky, 3 sloupce).
    3. Sledujte, jak adresa buňky (např. B2) funguje naprosto stejně jako indexování vícerozměrného pole `matice`.

**5. Test ukazatelové aritmetiky**
*   **Nástroj:** [OnlineGDB (C Compiler)](https://www.onlinegdb.com/online_c_compiler)
*   **Postup:**
    1. Definujte statické pole `int cisla = {1, 2, 3};`.
    2. Vytvořte ukazatel na první prvek: `int *ptr = cisla;`.
    3. Vypište hodnotu pomocí `printf("%d", *(ptr + 1));`.
    4. Sledujte, že výstupem bude číslo 2, protože přičtení jedničky k ukazateli posune adresu na další prvek v poli.

**6. Výpočet délky dynamického seznamu**
*   **Nástroj:** [Repl.it (Python)](https://replit.com/)
*   **Postup:**
    1. Vytvořte nový Python projekt.
    2. Nadeklarujte dynamický seznam: `seznam = [1, "text", 3.14]` (všimněte si, že prvky mohou být různých typů).
    3. Zkuste připojit nový prvek pomocí `seznam.append(42)`.
    4. Použijte funkci `len(seznam)` a vytiskněte výsledek do konzole pro ověření změny velikosti.

---

## 2. Znakové řetězce
Znakové řetězce se chovají odlišně v jazycích C (pole znaků ukončené `\0`) a Python (neměnné objekty).

**1. Hledání nulového ukončovacího znaku v C**
*   **Nástroj:** [Python Tutor (C režim)](https://pythontutor.com/c.html)
*   **Postup:**
    1. Napište kód: `char pozdrav[] = "Ahoj";`.
    2. Spusťte vizualizátor a prozkoumejte sekci paměti.
    3. Uvidíte, že velikost pole je ve skutečnosti 5, přičemž pátý znak je přesně `\0` (nulový znak signalizující konec).

**2. Pochopení neměnnosti (immutability) v Pythonu**
*   **Nástroj:** [W3Schools Python Editor](https://www.w3schools.com/python/trypython.asp?filename=demo_default)
*   **Postup:**
    1. Do editoru zadejte: `slovo = "Ahoj"`.
    2. Pokuste se změnit první písmeno příkazem `slovo = "O"`.
    3. Spusťte kód a analyzujte chybovou hlášku *TypeError*, která dokazuje, že řetězce v Pythonu jsou neměnné.

**3. Převod textu na ASCII hodnoty**
*   **Nástroj:** [CyberChef](https://gchq.github.io/CyberChef/)
*   **Postup:**
    1. V levém panelu vyhledejte operaci "To Hex" nebo "To Decimal" a přetáhněte ji do sloupce "Recipe".
    2. Do pole "Input" vložte text `Ahoj!`.
    3. Ve výstupu uvidíte, pod jakými číselnými hodnotami jsou znaky fyzicky uloženy v paměti počítače (reprezentace v C).

**4. Rychlost a způsoby spojování řetězců**
*   **Nástroj:** [OnlineGDB (Python Compiler)](https://www.onlinegdb.com/online_python_compiler)
*   **Postup:**
    1. Definujte `str1 = "Ahoj "` a `str2 = "světe"`.
    2. Spojte je pomocí operátoru `+` do proměnné `vysledek`.
    3. Pomocí `print(vysledek)` ověřte, že se spojení podařilo (uvědomte si, že na pozadí Python musel vytvořit zcela nový objekt).

**5. Volání metod objektu `str` v Pythonu**
*   **Nástroj:** [Programiz Python Online](https://www.programiz.com/python-programming/online-compiler/)
*   **Postup:**
    1. Vytvořte řetězec obsahující nadbytečné mezery a malá písmena: `text = "  python je super  "`.
    2. Použijte na něj metodu `.strip()` k odstranění mezer na začátku a konci.
    3. Dále na výsledek aplikujte metodu `.upper()` k převodu na velká písmena a výsledek vypište.

**6. Porovnávání řetězců (C vs Python)**
*   **Nástroj:** [Online C Compiler](https://www.onlinegdb.com/)
*   **Postup:**
    1. Napište kód v C s využitím `<string.h>`.
    2. Vytvořte `char a[] = "Test";` a `char b[] = "Test";`.
    3. Zkuste je porovnat pomocí `if (a == b)`. Bude to fungovat? Nebude, protože porovnáváte adresy polí.
    4. Změňte podmínku na použití funkce `strcmp(a, b) == 0` pro správné porovnání obsahu.

---

## 3. Regulární výrazy a jejich využití při práci s textem
Tato kapitola představuje regexy jako mocný nástroj pro vyhledávání, extrakci a validaci textu.

**1. Interaktivní validace e-mailových adres**
*   **Nástroj:** [Regex101](https://regex101.com/)
*   **Postup:**
    1. Otevřete stránku a nastavte prostředí na Python.
    2. Do testovacího pole (Test String) vložte několik platných i neplatných e-mailů.
    3. Do pole "Regular Expression" začněte psát vzor využívající třídy znaků a kvantifikátory, např.: `[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`.
    4. Sledujte, jak pravý panel analyzuje a barevně zvýrazňuje jednotlivé shody.

**2. Extrakce telefonních čísel s modulem `re`**
*   **Nástroj:** [Pythex](https://pythex.org/)
*   **Postup:**
    1. Do pole "Your test string" vložte text obsahující telefonní čísla (např. "+420 123 456 789").
    2. Do pole "Your regular expression" napište vzor chytající číslice: `\+?\d{3}\s?\d{3}\s?\d{3}\s?\d{3}`.
    3. Pomocí nástroje otestujte, že vzor úspěšně zachytí požadovaná data.

**3. Čištění textu (hledání bílých znaků)**
*   **Nástroj:** [RegExr](https://regexr.com/)
*   **Postup:**
    1. Vložte velmi neuspořádaný text s mnoha přebytečnými tabulátory a mezerami.
    2. Použijte metaznak pro bílé znaky `\s` v kombinaci s kvantifikátorem `+` (tedy `\s+` pro jeden a více bílých znaků).
    3. Přepněte do záložky "Replace" a nechte je nahradit jedinou mezerou. Sledujte "čištění dat" v reálném čase.

**4. Ukotvení na začátek a konec řetězce**
*   **Nástroj:** [Regex101](https://regex101.com/)
*   **Postup:**
    1. Vložte do testu řádky, některé začínající slovem "Chyba:" a jiné končící "Chyba:".
    2. Použijte výraz `^Chyba:`.
    3. Všimněte si, že se označí pouze slova na samém začátku řádku. Zkuste to samé s koncem řádku pomocí znaku dolaru: `Chyba:$`.

**5. Luštění regex hádanek**
*   **Nástroj:** [Regex Crossword](https://regexcrossword.com/)
*   **Postup:**
    1. Otevřete tutoriál.
    2. Hra vám předloží tabulku, kde řádky a sloupce mají jako nápovědu regulární výrazy.
    3. Musíte doplnit přesné literály (znaky), které projdou validací všech dotčených výrazů, čímž si skvěle procvičíte čtení struktury regexu.

**6. Pokročilé vyhledávání v lokálním souboru**
*   **Nástroj:** Notepad++ (součást Windows/ke stažení)
*   **Postup:**
    1. Otevřete libovolný větší textový soubor v Notepad++.
    2. Zmáčkněte `Ctrl+F` a v dialogu zaškrtněte "Regulární výrazy" v sekci Režim vyhledávání.
    3. Zkuste vyhledat všechny řádky končící tečkou zadáním `\.$` a klikněte na "Najít vše".

---

## 4. Datové soubory a jejich význam v programování
Tato sekce vysvětluje rozdíl mezi textovými a binárními soubory a cyklus práce s nimi (otevření, čtení/zápis, zavření).

**1. Analýza textového vs. binárního souboru**
*   **Nástroj:** Poznámkový blok (Notepad - Windows)
*   **Postup:**
    1. Vytvořte jednoduchý textový dokument (`.txt`) a něco do něj napište. Otevřete ho v Poznámkovém bloku - uvidíte čitelný text.
    2. Vezměte libovolný obrázek (`.jpg` nebo `.png`) a přetáhněte ho do Poznámkového bloku.
    3. Uvidíte "rozsypaný čaj" – to je ukázka binárních dat interpretovaných chybně jako text.

**2. Pohled do skutečné struktury binárního souboru**
*   **Nástroj:** [HexEd.it](https://hexed.it/)
*   **Postup:**
    1. Otevřete online editor a nahrajte do něj libovolný binární soubor (např. spouštěcí `.exe` nebo obrázek `.png`).
    2. Prohlédněte si hexadecimální reprezentaci bytů.
    3. Na začátku souboru (tzv. hlavička) často najdete textový identifikátor formátu (např. "PNG").

**3. Použití kontextového manažeru `with` v Pythonu**
*   **Nástroj:** [Google Colab](https://colab.research.google.com/)
*   **Postup:**
    1. Vytvořte nový zápisník (Notebook).
    2. Do buňky s kódem vložte vytvoření souboru pomocí kontextového manažeru: `with open("test.txt", "w") as f:` a na odsazený řádek `f.write("Ahoj")`.
    3. V levém panelu "Soubory" (ikonka složky) ověřte, že se soubor bezpečně vytvořil a uložil bez nutnosti volat `f.close()`.

**4. Rozdíl mezi režimem zápisu (`w`) a připojení (`a`)**
*   **Nástroj:** [Repl.it (Python)](https://replit.com/)
*   **Postup:**
    1. Ve vašem kódu použijte režim `"w"` pro zápis do souboru `data.txt` a napište do něj slovo "První".
    2. Kód spusťte znovu, ale zapište slovo "Druhý" stále s režimem `"w"`. Přečtěte obsah - uvidíte jen "Druhý" (soubor se přepsal).
    3. Změňte režim na `"a"` (append/připojení), zapište "Třetí" a zkontrolujte, že v souboru nyní zůstala i předchozí data.

**5. Únik paměti (Memory leak) v jazyce C**
*   **Nástroj:** [OnlineGDB (C Compiler)](https://www.onlinegdb.com/online_c_compiler)
*   **Postup:**
    1. Pomocí `FILE *soubor = fopen("test.txt", "w");` otevřete soubor.
    2. Zapište text příkazem `fprintf(soubor, "Zápis");`.
    3. Program ukončete, ale záměrně vynechejte příkaz `fclose(soubor);`.
    4. Ačkoliv online kompilátory často procesy uklidí po konci programu, zamyslete se nad riziky poškození dat u dlouho běžících aplikací. Opravte to přidáním zavírací funkce.

**6. Čtení souboru po řádcích**
*   **Nástroj:** [Google Colab](https://colab.research.google.com/)
*   **Postup:**
    1. Vytvořte si ve svém Colabu přes levé menu vícerádkový textový soubor.
    2. Otevřete jej v Pythonu pomocí `with open()`.
    3. Použijte cyklus `for radek in soubor:` a vytiskněte každý řádek (vyhnete se tím načtení celého velkého souboru do paměti naráz).

---

## 5. Nejpoužívanější typy datových formátů
Tato kapitola představuje XML, JSON, YAML a CSV jako způsoby strukturování dat.

**1. Analýza tabulkových dat**
*   **Nástroj:** MS Excel nebo Poznámkový blok
*   **Postup:**
    1. Otevřete Poznámkový blok a vytvořte prostý text: `Jmeno,Vek,Mesto\nJan,25,Praha\nEva,30,Brno`.
    2. Uložte jako `data.csv`.
    3. Dvakrát klikněte na soubor. Pravděpodobně se otevře v Excelu nebo jiném tabulkovém editoru a automaticky se rozdělí do buněk na základě oddělovače (čárky).

**2. Formátování a validace hierarchického XML**
*   **Nástroj:** [CodeBeautify XML Viewer](https://codebeautify.org/xmlviewer)
*   **Postup:**
    1. Do levého okna napište jednoduché XML: `<uzivatele><uzivatel><jmeno>Jan</jmeno></uzivatel></uzivatele>`.
    2. Smažte jednu z uzavíracích značek (např. `</jmeno>`).
    3. Sledujte chybovou hlášku. XML klade obrovský důraz na správné ukončení stromových elementů (validaci).

**3. Tvorba kompaktního API záznamu v JSONu**
*   **Nástroj:** [JSONLint](https://jsonlint.com/)
*   **Postup:**
    1. Pokuste se vytvořit JSON s atributy "jmeno", "vek" a "aktivni" (boolean).
    2. Kód: `{ "jmeno": "Jan", "vek": 25, "aktivni": true }`.
    3. Klikněte na "Validate JSON". Tento formát je striktní ohledně syntaxe (např. klíče musí být v dvojitých uvozovkách).

**4. Vizualizace komplexního JSON objektu**
*   **Nástroj:** [JSON Crack](https://jsoncrack.com/editor)
*   **Postup:**
    1. Zkopírujte předgenerovaný složitý JSON z editoru.
    2. Nástroj ho obratem převede na vizuální interaktivní myšlenkovou mapu, což dokonale demonstruje jeho hierarchickou a uzlovou strukturu typickou pro webová API.

**5. Odsazování v konfiguraci YAML**
*   **Nástroj:** [YAML Lint](https://www.yamllint.com/)
*   **Postup:**
    1. Vytvořte YAML objekt (např. pro CI/CD): `server:\n  port: 8080\n  ip: 127.0.0.1`.
    2. Odstraňte u druhého řádku (`port`) odsazení (mezery) a zkuste validovat.
    3. Lintovací nástroj ohlásí chybu – v YAMLu nahrazuje odsazení složené závorky a určuje strukturu.

**6. Konverze formátů mezi sebou**
*   **Nástroj:** [ConvertCSV](https://www.convertcsv.com/csv-to-json.htm)
*   **Postup:**
    1. Do nástroje vložte CSV data (např. `Jméno,Věk\nPetr,22`).
    2. Nechte nástroj převést tento plošný CSV soubor na formát JSON.
    3. Pozorujte, že každý řádek CSV se stal samostatným JSON objektem uvnitř JSON pole (array), což krásně demonstruje sémantické rozdíly v zápisu.

---

## 6. Další datové struktury
Poslední část radí, jak vybírat datovou strukturu (seznam, fronta, zásobník, množina, slovník, strom, graf) podle požadovaných operací.

**1. Simulace chování zásobníku (LIFO)**
*   **Nástroj:** [Python Tutor](https://pythontutor.com/)
*   **Postup:**
    1. Vložte do editoru kód představující funkci "Zpět": `zasobnik = []`, poté `zasobnik.append("krok 1")` a `zasobnik.append("krok 2")`.
    2. Zavolejte `zasobnik.pop()`.
    3. Krokujte program. Na vizualizaci paměti jasně uvidíte princip **LIFO** (Last In, First Out) – odebere se prvek "krok 2", který tam přibyl jako poslední.

**2. Vizualizace fronty (FIFO)**
*   **Nástroj:** [VisuAlgo (Queue)](https://visualgo.net/en/list)
*   **Postup:**
    1. Otevřete simulaci fronty (Queue).
    2. Pomocí tlačítka "Enqueue" přidejte prvky 10, 20 a 30.
    3. Pomocí tlačítka "Dequeue" prvky odebírejte. Animace jasně prokáže princip **FIFO** (First In, First Out) – první odchází prvek 10.

**3. Testování unikátnosti s Množinou (Set)**
*   **Nástroj:** [Programiz Python Online](https://www.programiz.com/python-programming/online-compiler/)
*   **Postup:**
    1. Vytvořte klasický seznam s duplicitami: `id_uzivatelu =`.
    2. Převeďte seznam na množinu: `unikatni_id = set(id_uzivatelu)`.
    3. Výsledek vypište (`print`). Zobrazí se struktura obsahující pouze `{1, 2, 3, 4}` – perfektní volba struktury pro odstranění duplicit.

**4. Rychlé vyhledávání ve Slovníku (Dictionary)**
*   **Nástroj:** [Repl.it (Python)](https://replit.com/)
*   **Postup:**
    1. Vytvořte slovník simulující databázi: `studenti = {"Jan": 85, "Eva": 92}`.
    2. Chtějte najít skóre Evy: `print(studenti["Eva"])`.
    3. Uvědomte si, že díky *hashování* skrytém na pozadí programu Python nemusel porovnávat "Evu" s "Janem", ale přesně rovnou sáhl na správnou paměťovou adresu (klíč → hodnota).

**5. Modelování stromové struktury (Hierarchie)**
*   **Nástroj:** [Draw.io](https://app.diagrams.net/)
*   **Postup:**
    1. Otevřete plátno pro kreslení diagramů.
    2. Nakreslete uzly. Vytvořte kořen (Root) např. se jménem `C:\`.
    3. Přidejte dvě šipky pod kořen mířící do uzlů `Program Files` a `Users`.
    4. Vizualizujete tak datovou strukturu zvanou **Strom**, jejíž podstatou je relace nadřazenosti/podřazenosti.

**6. Grafy jako abstrakce vztahů v reálném světě**
*   **Nástroj:** [CS Academy Graph Editor](https://csacademy.com/app/graph_editor/)
*   **Postup:**
    1. V editoru vlevo napište pod sebe na jednotlivé řádky dvojice měst: `Praha Brno`, `Brno Ostrava`, `Praha Plzen`.
    2. V pravém plátně se okamžitě vygeneruje **Graf**, kde města jsou vrcholy a silnice (vztahy mezi nimi) představují hrany.
    3. Tyto sítě se využívají při programování navigací, protože tu na rozdíl od stromu není žádný jasný "kořen".