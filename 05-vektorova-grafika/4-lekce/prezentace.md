## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**3D scéna: více než samotný model**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Když se řekne 3D grafika, mnoho lidí si představí trojrozměrný model. Výsledný obraz ale vzniká z celé **scény**.

Scéna může obsahovat:

- geometrické objekty,
- materiály,
- textury,
- světla,
- kamery,
- animace,
- částicové systémy,
- fyzikální simulace.

Model je tedy jen jedna část.

Aby byl šedý model auta viditelný jako realistický automobil, potřebujeme určit, jak jeho lak reaguje na světlo, jaké je okolní prostředí, odkud se na něj dívá kamera a jak se vypočítají odrazy.

Moderní 3D software proto připomíná kombinaci:

- modelářské dílny,
- fotografického studia,
- filmového animačního pracoviště,
- fyzikálního simulátoru.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Polygonální síť: vrcholy, hrany a plochy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Nejběžnější reprezentací v real-time grafice a mnoha 3D programech je **polygonální mesh — síť**.

Je tvořena:

- vertices — vrcholy,
- edges — hranami,
- faces — plochami.

Grafická karta nakonec velmi často pracuje s **trojúhelníky**, protože trojúhelník vždy leží v jedné rovině a jeho rasterizace je dobře definovaná.

Model může být při práci vytvořen z čtyřúhelníků nebo složitějších polygonů, ale při renderování se obvykle trianguluje.

Důležitá je **topologie** — způsob, jak jsou vrcholy a hrany propojeny.

Dobrá topologie je zásadní například pro animaci postavy. Síť kolem lokte musí být navržena tak, aby se při ohnutí deformovala přirozeně.

Počet polygonů ovlivňuje detail i výpočetní náročnost. Filmový model může mít miliony polygonů, real-time hra musí hlídat výkon.

Moderní systémy umějí pracovat s velmi vysokou geometrickou složitostí, ale optimalizace stále zůstává důležitou součástí grafiky.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**NURBS, subdivision a sculpting**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Polygonální modelování není jediný přístup.

**NURBS modelování** používá matematické křivky a plochy. Je velmi vhodné pro hladké technické povrchy, například karoserie automobilu nebo průmyslový design.

**Subdivision surface** začíná z relativně hrubé polygonální sítě a matematicky vytváří hladší povrch. Modelář tak může ovládat velký tvar pomocí menšího počtu základních polygonů.

**Sculpting** napodobuje digitální sochařství. Uživatel pomocí virtuálních štětců tlačí, vyhlazuje nebo vytahuje povrch.

Používá se například pro:

- postavy,
- organické modely,
- tváře,
- fantastické bytosti,
- jemné povrchové detaily.

V profesionálním workflow se metody často kombinují.

Postava může vzniknout sculptingem ve vysokém detailu. Potom se vytvoří jednodušší topologie vhodná pro animaci — **retopology** — a jemné detaily se přenesou do normálových nebo displacement map.

Neexistuje tedy jediný „správný“ způsob 3D modelování. Volba závisí na tom, zda připravujeme technický díl, filmovou postavu, herní prostředí nebo model pro 3D tisk.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**UV mapping a textury**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

3D geometrie určuje tvar, ale povrch potřebuje další informace.

**UV mapping** převádí povrch 3D modelu do 2D souřadnicové mapy.

Můžeme si to představit podobně jako rozložení papírového modelu krabice na rovinu.

Na tento 2D „střih“ lze položit texturu.

Písmena U a V se používají proto, že X, Y a Z už tradičně označují prostorové souřadnice.

Textura nemusí znamenat jen barevnou fotografii povrchu. Moderní materiál může používat několik map:

- base color,
- roughness,
- metallic,
- normal,
- displacement,
- ambient occlusion.

Normálová mapa například vytváří dojem drobných nerovností změnou orientace povrchových normál bez toho, aby skutečně přidala odpovídající polygonální geometrii.

Displacement může naopak geometrický povrch skutečně posouvat.

Textury lze také generovat **procedurálně** pomocí matematických funkcí a uzlových systémů. Tím lze vytvářet například dřevo, kámen, mraky nebo šum bez klasického obrazového souboru.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**PBR materiály: jak povrch reaguje na světlo**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Moderní real-time i filmová grafika často používá **PBR — Physically Based Rendering**.

Cílem není dokonale simulovat veškerou fyziku světla, ale používat materiálový model, který se chová konzistentněji a fyzikálně uvěřitelně v různých světelných podmínkách.

Častý workflow používá parametry:

- base color,
- metallic,
- roughness.

**Metallic** určuje, zda se materiál chová více jako kov nebo dielektrikum.

**Roughness** ovlivňuje mikrostrukturu povrchu a tím ostrost odrazů.

Hladký lak může mít ostré odlesky, hrubý povrch rozptýlené.

Základem je **BRDF — Bidirectional Reflectance Distribution Function**, matematický model popisující, jak se světlo odráží podle směru dopadu a pozorování.

Student nemusí počítat BRDF integrály, ale měl by pochopit, že materiál není jen „barva objektu“.

Stejná šedá barva může vypadat jako:

- kov,
- plast,
- guma,
- keramika,

podle způsobu interakce se světlem.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kamera, projekce a perspektiva**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

3D scéna se musí převést na 2D obraz.

K tomu slouží virtuální kamera.

**Perspektivní projekce** napodobuje běžnou kameru: vzdálené objekty se jeví menší.

**Ortografická projekce** zachovává měřítko nezávisle na vzdálenosti. Používá se v technických pohledech a některých stylizovaných hrách.

Kamera má parametry podobné fotografii:

- pozice,
- směr,
- zorné pole,
- clipping planes,
- někdy fyzicky modelovanou ohniskovou vzdálenost a clonu.

Při renderování architektury nebo filmu se proto znalosti digitální fotografie přímo propojují s 3D grafikou.

Virtuální kamera může simulovat:

- hloubku ostrosti,
- motion blur,
- zkreslení objektivu,
- expozici.

Rozdíl je v tom, že virtuální scéna dovoluje téměř úplnou kontrolu nad prostředím.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Světla a prostředí**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Bez světla není vidět materiál ani tvar.

3D programy poskytují různé typy světel:

- point light,
- spot light,
- directional light,
- area light,
- environment lighting.

Jednoduché **point light** vyzařuje z bodu.

**Directional light** napodobuje velmi vzdálený zdroj, typicky slunce, takže paprsky mají přibližně stejný směr.

**Area light** má nenulovou plochu a vytváří měkčí stíny.

Moderní scény často používají **HDRI environment maps** jako zdroj okolního osvětlení a odrazů.

Historický pojem „ambient light“ jako jednoduché rovnoměrné přisvícení je užitečný pro základní model, ale fyzikálně realističtější rendering se snaží světlo od prostředí a nepřímé odrazy vypočítat skutečněji.

**Hlavní myšlenka čtvrté lekce:** 3D grafika není jen tvorba geometrie. Výsledný obraz vzniká kombinací modelu, topologie, materiálů, textur, kamery a osvětlení.

---

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
