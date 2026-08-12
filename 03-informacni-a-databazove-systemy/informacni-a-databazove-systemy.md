# Informační a databázové systémy

## Modernizovaný výukový text

> Informační systém není jen program a databáze není jen soubor tabulek. Informační systém propojuje lidi, pravidla, procesy, data a techniku tak, aby organizace dokázala vykonávat svou činnost a rozhodovat se. Databázový systém je jednou z jeho důležitých technických částí: data ukládá, zpřístupňuje, chrání a umožňuje je hromadně zpracovávat.

K výkladu se budeme vracet k modelové škole. Ta používá systém pro evidenci žáků, elektronickou žákovskou knížku, knihovnu, rezervaci učeben, správu účtů i ekonomickou agendu. Každý z těchto systémů řeší jiný úkol, ale systémy si zároveň předávají data. Když nastoupí nový žák, nemá správce jeho jméno ručně opisovat do pěti aplikací. Správně navržený tok dat založí potřebné účty, přiřadí oprávnění a poskytne učitelům jen ty informace, které skutečně potřebují.

První tři lekce se soustředí na informační systémy jako celek: jejich smysl, typy, uživatele, vznik, nasazení a správu. Další tři lekce vysvětlí databáze, moderní NoSQL modely, velká data a datové sklady. Relační databáze a jazyk SQL zde tvoří pouze nezbytný kontext, protože jejich podrobnému návrhu a používání je věnován samostatný tematický okruh.

# 1. Informační systémy v digitální době

## 1.1 Od dat k informaci a rozhodnutí

Zápis `U-204` je sám o sobě pouze údaj. Teprve kontext prozradí, že jde o učebnu číslo 204. Když jej systém spojí s rozvrhem, kapacitou místnosti a stavem vybavení, vzniká informace: učebna je ve středu třetí hodinu volná a lze v ní uspořádat seminář pro dvacet lidí. **Data** jsou zaznamenané hodnoty, znaky nebo měření. **Informace** vzniká, když data vyložíme v určité souvislosti a můžeme podle nich jednat. Zpracovaná informace se může stát podkladem pro znalost a rozhodnutí.

**Informační systém — IS** je uspořádaný celek, který data získává, přenáší, zpracovává, ukládá a předává lidem nebo dalším systémům. Jeho hlavním účelem je podporovat konkrétní činnost: obsloužit zákazníka, řídit výrobu, vyplatit mzdu, vydat občanský průkaz, evidovat léčbu nebo naplánovat dopravu. Dobře fungující IS omezuje zbytečné opisování, hlídá pravidla, zpřístupňuje správnou informaci oprávněnému uživateli a vytváří podklady pro kontrolu a rozhodování.

Informační systém nemusí být počítačový. Kartotéka, formuláře a dohodnutý postup mohou také tvořit systém práce s informacemi. V digitální době však většinu rozsáhlejších systémů podporují počítače a sítě. Samotná aplikace přesto není celý IS. Pokud školní software umí zapsat absenci, ale učitelé nevědí, kdo ji má omlouvat, nebo si vedou paralelní soukromé seznamy, selhává proces a organizace, nikoli nutně program.

## 1.2 Komponenty informačního systému

Užitečný mentální model tvoří pět vzájemně závislých složek: **lidé, procesy, data, software a technická infrastruktura**.

**Lidé** do systému vstupují v různých rolích. Koncový uživatel zadává údaje nebo čte výsledek, vedoucí sleduje ukazatele, analytik hledá souvislosti, správce nastavuje účty a vývojář systém mění. Lidé také nesou odpovědnost za rozhodnutí. Automatické doporučení může pomoci lékaři či úředníkovi, ale u závažného rozhodnutí nemá zakrýt, kdo výsledek posoudil.

**Procesy** popisují, co se má stát a v jakém pořadí. Při přijetí žáka se například ověří doklady, založí záznam, přiřadí třída a vytvoří školní účet. Proces obsahuje i výjimky: co když už účet existuje nebo jsou údaje neúplné? Digitalizace špatně navrženého procesu může pouze zrychlit vznik chyb.

**Data** zachycují stav sledované skutečnosti. Musí mít známý význam, původ, formát a přiměřenou kvalitu. Chybně zadané datum narození může ovlivnit přístup ke službě i statistiku. **Software** provádí pravidla, nabízí uživatelské rozhraní a propojuje systém s okolím. **Infrastruktura** zahrnuje koncová zařízení, servery, úložiště, síť, cloudové služby a prostředky zabezpečení.

Tyto složky nelze hodnotit odděleně. Rychlá databáze nepomůže, když zaměstnanci sdílejí hesla. Přehledné rozhraní nezachrání proces, který nutí člověka zadávat stejný údaj třikrát. A detailní report je bezcenný, pokud vedení neví, podle jaké definice se počítá jeho ukazatel.

## 1.3 Tok dat: vstup, zpracování, výstup a zpětná vazba

Činnost IS lze popsat jako tok. **Vstupem** do knihovního systému je identita čtenáře a kód výtisku. Při **zpracování** systém ověří oprávnění, zjistí dostupnost knihy, založí výpůjčku a vypočítá datum vrácení. **Výstupem** je potvrzení pro žáka a změněný stav výtisku. **Zpětná vazba** upozorní na neobvyklý stav nebo pomůže proces upravit; například statistika ukáže, že se povinná četba vrací pozdě, protože je výpůjční lhůta příliš krátká.

Do toku patří také kontrola. Systém může ověřit, zda je povinné pole vyplněno, zda číslo dává smysl a zda má uživatel právo operaci provést. Kontrola však nesmí být slepá. Pokud formulář odmítá správnou zahraniční adresu jen proto, že očekává české PSČ, technické pravidlo zkresluje skutečnost.

Moderní IS obvykle není izolovaný. Školní aplikace může čerpat identity z adresářové služby, rozvrh z jiného systému a upozornění odesílat přes e-mailovou službu. Komunikaci umožňuje **API — aplikační programové rozhraní** nebo pravidelný import a export souborů. Integrace snižuje duplicity, ale vytváří závislosti. Když se změní význam položky nebo vypadne služba, musí být zřejmé, který systém je autoritativním zdrojem a jak se chyba napraví.

