## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Hypertext a značkovací jazyk**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Když Tim Berners-Lee na počátku devadesátých let navrhoval World Wide Web, potřeboval jednoduchý způsob, jak popsat dokumenty a propojit je odkazy. Z této potřeby vznikl **HTML — HyperText Markup Language**, tedy hypertextový značkovací jazyk. Slovo *hypertext* připomíná jeho zásadní vlastnost: dokument nemusí být izolovanou stránkou, ale může odkazovat na jiné dokumenty, jejich části, obrázky, soubory nebo služby. Slovo *značkovací* zase říká, že význam částí dokumentu zapisujeme pomocí značek.

HTML není programovací jazyk v běžném smyslu. Nezadává algoritmus typu „opakuj tento příkaz desetkrát“, ale popisuje **strukturu a význam obsahu**. Nadpis označíme jako nadpis, odstavec jako odstavec, navigaci jako navigaci a tabulková data jako tabulku. Prohlížeč z těchto informací sestaví dokumentový strom a podle výchozích pravidel, připojených stylů a dalších zdrojů stránku vykreslí.

Historie HTML prošla verzemi HTML 2, HTML 4.01 a obdobím XHTML, které přeneslo do webového prostředí přísnější syntaktická pravidla XML. Pro současnou praxi je však důležitější jiná změna: HTML se dnes vyvíjí jako **Living Standard**, průběžně aktualizovaný standard. Označení „HTML5“ se stále běžně používá jako historická a praktická zkratka pro moderní HTML, není ale vhodné představovat HTML jako produkt, u něhož se po letech čeká na další velké číslo verze.

Také deklarace `<!doctype html>` už nefunguje jako přepínač mezi různými verzemi HTML. V moderním dokumentu je to krátká standardní deklarace, která mimo jiné zajistí, aby prohlížeč nepřešel do historického režimu kompatibility s velmi starými stránkami. V minulosti byly deklarace XHTML nebo HTML 4 mnohem delší, protože odkazovaly na konkrétní definice dokumentu. Pro dnešní stránku obvykle stačí:

```html
<!doctype html>
<html lang="cs">
  ...
</html>
```

Právě jednoduchost je jednou ze silných vlastností webu. Minimální dokument lze napsat v obyčejném textovém editoru a otevřít v prohlížeči bez speciálního kompilátoru. To však neznamená, že na kvalitě struktury nezáleží. Prohlížeč se s mnoha chybami pokusí vypořádat, ale jiný software — čtečka obrazovky, vyhledávač, překladač, archivní systém nebo automatický nástroj — potřebuje co nejjednoznačnější dokument.

***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Element, značka, atribut a vnořování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


V běžné řeči se často zaměňují pojmy **značka — tag** a **element**. Značka je syntaktická část zápisu, například `<p>` nebo `</p>`. Element zahrnuje celý významový prvek dokumentu, tedy počáteční značku, obsah a případnou koncovou značku:

```html
<p>Toto je jeden odstavec.</p>
```

Mnoho elementů je párových, ale některé mají v HTML pouze počáteční značku a žádný vnitřní obsah. Přesněji se označují jako **void elements**; patří mezi ně například `img`, `br`, `hr`, `meta`, `link` nebo `input`. Zápis `<br />` je v HTML tolerovaná syntaxe ovlivněná XHTML, lomítko však moderní HTML nepotřebuje a nevytváří z elementu „párový“ prvek.

Element může mít **atributy**, které doplňují jeho vlastnosti. U odkazu `href` určuje cíl, u obrázku `src` zdroj dat a `alt` textovou alternativu, u většiny elementů lze použít například `class` nebo `id`.

```html
<a class="download" href="materialy/lekce.pdf">Stáhnout lekci</a>
```

Atribut `class` může stejnou třídu přiřadit více prvkům a je proto základním spojovacím bodem mezi HTML a CSS. `id` má naopak v rámci dokumentu identifikovat jediný prvek; využívá se například pro odkazy na konkrétní část stránky, vztahy mezi formulářovými prvky a někdy pro JavaScript.

HTML elementy se **vnořují** do sebe a vytvářejí hierarchii. Ta není jen otázkou úhledného odsazení zdrojového kódu. Prohlížeč z ní vytváří strom DOM a pomocné technologie z ní odvozují strukturu dokumentu. Pokud se značky nesprávně překříží, prohlížeč se snaží zápis opravit podle standardních pravidel parseru, výsledný strom však nemusí odpovídat představě autora.

Komentáře mají tvar `<!-- komentář -->`. Jsou užitečné pro vysvětlení zdrojového kódu, ale nejsou bezpečným místem pro hesla, API klíče ani neveřejné poznámky. Komentář je součástí dokumentu staženého do prohlížeče a uživatel jej může zobrazit ve zdrojovém kódu.

Entity a znakové odkazy řeší situace, kdy chceme zapsat znak se speciálním významem nebo znak obtížně dostupný na klávesnici. Například `<` lze v textu zapsat jako `&lt;` a nezlomitelnou mezeru jako `&nbsp;`. V dokumentu používajícím UTF-8 však většinu běžných znaků, včetně české diakritiky, zapisujeme přímo. Není důvod převádět každé písmeno na číselný kód.

***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kostra moderního dokumentu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Běžná stránka začíná deklarací typu dokumentu, následuje kořenový element `html`, hlavička `head` a viditelné tělo `body`. Hlavička obsahuje metadata a odkazy na zdroje, nikoli hlavní obsah stránky.

```html
<!doctype html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Úvod do moderního HTML a CSS">
  <title>HTML a CSS — výukový web</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
</html>
```

Atribut `lang="cs"` pomáhá například čtečkám obrazovky a překladovým nástrojům správně určit jazyk. `meta charset="utf-8"` nastavuje znakové kódování. Meta prvek `viewport` je důležitý pro přirozené zobrazení na mobilních zařízeních. `title` vytváří název dokumentu, který se používá v kartě prohlížeče, historii, záložkách a často i ve výsledcích vyhledávání.

Starší materiály často přikládaly velký význam meta značce `keywords`. Současné vyhledávače ji pro běžné hodnocení stránky nepovažují za užitečný seznam „kouzelných slov“. Podstatnější je kvalitní obsah, srozumitelná struktura, správné nadpisy, užitečný titulek a popis, rychlost, dostupnost a důvěryhodnost stránky.

***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Validní kód není totéž co kvalitní web**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Validace** kontroluje, zda dokument odpovídá syntaktickým pravidlům standardu. Dokáže odhalit například nepovolený atribut, chybějící povinnou část nebo chybu ve vnoření. Validátor je proto výborný diagnostický nástroj, podobně jako překladač nebo linter v programování.

Validní stránka však může být nepřístupná, pomalá nebo obsahově špatná. Nadpisy mohou být použity jen kvůli velikosti písma, obrázky mohou mít nicneříkající alternativní text a formulář může být pro člověka ovládajícího počítač klávesnicí prakticky nepoužitelný. Naopak drobná validační chyba nemusí způsobit viditelnou katastrofu, protože HTML parser je navržen tak, aby se s mnoha chybami deterministicky vypořádal.

Smyslem validace proto není získat zelenou ikonku za každou cenu. Je to jedna vrstva kontroly vedle přístupnosti, použitelnosti, funkčnosti a výkonu. Kvalitní pracovní postup kombinuje validátor s nástroji prohlížeče, testováním na různých rozměrech obrazovky a skutečným používáním stránky.

# 2. Sémantická struktura, odkazy, média a formuláře

***
