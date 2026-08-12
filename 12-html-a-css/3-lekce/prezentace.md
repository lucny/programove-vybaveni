## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**CSS není „HTML s barvami“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak kaskáda rozhodne spor**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Selektory jako dotaz na dokument**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Základní selektory vybírají element, třídu nebo identifikátor: `p`, `.note`, `#menu`. Kombinátory popisují vztahy v hierarchii, například `.article p` vybere odstavce uvnitř článku a `.menu > li` pouze položky, které jsou přímými potomky menu.

Atributové selektory umožňují pracovat s vlastnostmi HTML, například `input[type="email"]`. **Pseudotřídy** popisují stav nebo vztah, například `:hover`, `:focus-visible`, `:checked`, `:first-child` nebo moderní `:has()`. **Pseudoelementy** jako `::before`, `::after` nebo `::first-line` reprezentují část elementu, kterou není nutné přidávat jako další HTML uzel.

Zvlášť důležitý je `:focus-visible`. Web nesmí spoléhat pouze na myš. Člověk, který používá klávesnici, potřebuje vidět, který ovládací prvek má právě fokus. „Designové“ odstranění obrysu bez rovnocenné náhrady je typický příklad úpravy, která stránku vizuálně zjednoduší a současně zhorší její použitelnost.

***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Každý prvek je krabice**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jednotky nejsou soutěž „pixely proti procentům“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Starší poučka někdy říká, že responzivní web musí používat relativní jednotky a pixely jsou špatně. Tak jednoduché to není. CSS `px` je **referenční pixel**, nikoli vždy jeden fyzický bod displeje, a pro rámeček o tloušťce 1 px je zcela rozumný. Pro typografii, mezery a pružný layout však často lépe fungují jednotky odvozené od kontextu.

`rem` se vztahuje k velikosti písma kořenového elementu, `em` k aktuálnímu kontextu, `%` k vlastnosti a rodičovskému rozměru podle konkrétního pravidla, `vw` a `vh` k viewportu. Moderní viewportové jednotky jako `dvh` pomáhají řešit dynamickou výšku mobilních prohlížečů. Funkce `min()`, `max()` a `clamp()` dovolují vytvářet plynule se měnící hodnoty s rozumnými hranicemi.

Například nadpis může růst podle šířky obrazovky, ale nikdy nebude příliš malý ani absurdně velký:

```css
h1 {
  font-size: clamp(2rem, 5vw, 4.5rem);
}
```

# 4. Layout: od normálního toku k Flexboxu a Gridu

***
