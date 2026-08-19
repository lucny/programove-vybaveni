# Experimenty

## 1. Důvody vzniku strukturovaného programování, zásady a základní rysy
**1.1 Sekvenční tok programu (Scratch)**
*   **Nástroj:** [Scratch](https://scratch.mit.edu)
*   **Cíl:** Ověření sekvence, kde jsou příkazy vykonávány postupně jeden za druhým.
*   **Postup:** Otevřete editor. Přetáhněte pod blok "Po kliknutí na vlaječku" tři bloky z kategorie Vzhled: "Řekni Ahoj", "Změň kostým", "Řekni Konec".
*   **Pozorování:** Postava vykoná příkazy striktně shora dolů. Program se nevrací ani nepřeskakuje.

**1.2 Důsledky příkazu GOTO (Windows CMD/Notepad)**
*   **Nástroj:** Poznámkový blok (Notepad) ve Windows.
*   **Cíl:** Simulace nepřehledného nestrukturovaného kódu s bezpodmínečnými skoky.
*   **Postup:** Vytvořte soubor `test.bat`. Napište do něj:
    `:start`
    `echo Zacykleno!`
    `goto start`
    Soubor uložte a spusťte.
*   **Pozorování:** Program vytvoří nekonečnou smyčku. Změna nebo oprava takového toku je obtížná, což historicky vedlo k zákazu příkazu GOTO.

**1.3 Rozklad složitého problému (Blockly Games)**
*   **Nástroj:** [Blockly Games - Bludiště](https://blockly.games/maze)
*   **Cíl:** Nácvik rozkladu problému na menší zvládnutelné části.
*   **Postup:** Otevřete úroveň 10. Místo psaní jednoho dlouhého kódu vizuálně rozložte cestu panáčka na dílčí podprogramy pomocí bloků.
*   **Pozorování:** Modulární přístup dělá program čitelnějším.

**1.4 Omezení platnosti proměnných v prohlížeči**
*   **Nástroj:** Webový prohlížeč (klávesa F12 -> Console).
*   **Cíl:** Test lokálních proměnných s omezenou platností.
*   **Postup:** Napište do konzole: `{ let x = 5; }` a stiskněte Enter. Poté napište `console.log(x);`.
*   **Pozorování:** Prohlížeč vyhodí chybu, protože proměnná `x` existovala pouze uvnitř bloku (omezená platnost).

**1.5 Systematické pojmenování proměnných (Replit Python)**
*   **Nástroj:** [Replit (Python)](https://replit.com)
*   **Cíl:** Ukázka vlivu pojmenování na čitelnost kódu.
*   **Postup:** Napište kód: `a = 10; b = 20; c = a * b`. Pak ho přepište na: `cena = 10; pocet = 20; celkem = cena * pocet`.
*   **Pozorování:** Funkčnost je stejná, ale druhý kód je pro autora snáze pochopitelný a udržovatelný i po čase.

**1.6 Logická struktura kódu bez skoků (Code.org)**
*   **Nástroj:** [Code.org - Hodina kódu](https://code.org/hourofcode/overview)
*   **Cíl:** Aplikace základních rysů strukturovaného programování formou hry.
*   **Postup:** Vyberte si libovolnou aktivitu a vyřešte bludiště pouze pomocí sekvencí a cyklů.
*   **Pozorování:** Nástroj vůbec neumožňuje skoky typu GOTO, vynucuje strukturované konstrukce, což snižuje riziko chyb.


## 2. Konstanty, proměnné, datové typy
**2.1 Sledování paměti proměnných (Python Tutor)**
*   **Nástroj:** [Python Tutor](https://pythontutor.com)
*   **Cíl:** Vizualizace proměnné jako pojmenovaného místa v paměti.
*   **Postup:** Vložte kód `x = 5`, na další řádek `x = 10`. Klikejte na "Next".
*   **Pozorování:** Nástroj graficky ukazuje, jak se hodnota ve stejném místě v paměti mění za běhu programu.

**2.2 Statické typování v jazyce C (OnlineGDB)**
*   **Nástroj:** [OnlineGDB - C Compiler](https://www.onlinegdb.com/online_c_compiler)
*   **Cíl:** Demonstrace chybové kontroly u statického typování.
*   **Postup:** Napište kód: `int cislo = "Text";` a klikněte na Run.
*   **Pozorování:** Kompilátor vyhodí chybu. U statického typování musí být typ explicitně deklarován a nelze do celého čísla (`int`) vložit text.

**2.3 Dynamické typování v Pythonu (Programiz)**
*   **Nástroj:** [Programiz - Python Compiler](https://www.programiz.com/python-programming/online-compiler/)
*   **Cíl:** Ověření změny typu za běhu.
*   **Postup:** Napište:
    `promenna = 42`
    `print(type(promenna))`
    `promenna = "Hello"`
    `print(type(promenna))`
*   **Pozorování:** Výpis ukáže nejprve `<class 'int'>` a poté `<class 'str'>`. Python typ odvozuje a dynamicky mění.

**2.4 Simulace konstanty (Replit Python vs C)**
*   **Nástroj:** [Replit](https://replit.com)
*   **Cíl:** Rozdíl mezi pevnou konstantou a konvencí.
*   **Postup:** V Pythonu napište `PI = 3.14` a na další řádek `PI = 4`. Vytiskněte hodnotu.
*   **Pozorování:** Python hodnotu změní. Velká písmena jsou jen konvence. Skutečnou neměnnost konstanty pomocí klíčového slova `const` zajišťuje jazyk C.

**2.5 Typ logické hodnoty (Prohlížečová konzole JS)**
*   **Nástroj:** Webový prohlížeč (F12).
*   **Cíl:** Práce s datovým typem boolean.
*   **Postup:** Zadejte příkaz `let jePlnolety = true; console.log(typeof jePlnolety);`
*   **Pozorování:** Konzole potvrdí datový typ logické hodnoty (`boolean`), který nabývá pouze stavů true/false.

**2.6 Rozsah možných hodnot (Windows Kalkulačka)**
*   **Nástroj:** Kalkulačka Windows (režim Programátor).
*   **Cíl:** Pochopení velikosti paměti pro typy dat.
*   **Postup:** Přepněte na typ "BYTE" (8 bitů) a zkuste zadat číslo 300.
*   **Pozorování:** Kalkulačka to nedovolí, protože rozsah hodnoty pro tento typ je vyčerpán.


## 3. Řídicí struktury
**3.1 Sledování toku podmínky (VisuAlgo)**
*   **Nástroj:** [VisuAlgo](https://visualgo.net) (sekce Control Flow).
*   **Cíl:** Vizuální reprezentace větvení (selekce).
*   **Postup:** Spusťte krokování u libovolného algoritmu obsahujícího příkaz `if`.
*   **Pozorování:** Program se na základě podmínky rozhodne pro jednu ze dvou cest, čímž prokáže fungování selekce.

**3.2 Řetězení podmínek elif (Programiz)**
*   **Nástroj:** [Programiz - Python](https://www.programiz.com/python-programming/online-compiler/)
*   **Cíl:** Testování vícenásobných podmínek.
*   **Postup:** Napište program s proměnnou `vek`. Použijte strukturu `if vek < 18:`, `elif vek < 65:` a `else:`. Měňte hodnotu `vek`.
*   **Pozorování:** Program testuje více podmínek postupně, dokud nenajde platnou větev.

**3.3 Zkrácený zápis větvení (Replit Python)**
*   **Nástroj:** [Replit](https://replit.com)
*   **Cíl:** Aplikace ternárního operátoru.
*   **Postup:** Napište `vysledek = "Plnoletý" if vek >= 18 else "Nezletilý"`.
*   **Pozorování:** Jde o funkční stručné rozhodnutí v rámci jednoho výrazu nahrazující standardní `if-else`.

**3.4 Přepínač Switch (OnlineGDB C)**
*   **Nástroj:** [OnlineGDB - C](https://www.onlinegdb.com)
*   **Cíl:** Výběr z mnoha větví.
*   **Postup:** Definujte proměnnou `int volba = 2;`. Napište příkaz `switch(volba)` s větvemi `case 1:` a `case 2:`. Na konec větve 2 přidejte `break;`.
*   **Pozorování:** Vykoná se pouze větev 2. Příkaz break zamezil nechtěnému průchodu do dalších větví.

**3.5 Cyklus s předem známým počtem iterací (Trinket Python)**
*   **Nástroj:** [Trinket - Python Turtle](https://trinket.io/turtle)
*   **Cíl:** Grafické využití cyklu for a range().
*   **Postup:** Vložte kód pro vykreslení čtverce:
    `import turtle`
    `for i in range(4): turtle.forward(50); turtle.right(90)`
*   **Pozorování:** Blok odsazeného kódu se díky konstruktu `range()` opakuje přesně čtyřikrát.

**3.6 Simulace chybějícího do...while v Pythonu**
*   **Nástroj:** [Programiz - Python](https://www.programiz.com/python-programming/online-compiler/)
*   **Cíl:** Test manuálního řízení cyklu.
*   **Postup:** Vložte kód:
    `while True:`
    `  print("Proběhnu aspoň jednou")`
    `  break`
*   **Pozorování:** Tělo cyklu proběhne vždy alespoň jednou (jak by učinil cyklus do...while), protože podmínka pro ukončení (zde simulovaná breakem) leží až uvnitř těla.


## 4. Podprogramy a jejich význam; funkce, lokální a globální proměnné
**4.1 Testování zániku lokálních proměnných (Python Tutor)**
*   **Nástroj:** [Python Tutor](https://pythontutor.com)
*   **Cíl:** Ověření, že po ukončení funkce lokální proměnné mizí z paměti.
*   **Postup:** Zadejte funkci `def pokus(): x = 10`, na další řádek ji zavolejte `pokus()` a nakonec dejte `print(x)`. Krokujte.
*   **Pozorování:** Nástroj ukáže chybu `NameError`. Proměnná `x` existovala pouze po dobu vykonávání funkce.

**4.2 Předávání argumentů (Google Colab)**
*   **Nástroj:** [Google Colab](https://colab.research.google.com/)
*   **Cíl:** Odlišení parametrů a argumentů.
*   **Postup:** V první buňce nadefinujte `def soucet(a, b): return a + b`. Ve druhé zavolejte `soucet(5, 3)`.
*   **Pozorování:** Zde `a` a `b` v definici tvoří parametry v hlavičce, zatímco čísla `5` a `3` předaná při volání představují konkrétní argumenty.

**4.3 Procedura bez návratové hodnoty (OnlineGDB C)**
*   **Nástroj:** [OnlineGDB - C](https://www.onlinegdb.com)
*   **Cíl:** Testování funkce typu `void`.
*   **Postup:** Napište funkci: `void pozdrav() { printf("Ahoj\n"); }` a zavolejte ji v `main()`.
*   **Pozorování:** Funkce provede akci (tisk textu), ale nevrací výsledek (nemá příkaz `return`), čímž se stává procedurou.

**4.4 Sdílení globální proměnné (Replit Python)**
*   **Nástroj:** [Replit](https://replit.com)
*   **Cíl:** Uchování hodnoty mezi voláními.
*   **Postup:** Mimo funkce definujte `pocitadlo = 0`. Uvnitř funkce napište `global pocitadlo` a `pocitadlo += 1`. Funkci zavolejte třikrát.
*   **Pozorování:** Proměnná se sdílí a uchovává si hodnotu (vypíše 3), protože je deklarována mimo funkci a viditelná v celém programu.

**4.5 Tvorba vlastního bloku (Scratch)**
*   **Nástroj:** [Scratch](https://scratch.mit.edu)
*   **Cíl:** Vizuální princip podprogramů a znovupoužitelnosti.
*   **Postup:** V záložce "Moje bloky" vytvořte blok "Skok". Definujte ho jako pohnutí nahoru a dolů. Pak tento blok třikrát vložte do hlavního skriptu.
*   **Pozorování:** Kód je přehlednější a akci lze opakovaně používat, čímž je demonstrován princip znovupoužitelnosti.

**4.6 Nežádoucí změny globálních proměnných (Online Python)**
*   **Nástroj:** [Programiz - Python](https://www.programiz.com/python-programming/online-compiler/)
*   **Cíl:** Simulace rizik konfliktů.
*   **Postup:** Vytvořte globální proměnnou `heslo = "123"`. V jedné funkci toto heslo omylem přepište příkazem `heslo = "000"`.
*   **Pozorování:** Program ilustruje nežádoucí změnu, kdy jakákoliv funkce může nechtěně modifikovat data. Proto se doporučuje minimalizovat používání globálních proměnných.


## 5. Modularita programů, knihovny a jejich využití, hlavičkové soubory
**5.1 Standardní knihovny C (Godbolt Compiler Explorer)**
*   **Nástroj:** [Godbolt](https://godbolt.org)
*   **Cíl:** Analýza připojování standardních hlavičkových souborů.
*   **Postup:** Napište `printf("Test");` bez direktivy `#include <stdio.h>`.
*   **Pozorování:** Kompilátor vyhodí chybu, protože nezná definici vstupně-výstupní funkce. Hlavičkový soubor slouží jako rozhraní k dodávaným funkcím jazyka.

**5.2 Import externí knihovny v Pythonu (Google Colab)**
*   **Nástroj:** [Google Colab](https://colab.research.google.com)
*   **Cíl:** Modulární připojení pomocí `import`.
*   **Postup:** V buňce zadejte `import math` a na dalším řádku zavolejte matematickou funkci `print(math.sqrt(16))`.
*   **Pozorování:** Místo implementace vlastního výpočtu odmocniny byl využit předpřipravený otestovaný kód ze standardní knihovny.

**5.3 Oddělení modulu (Replit Python)**
*   **Nástroj:** [Replit](https://replit.com)
*   **Cíl:** Ukázka tvorby vlastního modulu `.py`.
*   **Postup:** Vytvořte soubor `matematika.py` a do něj dejte funkci `secist(a, b)`. V souboru `main.py` napište `import matematika` a zavolejte `matematika.secist(2, 2)`.
*   **Pozorování:** Logicky související celky byly rozděleny pro snadnější údržbu.

**5.4 Ochrana proti vícenásobnému zahrnutí (OnlineGDB C)**
*   **Nástroj:** [OnlineGDB - C](https://www.onlinegdb.com) (umožňuje více souborů)
*   **Cíl:** Vytvoření uživatelského hlavičkového souboru s include guardem.
*   **Postup:** Vytvořte `matematika.h`. Napište do něj `#ifndef MATEMATIKA_H`, na další řádek `#define MATEMATIKA_H`, následně deklaraci funkce a zakončete `#endif`.
*   **Pozorování:** Tyto direktivy preprocesoru ochrání projekt, aby do něj hlavičkový soubor s deklaracemi nebyl vložen duplicitně, což by způsobilo kolize.

**5.5 Částečný import funkcí (Programiz Python)**
*   **Nástroj:** [Programiz - Python](https://www.programiz.com)
*   **Cíl:** Připojení pouze konkrétní části modulu.
*   **Postup:** Zadejte `from math import pi` a vypište `print(pi)`. Zkuste zavolat i `sqrt(9)`.
*   **Pozorování:** Hodnota `pi` se vypíše, ale `sqrt` vyvolá chybu, jelikož se do jmenného prostoru importovala explicitně pouze zadaná konstanta, nikoliv celý modul.

**5.6 Matematické funkce z C knihoven (OnlineGDB C)**
*   **Nástroj:** [OnlineGDB - C](https://www.onlinegdb.com)
*   **Cíl:** Využití lomených závorek pro systémové funkce.
*   **Postup:** Na začátek vložte `#include <math.h>` a do `main()` zkuste `double x = sin(1.0);`.
*   **Pozorování:** Kompilátor pochopí lomené závorky tak, že jde o standardní (systémovou) knihovnu poskytující matematické funkce, na rozdíl od uživatelských souborů ve dvojitých uvozovkách.


## 6. Rekurze, výjimky a validace vstupu
**6.1 Vizualizace rekurzivního volání (Recursion Visualizer)**
*   **Nástroj:** [Recursion Visualizer](https://recursion.vercel.app/)
*   **Cíl:** Pochopení stromu rekurze u výpočtu faktoriálu.
*   **Postup:** Vyberte algoritmus "Factorial" a krokujte.
*   **Pozorování:** Funkce předává zjednodušenou verzi problému (např. volá 4! pro vyřešení 5!), dokud nedosáhne jednoduchého případu.

**6.2 Absence ukončovací podmínky (Python Tutor)**
*   **Nástroj:** [Python Tutor](https://pythontutor.com)
*   **Cíl:** Následek chybějící ukončovací podmínky (přetečení zásobníku).
*   **Postup:** Napište funkci `def smycka(): return smycka()`. Zavolejte `smycka()`.
*   **Pozorování:** Nástroj ukáže error (RecursionError). Bez ukončovací podmínky by funkce volala sama sebe donekonečna a program končí chybou.

**6.3 Stromová adresářová struktura jako rekurze (Windows CMD)**
*   **Nástroj:** Příkazový řádek (CMD)
*   **Cíl:** Demonstrovat přirozené použití rekurze pro hierarchii problému.
*   **Postup:** V prázdné složce vytvořte pár podsložek. Otevřete zde CMD a zadejte příkaz `tree`.
*   **Pozorování:** Výpis ukáže průchod, kdy OS pro každou složku opakuje stejný postup hledání podsložek – ukázka problému přirozeně řešitelného rekurzí.

**6.4 Zachycení nečekaného vstupu pomocí výjimky (Replit Python)**
*   **Nástroj:** [Replit](https://replit.com)
*   **Cíl:** Ošetření situace ValueError, kdy operaci nelze dokončit.
*   **Postup:** Zkuste kód z učiva: `int("abc")`. Pak ho obalte do struktury `try: / except ValueError: print("Nelze převést.")`.
*   **Pozorování:** Místo pádu s červeným chybovým hlášením zachytí blok `except` výjimku a program pokračuje dále definovanou vlastní hláškou.

**6.5 Nekonečný cyklus s validací a výjimkou (Programiz Python)**
*   **Nástroj:** [Programiz - Python](https://www.programiz.com)
*   **Cíl:** Spojení cyklu a validace pro opakované zadávání hodnoty.
*   **Postup:** Opište celý kód ze zdrojového textu: `while True: try: ... if 0 <= cislo <= 130: break`. Pokud nástroj online vstupy neumí, nasimulujte to fixními daty.
*   **Pozorování:** Využívají se zde tři principy najednou: výjimka chytá písmena a validace typu `if` odmítá neplatný věk záporných čísel nebo čísel nesmyslně vysokých.

**6.6 Validace formátu vs významu**
*   **Nástroj:** [Regex101](https://regex101.com)
*   **Cíl:** Zamyšlení nad validací smysluplnosti dat.
*   **Postup:** Cílem validace je zkoumat nejen překlad vstupu, ale i pravidla. Ve webovém nástroji vložte libovolný regulární výraz a testujte vstupní texty, zda sedí se vzorem (např. e-mail).
*   **Pozorování:** I když data úspěšně systémem projdou z hlediska datového typu (jsou čistý text / string), validace navíc kontroluje, že splňují přísná interní pravidla aplikace a dávají smysl (mají zavináč apod.).
