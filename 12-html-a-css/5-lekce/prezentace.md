## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vizuální hierarchie před efekty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Webdesign není soutěž o největší množství barev, animací a neobvyklých fontů. Úkolem rozhraní je vést pozornost. Uživatel má poznat, co je hlavní nadpis, co je ovládací prvek, která informace spolu souvisí a jak pokračovat.

Vizuální hierarchii vytváří velikost, kontrast, prostor, zarovnání, seskupení a opakování. Dobře navržený web může být graficky velmi střídmý a přesto působit profesionálně, protože vztahy mezi prvky jsou jasné. Naopak stránka s deseti efektními komponentami může působit chaoticky, pokud každá soutěží o pozornost.

Typografie na webu musí počítat s různými displeji a s tím, že uživatel může text zvětšit. Důležitá je čitelná velikost, délka řádku, řádkování a kontrast. Rozdělení na „patkové písmo patří jen na papír, bezpatkové jen na displej“ je příliš hrubé. Moderní displeje vykreslí kvalitní serifové písmo velmi dobře; rozhodující je konkrétní rodina, velikost, kontext a čitelnost. Pro uživatelská rozhraní se bezpatková písma používají často, ale nejde o fyzikální zákaz patek.

Webové fonty navíc ovlivňují výkon. Stahování několika řezů velké rodiny může přidat stovky kilobajtů a zpozdit vykreslení. Proto je vhodné vybírat jen potřebné řezy, zvážit systémová písma, používat moderní formáty a rozumně nastavit načítání.

***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Přístupnost není speciální režim pro „někoho jiného“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Web accessibility** znamená, že obsah a ovládání zůstávají použitelné pro lidi s různými schopnostmi, zařízeními a způsoby práce. Člověk může nevidět, hůře rozlišovat barvy, mít třes rukou, používat pouze klávesnici, zvětšit si stránku na 200 %, mít dočasně zlomenou ruku nebo číst web venku na telefonu s odlesky. Přístupnost proto často zlepšuje použitelnost všem.

Dobrý základ překvapivě nevzniká hlavně přidáváním ARIA atributů, ale **správným nativním HTML**. Skutečné tlačítko `button` už umí získat fokus, reagovat na klávesnici a má známou roli pro asistivní technologie. Když místo něj autor udělá klikací `div`, musí velkou část tohoto chování znovu doprogramovat.

Základní pravidla se dají ověřovat v běžné praxi: lze web projít pouze klávesnicí, je fokus viditelný, mají formuláře popisky, mají významové obrázky vhodný `alt`, není informace sdělena jen barvou, je kontrast dostatečný a zůstává stránka použitelná po zvětšení textu? Pro multimédia jsou důležité titulky a podle typu obsahu také přepis nebo zvukový popis.

Aktuálním referenčním rámcem jsou **WCAG 2.2**. Není nutné při prvním seznámení memorovat každé kritérium. Důležitější je pochopit čtyři principy: obsah má být vnímatelný, ovladatelný, srozumitelný a dostatečně robustní pro různé technologie.

***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Pohyb má vysvětlovat, ne překážet**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


CSS umí přechody, transformace a animace. Jemná změna stavu tlačítka může pomoci pochopit reakci rozhraní, animované otevření panelu může ukázat prostorovou návaznost. Neustálé poskakování, parallax a automaticky se pohybující pozadí však mohou snižovat čitelnost a u části uživatelů vyvolávat nevolnost.

Média query `prefers-reduced-motion` umožňuje respektovat systémovou preferenci omezeného pohybu. Podobně `prefers-color-scheme` může pomoci s tmavým režimem. Není to výzva vytvářet dvě kompletně odlišné stránky, ale ukázka principu: web může reagovat nejen na velikost obrazovky, ale i na potřeby uživatele.

***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Výkon je součást designu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Stránka, která vypadá dokonale až deset sekund po kliknutí, má problém použitelnosti. Výkon ovlivňují velikosti obrázků, počet a velikost fontů, množství CSS a JavaScriptu, způsob načítání zdrojů i serverová infrastruktura.

HTML a CSS mohou výkon zlepšit už samy. Správné rozměry obrázků omezí posuny layoutu, responzivní zdroje zabrání stahování zbytečně velkých souborů, `loading="lazy"` může odložit obrázky mimo aktuální obrazovku a jednoduchá sémantická stránka často potřebuje méně kódu než rozhraní sestavené z mnoha univerzálních komponent.

Není správné předpokládat, že externí CSS je rychlé proto, že se vždy jednou stáhne a pak ho „celý internet“ sdílí z cache. Prohlížeče cache spravují podle bezpečnostních a soukromých kontextů a podmínky se mění. Hlavní výhodou externího stylu je především sdílená údržba a možnost opakovaného použití v rámci vlastního webu; cache je další praktická výhoda, nikoli záruka.

# 6. Od zdrojového souboru k publikovanému webu

***
