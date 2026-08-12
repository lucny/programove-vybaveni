# Zpracování textu na počítači

## Modernizovaný výukový text pro studenty informačních technologií

> Textový dokument dnes nemusí vznikat jen ve Wordu. Může být prostým souborem v UTF-8, dokumentem v Markdownu uloženým v Git repozitáři, vědeckou prací sázenou v LaTeXu, webovou stránkou v HTML nebo finálním PDF určeným pro tisk. Všechny tyto podoby řeší stejnou otázku: jak oddělit obsah, strukturu, vzhled a způsob publikace tak, aby byl dokument čitelný, přenositelný a dlouhodobě použitelný.

Tento text modernizuje původní výukový materiál **Zpracování textu na počítači**. Zachovává jeho hlavní témata — textové editory, textové procesory, DTP, typografii, písma, strukturu dokumentu, styly a šablony, předtiskovou přípravu, PDF a elektronické knihy — ale rozšiřuje je o dvě technologie, které jsou dnes pro informatiku mimořádně důležité: **Markdown** a **LaTeX**.

Markdown ukazuje, jak lze obsah a strukturu dokumentu popsat jednoduchým čitelným textem, který se snadno verzovuje, publikuje na webu a převádí do dalších formátů. LaTeX naopak představuje profesionální typografický systém založený na zdrojovém textu a automatizované sazbě, který je mimořádně silný při práci s matematickými výrazy, rozsáhlými dokumenty, bibliografií a přesně definovanou strukturou.

Text je psán jako souvislý výklad. Jednotlivé kapitoly proto neslouží jen k zapamatování pojmů, ale vysvětlují, proč různé typy dokumentů a nástrojů existují, jak spolu souvisejí a kdy je vhodné který z nich použít. Díky tomu může materiál sloužit také jako podklad pro komentované prezentace a podcastové minipořady.

---

# 1. Textové dokumenty a nástroje pro práci s textem

## 1.1 Text jako data

Text, který člověk vidí na obrazovce, je pro počítač strukturovaná posloupnost dat. Každý znak musí být reprezentován číselnou hodnotou podle zvoleného znakového kódování, nejčastěji dnes UTF-8.

To znamená, že věta `Ahoj světe` není v souboru uložena jako obrázek písmen, ale jako sekvence bajtů, které software interpretuje jako konkrétní znaky Unicode.

U prostého textového souboru se ukládá především samotný text a řídicí znaky, například konec řádku. Neobsahuje automaticky informaci o tom, že nadpis má být modrý, odstavec zarovnaný do bloku nebo slovo zvýrazněno tučně.

To je důležité rozlišení:

**obsah textu není totéž co jeho vizuální formátování.**

Stejný text může být zobrazen v tisíci různých fontech a stále zůstává obsahově stejný. To je jedna z hlavních myšlenek moderní digitální sazby: je výhodné co nejvíce oddělit **co dokument říká** od **jak dokument vypadá**.

Prostý text má mnoho výhod: je snadno čitelný téměř na každém systému, lze jej vyhledávat, dobře se komprimuje, snadno se porovnává a verzovuje a je dlouhodobě velmi přenositelný. Proto se používá pro zdrojové kódy, konfigurační soubory, logy, Markdown, HTML, LaTeX i velké množství technické dokumentace.

---

## 1.2 Textový editor, textový procesor a DTP

Nástroje pro práci s textem se liší podle toho, zda chceme hlavně **psát obsah**, **formátovat dokument** nebo **přesně řídit sazbu stránky**.

**Textový editor** pracuje především s prostým textem. Patří sem například Visual Studio Code, Notepad, Vim, Nano, Emacs nebo Sublime Text. Je ideální pro programování, Markdown, HTML, LaTeX, konfigurační soubory a technické poznámky.

Textový editor obvykle neukládá „tučné písmo“ nebo „obrázek zarovnaný vlevo“ přímo jako vizuální stav. Pokud takovou strukturu potřebujeme, zapisujeme ji pomocí značek nebo syntaxe.