## 1.4 Veřejné a firemní informační systémy

Ve veřejném sektoru podporují IS služby, na které má občan právní nárok nebo povinnost. Patří sem evidence obyvatel, daňové systémy, katastr nemovitostí, elektronické podání, zdravotnické systémy či registr vozidel. U takových systémů je zásadní dostupnost, správnost, dohledatelnost změn, ochrana citlivých údajů a možnost nápravy. Uživatel si často nemůže vybrat konkurenční službu, a proto musí být systém navržen také pro lidi s různými schopnostmi a technickým vybavením.

Firemní IS podporují prodej, nákup, výrobu, logistiku, finance, personalistiku nebo kontakt se zákazníkem. V e-shopu například objednávka projde přes katalog, platbu, sklad, expedici, účetnictví a zákaznickou podporu. Z pohledu kupujícího jde o jeden nákup, uvnitř firmy se však předává mezi několika subsystémy. Chyba na rozhraní se projeví jako prodané zboží, které ve skladu není, nebo jako zaplacená objednávka bez pokynu k expedici.

Rozdíl mezi veřejným a firemním systémem není v použité databázi. Liší se především účelem, odpovědností, právním rámcem, okruhem uživatelů a následky selhání. Nemocniční IS i internetový obchod mohou používat podobné technické komponenty, ale výpadek nebo únik dat má v každém prostředí jinou závažnost.

## 1.5 Od provozních dat k business intelligence

Provozní systém zaznamenává jednotlivé události: objednávky, platby, absence nebo výpůjčky. Vedení však obvykle nepotřebuje číst tisíce záznamů. Ptá se, zda roste počet reklamací, kde vznikají zpoždění nebo které učebny jsou dlouhodobě nevyužité. **Business intelligence — BI** je soubor postupů a nástrojů, které převádějí data na přehledy, ukazatele a analýzy podporující rozhodování.

Data se obvykle převezmou z více zdrojů, sjednotí se jejich význam a zobrazí se v reportu nebo interaktivním přehledu. BI může upozornit na odchylku, umožnit porovnání období a rozbalit souhrn do detailu. Nezajišťuje však automaticky pravdivý závěr. Graf počtu absencí může být přesný, a přesto zavádějící, pokud se meziročně změnil způsob evidence. Kvalitní BI proto vyžaduje známý původ dat, jednotné definice ukazatelů a člověka, který rozumí kontextu.

**Hlavní myšlenka:** Informační systém převádí data na činnost a rozhodnutí. Jeho kvalita závisí na shodě mezi lidmi, procesy, daty a technikou, nikoli pouze na vlastnostech programu.

# 2. Typy informačních systémů

## 2.1 Systémy podle úrovně řízení

Tradiční manažerská pyramida rozlišuje systémy podle toho, jaké otázky řeší a kdo je používá. Na provozní úrovni vzniká velké množství konkrétních záznamů. Střední řízení sleduje průběh činnosti a odchylky. Vrcholové vedení pracuje s dlouhodobými souhrny, scénáři a nejistotou. Hranice nejsou ostré a jeden moderní produkt může obsahovat více vrstev, ale rozdělení pomáhá pochopit odlišné potřeby uživatelů.

**Transakční informační systém — TPS, Transaction Processing System** zachycuje jednotlivé události. V bance připíše platbu, v obchodě zaúčtuje prodej, v hotelu vytvoří rezervaci a ve škole zapíše klasifikaci. Uživatelé jsou především pracovníci provozu a zákazníci v samoobslužném rozhraní. TPS musí být rychlý, přesný a spolehlivý. Při prodeji poslední vstupenky nesmí dvě souběžné operace potvrdit stejné místo.

**Manažerský informační systém — MIS, Management Information System** vytváří pravidelné souhrny pro vedoucí provozu. Mistr ve výrobě vidí zmetkovitost podle směn, vedoucí prodejny obrat a stav zásob, ředitel školy absence podle tříd. MIS často upozorňuje na výjimky: hodnota překročila mez, výkon zaostal za plánem nebo úkol nebyl dokončen. Smyslem není zobrazit všechna data, ale umožnit rychlé řízení opakujících se situací.

**Systém pro podporu rozhodování — DSS, Decision Support System** pomáhá u méně rutinních otázek. Kombinuje data, modely a varianty typu „co se stane, když“. Dopravní podnik může porovnat několik návrhů linek podle nákladů, vytížení a dostupnosti. Banka může modelovat úvěrové riziko a výrobce důsledky změny dodavatele. DSS nerozhoduje sám; ukazuje scénáře, předpoklady a citlivost výsledku na změnu vstupů.

**Systém pro podporu vrcholového řízení — EIS/ESS** nabízí strategické ukazatele v agregované podobě. Vedení sleduje dlouhodobý vývoj, rizika, kapacity a vztah k okolnímu trhu. Typickým výstupem je manažerský dashboard, ale pěkný panel není důkazem kvalitního systému. Rozhodující je, zda lze ukazatel vysvětlit a dohledat k důvěryhodným zdrojům.

## 2.2 Podnikové systémy: ERP, CRM a řízení dodavatelského řetězce

**ERP — Enterprise Resource Planning** integruje klíčové podnikové oblasti, například finance, nákup, sklad, výrobu, prodej a personalistiku. Představme si výrobní firmu bez společného systému: obchodník slíbí termín, aniž zná zásoby; výroba dostane změnu objednávky e-mailem; účetní pracuje s původní cenou. ERP vytvoří společný tok. Přijatá objednávka ovlivní plán materiálu, výrobu, expedici i fakturaci a změna zůstane dohledatelná.

