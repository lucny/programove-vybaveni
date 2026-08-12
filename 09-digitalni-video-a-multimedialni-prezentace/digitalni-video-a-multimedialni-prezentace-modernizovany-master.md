# Digitální video a multimediální prezentace

## Modernizovaný výukový text

> Video není jen rychlá řada fotografií a prezentace není jen soubor snímků. V obou případech spojujeme obraz, zvuk, čas a záměr do sdělení, které musí počítač správně zachytit, uložit, přenést a zobrazit - a člověk pochopit.

# 1. Od světla k digitálnímu videu

## 1.1 Video jako řada obrazů v čase

Když kamera zaznamená míč letící vzduchem, nevytváří v běžném videu nepřetržitý obraz pohybu. Pořídí rychlou posloupnost jednotlivých snímků a při přehrávání je zobrazí ve stejném pořadí. Lidské vidění a mozek změny propojí do vjemu plynulého děje. Digitální video proto můžeme chápat jako časovou řadu rastrových obrazů doplněnou zvukem, časovými údaji a dalšími informacemi.

Analogové televizní a videokazetové systémy také pracovaly s obrazem rozloženým v čase, jeho jas a barvu však přenášely jako spojitě proměnný elektrický signál. Byly svázány s normami, jako jsou PAL, NTSC a SECAM, a kopírování či přenos obvykle postupně přidávaly šum a zkreslení. Digitální video ukládá číselnou reprezentaci obrazu. Kopie stejných dat může být bitově totožná s originálem, neznamená to však, že každý digitální převod nebo export proběhne beze ztráty. Ztrátová komprese může část obrazové informace záměrně odstranit.

Každý snímek je tvořen pixely, ale samotné pixely ještě neurčují kvalitu výsledku. Záleží také na kvalitě optiky a snímače, množství světla, dynamickém rozsahu, barevném záznamu, snímkové frekvenci, kompresi a způsobu zobrazení. Video ve 4K natočené za špatného světla s agresivní kompresí může působit hůře než pečlivě pořízené Full HD.

## 1.2 Co se děje uvnitř kamery

Objektiv soustředí světlo na obrazový snímač, dnes nejčastěji typu **CMOS**. Jeho miliony světlocitlivých míst převádějí dopadající světlo na elektrický náboj. Tento analogový signál změří A/D převodník a obrazový procesor z něj sestaví digitální snímek. Starší nebo specializovaná zařízení mohou používat i snímače CCD, pro běžné vysvětlení současné kamery je však CMOS reprezentativnější.

Jedno světlocitlivé místo samo obvykle nerozpoznává plnou barvu. Před snímačem proto může být mozaika barevných filtrů, často **Bayerova maska**, v níž jsou zastoupeny červené, zelené a modré prvky. Kamera z naměřených hodnot odhadne chybějící barevné složky sousedních pixelů procesem zvaným **demosaicing**. Výsledný barevný pixel je tedy částečně výsledkem výpočtu, nikoli tří nezávislých měření na jediném místě.

Při natáčení se potkávají tři základní expoziční volby. Clona ovlivňuje množství světla a hloubku ostrosti, expoziční čas ovlivňuje množství světla i rozmazání pohybu a nastavení ISO či zisku zesiluje obrazový signál. Vyšší ISO nezpůsobí, že by snímač zachytil více fotonů; zesílí signál i jeho šum. Proto je zpravidla lepší nejprve pracovat se světlem, clonou a časem a teprve potom výrazně zvyšovat zesílení.

U videa nemůžeme expoziční čas volit zcela nezávisle na snímkové frekvenci. Příliš krátký čas zmrazí každý snímek a pohyb může působit trhaně, příliš dlouhý jej nadměrně rozmaže. Tradiční orientační pravidlo používá čas přibližně odpovídající polovině délky snímku, například kolem 1/50 s při 25 fps. Není to přírodní zákon, ale dobrý výchozí bod pro přirozeně působící pohyb.

## 1.3 Rozlišení, poměr stran a skutečná ostrost

**Rozlišení** udává pixelové rozměry snímku. Full HD má typicky 1920 × 1080 pixelů, označení 4K ale není ve všech prostředích úplně stejné: spotřební UHD běžně znamená 3840 × 2160, zatímco digitální kino používá i širší variantu 4096 × 2160. Vyšší rozlišení umožní zachovat jemnější detail nebo bezpečněji oříznout obraz, současně však zvyšuje datové, výpočetní a úložné nároky.

**Poměr stran - aspect ratio** popisuje vztah šířky a výšky, například 16:9, 4:3, čtvercový 1:1 nebo svislý 9:16. Poměr stran není totéž co rozlišení. Video 1920 × 1080 i 1280 × 720 má poměr 16:9, pouze obsahuje jiný počet pixelů. Při přípravě je rozumné znát cílové prostředí před natáčením: obraz určený pro širokou projekci se komponuje jinak než svislé video pro telefon.

Ostrost dále ovlivňuje zaostření, pohyb kamery, kvalita objektivu, šum a komprese. **Optický zoom** mění ohniskovou vzdálenost objektivu a může přiblížit scénu bez prostého zvětšování pixelů. **Digitální zoom** obvykle pouze vyřízne část snímku a dopočítá ji do požadované velikosti. Může být praktický, ale nevytvoří skutečný detail, který snímač nezachytil.

