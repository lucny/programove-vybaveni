# HTML a CSS

> Webová stránka není obrázek nakreslený v prohlížeči. Je to strukturovaný dokument, jehož význam popisuje HTML a jehož podobu, rozložení a přizpůsobení různým zařízením řídí CSS. Kvalitní web proto nevzniká hromaděním značek a vlastností, ale promyšleným oddělením obsahu, struktury a prezentace.

# 1. HTML: dokument, kterému rozumí člověk i stroj

## 1.1 Hypertext a značkovací jazyk

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

## 1.2 Element, značka, atribut a vnořování

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

## 1.3 Kostra moderního dokumentu

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

## 1.4 Validní kód není totéž co kvalitní web

**Validace** kontroluje, zda dokument odpovídá syntaktickým pravidlům standardu. Dokáže odhalit například nepovolený atribut, chybějící povinnou část nebo chybu ve vnoření. Validátor je proto výborný diagnostický nástroj, podobně jako překladač nebo linter v programování.

Validní stránka však může být nepřístupná, pomalá nebo obsahově špatná. Nadpisy mohou být použity jen kvůli velikosti písma, obrázky mohou mít nicneříkající alternativní text a formulář může být pro člověka ovládajícího počítač klávesnicí prakticky nepoužitelný. Naopak drobná validační chyba nemusí způsobit viditelnou katastrofu, protože HTML parser je navržen tak, aby se s mnoha chybami deterministicky vypořádal.

Smyslem validace proto není získat zelenou ikonku za každou cenu. Je to jedna vrstva kontroly vedle přístupnosti, použitelnosti, funkčnosti a výkonu. Kvalitní pracovní postup kombinuje validátor s nástroji prohlížeče, testováním na různých rozměrech obrazovky a skutečným používáním stránky.

# 2. Sémantická struktura, odkazy, média a formuláře

## 2.1 Nadpis není „větší text“

HTML dává obsahu význam. Nadpisy `h1` až `h6` vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma. Vzhled nadpisu lze změnit CSS, jeho význam však zůstává. Podobně `strong` označuje silnou důležitost, `em` zdůraznění, `blockquote` delší citaci a `code` úsek počítačového kódu.

To je podstata **sémantického HTML**: vybrat element podle toho, co obsah znamená, nikoli podle toho, jak chceme, aby vypadal. Když autor použije `div` úplně na všechno, vizuálně může stránku pomocí CSS napodobit. Ztrácí však informaci, že určitá oblast je navigace, hlavní obsah nebo samostatný článek.

Moderní HTML proto nabízí elementy jako `header`, `nav`, `main`, `article`, `section`, `aside` a `footer`. Nejsou to hotové grafické bloky. Prohlížeč jim nepřidělí „profesionální layout“ automaticky. Jsou to významové kontejnery.

Představme si školní web. `header` může obsahovat název školy a hlavní navigaci, `main` vlastní obsah stránky, `article` jednu samostatně publikovatelnou aktualitu, `aside` související informace a `footer` kontakty či právní údaje. Když stejný dokument čte čtečka obrazovky, sémantická struktura umožní rychleji přeskakovat mezi významovými oblastmi.

Element `div` tím nezmizel. Stále je vhodným neutrálním kontejnerem tam, kde žádný přesnější význam neexistuje. Chybou není použít `div`; chybou je používat jej automaticky místo elementu, který skutečný význam už popisuje.

## 2.2 Odkaz vytváří web

Element `a` je jedním z prvků, které odlišily web od běžného elektronického dokumentu. Jeho atribut `href` může obsahovat absolutní URL, relativní cestu nebo fragment odkazující na element s konkrétním `id`.

```html
<a href="https://example.org/dokumentace">Externí dokumentace</a>
<a href="galerie.html">Galerie v tomto webu</a>
<a href="#kontakt">Přejít na kontakt</a>
```

Relativní odkazy jsou praktické uvnitř jednoho webu, protože projekt lze přesunout na jinou doménu nebo do jiné složky bez přepisování všech adres. Je však nutné rozumět, vůči čemu se cesta vyhodnocuje. Zápis `../images/logo.svg` znamená „o adresář výše a potom do složky images“.