Výhodou ERP je jednotnější význam dat a omezení ručního přepisování. Nevýhodou bývá náročné zavedení. Organizace musí rozhodnout, zda přizpůsobí procesy standardnímu produktu, nebo draze upraví produkt svým zvyklostem. Snaha zachovat v novém ERP všechny historické výjimky může pouze zakonzervovat špatné postupy.

**CRM — Customer Relationship Management** podporuje vztahy se zákazníky. Obchodník vidí kontakty, nabídky, historii komunikace a další dohodnutý krok; servisní pracovník zná předchozí reklamace; marketing vyhodnocuje kampaně. CRM má uživateli pomoci navázat na skutečnou historii, ne vytvořit dojem vševědoucího sledování. Použití údajů musí odpovídat účelu, o němž zákazník ví, a přístup má mít jen oprávněná role.

**SCM — Supply Chain Management** podporuje dodavatelský řetězec od nákupu přes sklad a dopravu po předání zákazníkovi. Maloobchodní síť může propojit prodejní data s předpovědí poptávky a včas doplnit zásoby. Přehnaně optimalizovaný řetězec bez rezerv je však křehký: krátkodobě snižuje náklady, ale při výpadku dodavatele nemá kam sáhnout. IS proto podporuje rozhodnutí, které stále obsahuje obchodní kompromis.

## 2.3 Oborové systémy a konkrétní využití

**Geografický informační systém — GIS** propojuje data s polohou. Město v něm eviduje sítě, pozemky a dopravní omezení; hasiči plánují dojezd; zemědělec porovnává stav půdy a vegetace; logistická firma optimalizuje trasy. GIS nepracuje jen s obrázkem mapy. Ukládá objekty, jejich vlastnosti a prostorové vztahy, takže lze vyhledat například školy v určité dojezdové vzdálenosti od nové autobusové linky.

**Nemocniční a zdravotnické IS** spojují objednávání, dokumentaci, laboratorní výsledky, medikaci, vykazování a správu lůžek. Lékař potřebuje rychlý a úplný pohled na konkrétního pacienta, vedení sleduje kapacity a zdravotní pojišťovna kontroluje vykázanou péči. Stejná data tak používají různé role k jinému účelu. Proto jsou zásadní oprávnění, audit změn a rozlišení mezi léčbou, administrativou a výzkumem.

**Školní informační systém** spravuje žáky, třídy, rozvrh, hodnocení, docházku a komunikaci. Učitel zapisuje hodnocení, žák sleduje vlastní výsledky, rodič údaje svého dítěte a vedení souhrny. Správně nastavené role zabrání tomu, aby třídní učitel omylem viděl citlivé údaje celé školy. Propojení s adresářovou službou může automaticky vytvořit a po odchodu také zrušit účet.

Veřejná správa používá **správní a evidenční systémy** pro agendy obyvatel, daní, vozidel, stavebních řízení či sociálních dávek. Důležitá je právní platnost úkonu, identifikace osoby, zaznamenání času a možnost přezkumu. Uživatel musí rozumět tomu, co odesílá, a nesmí být vyloučen jen kvůli nepřístupnému rozhraní.

## 2.4 Kancelářské, komunikační a znalostní systémy

**Kancelářské a kolaborační systémy** podporují tvorbu dokumentů, sdílení souborů, komunikaci, kalendáře a pracovní postupy. Jejich přínos není v tom, že nahradí papír obrazovkou, ale že umožní společnou práci, verzování, vyhledávání a schvalování. Bez dohodnutých pravidel však vzniknou desítky kopií souboru a důležitá rozhodnutí zůstanou v soukromých chatech.

**Systémy pro správu dokumentů — DMS** evidují dokument jako řízený objekt. Uchovávají metadata, verze, oprávnění, schvalovací stav a dobu uchování. Elektronická faktura tak není jen PDF ve složce; je spojena s dodavatelem, objednávkou, schválením a účetním záznamem. **Systémy pro řízení obsahu — CMS** se zaměřují na publikování obsahu, například webu nebo intranetu.

**Znalostní a expertní systémy** uchovávají a zpřístupňují odborné znalosti. Klasický expertní systém používá znalostní bázi a pravidla typu „jestliže–pak“. Servisní technik může podle příznaků dohledat pravděpodobnou příčinu poruchy a systém umí ukázat postup odvození. Model strojového učení se naproti tomu učí vzory z příkladů a často vrací pravděpodobnost. Současné systémy oba přístupy kombinují, například pravidla vymezí bezpečné hranice a model seřadí doporučení. Umělá inteligence ale může chybovat, přebírat zkreslení tréninkových dat a vytvářet přesvědčivě znějící nepravdy. Výstup musí být ověřitelný přiměřeně závažnosti rozhodnutí.

## 2.5 Jeden systém může patřit do více kategorií

Kategorie se překrývají. E-shop je TPS při přijetí objednávky, CRM při práci se zákazníkem, SCM při doplňování zásob a zdroj BI při vyhodnocení prodeje. ERP může obsahovat transakční i manažerské moduly. GIS může sloužit operátorovi záchranné služby i strategickému plánování kraje.

Při určování typu je proto lepší položit čtyři otázky: kdo systém používá, jaký problém řeší, s jak podrobnými daty pracuje a jaký druh rozhodnutí podporuje. Název produktu je méně důležitý než skutečná funkce. Tím se vyhneme omylu, že každá organizace potřebuje samostatný program pro každou zkratku.

**Hlavní myšlenka:** Typ IS určuje především úloha a uživatel. Provozní systémy zaznamenávají události, manažerské systémy hlídají chod organizace a rozhodovací systémy pomáhají volit mezi variantami; podnikové a oborové systémy tyto vrstvy propojují.

# 3. Životní cyklus informačního systému

## 3.1 Od skutečné potřeby k požadavkům

Životní cyklus IS začíná ještě před programováním. Organizace nejprve vymezí problém a cíle. Věta „chceme moderní aplikaci s AI“ není použitelný cíl. Lepší požadavek zní: „Žák musí na jednom místě zjistit, zda je učebna volná, a oprávněný pracovník musí dohledat, kdo rezervaci změnil.“ První část popisuje funkci, druhá auditní a bezpečnostní vlastnost.