## 1.4 Snímková frekvence a charakter pohybu

**Snímková frekvence - frame rate** udává počet snímků za sekundu, zkráceně fps. Filmový obraz se tradičně spojuje s 24 fps, evropská televizní a síťová prostředí často pracují s 25 nebo 50 fps a některé sportovní, herní či internetové záznamy s 30 nebo 60 fps. Vyšší hodnota může zobrazit rychlý pohyb plynuleji, není však automaticky „kvalitnější“ pro každý záměr. Změní vzhled pohybu, nároky na světlo i množství dat.

Záznam pořízený například při 100 fps lze v projektu 25 fps zpomalit na čtvrtinovou rychlost a stále mít pro každý výsledný snímek původní obraz. Když naopak zpomalíme běžný záznam bez dostatku snímků, software musí snímky opakovat nebo dopočítávat. Optický tok a AI interpolace mohou mezisnímky odhadnout, ale u překrývajících se objektů, rychlých rukou nebo vody často vzniknou deformace.

Historická televize šetřila přenosovou kapacitu **prokládaným obrazem - interlacing**. Jeden časový okamžik nesl liché a další sudé řádky, což označení 1080i dodnes připomíná. Moderní displeje i internetové video jsou převážně progresivní: každý snímek obsahuje celý obraz a označuje se například 1080p. Starý prokládaný záznam je při převodu nutné správně odstranit procesem deinterlacingu, jinak se na pohybujících hranách objeví „hřebínky“.

## 1.5 Barva, jas a dynamický rozsah

Kamera musí barvu nejen zachytit, ale také popsat ve zvoleném barevném prostoru. **Vyvážení bílé - white balance** říká, co má při daném osvětlení působit neutrálně. Automatika je pohodlná, může však během jednoho záběru měnit barevnost. Při smíšeném světle z okna a žárovek navíc nemusí existovat jediné nastavení, které opraví celou scénu. Proto se vyplatí sjednotit zdroje světla nebo vědomě určit, který z nich je hlavní.

Video často odděluje jasovou informaci od barevných složek a barvu ukládá s menším prostorovým rozlišením. Tato **chroma subsampling** strategie využívá toho, že lidské vidění obvykle vnímá jemný detail více v jasu než v barvě. Zápis 4:4:4 zachovává barvu nejpodrobněji, 4:2:2 a 4:2:0 ji vzorkují úsporněji. Pro běžné přehrávání může 4:2:0 vypadat výborně, při klíčování zeleného pozadí nebo výrazných barevných úpravách je bohatší záznam výhodou.

**Bitová hloubka** určuje počet úrovní dostupných pro barevné složky. Osmibitové video má na složku 256 hodnot, desetibitové 1024. Větší přesnost pomáhá omezit viditelné pruhy v jemných přechodech a poskytuje rezervu pro postprodukci. **HDR - High Dynamic Range** navíc umožňuje pracovat s větším rozsahem jasů a širšími barvami než tradiční SDR, ale pouze tehdy, když celý řetězec od kamery přes úpravu až po displej používá správná metadata a kompatibilní zobrazení. Pouhé označení souboru jako HDR nevykouzlí informaci, která nebyla zachycena.

# 2. Komprese, kodeky a kontejnery

## 2.1 Proč nekomprimované video rychle zaplní disk

Jeden snímek 1920 × 1080 obsahuje více než dva miliony pixelů. Pokud bychom pro každý pixel uložili tři osmibitové barevné složky a zobrazili 25 snímků za sekundu, hrubý tok by přesáhl 1,2 gigabitu za sekundu, ještě bez zvuku a režie. Minuta by zabrala několik gigabajtů. Profesionální nekomprimované video existuje, pro běžnou kameru, web nebo školní projekt by však bylo zbytečně náročné.

Komprese využívá dvě nápadné skutečnosti. Uvnitř jednoho snímku bývají sousední pixely podobné a mezi dvěma po sobě jdoucími snímky se často velká část obrazu téměř nezmění. Kodek proto nemusí pokaždé znovu popisovat celou modrou oblohu ani nehybnou stěnu.

**Kodek** je metoda a její programová či hardwarová realizace pro kódování a dekódování média. Některé kodeky pracují bezeztrátově, takže lze rekonstruovat původní data přesně. U distribučního videa je běžnější ztrátová komprese, která odstraňuje méně podstatné informace a aproximuje obraz tak, aby byl při mnohem menším toku vnímaný rozdíl přijatelný.

## 2.2 Prostorová a časová komprese

**Intraframe** komprese zpracuje každý snímek převážně samostatně, podobně jako fotografii. U pracovních kodeků usnadňuje přesné přeskakování po časové ose a snižuje výpočetní náročnost střihu, soubory však bývají větší.

**Interframe** komprese hledá podobnost v čase. Skupina snímků může začínat úplným klíčovým snímkem, po němž následují snímky popisující hlavně změny a odhad pohybu bloků. Když se člověk pohybuje před statickým pozadím, je úspornější říci přibližně „tato oblast se posunula“ než znovu uložit každý pixel. Série souvisejících snímků se často označuje **GOP - Group of Pictures**.

