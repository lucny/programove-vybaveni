## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Od automatického doplňování k AI asistentovi**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Klasické vývojové prostředí již dlouho nabízí **automatické doplňování kódu (autocomplete)**, zvýraznění syntaxe, navigaci mezi symboly nebo statickou analýzu. Tyto nástroje obvykle pracují podle syntaxe jazyka, typů, názvů funkcí a informací dostupných v projektu.

AI asistenti tento princip rozšiřují. Dokážou pracovat s přirozeným jazykem a na základě kontextu navrhovat celé bloky programu, vysvětlovat existující kód nebo provádět změny ve více souborech.

Vývoj lze zjednodušeně popsat jako postup:

**automatické doplňování → generování kódu → konverzační asistent → programovací agent**

- **Automatické doplňování** navrhuje názvy funkcí, metod, proměnných nebo krátké části kódu.
- **Generování kódu** vytváří delší úseky programu podle komentáře nebo zadání v přirozeném jazyce.
- **Konverzační asistent** umožňuje o projektu diskutovat, ptát se na význam kódu nebo požadovat konkrétní úpravy.
- **Programovací agent** může dostat širší úkol, prozkoumat projekt, změnit více souborů, spustit příkazy nebo testy a podle jejich výsledků další postup upravit.

Příklady současných nástrojů zahrnují například **GitHub Copilot, OpenAI Codex, Claude Code** nebo AI funkce integrované přímo do vývojových prostředí. Konkrétní produkty se rychle mění, důležitější je proto pochopit obecný princip jejich práce.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**AI při psaní, vysvětlování a úpravách kódu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


AI může při programování zastávat několik různých rolí. Nejjednodušší je pomoc při psaní nového kódu. Programátor může například zadat:

> Vytvoř funkci v Pythonu, která načte CSV soubor, odstraní prázdné řádky a vrátí seznam slovníků.

AI může připravit návrh funkce, který programátor dále upraví a otestuje. Stejným způsobem lze využít AI také k vysvětlení cizího nebo staršího kódu, doplnění komentářů a dokumentace, návrhu refaktoringu nebo převodu jednoduchého řešení mezi programovacími jazyky.

Mezi běžné možnosti patří:

- **generování nového kódu** podle slovního popisu,
- **doplňování rozepsaných funkcí** a opakujících se konstrukcí,
- **vysvětlení existujícího kódu** krok za krokem,
- **refaktoring** bez změny vnějšího chování programu,
- **tvorba dokumentace** a komentářů,
- **převod jednoduchých částí programu** mezi různými jazyky nebo knihovnami,
- **návrh alternativního řešení** stejného problému.

Kvalita výsledku silně závisí na kvalitě zadání a dostupném kontextu. Obecný požadavek „napiš program“ obvykle poskytne horší výsledek než přesnější specifikace obsahující účel, vstupy, očekávané výstupy, omezení a prostředí, ve kterém má kód fungovat.

Užitečné zadání proto často obsahuje:

**cíl → vstup → očekávaný výstup → omezení → relevantní kontext projektu**

AI nedokáže automaticky poznat všechny nevyřčené požadavky. Pokud například neví, jaké verze knihoven projekt používá nebo jak je uspořádána jeho architektura, může navrhnout řešení, které do projektu nezapadne.

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**AI při ladění, testování a code review**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


AI lze využít také při hledání chyb. Programátor může modelu předložit chybovou zprávu, relevantní část kódu a popis očekávaného chování. AI může navrhnout možné příčiny problému a postup, jak jednotlivé hypotézy ověřit.

Rozumný pracovní postup může vypadat takto:

**chyba → reprodukce → hypotéza → test → oprava → nové spuštění testů**

Důležitá je právě **reprodukce chyby**. Pokud programátor nedokáže popsat, kdy problém nastává, může AI pouze hádat. Stejně jako při běžném ladění je proto vhodné nejprve určit konkrétní vstup a situaci, která chybu vyvolá.

AI může pomoci také při testování:

- navrhnout **unit testy** pro jednotlivé funkce,
- hledat **hraniční případy** (*edge cases*),
- generovat testovací data,
- vysvětlovat příčinu selhání testu,
- navrhovat testy pro chybu, která byla právě opravena,
- kontrolovat změny při **code review**.

Například pro funkci, která počítá průměr hodnot, nestačí otestovat pouze běžný seznam čísel. AI může upozornit také na prázdný seznam, záporné hodnoty, velmi velká čísla nebo chybný datový typ.

AI však **nenahrazuje debugger ani automatické testy**. Její návrh je hypotéza, kterou je třeba ověřit spuštěním programu, testů nebo kontrolou skutečného stavu proměnných.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Agentní programování: když AI dostane celý úkol**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Pokročilejší AI nástroje mohou fungovat jako **programovací agenti**. Místo vytvoření jednoho úseku kódu dostanou širší úkol a samostatně provedou více kroků.

