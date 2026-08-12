## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**TeX a LaTeX: proč vznikly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.1 TeX a LaTeX: proč vznikly

LaTeX je jedním z nejdůležitějších systémů pro technické a vědecké publikování.

Je postaven na systému **TeX**, který vytvořil Donald Knuth na konci 70. let 20. století poté, co nebyl spokojen s kvalitou sazby svých matematických knih.

TeX je velmi přesný typografický sazební systém.

LaTeX, původně vytvořený Leslie Lamportem, nad ním přidává vyšší úroveň strukturálních příkazů a dokumentových tříd.

Uživatel tak nemusí řešit každý typografický detail ručně.

Místo:

> nastav nadpis na 17 bodů, bold, mezeru 8 mm…

napíše:

```latex
\section{Výsledky experimentu}
```

Dokumentová třída a šablona rozhodnou, jak bude sekce vypadat.

To je filozoficky velmi podobné Markdownu, ale LaTeX nabízí mnohem větší kontrolu a typografickou přesnost.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**První dokument v LaTeXu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.2 První dokument v LaTeXu

Jednoduchý dokument může vypadat:

```latex
\documentclass{article}

\usepackage[czech]{babel}
\usepackage{amsmath}

\title{Můj první dokument}
\author{Jan Novák}

\begin{document}

\maketitle

\section{Úvod}

Toto je první odstavec dokumentu.

\section{Výpočet}

Platí vztah

\[
E = mc^2
\]

\end{document}
```

Zdrojový `.tex` soubor je prostý text.

Potom jej zpracuje TeX engine a vytvoří například PDF.

Tento proces se často označuje jako **kompilace** nebo sazba.

Klasické nástroje zahrnují pdfLaTeX, XeLaTeX a LuaLaTeX.

Každý používá trochu jiné technologické možnosti.

Pro moderní práci s Unicode a systémovými OpenType fonty jsou velmi zajímavé XeLaTeX a LuaLaTeX.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Příkazy a prostředí**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.3 Příkazy a prostředí

LaTeX používá příkazy začínající zpětným lomítkem.

Například:

```latex
\section{Nadpis}
```

nebo:

```latex
\textbf{tučný text}
```

Složitější struktury se zapisují pomocí **environmentů**:

```latex
\begin{itemize}
  \item První bod
  \item Druhý bod
\end{itemize}
```

Podobně existují prostředí pro rovnice, tabulky, obrázky, citace, theorem nebo code listings.

LaTeX tak připomíná deklarativní programovací jazyk.

Autor především říká:

**co daný objekt znamená**

a sazební systém rozhoduje:

**jak jej typograficky umístit.**

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Matematika: hlavní doména LaTeXu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.4 Matematika: hlavní doména LaTeXu

Jednou z nejsilnějších stránek LaTeXu je matematická sazba.

Inline výraz:

```latex
$E = mc^2$
```

Samostatná rovnice:

```latex
\[
f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
\]
```

Suma:

```latex
\[
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
\]
```

Matice:

```latex
\[
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\]
```

Složitá matematika zůstává ve zdroji systematická a dobře čitelná.

Proto je LaTeX standardním nástrojem v matematice, fyzice, informatice, inženýrství a vědeckých publikacích.

Markdownové systémy často přebírají právě LaTeXovou matematickou syntaxi pomocí nástrojů jako MathJax nebo KaTeX.

To je další důležitý most mezi oběma technologiemi.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Dokumentové třídy a balíčky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.5 Dokumentové třídy a balíčky

LaTeX má modulární strukturu.

Základní typ dokumentu určuje **document class**:

```latex
\documentclass{article}
```

Další možnosti jsou například `report`, `book` nebo `beamer`.

Beamer se používá pro tvorbu prezentací.

Funkce rozšiřují **packages — balíčky**.

Například:

```latex
\usepackage{graphicx}
```

pro obrázky,

```latex
\usepackage{amsmath}
```

pro matematiku,

```latex
\usepackage{hyperref}
```

pro odkazy a PDF hyperlinky.

Ekosystém LaTeXu obsahuje tisíce balíčků distribuovaných například prostřednictvím CTAN.

Běžná instalace LaTeXu proto není pouze jeden program. Distribuce jako TeX Live nebo MiKTeX zahrnuje engine, balíčky, fonty a další nástroje.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Obrázky, tabulky a floating objects**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.6 Obrázky, tabulky a floating objects

