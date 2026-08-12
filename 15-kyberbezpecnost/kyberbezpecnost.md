# Kyberbezpečnost

## Modernizovaný výukový text

> Kyberbezpečnost není jen antivirus a silné heslo. Je to způsob, jak chránit zařízení, účty, data a služby před chybou, zneužitím i úmyslným útokem — a zároveň zajistit, aby systém dokázal incident rozpoznat, omezit jeho dopad a obnovit běžný provoz.

Digitální systémy dnes řídí školní informační systémy, bankovnictví, dopravu, zdravotnictví, výrobu i komunikaci. Útok na informační systém proto nemusí skončit pouze ztrátou souboru. Může způsobit výpadek služby, únik osobních údajů, finanční škodu, manipulaci s informacemi nebo skutečné fyzické následky.

Kyberbezpečnost je proto vhodné chápat jako soubor technických, organizačních a lidských opatření. Nestačí pouze zabránit tomu, aby se do počítače dostal škodlivý program. Musíme také chránit identitu uživatelů, správně nastavovat přístupová práva, bezpečně přenášet a ukládat data, aktualizovat software, zálohovat, sledovat neobvyklé chování a být připraveni na situaci, kdy některé ochranné opatření selže.

# 1. Kyberprostor, hrozby a řízení bezpečnosti

## 1.1 Kyberprostor není „virtuální svět oddělený od reality“

Pojem **kyberprostor** označuje prostředí tvořené propojenými informačními a komunikačními technologiemi: počítači, servery, síťovými prvky, cloudovými službami, mobilními zařízeními, průmyslovými systémy, databázemi i softwarem, který nad nimi pracuje.

Označení „virtuální prostor“ může být užitečné, ale snadno vede k omylu, že jde o něco nehmotného a odděleného od skutečného světa. Ve skutečnosti stojí kyberprostor na fyzické infrastruktuře — datových centrech, optických kabelech, routerech, rádiových sítích a koncových zařízeních. Útok na informační systém proto může mít jak digitální, tak fyzické důsledky.

Například útok na školní informační systém může znepřístupnit rozvrhy a známky. Útok na nemocnici může omezit dostupnost zdravotnické dokumentace. Napadení průmyslového řídicího systému může ovlivnit skutečný výrobní proces.

Pro bezpečnost je důležité rozlišovat několik základních pojmů.

**Aktivum** je něco, co má pro organizaci nebo uživatele hodnotu: data, účet, server, know-how, provozní systém nebo například reputace.

**Hrozba** je něco, co může aktivum poškodit. Může jít o útočníka, malware, požár, výpadek napájení nebo lidskou chybu.

**Zranitelnost** je slabé místo, které může hrozba využít — například neopravená chyba v programu, slabé heslo nebo špatně nastavené přístupové oprávnění.

**Riziko** vyjadřuje možnost, že určitá hrozba zranitelnost skutečně využije, a závažnost následků.

Jednoduchý model můžeme zapsat:

**aktivum → hrozba → zranitelnost → možné následky → riziko → ochranné opatření**

Bezpečnost proto nezačíná nákupem produktu. Začíná otázkou: **Co chráníme, před čím, jakým způsobem může dojít ke škodě a která opatření dávají vzhledem k riziku smysl?**

## 1.2 Důvěrnost, integrita a dostupnost

Velká část informační bezpečnosti se dá popsat pomocí tří základních vlastností, známých jako **CIA triáda**:

- **Confidentiality — důvěrnost**
- **Integrity — integrita**
- **Availability — dostupnost**

**Důvěrnost** znamená, že se k informaci dostane pouze ten, kdo k ní má oprávnění. Pokud někdo odcizí databázi hesel nebo zdravotnickou dokumentaci, byla narušena důvěrnost.

**Integrita** znamená, že data nejsou neoprávněně nebo nepozorovaně změněna. Pokud útočník změní číslo účtu na faktuře nebo přepíše známku v databázi, jde o narušení integrity.

**Dostupnost** znamená, že systém a data jsou použitelné tehdy, kdy je oprávněný uživatel potřebuje. Výpadek serveru nebo DDoS útok může dostupnost výrazně omezit.

Je důležité nezaměňovat **důvěrnost** s **ochranou soukromí — privacy**. Soukromí je širší pojem: řeší, jaké osobní údaje se vůbec sbírají, k jakému účelu, kdo je smí používat a jak dlouho se uchovávají. Data mohou být technicky dobře zašifrovaná, a přesto může být jejich sběr nebo použití z pohledu soukromí problematické.

Dobrá bezpečnost musí chránit všechny tři vlastnosti. Dokonale utajený systém, který je neustále nedostupný, není dobře zabezpečený. Stejně tak záloha, kterou lze snadno neoprávněně změnit, nemusí být spolehlivou zálohou.

## 1.3 Typy útoků a motivace útočníků

Útočníci nemají vždy stejný cíl. Někdo chce finanční zisk, jiný získává informace, narušuje provoz, prosazuje politický cíl nebo pouze zkouší, co dokáže.

Mezi běžné motivace patří:

- krádež peněz nebo přístupových údajů,
- získání osobních údajů či obchodního know-how,
- vydírání,
- špionáž,
- sabotáž,
- poškození pověsti,
- ideologická nebo politická motivace,
- získání přístupu do systému pro další útok.

Útok může mířit na **důvěrnost**, **integritu** nebo **dostupnost**. Například ransomware často kombinuje více cílů: data zašifruje, čímž omezí dostupnost, a moderní skupiny je často také odcizí, čímž poruší důvěrnost.

Typickým útokem na dostupnost je **DoS — Denial of Service**, při kterém je služba přetížena nebo jinak vyřazena z provozu. Pokud útok přichází současně z velkého množství zařízení, mluvíme o **DDoS — Distributed Denial of Service**.

Útočník může využít **botnet**, tedy síť kompromitovaných zařízení řízených bez vědomí jejich vlastníků. Botnet nemusí být tvořen pouze počítači; součástí mohou být servery, routery, kamery nebo špatně zabezpečená IoT zařízení.

U cílených a dlouhodobých útoků se někdy používá pojem **APT — Advanced Persistent Threat**. Nejde o konkrétní typ malwaru, ale o způsob útoku, při němž schopný protivník dlouhodobě usiluje o přístup k určité organizaci a snaží se v systému zůstat co nejméně nápadně.

Důležitou oblastí jsou také **útoky na dodavatelský řetězec — supply-chain attacks**. Útočník nemusí napadnout cílovou organizaci přímo. Může kompromitovat software, aktualizační mechanismus nebo dodavatele, kterému organizace důvěřuje.

V mezinárodním prostředí mohou kybernetické operace souviset také se špionáží, sabotáží nebo ozbrojeným konfliktem. Označení **kyberválka** se však používá opatrně: ne každý útok vedený ze zahraničí je válečnou operací a jednoznačné určení původce útoku bývá technicky i politicky obtížné.

## 1.4 Bezpečnostní incident není totéž co útok

Ne každá hrozba skončí incidentem a ne každý incident vznikne útokem.

**Kybernetický bezpečnostní incident** je událost, která skutečně naruší nebo významně ohrozí bezpečnost systému či služby. Může být způsobena útočníkem, chybou administrátora, poruchou zařízení nebo chybnou aktualizací.

Praktický rozdíl:

```text
hrozba       → něco může způsobit škodu
zranitelnost → slabé místo umožňuje útok
útok         → někdo se slabinu snaží využít
incident     → bezpečnost systému byla skutečně narušena
```

Organizace potřebuje nejen preventivní ochranu, ale také schopnost incident **detekovat, vyhodnotit, omezit, odstranit jeho příčinu a obnovit provoz**.

Specializované týmy pro reakci na bezpečnostní incidenty se označují například jako **CERT — Computer Emergency Response Team** nebo **CSIRT — Computer Security Incident Response Team**. Jejich úkolem může být koordinace reakce, analýza incidentů, předávání varování a spolupráce s dalšími organizacemi.

## 1.5 Kybernetická bezpečnost a právo v České republice

Právní úprava kybernetické bezpečnosti se v čase mění, proto není vhodné učit se staré číslo zákona jako neměnný údaj. Od **1. listopadu 2025** je v České republice účinný **zákon č. 264/2025 Sb., o kybernetické bezpečnosti**, který nahradil dřívější právní úpravu a zavádí požadavky evropské směrnice **NIS2**.

Zákon se nevztahuje stejně na každého uživatele počítače. Zaměřuje se především na poskytovatele vybraných regulovaných služeb a stanovuje povinnosti odpovídající významu a rizikovosti jejich činnosti. Patří mezi ně zejména zavádění bezpečnostních opatření, řízení kybernetických rizik, evidence a hlášení incidentů a další organizační a technické povinnosti.

Ústředním orgánem České republiky pro kybernetickou bezpečnost je **NÚKIB — Národní úřad pro kybernetickou a informační bezpečnost**.

Pro středoškolské pochopení je důležitější princip než detailní právní procedura:

> U významných digitálních služeb není kyberbezpečnost pouze dobrovolnou technickou disciplínou. Stává se také součástí řízení organizace, odpovědnosti vedení, řízení rizik a zákonných povinností.

# 2. Malware a sociální inženýrství

## 2.1 Jak se škodlivý software dostane do systému

**Malware — malicious software** je obecné označení pro software vytvořený nebo upravený tak, aby prováděl škodlivou činnost.

Představa, že malware se do počítače dostane pouze otevřením „zavirovaného souboru“, je příliš úzká. Útočník může využít několik cest.

Častým mechanismem je škodlivá e-mailová příloha nebo odkaz. Soubor může obsahovat spustitelný program, makro, skript nebo jiný obsah, který se snaží uživatele přimět ke spuštění.

Jinou cestou je zneužití **zranitelnosti**. Útočník využije chybu v operačním systému, prohlížeči, síťové službě nebo jiné aplikaci. Pokud existuje oprava, ale zařízení není aktualizováno, může být útok zbytečně snadný.

Malware může být šířen také:

- podvodnými instalačními balíčky,
- pirátským nebo pozměněným softwarem,
- škodlivou reklamou,
- kompromitovaným webem,
- vyměnitelným médiem,
- P2P sítí,
- zneužitým účtem,
- kompromitovanou aktualizací důvěryhodného programu.

Moderní útok proto často není jedna událost, ale **řetězec kroků**. Uživatel klikne na podvodný odkaz, zadá heslo na falešném webu, útočník získá účet, přes něj pošle škodlivý soubor dalším lidem a teprve následně se do systému dostane malware.

## 2.2 Virus, červ, trojský kůň a další malware

Jednotlivé názvy nepopisují vždy účel malwaru; často popisují především způsob šíření nebo chování.

**Počítačový virus** připojuje svůj kód k jinému souboru nebo programu a při jeho spuštění se může dále šířit. Historicky šlo o velmi významnou kategorii, ale dnešní škodlivé kampaně často používají jiné mechanismy.

**Červ — worm** se dokáže šířit samostatně, typicky prostřednictvím sítě a zranitelných služeb. Nebezpečný může být právě rychlostí automatického šíření.

**Trojský kůň — Trojan** se tváří jako legitimní nebo užitečný program, ale obsahuje škodlivou funkci. Na rozdíl od červa nemusí mít vlastní mechanismus automatického šíření; často spoléhá na to, že jej uživatel spustí.

**Spyware** sleduje uživatele nebo sbírá informace. Specializovanou podobou je **infostealer**, který se snaží získat například hesla, cookies, kryptoměnové peněženky nebo jiné přístupové údaje.

**RAT — Remote Access Trojan** poskytuje útočníkovi vzdálené ovládání napadeného systému. Může umožnit spouštět příkazy, přenášet soubory nebo sledovat aktivitu uživatele.

**Rootkit** se snaží skrýt přítomnost škodlivého kódu nebo útočníka v systému a někdy zasahuje do nízkoúrovňových částí operačního systému.

**Ransomware** omezuje přístup k datům, typicky jejich zašifrováním, a požaduje výkupné. Moderní ransomware často používá model **double extortion**: před šifrováním data také odcizí a hrozí jejich zveřejněním.

**Wiper** data ničí nebo poškozuje bez skutečného cíle jejich obnovení. Může se tvářit jako ransomware, ale jeho účelem je sabotáž.

Malware může být současně členem více kategorií. Trojský kůň může po spuštění nainstalovat infostealer, který připojí zařízení do botnetu. Není proto vždy užitečné hledat jedinou nálepku; důležitější je pochopit, **co malware dělá, jak se šíří a jaký přístup získal**.

## 2.3 Sociální inženýrství: útok na člověka

Technicky zabezpečený systém může být obejit, pokud útočník přesvědčí oprávněného člověka, aby mu přístup poskytl sám.

**Sociální inženýrství** využívá psychologické principy: důvěru, strach, zvědavost, autoritu, časový tlak nebo ochotu pomoci.

Typickým příkladem je **phishing**. Útočník napodobuje důvěryhodnou službu a snaží se přimět oběť, aby otevřela odkaz, zadala přihlašovací údaje nebo provedla platbu.

**Spear phishing** je cílený phishing připravený pro konkrétní osobu nebo organizaci. Může využívat jména kolegů, informace z webu firmy nebo skutečný kontext projektu.

**Smishing** používá SMS či jiné textové zprávy. **Vishing** využívá hlasový hovor.

**Baiting** nabízí lákavou odměnu — například „bezplatný software“, dokument nebo nalezený USB disk — a spoléhá na zvědavost oběti.

Stále častěji se objevují podvodné QR kódy, někdy označované jako **QR phishing** nebo **quishing**. QR kód zakryje skutečnou cílovou adresu a na telefonu může být obtížnější doménu před otevřením pečlivě zkontrolovat.

Generativní AI navíc snižuje náklady na přípravu přesvědčivého textu, napodobení stylu komunikace nebo vytváření syntetického hlasu a obrazu. Gramaticky bezchybná zpráva proto není důkazem, že je pravá.

## 2.4 Proč funguje phishing i na zkušené uživatele

Phishing není test inteligence. Úspěšné útoky využívají situaci, ve které člověk reaguje rychle a podle naučených vzorců.

Typická podvodná zpráva kombinuje několik prvků:

**autorita** — „píše ředitel“, „volá banka“, „bezpečnostní oddělení žádá ověření“;

**naléhavost** — „účet bude za 15 minut zablokován“;

**strach** — „zaznamenali jsme neoprávněnou platbu“;

**odměna** — „vyhráli jste“;

**rutina** — zpráva napodobuje běžný pracovní postup.

Dobrá obrana proto nestojí pouze na školení „nikdy neklikejte“. Uživatel potřebuje mít bezpečný způsob, jak požadavek ověřit jiným kanálem.

Pokud například přijde neobvyklý příkaz k platbě od vedoucího, je správným postupem ověřit jej telefonicky na známém čísle nebo osobně — nikoli odpovědí na stejný podezřelý e-mail.

# 3. Rozpoznání napadení a vícevrstvá obrana