Výhoda se projeví při distribuci, nevýhoda při chybě nebo střihu. Poškození referenčního snímku může ovlivnit více následujících obrazů a dekodér musí pro přesné zobrazení některého okamžiku nejprve zpracovat jeho okolí. Proto může silně komprimovaný soubor přehrávač zvládnout plynule, zatímco editor se při jeho posouvání zadýchává.

Komprese také vysvětluje, proč jsou náročné konfety, déšť, listí nebo rychlé blikání. Mezi snímky se mění velká část jemného obrazu a kodek má při omezeném datovém toku málo prostoru. Objeví se bloky, rozmazané detaily nebo pruhy v přechodech. Zvýšení rozlišení bez odpovídajícího toku může situaci dokonce zhoršit, protože stejné množství dat se dělí mezi více pixelů.

## 2.3 Bitrate, kvalita a velikost souboru

**Datový tok - bitrate** udává množství dat za sekundu, typicky v Mbit/s. Přibližnou velikost videa lze odhadnout:

`velikost v bytech ≈ bitrate v bitech za sekundu × délka v sekundách / 8`

Desetiminutové video s celkovým tokem 8 Mbit/s tedy zabere přibližně 600 MB. Jde o odhad; připočítává se zvuk, metadata a režie kontejneru.

Při **CBR - Constant Bit Rate** se tok drží blízko zadané hodnoty, což může být užitečné tam, kde potřebujeme předvídatelnou přenosovou kapacitu. **VBR - Variable Bit Rate** dává více dat složitému pohybu a méně statickým scénám, takže při stejné průměrné velikosti často využije prostor účinněji. Dvouprůchodové kódování může nejprve analyzovat celé video a ve druhém průchodu data lépe rozdělit; pro živý přenos na takovou analýzu není čas.

Bitrate nelze posuzovat bez kodeku, rozlišení, snímkové frekvence a obsahu. Stejných 5 Mbit/s může stačit na klidný rozhovor, ale rozpadat se při rychlém sportu. Novější kodek může při srovnatelné vnímané kvalitě potřebovat nižší tok, jeho kódování však může být náročnější a starší zařízení jej nemusí podporovat.

## 2.4 H.264, HEVC, VP9 a AV1 jako reprezentativní generace

Pro přenosný mentální model stačí několik reprezentantů. **H.264/AVC** se stal velmi rozšířenou volbou díky dobrému kompromisu mezi kvalitou, výkonem a kompatibilitou. **HEVC/H.265** dokáže komprimovat účinněji, zvláště u vysokých rozlišení, ale jeho nasazení ovlivňují licenční podmínky a podpora zařízení. **VP9** je otevřeněji distribuovaná alternativa používaná zejména na webu.

**AV1** je novější otevřený kodek navržený pro účinnou distribuci kvalitního videa včetně vysokých rozlišení, HDR a internetového přenosu. Postupně získává hardwarovou podporu, přesto nelze automaticky předpokládat kompatibilitu se všemi staršími přehrávači. Volba „nejmodernějšího“ kodeku proto není vždy nejlepší; rozhoduje cílové zařízení, rychlost kódování, licence, kvalita a dostupný datový tok.

Při produkci se navíc často používá jiná strategie než při publikaci. Kamera nebo převodní program může vytvořit snadno editovatelný pracovní kodek s vyšším tokem. Hotové video se potom exportuje do účinného distribučního kodeku. Opakované převádění mezi ztrátovými formáty je podobné opakovanému ukládání JPEG fotografie: každá generace může přidat další ztrátu, i když výsledné rozlišení zůstává stejné.

## 2.5 Kontejner není kodek

Soubor s příponou `.mp4` není jedním druhem obrazové komprese. **Multimediální kontejner** je obálka, která může nést video, jednu nebo více zvukových stop, titulky, kapitoly, náhledy a metadata. Kodek určuje, jak je konkrétní stopa zakódována; kontejner určuje, jak jsou stopy organizovány a synchronizovány.

MP4 je velmi rozšířený kontejner pro distribuci, MKV je pružný například pro více zvukových a titulkových stop a WebM je zaměřen na webové použití. MOV se často objevuje v produkčních postupech. AVI je historicky důležitý, ale pro nové komplexní distribuční projekty už obvykle nepřináší výhodu. Jeden MP4 může obsahovat video H.264, jiný HEVC; dva soubory se stejnou příponou proto nemusí přehrát stejné zařízení.

Praktická diagnostika vždy klade dvě otázky: „Jaký je kontejner?“ a „Jakými kodeky jsou zakódovány jeho stopy?“ Zpráva „formát není podporován“ může ve skutečnosti znamenat, že aplikace otevřela kontejner, ale neumí dekódovat video nebo zvuk uvnitř.

# 3. Natáčení: technika slouží příběhu

## 3.1 Preprodukce ušetří nejvíce času

Krátký školní medailon může vzniknout dvěma způsoby. Skupina přijde na místo a začne bez přípravy natáčet vše, co ji napadne. Nebo si předem ujasní hlavní sdělení, publikum, délku, prostředí, účastníky a potřebné záběry. Druhá skupina možná stráví hodinu plánováním, ale při střihu nebude zoufale hledat obraz, který nikdy nevznikl.