V profesionálním dokumentu není vhodné ručně natlačit obrázek na přesné místo bez ohledu na sazbu.

LaTeX používá objekty typu **float**.

Například:

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.7\textwidth]{schema.pdf}
  \caption{Schéma sítě}
  \label{fig:sit}
\end{figure}
```

Sazební systém se snaží obrázek umístit na typograficky vhodné místo.

To může začátečníka překvapit: obrázek nemusí skončit přesně tam, kde je ve zdrojovém souboru.

Tento princip ale pomáhá kvalitě sazby rozsáhlých dokumentů.

Podobně fungují tabulky.

LaTeX nabízí velmi přesnou kontrolu, ale ruční tvorba složitých tabulek může být náročná. Často je proto efektivní tabulku generovat z dat pomocí skriptu.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Křížové odkazy a automatické číslování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.7 Křížové odkazy a automatické číslování

LaTeX exceluje ve velkých dokumentech.

Můžeme označit rovnici:

```latex
\label{eq:newton}
```

a později napsat:

```latex
Rovnice~\ref{eq:newton}
```

Číslo se automaticky dopočítá.

Stejně fungují kapitoly, obrázky, tabulky a rovnice.

To eliminuje ruční aktualizaci čísel.

Při vložení nového obrázku se další obrázky přečíslují automaticky a reference zůstanou správné.

Tato vlastnost je zásadní u diplomových prací, knih a technické dokumentace.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.8

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Bibliografie: BibTeX a biblatex**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.8 Bibliografie: BibTeX a biblatex

V odborném textu potřebujeme systematicky pracovat se zdroji.

Bibliografické údaje lze uložit do `.bib` souboru:

```bibtex
@book{knuth1984,
  author = {Donald E. Knuth},
  title  = {The TeXbook},
  year   = {1984}
}
```

V textu pak citujeme pomocí klíče.

Systém vytvoří citaci, seznam literatury a správný styl záznamu.

Historicky se používá BibTeX.

Modernější workflow často používá balíček `biblatex` spolu s backendem Biber.

Výhodou je opět oddělení **dat o zdrojích** od jejich výsledné grafické podoby.

Jedna bibliografická databáze tak může být vysázena podle různých citačních stylů.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.9

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**LaTeX, Git a reprodukovatelné dokumenty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.9 LaTeX, Git a reprodukovatelné dokumenty

LaTeXový dokument je prostý text, a proto se velmi dobře kombinuje s Git.

To umožňuje přesné verzování, spolupráci, automatické sestavení a review změn.

Vědecký projekt může mít strukturu:

```text
paper/
├── main.tex
├── sections/
├── figures/
├── bibliography.bib
└── data/
```

CI pipeline může po každém commitu automaticky vytvořit nové PDF.

To se blíží principu **reproducible research**.

Zdrojový kód analýzy, data, grafy a výsledná publikace mohou být součástí jednoho verzovaného projektu.

Nástroje jako Jupyter, Quarto, R Markdown nebo Pandoc tuto myšlenku rozšiřují: text lze kombinovat přímo s vykonávaným kódem a automaticky generovanými grafy.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.10

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Markdown versus LaTeX**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 5.10 Markdown versus LaTeX

Markdown a LaTeX nejsou soupeři, kteří řeší stejný problém stejným způsobem.

Markdown je nejlepší tam, kde chceme jednoduchost, rychlost, čitelný zdroj, dokumentaci, web a Git workflow.

LaTeX je silnější tam, kde potřebujeme precizní sazbu, matematiku, bibliografii, rozsáhlou strukturu, automatické reference a profesionální PDF.

Často se velmi dobře kombinují.

Například Pandoc může převést:

**Markdown → LaTeX → PDF**

Autor píše jednoduchý Markdown, ale výsledný PDF dokument vysází LaTeX.

To je typický příklad moderní publikační pipeline:

**jednoduchý zdroj → transformační nástroj → profesionální sazební systém → výsledný dokument**

**Hlavní myšlenka páté lekce:** LaTeX chápe dokument podobně jako program: autor zapisuje strukturu a význam, zatímco sazební systém automaticky řeší vzhled, číslování, reference a typografii.

---

# 6. Publikace, předtisková příprava a elektronické dokumenty

## 6.1 Dokument nekončí tlačítkem Uložit

Dokument má životní cyklus.

Může vzniknout jako Markdown, DOCX, ODT, LaTeX nebo DTP projekt.

Potom prochází revizí, korekturou, sazbou, exportem, kontrolou a publikací.

Výstupní formát závisí na cíli.

Pro web můžeme vytvořit HTML. Pro tisk PDF. Pro čtečky EPUB. Pro další editaci DOCX.

Proto je výhodné přemýšlet o zdrojovém dokumentu a výsledných formátech odděleně.

---

## 6.2 Předtisková příprava

Před odesláním dokumentu do profesionálního tisku se provádí **preflight**.

Kontrolují se například rozměry stránky, spadávka, rozlišení obrázků, fonty, barevné prostory, přetisky, průhlednosti a ořezové značky.

**Spadávka — bleed** znamená, že obraz nebo barevná plocha pokračuje za finální ořez stránky.

Tiskař může papír po tisku oříznout bez rizika, že na hraně vznikne bílý proužek kvůli drobné odchylce řezu.

**Ořezové značky** ukazují místo finálního ořezu.

Není ale vhodné automaticky přidávat všechny tiskové značky do každého PDF. Konkrétní požadavky určuje tiskárna.

---

## 6.3 PostScript a cesta k PDF

PostScript je stránkový popisný jazyk vytvořený společností Adobe.

Místo toho, aby ukládal hotový rastrový obraz stránky, může popsat text, křivky, výplně a transformace.

Tiskárna nebo RIP následně popis rasterizuje pro konkrétní výstupní zařízení.

PostScript měl zásadní význam pro rozvoj digitální sazby a desktop publishingu.

PDF na něj historicky navazuje, ale není prostě jen modernější PostScript.

PDF je dokumentový formát s vlastní strukturou, možností náhodného přístupu k objektům, metadaty, fonty, obrázky a dalšími funkcemi.

V moderním workflow je PDF mnohem běžnější jako výměnný a tiskový formát.

PostScript však zůstává důležitou součástí historie počítačové typografie a pomáhá pochopit myšlenku **page description language**.

---

## 6.4 Elektronické knihy a reflowable layout

Elektronická kniha nemusí mít pevné stránky jako PDF.

Formát **EPUB** typicky používá **reflowable layout**.

Text se přizpůsobuje velikosti displeje, nastavené velikosti písma a orientaci zařízení.

Čtenář může zvětšit písmo a řádky se automaticky přelomí.

Uvnitř EPUB jsou typicky použity technologie příbuzné webu: HTML, CSS, obrázky a metadata.

EPUB je v podstatě strukturovaný balíček těchto zdrojů.

PDF má opačnou filozofii: snaží se zachovat pevný layout stránky.

Proto je PDF vhodné pro odborné články, formuláře a dokumenty s přesnou sazbou.

EPUB je vhodnější pro beletrii a knihy určené pro různé velikosti displejů.

Historický formát MOBI byl významně spojen s ekosystémem Kindle, ale současné e-knižní workflow se výrazně posunulo a EPUB je důležitým otevřeným standardem.

---

## 6.5 Přístupnost dokumentů

Moderní dokument nemá být pouze vizuálně pěkný.

Musí být použitelný také pro lidi používající screen reader, zvětšení, klávesnicovou navigaci nebo jiné asistenční technologie.

Přístupnost začíná strukturou.

Správný nadpis musí být skutečný nadpis.

Obrázek by měl mít alternativní text.

Tabulka má mít logickou strukturu.

Odkaz by neměl být popsán pouze jako `klikněte zde`, ale například `Stáhnout studijní materiál v PDF`.

PDF může obsahovat **tagged structure**, která čtečce obrazovky pomáhá pochopit pořadí a význam prvků.

Markdown a HTML mají velkou výhodu, pokud autor správně používá sémantickou strukturu.

Přístupnost není dodatečný kosmetický krok. Je součást správně navrženého dokumentu.

---

## 6.6 Dokument jako single source of truth

Moderní publikační systémy se stále více snaží nevytvářet každou verzi dokumentu zvlášť.

Místo toho existuje jeden **master source**.

Například:

```text
course.md
```

z něhož lze vytvořit web, PDF, prezentaci nebo e-knihu.

Tento princip se nazývá **single source publishing**.

Velkou výhodou je konzistence.

Když opravíme chybu ve zdroji, změna se může promítnout do všech výstupů.

Nástroje jako Pandoc, Quarto, Sphinx, MkDocs, Docusaurus nebo statické generátory webů používají různé varianty tohoto principu.

Pro rozsáhlé výukové materiály je to mimořádně zajímavé:

**obsah → strukturovaný Markdown → šablony → několik forem publikace**

Právě zde se propojuje textové zpracování s automatizací a softwarovým inženýrstvím.

---

## 6.7 Moderní publikační pipeline

Představme si technickou učebnici.

Autor píše kapitoly v Markdownu.

Matematiku zapisuje LaTeXovou syntaxí.

Obrázky vznikají jako SVG.

Zdrojové soubory jsou v Git repozitáři.

Automatická pipeline provede:

1. kontrolu syntaxe,
2. kontrolu odkazů,
3. generování obsahu,
4. převod Markdownu,
5. sazbu LaTeXem,
6. export PDF,
7. vytvoření HTML webu.

Výsledek může být automaticky publikován.

Tento přístup je velmi odlišný od tradičního dokumentu, který existuje jako jediný `.docx` soubor na jednom počítači.

Text se stává součástí **reprodukovatelného informačního systému**.

To je jedna z nejvýznamnějších změn v současném zpracování textu.

---

## 6.8 Kdy použít který nástroj

Neexistuje jeden nejlepší nástroj pro všechny dokumenty.

**Textový procesor** použijeme, když chceme rychlou interaktivní editaci, spolupracujeme s běžnými kancelářskými uživateli a potřebujeme WYSIWYG.

**Markdown** použijeme, když chceme jednoduchý zdroj, pracujeme s Git, tvoříme dokumentaci, publikujeme na web nebo chceme snadné převody.

**LaTeX** použijeme, když máme matematiku, rozsáhlé odkazy, bibliografii, odbornou sazbu a potřebujeme stabilní automatické PDF.

**DTP** použijeme, když je finální vizuální layout stránky hlavním cílem, pracujeme s časopisem, katalogem nebo knihou s komplexní grafikou a potřebujeme detailní předtiskovou přípravu.

**HTML/CSS** použijeme, když je cílem primárně webový dokument a responzivní zobrazení.

V profesionálním workflow se nástroje často kombinují.

**Hlavní myšlenka šesté lekce:** dokument není jeden soubor ani jedna aplikace. Je to obsah, struktura a sada transformačních kroků, které mohou vést k různým výstupům pro web, tisk, archiv nebo elektronickou knihu.

---

# Závěrečné propojení kurzu

Zpracování textu na počítači začíná jednoduchým znakem a končí celým publikačním systémem.

Na nejnižší úrovni máme:

**znaky → Unicode → bajty**

Z nich vzniká prostý text.

K textu přidáme významovou strukturu:

**odstavec → nadpis → seznam → tabulka → kapitola**

Tu můžeme zapsat různými způsoby:

**Markdown / LaTeX / HTML / DOCX**

Potom přichází typografie:

**font → řádkování → mezery → hierarchie → stránková sazba**

A nakonec publikace:

**zdroj → šablona → sazba → PDF / HTML / EPUB / tisk**

Největší změnou moderního zpracování textu je posun od dokumentu jako jednoho ručně formátovaného souboru k dokumentu jako **strukturovanému zdroji, který lze automaticky transformovat**.

Markdown ukazuje nejjednodušší podobu tohoto principu.

LaTeX ukazuje jeho profesionální sazební variantu.

Git umožňuje zdroj verzovat.

Pandoc, Quarto a podobné nástroje z něj mohou generovat více výstupů.

A automatizační pipeline může celý proces opakovat pokaždé stejným způsobem.

Výsledná cesta proto může vypadat:

**myšlenka → strukturovaný text → verzovaný zdroj → automatická sazba → publikace → čtenář**

Právě toto propojení dává tématu „zpracování textu na počítači“ současný význam. Nejde jen o ovládání Wordu nebo znalost několika typografických pravidel. Jde o pochopení, **jak se text mění v dlouhodobě udržitelný, strojově zpracovatelný a kvalitně publikovatelný dokument**.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