## 3.1 Příznak není důkaz

Napadený systém nemusí vykazovat dramatické projevy. Moderní útočník se často snaží zůstat nenápadný.

Podezřelé mohou být například:

- neobvykle vysoké vytížení CPU nebo disku,
- nečekaná síťová komunikace,
- náhlé zpomalení,
- nové procesy nebo služby,
- neznámá rozšíření prohlížeče,
- změna nastavení bezpečnostních nástrojů,
- neočekávané přihlášení k účtu,
- soubory s neznámou příponou,
- hromadné změny či šifrování souborů,
- zprávy odeslané z účtu bez vědomí vlastníka.

Žádný jednotlivý příznak však automaticky nedokazuje malware. Vysoké využití procesoru může způsobit aktualizace, renderování videa nebo legitimní program. Bezpečnostní diagnostika proto hledá **souvislosti** a více nezávislých signálů.

Velmi důležité jsou **logy**: záznamy o přihlášení, spuštěných procesech, síťové komunikaci a změnách systému. Organizace proto nechrání pouze zařízení, ale také sleduje, co se v nich děje.

## 3.2 Obrana do hloubky

Neexistuje jedno opatření, které by zastavilo všechny útoky. Proto se používá princip **defense in depth — obrana do hloubky**.

Představme si několik vrstev:

```text
bezpečné chování uživatele
        ↓
silná autentizace
        ↓
aktualizovaný software
        ↓
omezená oprávnění
        ↓
antimalware / EDR
        ↓
firewall a segmentace
        ↓
monitoring a logy
        ↓
zálohy a obnova
```

Když jedna vrstva selže, další může útok zastavit nebo alespoň omezit jeho následky.

**Aktualizace** odstraňují známé zranitelnosti. Odkládání bezpečnostních oprav prodlužuje dobu, po kterou je známá slabina použitelná.

**Princip nejmenších oprávnění — least privilege** říká, že účet a program mají dostat jen taková práva, která skutečně potřebují. Uživatel, který běžně nepracuje jako správce, omezuje dopad části útoků.

**Firewall** filtruje síťovou komunikaci podle pravidel. Neumí sám rozpoznat každý škodlivý soubor a nenahrazuje aktualizace nebo autentizaci.

**Segmentace sítě** odděluje různé části infrastruktury. Pokud se například kompromituje studentské zařízení, nemělo by mít automaticky stejný přístup jako administrátorský server.

## 3.3 Antivirus, antimalware a EDR

Klasický antivirus porovnával soubory především s databází známých **signatur**. Tento princip stále existuje, ale moderní ochrana používá více technik.

**Signaturní detekce** hledá známé vzory. Je rychlá a přesná u již známých hrozeb, ale sama nestačí na nový nebo pozměněný malware.

**Heuristika** hledá podezřelé vlastnosti programu.

**Behaviorální analýza** sleduje chování. Podezřelý může být například proces, který začne hromadně měnit dokumenty, vypne bezpečnostní nástroj nebo se snaží spouštět kód neobvyklým způsobem.

**Reputační služby** porovnávají soubor, adresu nebo certifikát s informacemi získanými z velkého množství zařízení.

**Sandbox** spustí podezřelý obsah v izolovaném prostředí a sleduje, jak se chová.

V organizacích se používá také **EDR — Endpoint Detection and Response**. EDR neslouží pouze k blokování známého malwaru; shromažďuje informace o aktivitě koncových zařízení a pomáhá analyzovat a omezovat incident.

Antivirus proto není „magický filtr“. Je jednou z vrstev ochrany a může mít falešně pozitivní i falešně negativní výsledky.

## 3.4 Zálohy jako bezpečnostní opatření

Záloha není pouze ochrana před poruchou disku. Je zásadní také při ransomwaru, chybě správce nebo nechtěném smazání.

Známé pravidlo **3–2–1** doporučuje mít alespoň:

- tři kopie dat,
- na dvou různých typech úložiště,
- jednu kopii oddělenou od hlavního systému.

Dnes je důležitá také otázka, zda útočník může zálohu smazat. Organizace proto používají **offline**, oddělené nebo **immutable** zálohy, které nelze běžným účtem jednoduše přepsat.

Nejdůležitější kontrolní otázka není „Máme zálohu?“, ale:

> Dokážeme z ní skutečně obnovit systém a víme, jak dlouho obnova potrvá?

Záloha, kterou nikdo nikdy nezkusil obnovit, je pouze předpoklad.

## 3.5 Co dělat při podezření na incident

U domácího zařízení i v organizaci je důležité nejednat zbrkle.

Pokud zařízení začne například hromadně šifrovat soubory nebo existuje silné podezření na aktivní útok, je vhodné **omezit jeho síťové spojení**, aby se útok dále nešířil. V organizaci je současně nutné co nejrychleji kontaktovat správce nebo bezpečnostní tým.

Není vhodné bez rozmyslu mazat soubory a „uklízet stopy“. Logy a další informace mohou být důležité pro zjištění, co se stalo.