**Textový procesor** kombinuje obsah a formátování v interaktivním dokumentu. Typickými příklady jsou Microsoft Word, LibreOffice Writer, Google Docs nebo Apple Pages. Uživatel přímo vidí přibližný výsledný vzhled a používá nástroje pro styly, tabulky, obrázky, záhlaví, obsah, revize a komentáře. Tento přístup se označuje jako **WYSIWYG — What You See Is What You Get**.

**DTP — Desktop Publishing** je zaměřeno na profesionální sazbu a layout. Patří sem Adobe InDesign, Affinity Publisher, QuarkXPress nebo Scribus. DTP je vhodné pro časopisy, knihy, katalogy, letáky nebo rozsáhlé tiskové materiály, kde je důležitá přesná práce s typografií, obrázky, stránkovými mřížkami a tiskovou produkcí.

Vedle WYSIWYG existuje jiný přístup: dokument zapisujeme jako **zdrojový text** a výslednou podobu generuje sazební systém. Sem patří Markdown, LaTeX, HTML + CSS, AsciiDoc nebo reStructuredText. Tento způsob je mimořádně zajímavý pro informatiku, protože se podobá programování: dokument má zdrojový kód, syntaxi, strukturu, šablonu a proces převodu do výsledného formátu.

---

## 1.3 Formát souboru není totéž co aplikace

Dokument nevlastní program, ve kterém vznikl. Je uložen v určitém **formátu**.

Například Microsoft Word běžně pracuje s DOCX, ale umí otevřít nebo exportovat i další formáty. LibreOffice Writer používá jako nativní formát ODT, ale může pracovat také s DOCX.

To je důležité pro dlouhodobou kompatibilitu. Když dokument uložíme pouze v proprietárním pracovním formátu konkrétní aplikace, jsme závislí na tom, zda bude tento formát v budoucnu podporován.

Proto je vhodné rozlišovat:

- pracovní formát,
- výměnný formát,
- publikační formát,
- archivní formát.

Například DOCX může být pracovní dokument, PDF distribuční verze, PDF/A archivní varianta a TXT nebo Markdown dlouhodobě velmi přenositelný zdrojový text.

---

## 1.4 DOCX a ODT: dokument jako balíček strukturovaných dat

Soubor `.docx` není jeden neprůhledný binární blok. Technicky jde o ZIP archiv obsahující XML dokumenty a další soubory.

Uvnitř mohou být například textové části, informace o stylech, vztahy mezi objekty, obrázky a metadata.

Podobně fungují dokumenty standardu OpenDocument, například `.odt`.

To je dobrý příklad oddělení struktury a prezentace. Dokument neobsahuje jen výsledný obrázek stránky, ale popis jednotlivých prvků. Díky tomu lze text vyhledávat, měnit styly nebo generovat obsah.

Současně je ale formát kancelářského dokumentu velmi složitý. Proto není vhodný pro ruční editaci nebo verzování pomocí Git diffu. Dva DOCX soubory mohou být z pohledu uživatele téměř stejné, ale uvnitř se může změnit mnoho XML struktur.

Právě zde získávají prosté textové formáty typu Markdown nebo LaTeX velkou výhodu.

---

## 1.5 PDF: dokument jako stabilní výstup

PDF — Portable Document Format — vznikl proto, aby se dokument zobrazil a vytiskl konzistentně na různých zařízeních.

Na rozdíl od DOCX není hlavním cílem PDF snadná editace obsahu. PDF se snaží zachovat výslednou stránkovou kompozici: umístění textu, fonty, vektorovou grafiku, rastrové obrázky a rozměry stránky.

PDF může obsahovat skutečný text, nikoli jen obraz stránky. Proto lze v kvalitně vytvořeném PDF text vyhledávat, kopírovat nebo indexovat.

PDF může obsahovat také odkazy, formuláře, záložky, metadata, vložené fonty a digitální podpisy.