Text odkazu by měl dávat smysl i bez okolní věty. „Podrobný ceník“ je informativnější než pět odkazů pojmenovaných „zde“. Otevření odkazu do nové karty pomocí `target="_blank"` není vhodné používat automaticky. Uživatel obvykle rozhoduje, zda chce novou kartu, a neočekávané otevření nového kontextu může být matoucí. Pokud pro ně existuje důvod, má rozhraní chování srozumitelně naznačit.

Navigace není jen grafický pruh s tlačítky. Je to informační architektura webu. Na menším webu může stačit hlavní navigace a několik kontextových odkazů, rozsáhlejší služba využije drobečkovou navigaci, vyhledávání a promyšlenou hierarchii kategorií. Původní metafora „drobečků“ z pohádky zůstává výstižná: breadcrumb ukazuje cestu v hierarchii a pomáhá uživateli pochopit, kde se nachází.

## 2.3 Obrázek není jen soubor vedle HTML

Obrázek vkládáme elementem `img`, ale kvalitní zápis řeší více než samotnou cestu k souboru.

```html
<img
  src="images/laborator.jpg"
  alt="Studenti měřící síťový provoz v laboratoři"
  width="1200"
  height="800"
  loading="lazy">
```

`alt` je **textová alternativa**, nikoli titulek pro najetí myší. Má předat význam obrázku člověku, který jej nevidí nebo jej z nějakého důvodu nenačetl. U dekorativního obrázku, který nenese žádnou informaci, je naopak často správné `alt=""`, aby jej čtečka obrazovky zbytečně neoznamovala.

Atributy `width` a `height` mají i v responzivním webu praktický význam. Prohlížeč z nich předem zná poměr stran a může rezervovat místo, takže se stránka při načtení méně „rozskáče“. CSS může výslednou šířku stále přizpůsobit kontejneru například pravidlem `max-width: 100%; height: auto;`.

Pro různá zařízení není vždy rozumné posílat tentýž obrovský obrázek. HTML proto podporuje responzivní obrázky pomocí `srcset`, `sizes` a elementu `picture`. Prohlížeč může vybrat vhodný soubor podle hustoty pixelů, velikosti zobrazení a podporovaného formátu. Moderní web tak může nabídnout například AVIF nebo WebP a zároveň ponechat vhodnou alternativu.

Elementy `audio` a `video` umožňují přehrávat multimédia přímo bez historických pluginů typu Flash. Je však nutné myslet na titulky, ovládání klávesnicí, případné přepisy a na datový objem. To, že prohlížeč video umí přehrát, ještě neznamená, že je správné automaticky stáhnout desítky megabajtů hned po otevření stránky.

`iframe` se stále používá pro vložení samostatného dokumentu nebo externí aplikace, například mapy či videopřehrávače. Není však náhradou za layout stránky, jak tomu bývalo u historických rámů. Vložený dokument má vlastní kontext, bezpečnostní omezení a často také dopady na výkon a soukromí.

## 2.4 Tabulka patří datům, ne layoutu

Tabulky bývaly v počátcích webdesignu zneužívány k rozmístění celé stránky. Dnes k tomu máme CSS Grid a Flexbox. Element `table` proto vracíme k jeho skutečnému účelu: **tabulkovým datům**.

```html
<table>
  <caption>Výsledky měření latence</caption>
  <thead>
    <tr><th scope="col">Síť</th><th scope="col">Latence</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">LAN</th><td>1 ms</td></tr>
    <tr><th scope="row">Mobilní síť</th><td>28 ms</td></tr>
  </tbody>
</table>
```

`caption`, záhlaví `th` a vhodně určený vztah řádků a sloupců pomáhají nejen vizuální orientaci, ale i přístupnosti. U velmi široké tabulky je navíc potřeba promyslet, jak se bude chovat na telefonu; někdy je vhodný horizontální posuv, jindy změna prezentace dat.

## 2.5 Formulář je rozhovor mezi člověkem a systémem

Formuláře jsou místem, kde uživatel přestává být pouhým čtenářem. Zadává jméno, vybírá datum, vyhledává, přihlašuje se nebo odesílá soubor. HTML nabízí různé typy vstupů a část základní validace už přímo v prohlížeči.

