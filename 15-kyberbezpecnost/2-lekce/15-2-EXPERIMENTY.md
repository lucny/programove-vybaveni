<!--
author: Marek Lučný
title: Malware a sociální inženýrství – praktická laboratoř
language: cs
mode: Textbook
comment: Šest bezpečně vedených experimentů ke druhé lekci okruhu Kyberbezpečnost.
-->

# Praktická laboratoř: Malware a sociální inženýrství

Malware nemusí do počítače prorazit dveře. Často mu je otevře člověk, který uvěřil naléhavé zprávě, zaměnil podvrženou adresu za pravou nebo spustil soubor vydávající se za něco užitečného. V šesti experimentech si proto vyzkoušíte nejen technické nástroje, ale hlavně **způsob rozhodování, který útok přeruší dříve, než začne škodit**.

> **🛡️ Bezpečnostní pravidlo laboratoře**
>
> Nestahujte skutečný malware, neotvírejte neznámé přílohy, nenavštěvujte podezřelé adresy a nikam nevkládejte skutečná hesla, osobní údaje ani neveřejné soubory. Používejte pouze připravené neškodné materiály a fiktivní adresy s koncovkou `.example`. Narazíte-li při práci na skutečně podezřelý soubor nebo zprávu, dále s nimi nemanipulujte a informujte učitele nebo správce.

## Jak pracovat

U každého experimentu nejprve zapište předpověď. Během práce oddělujte **pozorování** od **interpretace**: text hlavičky, vypočtený hash nebo skutečný název domény je pozorování; tvrzení, co znamená, je interpretace. Žádný jednotlivý signál neposkytuje stoprocentní jistotu.

```text
Předpověď:
Pozorování nebo důkaz:
Vysvětlení odborným pojmem:
Rozhodnutí a navržená reakce:
Omezení výsledku:
```

| Experiment | Hlavní pojem | Nástroj | Orientační čas |
|---|---|---|---:|
| 2.1 Digitální otisk souboru | hash, detekce, falešný poplach | PowerShell / CyberChef, VirusTotal | 35 min |
| 2.2 Phishing pod časovým tlakem | phishing, doména, manipulace | Jigsaw Phishing Quiz | 30 min |
| 2.3 URL pod mikroskopem | části URL, kódování, přesměrování | CyberChef | 35 min |
| 2.4 Detektiv e-mailových hlaviček | SPF, DKIM, DMARC, Received | textový editor / Messageheader | 40 min |
| 2.5 Laboratoř psychologického nátlaku | pretexting, smishing, vishing, baiting | připravené karty, stopky | 35 min |
| 2.6 Rekonstrukce malwarového incidentu | útočný řetězec, trojan, infostealer | karty / diagrams.net | 45 min |

## Experiment 2.1: Digitální otisk a vícezdrojová kontrola souboru

**Cíl:** Vypočítat kryptografický otisk souboru, pozorovat jeho změnu po nepatrné úpravě a kriticky interpretovat výsledek více detekčních nástrojů.

