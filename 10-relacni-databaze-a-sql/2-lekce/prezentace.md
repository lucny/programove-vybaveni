## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Návrh začíná otázkami, ne tabulkami**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Databáze není cílem sama o sobě. Nejdříve je třeba zjistit, co má systém umět, kdo jej používá a která pravidla nesmí porušit. U rezervačního systému mohou požadavky znít: student vidí volné učebny, učitel vytvoří rezervaci, správce zablokuje místnost kvůli opravě a vedení zjistí vytížení budov. Zároveň nesmějí vzniknout dvě platné rezervace stejné učebny ve stejném čase.

Při analýze se hledají entity, jejich vlastnosti, vztahy a obchodní pravidla. Nestačí opsat políčka z formuláře. Jedno pole „účastníci“ by například v uživatelském rozhraní mohlo působit přirozeně, ale v databázi skrývá opakující se skupinu lidí. Stejně tak věta „rezervace má stav“ vyžaduje rozhodnutí, které stavy existují a jaké přechody mezi nimi jsou povolené.

Následuje **konceptuální návrh**, který popisuje význam dat bez ohledu na konkrétní databázový produkt. **Logický návrh** převádí koncept do tabulek, atributů, klíčů a omezení. **Fyzický návrh** řeší konkrétní datové typy, indexy, rozdělení dat a provozní nastavení zvoleného systému, například PostgreSQL, MySQL, MariaDB, SQL Server nebo Oracle Database. Tato úroveň ovlivňuje výkon, neměla by však opravovat chybný významový model.

***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**ER diagram jako mapa významu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**ER diagram – Entity-Relationship Diagram** zobrazuje entity, jejich atributy a vztahy. V praxi se často používá notace „crow's foot“, v níž symboly na koncích čar vyjadřují minimum a maximum účasti ve vztahu. Diagram školních rezervací může obsahovat entity `Uzivatel`, `Ucebna`, `Rezervace` a `Ucast`. Mezi učebnou a rezervací je vztah 1:N, mezi uživatelem a rezervací může být jednou vztah organizátora 1:N a podruhé vztah účasti N:M.

Diagram není obrázek vytvořený až po hotové databázi. Je to komunikační nástroj, na kterém může učitel, správce školy i vývojář odhalit rozdílné představy dříve, než vznikne kód. Například otázka, zda lze rezervaci přesunout mezi učebnami, rozhoduje o tom, zda je učebna vlastností rezervace, nebo zda má systém evidovat samostatné časové intervaly a historii změn.

**Slabá entita** nemá úplnou identitu bez svého vlastníka. Typickým příkladem je položka objednávky označená pořadovým číslem pouze v rámci jedné objednávky; identifikuje ji tedy dvojice `(objednavka_id, poradi)`. Faktura naproti tomu běžně vlastní samostatné číslo a automaticky slabou entitou není. Toto rozlišení ukazuje, proč návrh nelze odvodit jen z názvu objektu.

***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Normalizace odstraňuje skryté závislosti**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Normalizace rozděluje data tak, aby jeden fakt nebyl zbytečně uložen na mnoha místech a nevznikaly **anomálie vložení, změny a odstranění**. Není to samoúčelná soutěž v počtu tabulek. Je to způsob, jak vyjádřit, na čem který údaj skutečně závisí.

V **první normální formě (1NF)** má každá pozice tabulky jednu hodnotu odpovídající dané doméně a neopakují se skupiny sloupců typu `ucastnik1`, `ucastnik2`, `ucastnik3`. Seznam účastníků se proto nepíše do jednoho textového pole; každý vztah se uloží jako samostatný řádek vazební tabulky. „Atomická“ hodnota přitom závisí na zamýšleném použití. Celá poštovní adresa může být pro jeden systém jediným textem, zatímco doručovací systém ji potřebuje rozdělit.

**Druhá normální forma (2NF)** řeší částečnou závislost na složeném klíči. Kdyby tabulka účasti s klíčem `(rezervace_id, uzivatel_id)` obsahovala také `email_uzivatele`, e-mail by závisel pouze na `uzivatel_id`, nikoli na celé dvojici. Patří tedy do tabulky uživatelů. U tabulky s jednosloupcovým klíčem je podmínka 2NF splněna automaticky, pokud je již v 1NF.

**Třetí normální forma (3NF)** odstraňuje tranzitivní závislosti neklíčových atributů. Kdyby tabulka učeben obsahovala `budova_id` i `adresa_budovy`, adresa by závisela na budově a teprve budova na učebně. Údaj o adrese patří do samostatné tabulky `budova`. Praktická pomůcka říká, že neklíčový údaj má popisovat „klíč, celý klíč a nic než klíč“, ale skutečné rozhodnutí vychází z funkčních závislostí a významu dat.

Vyšší normální formy řeší další druhy závislostí, pro základní návrh však obvykle stačí dobře porozumět prvním třem. Někdy se data záměrně **denormalizují**, například v analytickém skladu nebo kvůli velmi častému čtení. Takový krok má být vědomým kompromisem s jasným způsobem, jak udržet kopie konzistentní, ne opravou špatně navrženého dotazu.

***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Omezení převádějí pravidla do databáze**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Pravidlo, které zůstane pouze v dokumentaci nebo ve formuláři jedné aplikace, lze snadno obejít jiným importem či programem. Proto se co nejvíce pravidel zapisuje přímo do schématu. `PRIMARY KEY` chrání identitu, `FOREIGN KEY` odkazy, `UNIQUE` jedinečnost, `NOT NULL` povinné údaje a `CHECK` podmínky nad hodnotou či řádkem.

Databáze může například kontrolovat, že kapacita učebny je kladná a konec rezervace následuje po začátku. Složitější pravidlo zákazu překrývajících se rezervací vyžaduje podle systému zvláštní omezení, transakční logiku nebo bezpečně napsanou proceduru. Jednoduchá kontrola „nejprve se podívám a potom vložím“ v aplikaci nestačí: mezi těmito dvěma kroky může stejný termín obsadit jiný uživatel.

---

# Lekce 3: Vytvoření databáze a bezpečné změny dat

***