```html
<form action="/registrace" method="post">
  <label for="email">E-mail</label>
  <input id="email" name="email" type="email" autocomplete="email" required>
  <button type="submit">Registrovat</button>
</form>
```

Důležitá je vazba `label` na konkrétní ovládací prvek. Placeholder není plnohodnotná náhrada popisku: po začátku psaní mizí, mívá horší kontrast a uživatel může zapomenout, co pole znamenalo. Atribut `name` určuje jméno hodnoty při odeslání, `type` může prohlížeči napovědět vhodnou klávesnici a základní kontrolu a `autocomplete` umožní využít bezpečně uložené údaje uživatele.

Klientská validace zlepšuje pohodlí, ale nesmí být jedinou bezpečnostní kontrolou. HTML formulář lze obejít a požadavek lze odeslat jiným programem. Serverová aplikace proto musí všechna důležitá data ověřit znovu. Tato hranice mezi HTML formulářem a backendem bude klíčová v tématu webových aplikací.

# 3. CSS: kaskáda, selektory a box model

## 3.1 CSS není „HTML s barvami“

**CSS — Cascading Style Sheets** popisuje prezentaci strukturovaného dokumentu. Oddělení HTML a CSS umožňuje, aby stejný obsah získal jiný vzhled na monitoru, telefonu nebo při tisku a aby společná pravidla řídila stovky stránek najednou.

Historická představa „CSS1, CSS2, CSS3 a jednou CSS4“ už neodpovídá způsobu, jakým se standard vyvíjí. CSS je rozděleno do mnoha modulů — například barvy, selektory, Grid, Flexbox nebo média — které postupují vlastním tempem. Označení „CSS3“ je stále srozumitelná historická zkratka, ale není názvem jediné současné verze celého jazyka.

Nejčastější a nejlépe udržovatelný způsob připojení stylů je externí soubor:

```html
<link rel="stylesheet" href="styles.css">
```

Interní pravidla v elementu `style` mají smysl například v malém samostatném dokumentu. Inline styl v atributu `style` je někdy praktický při dynamickém generování nebo v omezeném prostředí, ale pro běžnou údržbu se rychle stává překážkou, protože míchá strukturu s prezentací.

CSS pravidlo obsahuje selektor a blok deklarací:

```css
.card {
  padding: 1.25rem;
  border: 1px solid #cbd5e1;
  border-radius: 0.75rem;
}
```

Selektor říká „koho vyber“, deklarace „co změň“. Tím však vysvětlení nekončí, protože na jeden element může současně mířit mnoho pravidel. Právě jejich vyhodnocení dává CSS slovo **kaskádové**.

## 3.2 Jak kaskáda rozhodne spor

Představme si nadpis, na který se vztahuje obecné pravidlo pro všechny `h2`, pravidlo třídy `.warning`, styl v konkrétním komponentu a uživatelské nastavení. Které vyhraje? Není správné říci pouze „poslední zapsané pravidlo“ nebo „ID vždy přebije třídu“.

Kaskáda zohledňuje původ pravidla, důležitost, případné **cascade layers**, specificitu selektoru, rozsah a nakonec pořadí. Teprve když předchozí kritéria nerozhodnou, získá přednost pozdější stejně silné pravidlo. Pro běžnou práci proto stačí rozumět několika principům: nepoužívat zbytečně přehnaně specifické selektory, organizovat komponenty pomocí tříd a s `!important` zacházet jako s výjimečným nástrojem, nikoli univerzální opravou.

**Dědičnost** je jiný mechanismus. Některé vlastnosti, například barva textu nebo rodina písma, se přirozeně dědí z rodiče na potomky. Jiné, například `margin` nebo `border`, se běžně nedědí. Když tedy nastavíme `font-family` na `body`, většina textových potomků ji převezme. Když nastavíme rámeček na `body`, každý odstavec vlastní rámeček nedostane.

Moderní CSS přidává nástroje, které velké projekty zpřehledňují. **Custom properties** fungují jako kaskádové proměnné:

```css
:root {
  --space: 1rem;
  --surface: #f8fafc;
}

.card {
  padding: var(--space);
  background: var(--surface);
}
```

Jejich výhodou není jen kratší zápis. Protože podléhají kaskádě, lze například změnit hodnoty v tmavém režimu nebo uvnitř konkrétní komponenty bez přepisování každé jednotlivé deklarace.

