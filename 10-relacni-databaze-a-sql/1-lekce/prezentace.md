## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Proč nestačí jedna velká tabulka**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednoduchý seznam rezervací by mohl obsahovat datum, čas, číslo učebny, kapacitu, jméno organizátora, jeho e-mail a názvy všech účastníků. Dokud má seznam deset řádků, vypadá použitelně. Jakmile se však změní kapacita učebny, je nutné opravit každý řádek, ve kterém se učebna objevuje. Překlep v jediném z nich vytvoří dvě různé verze téhož údaje. Smazání poslední rezervace určité učebny by navíc mohlo odstranit i jedinou informaci o její existenci.

Relační databáze řeší podobné potíže tím, že rozděluje fakta podle jejich významu. Údaj o učebně patří do tabulky `ucebna`, údaje o člověku do tabulky `uzivatel` a konkrétní událost do tabulky `rezervace`. Vztah mezi rezervací a účastníky zachytí další tabulka. Každé tvrzení se tak pokud možno ukládá na jednom místě a ostatní části databáze se na něj odkazují.

Relační model formuloval Edgar F. Codd na začátku sedmdesátých let. Jeho matematickým základem je **relace**, tedy množina uspořádaných n-tic. V běžném databázovém systému ji prakticky vnímáme jako tabulku. Sloupce představují **atributy**, řádky jednotlivé n-tice neboli záznamy a každému atributu přísluší určitá **doména** povolených hodnot. Databázové SQL tabulky nejsou přesnou kopií matematických relací – mohou například pracovat s `NULL` a bez omezení připustit duplicitní řádky. Myšlenka popsat data pomocí vztahů a operovat nad nimi jako nad celky však zůstává základem.

***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Tabulka, řádek, sloupec a datový typ**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Dobrá tabulka zastupuje jeden druh objektu nebo události. Tabulka `ucebna` může mít sloupce `ucebna_id`, `oznaceni`, `kapacita` a `budova`; tabulka `rezervace` sloupce `rezervace_id`, `ucebna_id`, `organizator_id`, `zacatek`, `konec` a `ucel`. Jeden řádek rezervace pak tvrdí, že určitý organizátor obsadil určitou učebnu v konkrétním čase.

Sloupec má kromě názvu také datový typ. Text, celé číslo, desetinné číslo, datum, časový okamžik a logická hodnota nejsou zaměnitelné obaly. Typ určuje, které hodnoty lze uložit a jaké operace dávají smysl. Datum lze chronologicky řadit a odčítat, zatímco text `"12. 3. 2026"` je pro databázi jen posloupnost znaků závislá na zápisu. Peněžní částky je obvykle vhodnější ukládat jako přesné desetinné číslo než jako binární číslo s plovoucí desetinnou čárkou.

Zvláštní hodnotou je `NULL`. Neznamená nulu ani prázdný text, ale chybějící, neznámou nebo nepoužitelnou hodnotu. Proto se na ni neptáme pomocí `= NULL`, nýbrž pomocí `IS NULL`. Porovnání s neznámou hodnotou totiž nevede jednoduše k pravdě či nepravdě; SQL používá tříhodnotovou logiku s výsledky pravda, nepravda a neznámo. To je důvod, proč mohou řádky s `NULL` z výsledku podmínky nečekaně zmizet.

***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Klíče dávají záznamům identitu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Každý řádek musí být spolehlivě rozlišitelný. **Kandidátský klíč** je minimální kombinace atributů, která záznam jednoznačně určuje. U uživatele může být kandidátem školní e-mail; databázový návrhář z kandidátů zvolí **primární klíč**. Často jde o uměle vytvořené číselné nebo UUID identifikační číslo, protože jméno ani e-mail nemusejí být po celou dobu neměnné. Další kandidátské klíče lze chránit omezením `UNIQUE`.

Primární klíč může být i **složený**. V tabulce `ucastnik_rezervace` může dvojice `(rezervace_id, uzivatel_id)` současně říkat, ke které rezervaci uživatel patří, a zabránit jeho dvojímu přihlášení. Umělý identifikátor není povinný v každé tabulce; rozhodující je stabilní a jednoznačná identita.

**Cizí klíč** propojuje řádek s řádkem jiné, případně stejné tabulky. Hodnota `rezervace.ucebna_id` musí odpovídat existující učebně. Databázový systém tak dokáže odmítnout rezervaci neexistující místnosti. Cizí klíč tedy není jen pomůcka pro dotazy, ale pravidlo referenční integrity.

***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kardinalita a převod vztahů do tabulek**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Vztah **1:N** znamená, že jedna učebna může mít mnoho rezervací, ale každá rezervace se týká právě jedné učebny. Cizí klíč se proto umístí na stranu „mnoho“, tedy do tabulky `rezervace`. U vztahu **1:1** patří odkaz obvykle tam, kde dává významově smysl, a jeho jedinečnost se zajistí omezením `UNIQUE`. Příkladem může být uživatel a jeho volitelný profil s rozšířenými údaji.

Vztah **N:M** nelze zachytit jediným cizím klíčem. Jedna rezervace má více účastníků a jeden uživatel se účastní více rezervací. Vznikne proto **vazební tabulka** `ucastnik_rezervace`, jejíž každý řádek představuje jedno přihlášení. Vazební tabulka může nést i vlastní údaje, například čas přihlášení nebo roli účastníka.

Kardinalita sama neříká vše. Návrh musí určit také povinnost vztahu. Rezervace musí mít organizátora, ale uživatel nemusí mít žádnou rezervaci. Tyto rozdíly se později projeví v povolení či zákazu `NULL`, v cizích klíčích a ve způsobu spojování tabulek.

---

# Lekce 2: Od požadavků k databázovému schématu

***