Pokud byly kompromitovány přihlašovací údaje, heslo se mění z **důvěryhodného čistého zařízení**, přičemž se ukončí aktivní relace a zkontrolují další způsoby obnovy účtu.

Obecný postup má několik fází:

**detekce → omezení dopadu → analýza → odstranění příčiny → obnova → poučení**

Cílem není pouze „zprovoznit počítač“, ale také pochopit, jak útočník získal přístup a zda v systému nezůstal další.

# 4. Digitální identita, autentizace a hesla

## 4.1 Identita, autentizace a autorizace

Tyto pojmy se často zaměňují.

**Identifikace** odpovídá na otázku: **Za koho se vydáváte?**

Například zadáte uživatelské jméno `eva.novakova`.

**Autentizace** odpovídá: **Dokážete, že touto osobou nebo účtem skutečně jste?**

Například zadáte heslo nebo použijete bezpečnostní klíč.

**Autorizace** odpovídá: **Co smíte po přihlášení dělat?**

Student může číst své známky, učitel může známky zapisovat a správce může spravovat účty.

Můžeme tedy zapsat:

```text
identita → autentizace → autorizace
kdo?       opravdu kdo?    co smí?
```

Bezpečný systém musí oddělovat tyto kroky. To, že je uživatel úspěšně přihlášen, neznamená, že smí provést jakoukoli operaci.

## 4.2 Autentizační faktory a MFA

Autentizační metody se tradičně rozdělují podle typu důkazu.

**Něco, co vím** — heslo nebo PIN.

**Něco, co mám** — telefon, bezpečnostní klíč, čipová karta.

**Něco, čím jsem** — biometrická vlastnost, například otisk prstu nebo rozpoznání obličeje.

**MFA — Multi-Factor Authentication** kombinuje alespoň dva nezávislé faktory. Dvě hesla nejsou dva faktory; obě patří do skupiny „něco, co vím“.

Ne všechny druhy MFA mají stejnou odolnost.

SMS kód je obvykle lepší než samotné heslo, ale může být ohrožen například sociálním inženýrstvím nebo převodem telefonního čísla.

Aplikace generující **TOTP** kódy je zpravidla odolnější vůči některým telefonním útokům, ale uživatel může kód stále omylem zadat na phishingovou stránku.

Push notifikace mohou být zneužity pomocí **MFA fatigue**: útočník opakovaně posílá potvrzovací výzvy a doufá, že uživatel některou ze zvyku schválí.

Silnější ochranu proti phishingu poskytují autentizační mechanismy založené na veřejném klíči, například **FIDO2/WebAuthn**, hardwarové bezpečnostní klíče a **passkeys**. Ty jsou svázány s konkrétní službou a falešný web nemůže jednoduše převzít autentizační tajemství stejným způsobem jako heslo.

## 4.3 Heslo: délka, jedinečnost a správce hesel

Starší bezpečnostní poučky často požadovaly například „osm znaků, velké písmeno, malé písmeno, číslici, symbol a změnu každých 30 dní“. Takové pravidlo může vést k předvídatelným heslům typu `Heslo2026!`.

Moderní doporučení klade větší důraz na:

**délku** — dlouhé heslo nebo heslová fráze má větší prostor možných kombinací;

**jedinečnost** — každá služba má mít jiné heslo;

**nepředvídatelnost** — nepoužívat běžné fráze a známá uniklá hesla;

**správce hesel** — umožňuje generovat a ukládat dlouhá náhodná hesla.

Uživatel by si proto neměl pamatovat desítky variant jednoho hesla. Mnohem bezpečnější je chránit kvalitně správce hesel a pro jednotlivé služby používat unikátní generovaná hesla.

Automatická pravidelná změna hesla bez důvodu už není obecně považována za nejlepší postup. Heslo je nutné změnit zejména tehdy, když existuje podezření nebo důkaz, že bylo kompromitováno.

Důležitá je také **obnova účtu**. Pokud služba umožní obejít silné přihlášení jednoduchou otázkou „Jak se jmenoval váš první pes?“, může být právě obnova nejslabším článkem systému.

## 4.4 Jak se na hesla útočí

**Brute force** zkouší velké množství možných hesel.

**Slovníkový útok** používá seznamy častých hesel, slov a typických variant.

**Password spraying** zkouší malé množství velmi častých hesel proti mnoha účtům, aby se vyhnul rychlému zablokování jednoho konkrétního účtu.

**Credential stuffing** používá dvojice e-mail–heslo uniklé z jedné služby a automaticky je zkouší na jiných službách. Právě proto je opakované použití hesla tak nebezpečné.

**Phishing** heslo neuhodne — uživatel jej útočníkovi sám zadá.

**Keylogger** zachycuje stisky kláves nebo jiným způsobem sbírá zadávané informace.

Na straně služby se proti hádání hesel používá například **rate limiting**, tedy omezení rychlosti neúspěšných pokusů, a blokování známých kompromitovaných hesel.

## 4.5 Passkeys: přihlášení bez sdíleného hesla

**Passkey** používá asymetrickou kryptografii. Zařízení vytvoří dvojici klíčů. Veřejný klíč dostane služba, soukromý klíč zůstává v autentizačním prostředí uživatele.