Analytik zjišťuje potřeby rozhovory, pozorováním práce, studiem dokumentů a modelováním procesů. Hledá také výjimky: co když se rezervace překrývají, učebna je náhle mimo provoz nebo uživatel odejde ze školy? **Funkční požadavky** určují, co má systém dělat. **Nefunkční požadavky** popisují například rychlost, dostupnost, bezpečnost, přístupnost a obnovitelnost. Požadavek „systém bude rychlý“ nelze dobře ověřit; měřitelná odezva při očekávané zátěži už testovat jde.

Součástí úvodního rozhodování je proveditelnost. Organizace porovnává přínosy, náklady, rizika, čas, dostupné lidi a právní omezení. Někdy není nejlepším řešením nový software, ale zjednodušení procesu nebo lepší použití existujícího systému.

## 3.2 Návrh, realizace a ověřování

Při návrhu se potřeba převádí do modelu procesů, dat, uživatelských rolí a technické architektury. Rozhoduje se, které části budou ve webové či mobilní aplikaci, kde budou pravidla, jak se systém spojí s okolím a jak bude chráněn. Prototyp může odhalit, že uživatelé rozumějí procesu jinak, než předpokládala specifikace.

Následuje realizace: konfigurace hotového produktu, programování vlastního řešení nebo jejich kombinace. Vývoj může probíhat sekvenčně, kdy se fáze uzavírají postupně, nebo iterativně v menších cyklech. Iterace umožní dříve získat zpětnou vazbu, ale neznamená práci bez plánu a dokumentace.

Testování neověřuje jen to, zda lze kliknout na tlačítko. Jednotkové testy kontrolují menší části, integrační testy komunikaci komponent, systémové testy celek a uživatelské akceptační testy skutečné scénáře. Zkouší se výkon, přístupová práva, obnova po chybě i přístupnost. Úspěšný běžný scénář nestačí: zvlášť důležité jsou souběžné operace, neúplná data a výpadky okolních služeb.

## 3.3 Nasazení není pouhé zapnutí programu

Při nasazení se řešení přesouvá do skutečného provozu. Je třeba připravit infrastrukturu, účty, podporu, návody a školení. Kritickým bodem bývá **migrace dat** ze starého systému. Staré údaje mohou mít duplicity, nejednotné kódy nebo chybějící význam. Bez čištění bychom do nové aplikace pouze přenesli staré problémy.

Základní strategie přechodu jsou čtyři. Při **přímém přechodu** se starý systém vypne a nový začne fungovat v určený okamžik. Je rychlý, ale rizikový. **Paralelní provoz** po omezenou dobu udržuje oba systémy; usnadňuje kontrolu, ale stojí více práce a hrozí rozcházení zápisů. **Pilotní nasazení** začne v jedné části organizace a zkušenost se využije před rozšířením. **Postupné nasazení** zapíná jednotlivé moduly nebo skupiny uživatelů po etapách.

Volba závisí na následcích chyby a možnosti návratu. U školní rezervace učeben lze tolerovat krátké omezení, u nemocniční medikace nebo bankovních plateb musí být přechod podstatně přísnější. Před spuštěním se stanoví podmínky úspěchu, odpovědnosti, komunikační plán a **rollback**, tedy postup návratu k bezpečnému stavu.

Uživatelé musí rozumět nejen tlačítkům, ale i změně procesu. Odpor často nevzniká z neochoty učit se, nýbrž z toho, že systém přidává práci nebo neřeší skutečnou potřebu. Zpětná vazba uživatelů je proto součástí nasazení, nikoli překážkou projektu.

## 3.4 Provoz, údržba a bezpečnost

Provoz bývá nejdelší a často nejdražší část života IS. Správci sledují dostupnost, výkon, chybové stavy, využití kapacity a bezpečnostní události. **Incident** je konkrétní narušení služby, například nemožnost přihlášení. **Problém** je jeho hlubší příčina, například chybná synchronizace účtů. Rychlé obnovení služby a odstranění příčiny jsou dva rozdílné úkoly.

Údržba zahrnuje opravy chyb, bezpečnostní aktualizace, přizpůsobení změnám zákonů a procesů i rozvoj funkcí. Změna se má evidovat, posoudit, otestovat a teprve poté nasadit. Dokumentace musí zachytit architekturu, rozhraní, konfiguraci, role i postup obnovy. Dokument, který nikdo neaktualizuje, poskytuje při incidentu falešnou jistotu.

Bezpečnost stojí na více vrstvách. Uživatel se ověřuje, systém mu přidělí jen potřebná oprávnění a významné operace zapisuje do auditu. Data se chrání při přenosu i uložení. Zálohy musí být oddělené od běžného provozu a pravidelně se testuje obnova. Replikace může zvýšit dostupnost, ale není sama o sobě zálohou: chybně smazaná data se mohou okamžitě rozšířit na všechny repliky.

## 3.5 Vlastní vývoj, hotové řešení, cloud a outsourcing

Organizace může systém vyvíjet vlastními silami, koupit hotové řešení, objednat vývoj, využít cloudovou službu nebo přístupy kombinovat. **Vlastní vývoj** dává vysokou kontrolu a možnost přizpůsobení, ale vyžaduje schopný tým a dlouhodobou odpovědnost. **Hotové řešení — COTS** lze nasadit rychleji, avšak organizace se částečně přizpůsobuje produktu.

Při **outsourcingu** zajišťuje část vývoje nebo provozu externí dodavatel. Přináší odborné kapacity, ale odpovědnost organizace nezmizí. Smlouva musí vymezit dostupnost, podporu, zabezpečení, vlastnictví a přenositelnost dat, ukončení spolupráce i řešení incidentů. Kritické znalosti nemají zůstat pouze u jediné cizí firmy.