**Preprodukce** zahrnuje námět, scénář, rozpočet, termíny, svolení k natáčení, kontrolu lokace a technický plán. U hrané nebo vysvětlující scény pomůže storyboard, u reportáže seznam záběrů a otázek. Je vhodné promyslet také formát výsledku, titulky, autorská práva a způsob zveřejnění. Jestliže má být video přístupné bez zvuku, musí již scénář počítat s titulky a obrazovou srozumitelností.

Jednoduchý plán odpoví na pět otázek: Co má divák po zhlédnutí vědět nebo udělat? Pro koho video vzniká? Jaký obraz a zvuk toto sdělení unesou? Co musíme zachytit jen jednou a nesmíme pokazit? Kam a v jaké podobě se výsledek publikuje?

## 3.2 Kompozice, velikosti záběrů a prostor

Velký celek představí prostředí, celek ukáže postavu v prostoru, polocelek se hodí pro jednání a detail soustředí pozornost na tvář nebo předmět. Velký detail může zvýraznit oči, ruce či drobnou součástku. Nejde o slovník, který je nutné mechanicky použít celý, ale o řízení divákovy pozornosti.

**Pravidlo třetin** nabízí užitečnou výchozí mřížku: důležité prvky umísťujeme poblíž třetin obrazu, místo abychom vše bez rozmyslu centrovali. Symetrie, středová kompozice nebo záměrně prázdný prostor však mohou fungovat stejně dobře. Pravidlo je pomůcka, nikoli estetický zákon. Kompozice musí zejména ukázat vztahy, směr pohledu a to, co je v daném okamžiku podstatné.

Při rozhovoru dvou lidí pomáhá **pravidlo osy 180°**. Představíme si čáru mezi postavami a kamery držíme na jedné její straně. Na výsledných záběrech pak osoby hledí proti sobě a prostor zůstává srozumitelný. Překročení osy není zakázané, musí však být vědomé a divák by měl změnu prostoru pochopit například z pohybu kamery nebo širšího záběru.

Pohyb kamery má mít důvod. Panoráma může odhalit prostředí, jízda sledovat postavu a pomalé přiblížení zdůraznit okamžik. Původní poučka, že každý záběr musí obsahovat pohyb, je zavádějící. Statický záběr může být klidný, přesný a působivý; bezúčelné kroužení a zoomování naopak ztěžuje sledování.

## 3.3 Stabilita, ostření a práce s objektivem

Stativ je často nejlevnější způsob, jak obraz výrazně zlepšit. Optická stabilizace posouvá člen objektivu nebo snímač, elektronická stabilizace obraz ořezává a softwarově vyrovnává, gimbal mechanicky kompenzuje natočení kamery. Každá metoda má hranice: elektronická stabilizace ubírá okraje a může deformovat pohyb, optická nemusí odstranit chůzi a gimbal nenahradí promyšlenou trasu.

Automatické ostření dnes dokáže sledovat obličej nebo oči, ale může přeostřit na člověka v pozadí či začít „lovit“ v šeru. Před důležitým záběrem je vhodné ověřit, co kamera skutečně sleduje. Manuální ostření dává kontrolu u připravené scény, vyžaduje však cvik a vhodný náhled.

Změna ohniskové vzdálenosti ovlivňuje nejen velikost objektu, ale způsob, jakým zvolená vzdálenost kamery ukáže prostor. Široký objektiv zblízka zvýrazní rozdíly mezi blízkým a vzdáleným, delší ohnisko z větší vzdálenosti působí plošším dojmem. Často tedy nestačí „přiblížit zoom“; je třeba zvolit polohu kamery podle požadované perspektivy.

## 3.4 Světlo, expozice a barva v praxi

Dobré světlo nemusí znamenat drahou soupravu. Rozhovor poblíž velkého okna může působit lépe než záznam pod směsí stropních zářivek a ostrého bodového světla. Hlavní neboli klíčové světlo tvaruje tvář, doplňkové světlo může změkčit stíny a protisvětlo oddělit postavu od pozadí. Tříbodové svícení je užitečný model, ne povinnost pro každou scénu.

Nejčastější problém představuje velký rozdíl mezi světlými a tmavými částmi. Kamera nemusí současně zachovat oblohu za oknem i tvář v tmavé místnosti. Pomůže změna pozice, zatažení závěsu, přidání světla na tvář nebo vědomá volba, která část má zůstat správně exponovaná. Přepaly bez kresby nelze v postprodukci spolehlivě obnovit.

Před sérií záběrů je vhodné nastavit vyvážení bílé konzistentně. Automatika může při průchodu barevného objektu před kamerou změnit celý odstín scény, což později komplikuje střih. U kontrolovaného natáčení proto pomůže pevný režim nebo měření podle neutrální plochy.

## 3.5 Zvuk je polovina zážitku

Divák často snese mírně roztřesený obraz, ale rychle odejde od videa, v němž nerozumí řeči. Vestavěný mikrofon daleko od mluvčího zachytí hodně místnosti, ozvěny a ruchu. Externí klopový, směrový nebo reportážní mikrofon umístěný blízko zdroje obvykle přinese větší zlepšení než další zvýšení rozlišení kamery.

Před natáčením je rozumné pořídit krátkou zkoušku a poslechnout ji ve sluchátkách. Měřič úrovně neodhalí hučení klimatizace ani odrazy prázdné učebny. Záznam nesmí přebuzovat; je vhodné ponechat rezervu pro smích nebo hlasitější slovo. Několik sekund přirozeného zvuku prostoru, **room tone**, může při střihu pomoci vyplnit mezery.