Při přihlášení server pošle výzvu a zařízení ji podepíše soukromým klíčem. Server podpis ověří veřejným klíčem.

Důležitá výhoda spočívá v tom, že server neuchovává tajemství, které by se dalo stejně jako databáze hesel použít k přihlášení. Passkey je navíc vázán na konkrétní doménu, což výrazně omezuje klasický phishing.

Uživatel může passkey odemknout například biometrikou nebo PINem zařízení. Biometrický údaj se přitom typicky neposílá webové službě; slouží místně k povolení použití uloženého klíče.

Passkeys nejsou řešením všech problémů. Stále je nutné chránit zařízení, účet pro synchronizaci klíčů a proces obnovy. Dobře navržená veřejnoklíčová autentizace ale odstraňuje několik slabin klasických hesel najednou.

# 5. Ochrana dat a kryptografie

## 5.1 Data v klidu, při přenosu a při zpracování

Data mohou být ohrožena v různých stavech.

**Data at rest — data v klidu** jsou například soubory na disku, databáze nebo záloha.

**Data in transit — data při přenosu** putují sítí.

**Data in use — data při zpracování** jsou právě používána programem a často se nacházejí v operační paměti.

Ochranná opatření se proto liší. Šifrování disku chrání zejména data uložená na odcizeném zařízení. TLS chrání síťovou komunikaci. Přístupová práva a izolace procesů chrání data během práce systému.

K narušení dat může dojít mnoha způsoby:

- únikem databáze,
- odcizením zařízení,
- chybným nastavením cloudového úložiště,
- phishingem a převzetím účtu,
- zneužitím zranitelnosti,
- nechtěným smazáním,
- ransomwarem,
- chybou aplikace,
- odposlechem nezabezpečené komunikace.

**Packet sniffing** znamená zachytávání síťových paketů. Nástroj jako Wireshark je legitimní diagnostický nástroj; jeho použití samo o sobě není útok. Riziko vzniká tehdy, když někdo neoprávněně zachytává nebo zneužívá cizí komunikaci.

Při **Man-in-the-Middle — MitM** útoku se protivník snaží dostat mezi komunikující strany a komunikaci číst nebo měnit. Správně ověřené šifrované protokoly, například HTTPS s platným TLS certifikátem, takový útok výrazně komplikují.

## 5.2 Symetrické a asymetrické šifrování

**Šifrování** převádí otevřená data — plaintext — do podoby, kterou bez příslušného klíče nelze běžně přečíst.

U **symetrického šifrování** se pro šifrování a dešifrování používá stejný tajný klíč.

```text
plaintext + tajný klíč → ciphertext
ciphertext + stejný klíč → plaintext
```

Moderním příkladem je **AES — Advanced Encryption Standard**.

Symetrická kryptografie je velmi rychlá a hodí se pro velké množství dat. Zásadním problémem je bezpečné předání tajného klíče druhé straně.

**Asymetrická kryptografie** používá dvojici matematicky souvisejících klíčů:

- **veřejný klíč** lze zveřejnit,
- **soukromý klíč** musí zůstat chráněný.

Patří sem například RSA a kryptografie nad eliptickými křivkami.

Není správné tvrdit, že asymetrické šifrování je prostě „bezpečnější“. Jde o jiný nástroj s jinými vlastnostmi. Asymetrické operace jsou výpočetně náročnější a v praxi se často kombinují se symetrickou kryptografií.

Například u TLS se veřejnoklíčové mechanismy používají k autentizaci a bezpečnému vytvoření společného tajemství, zatímco samotný větší datový přenos chrání rychlá symetrická kryptografie. Tento přístup se označuje jako **hybridní kryptografie**.

## 5.3 Hash není šifrování

**Hashovací funkce** vezme vstup libovolné délky a vytvoří výstup pevné délky.

Například SHA-256 vytvoří 256bitový hash.

Hashovací funkce není šifrování, protože jejím účelem není umožnit pozdější dešifrování. Z hashe se nemá dát prakticky rekonstruovat původní vstup.

Dobrá kryptografická hashovací funkce má mimo jiné znesnadnit:

- nalezení vstupu odpovídajícího zadanému hashi,
- nalezení jiného vstupu se stejným hashem.

Není přesné říkat, že hash je „unikátní hodnota“. Protože možných vstupů je více než možných hashů pevné délky, **kolize matematicky existují**. Bezpečná hashovací funkce pouze zajišťuje, že je prakticky velmi obtížné je cíleně nalézt.

Hash se používá například pro kontrolu integrity:

```text
soubor → SHA-256 → kontrolní otisk
```

Pokud po přenosu vyjde jiný hash, obsah se změnil.

### Hesla se nemají ukládat jako běžný SHA-256

Server by neměl uchovávat hesla v otevřené podobě ani je jednoduše ukládat pomocí rychlé hashovací funkce.

Pro hesla se používají specializované **password hashing / key derivation** algoritmy, například Argon2, scrypt nebo bcrypt. Jsou záměrně výpočetně náročnější, aby útočník po odcizení databáze nemohl extrémně rychle zkoušet miliardy kandidátů.

