## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Proč Markdown vznikl**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Představme si, že chceme napsat krátký technický dokument. Potřebujeme nadpisy, seznam, odkaz, kus kódu a několik zvýrazněných slov.

V HTML bychom mohli napsat:

```html
<h1>Nadpis</h1>
<p>Toto je <strong>důležitý</strong> text.</p>
```

Je to přesné, ale při běžném psaní trochu těžkopádné.

Markdown vznikl s cílem, aby zdrojový text zůstal čitelný i bez převodu.

Stejnou strukturu můžeme zapsat:

```markdown
# Nadpis

Toto je **důležitý** text.
```

I člověk, který Markdown nikdy neviděl, většinou pochopí, co text znamená.

To je největší síla Markdownu:

**dokument je současně zdrojový kód i dobře čitelný prostý text.**

Markdown je proto velmi oblíbený v GitHub repozitářích, technické dokumentaci, poznámkových systémech, statických generátorech webů, vzdělávacích systémech, Jupyter prostředí, chatovacích aplikacích a AI pracovních postupech.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Základní syntaxe Markdownu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Markdown používá jednoduché znaky známé z běžné klávesnice.

### Nadpisy

```markdown
# Nadpis první úrovně
## Nadpis druhé úrovně
### Nadpis třetí úrovně
```

Počet znaků `#` vyjadřuje úroveň struktury. To je důležité: nadpis není jen větší tučný text. Nese **sémantickou informaci o hierarchii dokumentu**.

### Zvýraznění

```markdown
*kurzíva*
**tučně**
~~přeškrtnutí~~
```

Přeškrtnutí není součástí úplně každé varianty Markdownu, ale je běžné například v GitHub Flavored Markdown.

### Seznamy

```markdown
- první položka
- druhá položka
- třetí položka
```

Číslovaný seznam:

```markdown
1. první krok
2. druhý krok
3. třetí krok
```

### Odkazy

```markdown
[OpenAI](https://openai.com/)
```

### Obrázky

```markdown
![Alternativní text](images/schema.png)
```

Alternativní text je důležitý pro přístupnost a také jako náhradní informace, pokud se obraz nezobrazí.

### Citace

```markdown
> Toto je bloková citace.
```

### Kód

Inline kód:

```markdown
Použij příkaz `npm install`.
```

Víceřádkový blok:

````markdown
```python
print("Ahoj")
```
````

Právě kódové bloky jsou jedním z důvodů, proč je Markdown mimořádně vhodný pro informatické materiály.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Markdown není jeden dokonale jednotný standard**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Pojem Markdown se používá pro rodinu podobných syntaktických variant.

Původní Markdown vytvořil John Gruber s přispěním Aarona Swartze. Později vznikly přesněji specifikované varianty a rozšíření.

Důležitý je **CommonMark**, který se snaží přesně popsat základní syntaxi a odstranit některé nejasnosti původního Markdownu.

Velmi rozšířený je **GitHub Flavored Markdown — GFM**. Přidává například tabulky, task lists, strikethrough a automatické rozpoznávání některých odkazů.

Tabulka může vypadat:

```markdown
| Formát | Použití |
|---|---|
| Markdown | dokumentace |
| LaTeX | odborná sazba |
| PDF | distribuce |
```

Task list:

```markdown
- [x] napsat osnovu
- [ ] vytvořit obrázky
- [ ] exportovat PDF
```

Některé systémy podporují další rozšíření: matematiku, poznámky pod čarou, definice, atributy, diagramy nebo admonitions.

Proto musí autor vědět, **který Markdown renderer cílové prostředí používá**. Syntaxe, která funguje na GitHubu, nemusí fungovat úplně stejně v jiné aplikaci.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Markdown a oddělení obsahu od vzhledu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Markdown záměrně neřeší přesné typografické detaily.

Autor obvykle napíše:

```markdown
## Výsledky experimentu
```

a ne:

> použij 18bodové písmo, barvu #203050, horní mezeru 14 px a dolní 8 px.

Vzhled určuje až systém, který Markdown vykreslí.