U každého důležitého záběru se vyplatí krátce zkontrolovat obraz, ostrost i zvuk, ale nepodlehnout nekonečnému kontrolování. Praktický postup je: připravit scénu, zkontrolovat baterii, kapacitu a nastavení, natočit zkušební úsek, poslechnout, teprve potom zaznamenat celý výkon.

# 4. Postprodukce, export a distribuce

## 4.1 Nedestruktivní střih a práce s materiálem

Program pro nelineární střih - **NLE, Non-Linear Editor** - si lze představit jako časovou osu obrazových a zvukových vrstev. Klipy se na ní zkracují, přesouvají a kombinují, ale zdrojové soubory obvykle zůstávají nezměněné. Projekt ukládá rozhodnutí, nikoli automaticky všechny použité záběry. Když originál přesuneme nebo smažeme, projekt jej nemusí najít.

Proto postprodukce začíná organizací. Soubory se zálohují, přehledně pojmenují, rozdělí podle scén a podle potřeby doplní poznámkami. Z náročných originálů lze vytvořit lehčí **proxy** soubory pro plynulý střih; při finálním exportu se editor vrátí k plné kvalitě. Proxy není podvod ani horší verze výsledku, ale pracovní náhrada.

Hrubý střih nejprve určí obsah a pořadí, jemný střih rytmus a přesné návaznosti. Střih není jen odstraňování chyb. Výběrem okamžiku měníme význam: reakční záběr po otázce může působit jako souhlas, nesouhlas nebo nejistota podle délky a kontextu. Etická odpovědnost proto začíná už na časové ose.

Přechod není ozdoba, kterou je nutné vložit mezi každý záběr. Přímý střih bývá nejčitelnější, prolínačka může naznačit změnu času nebo nálady a zatmívačka uzavřít celek. Efekt má sloužit významu; katalog přechodů sám o sobě profesionální video nevytvoří.

## 4.2 Obrazová a zvuková úprava

**Barevná korekce** sjednocuje expozici, vyvážení bílé a kontrast záběrů, aby na sebe přirozeně navazovaly. **Color grading** pak vědomě vytváří vzhled a náladu. Hranice se v praxi překrývá, důležité je pořadí: nejprve opravit a sjednotit, potom stylizovat. LUT může být užitečná převodní nebo tvůrčí tabulka, není však univerzální filtr, který automaticky opraví špatně natočený materiál.

Při úpravách se hodí technické náhledy, například histogram, waveform a vectorscope. Monitor může mít nesprávný jas nebo barevný režim, zatímco měřicí graf pomůže odhalit přepaly, stlačené stíny či barevný posun. Smyslem není naučit se studiovou koloristiku, ale nekontrolovat obraz pouze podle náhodně nastaveného displeje.

**Klíčování - chroma key** nahrazuje vybranou barvu, nejčastěji zelené nebo modré pozadí, jiným obrazem. Dobré oddělení nevzniká až kliknutím v editoru: pozadí musí být rovnoměrně osvětlené, postava od něj dostatečně vzdálená a záznam musí zachovat použitelné barevné hrany. Zmačkané plátno, barevné odlesky na tváři nebo silná komprese práci výrazně ztíží.

Zvukové stopy je potřeba vyčistit, srovnat a smíchat. Mluvené slovo musí zůstat srozumitelné nad hudbou, ruchy a efekty. Krátké prolínání zvuku zabrání lupnutí na střihu, automatizace hlasitosti stáhne hudbu během řeči a opatrný ekvalizér či dynamická komprese mohou hlas vyrovnat. Silná redukce šumu však vytváří artefakty a nenahradí čistý záznam.

Titulky nejsou jen překlad. Zachycují mluvený obsah a podle potřeby také identitu mluvčího a významové zvuky. Automatický přepis urychlí práci, ale názvy, čísla a odborné pojmy je nutné zkontrolovat. Titulky musí být správně načasované, čitelné a nesmějí zakrývat důležitou obrazovou informaci.

## 4.3 Export podle cíle, ne podle největšího čísla

Projekt, pracovní soubory a hotové distribuční video jsou tři různé věci. Projekt zachovává editovatelnost, archivní nebo mezilehlý export drží vysokou kvalitu a distribuční soubor upřednostňuje rozumnou velikost a kompatibilitu. Jediný silně komprimovaný soubor z webu proto není dobrý dlouhodobý master.

Při exportu volíme rozlišení, snímkovou frekvenci, barevný režim, kodek, bitrate, zvuk a kontejner. Pokud zdroj vznikl v 1080p, export do 4K obvykle pouze dopočítá pixely. Pokud byl natočen při 25 fps, převod na 60 fps nevytvoří autentický pohyb bez odhadu mezisnímků. Rozumné je zachovat přirozené parametry projektu a přizpůsobit kopii konkrétnímu cíli.

Před odevzdáním je nutné zhlédnout skutečně vyexportovaný soubor, ideálně na více zařízeních. Kontrolujeme začátek a konec, synchronizaci zvuku, titulky, barevnost, hlasitost, chybějící média i nechtěný černý rám. Úspěšně dokončený export neznamená automaticky správný film.

## 4.4 Co se stane po stisknutí „Publikovat“

