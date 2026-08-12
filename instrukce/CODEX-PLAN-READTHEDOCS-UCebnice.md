# Autonomní plán pro Codex: elektronická učebnice Read the Docs

## 0. Cíl

Vytvoř opakovatelný publikační systém, který z existujícího repozitáře s výukovými okruhy generuje elektronickou učebnici založenou na **MkDocs + Material for MkDocs** a publikovatelnou přes **Read the Docs**.

Zdroj pravdy zůstává v současné struktuře repozitáře:

- hlavní revidovaný Markdown dokument každého okruhu;
- šest složek `1-lekce` až `6-lekce`;
- LiaScript kvízy `K-L-QUIZ.md`;
- WEBP grafická shrnutí v `media/images`;
- volitelné budoucí doplňkové praktické kapitoly.

Publikační vrstva (`docs/`, PDF, LaTeX, `mkdocs.yml`) musí být **generovaná a kdykoli reprodukovatelná**. Neprováděj ruční úpravy stovek výsledných stránek.

---

# 1. Neměnné zásady

1. **Neměň odborný obsah master dokumentů.** Neopravuj styl, terminologii, fakta ani strukturu podkapitol, pokud k tomu není samostatné zadání.
2. **Neměň obsah QUIZ souborů.** Pouze je validuj a generuj na ně správné LiaScript odkazy.
3. **Neměň WEBP obrázky.** Pro LaTeX/PDF můžeš vytvořit dočasné PNG kopie.
4. **Neodhaduj chybějící názvy nebo vazby.** Nejednoznačnost je validační chyba.
5. **Nevytvářej ručně 120 lekcí.** Vytvoř parser, validátor a generátor.
6. **Pracuj nedestruktivně.** Neprováděj `git reset --hard`, `git clean -fd` ani mazání uživatelských změn.
7. **Generované soubory musí být označené.** Každý generovaný Markdown začni komentářem:

```html
<!--
GENERATED FILE.
Do not edit manually.
Generator: tools/textbook.py
Source: ...
-->
```

---

# 2. Git a bezpečný začátek

Nejprve spusť:

```bash
git status
git branch --show-current
git remote -v
```

Pokud je pracovní strom čistý, vytvoř větev:

```text
feature/readthedocs-textbook
```

Pokud existují nesouvisející necommitnuté změny, nesmaž je a nepřidávej je do svých commitů. Pokud by hrozilo jejich přepsání, zastav se a napiš přesný konflikt.

Commity vytvářej až po úspěšném dokončení jednotlivých fází.

---

# 3. Očekávaná zdrojová struktura

Tematické adresáře mají podobu:

```text
01-zaklady-informatiky/
02-programy-a-data/
03-informacni-a-databazove-systemy/
...
20-datove-struktury-a-soubory/
```

Každý okruh má:

```text
<topic>/
├── <master>.md
├── 1-lekce/
│   ├── K-1-QUIZ.md
│   └── media/images/*.webp
├── 2-lekce/
├── 3-lekce/
├── 4-lekce/
├── 5-lekce/
└── 6-lekce/
```

Například:

```text
02-programy-a-data/
├── programy-a-data.md
├── 1-lekce/
│   ├── 2-1-QUIZ.md
│   └── media/images/
│       ├── 02-programy-a-data-1-1.webp
│       ├── 02-programy-a-data-1-2.webp
│       └── ...
└── ...
```

Za výukové okruhy nepovažuj:

```text
.vscode/
.opencode/
instrukce/
_generated/
node_modules/
docs/
site/
.textbook-build/
```

---

# 4. Cílová struktura

Vytvoř:

```text
repo/
├── 01-zaklady-informatiky/        # zdroj
├── 02-programy-a-data/            # zdroj
├── ...
├── tools/
│   ├── textbook.py
│   └── README.md
├── textbook/
│   ├── config.yml
│   ├── theme/
│   │   └── extra.css
│   └── templates/
├── docs/                          # generováno
│   ├── index.md
│   ├── stylesheets/
│   │   └── extra.css
│   ├── assets/images/
│   ├── downloads/
│   ├── 01-zaklady-informatiky/
│   │   ├── index.md
│   │   ├── 1-lekce/
│   │   │   ├── index.md
│   │   │   └── případné-doplňky.md
│   │   └── ...
│   └── ...
├── mkdocs.yml
├── requirements.txt
├── .readthedocs.yaml
├── TEXTBOOK-AUTHORING.md
└── TEXTBOOK-BUILD-REPORT.md
```

