## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**TeX a LaTeX: proč vznikly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
