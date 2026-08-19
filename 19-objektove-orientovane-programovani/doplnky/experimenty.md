# Experimenty

Tento dokument obsahuje praktické experimenty a úlohy, které slouží jako přímý doplněk k teoretickým konceptům objektově orientovaného programování z poskytnutých zdrojů. Každá úloha využívá volně dostupné nástroje a obsahuje návodný postup.

## 1. Důvody vzniku OOP a jeho principy

Tato sada experimentů vám pomůže pochopit rozdíl mezi procedurálním přístupem a objektovým paradigmatem, kde objekty spojují data a chování.

1. **Vizuální objekty vs. sekvenční kód**
   * **Cíl:** Pochopit, jak objekty (postavy) zapouzdřují vlastní stav a chování.
   * **Nástroj:** [Scratch](https://scratch.mit.edu/)
   * **Postup:** Vytvořte nový projekt. Přidejte dvě různé postavy (např. kočku a psa). Každé postavě nastavte vlastní proměnnou (např. "Energie") a vytvořte pro ně samostatné skripty reagující na kliknutí (snížení energie a vydání zvuku). Pozorujte, že každá postava funguje jako nezávislý **objekt** se svým vlastním stavem a metodami, čímž předejdete zmatenému "spaghetti" kódu.
2. **Kalkulačka procedurálně**
   * **Cíl:** Zjistit limity procedurálního návrhu na reálném kódu.
   * **Nástroj:** [Programiz Python Compiler](https://www.programiz.com/python-programming/online-compiler/)
   * **Postup:** Napište jednoduchý kód používající pouze globální proměnné pro uložení dvou čísel a sérii if/else podmínek pro operace. Zkuste kód upravit tak, aby pracoval se třemi nezávislými výpočty najednou. Zjistíte, že neustálé duplikování proměnných vede ke špatné organizaci.
3. **Objekty přímo v operačním systému**
   * **Cíl:** Vidět, že OOP se používá i v běžné správě počítače.
   * **Nástroj:** Nástroj Windows PowerShell (součást Windows)
   * **Postup:** Otevřete PowerShell a zadejte příkaz `Get-Process`. Zobrazí se seznam běžících procesů. Poté zadejte `Get-Process | Get-Member`. Zobrazíte tím definici třídy procesu (jeho "metody" a "atributy", jako např. název nebo spotřebu paměti). Uvědomíte si tak, že operační systém pracuje s reálnými instancemi tříd.
4. **První logický objekt pomocí slovníku**
   * **Cíl:** Simulovat spojení dat před zavedením skutečných tříd.
   * **Nástroj:** [Replit (Python)](https://replit.com/)
   * **Postup:** Založte Python projekt. Vytvořte slovník `auto = {"znacka": "Skoda", "palivo": 50}`. Napište globální funkci `jed(auto)`, která sníží hodnotu paliva. Toto je přechodný krok, který ukazuje, jak procedurální programování odděluje data a operace nad nimi.
5. **Kreslení stavu systému**
   * **Cíl:** Analyzovat, co by měl systém uchovávat.
   * **Nástroj:** [Miro](https://miro.com/) nebo Papír
   * **Postup:** Zvolte si doménu (např. Počítačová hra) a vypište, jaké entity by v ní měly existovat (hráč, nepřítel, zbraň). U každé entity vypište její atributy (zdraví, poškození) a co dokáže dělat (útočit, bránit se). Připravíte si tak půdu pro tvorbu prvních tříd.
6. **Rozdíl mezi definicí a instancí v praxi**
   * **Cíl:** Fyzicky pochopit, že třída neexistuje jako data, dokud z ní neuděláme objekt.
   * **Nástroj:** [Thonny IDE](https://thonny.org/)
   * **Postup:** Napište do skriptu prázdnou třídu `class Auto: pass`. Spusťte program a podívejte se do průzkumníka proměnných – neuvidíte žádná data. Až když přidáte `moje_auto = Auto()`, objeví se v paměti skutečná instance.

## 2. Třídy a objekty

V této sekci se zaměříme na stavbu třídy, používání konstruktorů a skrývání vnitřního stavu (zapouzdření) v jazycích Python a C++.

1. **UML návrh vaší první třídy**
   * **Cíl:** Vizualizovat strukturu třídy před psaním kódu.
   * **Nástroj:** [Draw.io](https://app.diagrams.net/)
   * **Postup:** V levém menu najděte záložku "UML" a přetáhněte na plochu prvek "Class" (Třída). Pojmenujte ji `BankovniUcet`. Do sekce atributů přidejte `- zustatek: float` (znak mínus značí private) a do sekce metod `+ vloz_penize(castka)` (plus značí public). Tento diagram slouží jako předpis, jak bude váš kód vypadat.
2. **Experiment s Konstruktorem a Destruktorem v C++**
   * **Cíl:** Sledovat životní cyklus objektu.
   * **Nástroj:** [OnlineGDB (C++)](https://www.onlinegdb.com/)
   * **Postup:** Vytvořte třídu `Auto`. Do konstruktoru `Auto()` vložte výpis `cout << "Auto vyrobeno";` a do destruktoru `~Auto()` vložte `cout << "Auto zniceno";`. Vytvořte instanci této třídy uvnitř funkce `main`. Po spuštění uvidíte, že se obě metody volají zcela automaticky.
3. **Sdílení dat přes Třídní atributy**
   * **Cíl:** Otestovat rozdíl mezi atributy instance a třídy.
   * **Nástroj:** [Google Colab (Python)](https://colab.research.google.com/)
   * **Postup:** Vytvořte třídu `Pes` s třídní proměnnou `pocet_psu = 0`. V konstruktoru `__init__` tuto hodnotu vždy zvyšte o 1 (`Pes.pocet_psu += 1`). Následně vytvořte 3 různé instance psa a vypište `Pes.pocet_psu`. Uvidíte, jak se hodnota sdílí napříč všemi objekty.
4. **Porušení zapouzdření a jeho následky**
   * **Cíl:** Zjistit, proč je přímý přístup k atributům nebezpečný.
   * **Nástroj:** [Python Tutor](https://pythontutor.com/)
   * **Postup:** Napište Python kód s třídou `Ucet`, která má atribut `zustatek`. Vytvořte instanci a manuálně nastavte `ucet.zustatek = -5000`. Vizualizujte krok po kroku. Následně se pokuste opravit návrh tak, abyste použili metodu pro vklad, která zamezí zadání záporné hodnoty.
5. **Strikní public/private kontrola v C++**
   * **Cíl:** Zkusit obejít kompilátor při zapouzdření.
   * **Nástroj:** [C++ Shell](http://cpp.sh/)
   * **Postup:** Deklarujte v C++ třídu s klíčovým slovem `private:` a pod něj umístěte proměnnou `tajne_heslo`. Z funkce `main` se pokuste napsat `objekt.tajne_heslo = 123;`. Zkuste kód zkompilovat. Kompilátor vás nepustí a nahlásí chybu viditelnosti, což demonstruje pilíř bezpečnosti OOP.
6. **Moderní Gettery a Settery v Pythonu**
   * **Cíl:** Implementovat bezpečný přístup přes dekorátor.
   * **Nástroj:** [Replit (Python)](https://replit.com/)
   * **Postup:** Napište třídu `Teplomer`. Využijte privátní atribut `_teplota`. Vytvořte metodu `teplota` označenou dekorátorem `@property` a další metodu `@teplota.setter`. V setteru implementujte podmínku, že teplota nesmí klesnout pod absolutní nulu (-273.15 °C). Otestujte zadáním neplatné hodnoty.

## 3. Dědičnost a polymorfismus

Cílem této kapitoly je vyzkoušet si opakované použití kódu (rodič a potomek) a přepisování či přetěžování chování (polymorfismus).

1. **Rodokmen dědičnosti**
   * **Cíl:** Logicky uspořádat specializaci objektů.
   * **Nástroj:** [Creately](https://creately.com/) nebo podobný diagramový nástroj.
   * **Postup:** Navrhněte diagram se základní třídou `Zvíře`. Od ní vyveďte šipky k `Pták` a `Ssavec`. Od nich dále k `Orel` a `Pes`. Ke každému boxu připište jednu metodu, kterou zdědí všechny podřízené třídy. Vizualizujete si vztah "je".
2. **Překrytí (Override) metody krok za krokem**
   * **Cíl:** Sledovat, jak program vybírá správnou metodu.
   * **Nástroj:** [Python Tutor](https://pythontutor.com/)
   * **Postup:** Definujte základní třídu `Zvire` s metodou `zvuk()`, která vrátí "Nějaký zvuk". Z ní odvoďte `Pes(Zvire)` a metodu `zvuk()` přepište, aby vracela "Haf". Vytvořte obě instance, pusťte vizualizaci a sledujte, jak u instance `Pes` program ignoruje rodičovskou metodu a spouští tu přepsanou.
3. **Pole polymorfních objektů**
   * **Cíl:** Zpracovat různé objekty jednotným příkazem.
   * **Nástroj:** [Google Colab (Python)](https://colab.research.google.com/)
   * **Postup:** Vytvořte třídy `Pes`, `Kocka` a `Auto`. Každé dejte metodu `vydej_zvuk()`. Následně vytvořte seznam (pole) `entit = [Pes(), Kocka(), Auto()]` a projděte je cyklem `for objekt in entit: objekt.vydej_zvuk()`. Toto demonstruje polymorfismus v praxi (různé chování na stejný příkaz).
4. **Přetěžování (Overloading) metod v C++**
   * **Cíl:** Otestovat definici více metod se stejným jménem.
   * **Nástroj:** [OnlineGDB (C++)](https://www.onlinegdb.com/)
   * **Postup:** Vytvořte třídu `Kalkulacka` a do ní vložte dvě metody pojmenované stejně: `void tiskni(int cislo)` a `void tiskni(double cislo)`. V `main` vyzkoušejte zavolat funkci celým číslem a poté desetinným. Kompilátor dynamicky vybere správnou metodu.
5. **Simulace přetěžování v Pythonu**
   * **Cíl:** Zvládnout absenci formálního přetěžování v Pythonu pomocí výchozích argumentů.
   * **Nástroj:** [Replit (Python)](https://replit.com/)
   * **Postup:** Napište třídu `Ucet` s metodou `uloz_penize(self, castka, mena="CZK")`. Zavolejte metodu nejprve pouze s částkou a poté s částkou i měnou. Využijete tak různé možnosti volání jediné metody.
6. **Vícenásobná dědičnost a její úskalí**
   * **Cíl:** Zjistit, jak se chová třída se dvěma rodiči.
   * **Nástroj:** [Thonny IDE](https://thonny.org/)
   * **Postup:** V Pythonu vytvořte třídu `Auto` a třídu `Lod`. Obě ať mají metodu `pohyb()`. Vytvořte odvozenou třídu `Obojzivelnik(Auto, Lod)`, zavolejte metodu `pohyb()` a pomocí zjištění Method Resolution Order (vypište `Obojzivelnik.mro()`) prozkoumejte, jak Python vyřešil konflikt stejného jména metody.

## 4. Vytváření objektů, možnosti práce s objekty a s pamětí

Správa paměti ukazuje propastný rozdíl mezi hodnotovým/manuálním přístupem v C++ a referenčním/automatickým Garbage Collectorem v Pythonu.

1. **Zásobník (Stack) vs. Halda (Heap) naživo**
   * **Cíl:** Zjistit, jak se kód překládá pro procesor.
   * **Nástroj:** [Compiler Explorer (Godbolt)](https://godbolt.org/)
   * **Postup:** Vložte jednoduchý C++ kód, kde vytvoříte běžný objekt `Auto a;` a vedle objekt dynamicky: `Auto* b = new Auto();`. V assemblerové části obrazovky hledejte instrukci volání paměti pro `new` (halda). Jasně uvidíte složitost dynamické alokace.
2. **Adresy referencí a pointerů**
   * **Cíl:** Odhalit skryté předávání odkazů.
   * **Nástroj:** [OnlineGDB (C++)](https://www.onlinegdb.com/)
   * **Postup:** V C++ vytvořte proměnnou a použijte operátor adresy (`&`) k jejímu výpisu do konzole. Následně vytvořte ukazatel a předejte hodnotu by-reference (odkazem). Sledujte, že obě proměnné ukazují na stejný blok v paměti.
3. **Hodnota vs. Reference v Pythonu**
   * **Cíl:** Pozorovat, že Python vždy používá reference pro objekty.
   * **Nástroj:** [Python Tutor](https://pythontutor.com/)
   * **Postup:** Napište funkci, která jako parametr vezme instanci objektu a změní jeho atribut. Před vytvořením funkce vytvořte objekt, pošlete ho do funkce a po jejím skončení hodnotu vypište. Uvidíte, že se původní objekt změnil (nekopíroval se).
4. **Experiment s Memory Leak (Únikem paměti)**
   * **Cíl:** Vytvořit záměrný problém s nesprávou paměti v C++.
   * **Nástroj:** [C++ Shell](http://cpp.sh/)
   * **Postup:** Napište nekonečný cyklus nebo cyklus o 10 000 krocích, ve kterém dojde k vytvoření objektu přes operátor `new` (např. pole integerů). **Záměrně opomeňte zavolat `delete`**.  Dojde k simulaci zaplňování paměti na haldě (Heap).
5. **Pozorování Garbage Collectoru**
   * **Cíl:** Zjistit, kdy Python maže objekty z paměti.
   * **Nástroj:** [Replit (Python)](https://replit.com/)
   * **Postup:** Importujte modul `gc` (Garbage Collector). Vytvořte třídu `Test` s destruktorem `__del__`, který vytiskne zprávu o smazání. Následně instanci přiřaďte do proměnné a hned na to přepište tuto proměnnou hodnotou `None`. Uvidíte, jak Garbage Collector okamžitě a automaticky objekt smaže.
6. **Inteligentní ukazatele (Smart Pointers) v moderním C++**
   * **Cíl:** Zabezpečit únik paměti v C++ automaticky.
   * **Nástroj:** [OnlineGDB (C++)](https://www.onlinegdb.com/)
   * **Postup:** Naimportujte hlavičku `<memory>`. Místo klasického klíčového slova `new` vytvořte objekt obalený ve standardním chytrém ukazateli: `std::unique_ptr<Auto> a = std::make_unique<Auto>();`. Otestujte, že po ukončení rozsahu platnosti (bloku `{ }`) se destruktor zavolá sám od sebe bez explicitního `delete`.

## 5. Další aplikace principů OOP: abstraktní třídy, rozhraní

Tyto experimenty vám ukážou, jak využívat třídy čistě jako šablony a smlouvy definující povinné metody pro ostatní třídy (polymorfismus na vyšší úrovni).

1. **Čistě virtuální metoda v C++**
   * **Cíl:** Zabránit instanciaci abstraktní třídy v C++.
   * **Nástroj:** [OnlineGDB (C++)](https://www.onlinegdb.com/)
   * **Postup:** Vytvořte třídu `Vozidlo` a definujte metodu s přiřazením k nule: `virtual void jed() = 0;`. V bloku `main` se pokuste napsat `Vozidlo v;`. Kompilátor to zakáže s odůvodněním, že třída je plně abstraktní a musíte vytvořit konkrétního potomka, který metodu zrealizuje.
2. **Modul ABC v Pythonu**
   * **Cíl:** Vynutit si implementaci metody u potomků v Pythonu.
   * **Nástroj:** [Google Colab (Python)](https://colab.research.google.com/)
   * **Postup:** Naimportujte moduly z `abc` (Abstract Base Classes). Vytvořte rodičovskou třídu `Zviratko(ABC)` a nad její metodu `zvuk()` přidejte dekorátor `@abstractmethod`. Vytvořte třídu `Kocka`, která od ní dědí, ale **nenaprogramujte** do ní metodu `zvuk`. Při pokusu vytvořit objekt kočky narazíte na cílenou chybovou hlášku.
3. **Simulace rozhraní (Interface) v Pythonu**
   * **Cíl:** Implementovat společnou "smlouvu" pro nesouvisející objekty.
   * **Nástroj:** [Thonny IDE](https://thonny.org/)
   * **Postup:** Vytvořte prázdnou abstraktní třídu `Pohyblivy` s metodou `pohni_se()`. Vytvořte dvě naprosto rozdílné třídy `Auto` a `Robot`, obě ať dědí od `Pohyblivy` a implementují `pohni_se()`. Tento experiment učí, že rozhraní definuje **CO** objekt dělá, ne **JAK** to dělá.
4. **Generátor API jako abstrakce rozhraní**
   * **Cíl:** Vizualizovat si, jak vypadá návrh rozhraní (Interface) ve velkých systémech.
   * **Nástroj:** [Swagger Editor](https://editor.swagger.io/)
   * **Postup:** Otevřete editor a podívejte se na ukázkový YAML konfigurační soubor. Najděte definice požadavků (GET, POST). Berte tento soubor jako reálné API rozhraní — definuje jména metod a co musí vrátit, aniž by ukazovalo, jak je vnitřní kód napsaný.
5. **Návrh rozhraní v UML**
   * **Cíl:** Správně vizualizovat závislosti na rozhraní.
   * **Nástroj:** [Draw.io](https://app.diagrams.net/)
   * **Postup:** Přidejte komponentu Třídy, upravte její nadpis doplněním stereotypu `<<interface>>` (např. `<<Pohyblivy>>`). Pomocí přerušované šipky zakončené prázdným trojúhelníkem (realization) ji spojte s běžnými třídami jako `Auto` a `Pes`. Vizuálně tak zafixujete rozdíl mezi běžnou dědičností a implementací kontraktu.
6. **Rozdíl mezi abstraktní třídou a rozhraním v C++**
   * **Cíl:** Vytvořit obě struktury pro srovnání.
   * **Nástroj:** [C++ Shell](http://cpp.sh/)
   * **Postup:** Vytvořte abstraktní třídu obsahující jak běžnou předpřipravenou metodu `zapni_motor()`, tak čistě virtuální metodu `pohni_se() = 0;`. Následně pod to vytvořte čisté rozhraní (Interface), které nesmí obsahovat nic jiného než pouze abstraktní metody. Na tomto kontrastu pochopíte rozdíl.

## 6. Návrh objektového programu

Poslední část prozkoumává systémovou architekturu: správné rozdělení odpovědností, skládání objektů a použití návrhových vzorů.

1. **Dědičnost ("Je") vs. Kompozice ("Má") na papíře**
   * **Cíl:** Rozhodnout se pro správný vztah mezi objekty.
   * **Nástroj:** Papír nebo textový dokument.
   * **Postup:** Vypište si pět dvojic objektů (např. Počítač/Procesor, Tlačítko/Text, Zvíře/Pes, Pták/Křídlo). U každé dvojice napište, zda dává smysl věta "A JE B" (dědičnost) nebo "A MÁ B" (kompozice). Pokud Počítač není Procesor, nesmíte použít dědičnost.
2. **Kódování kompozice v Pythonu**
   * **Cíl:** Sestavit velký objekt z menších nezávislých částí.
   * **Nástroj:** [Replit (Python)](https://replit.com/)
   * **Postup:** Napište nezávislou třídu `Motor` (s metodou start) a třídu `Kolo`. Následně vytvořte třídu `Auto`. V konstruktoru Auta nebudete dědit, ale vytvoříte si proměnnou `self.motor = Motor()`. V metodě `nastartuj_auto()` pak zavoláte `self.motor.start()`. Tím jste úspěšně realizovali návrh pomocí kompozice.
3. **Princip jedné odpovědnosti (Single Responsibility)**
   * **Cíl:** Rozbít "Božskou třídu" (God class).
   * **Nástroj:** Jakýkoliv textový editor.
   * **Postup:** Zkopírujte si ze studijního materiálu třídu `Student` z bloku, která ukládá do databáze, tiskne vysvědčení a odesílá maily. Podle návrhu z bloku ji rozdělte do čtyř menších, nezávislých tříd (`Student`, `DatabazeStudentu`, `TvorbaVysvedceni`, `OdesilaniZprav`).
4. **Návrhový vzor Observer (Pozorovatel)**
   * **Cíl:** Vyzkoušet si dynamickou reakci jednoho objektu na změnu druhého.
   * **Nástroj:** [Python Tutor](https://pythontutor.com/)
   * **Postup:** Napište jednoduchou třídu `MeteorologickaStanice`, která má list pozorovatelů (např. display telefonů). Přidejte metodu `pridej_pozorovatele()` a `zmena_teploty()`. Při spuštění `zmena_teploty()` projděte cyklem for všechny pozorovatele v listu a zavolejte na nich `.aktualizuj()`.
5. **Návrhový vzor Factory (Továrna)**
   * **Cíl:** Oddělit proces tvorby objektu od jeho logiky.
   * **Nástroj:** [OnlineGDB (Python/C++)](https://www.onlinegdb.com/)
   * **Postup:** Navrhněte třídu `VozidloFactory`, která má jedinou metodu `vytvor_vozidlo(typ)`. V této metodě udělejte podmínku: pokud je typ "auto", vraťte novou instanci `Auto()`, pokud "kolo", vraťte instanci `Kolo()`. Skryjete tak logiku vytváření za jedinou metodu.
6. **Rozdělení programu pomocí MVC architektonického vzoru**
   * **Cíl:** Zažít striktní oddělení dat, logiky a zobrazení.
   * **Nástroj:** [Google Colab (Python)](https://colab.research.google.com/)
   * **Postup:** Vytvořte tři třídy:
     1. `KnihaModel` - uchovává pouze seznam dostupných knih.
     2. `KnihovnaView` - má metodu `zobraz_knihy(seznam)`, která udělá pouze print() dat do konzole.
     3. `KnihovnaController` - propojuje je. Zeptá se Modelu na knihy a pak pošle data do View pro zobrazení. Tímto si naprogramujete základy robustní systémové architektury velkých aplikací.