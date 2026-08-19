<!--
author: Marek Lučný
title: Kryptografie a bezpečná komunikace – praktická laboratoř
language: cs
mode: Textbook
comment: Šest názorných experimentů k páté lekci okruhu Kyberbezpečnost.
-->

# Praktická laboratoř: Kryptografie a bezpečná komunikace

Kryptografie bývá na obrázcích znázorněna visacím zámkem. Ve skutečnosti je zajímavější: umí odhalit změnu jediného znaku, uzamknout archiv, prokázat totožnost serveru a doručit tajemství člověku, kterého jsme nikdy osobně nepotkali. V této laboratoři nebudete kryptografii jen obdivovat z dálky. Budete vytvářet důkazy, zkoušet chybné heslo, číst certifikát a předávat zašifrovanou zprávu.

> **🛡️ Bezpečnostní pravidlo laboratoře**
>
> Pracujte jen s připravenými cvičnými soubory, veřejnými tréninkovými klíči a schválenými weby. Do online nástrojů nevkládejte osobní údaje, skutečná hesla, soukromé klíče ani neveřejné dokumenty. Varování prohlížeče nikdy neobcházejte. Vytvořené klíče a hesla jsou pouze pro výuku a nesmějí se později použít u skutečného účtu.

| Experiment | Hlavní otázka | Nástroj | Orientační čas |
|---|---|---|---:|
| 5.1 Lavina v digitálním otisku | Pozná hash i nepatrnou změnu? | PowerShell / CyberChef | 30 min |
| 5.2 Trezor v jednom souboru | Co skutečně chrání šifrovaný archiv? | 7-Zip | 35 min |
| 5.3 Občanský průkaz webu | Komu prohlížeč věří a proč? | webový prohlížeč | 35 min |
| 5.4 Rentgen TLS serveru | Je známka A celý příběh? | Qualys SSL Labs | 40 min |
| 5.5 Tajná zásilka bez společného hesla | Jak spolupracuje veřejný a soukromý klíč? | CyberChef / OpenPGP | 45 min |
| 5.6 Ověřujeme člověka, ne jen zámek | Jak odhalit prostředníka v E2EE komunikaci? | Signal / učitelská demonstrace | 35 min |

U každého experimentu zaznamenejte **předpověď, měření, vysvětlení a omezení výsledku**. V kryptografii může správně vypadající řetězec snadno svádět k větším závěrům, než skutečně dovoluje.

## Experiment 5.1: Lavina v digitálním otisku

**Cíl:** Vypočítat SHA-256 dvou téměř shodných souborů, změřit lavinový efekt a rozlišit kontrolu integrity od šifrování a ověření původu.

