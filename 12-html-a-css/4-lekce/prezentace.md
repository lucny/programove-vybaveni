## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Normální tok je výchozí, ne překážka**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Než použijeme jakýkoli layout systém, prohlížeč skládá dokument podle **normal flow**. Blokové prvky typicky postupují pod sebou, inline obsah uvnitř řádků. Tento přirozený tok je překvapivě schopný a má jednu velkou výhodu: když se text prodlouží nebo se změní šířka okna, obsah se automaticky přeskupí.

Historické weby často layout simulovaly tabulkami, plovoucími prvky nebo rámy. Tyto techniky řešily skutečné problémy své doby, ale dnešní CSS nabízí nástroje vytvořené přímo pro rozložení. `float` si zachoval vhodný účel například pro obtékání obrázku textem, nemusí však nést celou strukturu webu.

Pozicování pomocí `position: relative`, `absolute`, `fixed` a `sticky` je užitečné pro konkrétní vztahy: odznak v rohu karty, přichycenou hlavičku nebo překrytí vrstev. Není ale dobrým výchozím způsobem, jak ručně rozmístit každou část stránky na pevné souřadnice. Takový návrh se rozpadne ve chvíli, kdy se změní obsah, font nebo rozměr zařízení.

***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Flexbox: když řešíme hlavně jeden směr**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Grid: vztahy v řádcích i sloupcích**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Responzivní design není sada tří obrazovek**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***