`docs/` musí být možné smazat a kompletně znovu vytvořit.

---

# 5. Konfigurace

Vytvoř `textbook/config.yml`, minimálně:

```yaml
site:
  name: "Informatika"
  language: "cs"

source:
  topic_pattern: '^\\d{2}-.+$'
  lessons: [1, 2, 3, 4, 5, 6]

liascript:
  reader_base: "https://liascript.github.io/course/?"
  raw_base: ""
  branch: "main"

exports:
  pdf: true
  latex: true

build:
  strict_quizzes: true
  missing_images_are_errors: false
```

`liascript.raw_base` musí být konfigurovatelný. Pro veřejný GitHub repozitář má mít tvar:

```text
https://raw.githubusercontent.com/OWNER/REPOSITORY/main/
```

Je-li prázdné, pokus se bezpečně odvodit GitHub owner/repository z `git remote get-url origin`. Pokud to nejde spolehlivě, skonči s jasnou validační chybou; nevytvářej falešnou URL.

---

# 6. Jeden hlavní nástroj

Vytvoř platformně nezávislý Python CLI:

```text
tools/textbook.py
```

Používej `pathlib` a UTF-8.

Podporuj minimálně:

```bash
python tools/textbook.py audit
python tools/textbook.py validate
python tools/textbook.py build
python tools/textbook.py export
python tools/textbook.py all
```

Podporuj také omezení na pilotní témata:

```bash
python tools/textbook.py validate --topics 01,02
python tools/textbook.py build --topics 01,02
python tools/textbook.py export --topics 01,02
```

Volitelně:

```bash
python tools/textbook.py validate --online
```

---

# 7. Fáze A — audit repozitáře

Nejprve pouze analyzuj, nic negeneruj.

Zjisti:

- počet a seznam tematických adresářů;
- jejich numerické pořadí;
- master Markdown každého okruhu;
- existenci lekcí 1–6;
- očekávaný QUIZ v každé lekci;
- WEBP soubory;
- volitelné `doplnky/`;
- nečekané nebo duplicitní soubory.

Výsledek ulož do:

```text
TEXTBOOK-BUILD-REPORT.md
```

### Hledání master souboru

V kořeni okruhu musí být právě jeden hlavní `.md` kandidát.

Ignoruj:

```text
README*.md
*-QUIZ.md
```

Pokud existují dva nebo více kandidátů, nevybírej podle odhadu. Ohlásit chybu.

---

# 8. Fáze B — parser masterů

Očekávaná struktura:

```markdown
# Název okruhu

## Modernizovaný výukový text

Úvod...

# 1. Název lekce

## 1.1 Název podkapitoly

Text...

## 1.2 Název podkapitoly

Text...

# 2. Název lekce
```

Toleruj:

```text
# 1 Název
# 1. Název
## 1.1 Název
## 1.1. Název
```

Každý okruh musí obsahovat hlavní lekce:

```text
1, 2, 3, 4, 5, 6
```

Podkapitoly v lekci `N` musí patřit k `N.x`.

Počet podkapitol není pevný.

Parser nesmí interpretovat nadpis uvnitř fenced code blocku jako strukturu dokumentu.

### Úvod

Obsah před první lekcí použij pro `docs/<topic>/index.md`.

### Závěrečné propojení

Pokud po 6. lekci existuje:

```markdown
# Závěrečné propojení
```

nebo odpovídající závěrečný blok, připoj jej na konec 6. lekce **před** procvičení. Kvíz má zůstat poslední didaktickou částí lekce.

---

# 9. Fáze C — generování webových stránek

## Jedna hlavní stránka = jedna lekce

Generuj:

```text
docs/<topic>/N-lekce/index.md
```

Stránka obsahuje:

1. H1 název lekce;
2. všechny H2 podkapitoly;
3. původní výukový text;
4. WEBP shrnutí po každé podkapitole;
5. případné závěrečné propojení;
6. odkazy na PDF/LaTeX;
7. blok „Procvičení lekce“ s LiaScript tlačítkem.

## Index okruhu

Generuj:

```text
docs/<topic>/index.md
```

Obsah:

- H1 název okruhu;
- původní úvodní text;
- seznam šesti lekcí;
- PDF celého okruhu;
- LaTeX celého okruhu.

Nevymýšlej nové odborné anotace.

## Hlavní index

`docs/index.md` obsahuje přehled všech okruhů v numerickém pořadí `01 → 20`.

---

# 10. Fáze D — grafická shrnutí

Po každé podkapitole automaticky vlož odpovídající WEBP.

Pro:

```text
topic = 02-programy-a-data
lesson = 1
subchapter = 1
```

očekávej:

```text
02-programy-a-data/1-lekce/media/images/02-programy-a-data-1-1.webp
```

Zkopíruj do například:

```text
docs/assets/images/02-programy-a-data/1-lekce/02-programy-a-data-1-1.webp
```

Alt text:

```text
Grafické shrnutí podkapitoly 1.1 – <název podkapitoly>
```

Pravidla:

- chybějící očekávaný WEBP = warning;
- build pokračuje;
- nevkládej rozbitý odkaz;
- dva kandidáti = error;
- nepřiřaditelný WEBP = warning `orphan image`.

---

# 11. Fáze E — LiaScript kvízy

Pro okruh `K` a lekci `L` očekávej:

```text
K-L-QUIZ.md
```

Například:

```text
02-programy-a-data/1-lekce/2-1-QUIZ.md
```

Číslo v QUIZ názvu nemusí mít úvodní nulu.

## Správná LiaScript URL

Nikdy neodkazuj na MkDocs HTML výstup kvízu.

Použij:

```text
<reader_base><raw_base><relative-path-to-quiz>
```

Příklad:

```text
https://liascript.github.io/course/?https://raw.githubusercontent.com/OWNER/REPO/main/02-programy-a-data/1-lekce/2-1-QUIZ.md
```

Na konec lekce generuj:

```markdown
---

## Procvičení lekce

Ověřte si porozumění v interaktivním kvízu.

[Spustit interaktivní kvíz v LiaScriptu](...){ .md-button .md-button--primary }
```

### Validace

Pokud `strict_quizzes: true`:

- chybějící kvíz = error;
- více kandidátů = error;
- špatné číslo okruhu = error;
- špatné číslo lekce = error.

`validate --online` může volitelně ověřit dostupnost raw URL.

Síťové ověření nesmí být nutné pro běžný lokální build.

Je-li repozitář privátní a raw soubor není veřejně dostupný, explicitně nahlas, že veřejný LiaScript reader jej nebude moci načíst.

---

# 12. Fáze F — budoucí doplňkové kapitoly

Podporuj nepovinný adresář:

```text
N-lekce/doplnky/
```

Například:

```text
1-lekce/doplnky/
├── 01-praktikum-soubory.md
├── 02-experiment-kodovani.md
└── 03-projekt.md
```

Každý doplněk:

- zůstává samostatný zdrojový soubor;
- generuje se jako samostatná stránka;
- patří pod konkrétní lekci v navigaci;
- musí mít první H1;
- řadí se podle číselného prefixu.

Absence `doplnky/` není warning.

Navigace:

```text
02 Programy a data
└── 1. <název lekce>
    ├── Výukový text
    ├── Praktikum ...
    ├── Experiment ...
    └── Projekt ...
```

---

# 13. Fáze G — Material for MkDocs

Použij Material for MkDocs a kompatibilní MkDocs.

Závislosti připni na verze ověřené pilotem. Neinstaluj bez rozmyslu neomezené major verze.

Minimální konfigurace:

```yaml
theme:
  name: material
  language: cs
  features:
    - navigation.sections
    - navigation.indexes
    - navigation.path
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy

plugins:
  - search

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - pymdownx.details
  - pymdownx.superfences
```

