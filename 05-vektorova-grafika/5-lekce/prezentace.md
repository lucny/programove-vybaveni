## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rendering: cesta od scény k výslednému obrazu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Rendering** je výpočet výsledného 2D obrazu z popisu 3D scény.

Program musí rozhodnout například:

- které objekty kamera vidí,
- jakou barvu má každý bod povrchu,
- zda je ve stínu,
- co se v něm odráží,
- jak na něj dopadá nepřímé světlo.

U real-time aplikace musí celý proces proběhnout desítky nebo stovkykrát za sekundu.

U filmového renderingu může jediný snímek trvat minuty nebo hodiny, pokud je prioritou maximální kvalita.

Existují proto různé renderovací přístupy.

Nejznámější jsou:

- rasterizace,
- ray tracing,
- path tracing.

Moderní enginy je často kombinují.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rasterizace v 3D grafice**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

3D rasterizace převádí geometrické trojúhelníky na fragmenty a pixely obrazovky.

Zjednodušeně:

1. vrcholy modelu se transformují do prostoru kamery,
2. geometrie se promítne na 2D plochu,
3. trojúhelníky se rasterizují,
4. shader vypočítá vlastnosti pixelů.

Grafické procesory jsou pro tento proces extrémně optimalizované.

Proto rasterizace dlouho dominovala real-time grafice.

Realistické stíny, odrazy a nepřímé světlo se v klasické rasterizační pipeline často řeší pomocí aproximací:

- shadow maps,
- reflection probes,
- screen-space reflections,
- baked lightmaps.

Výsledek může být velmi přesvědčivý, ale některé efekty selhávají v případech, které aproximace nepokrývá.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Ray tracing a cesta paprsku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Ray tracing** sleduje virtuální paprsky a jejich průsečíky se scénou.

Často se vysvětluje, že „simuluje cestu světla od zdroje“. V klasickém počítačovém ray tracingu se však prakticky často postupuje opačně: primární paprsek vysíláme **z kamery do scény**, protože nás zajímají pouze cesty, které mohou přispět do výsledného pixelu.

Po zásahu povrchu lze vyslat další paprsky:

- ke světlu kvůli stínu,
- ve směru odrazu,
- ve směru lomu.

Tím lze přirozeněji vypočítat odrazy a průhlednost než pomocí mnoha rasterizačních triků.

Ray tracing je výpočetně náročný, ale moderní GPU mají specializovaný hardware pro akceleraci průsečíků paprsků s geometrií.

Proto se dnes používá také v real-time hrách, často v hybridní kombinaci s rasterizací.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Path tracing a global illumination**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Path tracing** je Monte Carlo metoda pro simulaci transportu světla.

Z kamery vysílá paprsky do scény a při každém zásahu náhodně vzorkuje možné další směry. Mnoho takových cest postupně odhaduje světelný příspěvek.

Díky tomu může přirozeně zahrnout:

- přímé světlo,
- nepřímé odrazy,
- měkké stíny,
- color bleeding,
- vícečetné odrazy.

Výsledný obraz je zpočátku zašuměný. S rostoucím počtem vzorků se odhad zpřesňuje.

Moderní renderer může použít **denoising**, který pomáhá z menšího počtu vzorků rekonstruovat čistší obraz.

**Global illumination** není jedna konkrétní kombinace ray tracingu a radiosity. Je to obecný pojem pro techniky, které počítají také **nepřímé osvětlení**, tedy světlo odražené mezi povrchy.

Path tracing je jednou z metod global illumination.

**Radiosity** je historicky významná metoda vhodná především pro difuzní výměnu energie mezi plochami.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Ambient occlusion a proč roh bývá tmavší**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Ambient occlusion — AO** odhaduje, jak moc je určitý bod povrchu „zakrytý“ okolní geometrií.

Roh místnosti, škvíra nebo místo, kde se dva objekty téměř dotýkají, má menší přístup k okolnímu světlu než volně vystavená plocha.

AO proto vytváří jemné kontaktní stíny, které pomáhají číst tvar.

Nejde ale o kompletní fyzikální osvětlení. Je to aproximace viditelnosti okolní hemisféry.

V real-time grafice existují screen-space varianty jako SSAO, které pracují pouze s informacemi aktuálně viditelnými na obrazovce.

Výsledek je rychlý, ale může mít artefakty.

AO se často používá jako jedna součást širšího PBR a global illumination workflow.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Keyframe animace a interpolace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Animace znamená změnu vlastností v čase.

V **keyframe animaci** animátor nastaví hodnoty v určitých klíčových okamžicích.

Například:

čas 0 s → objekt je vlevo,

čas 2 s → objekt je vpravo.

Program vypočítá mezilehlé stavy pomocí interpolace.

Animovat lze:

- pozici,
- rotaci,
- měřítko,
- barvu,
- intenzitu světla,
- parametry materiálu,
- tvar objektu.

Interpolace nemusí být lineární. Křivky v animačním editoru umožňují vytvářet zrychlení, zpomalení a přirozené časování.

Právě timing a spacing jsou zásadní pro dojem pohybu. Technicky správná interpolace může působit roboticky, pokud nerespektuje principy animace.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Rigging, skinning a animace postavy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Složitou postavu nechceme animovat posouváním tisíců vrcholů.

Proto se vytváří **rig — kostra a řídicí systém**.

Kostru tvoří hierarchie bones.

Například pohyb předloktí závisí na lokti, pohyb ruky na předloktí a podobně.

Síť postavy se ke kostře připojí pomocí **skinningu**. Jednotlivé vrcholy mohou být ovlivňovány několika kostmi s různými vahami.

Pokud je skinning špatně nastaven, při ohnutí lokte nebo kolena vzniknou nepřirozené deformace.

Animátor často nepohybuje kostmi přímo, ale používá ovládací prvky a **inverse kinematics — IK**.

U IK například určí pozici chodidla a systém dopočítá potřebné úhly nohy.

To je výhodné při kontaktu postavy se zemí nebo objektem.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.8

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Motion capture a particle systems**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Motion capture** zaznamenává pohyb skutečného člověka nebo objektu a převádí jej na animační data.

Systém může používat:

- optické markery,
- inerciální senzory,
- kamery bez markerů,
- kombinované metody.

Data z motion capture obvykle nejsou hotová animace. Je potřeba je vyčistit, přizpůsobit virtuální postavě a ručně upravit.

Podobně **particle system** není jen „animace kouře“.

Částicový systém vytváří mnoho jednoduchých prvků, jejichž vznik, pohyb a zánik řídí pravidla.

Používá se pro:

- jiskry,
- déšť,
- prach,
- kouř,
- magické efekty,
- hejna.

Moderní kouř a kapaliny ale mohou využívat i komplexní fyzikální simulace, kde částice tvoří jen jednu část systému.

**Hlavní myšlenka páté lekce:** rendering řeší, jak ze scény vznikne obraz, zatímco animace určuje, jak se scéna mění v čase. Realistický výsledek často kombinuje fyzikální modely, aproximace, výtvarné rozhodování a vysoký výpočetní výkon.

---


------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