## 3.3 Selektory jako dotaz na dokument

Základní selektory vybírají element, třídu nebo identifikátor: `p`, `.note`, `#menu`. Kombinátory popisují vztahy v hierarchii, například `.article p` vybere odstavce uvnitř článku a `.menu > li` pouze položky, které jsou přímými potomky menu.

Atributové selektory umožňují pracovat s vlastnostmi HTML, například `input[type="email"]`. **Pseudotřídy** popisují stav nebo vztah, například `:hover`, `:focus-visible`, `:checked`, `:first-child` nebo moderní `:has()`. **Pseudoelementy** jako `::before`, `::after` nebo `::first-line` reprezentují část elementu, kterou není nutné přidávat jako další HTML uzel.

Zvlášť důležitý je `:focus-visible`. Web nesmí spoléhat pouze na myš. Člověk, který používá klávesnici, potřebuje vidět, který ovládací prvek má právě fokus. „Designové“ odstranění obrysu bez rovnocenné náhrady je typický příklad úpravy, která stránku vizuálně zjednoduší a současně zhorší její použitelnost.

## 3.4 Každý prvek je krabice

Prohlížeč musí každý viditelný element umístit do prostoru. Základní mentální model tvoří **CSS box model**:

**content → padding → border → margin**

Obsah je vnitřní plocha, `padding` vytváří prostor mezi obsahem a rámečkem, `border` je okraj a `margin` vnější odstup od okolí. Výchozí způsob výpočtu rozměrů může začátečníka překvapit. Při `box-sizing: content-box` se zadaná `width` vztahuje pouze k obsahu a padding s borderem se přičtou navíc. Proto se v mnoha projektech používá:

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

Potom se `width` snáze chápe jako výsledná šířka boxu včetně paddingu a borderu.

Další překvapení představuje **margin collapsing** u některých bloků v normálním toku. Dva svislé marginy se nemusí jednoduše sečíst. I to připomíná, že CSS není grafický editor s absolutními souřadnicemi; je to systém pravidel pro rozvržení dokumentu.

## 3.5 Jednotky nejsou soutěž „pixely proti procentům“

Starší poučka někdy říká, že responzivní web musí používat relativní jednotky a pixely jsou špatně. Tak jednoduché to není. CSS `px` je **referenční pixel**, nikoli vždy jeden fyzický bod displeje, a pro rámeček o tloušťce 1 px je zcela rozumný. Pro typografii, mezery a pružný layout však často lépe fungují jednotky odvozené od kontextu.

`rem` se vztahuje k velikosti písma kořenového elementu, `em` k aktuálnímu kontextu, `%` k vlastnosti a rodičovskému rozměru podle konkrétního pravidla, `vw` a `vh` k viewportu. Moderní viewportové jednotky jako `dvh` pomáhají řešit dynamickou výšku mobilních prohlížečů. Funkce `min()`, `max()` a `clamp()` dovolují vytvářet plynule se měnící hodnoty s rozumnými hranicemi.

Například nadpis může růst podle šířky obrazovky, ale nikdy nebude příliš malý ani absurdně velký:

```css
h1 {
  font-size: clamp(2rem, 5vw, 4.5rem);
}
```

# 4. Layout: od normálního toku k Flexboxu a Gridu

## 4.1 Normální tok je výchozí, ne překážka

Než použijeme jakýkoli layout systém, prohlížeč skládá dokument podle **normal flow**. Blokové prvky typicky postupují pod sebou, inline obsah uvnitř řádků. Tento přirozený tok je překvapivě schopný a má jednu velkou výhodu: když se text prodlouží nebo se změní šířka okna, obsah se automaticky přeskupí.

Historické weby často layout simulovaly tabulkami, plovoucími prvky nebo rámy. Tyto techniky řešily skutečné problémy své doby, ale dnešní CSS nabízí nástroje vytvořené přímo pro rozložení. `float` si zachoval vhodný účel například pro obtékání obrázku textem, nemusí však nést celou strukturu webu.