Video nahrané na platformu obvykle není divákům posíláno jako jediný původní soubor. Služba je překóduje do více rozlišení, toků a někdy i kodeků. Vytvoří krátké segmenty a přehrávač za běhu vybírá variantu podle rychlosti připojení, velikosti obrazovky a výkonu zařízení. Tento princip se nazývá **adaptivní streaming**.

Pro doručování se používají technologie nad HTTP, například HLS a MPEG-DASH. Přehrávač udržuje **buffer**, malou zásobu dopředu staženého videa. Větší zásoba lépe překlene výkyv sítě, ale u živého vysílání zvýší zpoždění. Adaptivní algoritmus proto hledá kompromis mezi kvalitou, plynulostí a latencí.

RTMP se často používá pro dopravu živého signálu od vysílacího programu k serveru, nikoli jako univerzální způsob, kterým dnešní webový přehrávač doručuje video každému divákovi. Server může vstup převést do variant pro HLS nebo DASH a roznést je přes síť CDN. Oddělení vstupu, překódování a distribuce umožní obsloužit mnoho různých zařízení.

## 4.5 Přístupnost, práva a archivace

Přístupné video počítá s různými způsoby vnímání. Pro neslyšící a nedoslýchavé jsou zásadní přesné titulky, pro nevidomé může být potřebný zvukový popis důležité vizuální informace. Samostatný přepis pomáhá také při vyhledávání, rychlém studiu a použití v hlučném či tichém prostředí. Přístupnost není závěrečný filtr; nejlépe se navrhuje už ve scénáři.

Hudba, fotografie, font, klip z filmu i hlas jiné osoby mohou podléhat autorským nebo osobnostním právům. Skutečnost, že je soubor snadno dostupný na internetu, neznamená, že jej lze libovolně použít. U vlastního projektu je vhodné evidovat licence a souhlasy spolu se zdroji, ne až po zveřejnění hledat, odkud která položka pochází.

Archivace má uchovat zdrojové záběry, projekt, důležité grafické a zvukové prvky, kvalitní master i informace o použitých verzích a licencích. Synchronizovaná složka sama o sobě není úplná záloha: omylem smazaný soubor se může smazat všude. U hodnotného projektu potřebujeme oddělenou kopii a možnost návratu ke starší verzi.

# 5. Multimediální prezentace jako řízené sdělení

## 5.1 Prezentace není dokument promítnutý na stěnu

Snímek má podporovat pozornost publika v určitém okamžiku, zatímco dokument musí často fungovat i bez autora. Když na plátno vložíme celé odstavce a současně je čteme, publikum soutěží mezi poslechem a čtením. Dobrá prezentace proto rozděluje role: řečník vysvětluje, snímek orientuje, ukazuje důkaz, vztah nebo obraz a doprovodný materiál uchovává podrobnosti.

Začátek má vyjasnit problém a důvod, proč se jím zabývat. Hlavní část postupuje po srozumitelných krocích a závěr nevypíše pouze nadpisy, ale vrátí se k původní otázce a ukáže další rozhodnutí či akci. Storytelling neznamená přidat dramatickou historku ke každému tématu. Znamená uspořádat informace jako cestu od situace přes překážku a vysvětlení k výsledku.

Před návrhem vzhledu pomáhá formulovat jednu větu: „Po této prezentaci má publikum pochopit, že…“ Každý snímek potom obhajuje své místo. Pokud nepodporuje cíl, může patřit do poznámek, přílohy nebo být odstraněn.

## 5.2 Vizuální hierarchie, typografie a barva

Čitelnost vzniká kontrastem, velikostí, prostorem a konzistencí. Nadpis musí být rozpoznatelný, nejdůležitější prvek nesmí soupeřit s pěti stejně výraznými ozdobami a text musí být dost velký pro poslední řadu. Neexistuje univerzální minimální velikost písma pro každou místnost a displej; rozhoduje pozorovací vzdálenost, rozlišení a množství obsahu. Správný test je zobrazit snímek v cílovém prostředí.

Jednotná sada písem, barev, okrajů a stylů snižuje kognitivní zátěž. Pravidlo „nejvýše tři barvy“ může začátečníkovi pomoci, ale důležitější je funkční barevný systém a dostatečný kontrast. Barevný význam nesmí být jediným nositelem informace: červená a zelená čára v grafu potřebují také rozdílný styl nebo popisek.

Populární tvrzení, že modrá vždy znamená důvěru a červená vášeň, je příliš zjednodušené. Význam barvy závisí na kultuře, kontextu, odstínu a kombinaci s dalšími prvky. Při návrhu je spolehlivější ptát se, zda barva vytváří hierarchii, zachovává čitelnost a odpovídá obsahu.

Obrázek má mít sdělovací roli. Ilustrační fotografie může vytvořit atmosféru, diagram vysvětlit mechanismus a graf podpořit tvrzení daty. Dekorativní směs ikon a fotografií bez vztahu k výkladu pozornost spíše rozptyluje. U grafu je často účinnější zvýraznit jednu důležitou řadu a přímo ji popsat než ukázat výchozí legendu s mnoha barvami.

## 5.3 Animace, video a interaktivita

Animace je užitečná, když ukáže změnu v čase, sestavení systému nebo vztah částí. Postupné odhalení diagramu může řídit pozornost, ale náhodné přílety textu a otáčení objektů prodlužují prezentaci bez informační hodnoty. Stejně jako střihový přechod má animace vysvětlovat, ne dokazovat, že software nabízí efekty.

