<!--
title: Fáze tvorby programu a vývojářské nástroje – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co se řeší ve fázi návrhu a plánování?**

<!-- data-randomize="true" -->
[(X)] Struktura aplikace, algoritmy a logika programu.
[( )] Pouze konečné nasazení hotové aplikace.
[( )] Výhradně oprava syntaktických chyb.
[( )] Jen archivace starých verzí dokumentace.

---

**2. K čemu slouží UML?**

<!-- data-randomize="true" -->
[(X)] Ke standardizované vizualizaci návrhu systému pomocí diagramů.
[( )] Ke kompilaci zdrojového kódu.
[( )] Ke správě balíčků v Pythonu.
[( )] K automatickému nasazení kontejnerů.

---

**3. Které typy UML diagramů kapitola uvádí?**

<!-- data-randomize="true" -->
[[X]] diagram tříd
[[X]] diagram aktivit
[[X]] diagram stavů
[[ ]] diagram rychlosti procesoru
[[ ]] diagram zaplnění disku

---

**4. Co je hlavním účelem IDE při psaní kódu?**

<!-- data-randomize="true" -->
[(X)] Spojit editor, ladění a testování do jednoho prostředí.
[( )] Nahradit požadavky a návrh aplikace.
[( )] Uchovávat pouze výsledné binární soubory.
[( )] Sloužit výhradně jako webový prohlížeč.

---

**5. Který nástroj je v kapitole uveden pro jednotkové testování v Javě?**

<!-- data-randomize="true" -->
[(X)] JUnit.
[( )] Selenium.
[( )] Postman.
[( )] Markdown.

---

**6. K čemu se používá Selenium?**

<!-- data-randomize="true" -->
[(X)] K automatizovanému testování webových stránek.
[( )] Ke kreslení UML diagramů.
[( )] K verzování zdrojového kódu.
[( )] Ke generování dokumentace z komentářů.

---

**7. K čemu se používá Postman?**

<!-- data-randomize="true" -->
[(X)] K testování API.
[( )] Ke kompilaci jazyka C.
[( )] K úpravě obrázků.
[( )] Ke správě větví v Gitu.

---

**8. Jakou roli má Git ve vývojovém procesu?**

<!-- data-randomize="true" -->
[(X)] Sleduje změny a podporuje spolupráci nad verzemi kódu.
[( )] Nahrazuje všechny automatické testy.
[( )] Generuje UML diagram tříd.
[( )] Překládá Markdown do strojového kódu.

---

**9. Které nástroje nebo formáty souvisejí podle kapitoly s dokumentací?**

<!-- data-randomize="true" -->
[[X]] Markdown
[[X]] Sphinx
[[X]] Read the Docs
[[ ]] JUnit
[[ ]] Postman

---

**10. Proč je dokumentace důležitou fází?**

<!-- data-randomize="true" -->
[(X)] Podporuje srozumitelnost a dlouhodobou udržitelnost kódu.
[( )] Zajišťuje automaticky bezchybný algoritmus.
[( )] Odstraňuje potřebu verzovacího systému.
[( )] Nahrazuje komunikaci v týmu i testování.


# 2. Interaktivní shrnutí kapitoly

## Vývoj je posloupnost navazujících činností

Tvorba programu nezačíná psaním prvního příkazu. V návrhu se vyjasňuje struktura aplikace, algoritmy a logika. [[UML]] nabízí společný jazyk pro diagramy: diagram tříd zachycuje třídy a vztahy, diagram aktivit procesy a diagram stavů možné stavy objektu.

Modelovací nástroje jako draw.io nebo DIA pomáhají návrh sdílet a zpřesňovat. Diagram však [[ nahrazuje funkční program | (zachycuje vybraný pohled na připravovaný systém) | automaticky opravuje chyby v kódu ]].

## Od editoru k běžící aplikaci

Při implementaci lze použít textový či konzolový editor, integrované prostředí ale spojuje více nástrojů. [[IDE]] obvykle nabízí editor, překlad nebo spuštění, debugger a testování. Volba nástroje závisí na projektu i situaci; rychlá změna skriptu může vzniknout ve Vimu či Nanu, rozsáhlý projekt těží z integrace.

## Testy ověřují různé vrstvy

Jednotkové testy kontrolují malé části kódu pomocí frameworků jako xUnit či [[JUnit]]. Selenium může simulovat práci s webem a [[Postman]] pomáhá posílat a kontrolovat požadavky API.

**Přiřaď nástroje k jejich typickým úlohám:**

<!-- data-randomize="true" -->
[[X]] JUnit — jednotkové testy v Javě
[[X]] Selenium — automatizace webového rozhraní
[[X]] Postman — zkoušení API
[[X]] Git — historie a spolupráce nad kódem
[[ ]] Sphinx — orchestrátor kontejnerů

Testování není jednorázová kontrola na konci. Změny programu je potřeba ověřovat opakovaně, protože oprava jedné části může ovlivnit jinou.

## Historie a znalosti projektu

Git zaznamenává změny a dovoluje návrat, porovnávání i týmovou práci. Platforma GitHub staví nad Gitem sdílení a spolupráci. Dokumentace pak zachycuje účel, použití a rozhodnutí projektu. Markdown usnadňuje prostý strukturovaný text, [[Sphinx]] generování dokumentace a Read the Docs její publikaci.

Dlouhodobě udržitelný projekt proto propojuje [[ (návrh, implementaci, testování, verzování a dokumentaci) | jen psaní a konečné odevzdání | pouze nástroje bez pracovního postupu ]].