Pokud konkrétní verze některý parametr nepodporuje, ověř dokumentaci a použij funkční ekvivalent.

---

# 14. Fáze H — navigace

Globální navigace:

```text
Informatika
├── 01 Základy informatiky
│   ├── Přehled
│   ├── 1. <lekce>
│   │   ├── Výukový text
│   │   └── případné doplňky
│   ├── ...
│   └── 6. <lekce>
├── 02 Programy a data
│   └── ...
└── ...
```

Podkapitoly `1.1`, `1.2` atd. nevkládej do globálního sidebaru. Mají být v lokálním TOC dané lekce.

Názvy lekcí získávej z master dokumentů, nikoli z adresářů `1-lekce`.

---

# 15. Fáze I — stylové výukové bloky

Podporuj explicitně označené bloky:

```text
principle
example
tip
warning
history
practice
```

Význam:

```text
principle = podstatný princip
example   = konkrétní příklad
tip       = praktické doporučení
warning   = riziko nebo důležité upozornění
history   = historická či kontextová poznámka
practice  = praktikum nebo experiment
```

Zdrojová syntax:

```markdown
!!! principle "Princip"
    Text.
```

Generátor **nesmí sám rozhodovat**, který běžný odstavec má být převeden na box.

Vzhled střídmý:

```text
principle → tmavě modrý akcent
example   → tyrkysový
tip       → neutrální/středně modrý
warning   → červený pouze pro riziko
history   → šedý
practice  → oranžový
```

Barva nesmí být jediným nositelem významu.

---

# 16. Fáze J — vlastní CSS

Vytvoř:

```text
textbook/theme/extra.css
```

a při buildu kopíruj do:

```text
docs/stylesheets/extra.css
```

Uprav:

- rozumnou maximální šířku textového sloupce;
- typografii nadpisů;
- mezery;
- responzivní obrázky;
- WEBP shrnutí;
- LiaScript tlačítko;
- download tlačítka;
- admonition bloky;
- mobilní zobrazení;
- tiskový režim.

Nevytvářej neonové, animované ani dekorativně přeplněné UI.

---

# 17. Fáze K — LaTeX a PDF

Generuj z téhož připraveného obsahu jako web:

```text
generated Markdown
       ↓
Pandoc
       ├── .tex
       └── PDF přes XeLaTeX
```

## WEBP

Pro export vytvoř dočasné PNG v:

```text
.textbook-build/export-assets/
```

Původní WEBP nikdy nepřepisuj.

## Výstupy pro lekci

```text
docs/downloads/<topic>/<topic>-N.pdf
docs/downloads/<topic>/<topic>-N.tex
```

## Výstupy pro celý okruh

```text
docs/downloads/<topic>/<topic>.pdf
docs/downloads/<topic>/<topic>.tex
```

Například:

```text
docs/downloads/02-programy-a-data/
├── 02-programy-a-data.pdf
├── 02-programy-a-data.tex
├── 02-programy-a-data-1.pdf
├── 02-programy-a-data-1.tex
└── ...
```

PDF musí správně zobrazovat českou diakritiku, kód, tabulky a obrázky.

Obrázky omez na `\linewidth`.

Interaktivní kvíz v PDF nahraď klikacím odkazem na LiaScript. QR kód je volitelné budoucí rozšíření.

Pokud jsou exporty v konfiguraci zapnuté, jejich selhání je produkční build error.

---

# 18. Fáze L — Read the Docs

Vytvoř `.readthedocs.yaml`.

Musí:

1. použít podporované Linux prostředí;
2. instalovat Python závislosti;
3. před MkDocs buildem spustit generátor;
4. instalovat potřebné systémové nástroje pro Pandoc/XeLaTeX;
5. použít `mkdocs.yml`.

Přesnou syntaxi ověř podle **aktuální dokumentace Read the Docs v okamžiku implementace**. Nevymýšlej neověřené klíče.

Preferuj aktuálně podporovaný build hook, ve kterém už jsou dostupné potřebné závislosti.

Ověř:

```bash
mkdocs build --strict
```

a následně Read the Docs preview/production build, pokud je dostupný.