**Nástroj:** Vestavěný příkaz `Get-FileHash` ve Windows PowerShellu nebo bezplatná webová aplikace [CyberChef](https://gchq.github.io/CyberChef/) a služba [VirusTotal](https://www.virustotal.com/gui/home/upload). Pracuje se pouze s připraveným neškodným textovým souborem.

**Úkoly:**

1. Vypočítejte SHA-256 původního vzorku a jeho kopie, ve které změníte jediný znak.
2. Porovnejte oba otisky a vysvětlete, proč se výrazně liší, přestože soubory vypadají téměř stejně.
3. Prověřte pouze původní neškodný vzorek ve VirusTotal a výsledek interpretujte bez ukvapeného výroku „bezpečný“ či „nebezpečný“.

**Výstupy:** Tabulka se dvěma hashi, záznam výsledku z VirusTotal, vysvětlení rozdílu mezi identifikací a detekcí a dvě omezení provedeného ověření.

<details>

<summary>**🧠 Rozbalit článek k tématu: Otisk není rozsudek**</summary>

**Soubor dostává téměř jedinečnou poznávací značku**

Kdybychom chtěli popsat soubor pouze názvem, daleko bychom nedošli. Soubor `faktura.pdf` lze během sekundy přejmenovat na `fotografie.jpg`; jméno se změnilo, obsah nikoli. Kryptografická hashovací funkce proto přečte obsah souboru a vypočítá z něj řetězec pevné délky – **hash** neboli digitální otisk. U SHA-256 má podobu 64 šestnáctkových znaků.

Dobrá hashovací funkce se chová trochu jako mimořádně citlivý mixér. Vhodíte téměř stejnou směs, ale jediná změněná ingredience promění celý výsledný vzor. Této vlastnosti se říká lavinový efekt. Z hashe se přitom prakticky nedá zpětně sestavit původní obsah a je krajně nepravděpodobné, že dva různé běžné soubory vytvoří stejný SHA-256.

Hash se používá ke kontrole integrity staženého obrazu operačního systému, k porovnávání záloh, k vyhledávání známých souborů v bezpečnostních databázích i při digitální forenzní analýze. Je však důležité nepřisoudit mu kouzelnou moc. Hash říká: „Tyto bajty odpovídají tomuto otisku.“ Neříká: „Tento program je poctivý.“ Škodlivý i neškodný soubor může mít dokonale platný hash.

**Proč se bezpečnostní nástroje někdy neshodnou**

Antivirový program může hledat známou **signaturu**, tedy charakteristický vzor již popsaného malwaru. Může také používat heuristiku, model strojového učení nebo pozorovat chování programu v izolovaném prostředí. Každý výrobce používá jiné metody, databáze a prahové hodnoty. Výsledky proto nemusí být stejné.

VirusTotal shromažďuje výstupy více bezpečnostních nástrojů na jednom místě. Je to podobné jako panel odborníků: shoda mnoha nezávislých hlasů je užitečný signál, ale počet hlasů sám nenahrazuje kontext. Jediná detekce může být **falešně pozitivní výsledek**, například záměna neobvyklého legitimního nástroje za hrozbu. Nula detekcí zase není důkaz neviny: zcela nový malware ještě nemusí být známý a některé škodlivé vlastnosti se projeví až za určitých podmínek.

Ptejte se proto: Odkud soubor pochází? Očekával jsem jej? Souhlasí jeho hash s údajem od důvěryhodného vydavatele? Je digitálně podepsaný? Jak je starý výsledek analýzy? Co přesně nástroje označily? Bez těchto otázek je číslo jen číslem.

**Cizí služba není místo pro soukromé dokumenty**

Při odeslání souboru do online analyzátoru opouští soubor vaše zařízení. Nikdy proto neodesílejte osobní dokumenty, neveřejný zdrojový kód, školní databáze ani skutečné podezřelé přílohy. V tomto experimentu je připraven zvláštní neškodný text bez soukromých údajů. U reálného incidentu se postupuje podle pravidel organizace a soubor předává oprávněnému správci.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Příprava**

1. Stáhněte si [bezpečný vzorek](./materialy/2-1-bezpecny-vzorek.txt). Otevřete jej v textovém editoru a ověřte, že obsahuje pouze výukový text s identifikátorem `PV-KYB-2-1`.
2. Vytvořte jeho kopii s názvem `2-1-bezpecny-vzorek-zmena.txt`. V kopii změňte jediný znak, například tečku na vykřičník, a soubor uložte.
3. Předpovězte, zda se změní několik znaků hashe, jeho polovina, nebo téměř celý hash.

**Postup v PowerShellu**

1. Otevřete Průzkumníka v adresáři se soubory. Klikněte do adresního řádku, napište `powershell` a potvrďte Enter. PowerShell se otevře přímo v dané složce.
2. Pro původní soubor spusťte:

   `Get-FileHash -Algorithm SHA256 -LiteralPath ".\2-1-bezpecny-vzorek.txt"`

3. Stejný příkaz zopakujte s názvem změněné kopie. Oba řetězce zapište nebo bezpečně zkopírujte do protokolu.
4. Nemáte-li PowerShell, otevřete CyberChef, přetáhněte do vstupu vždy jeden připravený soubor a do sloupce Recipe vložte operaci `SHA2` s délkou 256. Používejte jen výukové soubory.

**Kontrola ve VirusTotal**

1. Otevřete VirusTotal a zvolte kartu pro soubor. Přečtěte si upozornění služby a odešlete **výhradně původní připravený vzorek**. Žádný vlastní dokument ani skutečnou přílohu nepoužívejte.
2. Zapište datum, počet hlásících nástrojů a názvy případných detekcí. Rozhraní služby se může změnit; důležitý je význam údajů, nikoli poloha tlačítka.
3. Pokud je odesílání ve školní síti blokováno, předejte učiteli vypočtený hash a pracujte s výsledkem nebo snímkem, který připravil. Experiment není podmíněn založením účtu.

| Soubor | SHA-256 | Co se změnilo | Výsledek detekce |
|---|---|---|---|
| původní vzorek | | nic | |
| změněná kopie | | jeden znak | neodesílá se |

**Ověření a odevzdání**

Ověřte, že oba hashe mají stejnou délku, ale odlišný obsah. K výsledku VirusTotal napište přesnou větu, například: „V okamžiku kontroly žádný použitý nástroj vzorek neoznačil; samo o sobě to nedokazuje bezpečnost libovolného souboru.“ Připojte omezení: služba nemusí znát nové hrozby a textový vzorek nereprezentuje chování spustitelného programu.

</details>

## Experiment 2.2: Phishing pod časovým tlakem

**Cíl:** Rozpoznat phishing pomocí kombinace technických, jazykových a kontextových signálů a vytvořit vlastní postup bezpečného ověření zprávy.

**Nástroj:** Volně dostupný [Jigsaw Phishing Quiz](https://phishingquiz.withgoogle.com/) od společnosti Jigsaw/Google, webový prohlížeč a laboratorní protokol. Do kvízu se nepřihlašuje a používají se pouze fiktivní údaje.

**Úkoly:**

1. Projděte výukové situace v kvízu a u každé rozhodněte dříve, než zobrazíte vysvětlení.
2. U nejméně tří případů zaznamenejte konkrétní důkazy: skutečnou adresu odesílatele, cílovou doménu odkazu, požadovanou akci a použitý psychologický tlak.
3. Sestavte pravidlo `ZASTAV – ZKONTROLUJ – OVĚŘ`, které lze použít i u spear phishingu, smishingu a quishingu.

**Výstupy:** Analytická tabulka tří situací, dvě opravená chybná rozhodnutí nebo dva nejnáročnější případy a stručný osobní kontrolní postup.

<details>

<summary>**🧠 Rozbalit článek k tématu: Phishing neloví hloupé lidi**</summary>

**Útočník soutěží s naší pozorností**

Phishingová zpráva nemusí být plná pravopisných chyb a podivných obrázků. Může napodobit běžný školní e-mail, upozornění cloudové služby nebo zprávu kolegy. Její hlavní zbraní často není technická dokonalost, ale vhodně zvolený okamžik. Když člověk spěchá na autobus, čeká zásilku nebo se bojí zablokování účtu, mozek používá rychlé zkratky.

Autorita, naléhavost, strach, odměna a rutina jsou jako tlačítka na ovládacím panelu pozornosti. „Ředitel potřebuje pomoc.“ „Účet za deset minut zanikne.“ „Vyhráli jste.“ „Tento formulář vyplňujete každý pátek.“ Dobrá obrana proto nezačíná pocitem studu, ale krátkou pauzou. Emoční reakce není důkaz podvodu, je však signálem přepnout z rychlého jednání do ověřování.

**Jméno na obálce není adresa domu**

V e-mailu lze snadno zobrazit důvěryhodně vypadající jméno, zatímco skutečná adresa odesílatele patří jiné doméně. Totéž platí pro odkazy: viditelný text `školní portál` nemusí odpovídat cíli. Rozhodující část webové adresy je název hostitele. Čte se opatrně zleva doprava, ale vlastnickou doménu často nejlépe odhalíme zprava před první lomítko.

Například v adrese `https://portal.skoly.example.utocnik.example/login` není hostitelem `portal.skoly.example`, ale celý řetězec `portal.skoly.example.utocnik.example`; rozhodující doména je zde `utocnik.example`. Tečky před ní vytvářejí pouze poddomény. Útočník spoléhá, že oko zachytí známá slova na začátku a přestane číst.

Technický signál však také není rozsudek. Odesílatel může legitimně používat externí systém, odkaz může vést přes marketingovou či přihlašovací službu a perfektní čeština nic nezaručuje. Potřebujeme **soubor signálů a kontext**: očekával jsem zprávu? Je žádost obvyklá? Chce heslo, kód, peníze nebo spuštění souboru? Mohu požadavek ověřit jiným kanálem?

**Jedna metoda, různé převleky**

Obecný phishing míří na mnoho lidí. **Spear phishing** je připraven pro konkrétní osobu či skupinu a může použít jméno učitele, projekt nebo veřejné informace. **Smishing** přichází v SMS, **vishing** po telefonu a **quishing** ukrývá cíl v QR kódu. Baiting slibuje návnadu – třeba bezplatný program nebo zajímavý obsah na nalezeném USB disku.

Kanál se mění, princip zůstává: vyvolat důvěru nebo tlak a přimět příjemce k akci, kterou by po klidném ověření neprovedl. Bezpečné pravidlo proto nesmí znít jen „neklikej v e-mailu“. Musí fungovat i tehdy, když někdo volá a zná naše jméno.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup k phishingovému kvízu**</summary>

**Příprava**

1. Připravte si tabulku se sloupci `první rozhodnutí`, `důkaz`, `manipulační prvek`, `správné ověření` a `opravené rozhodnutí`.
2. Pokud úvodní obrazovka požádá o jméno či e-mail pro personalizaci ukázek, použijte smyšlené údaje, například `Student` a `student@example.com`. Nezadávejte školní účet ani heslo.
3. Předem si napište, podle jakého jediného znaku byste zprávu nejčastěji posuzovali. Na konci ověříte, zda takové pravidlo stačí.

**Postup**

1. U každé situace nejprve samostatně zvolte „phishing“, nebo „legitimní“. Rozhodnutí si poznamenejte ještě před zobrazením vysvětlení.
2. Prohlédněte adresu odesílatele znak po znaku. Zvlášť označte část za symbolem `@`. Zobrazené jméno nepovažujte za důkaz identity.
3. U odkazu zjistěte jeho cíl najetím ukazatele bez kliknutí, pokud to ukázka umožňuje. Na dotykovém zařízení pracujte pouze s informací zobrazenou kvízem; odkaz neotevírejte.
4. Najděte hostitele mezi `https://` a prvním `/`, `?` nebo `#`. Zakroužkujte skutečnou doménu a všimněte si překlepů, přidaných slov a klamavých poddomén.
5. Zaznamenejte, co zpráva vyžaduje: přihlášení, otevření dokumentu, změnu hesla, platbu nebo sdělení údaje. Potom pojmenujte tlak – autorita, čas, strach, zvědavost, odměna či rutina.
6. Přečtěte vysvětlení kvízu. Jestliže jste se spletli, nepište jen „nedával jsem pozor“. Uveďte konkrétní signál, který jste přehlédli, a postup, který chybu příště zachytí.

| Situace | První rozhodnutí | Technický důkaz | Psychologický tlak | Bezpečné ověření |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Ověření a odevzdání**

Sestavte tři kroky: **ZASTAV** automatickou reakci, **ZKONTROLUJ** odesílatele, doménu, požadavek a kontext, **OVĚŘ** přes známou záložku, oficiální aplikaci nebo telefonní číslo získané mimo zprávu. Skóre z kvízu není hlavním výstupem; důležitá je schopnost doložit rozhodnutí a opravit vlastní chybnou strategii.

</details>

## Experiment 2.3: URL pod mikroskopem

**Cíl:** Rozebrat webovou adresu na jednotlivé části, odhalit klamavé konstrukce a vysvětlit rozdíl mezi kódováním, šifrováním a důvěryhodností webu.

**Nástroj:** Bezplatná webová aplikace [CyberChef](https://gchq.github.io/CyberChef/), která zpracovává vložená data v prohlížeči, a čtyři připravené fiktivní adresy. Není potřeba účet ani instalace.

**Úkoly:**

1. U čtyř fiktivních URL určete schéma, hostitele, skutečnou doménu, cestu, dotaz a případný fragment či údaj před znakem `@`.
2. Dekódujte procentově zapsanou adresu a vysvětlete, proč kódování není šifrování.
3. U každého příkladu pojmenujte použitý klam a navrhněte bezpečný způsob ověření bez návštěvy adresy.

**Výstupy:** Vyplněná tabulka rozboru čtyř URL, dekódovaný řetězec, vysvětlení dvou klamavých technik a kontrolní pravidlo pro práci s odkazy.

<details>

<summary>**🧠 Rozbalit článek k tématu: Adresa je věta s přesnou gramatikou**</summary>

**Lomítka, tečky a zavináč nejsou ozdoby**

URL je adresa zdroje na síti. Vypadá jako dlouhá technická věta a stejně jako věta má části s odlišnou funkcí. Ve `https://portal.skolni.example/ucet?jazyk=cs#heslo` je `https` schéma, `portal.skolni.example` hostitel, `/ucet` cesta, `jazyk=cs` dotaz a `heslo` fragment.

Hostitel říká, ke kterému serveru se prohlížeč pokusí připojit. Cesta a dotaz už určují zdroj na tomto serveru. Slovo známé značky v cestě proto neříká nic o vlastníkovi webu. Adresa `https://utocnik.example/google/prihlaseni` stále patří hostiteli `utocnik.example`.

Zvlášť matoucí může být znak `@`. V některých URL odděluje uživatelské informace od hostitele. V adrese `https://skolni.example@overeni-uctu.example/login` se prohlížeč připojuje k `overeni-uctu.example`; text `skolni.example` před zavináčem není cílová doména. Moderní prohlížeče mohou takový zápis varovně zobrazit, analytik se však musí umět orientovat i v prostém textu.

**Nečitelné neznamená zašifrované**

Některé znaky mají v URL speciální význam, a proto se zapisují procentovým kódováním. Mezery může nahradit `%20`, lomítko `%2F` a dvojtečku `%3A`. Operace je vratná bez klíče. Jde o **kódování**, nikoli šifrování. Jeho cílem je bezpečně zapsat znaky do adresy, ne skrýt tajemství. Útočník však může dlouhý kódovaný řetězec použít k zakrytí cíle před rychlým pohledem.

Šifrované spojení HTTPS chrání přenos mezi prohlížečem a serverem a certifikát pomáhá ověřit doménu. Ikona zámku ale neříká, že obsah webu je poctivý. Podvodník může získat platný certifikát pro svou vlastní podvodnou doménu. Zámek tedy může znamenat „s tímto podvodným serverem komunikujete šifrovaně“.

**Přesměrování může být legitimní i zneužitelné**

Weby běžně používají parametry jako `continue`, `redirect` nebo `next`, aby po přihlášení poslaly uživatele na původní stránku. Zkracovače adres a marketingové odkazy také přesměrovávají. To samo o sobě není útok, ale skrývá další krok. Bezpečný uživatel se při citlivé akci raději dostane ke službě přes vlastní záložku nebo ručně napsanou známou adresu.

Proč adresy pouze analyzujeme a nezkoušíme? Protože kliknutí je již interakce s cizím systémem. Může potvrdit aktivitu adresy, spustit stažení nebo využít chybu prohlížeče. V této laboratoři používáme rezervovanou koncovku `.example`, určenou pro dokumentaci, a zkoumáme text bez návštěvy cíle.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v CyberChef**</summary>

**Příprava**

Zkopírujte si do protokolu následující fiktivní adresy. Neotvírejte je; všechny slouží jako textový materiál.

```text
A  https://portal.skolni.example/prihlaseni
B  https://portal.skolni.example.utocnik.example/prihlaseni
C  https://skolni.example@overeni-uctu.example/login
D  https%3A%2F%2Fobnova-uctu.example%2Flogin%3Fcontinue%3Dhttps%253A%252F%252Fportal.skolni.example
```

**Postup**

1. U adres A až C nejprve barevně označte schéma, hostitele a cestu. U B porovnejte pořadí slov s A. U C vyhledejte znak `@` a určete hostitele až za ním.
2. Otevřete CyberChef. Do pole Input vložte pouze adresu D bez písmene a popisku.
3. Do vyhledávání operací napište `URL Decode` a přetáhněte tuto operaci do Recipe. Ve výstupu se objeví první dekódovaná vrstva.
4. Všimněte si, že hodnota parametru `continue` stále obsahuje znaky `%3A` a `%2F`. Přidejte `URL Decode` podruhé. Vysvětlete, co bylo zakódováno dvakrát a co je hostitelem první adresy.
5. Pokud je v dostupné verzi operace `Parse URI`, vyzkoušejte ji na jednotlivých dekódovaných adresách. Když není, rozdělte adresu ručně podle značek `://`, `/`, `?`, `#` a `@`.
6. U každého příkladu napište bezpečný způsob ověření. Například otevřít školní portál z vlastní záložky, nikoli opravovat podezřelou adresu a zkoušet ji.

| URL | Hostitel | Skutečná doména | Klam nebo zvláštnost | Bezpečné ověření |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |

**Ověření a odevzdání**

Odevzdejte tabulku a odpovězte: „Proč platné HTTPS nestačí k důvěře?“ a „Proč je `%2F` kódování, nikoli šifrování?“ Zkontrolujte, že jste žádnou z adres nenavštívili. Omezením úlohy je, že rozbor textu neověřuje skutečný obsah ani aktuální chování webu.

</details>

## Experiment 2.4: Detektiv e-mailových hlaviček

**Cíl:** Porovnat viditelný obsah e-mailu s technickými hlavičkami, vyhodnotit cestu zprávy a autentizační výsledky a formulovat rozhodnutí založené na více důkazech.

**Nástroj:** Běžný textový editor, dva připravené fiktivní soubory `.eml` a volitelně [Google Admin Toolbox Messageheader](https://toolbox.googleapps.com/apps/messageheader/). Není nutné používat vlastní e-mail ani účet.

**Úkoly:**

1. Porovnejte pole `From`, `Reply-To`, `Return-Path`, `Received` a `Authentication-Results` ve dvou připravených zprávách.
2. Určete nejstarší dohledatelný bod cesty, interpretujte SPF, DKIM a DMARC a spojte technické údaje s obsahem zprávy.
3. Sepište verdikt jako tvrzení podložené nejméně čtyřmi konkrétními důkazy a jedním omezením.

**Výstupy:** Srovnávací tabulka obou zpráv, stručná časová osa přenosu, zdůvodněný verdikt a návrh bezpečného nezávislého ověření.

<details>

<summary>**🧠 Rozbalit článek k tématu: Co se skrývá za řádkem Od**</summary>

**E-mail má pohlednici i přepravní protokol**

Poštovní aplikace ukazuje příjemci hlavně jméno odesílatele, předmět a text. Pod povrchem je však sada hlaviček popisujících vznik a cestu zprávy. Je to podobné jako balík: na dárkové kartičce může být napsáno cokoli, zatímco přepravní štítky ukazují, kudy zásilka skutečně prošla.

Pole `From` je autor uvedený ve zprávě a poštovní program z něj často zvýrazní jen zobrazované jméno. `Reply-To` určuje, kam se odešle odpověď, a může se od `From` lišit z legitimních důvodů – například u hromadné podpory – i z důvodů podvodných. `Return-Path` souvisí s obálkou při přenosu zprávy a používá se mimo jiné pro chybová hlášení.

Každý poštovní server může při převzetí přidat řádek `Received`. Proto se cesta obvykle čte **odspodu nahoru**: nejnižší důvěryhodný záznam bývá nejstarší a další servery přidávají nové řádky nad něj. Ani tato stopa není absolutní. Útočník může do původní zprávy vložit falešné řádky, ale nemůže zpětně změnit záznam, který později přidal server příjemce. Analytik proto zvažuje hranici důvěry a konzistenci údajů.

**SPF, DKIM a DMARC řeší různé otázky**

SPF dovoluje vlastníkovi domény zveřejnit, které servery smějí jejím jménem odesílat poštu na úrovni přenosové obálky. DKIM přidává kryptografický podpis vybraných částí zprávy; přijímající server jej ověří veřejným klíčem uloženým v DNS. DMARC propojuje autentizaci s doménou viditelnou v poli `From` a určuje doporučenou politiku pro nevyhovující zprávy.

Výsledek `pass` je užitečný, ale neznamená „obsah je pravdivý“. Útočník může poslat dokonale autentizovaný e-mail ze své vlastní domény nebo z kompromitovaného legitimního účtu. Naopak přeposílání a některé poštovní brány mohou autentizaci komplikovat. Tři zkratky jsou důkazní stopy, nikoli detektor lidského úmyslu.

**Verdikt vzniká skládáním stop**

Silná analýza spojuje technické údaje s kontextem. Neshoduje se zobrazované jméno s adresou? Směřuje odpověď jinam? Selhává autentizace? Žádá zpráva okamžité přihlášení přes neznámý odkaz? Přichází v době a situaci, kterou příjemce očekával? Jedna nesrovnalost může mít nevinné vysvětlení, ale několik nezávislých varovných signálů mění rozhodnutí.

Při skutečném podezření se zpráva nepřeposílá libovolně spolužákům a nezkouší se její odkaz. Uchová se jako důkaz a předá se určeným způsobem správci. Tato laboratoř používá plně fiktivní zprávy, takže si lze metodu vyzkoušet bez práce se soukromou komunikací.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup analýzy hlaviček**</summary>

**Příprava**

1. Stáhněte [podezřelou zprávu](./materialy/2-4-podezrely-email.eml) a [legitimní modelovou zprávu](./materialy/2-4-legitimni-email.eml). Oba soubory obsahují pouze fiktivní text a rezervované adresy.
2. Otevřete je v prostém textovém editoru, například Poznámkovém bloku nebo Visual Studio Code. Není nutné je importovat do e-mailového programu.
3. Připravte si dvě barvy: jednou označte přímá pozorování, druhou vlastní interpretace.

**Postup**

1. V obou souborech najděte `Date`, `From`, `To`, `Subject`, `Reply-To`, `Return-Path`, `Message-ID`, všechny řádky `Received` a `Authentication-Results`.
2. Porovnejte domény ve `From`, `Reply-To`, `Return-Path` a `Message-ID`. Shoda sama není důkazem legitimity, neshoda však vyžaduje vysvětlení.
3. Řádky `Received` čtěte od nejnižšího směrem nahoru. Z každého vypište čas, odesílající a přijímající server. Zkontrolujte, zda časy tvoří možnou posloupnost.
4. U SPF, DKIM a DMARC napište `pass`, `fail` nebo `none` a vlastními slovy vysvětlete, jakou otázku daný mechanismus řeší. Nevytvářejte souhrnný verdikt jen z jedné zkratky.
5. Prohlédněte tělo zprávy. Označte naléhavost, požadovanou akci a cílovou doménu odkazu. Odkaz neotvírejte.
6. Volitelně vložte hlavičky jedné **fiktivní** zprávy do Messageheader. Porovnejte grafickou časovou osu s ručním rozborem. Skutečné soukromé hlavičky do externí služby nevkládejte.

| Důkaz | Podezřelá zpráva | Legitimní model | Co z toho lze vyvodit |
|---|---|---|---|
| From / Reply-To | | | |
| Return-Path | | | |
| SPF | | | |
| DKIM | | | |
| DMARC | | | |
| obsah a odkaz | | | |

**Ověření a odevzdání**

Verdikt formulujte například: „Zprávu považuji za vysoce podezřelou, protože…“ a uveďte čtyři konkrétní stopy. Potom přidejte omezení: i autentizovaná zpráva může pocházet z kompromitovaného účtu a fiktivní hlavičky zjednodušují skutečný provoz. Bezpečné ověření proveďte přes známý kontakt školy nebo ruční otevření oficiálního portálu, nikdy přes odpověď či odkaz ze zprávy.

</details>

## Experiment 2.5: Laboratoř psychologického nátlaku

**Cíl:** Zažít rozdíl mezi rychlým rozhodnutím a strukturovanou analýzou, rozpoznat techniky sociálního inženýrství napříč kanály a nacvičit bezpečnou reakci.

**Nástroj:** Tisknutelné [karty manipulace](./materialy/2-5-karty-manipulace.md), stopky nebo časovač, papír a psací potřeby. Cvičení nevyžaduje účet, internet ani instalaci programu.

**Úkoly:**

1. Ve dvou průchodech – nejprve pod mírným časovým tlakem, potom bez něj – vyhodnoťte šest fiktivních situací.
2. U každé určete kanál, psychologickou páku, požadovanou akci a nejbezpečnější nezávislé ověření.
3. Jednu podvodnou žádost přepište do podoby legitimní organizační zprávy a sestavte krátkou bezpečnou reakci příjemce.

**Výstupy:** Vyplněná analytická karta šesti situací, porovnání rozhodování v obou průchodech, legitimně přeformulovaná zpráva a osobní věta pro zastavení nátlaku.

<details>

<summary>**🧠 Rozbalit článek k tématu: Útok na člověka je útok na systém**</summary>

**Nejslabší článek, nebo nejpružnější senzor?**

O lidech se někdy říká, že jsou nejslabším článkem bezpečnosti. Je to svůdná, ale neúplná metafora. Člověk sice může udělat chybu, zároveň však dokáže rozpoznat neobvyklý kontext, položit otázku a útok zastavit tam, kde automatické pravidlo selže. Smyslem výuky není hledat viníka, ale dát tomuto „lidskému senzoru“ vhodný postup a prostředí, ve kterém se nemusí bát ověřovat.

Sociální inženýrství pracuje s **pretextem** – uvěřitelným příběhem vysvětlujícím, kdo útočník je a proč něco potřebuje. Falešný technik chce vzdálený přístup, „ředitel“ dárkové poukazy a „banka“ kód z SMS. Příběh se snaží přeskočit běžná pravidla: je to prý tajné, výjimečné a nesmírně naléhavé.

Nátlak zužuje pozornost. Člověk přestane porovnávat alternativy a hledá nejrychlejší cestu, jak hrozbu odstranit nebo získat odměnu. Proto podvodné zprávy kombinují více pák: autoritu s časem, strach s finanční ztrátou, zvědavost s pocitem výlučnosti. Položme si řečnickou otázku: Kdyby byla žádost legitimní, proč by nesnesla třicet sekund nezávislého ověření?

**Kanál mění kulisy, nikoli princip**

SMS o zásilce je smishing, hlasový telefonát vishing a QR kód může být quishing. USB disk s lákavým štítkem využívá baiting. Cílená zpráva se jménem učitele může být spear phishing. Ve všech případech útočník žádá přenos hodnoty: peněz, hesla, jednorázového kódu, spuštění souboru, instalace aplikace nebo udělení přístupu.

Jednorázový kód z SMS není „jen číslo“. Může být druhým faktorem potvrzujícím přihlášení nebo platbu. Kdo jej nadiktuje volajícímu, může právě schvalovat jeho operaci. Nalezený USB disk není bezpečný proto, že vypadá opuštěně; může obsahovat škodlivý soubor nebo se vydávat za jiné zařízení. QR kód je jen způsob zápisu dat – podobně jako skrytý odkaz neukazuje cílovou adresu pouhým okem.

**Správná reakce chrání i vztahy**

Ověření neznamená obvinit odesílatele ze lži. Stačí říci: „Tuto žádost potvrzuji běžným postupem a zavolám na známé číslo.“ Organizace by měla takové chování podporovat. Když skutečný ředitel očekává, že zaměstnanec obejde pravidla jen proto, že je žádost naléhavá, nevědomky trénuje chování, které útočník zneužije.

Legitimní zpráva pomáhá ověřování: nevytváří umělý nátlak, nežádá heslo ani kód, vysvětluje účel a vede uživatele ke známému systému. Bezpečnost zde není překážka komunikace; je známkou kvalitního návrhu.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup skupinového cvičení**</summary>

**Příprava**

1. Vytvořte skupiny po třech až čtyřech. Rozdělte role `příjemce`, `analytik`, `ověřovatel` a případně `zapisovatel`. Role po třech kartách vystřídejte.
2. Otevřete nebo vytiskněte karty manipulace. Neotevírejte uvedené adresy a nepřipojujte nalezená skutečná USB zařízení; jde pouze o textové situace.
3. Cílem není vytvořit dokonalejší podvod. Tým analyzuje obranu a bezpečnou komunikaci.

**První průchod – rychlé rozhodnutí**

1. Učitel nebo zapisovatel ukáže kartu na 20 sekund. Příjemce zvolí `provedu`, `odmítnu` nebo `pozastavím a ověřím` a jednou větou vysvětlí proč.
2. Zapište první emoci a signál, který měl na rozhodnutí největší vliv. Časový limit má ukázat tlak, nikoli studenty zesměšnit.
3. Kartu odložte bez skupinové debaty a pokračujte další.

**Druhý průchod – analytický režim**

1. Ke každé kartě určete kanál: e-mail, SMS, fyzický předmět, telefon nebo QR kód.
2. Pojmenujte psychologickou páku: autorita, naléhavost, strach, odměna, zvědavost, důvěrnost nebo rutina. Jedna karta jich může používat několik.
3. Přesně napište, jakou hodnotu má příjemce předat nebo jakou akci provést. Nezůstávejte u obecného „něco chce“.
4. Navrhněte nezávislé ověření. Kontakt ani odkaz nesmí pocházet z podezřelé zprávy: použijte známé číslo, oficiální aplikaci, vlastní záložku nebo osobní dotaz.
5. Porovnejte první a druhé rozhodnutí. Změnilo se? Která otázka odhalila nejvíce?

**Přepis jedné zprávy**

Vyberte kartu A, B, D nebo F a napište legitimní organizační variantu. Musí jasně uvést účel a provozovatele, nesmí vyžadovat heslo ani jednorázový kód, nemá vytvářet zbytečný časový tlak a má uživatele vést do známého systému bez vloženého přihlašovacího odkazu.

**Ověření a odevzdání**

Odevzdejte analytickou kartu, srovnání obou průchodů a přepsanou zprávu. Připojte vlastní „brzdnou větu“, například: „Než předám údaj nebo něco spustím, ověřím žádost mimo kanál, kterým přišla.“ V závěru vysvětlete, proč znalost jména nebo školního projektu nedokazuje totožnost volajícího.

</details>

## Experiment 2.6: Rekonstrukce malwarového incidentu

**Cíl:** Sestavit z dílčích stop kauzální řetězec incidentu, rozlišit typy malwaru a umístit preventivní, detekční a obnovovací opatření do správných míst.

**Nástroj:** Připravené [karty incidentu](./materialy/2-6-karty-incidentu.md), papír a samolepicí lístky nebo bezplatný [diagrams.net](https://app.diagrams.net/) použitelný bez přihlášení. Žádný skutečný malware se nespouští.

**Úkoly:**

1. Seřaďte karty do nejpravděpodobnějšího řetězce, označte jednu falešnou stopu a oddělte důkaz od domněnky.
2. Určete, proč modelový program odpovídá trojskému koni a infostealeru, ale ne automaticky viru či červu.
3. Umístěte nejméně čtyři obranná opatření k bodům, kde by mohla řetězec přerušit, a sestavte stručný plán reakce.

**Výstupy:** Diagram incidentu s popsanými vazbami, tabulka důkazů a nejistot, čtyři zdůvodněná opatření a pětivěté hlášení incidentu.

<details>

<summary>**🧠 Rozbalit článek k tématu: Malware není jedna příšera, ale role v příběhu**</summary>

**Název kategorie popisuje vlastnost, ne celý životopis**

Slovo malware je zastřešující označení škodlivého softwaru. Jediný program může současně spadat do několika kategorií. Pokud se vydává za užitečný prohlížeč fotografií, je způsobem doručení **trojský kůň**. Jestliže tajně krade hesla, cookies nebo údaje z prohlížeče, plní roli **infostealeru**. Kdyby navíc umožnil vzdálené ovládání, mohl by být také RAT.

Virus se tradičně připojuje k jinému souboru či programu a šíří se jeho spuštěním. Červ se umí šířit mezi systémy automatizovaně, často přes síť a zranitelnost. To, že nakažený účet rozešle podvodné zprávy kontaktům, ještě nedělá ze škodlivého programu červa: šíří se zde sociální návnada prostřednictvím zneužitého účtu, nikoli nutně samočinná kopie programu po síti.

Ransomware zašifruje nebo jinak znepřístupní data a požaduje výkupné; moderní skupiny mohou před zašifrováním data také ukrást a hrozit zveřejněním. Wiper má data zničit. Spyware dlouhodobě sleduje uživatele a rootkit se snaží ukrýt přítomnost nebo udržet privilegovaný přístup. Kategorie pomáhají popsat chování a zvolit obranu, ale reálné rodiny malwaru hranice často překračují.

**Incident je řetěz, ne jediný okamžik**

Úspěšný útok mívá několik kroků: získání důvěry, doručení souboru či odkazu, spuštění, získání přístupu, krádež nebo změnu dat, pohyb k dalším účtům a dopad. Mezi kroky vznikají stopy. E-mailová brána může zaznamenat zprávu, ochrana zařízení neobvyklý proces, přihlašovací systém novou relaci a uživatel neočekávané odhlášení.

Analytik skládá časovou osu podobně jako vyšetřovatel dopravní nehody. Samotná stopa pneumatik neříká, kdo řídil, ale ve spojení s kamerovým záznamem a časem události zpřesní příběh. Proto rozlišuje **důkaz**, který karta přímo uvádí, a **inference**, která vysvětluje vazbu. Alternativní vysvětlení se nezamlčuje.

**Vrstvená obrana dává více šancí uspět**

Kdyby ochrana závisela jen na tom, že uživatel nikdy neklikne, jediná chyba by rozhodla vše. Vrstvená obrana nabízí další zastávky: filtrování zpráv, omezení spouštění neznámých aplikací, aktualizace, ochrana koncových bodů, vícefaktorové ověření odolné vůči phishingu, krátké relace, sledování neobvyklých přihlášení, zálohy a nacvičená reakce.

Po zjištění incidentu je důležité nejednat chaoticky. Zařízení se podle pravidel organizace izoluje, zachovají se důkazy, zneplatní odcizené relace a tokeny, obnoví se důvěryhodný stav a zkontroluje rozsah. Pouhá změna hesla nemusí odhlásit již odcizenou relaci. A pouhé smazání viditelného souboru nemusí odstranit všechny změny.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup rekonstrukce**</summary>

**Příprava**

1. Pracujte ve skupinách po třech až čtyřech. Rozstříhejte karty incidentu nebo je zkopírujte jako samostatné objekty do diagrams.net. Při použití webové aplikace zvolte uložení do zařízení; účet není nutný.
2. Nejdříve si přečtěte pouze text karet A až J. Nehledejte na internetu konkrétní malware – případ je zcela fiktivní a všechny potřebné informace jsou v materiálu.
3. Připravte tři druhy značek: `doloženo kartou`, `pravděpodobná inference` a `nejisté / alternativní vysvětlení`.

**Rekonstrukce**

1. Každý člen týmu samostatně navrhne první tři události. Teprve potom návrhy porovnejte, aby první hlas nepřevzal celou diskusi.
2. Seřaďte karty podle času a příčiny. Mezi sousední karty nakreslete šipku jen tehdy, když umíte doplnit sloveso, například `přimělo ke spuštění`, `umožnilo odcizení` nebo `vedlo k rozeslání`.
3. Vyberte kartu, která může být falešnou stopou. Vysvětlete, proč s incidentem časově souvisí, ale nemusí být jeho příčinou.
4. U škodlivého programu označte role `trojský kůň` a `infostealer`. Napište, jaký důkaz by byl navíc potřeba pro označení `virus`, `červ`, `RAT` nebo `ransomware`.
5. Rozdělte řetězec na fáze: sociální manipulace, doručení, spuštění, kompromitace, zneužití účtu, detekce, omezení škod a obnova.

**Vložení obranných bodů**

Ke čtyřem různým šipkám přidejte opatření a napište mechanismus účinku. Příklady: školení a nezávislé ověření zastaví spuštění; omezení aplikací blokuje neznámý program; ochrana zařízení může detekovat krádež dat; zneplatnění relací odebere přístup; kontrola rozeslaných zpráv chrání další příjemce. Alespoň jedno opatření musí být preventivní, jedno detekční a jedno obnovovací.

| Karta nebo vazba | Přímý důkaz | Inference | Co by ji ověřilo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Hlášení incidentu**

Napište přesně pět vět: co bylo pozorováno, jaký je pravděpodobný počáteční vektor, která aktiva mohla být zasažena, co má být provedeno okamžitě a co zatím zůstává nejisté. Nepište jméno domnělého pachatele; karty takovou informaci neposkytují.

**Ověření a odevzdání**

Odevzdejte fotografii papírového schématu nebo exportovaný diagram, tabulku a pětivěté hlášení. Zkontrolujte, že diagram nezaměňuje časovou následnost za příčinu a že změna hesla není jediným krokem reakce. Uveďte také potřebu zneplatnit relace, zachovat důkazy a ověřit důvěryhodný stav zařízení.

</details>

## Závěrečná reflexe

**Přijde neočekávaná příloha s naléhavou žádostí o spuštění. Která reakce je nejkvalitnější?**

<!-- data-randomize="true" -->
[( )] Spustit ji, pokud VirusTotal právě ukazuje nula detekcí.
[( )] Přeposlat ji spolužákům a zeptat se, zda se jim otevře.
[(X)] Zastavit se, ověřit žádost nezávislým kanálem, zachovat zprávu a postupovat podle pravidel školy.
[( )] Přejmenovat příponu souboru a vyzkoušet jej znovu.

Vyberte jeden experiment a doplňte konkrétní příklad do řetězce:

`manipulace nebo zranitelnost → akce uživatele či systému → kompromitace → stopa → reakce → dlouhodobé opatření`