Pro tisk existují specializované standardy například řady PDF/X. Pro archivaci dokumentů se používají profily PDF/A.

PDF je proto velmi vhodný **výstupní formát**, ale často není ideální jako zdroj, ze kterého chceme pokračovat v editaci.

---

# 2. Markdown: dokument jako jednoduchý čitelný zdrojový text

## 2.1 Proč Markdown vznikl

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

---

## 2.2 Základní syntaxe Markdownu

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

---

## 2.3 Markdown není jeden dokonale jednotný standard

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

---

## 2.4 Markdown a oddělení obsahu od vzhledu

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

---

## 2.5 Markdown a Git: dokument jako verze zdrojového kódu

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

---

## 2.6 Markdown v moderním vzdělávání

Markdown je velmi vhodný i pro výuku.

Student se soustředí na strukturu a obsah místo ručního formátování každého nadpisu.

Výukový materiál může obsahovat text, obrázky, tabulky, odkazy, matematiku, kód a interaktivní prvky podle cílového systému.

Markdown je základem například mnoha Jupyter Notebooků, statických webů, technických wiki, generátorů dokumentace a výukových platforem.

Některé systémy jej výrazně rozšiřují. LiaScript například používá Markdown jako základ, ale přidává kvízy, prezentace, interaktivní programování a další výukové prvky.

To ukazuje zajímavý princip: jednoduchý textový formát může být rozšířen do velmi komplexního publikačního systému, aniž by ztratil výhodu čitelného zdroje.

---

## 2.7 Metadata a front matter

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

---

## 2.8 Limity Markdownu

Markdown je silný právě svou jednoduchostí. Stejná vlastnost je ale také jeho omezením.

Není ideální pro přesnou vícesloupcovou sazbu, komplikované tabulky, detailní řízení typografie, složité matematické dokumenty bez rozšíření nebo přesnou kontrolu zalomení stránek.

Pokud autor začne Markdown obcházet množstvím vloženého HTML a speciálních rozšíření, může ztratit část původní jednoduchosti.

Proto je vhodné používat Markdown tam, kde je hlavním cílem obsah, struktura, přenositelnost, verzování a snadný převod.

Pro přesnou profesionální sazbu může být vhodnější LaTeX nebo DTP systém.

**Hlavní myšlenka druhé lekce:** Markdown je jednoduchý zdrojový formát, který odděluje významovou strukturu dokumentu od výsledného vzhledu. Díky tomu je výborný pro dokumentaci, vzdělávání, Git a automatizované publikační workflow.

---

# 3. Typografie a písmo

## 3.1 Typografie není zdobení textu

Typografie není umění vybrat hezký font. Je to disciplína, která organizuje text tak, aby byl čitelný, srozumitelný, hierarchický a vizuálně vyvážený.

Dobrá typografie často působí nenápadně. Čtenář se soustředí na obsah a nemusí bojovat s příliš dlouhými řádky, chaotickými nadpisy nebo nečitelným písmem.

Typografie řeší například volbu písma, velikost, řádkování, délku řádku, mezery, odstavce, hierarchii a sazbu stránky.

V českém textu řeší také správné používání uvozovek, pomlček, spojovníků, nezlomitelných mezer, zkratek a jednotek.

Typografické pravidlo má často praktický důvod. Například jednopísmenná předložka `v` by neměla zůstat sama na konci řádku, protože vizuálně narušuje čtení. Proto se mezi ni a následující slovo používá **nezlomitelná mezera**.

---

## 3.2 Zrcadlo sazby, okraje a délka řádku

Text na stránce potřebuje prostor.

**Zrcadlo sazby** je oblast stránky určená pro hlavní obsah. Kolem ní jsou okraje.

Příliš malé okraje vytvářejí pocit stísněnosti. Příliš velké mohou zbytečně omezit textovou plochu.

Velmi důležitá je **délka řádku**.

