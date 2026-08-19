## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Proč nekomprimované video rychle zaplní disk**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Jeden snímek 1920 × 1080 obsahuje více než dva miliony pixelů. Pokud bychom pro každý pixel uložili tři osmibitové barevné složky a zobrazili 25 snímků za sekundu, hrubý tok by přesáhl 1,2 gigabitu za sekundu, ještě bez zvuku a režie. Minuta by zabrala několik gigabajtů. Profesionální nekomprimované video existuje, pro běžnou kameru, web nebo školní projekt by však bylo zbytečně náročné.

Komprese využívá dvě nápadné skutečnosti. Uvnitř jednoho snímku bývají sousední pixely podobné a mezi dvěma po sobě jdoucími snímky se často velká část obrazu téměř nezmění. Kodek proto nemusí pokaždé znovu popisovat celou modrou oblohu ani nehybnou stěnu.

**Kodek** je metoda a její programová či hardwarová realizace pro kódování a dekódování média. Některé kodeky pracují bezeztrátově, takže lze rekonstruovat původní data přesně. U distribučního videa je běžnější ztrátová komprese, která odstraňuje méně podstatné informace a aproximuje obraz tak, aby byl při mnohem menším toku vnímaný rozdíl přijatelný.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Prostorová a časová komprese**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Intraframe** komprese zpracuje každý snímek převážně samostatně, podobně jako fotografii. U pracovních kodeků usnadňuje přesné přeskakování po časové ose a snižuje výpočetní náročnost střihu, soubory však bývají větší.

**Interframe** komprese hledá podobnost v čase. Skupina snímků může začínat úplným klíčovým snímkem, po němž následují snímky popisující hlavně změny a odhad pohybu bloků. Když se člověk pohybuje před statickým pozadím, je úspornější říci přibližně „tato oblast se posunula“ než znovu uložit každý pixel. Série souvisejících snímků se často označuje **GOP - Group of Pictures**.

Výhoda se projeví při distribuci, nevýhoda při chybě nebo střihu. Poškození referenčního snímku může ovlivnit více následujících obrazů a dekodér musí pro přesné zobrazení některého okamžiku nejprve zpracovat jeho okolí. Proto může silně komprimovaný soubor přehrávač zvládnout plynule, zatímco editor se při jeho posouvání zadýchává.

Komprese také vysvětluje, proč jsou náročné konfety, déšť, listí nebo rychlé blikání. Mezi snímky se mění velká část jemného obrazu a kodek má při omezeném datovém toku málo prostoru. Objeví se bloky, rozmazané detaily nebo pruhy v přechodech. Zvýšení rozlišení bez odpovídajícího toku může situaci dokonce zhoršit, protože stejné množství dat se dělí mezi více pixelů.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Bitrate, kvalita a velikost souboru**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Datový tok - bitrate** udává množství dat za sekundu, typicky v Mbit/s. Přibližnou velikost videa lze odhadnout:

`velikost v bytech ≈ bitrate v bitech za sekundu × délka v sekundách / 8`

Desetiminutové video s celkovým tokem 8 Mbit/s tedy zabere přibližně 600 MB. Jde o odhad; připočítává se zvuk, metadata a režie kontejneru.

Při **CBR - Constant Bit Rate** se tok drží blízko zadané hodnoty, což může být užitečné tam, kde potřebujeme předvídatelnou přenosovou kapacitu. **VBR - Variable Bit Rate** dává více dat složitému pohybu a méně statickým scénám, takže při stejné průměrné velikosti často využije prostor účinněji. Dvouprůchodové kódování může nejprve analyzovat celé video a ve druhém průchodu data lépe rozdělit; pro živý přenos na takovou analýzu není čas.

Bitrate nelze posuzovat bez kodeku, rozlišení, snímkové frekvence a obsahu. Stejných 5 Mbit/s může stačit na klidný rozhovor, ale rozpadat se při rychlém sportu. Novější kodek může při srovnatelné vnímané kvalitě potřebovat nižší tok, jeho kódování však může být náročnější a starší zařízení jej nemusí podporovat.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**H.264, HEVC, VP9 a AV1 jako reprezentativní generace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Pro přenosný mentální model stačí několik reprezentantů. **H.264/AVC** se stal velmi rozšířenou volbou díky dobrému kompromisu mezi kvalitou, výkonem a kompatibilitou. **HEVC/H.265** dokáže komprimovat účinněji, zvláště u vysokých rozlišení, ale jeho nasazení ovlivňují licenční podmínky a podpora zařízení. **VP9** je otevřeněji distribuovaná alternativa používaná zejména na webu.

**AV1** je novější otevřený kodek navržený pro účinnou distribuci kvalitního videa včetně vysokých rozlišení, HDR a internetového přenosu. Postupně získává hardwarovou podporu, přesto nelze automaticky předpokládat kompatibilitu se všemi staršími přehrávači. Volba „nejmodernějšího“ kodeku proto není vždy nejlepší; rozhoduje cílové zařízení, rychlost kódování, licence, kvalita a dostupný datový tok.

Při produkci se navíc často používá jiná strategie než při publikaci. Kamera nebo převodní program může vytvořit snadno editovatelný pracovní kodek s vyšším tokem. Hotové video se potom exportuje do účinného distribučního kodeku. Opakované převádění mezi ztrátovými formáty je podobné opakovanému ukládání JPEG fotografie: každá generace může přidat další ztrátu, i když výsledné rozlišení zůstává stejné.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Kontejner není kodek**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Soubor s příponou `.mp4` není jedním druhem obrazové komprese. **Multimediální kontejner** je obálka, která může nést video, jednu nebo více zvukových stop, titulky, kapitoly, náhledy a metadata. Kodek určuje, jak je konkrétní stopa zakódována; kontejner určuje, jak jsou stopy organizovány a synchronizovány.

MP4 je velmi rozšířený kontejner pro distribuci, MKV je pružný například pro více zvukových a titulkových stop a WebM je zaměřen na webové použití. MOV se často objevuje v produkčních postupech. AVI je historicky důležitý, ale pro nové komplexní distribuční projekty už obvykle nepřináší výhodu. Jeden MP4 může obsahovat video H.264, jiný HEVC; dva soubory se stejnou příponou proto nemusí přehrát stejné zařízení.

Praktická diagnostika vždy klade dvě otázky: „Jaký je kontejner?“ a „Jakými kodeky jsou zakódovány jeho stopy?“ Zpráva „formát není podporován“ může ve skutečnosti znamenat, že aplikace otevřela kontejner, ale neumí dekódovat video nebo zvuk uvnitř.


Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