Na webu může výslednou podobu řídit CSS. Při exportu do PDF ji může řídit šablona nebo LaTeX.

To přináší zásadní výhodu:

**jeden obsah lze publikovat v několika různých podobách.**

Například jeden soubor `lesson.md` může být převeden na HTML, PDF, DOCX, prezentaci nebo e-knihu.

Nástroj Pandoc je známý právě tím, že dokáže převádět velké množství značkovacích formátů.

Například:

```bash
pandoc lesson.md -o lesson.docx
```

nebo při odpovídající konfiguraci:

```bash
pandoc lesson.md -o lesson.pdf
```

Konkrétní výsledek závisí na instalovaných nástrojích, šablonách a použitých rozšířeních.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Markdown a Git: dokument jako verze zdrojového kódu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jedna z největších výhod Markdownu se projeví při spolupráci.

Protože jde o prostý text, Git dokáže přesně zobrazit změny.

Původní verze:

```markdown
HTTP používá port 80.
```

Nová verze:

```markdown
HTTP běžně používá port 80, HTTPS port 443.
```

Git ukáže změnu přímo na úrovni řádku.

U binárního kancelářského dokumentu je podobné porovnání mnohem obtížnější.

To umožňuje používat stejné postupy jako při vývoji software: commit, branch, pull request, code review a issue tracker.

Dokumentace se tak může stát součástí vývojového projektu. Tento přístup se často označuje jako **docs as code**.

Text vzniká podobným procesem jako program:

**zdroj → verze → kontrola → automatické sestavení → publikace**

To je důvod, proč Markdown používají téměř všechny moderní open-source projekty.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Markdown v moderním vzdělávání**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Markdown je velmi vhodný i pro výuku.

Student se soustředí na strukturu a obsah místo ručního formátování každého nadpisu.

Výukový materiál může obsahovat text, obrázky, tabulky, odkazy, matematiku, kód a interaktivní prvky podle cílového systému.

Markdown je základem například mnoha Jupyter Notebooků, statických webů, technických wiki, generátorů dokumentace a výukových platforem.

Některé systémy jej výrazně rozšiřují. LiaScript například používá Markdown jako základ, ale přidává kvízy, prezentace, interaktivní programování a další výukové prvky.

To ukazuje zajímavý princip: jednoduchý textový formát může být rozšířen do velmi komplexního publikačního systému, aniž by ztratil výhodu čitelného zdroje.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Metadata a front matter**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Samotný Markdown neobsahuje jednotný standard pro všechna metadata dokumentu.

Řada systémů používá takzvaný **front matter**.

Typický YAML front matter:

```yaml
---
title: Základy sítí
author: Jana Nováková
date: 2026-08-07
tags:
  - internet
  - sítě
---
```

Potom následuje vlastní Markdown.

Tyto informace může generátor použít pro název stránky, autora, navigaci, datum publikace, tagy nebo SEO metadata.

Je však důležité vědět, že YAML front matter není univerzální součást základního Markdownu. Jde o konvenci používanou konkrétními systémy, například některými statickými generátory webů.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.8

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Limity Markdownu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Markdown je silný právě svou jednoduchostí. Stejná vlastnost je ale také jeho omezením.

Není ideální pro přesnou vícesloupcovou sazbu, komplikované tabulky, detailní řízení typografie, složité matematické dokumenty bez rozšíření nebo přesnou kontrolu zalomení stránek.

Pokud autor začne Markdown obcházet množstvím vloženého HTML a speciálních rozšíření, může ztratit část původní jednoduchosti.

Proto je vhodné používat Markdown tam, kde je hlavním cílem obsah, struktura, přenositelnost, verzování a snadný převod.

Pro přesnou profesionální sazbu může být vhodnější LaTeX nebo DTP systém.

**Hlavní myšlenka druhé lekce:** Markdown je jednoduchý zdrojový formát, který odděluje významovou strukturu dokumentu od výsledného vzhledu. Díky tomu je výborný pro dokumentaci, vzdělávání, Git a automatizované publikační workflow.

---

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