Vložené video může ukázat experiment, postup nebo výpověď, kterou statický snímek nepřenese. Před vystoupením je třeba ověřit kodek, zvuk, internetové připojení a způsob spuštění. Kritický klip je bezpečnější mít lokálně a se záložní variantou. Během přehrávání má být jasné, na co se publikum dívá a jak dlouhý úsek skutečně potřebuje.

Interaktivita má smysl, pokud mění roli publika z pasivního příjemce na účastníka myšlení. Krátká otázka před vysvětlením odhalí představy, hlasování umožní porovnat názory a společná tabule zachytí návrhy. Kvíz není automaticky výuka; otázka musí souviset s cílem a odpověď potřebuje zpětnou vazbu.

Formát se volí podle situace. Snímková prezentace podporuje živý výklad, automatická prezentace musí být srozumitelnější sama o sobě, interaktivní panel dovoluje nelineární průchod a **screencast** ukazuje dění na obrazovce v čase. Myšlenková mapa je dobrá pro hierarchii a vztahy, infografika pro koncentrované vizuální vysvětlení. Není účelné převést každý obsah do každého formátu.

Prostorová média, 360° video a virtuální realita mohou dát publiku možnost rozhlížet se nebo jednat uvnitř simulovaného prostředí. Hodí se například pro výcvik, prohlídku místa nebo bezpečný nácvik situace. Současně mění způsob vyprávění: autor už nemá plnou kontrolu nad směrem pohledu, musí řešit orientaci, ovládání, výkon i riziko nevolnosti. Působivost technologie proto sama o sobě nestačí jako výukový důvod.

## 5.4 Technika vystoupení a záložní plán

Projektor nebo displej má jiné podání barev, jas a poměr stran než notebook. Příliš jemné čáry, slabý kontrast a drobný text se mohou ztratit. Před prezentací proto ověříme výstupní rozlišení, zvuk, kabely či bezdrátové připojení a vypneme rušivá oznámení. Prezentační ovladač dovolí řečníkovi pohyb, ale laserové ukazovátko nemá nahrazovat jasnou grafiku.

Technická jistota nevznikne přidáním dalšího zařízení, ale zkouškou a zálohou. Praktické minimum tvoří lokální kopie, export do PDF pro případ problémů s fonty či animacemi a možnost pokračovat i bez internetu. U videokonference navíc kontrolujeme sdílení správného okna, čitelnost na malých obrazovkách, mikrofon a to, zda publikum skutečně slyší systémový zvuk.

Přednes doplňuje vizuální návrh. Tempo, pauza, intonace, oční kontakt a práce s otázkami nemůže šablona vygenerovat za řečníka. Zkouška nahlas odhalí příliš dlouhé části, nejasné přechody i snímky, které vyžadují několik minut vysvětlování. Dobrá prezentace je scénář společné pozornosti, nikoli soutěž v počtu funkcí.

# 6. E-learning, umělá inteligence a důvěra v multimédia

## 6.1 Od živého výkladu k učebnímu prostředí

**E-learning** spojuje digitální obsah, komunikaci, aktivitu a zpětnou vazbu. Synchronní forma probíhá společně v čase, například při živé videolekci. Asynchronní forma umožní pracovat vlastním tempem s textem, videem, úlohami a diskusí. Obě lze kombinovat: samostudium připraví základ a společné setkání se věnuje otázkám, procvičení nebo spolupráci.

**LMS - Learning Management System** organizuje kurzy, účastníky, úkoly, testy a výsledky. Standardy a balíčky, například SCORM, pomáhají přenášet obsah a zaznamenávat vybrané interakce mezi různými systémy; interaktivní moduly H5P umožňují skládat otázky, videa a další aktivity. Technická kompatibilita však sama nezaručuje dobrou výuku. Video bez cíle a zpětné vazby zůstane videem, i když je vloženo do LMS.

Učební objekt má vést k činnosti. Krátké vysvětlení může následovat předpověď výsledku, manipulace s modelem, rozhodnutí v situaci nebo vlastní tvorba. Okamžitá zpětná vazba má vysvětlit, proč byla odpověď správná či chybná, ne pouze přidělit bod. Multimédia pomáhají tehdy, když různé kanály nesou doplňující se informaci; současně čtený odstavec, stejný hlasový komentář a rušivá animace mohou učení zhoršit.

## 6.2 Screencast jako malá video lekce

Screencast kombinuje záznam obrazovky, komentář, kurzor a někdy obraz kamery. Dobře se hodí pro postup v programu, protože ukazuje nejen výsledek, ale i pořadí akcí. Musí však být navržen stejně pečlivě jako jiné video. Nejdříve určíme jeden dosažitelný cíl, připravíme čisté prostředí bez osobních údajů, zvětšíme důležité prvky a odstraníme čekání či bloudění.

Komentář nemá pouze číst názvy tlačítek. Má vysvětlit záměr a rozhodování: proč danou volbu používáme, jak poznáme správný výsledek a jakou chybu čekat. Krátké kapitoly a titulky usnadní návrat ke konkrétnímu kroku. Jestliže se rozhraní často mění, je někdy trvanlivější vysvětlit princip a detailní klikací návod oddělit do snadno aktualizovatelné části.