Pozicování pomocí `position: relative`, `absolute`, `fixed` a `sticky` je užitečné pro konkrétní vztahy: odznak v rohu karty, přichycenou hlavičku nebo překrytí vrstev. Není ale dobrým výchozím způsobem, jak ručně rozmístit každou část stránky na pevné souřadnice. Takový návrh se rozpadne ve chvíli, kdy se změní obsah, font nebo rozměr zařízení.

## 4.2 Flexbox: když řešíme hlavně jeden směr

**Flexbox** je vhodný tam, kde prvky organizujeme především v jednom směru — do řádku nebo sloupce. Typickým příkladem je navigace, sada tlačítek, řada karet nebo zarovnání ikony s textem.

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
```

Flex kontejner řídí hlavní a příčnou osu. Vlastnosti jako `justify-content`, `align-items`, `gap`, `flex-grow`, `flex-shrink` a `flex-basis` dovolují rozdělovat volný prostor bez ručního počítání šířek.

Představme si řádek tří tlačítek. Ve starém layoutu by autor mohl každému nastavit procentuální šířku, připočítat margin a řešit zaokrouhlování. Flexbox dovolí říci, jak se mají prvky dělit o prostor, a prohlížeč výpočet provede podle skutečných rozměrů obsahu.

## 4.3 Grid: vztahy v řádcích i sloupcích

**CSS Grid** řeší dvourozměrné rozložení. Umožňuje definovat řádky a sloupce, mezery i oblasti a potom do nich umisťovat prvky. Hodí se pro galerii, dashboard nebo hlavní kostru stránky.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: 1rem;
}
```

Toto pravidlo je důležitější než katalog desítek vlastností: vytvoří tolik sloupců, kolik se jich rozumně vejde, přičemž karta nebude užší než 16 rem a dostupný prostor se rozdělí mezi sloupce. Responzivita tak může vzniknout už ze samotného layoutu, bez série přesně nastavených breakpointů.

Flexbox a Grid nejsou soupeři. Grid může řídit velké oblasti stránky a Flexbox zarovnání prvků uvnitř jedné karty. Dobrý layout kombinuje nástroje podle charakteru problému.

## 4.4 Responzivní design není sada tří obrazovek

Původní responzivní webdesign se často vysvětloval jako tři verze: mobil, tablet a desktop. Dnes je užitečnější myslet na **plynulé kontinuum velikostí**. Okno může mít libovolnou šířku, uživatel může zvětšit text, otevřít postranní panel nebo použít skládací displej.

Základ tvoří pružné rozměry, vhodný layout a obrázky, které se umějí přizpůsobit. **Media queries** potom zasahují tam, kde se při určité podmínce skutečně mění struktura nebo způsob ovládání.

```css
@media (width >= 60rem) {
  .page {
    grid-template-columns: 16rem 1fr;
  }
}
```

Vedle media queries existují **container queries**. Komponenta pak nereaguje na šířku celého okna, ale na prostor, který má skutečně k dispozici. Stejná karta se tak může v hlavním obsahu zobrazit vodorovně a v úzkém postranním panelu svisle, i když je viewport v obou případech stejný.

Tento přístup vede ke komponentám, které jsou přenosnější. Layout už není mapa konkrétního monitoru, ale soubor vztahů a omezení.

# 5. Webdesign, přístupnost a výkon

## 5.1 Vizuální hierarchie před efekty

Webdesign není soutěž o největší množství barev, animací a neobvyklých fontů. Úkolem rozhraní je vést pozornost. Uživatel má poznat, co je hlavní nadpis, co je ovládací prvek, která informace spolu souvisí a jak pokračovat.

Vizuální hierarchii vytváří velikost, kontrast, prostor, zarovnání, seskupení a opakování. Dobře navržený web může být graficky velmi střídmý a přesto působit profesionálně, protože vztahy mezi prvky jsou jasné. Naopak stránka s deseti efektními komponentami může působit chaoticky, pokud každá soutěží o pozornost.

Typografie na webu musí počítat s různými displeji a s tím, že uživatel může text zvětšit. Důležitá je čitelná velikost, délka řádku, řádkování a kontrast. Rozdělení na „patkové písmo patří jen na papír, bezpatkové jen na displej“ je příliš hrubé. Moderní displeje vykreslí kvalitní serifové písmo velmi dobře; rozhodující je konkrétní rodina, velikost, kontext a čitelnost. Pro uživatelská rozhraní se bezpatková písma používají často, ale nejde o fyzikální zákaz patek.