Pokud je řádek příliš dlouhý, oko obtížně hledá začátek následujícího řádku. Pokud je příliš krátký, čtenář musí často přeskakovat na nový řádek a rytmus čtení se rozpadá.

Optimální hodnota závisí na písmu, velikosti, médiu, jazyku a typu textu. Není proto vhodné používat jedno magické číslo.

V odborné sazbě se délka řádku často posuzuje podle počtu znaků a vlastností konkrétního písma.

---

## 3.3 Řádkování, odstavce, vdovy a sirotci

**Leading — řádkový proklad** je vzdálenost mezi řádky textu.

Příliš malé řádkování způsobuje, že se řádky vizuálně slévají. Příliš velké rozbíjí soudržnost odstavce.

Často se používá hodnota kolem 120 až 150 % velikosti písma, ale konkrétní vhodná hodnota závisí na písmu, šířce sloupce a účelu dokumentu.

Odstavce lze oddělovat například odsazením prvního řádku nebo vertikální mezerou. Není vhodné oba způsoby bezmyšlenkovitě kombinovat.

V sazbě se také řeší **vdovy a sirotci**. Pojmy se mezi typografickými tradicemi někdy používají mírně odlišně, ale obecně jde o nežádoucí osamocené řádky odstavce na začátku nebo konci stránky či sloupce.

Sazební systémy se snaží takové situace automaticky omezovat.

---

## 3.4 Kerning, tracking a mezislovní mezery

Vzdálenost mezi znaky není mechanicky stejná.

**Kerning** upravuje mezeru mezi konkrétní dvojicí znaků. Například kombinace `AV` potřebuje jiné optické nastavení než `HH`.

Bez kerningu by mezi šikmými tvary A a V vznikla vizuálně příliš velká mezera.

**Tracking** mění celkové rozestupy znaků v delším úseku textu. Je užitečný například u některých verzálek nebo grafických nadpisů, ale v běžném odstavcovém textu se používá opatrně.

Při zarovnání do bloku se může měnit i **mezislovní mezera**.

Pokud má řádek málo možností zalomení, mohou vzniknout nápadné mezery, které se opticky spojují do vertikálních řek.

Kvalitní sazební algoritmus proto kombinuje dělení slov, úpravu mezislovních mezer a případně mikrotypografické korekce.

Právě v této oblasti je LaTeX tradičně velmi silný.

---

## 3.5 Patkové, bezpatkové a monospace písmo

Písma lze dělit podle několika vlastností.

**Serif** — patková písma mají na zakončení tahů drobné patky. Příklady: Garamond, Georgia nebo Times.

Často se používají pro dlouhé tiskové texty, ale tvrzení „serif je vždy pro tisk a sans-serif vždy pro obrazovku“ je dnes příliš jednoduché. Moderní displeje mají vysoké rozlišení a kvalitní patkové fonty jsou na obrazovce běžně velmi čitelné.

**Sans-serif** — bezpatková písma mají čistší zakončení. Příklady: Helvetica, Arial, Inter nebo Roboto. Jsou běžná v rozhraních, webovém designu, titulcích a moderní sazbě.

**Monospace** — každý znak má stejnou šířku. Příklady: Consolas, JetBrains Mono nebo Courier. Používají se hlavně pro programový kód, terminál a data, kde je důležité přesné sloupcové zarovnání.

**Display a decorative** — dekorativní písma jsou určena hlavně pro krátké nadpisy a výrazné grafické použití. Pro dlouhý text mohou být únavná.

---

## 3.6 Font, rodina, řez a proměnné fonty

V běžné řeči se slovo font a písmo používá téměř zaměnitelně, typograficky je ale užitečné rozlišit rodinu a konkrétní řez.

Rodina může být například `Roboto` a řezy Regular, Italic, Bold nebo Bold Italic.

Moderní technologie přidává **variable fonts**.

Jediný fontový soubor může obsahovat plynule měnitelné osy, například weight, width nebo optical size.

