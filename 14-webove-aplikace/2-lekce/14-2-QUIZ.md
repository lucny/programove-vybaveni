<!--
title: Django jako konkrétní příklad backendového frameworku – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.**

<!-- data-randomize="true" -->
[(X)] Projekt, aplikace a cesta požadavku
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Django ORM — Object–Relational Mapping umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.**

<!-- data-randomize="true" -->
[(X)] Model a ORM: objektový pohled na relační databázi
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Když do modelu přidáme pole summary, databáze se sama bezpečně nezmění jen proto, že Pythonová třída vypadá jinak.**

<!-- data-randomize="true" -->
[(X)] Migrace: databázové schéma má historii
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Jednou z praktických předností Djanga je automaticky generované administrační rozhraní.**

<!-- data-randomize="true" -->
[(X)] Administrace a CRUD: rychlý nástroj, ne náhrada veřejného rozhraní
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**5. Které tvrzení odpovídá tématu Projekt, aplikace a cesta požadavku?**

<!-- data-randomize="true" -->
[(X)] Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**6. Které tvrzení odpovídá tématu Administrace a CRUD: rychlý nástroj, ne náhrada veřejného rozhraní?**

<!-- data-randomize="true" -->
[(X)] Jednou z praktických předností Djanga je automaticky generované administrační rozhraní.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Projekt, aplikace a cesta požadavku
[[X]] Model a ORM: objektový pohled na relační databázi
[[X]] Migrace: databázové schéma má historii
[[ ]] Od statické stránky k systému se stavem
[[ ]] MVC a příbuzné návrhové vzory

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Django jako konkrétní příklad backendového frameworku?**

<!-- data-randomize="true" -->
[(X)] Migrace: databázové schéma má historii
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.
[[X]] Django ORM — Object–Relational Mapping umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.
[[ ]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[ ]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Administrace a CRUD: rychlý nástroj, ne náhrada veřejného rozhraní
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

# 2. Interaktivní shrnutí kapitoly

## Projekt, aplikace a požadavek

Django projekt obsahuje konfiguraci celého webu, zatímco jednotlivé aplikace sdružují určitou oblast funkcí. Požadavek prochází přes URL konfiguraci do view, které použije modely nebo další služby a vrátí HTTP odpověď.

Routing propojuje cestu s obslužnou funkcí. View nemá obsahovat všechnu logiku systému; složitější pravidla je vhodné přesunout do vrstev, které lze samostatně testovat.

## Model a ORM

Model popisuje data, typy polí a vztahy. ORM převádí objektové operace na databázové dotazy, takže běžná práce nemusí skládat SQL ručně. ORM však [[ ruší potřebu rozumět databázi | (nezbavuje vývojáře odpovědnosti za dotazy a vztahy) | ukládá všechna data do HTML ]].

Primární a cizí klíče v databázi zůstávají základem integrity, i když s nimi aplikace pracuje přes objekty.

## Migrace

Změna modelu sama nezmění existující databázi. Migrace zaznamenává přechod schématu a dovoluje jej opakovat v dalších prostředích. Příkaz pro vytvoření migrace popíše změnu, její aplikování provede [[migrate]].

**Co patří k bezpečné změně schématu?**

<!-- data-randomize="true" -->
[[X]] evidovat migraci ve verzovacím systému
[[X]] otestovat změnu na realistických datech
[[X]] promyslet převod existujících hodnot
[[ ]] ručně měnit produkční tabulky bez záznamu

## Šablony, administrace a CRUD

Šablona kombinuje připravené HTML s daty z view. Administrace rychle poskytne rozhraní pro správce, ale není automaticky vhodným veřejným rozhraním pro běžné uživatele.

CRUD shrnuje vytvoření, čtení, změnu a odstranění dat. Každá operace musí respektovat validaci a [[oprávnění]], ne pouze existenci odpovídajícího formuláře.
