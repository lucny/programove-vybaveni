<!--
title: Od požadavků k databázovému schématu – kvíz
language: cs
-->

# 1. Testovací část

**1. Čím začíná smysluplný návrh databáze?**

<!-- data-randomize="true" -->
[(X)] Zjištěním požadavků, uživatelů a pravidel systému.
[( )] Výběrem indexu pro každý sloupec.
[( )] Zápisem hotových příkazů `CREATE TABLE`.
[( )] Importem formuláře do databáze.

---

**2. Co zachycuje konceptuální návrh?**

<!-- data-randomize="true" -->
[(X)] Význam entit a vztahů nezávisle na konkrétním databázovém produktu.
[( )] Konkrétní nastavení indexů a rozdělení dat.
[( )] Pouze vzhled uživatelského formuláře.
[( )] Postup pro obnovu databáze ze zálohy.

---

**3. Co převádí logický návrh?**

<!-- data-randomize="true" -->
[(X)] Koncept na tabulky, atributy, klíče a omezení.
[( )] Tabulky na grafické prvky ER diagramu.
[( )] Zálohu na soubor CSV.
[( )] Oprávnění na názvy uživatelů.

---

**4. Které rozhodnutí patří do fyzického návrhu?**

<!-- data-randomize="true" -->
[(X)] Volba datových typů, indexů a provozního nastavení konkrétního DBMS.
[( )] Určení, zda existuje entita učebna.
[( )] Rozlišení organizátora a účastníka rezervace.
[( )] Stanovení, že rezervace nesmějí kolidovat.

---

**5. K čemu slouží ER diagram?**

<!-- data-randomize="true" -->
[(X)] Ke společné diskusi o entitách, atributech a vztazích před tvorbou kódu.
[( )] K automatickému zrychlení všech dotazů.
[( )] K uložení dat namísto tabulek.
[( )] K šifrování citlivých hodnot.

---

**6. Co znamená, že položka objednávky je slabá entita?**

<!-- data-randomize="true" -->
[(X)] Bez objednávky nemá úplnou identitu; určí ji například objednávka a pořadí.
[( )] Nikdy nemůže obsahovat žádné atributy.
[( )] Musí být uložena v jediné společné tabulce.
[( )] Nemůže odkazovat na jiný záznam.

---

**7. Co požaduje první normální forma?**

<!-- data-randomize="true" -->
[(X)] Jednu hodnotu dané domény v každé pozici a žádné opakující se skupiny.
[( )] Všechny tabulky musí mít umělý číselný klíč.
[( )] Každý atribut musí být povinný.
[( )] Všechny dotazy musí používat index.

---

**8. Jakou závislost odstraňuje druhá normální forma?**

<!-- data-randomize="true" -->
[(X)] Závislost neklíčového údaje jen na části složeného klíče.
[( )] Závislost mezi tabulkou a databázovým serverem.
[( )] Závislost výsledku na pořadí řádků.
[( )] Závislost cizího klíče na primárním klíči.

---

**9. Co řeší třetí normální forma?**

<!-- data-randomize="true" -->
[(X)] Tranzitivní závislost neklíčového atributu na jiném neklíčovém atributu.
[( )] Počet povolených uživatelů databáze.
[( )] Podmínku pro spojení dvou tabulek.
[( )] Automatické generování identifikátoru.

---

**10. Která pravidla lze běžně zapsat přímo do schématu?**

<!-- data-randomize="true" -->
[[X]] Jedinečnost e-mailu.
[[X]] Povinné vyplnění kapacity.
[[X]] Kladná hodnota kapacity.
[[X]] Odkaz na existující učebnu.
[[ ]] Zákaz překryvu rezervací vždy vyřeší jediný `CHECK`.

# 2. Interaktivní shrnutí kapitoly

## Od problému k modelu

Databáze není cílem sama o sobě. Návrh začíná otázkami, co má systém umožnit, kdo ho používá a která pravidla nesmí být porušena. Rezervační systém může zobrazit volné učebny, umožnit učiteli rezervaci a správci blokaci místnosti. Současně musí zabránit dvěma platným rezervacím stejné učebny v jednom čase. Při analýze se hledají entity, jejich vlastnosti, vztahy a [[pravidla]].