Místo samostatných souborů Regular, Medium a Bold může aplikace použít hodnoty na kontinuální škále.

To je užitečné na webu i v profesionálním designu.

Nejčastější moderní formáty jsou OpenType, TrueType a WOFF2 pro web.

Fonty jsou softwarem podobné datové soubory a podléhají licencím. To, že máme font nainstalovaný v počítači, neznamená automaticky, že jej smíme vložit do komerční aplikace nebo distribuovat jako součást webu.

---

## 3.7 Typografická pravidla českého textu

Český text má vlastní konvence.

Typické české uvozovky jsou:

`„text“`

nikoli automaticky anglické:

`"text"`

Spojovník `-` spojuje části slov:

`česko-slovenský`

Pomlčka `–` odděluje větné části nebo rozsahy:

`Praha – Brno`

`2020–2026`

Nezlomitelná mezera se používá například mezi číslem a jednotkou `10 km` nebo u jednopísmenných předložek `v Praze`, aby se nevhodně nerozdělily přes konec řádku.

`20 %` znamená dvacet procent. Zápis `20% roztok` může být v české typografické praxi použit bez mezery, pokud celek funguje jako přídavné určení „dvacetiprocentní“.

Typický číselný zápis data je:

`7. 8. 2026`

s mezerami po tečkách.

Důležité je především používat jeden konzistentní styl v celém dokumentu.

---

# 4. Struktura dokumentu, styly a automatizace

## 4.1 Dokument má logickou strukturu

Dobře vytvořený dokument není jen série vizuálně formátovaných odstavců.

Má logickou hierarchii:

**dokument → kapitola → podkapitola → odstavec → věta**

K tomu mohou přistoupit další prvky: seznamy, tabulky, obrázky, popisky, poznámky pod čarou nebo citace.

Tato struktura má význam pro čtenáře, automatický obsah, přístupnost, převod do jiných formátů a vyhledávání.

Proto je chybou vytvořit nadpis tak, že pouze vezmeme běžný odstavec a ručně mu nastavíme větší písmo.

Vizuálně může vypadat správně, ale systém neví, že jde o skutečný nadpis.

Lepší je použít sémantický styl `Nadpis 1` nebo v Markdownu `# Nadpis`.

---

## 4.2 Styly místo ručního formátování

**Styl** je pojmenovaná sada vlastností.

Například styl Nadpis 2 může definovat font, velikost, řez, barvu, mezery a číslování.

Když chceme změnit vzhled všech podnadpisů, upravíme styl jednou.

To je mnohem robustnější než označit čtyřicet nadpisů a ručně měnit jejich velikost.

Styly poskytují konzistenci, rychlou globální změnu, podporu automatické struktury a lepší přístupnost.

Stejný princip najdeme v CSS na webu.

HTML říká:

```html
<h2>Výsledky</h2>
```

CSS určí, jak bude `h2` vypadat.

Markdown jde ještě dál: autor často zapisuje pouze strukturu a celý vzhled dodá až šablona.

---

## 4.3 Šablony

**Šablona** definuje základní strukturu a styly dokumentu.

Může obsahovat logo, záhlaví, zápatí, firemní barvy, styly nadpisů, vzor titulní stránky a standardní části dokumentu.

Šablony jsou velmi důležité ve firmách i školách.

Místo toho, aby každý autor vytvářel dokument od začátku, dostane definovaný systém.

Tím se zvyšuje vizuální konzistence, rychlost, správnost a použitelnost.

Stejnou myšlenku využívají také Markdown a LaTeX workflow.

Obsah může být uložen samostatně a jedna šablona z něj vytvoří školní materiál, jiná web a další PDF.

---

## 4.4 Automatický obsah, odkazy a křížové reference

Když dokument používá správné styly nadpisů, lze automaticky vytvořit **obsah**.

Není nutné ručně psát `Kapitola 1 .... 5`.

Systém si strukturu přečte a čísla stran doplní.