Příklad zadání:

> Přidej do aplikace export dat do CSV. Nejprve prozkoumej strukturu projektu, navrhni postup, proveď potřebné změny, přidej testy a na závěr shrň změněné soubory.

Agent může podle dostupných oprávnění:

1. prohledat soubory projektu,
2. najít relevantní části kódu,
3. vytvořit plán změn,
4. upravit jeden nebo více souborů,
5. spustit kompilaci, linter nebo testy,
6. vyhodnotit vzniklé chyby,
7. provést další opravy,
8. připravit souhrn změn nebo diff k lidské kontrole.

Typický agentní cyklus lze vyjádřit:

**zadání → plán → změna → spuštění → kontrola výsledku → oprava → diff → lidské schválení**

Tento způsob práce se liší od běžného chatování s AI především tím, že model používá **nástroje**. Může například číst a zapisovat soubory, vyhledávat v projektu, spouštět příkazy v terminálu nebo pracovat s verzovacím systémem.

S rostoucí samostatností agenta roste také význam kontroly. Agent může velmi rychle provést rozsáhlou změnu, ale stejnou rychlostí může rozšířit i chybný předpoklad do více částí projektu.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kontext projektu, instrukce a spolupráce s AI**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


AI pracuje pouze s informacemi, které má v daném okamžiku k dispozici. **Kontext** proto patří k nejdůležitějším faktorům ovlivňujícím kvalitu výsledku.

Pro práci nad skutečným projektem může být důležité, aby AI znala například:

- účel a architekturu projektu,
- používaný programovací jazyk a framework,
- způsob instalace závislostí,
- strukturu adresářů,
- pravidla pojmenování a formátování kódu,
- způsob spouštění a testování aplikace,
- části systému, které se nemají měnit,
- očekávané chování výsledku.

Tyto informace mohou být uloženy přímo v projektu. Význam mají například soubory `README.md`, technická dokumentace, testy, konfigurace projektu nebo specializované **instrukční soubory pro AI agenty**.

Dobře organizovaný projekt tak pomáhá nejen lidem, ale také AI. Pokud jsou názvy proměnných srozumitelné, moduly mají jasné odpovědnosti, testy popisují očekávané chování a dokumentace vysvětluje způsob spuštění, AI se v projektu orientuje podstatně lépe.

S AI lze proto pracovat podobně jako s novým členem vývojového týmu. Nestačí mu sdělit pouze „oprav projekt“. Potřebuje znát pravidla, omezení, dostupné nástroje a způsob, podle kterého lze poznat, že je úkol splněn.

***

## Snímek 6.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Proč AI kód nemůžeme slepě přijímat**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Kód vytvořený AI může na první pohled působit velmi přesvědčivě, ale stále může obsahovat chyby. Model generuje pravděpodobné řešení na základě zadaného kontextu a naučených vzorů; nemá automatickou záruku, že navržený program skutečně odpovídá požadavkům.

Mezi typická rizika patří:

- použití **neexistující funkce nebo API**,
- použití zastaralého způsobu práce s knihovnou,
- nesprávné pochopení zadání,
- přehlédnutí hraničních případů,
- zavedení bezpečnostní chyby,
- vytvoření zbytečně složitého řešení,
- změna jiné části programu, která s původním úkolem nesouvisí,
- kód, který sice projde některými testy, ale porušuje architekturu projektu.

Každou významnější AI změnu je proto vhodné podrobit stejnému procesu jako změnu vytvořenou člověkem:

1. **přečíst a pochopit změněný kód,**
2. zkontrolovat **diff**, tedy přesný rozdíl oproti předchozí verzi,
3. spustit program, kompilaci nebo statickou kontrolu,
4. spustit automatické testy,
5. podle potřeby provést bezpečnostní nebo výkonovou kontrolu,
6. teprve potom změnu uložit do verzovacího systému.

Verzovací systém je při práci s AI mimořádně užitečný. Před větší změnou lze vytvořit samostatnou větev a po práci agenta přesně zkontrolovat, co změnil. Pokud je výsledek chybný, lze změny snadno zahodit nebo se vrátit k předchozí verzi.

Základní princip lze shrnout:

**AI může kód navrhnout nebo upravit, ale odpovědnost za jeho přijetí zůstává na vývojáři.**

Využití AI při programování proto nejlépe funguje jako propojení všech nástrojů popsaných v tomto materiálu:

**IDE poskytuje pracovní prostředí → testy ověřují chování → Git uchovává a porovnává změny → AI pomáhá změny navrhovat a provádět → programátor výsledek chápe, kontroluje a schvaluje.**

***