Ke každému heslu se přidává náhodná hodnota zvaná **salt**. Dva uživatelé se stejným heslem pak nemají stejný uložený hash.

## 5.4 TLS a end-to-end šifrování

Při návštěvě webu přes HTTPS chrání komunikaci **TLS — Transport Layer Security**.

TLS řeší několik úloh:

- šifruje obsah přenosu,
- chrání integritu,
- umožňuje ověřit identitu serveru pomocí certifikátu.

HTTPS však chrání především úsek mezi klientem a konkrétním webovým serverem nebo terminujícím bodem TLS.

**End-to-End Encryption — E2EE** má jiný cíl. Data jsou zašifrována na zařízení odesílatele a dešifrována až na zařízení příjemce. Provozovatel přenosové infrastruktury nemá mít klíč umožňující běžně číst obsah zpráv.

To neznamená úplnou anonymitu. Systém může stále zpracovávat metadata, například kdo komunikuje, kdy, z jakého zařízení nebo jak velké zprávy přenáší.

Při hodnocení bezpečnosti komunikační aplikace proto nestačí tvrzení „používá šifrování“. Je nutné ptát se:

**Co přesně je šifrováno? Kde se nacházejí klíče? Kdo má možnost obsah dešifrovat? Jak se ověřuje druhá strana?**

## 5.5 Digitální podpis, certifikát a elektronický podpis

Digitální podpis se často chybně vysvětluje větou „odesílatel zašifruje celý dokument soukromým klíčem“. Takto se moderní digitální podpis obecně nechová.

Zjednodušený princip je:

```text
dokument
   ↓
hash
   ↓
podepsání hashe soukromým klíčem
   ↓
digitální podpis
```

Příjemce vypočítá hash dokumentu znovu a pomocí veřejného klíče ověří podpis.

Digitální podpis tak může potvrdit především:

**integritu** — podepsaný obsah nebyl po podpisu změněn;

**autenticitu kryptografického klíče** — podpis vytvořil držitel odpovídajícího soukromého klíče.

Zůstává však otázka: **Komu veřejný klíč patří?**

Tu může řešit **digitální certifikát**, který propojuje veřejný klíč s určitou identitou. Certifikáty vydávají certifikační autority v rámci systému označovaného jako **PKI — Public Key Infrastructure**.

Je vhodné rozlišovat technický pojem **digitální podpis** a právní pojem **elektronický podpis**.

Evropské nařízení **eIDAS** rozlišuje více úrovní elektronického podpisu. Ne každé elektronické podepsání dokumentu je kvalifikovaným podpisem. **Kvalifikovaný elektronický podpis — QES** má podle eIDAS v Evropské unii výslovně právní účinek rovnocenný vlastnoručnímu podpisu.

To neznamená, že jiné elektronické podpisy jsou automaticky „neplatné“. Jejich právní účinek se posuzuje podle konkrétní situace a požadované formy právního jednání. Pro technickou výuku je nejdůležitější pochopit vztah:

**soukromý klíč → vytvoření podpisu**

**veřejný klíč → ověření podpisu**

**certifikát → vazba veřejného klíče na identitu**

# 6. Bezpečnost jako proces: od jednotlivce k organizaci

## 6.1 Bezpečnost nelze „nainstalovat“

Kyberbezpečnost se někdy redukuje na seznam produktů: antivirus, firewall, VPN, správce hesel. Každý z nich může být užitečný, ale samotná instalace nástroje nezaručuje bezpečnost.

Bezpečnost je **proces řízení rizika**.

Organizace musí pravidelně:

1. vědět, jaká zařízení, služby a data používá;
2. sledovat zranitelnosti a hrozby;
3. instalovat opravy;
4. řídit přístupová práva;
5. kontrolovat konfiguraci;
6. sledovat incidenty;
7. testovat zálohy;
8. reagovat na změny.

Velký význam má také **inventarizace aktiv**. Nelze bezpečně aktualizovat server, o kterém správce ani neví, že existuje.

Stejně důležitý je konec životního cyklu. Software bez bezpečnostních aktualizací představuje rostoucí riziko, i když stále „funguje“.

## 6.2 Cloud nemění odpovědnost v kouzlo

Cloudová služba může být velmi dobře zabezpečená, ale její zákazník stále může udělat chybu.

Častým problémem není prolomení kryptografie cloudu, ale například:

- veřejně zpřístupněné úložiště,
- příliš široká oprávnění,
- kompromitovaný administrátorský účet,
- uniklý API klíč,
- špatně nastavená databáze.

Mluví se proto o **shared responsibility model — modelu sdílené odpovědnosti**. Poskytovatel cloudu chrání určitou část infrastruktury, zákazník ale odpovídá za správnou konfiguraci svých služeb, identity, data a přístupová oprávnění v rozsahu daném konkrétním modelem služby.

Otázka „Je cloud bezpečný?“ je proto příliš obecná. Přesnější je:

> Kterou část systému chrání poskytovatel a kterou musíme správně zabezpečit my?