**SaaS — Software as a Service** zpřístupňuje hotovou aplikaci jako službu. Poskytovatel provozuje infrastrukturu a aktualizace, zákazník spravuje zejména konfiguraci, uživatele a data. Cloud neznamená „bez správy“. Stále je nutné nastavit role, vícefaktorové ověřování, uchování dat, integrace a plán pro výpadek či změnu dodavatele. Užitečná je **exit strategie**: jak organizace získá svá data v použitelném formátu a jak bude pokračovat jinde.

Životní cyklus končí řízeným vyřazením. Účty se zruší, potřebná data se archivují nebo bezpečně odstraní, integrace se odpojí a uživatelé přejdou na náhradu. Opuštěný systém bez aktualizací se rychle stává bezpečnostním i provozním rizikem.

**Hlavní myšlenka:** Úspěšný IS nevzniká jedním nákupem ani jedním projektem. Jeho životní cyklus zahrnuje potřebu, návrh, realizaci, testování, bezpečné nasazení, dlouhodobou správu a nakonec řízené vyřazení.

# 4. Databáze a hromadné zpracování dat

## 4.1 Databáze, DBMS a aplikace

**Databáze** je organizovaná kolekce souvisejících dat určená k dlouhodobému používání. **Systém řízení báze dat — DBMS, Database Management System** je software, který databázi vytváří, zpřístupňuje a chrání. Zajišťuje dotazování, změny, souběžný přístup, oprávnění, integritu a obnovu. **Databázový systém** tvoří databáze, DBMS, potřebná infrastruktura, pravidla a uživatelé. Aplikace nad ním nabízí funkce konkrétního IS.

Když žák v knihovní aplikaci vyhledá titul, formulář obvykle neotevírá databázový soubor přímo. Odešle požadavek aplikační vrstvě, ta ověří identitu a oprávnění, provede dotaz přes databázový ovladač nebo API a výsledek převede do podoby stránky. Zápis výpůjčky navíc musí respektovat pravidla: výtisk je dostupný, čtenář má aktivní účet a operace se provede jako celek.

Databáze se používá proto, že běžný soubor obtížně zvládá mnoho souběžných uživatelů, vztahy mezi záznamy, řízení přístupu a spolehlivou obnovu. Tabulkový procesor je výborný pro menší analýzu, ale sdílený sešit s tisíci zákazníků není náhradou za provozní databázi. Naopak malý osobní seznam nemusí získat nic tím, že jej zbytečně přesuneme do složitého serverového DBMS.

## 4.2 Od předrelačních k postrelačním databázím

Historické **hierarchické databáze** organizovaly záznamy jako strom rodičů a potomků. Dobře odpovídaly situacím s přirozenou a stabilní hierarchií, ale složité vztahy mezi větvemi se vyjadřovaly obtížně. Princip přetrvává v adresářových službách, souborových stromech nebo dokumentech XML a JSON, i když jejich dnešní implementace nejsou prostým pokračováním původních DBMS.

**Síťový databázový model** dovoloval záznamu více vazeb a podporoval složitější struktury. Aplikační program však často musel znát cestu, po níž daty projde. Vývojář tedy nepopisoval jen požadovaný výsledek, ale navigoval mezi konkrétními záznamy. Tato těsná vazba ztěžovala změny struktury.

**Relační model** uspořádal data do relací, prakticky zobrazovaných jako tabulky, a oddělil logický dotaz od fyzického uložení. Vazby se vyjadřují klíči a data se zpracovávají deklarativním jazykem SQL. Relační databáze, například PostgreSQL, MySQL, Microsoft SQL Server nebo SQLite, zůstávají základní volbou pro mnoho transakčních aplikací, protože dobře podporují integritu, vztahy a transakce. Podrobný návrh tabulek, normalizace a SQL však patří do samostatného okruhu.

Označení **postrelační** není jeden přesný datový model. Používá se pro přístupy, které relační model rozšiřují nebo řeší potřeby, pro něž tabulky nejsou nejpřirozenější reprezentací. Patří sem objektově-relační rozšíření, objektové databáze a především různé NoSQL databáze. Moderní systémy se navíc ovlivňují: relační DBMS ukládají JSON a NoSQL produkty mohou podporovat transakce či dotazovací jazyky podobné SQL. Důležitější než nálepka je způsob modelování a typ požadovaných dotazů.

## 4.3 Datové modely a různé pohledy na stejnou skutečnost

**Datový model** určuje, z jakých stavebních prvků se data skládají, jaké vazby lze vyjádřit a jaké operace nad nimi systém provádí. Relační model používá tabulky a klíče, dokumentový model vnořené dokumenty, key-value model pár klíč–hodnota, grafový model uzly a hrany. Stejnou školní knihovnu lze popsat všemi těmito způsoby, ale každý zvýhodní jiné otázky.

V relační databázi lze oddělit tituly, fyzické výtisky, čtenáře a výpůjčky. Dokumentová databáze může uložit katalogový záznam s poli, autory a seznamem štítků v jednom dokumentu. Key-value databáze se hodí pro rychlé načtení relace přihlášeného uživatele podle náhodného klíče. Grafová databáze může sledovat vazby mezi knihami, tématy, autory a doporučeními. Volba není soutěž o „nejmodernější“ typ, ale rozhodnutí podle struktury dat, dotazů, objemu a provozních požadavků.

Vedle logického modelu rozlišujeme také fyzické uspořádání. **Řádkové uložení** drží hodnoty jednoho záznamu blízko sebe a hodí se pro časté čtení či změnu celých záznamů. **Sloupcové uložení** drží pohromadě hodnoty stejného sloupce a usnadňuje analytické součty nad mnoha řádky. Sloupcový analytický DBMS ale není totéž co NoSQL wide-column databáze; podobný název označuje jiný princip.

## 4.4 Uživatelé databáze a hromadné operace

Databázi nepoužívá jediný „uživatel“. Běžný uživatel pracuje přes formulář a databázi vůbec nemusí vidět. **Databázový administrátor — DBA** nastavuje účty, výkon, zálohy a obnovu. Vývojář vytváří aplikaci a dotazy, datový analytik zkoumá souhrny, datový inženýr připravuje přenosy a transformace. Vlastník dat rozhoduje o významu a oprávněném použití; správce technologie pouze neřeší obsahovou odpovědnost.