## 6.3 AI jako pomocník ve výrobním řetězci

Umělá inteligence může zasáhnout téměř do každé fáze. Při přípravě navrhne varianty osnovy, shrne podklady nebo pomůže vytvořit storyboard. Při postprodukci přepíše řeč, navrhne střih podle přepisu, vyhledá záběry, odstraní pozadí, přeloží titulky nebo syntetizuje hlas. Generativní model může ze slovního zadání vytvořit obraz, hudbu, animaci či celý videoklip.

Nejlepší mentální model není „AI udělá video“, ale „AI vytváří návrhy a odhady uvnitř konkrétního workflow“. Automatický přepis může přesvědčivě zaměnit jméno, generované pozadí změnit tvar produktu a překlad posunout význam. Upscaling či dopočítávání snímků nevytáhne z původního souboru tajné ztracené detaily; model vytvoří pravděpodobnou rekonstrukci. Pro umělecký výsledek může být skvělá, pro důkazní nebo vědecký záznam musí být jasně označena.

Při AI lokalizaci se propojí přepis, překlad, syntéza řeči a někdy úprava pohybu rtů. Výsledek může zpřístupnit obsah více lidem, současně však musí respektovat souhlas mluvčího, autorská práva a význam originálu. Realistický hlas ani přesný pohyb rtů už nejsou důkazem, že člověk danou větu skutečně pronesl.

## 6.4 Personalizace není totéž co kvalitní učení

AI tutor může vysvětlit pojem jiným příkladem, vytvořit procvičovací otázky nebo nabídnout nápovědu podle předchozí odpovědi. Adaptivní systém může změnit pořadí a obtížnost úloh. Taková personalizace je užitečná, pokud vede ke stejnému ověřitelnému cíli a pokud člověk rozumí, proč dostává určité doporučení.

Rizikem je přesvědčivá chyba, příliš snadná nápověda nebo hodnocení podle neprůhledných znaků. Analýza kliknutí a času v kurzu také neměří porozumění přímo. Člověk může dlouho tápat nebo naopak rychle využít dřívější znalost. Proto mají výsledky podporovat pedagogické rozhodnutí, nikoli automaticky nálepkovat schopnosti.

Při tvorbě testu může AI urychlit první návrh, ale autor musí zkontrolovat faktickou správnost, jednoznačnost, náročnost i to, zda otázka opravdu měří zamýšlenou dovednost. Náhodně vytvořený kvíz z textu může zvýšit počet interakcí, aniž by zlepšil pochopení.

## 6.5 Původ média a otázka důvěry

Digitální video lze sestříhat, přerámovat, zpomalit, doplnit syntetickým hlasem nebo celé vygenerovat. Samotný realistický vzhled proto není dostatečný důkaz pravosti. Důvěryhodnost posuzujeme podle původu, kontextu, historie úprav, nezávislého potvrzení a motivace zdroje.

Technologie **Content Credentials** založená na standardu C2PA může k médiu kryptograficky připojit informace o jeho původu a některých úpravách. Je užitečné představit si ji jako dohledatelnou historii, nikoli jako detektor pravdy. Záznam může pomoci ověřit, odkud soubor pochází a čím prošel, ale sám nezaručuje, že zachycená událost nebyla naaranžovaná nebo že tvrzení ve videu je pravdivé. Chybějící údaje také automaticky nedokazují podvod.

Při ověřování podezřelého videa proto hledáme původní zveřejnění, celé nezkrácené znění, datum a místo, další záznamy stejné události a důvěryhodnost autora. Kontrolujeme, zda zvuk odpovídá obrazu a zda titulek nevkládá scéně jiný význam. AI detektor může být jedním signálem, neměl by být jediným rozhodčím.

# Závěrečné propojení

Digitální video začíná fyzickou scénou. Světlo projde objektivem, snímač je převede na elektrické hodnoty a obrazový procesor vytvoří řadu digitálních snímků. Kodek zmenší jejich datovou náročnost, kontejner spojí obraz se zvukem, titulky a metadaty a postprodukce z materiálu sestaví sdělení. Distribuční systém pak připraví varianty, které se přizpůsobují síti a zařízení diváka.

Multimediální prezentace používá stejné stavební prvky, ale její kvalita nevzniká jejich počtem. Text, obraz, zvuk, video, animace a interaktivita musí mít rozdělené role a společný komunikační cíl. E-learning k nim přidává aktivitu, zpětnou vazbu a sledování pokroku. Umělá inteligence může celý řetězec urychlit a rozšířit, zároveň však zvyšuje potřebu kontroly, souhlasu a ověřování původu.

Celý okruh lze shrnout dvěma navazujícími cestami:

**scéna → světlo a zvuk → digitalizace → komprese a kontejner → střih → distribuce → obraz a zvuk pro diváka**

**záměr → struktura sdělení → volba médií → prezentace nebo kurz → aktivita publika → zpětná vazba a porozumění**

Nejdůležitější není zapamatovat si nejdelší seznam kodeků, kamer nebo prezentačních aplikací. Podstatné je rozlišit, co bylo zachyceno, jak je informace reprezentována, co se při kompresi či úpravě změnilo, jak technická volba slouží sdělení a podle čeho lze výslednému médiu důvěřovat.
