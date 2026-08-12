## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Syntéza: když zvuk nevznikne mikrofonem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Digitální zvuk nemusíme vždy nahrát. Můžeme jej **syntetizovat**, tedy vytvořit matematicky.

Nejjednodušší syntetizátor může začít oscilátorem generujícím sinusový, obdélníkový nebo pilový průběh. Tyto průběhy mají rozdílné spektrum, a proto znějí různě. Výsledný zvuk lze dále tvarovat filtrem, měnit jeho výšku, barvu a průběh v čase.

Nejdůležitější není pamatovat si názvy všech syntetických metod, ale pochopit princip: **zvukový zdroj vytvoří základní signál a další části syntetizátoru jej tvarují**. Vedle klasické subtraktivní syntézy existují například FM syntéza, wavetable nebo sampling, kde výchozím materiálem nejsou matematické průběhy, ale skutečné nahrané vzorky.

Právě sampling vysvětluje, jak může virtuální klavír znít velmi realisticky: nemusí matematicky napodobovat každou fyzikální vlastnost klavíru, ale může přehrávat pečlivě zaznamenané vzorky skutečného nástroje v různých výškách a dynamikách.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**ADSR: krátký příběh jednoho tónu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Samotný stálý elektronický tón by působil mrtvě. Hudební zvuk má začátek, vývoj a konec. Tento průběh dobře ilustruje obálka **ADSR**.

Po stisku klávesy během fáze Attack zvuk naroste. V Decay klesne na úroveň Sustain, na níž může zůstávat po dobu držení klávesy. Po jejím uvolnění přijde Release a tón postupně zanikne.

Klavír má velmi rychlý nástup a potom přirozeně slábne. Smyčcový „pad“ může naopak nabíhat pomalu a dlouho doznívat. Stejný základní oscilátor tak může díky jiné obálce působit jako úplně jiný zvuk.

ADSR je dobrý příklad obecnější myšlenky: v digitálním zvuku často neovládáme jen hodnotu, ale také **to, jak se tato hodnota mění v čase**.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**MIDI: digitální instrukce místo nahrávky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

MIDI je jeden z nejhezčích příkladů oddělení informace od výsledného zvuku.

Když stiskneme klávesu MIDI keyboardu, zařízení nemusí odeslat nahrávku klavíru. Pošle událost typu „zapnuta nota číslo 60 s touto velocity“. Po uvolnění přijde odpovídající Note Off. Virtuální nástroj pak teprve rozhodne, zda se ozve klavír, syntezátor, varhany nebo zcela futuristický zvuk.

MIDI tedy ukládá hlavně **hudební a řídicí události**, nikoli výslednou akustickou vlnu. Proto lze snadno změnit výšku tónu, rytmus, tempo nebo celý nástroj, aniž bychom hudbu znovu nahrávali.

Podobný princip využívá notační software. Notový zápis lze převést na MIDI, MIDI přehrát virtuálním nástrojem a teprve výsledek vyrenderovat do audio souboru. Opačný směr je podstatně obtížnější: z hotové hudební směsi musí software teprve odhadnout, které tóny a nástroje v ní znějí.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**DAW jako digitální studio**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Program typu **DAW — Digital Audio Workstation** spojuje do jednoho prostředí funkce, které dříve vyžadovaly několik samostatných zařízení. Můžeme si jej představit jako kombinaci vícestopého magnetofonu, mixážního pultu, efektových procesorů, MIDI sekvenceru a racku virtuálních nástrojů.

V programech jako Reaper, Ableton Live, FL Studio, Logic Pro nebo podobných může jedna stopa obsahovat skutečně nahraný hlas, druhá MIDI data ovládající syntezátor a třetí hudební podkres. Uživatel přitom nemusí znát všechny profesionální funkce. Pro pochopení principu stačí sledovat, že moderní zvukový projekt je **časová osa několika vrstev, které lze nezávisle nahrávat, upravovat a kombinovat**.

---

Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