Podle přístupu rozlišujeme **jednouživatelské** a **víceuživatelské** databáze. SQLite v lokální aplikaci může sloužit jednomu uživateli bez samostatného serveru. Serverové DBMS obsluhují mnoho klientů současně a musí řešit souběh. Toto rozdělení neříká, jaký datový model databáze používá; popisuje provozní způsob přístupu.

Síla databáze se projeví při hromadném zpracování. Místo tisíce ručních změn lze jedním příkazem vybrat, agregovat nebo aktualizovat celou množinu záznamů. Hromadná operace je rychlá, ale chyba má také hromadný dopad. Před změnou je nutné ověřit podmínku, zajistit oprávnění, vytvořit možnost návratu a zaznamenat, co se provedlo. Automatizace násobí správný postup i omyl.

**Hlavní myšlenka:** Databáze poskytuje organizované a sdílené uložení dat, DBMS řídí práci s nimi a aplikace z nich vytváří konkrétní službu. Datový model se vybírá podle toho, jaká data máme a jaké otázky nad nimi potřebujeme řešit.

# 5. NoSQL databáze

## 5.1 Proč vzniklo „Not only SQL“

Označení **NoSQL** se používá pro skupinu nerelačních databázových modelů. Často se vykládá jako „Not only SQL“ — nejen SQL. Neznamená zákaz relačních databází, absenci dotazovacího jazyka ani databázi bez pravidel. NoSQL systémy vznikaly pro různé potřeby: pružně se měnící dokumenty, velmi rychlý přístup podle klíče, zápis obrovského proudu událostí, distribuci mezi mnoho uzlů nebo efektivní procházení vztahů.

Ani „bezschémová databáze“ není přesný popis. Dokumentová databáze může přijmout dokumenty s rozdílnými poli, aplikace však stále očekává určitý význam, typy a povinné údaje. Schéma nezmizelo; část odpovědnosti se přesunula do aplikace, validačních pravidel a správy dat. Pružnost urychlí změnu, ale bez disciplíny může vytvořit směs nekompatibilních záznamů.

NoSQL není automaticky rychlejší. Výkon závisí na konkrétní operaci, datovém modelu, indexech, distribuci a konfiguraci. Relační databáze může být nejlepší pro účetní transakce, dokumentová pro katalog proměnlivých produktů a grafová pro hledání vazeb. Často se používají vedle sebe v jedné aplikaci, což označujeme jako **polyglot persistence**.

## 5.2 Dokumentové databáze

**Dokumentová databáze** ukládá záznam jako dokument, obvykle ve struktuře podobné JSON. Dokument obsahuje pole, vnořené objekty a seznamy. MongoDB může například uložit katalogový záznam knihy spolu s autory, štítky, jazyky a různými vydáními. Dva dokumenty ve stejné kolekci nemusí mít vždy úplně stejná pole.

Základním návrhovým pravidlem je ukládat společně data, která aplikace často čte a mění společně. Detail produktu v e-shopu může obsahovat parametry, obrázky a varianty. Jediné načtení poskytne celou stránku. Vnoření však není vhodné bez omezení. Pokud se stejný autor opakuje v tisících dokumentů a jeho údaje se často mění, vznikají duplicity. Rozsáhlé vztahy mnoho ku mnoha mohou být přehlednější pomocí odkazů nebo jiného modelu.

Dokumentové databáze se hodí pro katalogy s různými vlastnostmi, profily, správu obsahu, události aplikace nebo rychle se vyvíjející webové služby. Výhodou je přirozená shoda s objekty používanými v programu a pružný vývoj schématu. Nevýhodou může být duplicita, složitější globální kontrola pravidel a nutnost navrhovat strukturu podle skutečných přístupových vzorů.

## 5.3 Key-value databáze

**Key-value databáze** funguje jako rozsáhlý slovník. Jedinečný klíč ukazuje na hodnotu a systém ji velmi rychle uloží nebo načte. Příkladem je Redis. Webová aplikace může pod náhodným klíčem uchovat stav přihlášení, obsah krátkodobé cache nebo čítač požadavků.

Síla jednoduchého modelu je zároveň jeho omezením. Když známe klíč, je přístup velmi rychlý. Pokud se ale chceme ptát na libovolnou vlastnost ukrytou uvnitř hodnoty, systém ji nemusí umět efektivně prohledat. Datový model proto vyžaduje předem vědět, jak budou data vyhledávána.

Key-value úložiště se používají pro relace uživatelů, mezipaměť, nákupní košíky, žebříčky nebo omezení počtu požadavků. U cache musí aplikace počítat s tím, že položka zmizí nebo bude zastaralá. Mezipaměť zrychluje přístup, ale nemá se bez dalšího stát jediným důvěryhodným zdrojem důležitých dat.

## 5.4 Wide-column databáze

**Wide-column databáze** organizuje data do řádků a sloupcových rodin, ale není to relační tabulka s libovolnými spojeními. Apache Cassandra rozděluje data podle klíče mezi uzly a modeluje tabulky podle dotazů, které musí systém rychle obsloužit. Jeden typ informace proto může být uložen více způsoby pro různé dotazy.

Představme si miliony měření ze senzorů. Častý dotaz zní: „Vrať všechna měření daného senzoru za konkrétní den v časovém pořadí.“ Vhodný klíč spojí identitu senzoru s časovým úsekem a data uvnitř oddílu seřadí podle času. Nevhodný klíč by vytvořil jediný obrovský oddíl nebo nerovnoměrně zatížil několik uzlů.

Wide-column systémy se hodí pro telemetrii, časové řady, komunikační události a služby s velmi vysokým objemem zápisů a požadavkem na geografickou dostupnost. Výhodou je horizontální škálování a odolnost proti výpadku uzlu. Cenou bývá méně pružné dotazování a potřeba znát přístupové vzory už při návrhu. Cassandra navíc není „sloupcový datový sklad“ v analytickém smyslu; jde o distribuovaný wide-column model určený především pro jiný druh zátěže.