Stejně lze automatizovat seznam obrázků, seznam tabulek, číslování rovnic a křížové odkazy.

Například text:

> Viz obrázek 7 na straně 14.

je nebezpečné napsat ručně. Po vložení nového obrázku se může změnit číslování i strana.

Lepší je použít automatickou referenci na objekt.

LaTeX je v této oblasti mimořádně silný, protože používá značky a reference:

```latex
\label{fig:network}
```

a:

```latex
\ref{fig:network}
```

Při překladu se čísla dopočítají automaticky.

---

## 4.5 Revize, komentáře a spolupráce

Textové dokumenty často vznikají ve více lidech.

Textové procesory proto podporují komentáře, sledování změn, návrhy a historii verzí.

V cloudových editorech může více lidí pracovat současně.

Git používá jiný model spolupráce.

Autor provede změnu v textovém souboru, vytvoří commit a další člověk může přesně zkontrolovat diff.

Oba modely mají své výhody.

Word nebo Google Docs jsou velmi vhodné pro běžnou kancelářskou spolupráci a komentování.

Git + Markdown nebo LaTeX jsou výhodné při technické dokumentaci, kde je důležitá přesná historie, automatizace a provázání s vývojem.

---

## 4.6 Hromadná korespondence a generování dokumentů

Někdy nechceme vytvořit jeden dokument, ale stovky podobných dokumentů s různými daty.

Typickým příkladem jsou certifikáty, dopisy, jmenovky, faktury nebo pozvánky.

Textový procesor může použít **mail merge — hromadnou korespondenci**.

Máme šablonu:

> Vážený/á {{jmeno}},

a tabulku dat.

Program vytvoří samostatné personalizované dokumenty.

Moderní automatizace používá stejný princip v programování.

Markdown nebo LaTeX dokument může být vygenerován ze šablony pomocí Pythonu, JavaScriptu, Jinja2 nebo jiného nástroje.

Zpracování textu se tak propojuje s databázemi, automatizací a generováním dokumentů.

---

## 4.7 AI při práci s dokumenty

Generativní AI může pomáhat při návrhu struktury, korektuře, shrnutí, změně stylu, extrakci informací, převodu mezi formáty, návrhu tabulek a generování Markdownu nebo LaTeXu.

Je ale důležité rozlišit:

**jazykovou transformaci** a **ověření faktů**.

AI může velmi přesvědčivě přeformulovat i chybnou informaci.

U dokumentu s odborným obsahem proto zůstává nutná kontrola zdrojů, dat, citací a terminologie.

AI také nemusí spolehlivě zachovat komplikované formátování kancelářského dokumentu. Bezpečnější může být nechat model vytvořit strukturovaná data a vlastní dokument sestavit deterministickým skriptem.

To je stejný princip jako při automatizované tvorbě výukových materiálů:

**AI navrhne obsah → šablona určí strukturu → nástroj vytvoří dokument → validátor zkontroluje výsledek.**

---

# 5. LaTeX: programovatelná profesionální sazba

## 5.1 TeX a LaTeX: proč vznikly

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

---

## 5.2 První dokument v LaTeXu

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

---

## 5.3 Příkazy a prostředí

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

---

## 5.4 Matematika: hlavní doména LaTeXu

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

---

## 5.5 Dokumentové třídy a balíčky

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

---

## 5.6 Obrázky, tabulky a floating objects

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

---

## 5.7 Křížové odkazy a automatické číslování

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

---

## 5.8 Bibliografie: BibTeX a biblatex

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

---

## 5.9 LaTeX, Git a reprodukovatelné dokumenty

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

---

## 5.10 Markdown versus LaTeX

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

Právě toto propojení dává tématu „zpracování textu na počítači“ současný význam. Nejde jen o ovládání Wordu nebo znalost několika typografických pravidel. Jde o pochopení, **jak se text mění v dlouhodobě udržitelný, strojově zpracovatelný a kvalitně publikovatelný dokument**.
