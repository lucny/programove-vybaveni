## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Nadpis není „větší text“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


HTML dává obsahu význam. Nadpisy `h1` až `h6` vytvářejí hierarchii dokumentu; jejich hlavní úlohou není určovat velikost písma. Vzhled nadpisu lze změnit CSS, jeho význam však zůstává. Podobně `strong` označuje silnou důležitost, `em` zdůraznění, `blockquote` delší citaci a `code` úsek počítačového kódu.

To je podstata **sémantického HTML**: vybrat element podle toho, co obsah znamená, nikoli podle toho, jak chceme, aby vypadal. Když autor použije `div` úplně na všechno, vizuálně může stránku pomocí CSS napodobit. Ztrácí však informaci, že určitá oblast je navigace, hlavní obsah nebo samostatný článek.

Moderní HTML proto nabízí elementy jako `header`, `nav`, `main`, `article`, `section`, `aside` a `footer`. Nejsou to hotové grafické bloky. Prohlížeč jim nepřidělí „profesionální layout“ automaticky. Jsou to významové kontejnery.

Představme si školní web. `header` může obsahovat název školy a hlavní navigaci, `main` vlastní obsah stránky, `article` jednu samostatně publikovatelnou aktualitu, `aside` související informace a `footer` kontakty či právní údaje. Když stejný dokument čte čtečka obrazovky, sémantická struktura umožní rychleji přeskakovat mezi významovými oblastmi.

Element `div` tím nezmizel. Stále je vhodným neutrálním kontejnerem tam, kde žádný přesnější význam neexistuje. Chybou není použít `div`; chybou je používat jej automaticky místo elementu, který skutečný význam už popisuje.

***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Odkaz vytváří web**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Element `a` je jedním z prvků, které odlišily web od běžného elektronického dokumentu. Jeho atribut `href` může obsahovat absolutní URL, relativní cestu nebo fragment odkazující na element s konkrétním `id`.

```html
<a href="https://example.org/dokumentace">Externí dokumentace</a>
<a href="galerie.html">Galerie v tomto webu</a>
<a href="#kontakt">Přejít na kontakt</a>
```

Relativní odkazy jsou praktické uvnitř jednoho webu, protože projekt lze přesunout na jinou doménu nebo do jiné složky bez přepisování všech adres. Je však nutné rozumět, vůči čemu se cesta vyhodnocuje. Zápis `../images/logo.svg` znamená „o adresář výše a potom do složky images“.

Text odkazu by měl dávat smysl i bez okolní věty. „Podrobný ceník“ je informativnější než pět odkazů pojmenovaných „zde“. Otevření odkazu do nové karty pomocí `target="_blank"` není vhodné používat automaticky. Uživatel obvykle rozhoduje, zda chce novou kartu, a neočekávané otevření nového kontextu může být matoucí. Pokud pro ně existuje důvod, má rozhraní chování srozumitelně naznačit.

Navigace není jen grafický pruh s tlačítky. Je to informační architektura webu. Na menším webu může stačit hlavní navigace a několik kontextových odkazů, rozsáhlejší služba využije drobečkovou navigaci, vyhledávání a promyšlenou hierarchii kategorií. Původní metafora „drobečků“ z pohádky zůstává výstižná: breadcrumb ukazuje cestu v hierarchii a pomáhá uživateli pochopit, kde se nachází.

***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Obrázek není jen soubor vedle HTML**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Tabulka patří datům, ne layoutu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Formulář je rozhovor mezi člověkem a systémem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***