Nestačí opsat prvky formuláře. Pole „účastníci“ může v rozhraní vypadat jako jedna položka, ale v datech představuje opakující se skupinu lidí. Také stav rezervace vyžaduje výčet možných stavů a povolených přechodů. Model má vyjádřit skutečný význam, ne jen současnou podobu obrazovky.

## Tři úrovně návrhu

Konceptuální návrh popisuje, co data znamenají, bez vazby na konkrétní databázi. Logický návrh převádí tento model na tabulky, atributy, klíče a omezení. Fyzický návrh pak volí konkrétní datové typy, [[indexy]], rozdělení dat a provozní parametry systému, například PostgreSQL nebo MySQL. Fyzická vrstva ovlivňuje výkon, ale nemůže napravit chybný významový model.

ER diagram zobrazuje entity, jejich atributy a vztahy. V notaci crow's foot symboly na koncích čar vyjadřují minimální a maximální účast. Diagram je komunikační nástroj: učitel, správce a vývojář na něm mohou odhalit rozdílné představy dříve, než se vytvoří databáze. Entita je [[slabá]], pokud bez vlastníka nemá úplnou identitu; položku objednávky může určit dvojice `objednavka_id` a pořadí.

## Normalizace jako práce se závislostmi

Normalizace rozděluje data tak, aby se jeden fakt zbytečně neopakoval a nevznikaly anomálie při vložení, změně nebo odstranění. První normální forma (1NF) vyžaduje jednu hodnotu v každé pozici tabulky a odmítá opakující se skupiny typu `ucastnik1`, `ucastnik2`. Vztah účasti se proto ukládá jako samostatný řádek vazební tabulky, nikoli jako seznam v jednom poli. Co je atomické, závisí na účelu: adresa může být pro jeden systém text, pro doručování soubor samostatných částí.

Ve 2NF nesmí neklíčový údaj záviset jen na části složeného klíče. E-mail uživatele proto nepatří k dvojici `(rezervace_id, uzivatel_id)`, ale do tabulky uživatelů. 3NF odstraňuje [[tranzitivní]] závislosti: adresa budovy patří k budově, ne přímo k učebně, která na budovu odkazuje. Normalizace není soutěž v počtu tabulek; vychází z funkčních závislostí a významu údajů.

## Pravidla, která databáze vynutí

Pravidlo jen ve formuláři může obejít jiná aplikace nebo import. `PRIMARY KEY` chrání identitu, `FOREIGN KEY` odkazy, `UNIQUE` jedinečnost, `NOT NULL` povinnost hodnoty a `CHECK` podmínky nad hodnotou či řádkem. Databáze například umí zajistit kladnou kapacitu a to, že konec rezervace následuje po začátku. Zákaz kolizí je složitější: podle produktu potřebuje zvláštní omezení, transakční logiku nebo bezpečnou proceduru. Samotné „nejprve ověřit, pak vložit“ není při souběhu dostatečné.

## Vědomé kompromisy

Vyšší normální formy rozlišují další druhy závislostí, pro základní návrh však obvykle stačí porozumět prvním třem. Někdy je rozumné data záměrně denormalizovat, například v analytickém skladu nebo pro velmi časté čtení. Takové kopie ale musí mít jasný důvod a známý způsob, jak zůstanou konzistentní. Denormalizace není náhradou za špatně navržený dotaz. Podobně fyzické volby — datové typy či indexy — mají podporovat správný model, nikoli dodatečně opravovat nejasný význam dat.

Normalizace má omezit [[ opakování faktů | (redundanci a anomálie) | počet všech tabulek ]], ne vytvářet tabulky bez významu.

**Vyber pravidla vhodná pro databázové schéma:**

<!-- data-randomize="true" -->
[[X]] Jedinečnost hodnoty lze vyjádřit omezením `UNIQUE`.
[[X]] Povinný atribut lze vyjádřit pomocí `NOT NULL`.
[[ ]] Každé složité pravidlo vyřeší kontrola pouze ve formuláři.