**Nástroj:** Vestavěný příkaz `Get-FileHash` ve Windows PowerShellu. Alternativou je bezplatný [CyberChef](https://gchq.github.io/CyberChef/) spuštěný v prohlížeči. Výchozím materiálem je [připravený textový vzorek](./materialy/5-1-hash-vzorek.txt).

**Úkoly:**

1. Vytvořte kopii vzorku, změňte v ní právě jeden znak a předem odhadněte, jak velká část výsledného hashe se změní.
2. Vypočítejte SHA-256 obou souborů dvěma nezávislými způsoby a zkontrolujte, že nástroje dávají stejný výsledek.
3. Vysvětlete, co lze a nelze z rovnosti hashů dokázat, a navrhněte bezpečný způsob zveřejnění kontrolního součtu instalačního souboru.

**Výstupy:** Tabulka názvu souboru, velikosti a SHA-256; počet shodných pozic v obou hashech; krátké vysvětlení pojmů integrita, autenticita a šifrování; návrh důvěryhodného distribučního kanálu pro kontrolní součet.

<details>

<summary>**🧠 Rozbalit článek: Otisk, který prozradí i posunutou čárku**</summary>

**Stroj na jednoznačně vypadající zkratky**

Představte si román o pěti stech stranách. Chcete na dálku zjistit, zda v něm někdo nezměnil jedinou větu, ale nechcete porovnávat stránku po stránce. Hashovací funkce celý obsah „semleje“ do řetězce pevné délky. SHA-256 vrací 256 bitů, které se obvykle zapisují jako 64 šestnáctkových znaků. Stejně dlouhý otisk dostane krátká věta i obraz disku o mnoha gigabajtech.

Funkce je deterministická: stejný vstup musí dát stejný výstup. Zároveň má vykazovat **lavinový efekt** – drobná změna vstupu rozhází přibližně polovinu výstupních bitů. Není to chyba ani náhoda přidaná navíc. Právě díky tomu nelze ze shodného začátku dvou hashů usuzovat, že jsou soubory podobné. Hash není měřítko podobnosti; je to mimořádně citlivý otisk přesných bajtů.

**Tři otázky, které se často pletou**

Integrita odpovídá na otázku „Změnil se obsah?“. Důvěryhodně získaný hash nám umožní znovu spočítat otisk staženého souboru a hodnoty porovnat. **Autenticita** řeší „Kdo obsah vytvořil nebo schválil?“. Samotný hash autora nezná. Útočník, který na podvrženém webu vymění instalační soubor, může vedle něj snadno vystavit i nový hash. Proto se kontrolní součet publikuje přes důvěryhodný kanál nebo digitálně podepíše.

Šifrování odpovídá na třetí otázku: „Může obsah přečíst někdo nepovolaný?“. Hash původní data neschová. Naopak, hash běžného a snadno uhodnutelného hesla lze porovnávat se slovníkem předpočítaných hodnot. Proto se hesla neukládají jako prosté SHA-256, ale pomocí pomalých funkcí pro odvozování klíče a náhodné soli.

**Může mít dvojice různých souborů stejný hash?**

Protože možných vstupů je nekonečně více než 256bitových výstupů, kolize matematicky existovat musí. U moderní funkce je však cílem, aby nalezení použitelné kolize bylo výpočetně nereálné. To není totéž jako tvrdit, že kolize „neexistuje“. Bezpečnostní algoritmy stárnou: například MD5 a SHA-1 se již pro odolnost proti cíleným kolizím nepovažují za vhodné. Výběr algoritmu proto patří ke kontextu výsledku stejně jako samotný řetězec.

Hash je jako pečeť z citlivého vosku. Prozradí, že se zásilka změnila, jen pokud máme pravou pečeť s čím porovnat. Neřekne, zda byl obsah zásilky dobrý, tajný nebo pravdivý.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Příprava a předpověď**

1. Uložte [výukový vzorek](./materialy/5-1-hash-vzorek.txt) do vlastní pracovní složky. Zkontrolujte, že neobsahuje osobní ani neveřejná data.
2. Vytvořte kopii `5-1-hash-vzorek-zmena.txt`. V kopii změňte právě jeden viditelný znak, například tečku na vykřičník. Neměňte kódování ani konce řádků, pokud to editor umožňuje.
3. Zapište předpověď: budou se hashe lišit na jedné pozici, v několika znacích, nebo téměř celé?

**Měření v PowerShellu**

1. V Průzkumníku otevřete složku se soubory, klikněte do adresního řádku, napište `powershell` a stiskněte Enter.
2. Spusťte `Get-Item .\5-1-hash-vzorek*.txt | Select-Object Name,Length` a zapište velikosti souborů.
3. Pro původní soubor spusťte `Get-FileHash -Algorithm SHA256 -LiteralPath '.\5-1-hash-vzorek.txt'`.
4. Příkaz zopakujte pro změněnou kopii. Výstupy kopírujte přesně; jediný přehlédnutý znak znehodnotí porovnání.
5. Označte stejné pozice v obou 64znakových řetězcích. Nemusí jich být přesně polovina – lavinový efekt je statistická vlastnost, ne pravidlo pro každou jednotlivou dvojici.

**Nezávislá kontrola**

1. Otevřete CyberChef. Do levého pole vložte vždy obsah jednoho připraveného souboru a do receptu přetáhněte operaci `SHA2`.
2. Nastavte variantu 256. Ověřte, že výsledek odpovídá PowerShellu. Pokud ne, zkontrolujte konce řádků a to, zda CyberChef zpracovává přesně stejné bajty.
3. Do CyberChef nevkládejte skutečné dokumenty. Pro tento experiment stačí veřejný cvičný text.

| Soubor | Velikost v bajtech | SHA-256 | Počet shodných pozic |
|---|---:|---|---:|
| původní | | | |
| změněný | | | |

**Vyhodnocení**

Napište dvě přesné věty: „Shodný SHA-256 s velmi vysokou jistotou dokládá…“ a „Shodný SHA-256 sám nedokládá…“. Nakonec navrhněte, jak by vydavatel aplikace mohl hash zveřejnit tak, aby útočník nemohl snadno nahradit současně aplikaci i kontrolní údaj – například na zabezpečeném oficiálním webu a navíc s digitálním podpisem.

</details>

## Experiment 5.2: Trezor v jednom souboru

**Cíl:** Vytvořit archiv chráněný silným šifrováním, prakticky odlišit šifrování obsahu od skrytí názvů souborů a ověřit úspěšné rozšifrování pomocí hashe.

**Nástroj:** Bezplatný open-source program [7-Zip](https://www.7-zip.org/) ve Windows a připravená [cvičná tajná zpráva](./materialy/5-2-tajna-zprava.txt). 7z archiv používá pro šifrování AES-256.

**Úkoly:**

1. Vytvořte dva cvičné archivy: první se zašifrovaným obsahem, druhý navíc se zapnutou volbou šifrování názvů souborů.
2. Porovnejte, co lze bez hesla zjistit o obou archivech, a vyzkoušejte rozbalení s chybným a správným heslem.
3. Ověřte hashem, že rozšifrovaný soubor je bajtově shodný s originálem, a popište, co šifrovaný archiv nechrání.

**Výstupy:** Dva archivy bez citlivých dat; srovnávací tabulka viditelných metadat; SHA-256 originálu a obnovené kopie; tři zásady bezpečného předání hesla.

<details>

<summary>**🧠 Rozbalit článek: Pevný trezor se slabým kódem je stále slabý trezor**</summary>

**Šifrování mění čitelná data na nerozpoznatelný text**

Při symetrickém šifrování používá odesílatel i příjemce stejné tajemství – klíč. Je to podobné jako schránka, od níž mají oba kopii stejného klíče. Algoritmus AES je dnes běžným stavebním prvkem ochrany archivů, disků i síťové komunikace. Číslo 256 označuje délku klíče, nikoli délku hesla, počet kol ani záruku bezpečnosti celého postupu.

Člověk obvykle nezadává náhodný 256bitový klíč, ale zapamatovatelné heslo. Program z něj klíč odvodí. Zde vzniká nejčastější slabina: útočník nemusí „prolomit AES“, pokud může rychle zkoušet hesla jako `123456`, jméno školy nebo známý citát. Dlouhá jedinečná přístupová fráze je jako mnoho západek najednou. Ve skutečném životě ji ukládáme do správce hesel, nikoli na papírek přilepený k archivu.

**Zašifrovaný obsah nemusí znamenat skrytý obsah**

Archiv může chránit bajty souboru, ale ponechat viditelný jeho název, velikost či počet položek. Název `vysledky-onkologie-Novak.pdf` prozradí mnoho, i když dokument nelze otevřít. Formát 7z proto nabízí také šifrování hlaviček, v rozhraní označené jako **Encrypt file names**. Experiment se dvěma archivy zviditelní rozdíl mezi důvěrností obsahu a únikem metadat.

Ani správně zašifrovaný archiv nevymaže původní nezašifrovaný soubor, neskryje, že nějaký archiv existuje, a neochrání počítač, na kterém už útočník čte stisknuté klávesy. Kdo obdrží heslo stejným kompromitovaným e-mailem jako archiv, získal obě poloviny řešení. Šifrování je důležitá vrstva, ne kouzelný neviditelný plášť.

**Jak poznáme, že jsme zprávu dostali zpět správně?**

Po rozbalení může text vypadat v pořádku, ale spolehlivější je znovu spočítat hash a porovnat jej s originálem. Tím spojíme důvěrnost a integritu v jednom experimentu. Moderní šifrovací formáty obvykle obsahují i mechanismus, který odhalí chybné heslo nebo pozměnění zašifrovaných dat. Přesto je kontrola výstupu rozumnou součástí obnovy – stejně jako u zálohy není úspěchem vytvořený soubor, ale ověřená možnost jej použít.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Instalace a příprava**

1. Je-li 7-Zip již na školním počítači, použijte nainstalovanou verzi. Jinak jej stáhněte výhradně z [oficiálního webu 7-Zip](https://www.7-zip.org/download.html); instalaci na spravovaném zařízení provede učitel nebo správce.
2. Uložte [cvičný text](./materialy/5-2-tajna-zprava.txt) do prázdné pracovní složky. Spočítejte jeho SHA-256 a hodnotu odložte do protokolu.
3. Pro celý experiment použijte veřejnou laboratorní frázi `LAB-5-2-Modry-Mesic-47!`. Je napsaná v učebnici, a proto **není tajná a nesmí být použita nikde jinde**.

**Archiv A – obsah je šifrovaný, názvy jsou vidět**

1. Klikněte pravým tlačítkem na soubor, zvolte nabídku 7-Zip a `Add to archive…`.
2. Jako formát zvolte `7z`, archiv pojmenujte `5-2-obsah.7z` a v části Encryption vyberte `AES-256`.
3. Dvakrát zadejte laboratorní frázi. Volbu `Encrypt file names` zatím nechte vypnutou a archiv vytvořte.
4. Otevřete archiv bez rozbalení. Zapište, zda je vidět název souboru, jeho velikost a další údaje. Pokus o otevření obsahu by měl vyžádat heslo.

**Archiv B – šifrovaná je i hlavička**

1. Postup zopakujte, ale archiv pojmenujte `5-2-vcetne-nazvu.7z` a zapněte `Encrypt file names`.
2. Pokuste se zobrazit seznam souborů bez hesla. Porovnejte výsledek s archivem A.
3. U jednoho archivu nejprve zadejte záměrně chybné heslo. Zapište přesnou reakci programu; neposuzujte ji jen slovem „nefungovalo“.

**Obnova a kontrola**

1. Vytvořte složku `obnoveno`, archiv B do ní rozbalte se správnou laboratorní frází a otevřete obnovený text.
2. Spočítejte SHA-256 obnoveného souboru. Musí se rovnat hashi originálu. Pokud se liší, zkontrolujte, zda jste hashovali správné soubory a text po rozbalení znovu neuložili v editoru.
3. Do tabulky zapište, zda jsou bez hesla vidět: název, počet položek, velikost položky a její obsah.

| Pozorování bez hesla | Archiv A | Archiv B |
|---|---|---|
| název souboru | | |
| počet položek | | |
| velikost položky | | |
| obsah souboru | | |

**Závěr**

Navrhněte bezpečnější skutečný postup: archiv poslat jedním kanálem, heslo sdělit jiným ověřeným kanálem, použít jedinečnou dlouhou frázi a po doručení obě strany informovat, jak dlouho budou kopie uchovávat. Cvičné archivy můžete po kontrole odstranit; neobsahují skutečné tajemství.

</details>

## Experiment 5.3: Občanský průkaz webu

**Cíl:** Prozkoumat certifikát HTTPS serveru, přečíst jeho identitu, vydavatele, platnost a řetězec důvěry a správně vymezit, co ikona zabezpečeného spojení dokazuje.

**Nástroj:** Aktuální webový prohlížeč a stabilní demonstrační web [https://example.com](https://example.com). Přesné názvy položek se mezi prohlížeči liší; není třeba instalovat rozšíření.

**Úkoly:**

1. Otevřete certifikát serveru a zaznamenejte subjekt/domény, vydavatele, dobu platnosti, algoritmus podpisu a veřejný klíč.
2. Nakreslete řetězec od serverového certifikátu přes mezilehlou certifikační autoritu ke kořenové autoritě.
3. Vysvětlete, proč platné HTTPS chrání spojení, ale samo nepotvrzuje pravdivost, poctivost ani bezpečný obsah webu.

**Výstupy:** Vyplněná karta certifikátu; schéma řetězce důvěry; vysvětlení kontroly názvu, času a podpisu; tři tvrzení, která z platného HTTPS nelze odvodit.

<details>

<summary>**🧠 Rozbalit článek: Jak prohlížeč pozná správné dveře**</summary>

**Šifrovaný tunel potřebuje ceduli se jménem**

Kdyby prohlížeč pouze zašifroval spojení s prvním serverem, který odpoví, mohl by bezpečně šeptat přímo útočníkovi. TLS proto řeší nejen důvěrnost a integritu přenosu, ale také ověření identity serveru. Server předloží digitální certifikát: datový dokument spojující veřejný klíč s názvem domény a dobou platnosti.

Prohlížeč kontroluje několik věcí zároveň. Odpovídá navštívený název některému jménu v certifikátu? Není certifikát před začátkem nebo po konci platnosti? Podepsala jej autorita, které systém důvěřuje? Lze podpisy propojit až ke známému kořenovému certifikátu? Teprve kombinace kontrol vytváří důvěryhodný řetězec.

**Hierarchie podpisů místo telefonátu každému serveru**

Kořenové certifikační autority jsou předem uložené v operačním systému nebo prohlížeči. Kořen obvykle nepodepisuje každý web přímo; podepíše mezilehlou autoritu a ta vydává serverové certifikáty. Je to podobné jako ověřená matrika, která zmocní pobočku vydávat určité doklady. Omezuje se tím každodenní použití nejcitlivějšího kořenového klíče.

Digitální podpis certifikátu umožní ověřit, že jeho údaje po vydání nikdo nezměnil a že jej podepsal držitel odpovídajícího soukromého klíče. Veřejný klíč serveru se pak podílí na bezpečném navázání relace. Samotná data webu jsou během spojení šifrována rychlejší symetrickou kryptografií – asymetrické a symetrické metody tu nehrají proti sobě, ale tvoří tým.

**Zámeček není recenze podniku**

Platný certifikát pro `podvod.example` by dokazoval pouze to, že prohlížeč vytvořil chráněné spojení k doméně `podvod.example`, pokud její provozovatel doménu ovládá a získal certifikát. Neříká, že obchod pošle zaplacené zboží, článek obsahuje pravdu nebo stažený program neobsahuje chybu.

Proto moderní prohlížeče ikonu zámku upozadily. HTTPS je očekávaný základ bezpečného přenosu, nikoli medaile za důvěryhodnost. Naopak varování před neplatným certifikátem není dekorace. Může vzniknout chybným časem, špatnou konfigurací i útokem; student je nemá obcházet, ale zaznamenat a předat správci.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Otevření certifikátu**

1. Zkontrolujte správný čas zařízení a otevřete přesnou adresu `https://example.com`. Adresu napište ručně nebo použijte odkaz z této stránky.
2. V Chromiu/Edge klikněte na ikonu nastavení webu vlevo od adresy, otevřete informace o připojení a položku certifikátu. Ve Firefoxu bývá cesta přes ikonu vlevo od adresy, informace o zabezpečeném spojení a zobrazení certifikátu. Rozhraní se může měnit; hledejte údaje o certifikátu, nikoli návody k vypnutí ochrany.
3. Pokud síť používá oprávněnou školní TLS inspekci, vydavatel může být školní autorita. Tento rozdíl zaznamenejte a konzultujte s učitelem – právě to je zajímavý příklad změny řetězce důvěry.

**Karta certifikátu**

Zapište údaje vlastními slovy; neopisujte dlouhé sériové číslo ani celý veřejný klíč.

| Pole | Zjištěná hodnota | Co bezpečnostně znamená |
|---|---|---|
| navštívený hostitel | | jméno, které musí certifikát pokrývat |
| DNS jména / SAN | | identity povolené certifikátem |
| vydavatel | | autorita, která certifikát podepsala |
| platnost od–do | | časové okno důvěry |
| algoritmus podpisu | | způsob ověření podpisu vydavatele |
| typ a délka veřejného klíče | | veřejná část identity serveru |

**Řetězec důvěry**

1. Otevřete zobrazení `Certification Path`, `Certificate hierarchy` nebo podobnou položku.
2. Nakreslete tři patra: kořenová autorita → mezilehlá autorita → certifikát `example.com`. Pokud má váš řetězec jiný počet pater, nakreslete skutečnost.
3. Ke každé šipce napište „digitální podpis“. Ke kořenu napište, odkud mu prohlížeč důvěřuje.
4. Najděte doménu mezi alternativními názvy certifikátu. Pouhá podobnost jmen nestačí: certifikát pro jinou doménu není certifikátem pro právě navštívenou.

**Interpretace scénářů**

Rozhodněte, kterou kontrolu by porušil: certifikát včera vypršel; certifikát je platný, ale pro jinou doménu; řetězec končí neznámým kořenem; spojení je platné, ale web prodává neexistující vstupenky. U posledního scénáře vysvětlete, proč TLS může fungovat dokonale a web přesto podvádět. Žádné skutečné varování v rámci experimentu neobcházejte.

</details>

## Experiment 5.4: Rentgen TLS serveru

**Cíl:** Analyzovat veřejnou konfiguraci HTTPS serveru z více hledisek, interpretovat známku skeneru a navrhnout opravu, která nepoškodí potřebnou kompatibilitu.

**Nástroj:** Bezplatná služba [Qualys SSL Labs – SSL Server Test](https://www.ssllabs.com/ssltest/) a předem schválená veřejná doména, například `example.com`. Test směřuje pouze na veřejný server, nikdy na interní adresu ani cizí náhodně zvolený cíl.

**Úkoly:**

1. Spusťte nebo otevřete již uložený výsledek testu schválené domény a zaznamenejte celkovou známku i hlavní důvody.
2. Prozkoumejte podporované verze protokolu, certifikát, výměnu klíčů a simulaci klientů.
3. Vyberte jednu skutečnou slabinu nebo kompromis kompatibility a napište doporučení včetně možného vedlejšího dopadu.

**Výstupy:** Stručná zpráva s datem měření, známkou a čtyřmi důkazy; tabulka podporovaných klientů/protokolů; prioritizované doporučení a omezení vzdáleného testu.

<details>

<summary>**🧠 Rozbalit článek: Známka A není konec vyšetřování**</summary>

**Server nabízí menu, klient si vybírá společnou možnost**

TLS není jeden neměnný algoritmus. Klient a server při navázání spojení vyjednávají verzi protokolu a sadu kryptografických mechanismů. Starý klient nemusí znát moderní varianty; server, který kvůli kompatibilitě ponechá historické protokoly, zase rozšiřuje prostor pro útok. Správce proto řeší skutečný kompromis: koho ještě podporovat a jaké riziko je přitom přijatelné.

V dnešních konfiguracích se očekávají moderní verze TLS a bezpečné algoritmy. Důležitá je také **dopředná bezpečnost**: kompromitace dlouhodobého soukromého klíče serveru by neměla zpětně odemknout dříve zachycené relace. Toho lze dosáhnout dočasnými klíči vytvořenými pro jednotlivá spojení. Je to, jako kdyby hotel po každém hostu nejen vyměnil kartu, ale použil úplně nový zámek, jehož starý stav nelze obnovit z hlavního klíče.

**Co vlastně skener vidí**

SSL Labs se připojuje z internetu a zkoumá, co server nabízí: certifikační řetězec, protokoly, šifry, některé známé zranitelnosti a chování pro různé simulované klienty. Výsledek převádí na známku, aby upozornil na konfigurace vyžadující pozornost. Zelené písmeno je užitečný souhrn, ne matematický důkaz bezpečnosti.

Vzdálený skener nevidí, zda aplikace po přihlášení správně kontroluje oprávnění, zda databáze uniká jinou cestou, zda server bezpečně uchovává soukromý klíč ani zda provozovatel reaguje na incidenty. Může také testovat jiný uzel rozsáhlé distribuční sítě, než jaký používá konkrétní návštěvník. Datum a rozsah testu proto musí být součástí závěru.

**Oprava může někoho odříznout**

Vypnout zastaralý protokol zní jednoznačně správně, ale staré zařízení se pak nemusí připojit. Bezpečnostní doporučení má proto obsahovat vlastníka, prioritu, test kompatibility a plán návratu. Někdy je lepší starého klienta nahradit; jindy musí organizace dočasně použít oddělenou přechodovou službu. Dobrá analýza neříká jen „červené políčko špatně“, ale popisuje riziko a proveditelný další krok.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Bezpečné vymezení testu**

1. Učitel určí veřejné jméno serveru, které je dovoleno analyzovat. Výchozí demonstrační cíl může být `example.com`; nepoužívejte IP adresy školní sítě, domácí router ani náhodný cizí web.
2. Na stránce SSL Server Test zadejte pouze název hostitele bez cesty a přihlašovacích údajů. Je-li k dispozici volba nezobrazovat výsledek na veřejných přehledech, zapněte ji.
3. Test může trvat několik minut. Pokud je služba nedostupná nebo učitel nechce spouštět nové měření, použijte učitelem uložený výsledek. Nevytvářejte opakované testy ve smyčce.

**Čtení výsledku od celku k důkazu**

1. Zapište čas, cílový hostitel, nalezené adresy a celkovou známku. Pokud má více serverů různé výsledky, nepřepisujte je jedním průměrem.
2. V části certifikátu porovnejte domény, vydavatele, platnost a důvěryhodnost řetězce s pozorováním z experimentu 5.3.
3. V konfiguraci protokolů zaznamenejte podporu TLS 1.2 a TLS 1.3 a případnou podporu historických SSL/TLS. Barvu políčka vždy přeložte do věty, co přesně server přijímá.
4. Najděte údaj o dopředné bezpečnosti a simulaci navázání spojení různými klienty. Vyberte jeden moderní a jeden nejstarší simulovaný klient a porovnejte, zda se připojí a s jakým protokolem.
5. Prohlédněte upozornění na známé zranitelnosti. „Not vulnerable“ znamená, že konkrétní test daný problém neprokázal, nikoli že server nemá žádnou zranitelnost.

| Důkaz | Zjištění | Význam | Priorita |
|---|---|---|---|
| celková známka | | orientační souhrn | |
| verze protokolů | | kompatibilita a riziko | |
| řetězec certifikátu | | identita serveru | |
| dopředná bezpečnost | | ochrana starších relací | |
| simulovaný klient | | praktická kompatibilita | |

**Doporučení**

Napište jedno doporučení ve formátu: „Protože test dne … zjistil …, správce by měl …; před změnou musí ověřit …; úspěch se pozná podle …“. Připojte alespoň dvě omezení: skener hodnotí zvenčí jen TLS vrstvu a výsledek zachycuje konkrétní okamžik a konkrétní síťový uzel.

</details>

## Experiment 5.5: Tajná zásilka bez společného hesla

**Cíl:** Prakticky použít dvojici veřejného a soukromého klíče k zašifrování a rozšifrování zprávy a vysvětlit, proč důvěrnost bez ověření identity nezabrání útoku prostředníka.

**Nástroj:** Bezplatný [CyberChef](https://gchq.github.io/CyberChef/) s operacemi OpenPGP a připravená [cvičná zpráva](./materialy/5-5-pgp-zprava.txt). Všechny klíče vznikají pouze pro tento experiment a po něm se zahodí.

**Úkoly:**

1. Ve dvojici vytvořte cvičný pár OpenPGP klíčů a jasně oddělte veřejnou a soukromou část.
2. Předáním pouze veřejného klíče zašifrujte spolužákovi připravenou zprávu; příjemce ji rozšifruje soukromým klíčem.
3. Proveďte neúspěšný pokus s cizím klíčem a navrhněte způsob ověření otisku veřejného klíče.

**Výstupy:** Veřejný klíč a zašifrovaná cvičná zpráva; záznam úspěšného a neúspěšného rozšifrování; schéma toku klíčů; vysvětlení hybridního šifrování a útoku prostředníka.

<details>

<summary>**🧠 Rozbalit článek: Otevřená schránka, kterou zamkne každý a odemkne jediný člověk**</summary>

**Jak poslat tajemství bez předchozího tajemství**

U symetrického šifrování narážíme na otázku: jak bezpečně předat společný klíč člověku na druhém konci internetu? Asymetrická kryptografie používá matematicky svázanou dvojici. **Veřejný klíč** lze zveřejnit; **soukromý klíč** musí zůstat u vlastníka. Zprávu zašifrovanou pro veřejný klíč má umět rozšifrovat pouze odpovídající soukromý klíč.

Připomíná to schránku s otevřeným vhozem. Každý do ní může vložit zásilku a zaklapnout dvířka, ale vybrat ji dokáže jen majitel s klíčem. Metafora má hranice – skutečné algoritmy stojí na matematických problémech a správném softwaru – dobře však ukazuje, proč veřejný klíč nemusíme skrývat.

**Velkou zprávu ve skutečnosti zamyká rychlý dočasný klíč**

Asymetrické operace jsou výpočetně náročnější a nešifrují se jimi běžně celé velké soubory. OpenPGP proto využívá hybridní postup. Pro zprávu vytvoří náhodný symetrický relační klíč, jím zašifruje data a teprve tento malý klíč ochrání veřejným klíčem příjemce. V balíčku cestuje zašifrovaná zpráva i zašifrovaný relační klíč.

Stejný princip různými způsoby potkáme v TLS i zabezpečených komunikátorech: asymetrická kryptografie řeší identitu a dohodu klíčů, symetrická efektivně chrání proud dat. Pojmy veřejný a soukromý klíč tedy neznamenají, že každý bajt internetu prochází pomalou „veřejnou“ šifrou.

**Čí veřejný klíč jsme vlastně dostali?**

Když útočník nahradí veřejný klíč příjemce svým, odesílatel vytvoří dokonale zašifrovanou zprávu – ale pro útočníka. Potom ji prostředník může přečíst a znovu zašifrovat pravému adresátovi. Matematika funguje; selhalo přiřazení klíče k člověku.

Proto se ověřuje **otisk klíče** jiným důvěryhodným kanálem: osobně, videohovorem se známou osobou, přes podepsaný profil nebo v zavedeném systému důvěry. Jméno a e-mail ve vygenerovaném klíči nejsou samy o sobě průkaz totožnosti – kdokoli může napsat libovolný text. Soukromý klíč se naopak neposílá vůbec. Kdo jej získá, může číst zprávy určené jeho držiteli a podle způsobu použití se za něj i vydávat.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Role a cvičná identita**

1. Pracujte ve dvojici jako Alex a Bára. Nepoužívejte skutečný e-mail; cvičné identity mohou být `alex@example.com` a `bara@example.com`.
2. Otevřete CyberChef. Je-li operace `Generate PGP Key Pair` v nabídce, použijte ji k vytvoření dočasné dvojice pro Báru. Pokud ji aktuální verze nenabízí, použijte dvojici klíčů připravenou učitelem; nevkládejte do webu žádný skutečný klíč.
3. Ve výstupu jasně označte blok `PUBLIC KEY` a blok `PRIVATE KEY`. Soukromou část uloží Bára jen ve své pracovní relaci. Alex dostane pouze veřejný blok.
4. Zaznamenejte otisk veřejného klíče, pokud jej nástroj zobrazuje. Celý soukromý klíč ani jeho snímek se neodevzdává.

**Zašifrování u Alexe**

1. Alex otevře [cvičnou zprávu](./materialy/5-5-pgp-zprava.txt) a vloží její veřejný obsah do vstupu CyberChef.
2. Do receptu přidá operaci `PGP Encrypt` nebo `OpenPGP Encrypt` podle aktuálního názvu a vloží **veřejný** klíč Báry do příslušného pole.
3. Výstup bude blok zašifrovaného textu. Alex zkontroluje, že v něm nelze prostým čtením najít původní větu, a předá celý blok Báře.

**Rozšifrování u Báry**

1. Bára vloží zašifrovaný blok do vstupu, zvolí operaci `PGP Decrypt` a použije svůj dočasný soukromý klíč.
2. Porovná obnovený text s připravenou zprávou znak po znaku. Úspěch není jen absence chybové hlášky, ale přesná shoda obsahu.
3. Potom se pokusí zprávu rozšifrovat jiným cvičným soukromým klíčem od učitele nebo druhé dvojice. Zaznamená reakci, ale žádné soukromé klíče si dvojice trvale nevyměňují.

**Ověření identity a úklid**

Nakreslete tok: veřejný klíč Báry → Alex; otevřená zpráva + veřejný klíč → šifrovaný balíček; balíček + soukromý klíč Báry → zpráva. Potom doplňte, kde by prostředník mohl vyměnit veřejný klíč a jak by tomu zabránilo porovnání otisku osobně. Zavřete kartu CyberChef a smažte dočasné klíče z pracovních souborů. Online demonstrace není vhodná pro skutečně citlivou kryptografii ani dlouhodobé klíče.

</details>

## Experiment 5.6: Ověřujeme člověka, ne jen zámek

**Cíl:** Vysvětlit a bezpečně předvést ověření bezpečnostního čísla v end-to-end šifrované komunikaci a správně reagovat na změnu identity zařízení.

**Nástroj:** Bezplatná aplikace [Signal](https://signal.org/) a její [oficiální návod k bezpečnostnímu číslu](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed) ve dvojici, která Signal již dobrovolně používá, nebo učitelská demonstrace podle [připraveného protokolu](./materialy/5-6-e2ee-protokol.md). Kvůli experimentu si nikdo nemusí zakládat účet ani sdílet telefonní číslo.

**Úkoly:**

1. Otevřete bezpečnostní číslo stejné konverzace na dvou zařízeních a ověřte jej osobně QR kódem nebo porovnáním jiným důvěryhodným kanálem.
2. Zaznamenejte pouze výsledek shody, nikdy celý QR kód ani bezpečnostní číslo.
3. Vysvětlete, proč se číslo může legitimně změnit, jak má uživatel reagovat a jaká metadata E2EE samo neukrývá.

**Výstupy:** Anonymizovaný protokol shody; postup reakce na změnu bezpečnostního čísla; diagram „zařízení A – server – zařízení B“ s označením, kdo může číst obsah a jaká metadata mohou zůstat viditelná.

<details>

<summary>**🧠 Rozbalit článek: Zapečetěná obálka a neověřený kurýr**</summary>

**Konce šifrují, server přenáší**

Při end-to-end šifrování vzniká čitelná zpráva na zařízení odesílatele a znovu se objeví až na zařízení příjemce. Server přenáší šifrovaný obsah, ale nemá mít klíč potřebný k jeho přečtení. To je zásadní rozdíl proti spojení, které je šifrované jen mezi uživatelem a serverem: tam může provozovatel zprávu na serveru zpracovat v otevřené podobě.

„End-to-end“ však musí mít konkrétní konce. Je protějškem opravdu telefon kamaráda, nebo zařízení člověka, který se za něj vydává? Bez ověření identity by útočník ovládající směrování či registrační proces mohl zkusit vložit vlastní klíč. Signal proto pro dvojici účastníků vytváří **bezpečnostní číslo** a jeho QR podobu. Shoda na obou stranách je důkazem, že ověřujeme stejné kryptografické identity.

**Proč použít jiný kanál**

Poslat bezpečnostní číslo v téže neověřené konverzaci je jako požádat podezřelého kurýra, aby sám potvrdil, že zásilku nevyměnil. Silnější je porovnat QR kódy osobně nebo číslo ověřit hovorem, v němž spolehlivě poznáme druhého člověka. Důležité není opsat desítky číslic do školního protokolu; důležité je provést porovnání a zaznamenat jeho výsledek.

Bezpečnostní číslo se může změnit z legitimních důvodů – například po výměně telefonu nebo přeinstalaci aplikace. Změna není automatický důkaz útoku, ale důvod k novému ověření, zejména před citlivou konverzací. Správná reakce zní „pozastavit citlivé sdílení a ověřit“, nikoli „zpanikařit“ ani „upozornění vždy ignorovat“.

**Šifrovaný obsah není neviditelná komunikace**

E2EE chrání obsah při přenosu, ne všechny okolnosti komunikace. Podle systému a situace může být patrné, že určitá zařízení komunikují, kdy se připojila nebo jak velká data přenášejí. Zprávu může také přečíst člověk, který odemkne některý koncový telefon, uvidí náhled v oznámení nebo získá nezabezpečenou zálohu. Bezpečný komunikátor proto nenahrazuje zámek obrazovky, aktualizace, opatrnost vůči propojeným zařízením a rozumné zacházení s citlivým obsahem.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Volba bezpečné varianty**

1. Praktickou variantu provedou pouze dva lidé, kteří Signal už používají, navzájem se znají a dobrovolně chtějí otevřít svou společnou konverzaci. Neposílají žádný soukromý obsah a nesdělují čísla ostatním.
2. Všichni ostatní pracují s dvojicí demonstračních zařízení nebo se snímky připravenými učitelem. Hodnotí postup stejně plnohodnotně; instalace aplikace není podmínkou splnění úkolu.
3. Otevřete [protokol](./materialy/5-6-e2ee-protokol.md). Do jmen použijte role `zařízení A` a `zařízení B`, nikoli telefonní čísla.

**Ověření bezpečnostního čísla**

1. Na obou zařízeních otevřete tutéž individuální konverzaci. V informacích o kontaktu zvolte položku pro zobrazení bezpečnostního čísla. Přesný název se může podle verze lišit.
2. Stojí-li účastníci vedle sebe, jedno zařízení naskenuje QR kód z displeje druhého. Alternativně porovnají zobrazené číselné skupiny nahlas přes předem ověřený hovor.
3. Ověřte shodu na **obou** zařízeních. Pokud aplikace dovoluje kontakt označit jako ověřený, proveďte to až po úspěšném porovnání.
4. Do protokolu napište pouze `shoda`, `neshoda` nebo `demonstrace`. QR kód nefotografujte a celé bezpečnostní číslo nekopírujte.

**Model změny identity**

1. Zařízení se kvůli cvičení nepřeinstalovává. Učitel pouze předloží scénář: „Bára má nový telefon a aplikace oznámila změnu bezpečnostního čísla.“
2. Seřaďte reakce: přerušit posílání citlivých zpráv; kontaktovat Báru známým kanálem; zjistit, zda zařízení skutečně změnila; znovu porovnat číslo; teprve potom pokračovat.
3. Vysvětlete, proč samotná změna neprokazuje útok a proč její bezmyšlenkovité potvrzení ruší smysl kontroly.

**Diagram a závěr**

Nakreslete tři uzly: A, přenosový server a B. Plnou čarou označte šifrovaný obsah, klíče ponechte na koncích. Přerušovaně vyznačte možná metadata, například čas a velikost přenosu. Přidejte útočníka s odemčeným zařízením a vysvětlete, proč v tomto případě kvalitní E2EE nestačí. Odevzdejte jen anonymizovaný protokol a diagram.

</details>

## Závěrečná kryptografická mapa

Po dokončení přiřaďte ke každému experimentu vlastnost, kterou primárně ověřoval: **integritu, důvěrnost, autenticitu, správu klíčů nebo bezpečnost přenosu**. Některé experimenty patří do více sloupců – právě to je správné zjištění. Skutečný bezpečný systém nevzniká volbou jednoho „nejsilnějšího“ algoritmu, ale správným spojením algoritmů, klíčů, identity, nástrojů a lidského postupu.