---

# 19. Fáze M — `.gitignore`

Generované artefakty necommituj, pokud nejsou nutné pro hosting.

Zvaž:

```text
site/
docs/
.textbook-build/
```

Pokud Read the Docs umí spolehlivě `docs/` generovat během buildu, ignoruj jej.

Pokud hosting vyžaduje committed `docs/`, změnu zdokumentuj. Nedělej to automaticky bez důvodu.

---

# 20. Fáze N — automatické testy

Použij `pytest`.

Testuj minimálně:

## Parser

- přesně šest lekcí;
- podkapitoly;
- závěrečné propojení;
- české znaky;
- code fences;
- tabulky;
- nadpisy v code blocku nesmí ovlivnit parser.

## Obrázky

- správné přiřazení;
- chybějící obrázek;
- orphan image;
- duplicita.

## QUIZ

- správné párování;
- chybějící soubor;
- špatné číslo tématu;
- špatné číslo lekce.

## Doplňky

- řazení;
- první H1;
- absence složky je v pořádku.

## Výstup

- relativní odkazy;
- žádné `D:\...`;
- žádné jiné absolutní lokální cesty;
- správné LiaScript URL;
- správné kopírování médií;
- očekávané PDF/TEX.

---

# 21. Fáze O — pilot pouze na 01 a 02

Nejdříve:

```bash
python tools/textbook.py audit
python tools/textbook.py validate --topics 01,02
python tools/textbook.py build --topics 01,02
python tools/textbook.py export --topics 01,02
mkdocs serve
```

Ručně ověř:

- hlavní navigaci;
- názvy lekcí;
- lokální TOC;
- českou diakritiku;
- tabulky a kód;
- WEBP po správné podkapitole;
- responzivitu;
- minimálně 4 různé LiaScript kvízy;
- PDF jedné lekce;
- PDF celého okruhu;
- TEX jedné lekce;
- odkazy uvnitř PDF;
- fulltextové hledání;
- admonition bloky, pokud existují.

**Pilot je úspěšný pouze tehdy, pokud není nutné ručně opravovat generované `docs/`.**

Potřebná oprava se vždy provede v parseru/generátoru/configu.

---

# 22. Fáze P — rozšíření na všechny okruhy

Po úspěšném pilotu:

```bash
python tools/textbook.py all
mkdocs build --strict
pytest
```

Očekávaný základ:

```text
20 okruhů
6 základních lekcí na okruh
cca 120 hlavních lekcí
cca 120 LiaScript kvízů
```

Skutečné počty vždy zjisti z repozitáře. Pokud se liší, uveď rozdíl v reportu.

---

# 23. Validační report

`TEXTBOOK-BUILD-REPORT.md` musí obsahovat:

```text
Datum a čas
Git commit
Počet témat
Počet lekcí
Počet podkapitol
Počet nalezených QUIZ
Počet chybějících QUIZ
Počet nalezených WEBP
Počet chybějících očekávaných WEBP
Počet orphan WEBP
Počet doplňkových kapitol
Počet PDF
Počet TEX
Chyby
Warningy
```

Chyby seskup podle tématu.

Volitelně vytvoř i:

```text
.textbook-build/report.json
```

---

# 24. Dokumentace pro autora

Vytvoř krátký praktický soubor:

```text
TEXTBOOK-AUTHORING.md
```

Musí vysvětlit:

- kde editovat master;
- jak pojmenovat QUIZ;
- jak pojmenovat WEBP;
- jak přidat `doplnky/`;
- jak použít `!!! principle`, `!!! example` atd.;
- jak spustit `validate`;
- jak spustit lokální web;
- jak vytvořit PDF/LaTeX;
- co nikdy needitovat ručně;
- jak řešit běžné validační chyby.

---

# 25. Běžný workflow po dokončení

Autor má později postupovat pouze:

```text
1. upravit master / QUIZ / WEBP / doplněk
2. python tools/textbook.py validate
3. python tools/textbook.py all
4. mkdocs serve
5. vizuálně zkontrolovat
6. commit + push
7. Read the Docs provede nový build
```

Autor nemá ručně editovat:

```text
docs/
mkdocs.yml
PDF
TEX
```

pokud jsou tyto soubory generované.

---

# 26. Doporučené commity

Po stabilních fázích:

```text
build: add textbook repository audit
build: add source structure validator
build: generate MkDocs lesson pages
feat: add lesson images and LiaScript quiz links
feat: add Material navigation and textbook styling
feat: support optional lesson supplements
feat: add PDF and LaTeX exports
build: add Read the Docs configuration
test: add textbook generator regression tests
docs: add textbook authoring guide
```

Do commitů nepřidávej nesouvisející uživatelské změny.

---

# 27. Kritéria dokončení

Úkol je hotový jen tehdy, když:

- zdrojové master dokumenty nebyly obsahově přepsány;
- všechny okruhy jsou v numerickém pořadí;
- každá základní lekce má samostatnou stránku;
- všechny podkapitoly zůstaly zachovány;
- existující WEBP se zobrazují za správnou podkapitolou;
- chybějící WEBP jsou reportovány bez rozbití webu;
- každý očekávaný QUIZ má správně sestavenou LiaScript URL;
- LiaScript nedostává MkDocs HTML místo raw Markdownu;
- navigace zobrazuje okruh → lekci → případné doplňky;
- podkapitoly jsou v lokálním TOC;
- hledání funguje;
- stylové bloky jsou konzistentní;
- PDF lekce funguje;
- PDF celého okruhu funguje;
- TEX lekce funguje;
- TEX celého okruhu funguje;
- WEBP se pro TeX převádí pouze do dočasných PNG;
- `mkdocs build --strict` projde;
- testy projdou;
- Read the Docs build projde;
- report neobsahuje nevyřešenou kritickou chybu;
- `TEXTBOOK-AUTHORING.md` popisuje běžnou správu systému.

---

# 28. Co nedělat

Nesmíš:

- ručně vyrábět jednotlivé lekce místo generátoru;
- ručně udržovat stovky odkazů na obrázky;
- svévolně opravovat výukové texty;
- měnit obsah testů;
- hádat nejednoznačné párování;
- převádět LiaScript QUIZ na běžnou statickou MkDocs stránku;
- používat iframe pro LiaScript jako výchozí řešení;
- používat absolutní Windows cesty;
- záviset na Windows-only řešení;
- commitovat `node_modules`;
- skrývat warningy;
- pokračovat po chybě, která může způsobit nesprávné přiřazení obsahu.

---

# 29. Priorita implementace

Pokud bude nutné postup rozdělit, drž pořadí:

```text
1. audit
2. validátor
3. parser
4. generování lekcí
5. obrázky
6. LiaScript
7. navigace a hledání
8. vzhled
9. doplňky
10. LaTeX
11. PDF
12. Read the Docs
13. kosmetická vylepšení
```

Správnost obsahu a párování má vždy přednost před vzhledem.

---

# 30. Závěrečný report Codexu

Po dokončení vypiš:

```text
Větev:
Poslední commit:
Počet témat:
Počet lekcí:
Počet podkapitol:
QUIZ: OK / chyby
WEBP: nalezeno / chybí / orphan
Doplňky:
PDF:
LaTeX:
MkDocs build:
Read the Docs:
Testy:
Známé problémy:
Doporučený další krok:
```

Co nebylo skutečně ověřeno, označ **NEOVĚŘENO**, nikoli `OK`.

---

# 31. První autonomní krok

Začni pouze auditem a validátorem.

Nejprve vytvoř základ `tools/textbook.py`, potom spusť:

```bash
python tools/textbook.py audit
python tools/textbook.py validate --topics 01,02
```

Ověř, že parser správně chápe:

```text
01-zaklady-informatiky
02-programy-a-data
```

Teprve potom pokračuj generováním pilotní učebnice pro tato dvě témata.

Cílem není jednorázově vytvořit dokumentaci. Cílem je vytvořit **spolehlivý dlouhodobý publikační systém**, ve kterém bude možné další roky měnit výukové texty, přidávat snímky, kvízy a praktické kapitoly a celou elektronickou učebnici znovu sestavit jediným příkazem.
