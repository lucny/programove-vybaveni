# Experimenty

## 1. Fáze tvorby programu a vývojářské nástroje

**1. Návrh struktury pomocí diagramu tříd**
*   **Cíl:** Vizuálně navrhnout strukturu a vztahy mezi třídami budoucí aplikace.
*   **Nástroj:** [draw.io](https://app.diagrams.net/) (free online)
*   **Postup:** Otevřete aplikaci draw.io v prohlížeči. V levém menu najděte sekci "UML" a přetáhněte na plochu prvek "Class" (Třída). Vytvořte dvě třídy, například `Uzivatel` a `Objednavka`, definujte v nich základní atributy a spojte je čarou znázorňující jejich vztah. 

**2. Modelování procesu přes diagram aktivit**
*   **Cíl:** Popsat logiku programu a tok dat pomocí diagramu aktivit.
*   **Nástroj:** [draw.io](https://app.diagrams.net/) 
*   **Postup:** V draw.io vytvořte nový výkres. Pomocí startovního bodu, šipek a obdélníků namodelujte proces "Přihlášení uživatele" – od zadání hesla přes podmínku (ověření správnosti) až po úspěšný vstup nebo zobrazení chyby.

**3. Založení projektu a psaní kódu v IDE**
*   **Cíl:** Napsat první řádky kódu v textovém editoru určeném pro programátory.
*   **Nástroj:** [Visual Studio Code (VS Code)](https://code.visualstudio.com/) (open-source)
*   **Postup:** Stáhněte a nainstalujte VS Code. Vytvořte si na ploše složku `MujProjekt` a otevřete ji ve VS Code. Vytvořte soubor `index.py` a napište do něj `print("Hello World")`. Všimněte si, jak se mění barvy textu díky zvýrazňování syntaxe.

**4. Rychlé úpravy v konzolovém editoru**
*   **Cíl:** Vyzkoušet si práci s konzolovým editorem pro rychlé úpravy skriptů.
*   **Nástroj:** [Online Bash Emulator](https://replit.com/languages/bash) (nebo příkazový řádek Linuxu/WSL)
*   **Postup:** V online konzoli napište příkaz `nano skript.sh`. Do otevřeného okna napište `echo "Tohle je konzole"`. Stiskněte `Ctrl+O` pro uložení, potvrďte klávesou Enter a aplikaci ukončete pomocí `Ctrl+X`. 

**5. Testování webového API**
*   **Cíl:** Odeslat testovací požadavek na API a přečíst odpověď.
*   **Nástroj:** [Postman](https://www.postman.com/) (webová verze / app)
*   **Postup:** Přihlaste se do Postmanu. Vytvořte nový HTTP požadavek (metoda GET). Do pole pro URL vložte testovací adresu `https://jsonplaceholder.typicode.com/users` a klikněte na "Send". V dolní části obrazovky analyzujte vrácená data.

**6. Generování srozumitelné dokumentace**
*   **Cíl:** Vytvořit jednoduchý textový dokument pomocí značkovacího jazyka Markdown.
*   **Nástroj:** VS Code nebo [Dillinger.io](https://dillinger.io/) (online Markdown editor)
*   **Postup:** Vytvořte soubor `README.md`. Napište hlavní nadpis pomocí `# Nadpis` a vytvořte seznam funkcí aplikace pomocí hvězdiček `* položka`. V editoru si zapněte náhled (Preview), abyste viděli naformátovaný výsledek.


## 2. IDE, pomůcky pro editaci a refaktorování kódu

**1. Průzkum integrovaného rozhraní (IDE)**
*   **Cíl:** Zjistit, jak IDE kombinuje editor, správce balíčků a debugger.
*   **Nástroj:** VS Code
*   **Postup:** Spusťte VS Code. Prohlédněte si levý postranní panel – najděte ikonu lupy pro vyhledávání, ikonu brouka pro ladění a ikonu čtverečků pro instalaci rozšíření (Extensions). Nainstalujte si rozšíření pro váš oblíbený jazyk (např. Python).

**2. Tvorba a využití snippetů**
*   **Cíl:** Ušetřit čas vložením připravené šablony kódu (snippetu).
*   **Nástroj:** VS Code
*   **Postup:** V nastavení VS Code vyhledejte "User Snippets" a vyberte jazyk (např. Python). Definujte si zkratku (např. `defmain`), která po zadání automaticky vygeneruje strukturu hlavní funkce `if __name__ == "__main__":`. Vyzkoušejte ji v novém souboru.

**3. Statická analýza kódu pomocí Linteru**
*   **Cíl:** Nechat analyzovat kód a upozornit na potenciální chyby.
*   **Nástroj:** [ESLint Demo](https://eslint.org/play/) (online) nebo VS Code s ESLint rozšířením
*   **Postup:** Otevřete online ESLint Playground. Napište do něj záměrně špatně zformátovaný nebo chybový kód v JavaScriptu (např. proměnná, která není nikde použita). Pozorujte, jak linter okamžitě chybu podtrhne a nabídne vysvětlení.

**4. Rychlá navigace v projektu**
*   **Cíl:** Vyzkoušet si rychlé hledání funkcí, proměnných a tříd.
*   **Nástroj:** VS Code
*   **Postup:** Otevřete projekt s několika soubory. Umístěte kurzor na volání nějaké funkce, klikněte pravým tlačítkem a vyberte "Go to Definition" (Přejít na definici). IDE vás automaticky přesměruje do souboru, kde je funkce naprogramována.

**5. Zjednodušení a odstranění duplicit (Refaktorování 1)**
*   **Cíl:** Změnit strukturu kódu pro lepší čitelnost bez úpravy funkčnosti.
*   **Nástroj:** Libovolný textový editor
*   **Postup:** Vytvořte skript, který třikrát pod sebou vypisuje téměř identický text s malou obměnou. Následně kód zjednodušte vytvořením jednoho cyklu (loop), který tyto opakující se struktury odstraní. Spusťte program a ověřte, že výstup zůstal stejný.

**6. Rozdělení do menších funkcí (Refaktorování 2)**
*   **Cíl:** Rozdělit dlouhý kód do menších, logických a znovupoužitelných bloků.
*   **Nástroj:** Libovolný textový editor
*   **Postup:** Napište jednu dlouhou funkci, která načte data, matematicky je upraví a vypíše výsledek. Následně ji refaktorujte tak, že z ní vytvoříte tři oddělené funkce: `nacti_data()`, `uprav_data()` a `vypis_vysledek()`.


## 3. Nástroje pro ladění a testování kódu, vývoj řízený testy

**1. Zastavení běhu programu (Breakpoints)**
*   **Cíl:** Zastavit běh programu v určitém bodě a sledovat hodnoty proměnných.
*   **Nástroj:** VS Code (Debugger)
*   **Postup:** Napište krátký cyklus. Kliknutím vlevo vedle čísla řádku přidejte červenou tečku (breakpoint). Spusťte mód "Run and Debug". Program se zastaví; v levém panelu prozkoumejte aktuální hodnoty proměnných.

**2. Zachytávání výjimek (Try...Except)**
*   **Cíl:** Využít chybová hlášení k identifikaci problému bez pádu aplikace.
*   **Nástroj:** [Online Python Compiler](https://www.programiz.com/python-programming/online-compiler/)
*   **Postup:** Napište kód pro dělení dvou čísel, ale druhým číslem nechte být nulu. Kód obalte do bloku `try...except`. V bloku `except` nechte program vypsat vlastní chybové hlášení (např. "Nelze dělit nulou") místo toho, aby program havaroval.

**3. Implementace jednoduchého logování**
*   **Cíl:** Vypsat informace o průběhu programu do konzole.
*   **Nástroj:** Libovolný textový editor
*   **Postup:** Místo jednoduchého `print()` importujte v Pythonu knihovnu `logging`. Nastavte úroveň logování na INFO a do různých částí kódu přidejte zprávy typu `logging.info("Aplikace spuštěna")`. Spusťte skript a prohlédněte si výpis.

**4. Tvorba Unit testu s asercí**
*   **Cíl:** Otestovat izolovanou část kódu (funkci) ověřením očekávané hodnoty.
*   **Nástroj:** Textový editor (modul `unittest` v Pythonu)
*   **Postup:** Vytvořte funkci `secti(a, b)`. V témže souboru importujte modul `unittest` a napište testovací třídu. Použijte aserci (např. `self.assertEqual(secti(2,3), 5)`) k ověření, zda je výsledek správný. Spusťte soubor jako test.

**5. Záznam funkčního uživatelského testu (UI)**
*   **Cíl:** Simulovat uživatelské interakce na webové stránce.
*   **Nástroj:** [Selenium IDE](https://www.selenium.dev/selenium-ide/) (rozšíření do Chrome/Firefox)
*   **Postup:** Nainstalujte si rozšíření Selenium IDE do prohlížeče. Spusťte nahrávání, přejděte na libovolnou webovou stránku, klikněte na odkaz a do vyhledávání zadejte text. Zastavte nahrávání a přehrajte test znovu – prohlížeč vaše akce automaticky zopakuje.

**6. Pokus o TDD (Test-Driven Development)**
*   **Cíl:** Naprogramovat funkci s využitím metodiky vývoje řízeného testy.
*   **Nástroj:** Libovolné IDE
*   **Postup:** *Nejprve* napište test pro funkci `vrat_sude_cisla(seznam)`. Test zkontrolujte – neprojde (funkce ještě neexistuje). Až poté naprogramujte tělo funkce. Spouštějte test tak dlouho, dokud nesvítí zeleně.


## 4. Správa závislostí, virtuální prostředí, kontejnery

**1. Definice závislostí v requirements.txt**
*   **Cíl:** Shromáždit všechny potřebné knihovny do jednoho souboru.
*   **Nástroj:** Textový editor a Python (`pip`)
*   **Postup:** Vytvořte ve složce projektu soubor `requirements.txt`. Napište do něj název knihovny `requests`. V příkazovém řádku zadejte příkaz `pip install -r requirements.txt`. Ověřte, že se knihovna nainstalovala.

**2. Vytvoření souboru package.json v Node.js**
*   **Cíl:** Inicializovat projektovou strukturu pro správu JavaScriptových závislostí.
*   **Nástroj:** Příkazový řádek a instalovaný Node.js (`npm`)
*   **Postup:** V prázdné složce otevřete terminál a zadejte příkaz `npm init -y`. Otevřete nově vytvořený soubor `package.json` a prohlédněte si, jaké informace o projektu automaticky obsahuje.

**3. Vytvoření virtuálního prostředí**
*   **Cíl:** Izolovat závislosti projektu od zbytku systému.
*   **Nástroj:** Terminál a Python (`venv`)
*   **Postup:** V terminálu zadejte `python -m venv moje_prostredi`. Všimněte si, že se vytvořil nový adresář obsahující oddělený Python interpreter. Prostředí aktivujte (ve Windows např. `moje_prostredi\Scripts\activate`) a zkuste nainstalovat libovolný balíček.

**4. Seznámení se s Docker kontejnerem nanečisto**
*   **Cíl:** Spustit kontejner, který sdílí jádro hostitele, ale je izolovaný.
*   **Nástroj:** [Play with Docker](https://labs.play-with-docker.com/) (online sandbox)
*   **Postup:** Přihlaste se pomocí Docker účtu nebo GitHubu. Vytvořte novou instanci. V konzoli spusťte příkaz `docker run hello-world`. Docker stáhne obraz a spustí izolovaný kontejner, který vám do konzole vypíše uvítací text.

**5. Návrh vlastního souboru Dockerfile**
*   **Cíl:** Zjistit, jak se sestavuje obraz pro spuštění aplikace.
*   **Nástroj:** VS Code
*   **Postup:** Vytvořte čistý soubor s názvem `Dockerfile`. Podle oficiální dokumentace vložte základní instrukce: z jakého operačního systému se vychází (např. `FROM python:3.9`), zkopírujte kód `COPY . /app` a určete spouštěcí příkaz `CMD ["python", "app.py"]`.

**6. Architektura pomocí Docker Compose**
*   **Cíl:** Definovat spuštění vícero kontejnerů v jednom celku.
*   **Nástroj:** VS Code
*   **Postup:** Vytvořte soubor `docker-compose.yml`. Pomocí syntaxe YAML definujte dvě služby: webový server (např. Nginx) a databázi (např. MySQL). Pokud máte nainstalovaný Docker, otestujte strukturu zadáním příkazu `docker-compose up`.


## 5. Verzovací systémy, jejich funkce a využití v praxi

**1. Inicializace Git repozitáře a první commit**
*   **Cíl:** Začít sledovat změny v souborech v lokálním adresáři.
*   **Nástroj:** Git Bash nebo konzole
*   **Postup:** Ve složce s testovacím souborem spusťte příkaz `git init`. Tím vytvoříte repozitář. Přidejte soubor do sledování pomocí `git add .` a potvrďte změnu tzv. commitem: `git commit -m "První verze souboru"`.

**2. Práce na paralelní větvi (Branching)**
*   **Cíl:** Bezpečně upravovat kód, aniž byste ohrozili hlavní verzi.
*   **Nástroj:** Git Bash
*   **Postup:** Vytvořte novou větev příkazem `git branch experiment`. Přepněte se do ní pomocí `git checkout experiment`. Nyní upravte některý soubor a vytvořte nový commit. Změny se týkají pouze této větve.

**3. Sloučení větví (Merge)**
*   **Cíl:** Aplikovat změny z experimentální větve do hlavní větve,.
*   **Nástroj:** Git Bash
*   **Postup:** Přepněte se zpět do hlavní větve (`git checkout main` nebo `master`). Proveďte příkaz `git merge experiment`. Sledujte, jak se upravený kód přelil do vaší primární pracovní verze.

**4. Vytvoření vzdáleného repozitáře**
*   **Cíl:** Připravit místo na cloudové platformě pro sdílení s týmem,.
*   **Nástroj:** [GitHub](https://github.com/)
*   **Postup:** Založte si bezplatný účet na GitHubu. Klikněte na tlačítko "New repository". Zadejte název, zvolte veřejný či soukromý přístup a vytvořte prázdný repozitář. Zkopírujte si vygenerovanou URL adresu.

**5. Synchronizace Push a Pull**
*   **Cíl:** Odeslat lokální historii změn na server a naopak.
*   **Nástroj:** Git Bash
*   **Postup:** Propojte lokální repozitář se vzdáleným pomocí příkazu `git remote add origin [vaše-URL]`. Zkuste změny odeslat na server příkazem `git push origin main`. Příkazem `git pull` byste naopak stáhli případné změny od kolegů.

**6. Návrat ke starší verzi (Diff a záchrana)**
*   **Cíl:** Porovnat aktuální kód s historií a vrátit se v čase.
*   **Nástroj:** Git Bash
*   **Postup:** Otevřete log historie příkazem `git log` a zkopírujte si hash staršího commitu. Prohlédněte si, co se změnilo, příkazem `git diff`. Pokud chcete aktuální nesmyslné změny v souboru zahodit, použijte `git checkout -- nazev_souboru.py`.


## 6. Využití umělé inteligence při programování

**1. Generování kódu přesným zadáním (Prompting)**
*   **Cíl:** Nechat si podle slovního popisu vygenerovat požadovaný program.
*   **Nástroj:** [ChatGPT](https://chat.openai.com/) nebo [Claude](https://claude.ai/) (free verze)
*   **Postup:** Zadejte přesný požadavek obsahující účel, vstupy, výstupy a omezení. Například: *"Vytvoř funkci v Pythonu, která načte seznam čísel (vstup), odstraní sudá čísla a vrátí součet zbytku (očekávaný výstup). Nesmíš importovat žádné externí knihovny (omezení)."*

**2. Vysvětlení cizího kódu krok za krokem**
*   **Cíl:** Pochopit neznámý a složitý kód pomocí konverzačního asistenta,.
*   **Nástroj:** ChatGPT nebo Claude
*   **Postup:** Najděte si na internetu složitější fragment kódu (například komplikovaný regulární výraz). Vložte jej do AI nástroje s dotazem: *"Vysvětli mi krok za krokem, co dělá tento kód."* Přečtěte si vysvětlení logiky.

**3. Tvorba dokumentačních komentářů a Docstrings**
*   **Cíl:** Zlepšit srozumitelnost kódu vygenerováním dokumentace pomocí AI,.
*   **Nástroj:** ChatGPT
*   **Postup:** Předložte AI vlastní, nekomentovaný kód o délce asi 20 řádků. Požádejte: *"Doplň do tohoto kódu detailní inline komentáře a přidej hlavičkovou dokumentaci popisující, co přesně kód dělá."*

**4. Generování testovacích hraničních případů (Edge cases)**
*   **Cíl:** Nechat si navrhnout testovací scénáře, které by vás samotné nenapadly,.
*   **Nástroj:** ChatGPT
*   **Postup:** Ukažte AI kód vaší jednoduché funkce pro výpočet průměru čísel. Zadejte: *"Navrhni 5 extrémních hraničních případů (edge cases), které by mohly tuto funkci rozbít, a vytvoř pro ně v Pythonu unit testy."*

**5. Simulace opravy chyby pomocí reprodukce**
*   **Cíl:** Zapojit AI do reprodukce a zjišťování hypotéz při pádu programu,.
*   **Nástroj:** ChatGPT
*   **Postup:** Nasimulujte chybu ve vlastním kódu tak, aby vám kompilátor nebo terminál vyhodil chybovou hlášku. Zkopírujte zdrojový kód i s přesným chybovým výpisem do AI a požádejte: *"Při tomto vstupu mi program padá s touto chybou. Jaké jsou hypotézy příčiny a jak chybu opravím?"*.

**6. Návrh alternativního řešení a Refaktoring**
*   **Cíl:** Využít AI k analýze kódu a optimalizaci na efektivnější řešení bez změny chování.
*   **Nástroj:** ChatGPT
*   **Postup:** Vložte do AI pomalejší a neefektivní kód (například dvě do sebe vnořené smyčky `for`). Přidejte příkaz: *"Navrhni čistší alternativní řešení pro tento kód a zachovej jeho vnější chování."*. Porovnejte původní kód (diff) s nově navrženým řešením.