Webové fonty navíc ovlivňují výkon. Stahování několika řezů velké rodiny může přidat stovky kilobajtů a zpozdit vykreslení. Proto je vhodné vybírat jen potřebné řezy, zvážit systémová písma, používat moderní formáty a rozumně nastavit načítání.

## 5.2 Přístupnost není speciální režim pro „někoho jiného“

**Web accessibility** znamená, že obsah a ovládání zůstávají použitelné pro lidi s různými schopnostmi, zařízeními a způsoby práce. Člověk může nevidět, hůře rozlišovat barvy, mít třes rukou, používat pouze klávesnici, zvětšit si stránku na 200 %, mít dočasně zlomenou ruku nebo číst web venku na telefonu s odlesky. Přístupnost proto často zlepšuje použitelnost všem.

Dobrý základ překvapivě nevzniká hlavně přidáváním ARIA atributů, ale **správným nativním HTML**. Skutečné tlačítko `button` už umí získat fokus, reagovat na klávesnici a má známou roli pro asistivní technologie. Když místo něj autor udělá klikací `div`, musí velkou část tohoto chování znovu doprogramovat.

Základní pravidla se dají ověřovat v běžné praxi: lze web projít pouze klávesnicí, je fokus viditelný, mají formuláře popisky, mají významové obrázky vhodný `alt`, není informace sdělena jen barvou, je kontrast dostatečný a zůstává stránka použitelná po zvětšení textu? Pro multimédia jsou důležité titulky a podle typu obsahu také přepis nebo zvukový popis.

Aktuálním referenčním rámcem jsou **WCAG 2.2**. Není nutné při prvním seznámení memorovat každé kritérium. Důležitější je pochopit čtyři principy: obsah má být vnímatelný, ovladatelný, srozumitelný a dostatečně robustní pro různé technologie.

## 5.3 Pohyb má vysvětlovat, ne překážet

CSS umí přechody, transformace a animace. Jemná změna stavu tlačítka může pomoci pochopit reakci rozhraní, animované otevření panelu může ukázat prostorovou návaznost. Neustálé poskakování, parallax a automaticky se pohybující pozadí však mohou snižovat čitelnost a u části uživatelů vyvolávat nevolnost.

Média query `prefers-reduced-motion` umožňuje respektovat systémovou preferenci omezeného pohybu. Podobně `prefers-color-scheme` může pomoci s tmavým režimem. Není to výzva vytvářet dvě kompletně odlišné stránky, ale ukázka principu: web může reagovat nejen na velikost obrazovky, ale i na potřeby uživatele.

## 5.4 Výkon je součást designu

Stránka, která vypadá dokonale až deset sekund po kliknutí, má problém použitelnosti. Výkon ovlivňují velikosti obrázků, počet a velikost fontů, množství CSS a JavaScriptu, způsob načítání zdrojů i serverová infrastruktura.

HTML a CSS mohou výkon zlepšit už samy. Správné rozměry obrázků omezí posuny layoutu, responzivní zdroje zabrání stahování zbytečně velkých souborů, `loading="lazy"` může odložit obrázky mimo aktuální obrazovku a jednoduchá sémantická stránka často potřebuje méně kódu než rozhraní sestavené z mnoha univerzálních komponent.

Není správné předpokládat, že externí CSS je rychlé proto, že se vždy jednou stáhne a pak ho „celý internet“ sdílí z cache. Prohlížeče cache spravují podle bezpečnostních a soukromých kontextů a podmínky se mění. Hlavní výhodou externího stylu je především sdílená údržba a možnost opakovaného použití v rámci vlastního webu; cache je další praktická výhoda, nikoli záruka.

# 6. Od zdrojového souboru k publikovanému webu

## 6.1 Projekt je víc než `index.html`

Jednoduchý web může mít jen několik souborů, ale i u něj se vyplatí přehledná struktura:

```text
projekt/
├── index.html
├── kontakt.html
├── styles/
│   └── main.css
├── images/
│   ├── logo.svg
│   └── hero.webp
└── files/
    └── cenik.pdf
```