## 5.5 Grafové databáze

**Grafová databáze** ukládá **uzly**, **vztahy** a jejich vlastnosti. V Neo4j může být uzlem člověk, kniha nebo téma a vztah může znamenat „četl“, „napsal“ či „souvisí s“. Vztah je plnohodnotná součást modelu, nikoli jen nepřímá shoda hodnot ve dvou tabulkách.

Graf je výhodný, když otázka vede přes řetězec vazeb: Kteří lidé jsou propojeni s podezřelou transakcí? Jaké přestupy spojují dvě zastávky? Které knihy četli lidé s podobným profilem? Kdo má v podnikové síti nepřímý přístup k citlivému prostředku? Délka a tvar cesty jsou často důležitější než součet sloupce.

Použití zahrnuje sociální a znalostní sítě, doporučování, detekci podvodů, správu závislostí a síťovou bezpečnost. Grafová databáze ale není automaticky nejlepší jen proto, že data obsahují vztahy — vztahy má téměř každá databáze. Výhodu získá tehdy, když je procházení mnoha proměnlivých vazeb hlavní částí dotazů.

## 5.6 Distribuce, konzistence a volba modelu

Distribuovaná databáze ukládá data na více uzlech. **Replikace** vytváří kopie pro dostupnost a odolnost, **partitioning neboli sharding** rozděluje data, aby se zátěž rozložila. Když se přeruší spojení mezi uzly, systém musí rozhodnout, zda některé operace odmítne ve prospěch silnější konzistence, nebo je přijme ve prospěch dostupnosti a kopie později sladí. CAP teorém se týká právě chování při síťovém rozdělení; neříká, že si databáze jednou provždy vybere pouze dvě libovolná písmena ze tří.

**Eventual consistency — výsledná konzistence** znamená, že kopie mohou být dočasně rozdílné, ale bez dalších změn se sjednotí. Pro počet reakcí u příspěvku může být krátké zpoždění přijatelné. Pro zůstatek při převodu peněz by mohlo být nebezpečné. Některé NoSQL systémy dovolují úroveň konzistence volit podle operace a moderní produkty často podporují i transakce. Nelze tedy tvrdit, že NoSQL vždy obětuje správnost.

Při volbě se nejprve ptáme na data a dotazy: Je struktura pravidelná? Které záznamy se čtou společně? Jsou nejdůležitější vazby? Jaký objem zápisu očekáváme? Jaké chyby lze tolerovat? Jak rychle se musí systém obnovit? Teprve potom se vybírá produkt. Školní systém může použít relační databázi pro výpůjčky, dokumentový index pro katalog, key-value cache pro relace a graf pro doporučování. Více technologií však zvyšuje nároky na provoz, zálohování i znalosti týmu, proto musí mít každá jasný důvod.

**Hlavní myšlenka:** NoSQL není jedna technologie ani náhrada všech relačních databází. Dokumentový, key-value, wide-column a grafový model řeší odlišné přístupové vzory a přinášejí vlastní výhody i omezení.

# 6. Big data a datové sklady

## 6.1 Kdy se z dat stávají big data

**Big data — velká data** nejsou určena pevným počtem gigabajtů. Jde o data, jejichž vlastnosti překračují možnosti běžné architektury a vyžadují jiné způsoby ukládání, přenosu nebo zpracování. Často se popisují pomocí „V“: **volume** označuje objem, **velocity** rychlost vzniku a příchodu, **variety** různorodost formátů. Doplňuje se **veracity**, tedy nejistá kvalita a důvěryhodnost, a **value**, skutečná hodnota pro daný účel.

Meteorologická služba přijímá proud měření ze stanic, radarů a družic; e-shop vytváří objednávky, kliknutí a provozní logy; město získává data z dopravy a senzorů. Velikost sama nestačí. Milion jednoduchých řádků může zvládnout běžný DBMS, zatímco rychlý proud různorodých událostí vyžaduje distribuované zpracování. Správná otázka tedy nezní „Kolik dat už je big data?“, ale „Která vlastnost dat nutí změnit architekturu?“

Ne všechna dostupná data je účelné shromažďovat. Uchování stojí peníze, zvětšuje bezpečnostní dopad úniku a může porušovat zásadu omezení účelu. Datová strategie má určit, proč údaj potřebujeme, jak dlouho jej uchováme a podle čeho poznáme jeho přínos.

## 6.2 Datový sklad sjednocuje historická data

**Datový sklad — data warehouse, DWH** je analytické úložiště, které integruje data z více zdrojů, sjednocuje jejich význam a uchovává historii. Provozní systémy školy evidují rozvrh, docházku, výsledky a provoz učeben každý po svém. Datový sklad může vytvořit společné dimenze času, třídy a předmětu, takže analytik porovnává údaje podle jedné definice.

Data se do skladu dostávají procesem **ETL — extract, transform, load**: nejprve se získají ze zdrojů, poté vyčistí a převedou a nakonec načtou do cíle. U varianty **ELT** se nejprve načtou a transformují až v cílové platformě. Ani jeden postup není automaticky lepší; volba závisí na prostředí, objemu a potřebě uchovat původní data.

Pro analytiku se často používá model faktů a dimenzí. **Faktová tabulka** obsahuje měřené události, například počet prodaných kusů a cenu. **Dimenze** popisují čas, produkt, zákazníka nebo pobočku. Takzvané hvězdicové schéma umožňuje snadno odpovídat na otázky typu „Jak se vyvíjel prodej dané kategorie podle měsíců a regionů?“ Jde o analytický model, nikoli o náhradu provozní databáze.

Vedle skladu se používá **data lake — datové jezero**, které uchovává velké množství strukturovaných i nestrukturovaných dat v méně předem upravené podobě. Je pružné pro další zpracování, ale bez katalogu, pravidel kvality a odpovědnosti se může změnit v nepřehlednou „datovou bažinu“. Moderní architektury někdy vlastnosti skladu a jezera kombinují; principem stále zůstává řízený původ, význam a kvalita dat.