## 6.3 Zero Trust: nedůvěřovat automaticky podle umístění

Tradiční síť se někdy představovala jako hrad: uvnitř firemní sítě je „bezpečno“, venku je internet a firewall tvoří hradbu.

Moderní prostředí je složitější. Zaměstnanci pracují z domova, data jsou v cloudu, notebook se připojuje z různých sítí a aplikace komunikují s externími službami.

Princip **Zero Trust** proto říká, že přístup nemá být automaticky důvěryhodný jen proto, že přichází „zevnitř“.

Každý požadavek se má posuzovat podle identity, zařízení, oprávnění, kontextu a rizika. Uživatel dostane jen potřebný přístup a jeho důvěryhodnost se průběžně ověřuje.

Zero Trust neznamená „nevěřit nikomu a nic nefunguje“. Je to architektonický princip:

**nikoli „jsem uvnitř, tedy smím“**

ale:

**„jsem ověřený, splňuji podmínky a mám oprávnění právě k této činnosti“**

## 6.4 Lidská chyba je součást systému

Není realistické předpokládat, že uživatel nikdy neudělá chybu.

Dobře navržený systém proto chybu očekává a omezuje její následky.

Pokud jeden klik na škodlivou přílohu automaticky poskytne administrátorský přístup k celé síti a zároveň umožní smazat zálohy, není problém pouze „nepozorný uživatel“. Selhalo několik bezpečnostních vrstev.

Bezpečná organizace kombinuje:

- rozumné školení,
- technická omezení,
- vícefaktorovou autentizaci,
- princip nejmenších oprávnění,
- segmentaci,
- monitoring,
- jednoduché hlášení podezřelých událostí.

Uživatel musí vědět, **kam incident oznámit**, a nesmí se bát přiznat chybu. Čím déle zůstává incident skrytý, tím větší škodu může způsobit.

## 6.5 Bezpečnostní myšlení v praxi

Místo zapamatování dlouhého seznamu hrozeb je užitečné osvojit si několik kontrolních otázek.

Když používáte novou službu:

**Jaká data jí dávám?**

**Kdo je může číst?**

**Jak se přihlašuji?**

**Co se stane, když unikne moje heslo?**

**Lze zapnout MFA nebo passkey?**

**Jak služba obnovuje účet?**

**Kde jsou data uložena a lze je exportovat nebo smazat?**

Když instalujete program:

**Odkud pochází?**

**Je digitálně podepsaný?**

**Je stále podporovaný a aktualizovaný?**

**Jaká oprávnění požaduje?**

Když přijde neobvyklá zpráva:

**Proč po mně někdo chce právě tuto akci?**

**Vytváří umělý časový tlak?**

**Mohu požadavek ověřit jiným kanálem?**

**Odpovídá doména skutečné službě?**

Kyberbezpečnost není schopnost předvídat každý budoucí útok. Je to schopnost stavět systémy a pracovní návyky tak, aby chyba nebo kompromitace jedné části neznamenala automaticky ztrátu všeho.

# Závěrečné propojení

Kyberbezpečnost je nejlépe pochopitelná jako soustava navazujících vrstev.

Nejprve musíme vědět, **co chráníme**. Aktivem mohou být data, účet, zařízení, služba nebo reputace.

Potom zkoumáme **hrozby a zranitelnosti**. Útočník může využít technickou chybu, slabou autentizaci, nepozornost člověka nebo chybu v konfiguraci.

Ochranná opatření se skládají do více vrstev:

**aktualizace → omezená oprávnění → silná autentizace → ochrana zařízení → síťová ochrana → monitoring → záloha → reakce na incident**

Kryptografie chrání data, ale nevyřeší phishing. Antivirus může zachytit malware, ale neochrání účet, jehož heslo uživatel dobrovolně zadal útočníkovi. MFA výrazně zlepšuje bezpečnost identity, ale neochrání špatně nastavenou veřejnou databázi. Záloha zachrání data po havárii nebo ransomwaru, ale sama nezabrání úniku důvěrných informací.

Právě proto je důležitý princip **obrany do hloubky**.

Celý bezpečnostní cyklus lze zjednodušit:

**aktivum → riziko → prevence → detekce → reakce → obnova → poučení**

Nejlepší bezpečnost není systém, o kterém si myslíme, že jej nelze napadnout. Je to systém, který s možností chyby a útoku realisticky počítá, dokáže je včas rozpoznat a omezuje jejich následky.

## Referenční zdroje pro další studium

- NÚKIB — Portál k novému zákonu o kybernetické bezpečnosti: https://portal.nukib.gov.cz/
- NÚKIB — informace a doporučení: https://nukib.gov.cz/
- Směrnice NIS2, směrnice (EU) 2022/2555: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- NIST Digital Identity Guidelines, SP 800-63B: https://pages.nist.gov/800-63-4/sp800-63b.html
- CISA — Multi-Factor Authentication: https://www.cisa.gov/topics/cybersecurity-best-practices/multifactor-authentication
- eIDAS, nařízení (EU) č. 910/2014 v aktuálním znění: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0910-20241018