Názvy souborů je vhodné volit stabilně, bez závislosti na konkrétním počítači. Odkazy v HTML by měly používat webové cesty, ne lokální `C:\Users\...`. Rozdíl se často projeví až při publikaci: stránka, která na autorově počítači „funguje“, může na serveru přijít o obrázky kvůli špatným relativním cestám nebo rozdílu mezi velkými a malými písmeny v názvu souboru.

Pro verzování zdrojového kódu se hodí Git. U textových souborů HTML a CSS dokáže přesně ukázat, který řádek se změnil, a umožní bezpečně experimentovat. Malý statický web lze potom publikovat například na statickém hostingu nebo pomocí služby typu GitHub Pages. Dynamické webové aplikace potřebují další serverovou vrstvu, té se věnuje samostatný okruh.

## 6.2 DevTools: laboratoř přímo v prohlížeči

Nástroje pro vývojáře v prohlížeči umožňují prohlížet DOM, měnit CSS za běhu, sledovat box model, simulovat rozměry zařízení a zjišťovat, který styl skutečně vyhrál v kaskádě. To je mnohem účinnější než náhodně přepisovat hodnoty v souboru a znovu načítat stránku.

Typický problém: prvek má `margin`, ale mezera vypadá jinak, než autor čekal. DevTools ukáže výsledné rozměry boxu a seznam všech pravidel, včetně přeškrtnutých deklarací, které prohrály v kaskádě. CSS se tím mění z „magie, která někdy neposlouchá“ na systém, jehož rozhodování lze krok po kroku sledovat.

Stejným způsobem lze kontrolovat přístupnost, síťové požadavky, velikost zdrojů a výkon vykreslování. Prohlížeč je proto nejen cílové prostředí, ale i jeden z nejdůležitějších diagnostických nástrojů webového vývojáře.

## 6.3 Praktický pracovní postup

Při tvorbě nové stránky je výhodné nezačínat barvami. Nejprve si ujasníme obsah a informační strukturu, potom vytvoříme sémantické HTML, ověříme odkazy a základní ovladatelnost bez stylů. Teprve poté přidáme typografii, mezery a layout. Nakonec testujeme responzivitu, přístupnost, výkon a publikovanou verzi.

Tento postup má jednu zajímavou vlastnost: i když CSS selže nebo se nenačte, dobře napsané HTML zůstává srozumitelným dokumentem. A když později změníme design, nemusíme přepisovat obsah každé stránky. Oddělení vrstev tak není jen estetický ideál, ale praktická strategie pro dlouhodobou údržbu.

Před publikací je rozumné projít několik kontrolních otázek: fungují všechny odkazy a formuláře, má stránka správný titulek a jazyk, jsou obrázky optimalizované a mají smysluplné alternativy, lze vše ovládat klávesnicí, neztrácí se obsah při úzkém viewportu a nehlásí validátor nebo konzole zjevné chyby? U většího projektu se část těchto kontrol automatizuje v CI, ale princip zůstává stejný.

# Závěrečné propojení

HTML a CSS řeší dvě odlišné, ale těsně propojené vrstvy webu. HTML odpovídá především na otázku **„co tato část dokumentu znamená?“**, CSS na otázku **„jak má být v daném kontextu prezentována?“**. Když se role zamění, vzniká kód, který je obtížné upravovat a špatně se přizpůsobuje jiným zařízením nebo uživatelům.

Celý proces lze shrnout jako řetězec:

**obsah → sémantická struktura HTML → DOM → kaskáda a layout CSS → vykreslení v prohlížeči → vnímání a ovládání uživatelem**

Moderní webdesign proto není jen znalost značek a barev. Je to schopnost vytvořit dokument, který má smysluplnou strukturu, pružně se rozloží v různém prostoru, zůstává čitelný a ovladatelný a lze jej dlouhodobě udržovat. Flexbox, Grid, container queries nebo nové selektory jsou důležité nástroje, ale stojí na starší a stále platné myšlence: web funguje nejlépe tehdy, když je význam obsahu oddělen od způsobu jeho prezentace.

## Referenční zdroje pro další studium

- WHATWG: HTML Living Standard — https://html.spec.whatwg.org/
- W3C: CSS Snapshot — https://www.w3.org/TR/css-2026/
- MDN Web Docs: HTML a CSS — https://developer.mozilla.org/
- W3C: Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/