## 6.3 OLTP a OLAP řeší jiné úkoly

Správná zkratka pro provozní zpracování je **OLTP — Online Transaction Processing**. OLTP obsluhuje velké množství krátkých operací nad aktuálními daty: vytvoření objednávky, změnu rezervace, výběr z účtu. Typický dotaz pracuje s několika záznamy, odezva má být krátká a změna spolehlivá.

**OLAP — Online Analytical Processing** slouží analytice. Čte velké množství historických záznamů, seskupuje je a porovnává podle více rozměrů. Vedoucí prodeje začne celkovým obratem, rozpadne jej podle regionu, přejde na měsíc a nakonec na produkt. Přechod ze souhrnu do detailu se označuje jako **drill-down**, opačný směr jako **roll-up**. Filtrování a výběr řezu dat umožňuje zkoumat stejnou skutečnost z různých úhlů.

OLTP databáze je navržena pro bezpečné změny během provozu; datový sklad a OLAP pro rozsáhlé čtení a agregaci. Pokud analytik spustí náročný souhrn přímo nad živou databází e-shopu, může zpomalit zákaznické objednávky. Oddělení zátěží proto chrání provoz a současně umožní uchovat historický stav, který se v běžném systému průběžně přepisuje.

## 6.4 Zpracování velkých dat

Velká data se často dělí mezi více počítačů. **Dávkové zpracování — batch processing** zpracuje větší celek najednou, například noční souhrn denních transakcí. Je efektivní, pokud výsledek nemusí vzniknout okamžitě. **Proudové zpracování — stream processing** vyhodnocuje události průběžně; používá se pro detekci podvodu, monitoring sítě nebo řízení výroby.

Distribuované zpracování přesouvá výpočet k částem dat a výsledky skládá. Platformy jako Apache Spark mohou provádět transformace a analýzy nad rozsáhlými datovými sadami. Sloupcové analytické databáze zase čtou jen potřebné sloupce a dobře je komprimují, takže rychle počítají souhrny. Cloud dovoluje dočasně přidat výkon, ale nezruší potřebu řídit náklady a bezpečnost.

Z dat lze získávat popisné statistiky, hledat skupiny, neobvyklé případy a vztahy nebo vytvářet predikční modely. **Data mining — dolování dat** označuje hledání užitečných vzorů ve velkých datech pomocí statistiky, databázových metod a strojového učení. Nalezený vzor však není automaticky příčina ani trvalé pravidlo. Model se musí ověřit na datech, na nichž se neučil, a sledovat i po nasazení, protože svět se mění.

## 6.5 Jak lze data zneužít

Velké soubory dat umožňují užitečné objevy, ale také rozsáhlé zásahy do soukromí. Propojením zdánlivě nevinných údajů lze znovu rozpoznat člověka, odvodit zdravotní stav, pohyb, sociální vztahy nebo finanční situaci. **Pseudonymizace** nahrazuje přímý identifikátor jiným, ale možnost zpětného spojení může zůstat. **Anonymizace** má být nevratná, což je u bohatých propojitelných dat obtížné.

Profilování může rozhodovat, kdo uvidí nabídku, dostane úvěr nebo bude označen za rizikového. Pokud historická data obsahují nerovné zacházení, model jej může opakovat. Výsledek může být diskriminační i bez použití výslovně citlivého údaje, protože jiné proměnné fungují jako jeho zástupce. Automatické skóre proto potřebuje kontrolu účelu, kvality dat, dopadu na různé skupiny a možnost lidského přezkoumání.

Dalším rizikem je **účelový posun**: data shromážděná pro jednu službu se začnou používat k jinému cíli, který uživatel neočekával. Školní přístupový systém může být zaveden kvůli bezpečnosti, ale později použit k detailnímu sledování pohybu. Technická možnost není sama o sobě oprávněním.

Ochrana stojí na minimalizaci dat, omezení doby uchování, řízení přístupu, šifrování, auditu a transparentních pravidlech. Organizace má vědět, odkud data pocházejí, kdo za ně odpovídá a jak lze chybný záznam opravit. Etika a bezpečnost nejsou dodatek po dokončení analýzy; ovlivňují už to, co se bude sbírat a jaké rozhodnutí je přijatelné automatizovat.

**Hlavní myšlenka:** Big data vyžadují nové architektury kvůli objemu, rychlosti nebo různorodosti. Datový sklad sjednocuje historická data pro OLAP, zatímco OLTP chrání každodenní transakce. Schopnost rozsáhle analyzovat data musí doprovázet kontrola kvality, účelu, soukromí a dopadu rozhodnutí.

# Závěrečné propojení

Informační a databázový systém není totéž. Informační systém začíná potřebou organizace a zahrnuje lidi, procesy, data i techniku. Databázový systém je část infrastruktury, která data organizovaně ukládá a zpřístupňuje. Nad stejnou databází mohou pracovat provozní aplikace, manažerské přehledy i analytické nástroje, ale každý typ uživatele potřebuje jiný pohled a jiná oprávnění.

Celý okruh lze shrnout řetězcem:

**potřeba → proces → vstupní data → zpracování → provozní informace → databázový model → analytika → rozhodnutí → zpětná vazba**

Dobré řešení nezačíná otázkou „Jakou databázi použijeme?“, ale otázkami „Jaký problém řešíme, kdo bude výsledek používat a podle čeho poznáme, že systém funguje?“ Teprve potom se rozhoduje, zda postačí relační databáze, zda se hodí dokumentový, key-value, wide-column či grafový model a zda je nutný datový sklad nebo distribuované zpracování.

## Ověřené zdroje k dalšímu studiu

- [NIST Big Data Interoperability Framework: Definitions](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2)
- [MongoDB: Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [Apache Cassandra: Architecture Overview](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)
- [Neo4j: What is a Graph Database](https://neo4j.com/docs/getting-started/graph-database/)
- [PostgreSQL: Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)

