<!--
author: Marek Lučný
title: Rozpoznání napadení a vícevrstvá obrana – praktická laboratoř
language: cs
mode: Textbook
comment: Šest praktických experimentů s logy, Autoruns, Wiresharkem, zálohami, Nmapem a firewallem.
-->

# Praktická laboratoř: Rozpoznání napadení a vícevrstvá obrana

Počítač se na okamžik zpomalí. Ventilátor se roztočí. V logu přibude červená ikona. Je to útok, porucha, nebo jen aktualizace? Bezpečnostní analytik není věštec a dobrý nástroj není kouzelná koule. V této laboratoři budete **sbírat skutečné stopy na vlastním zařízení**, porovnávat je s očekáváním a zjišťovat, jak se navzájem doplňují logy, kontrola autostartu, síťový záznam, záloha, síťový inventář a firewall.

> **🛡️ Hranice laboratoře**
>
> Pracujte pouze na vlastním nebo učitelem určeném testovacím zařízení. Wireshark smí zachytávat jen váš vlastní provoz. Nmap nejprve míří výhradně na `127.0.0.1`; jinou adresu zadejte jen s výslovným souhlasem učitele a pouze z připraveného inventáře. Pravidlo firewallu vytvářejte jen na vyhrazeném zařízení, pod dohledem a s povinným odstraněním. Nic podezřelého nemažte, nevypínejte ochranu a nezkoušejte exploitovat nalezenou službu.

## Laboratorní deník

```text
Předpověď:
Přesný čas a provedená akce:
Pozorování nebo důkaz:
Možné vysvětlení:
Alternativní vysvětlení:
Omezení měření:
Bezpečné rozhodnutí:
```

| Experiment | Mise | Nástroj | Orientační čas |
|---|---|---|---:|
| 3.1 Lovec událostí | sestavit příběh z logů | Prohlížeč událostí | 40 min |
| 3.2 Černí pasažéři startu | prověřit autostart | Autoruns | 40 min |
| 3.3 Síť pod lupou | zachytit DNS, TCP a TLS | Wireshark | 45 min |
| 3.4 Záchranný člun pro data | provést skutečnou obnovu | soubory, hash, stopky | 45 min |
| 3.5 Radar služeb | zmapovat pouze schválený cíl | Nmap / Zenmap | 40 min |
| 3.6 Síťový vyhazovač | vytvořit a vrátit pravidlo | Windows Defender Firewall | 45 min |

## Experiment 3.1: Lovec událostí v Prohlížeči událostí

**Cíl:** Najít a interpretovat několik skutečných systémových událostí, sestavit jejich časovou osu a rozlišit záznam, příznak a důkaz incidentu.

**Nástroj:** Vestavěný **Prohlížeč událostí Windows** (`eventvwr.msc`) a pro počítač bez přístupu k bezpečnostnímu logu připravený soubor [modelových událostí](./materialy/3-1-modelove-logy.csv).

**Úkoly:**

1. Vyhledejte tři události z posledních 24 hodin v protokolech Systém nebo Aplikace a jednu přihlašovací událost, pokud je protokol Zabezpečení dostupný.
2. U každé zapište čas, úroveň, zdroj, ID, zařízení/účet a stručné vysvětlení vlastním jazykem.
3. Sestavte časovou osu, označte fakta a hypotézy a navrhněte dva další zdroje, které by hypotézu potvrdily nebo vyvrátily.

**Výstupy:** Tabulka nejméně čtyř událostí, anotovaná časová osa, snímek jednoho anonymizovaného detailu a závěr vysvětlující, proč červená ikona sama nedokazuje napadení.

<details>

<summary>**🧠 Rozbalit článek k tématu: Počítačový deník neumí číst myšlenky**</summary>

**Každá událost je věta bez celého odstavce**

Operační systém, ovladače, služby a aplikace průběžně zapisují události. Záznam může říkat: „služba se v 9:14 zastavila“, „přihlášení selhalo“ nebo „aplikace přestala odpovídat“. Neříká automaticky proč. Je to podobné jako čidlo u dveří: spolehlivě oznámí otevření, ale samo nerozezná zaměstnance od zloděje.

Prohlížeč událostí sdružuje protokoly například do oblastí **Aplikace**, **Systém** a **Zabezpečení**. Událost má čas, úroveň, zdroj a číselné ID. ID má význam až společně se zdrojem; stejné číslo od dvou různých poskytovatelů nemusí znamenat totéž. Text v záložce Obecné je vhodné číst spolu s podrobnostmi, ne izolovaně vyhledat první dramatické vysvětlení na internetu.

**Chyba není automaticky útok**

Červené označení Error znamená, že určitá operace selhala. Může jít o odpojenou tiskárnu, program ukončený uživatelem, krátký síťový výpadek nebo skutečný problém. Podobně úspěšné přihlášení není podezřelé bez kontextu. V bezpečnostním logu Windows se často setkáte s ID 4624 pro úspěšné a 4625 pro neúspěšné přihlášení, ale rozhodují také typ přihlášení, účet, zdroj a četnost.

Jeden překlep následovaný úspěšným místním přihlášením je jiný příběh než stovky neúspěchů z nečekaného zdroje. Bezpečnostní analýza proto používá **korelaci**: propojuje čas, uživatele, proces, síťovou komunikaci a další stopy.

**Časová osa je páteř vyšetřování**

Představte si, že v 8:17 vznikl nový proces, o čtyři sekundy později navázal spojení a v 8:19 jej ochrana zablokovala. Posloupnost podporuje hypotézu o souvislosti, ale neprokazuje, co bylo přeneseno. Potřebovali bychom detail procesu, hash souboru, síťový log, historii stažení a výpověď uživatele.

Analytik proto používá slovník jistoty: **doloženo**, **pravděpodobné**, **možné**, **neznámé**. Silný závěr není nejsebevědomější věta, ale věta, která přesně uvádí hranici důkazu.

**Logy mají slepá místa**

Záznam může být vypnutý, přepsaný, zpožděný nebo uložený s jiným časovým pásmem. Útočník s vysokým oprávněním se jej může pokusit změnit. Událost na jednom zařízení neukáže automaticky dění v cloudu. Organizace proto logy centralizují, chrání jejich integritu a porovnávají více zdrojů.

Pro středoškolskou laboratoř je nejdůležitější návyk: nejdříve zapsat přesné pozorování, potom teprve nabídnout vysvětlení. Věta „v 10:03 byl zaznamenán pád editoru“ je fakt. Věta „editor shodil malware“ je hypotéza, dokud ji další stopy nepodpoří.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v Prohlížeči událostí**</summary>

**Příprava**

1. Poznamenejte si přesný aktuální čas a uložte rozpracovanou práci. Do systému neprovádějte žádný umělý neúspěšný útok ani opakované hádání hesla.
2. Stiskněte `Win+R`, napište `eventvwr.msc` a potvrďte. Na školním zařízení může otevření některých protokolů vyžadovat oprávnění; takové omezení neobcházejte.
3. V levém stromu rozbalte `Protokoly systému Windows`. Začněte protokolem `Systém` nebo `Aplikace`.

**Sběr událostí**

1. V pravém panelu zvolte `Filtrovat aktuální protokol`. Nastavte posledních 24 hodin a úrovně Informace, Upozornění a Chyba. Nevybírejte jen chyby – potřebujete kontext.
2. Vyberte jednu informační, jednu varovnou a jednu chybovou událost. Zapište přesný čas, zdroj, ID a první větu popisu.
3. U každé položte tři otázky: Co systém přímo tvrdí? Jaké běžné vysvětlení existuje? Co by z ní udělalo bezpečnostně významnou stopu?
4. Pokud je protokol `Zabezpečení` dostupný, použijte `Filtrovat aktuální protokol` a do ID událostí zadejte `4624,4625`. Vyberte jediný záznam bez zveřejnění jména účtu, IP či názvu zařízení. Není-li dostupný, použijte modelové CSV.
5. Přepněte na záložku `Podrobnosti` a prohlédněte strukturovaná pole. Nic v protokolu nemažte a nepoužívejte volbu Vymazat protokol.

| Čas | Protokol a zdroj | ID / úroveň | Přímé pozorování | Hypotéza | Jistota |
|---|---|---:|---|---|---|
| | | | | | |

**Časová osa a interpretace**

1. Seřaďte události podle času. Pokud spolu zřejmě nesouvisejí, nevytvářejte umělý příběh; právě to je platný výsledek.
2. U modelového CSV samostatně propojte události mezi 8:17 a 8:20 a ke každé šipce napište, zda jde o časovou následnost, nebo doloženou příčinu.
3. Navrhněte dva další zdroje: detail ochrany, seznam procesů, historii instalace, DNS log nebo potvrzení uživatele.

**Ověření a odevzdání**

Ořízněte snímek tak, aby neobsahoval skutečné účty ani adresy. Závěr rozdělte na „Doloženo“, „Pravděpodobná interpretace“ a „Co chybí“. Připojte větu: „Úroveň Error popisuje selhání operace, nikoli automaticky kybernetický útok.“

</details>

## Experiment 3.2: Černí pasažéři startu s Autoruns

**Cíl:** Zmapovat programy spouštěné při startu a přihlášení, ověřit jejich původ a naučit se rozpoznávat položky vyžadující další kontrolu bez nebezpečného „čištění“ systému.

**Nástroj:** Bezplatný nástroj [Microsoft Sysinternals Autoruns](https://learn.microsoft.com/sysinternals/downloads/autoruns), případně učitelem připravený export nebo snímek na zařízení, kde nelze nástroj spustit.

**Úkoly:**

1. Najděte tři očekávané položky autostartu a jednu položku, jejíž účel není na první pohled jasný.
2. U každé ověřte umístění souboru, vydavatele, digitální podpis, čas a souvislost s instalovanou aplikací.
3. Zařaďte položku jako `očekávaná`, `zbytečná, ale legitimní`, `vyžaduje ověření` nebo `eskalovat správci`; nic bez schválení nevypínejte.

**Výstupy:** Anonymizovaný inventář čtyř položek, detailní karta jedné nejasné položky, důkaz o ověření podpisu a rozhodovací strom pro další postup.

<details>

<summary>**🧠 Rozbalit článek k tématu: Kdo nastupuje do vlaku při startu systému**</summary>

**Persistence je schopnost vrátit se**

Program spuštěný jen jednou po restartu zmizí. Legitimní aplikace i malware proto používají místa, která systém zpracuje při startu, přihlášení nebo určité události. Může jít o složku Po spuštění, klíče `Run`, služby, ovladače, naplánované úlohy, rozšíření Průzkumníka a řadu dalších mechanismů.

Této schopnosti říkáme **persistence**. Synchronizační klient potřebuje běžet po přihlášení, ovladač zvuku při startu a bezpečnostní agent nepřetržitě. Stejný mechanismus může využít spyware. Místo autostartu tedy není samo o sobě dobré ani zlé – je to nástupní stanice, na které kontrolujeme jízdenky.

**Autoruns ukazuje víc než Správce úloh**

Autoruns z rodiny Microsoft Sysinternals prochází mnoho míst automatického spouštění a zobrazuje název, popis, vydavatele, cestu a další údaje. Karty `Logon`, `Scheduled Tasks`, `Services` nebo `Drivers` odpovídají různým mechanismům. Pro první experiment je nejvhodnější `Logon`; ostatní mohou být rozsáhlé a citlivé.

Volba `Hide Signed Microsoft Entries` pomáhá zmenšit šum, ale nesmí se chápat jako detektor malwaru. Podepsaný soubor může obsahovat chybu nebo pocházet od kompromitovaného vydavatele. Nepodepsaný soubor může být starý legitimní nástroj. Platný podpis především říká, že se podepsaný obsah od podpisu nezměnil a odpovídá uvedenému certifikátu.

**Název lze zfalšovat, kontext se falšuje hůř**

Soubor `WindowsUpdate.exe` nemusí pocházet od Microsoftu. Proto se zkoumá úplná cesta, podpis, popis, čas instalace a návaznost na známý program. Kopie v dočasné složce uživatele je jiný signál než soubor v adresáři legitimní aplikace – stále však není automatickým důkazem.

Autoruns umí porovnat hash s VirusTotal. Tato funkce vyžaduje opatrnost: neznámé soubory se nesmějí automaticky odesílat mimo zařízení. V laboratoři necháváme volbu pro odeslání neznámých souborů vypnutou. I případný počet detekcí je pouze další stopa, nikoli rozsudek.

**Nejhorší diagnostický nástroj je náhodné vypínání**

Odškrtnutí položky může znemožnit synchronizaci, přihlášení, ovladač nebo ochranu systému. Profesionální postup začíná exportem a dokumentací, pokračuje ověřením a změnu provede oprávněný správce s plánem návratu. V této úloze se učíme číst, ne „lovit malware“ podle barvy řádku.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v Autoruns**</summary>

**Bezpečné spuštění**

1. Autoruns stáhněte pouze z Microsoft Learn. Rozbalte archiv do učitelem určené složky. Na školním počítači nic nestahujte ani nespouštějte bez souhlasu.
2. Spusťte `Autoruns64.exe` běžným způsobem. Jestliže učitel povolí zvýšená oprávnění, udělá to on; experiment je možné provést i jen nad viditelnými položkami.
3. Přečtěte licenční podmínky a počkejte na dokončení úvodního skenu. Během načítání nedělejte závěry z neúplného seznamu.
4. V nabídce Options zapněte `Verify Code Signatures`. Pro přehled lze zapnout `Hide Signed Microsoft Entries`. Volbu `Submit Unknown Images` ponechte vypnutou.

**Vyšetření položek**

1. Otevřete kartu `Logon`. Vyberte tři položky, které poznáváte podle používaných aplikací, a jednu nejasnou.
2. Zapište Entry, Description, Publisher a Image Path. V osobní cestě nahraďte uživatelské jméno symbolem `[UŽIVATEL]`.
3. Pravým tlačítkem použijte `Properties` nebo `Jump to Image`, pokud jsou dostupné. Ve vlastnostech souboru prohlédněte kartu Digitální podpisy a detail certifikátu. Soubor nespouštějte.
4. Použijte `Search Online` jen jako doplňkový zdroj. Ověřujte současně název vydavatele a cestu; první diskusní příspěvek není důkaz.
5. Pokud je zapnuta pouze kontrola známého hashe přes VirusTotal, zapište výsledek bez kliknutí na odeslání souboru. Nula detekcí neznamená bezpečí a jedna detekce může být falešný poplach.

| Položka | Mechanismus | Cesta | Podpis/vydavatel | Očekávaný účel | Rozhodnutí |
|---|---|---|---|---|---|
| | | | | | |

**Rozhodovací strom**

```text
Znám instalaci a účel?
 ├─ ano → odpovídá cesta a podpis? → zdokumentovat jako očekávané
 └─ ne  → ověřit cestu, podpis, čas, hash a chování
              ├─ vysvětleno → legitimní nebo zbytečné
              └─ nevysvětleno → neměnit, eskalovat správci
```

**Ověření a odevzdání**

Odevzdejte inventář a kartu nejasné položky. Potvrďte, že jste nic neodškrtli ani nesmazali. V závěru popište alespoň tři nezávislé signály a omezení: Autoruns ukazuje mechanismus automatického spuštění, ale sám nepozoruje kompletní budoucí chování programu.

</details>

## Experiment 3.3: Síť pod lupou ve Wiresharku

**Cíl:** Zachytit vlastní krátkou síťovou komunikaci, najít DNS dotaz, navázání TCP a TLS provoz a přesně popsat, co je v paketech viditelné a co chrání šifrování.

**Nástroj:** Bezplatný [Wireshark](https://www.wireshark.org/), připravený [protokol síťové expedice](./materialy/3-3-wireshark-protokol.md), příkaz `nslookup` a demonstrační stránka `https://example.com`.

**Úkoly:**

1. Zachyťte pouze krátký provoz vlastního zařízení při DNS dotazu a otevření jedné demonstrační stránky.
2. Pomocí filtrů najděte DNS dotaz/odpověď, začátek TCP spojení a TLS komunikaci.
3. Nakreslete sled `DNS → TCP → TLS → aplikační data` a oddělte metadata viditelná na síti od šifrovaného obsahu.

**Výstupy:** Anonymizovaný snímek tří vybraných paketů, vyplněný protokol, sekvenční diagram a vysvětlení rozdílu mezi capture filtrem a display filtrem.

<details>

<summary>**🧠 Rozbalit článek k tématu: Co zaslechne síťový mikroskop**</summary>

**Paket je obálka v obálce**

Síťová komunikace se vrství. Ethernetový rámec může obsahovat IP paket, ten TCP segment a ten část TLS záznamu. Wireshark tyto vrstvy rozebere a zobrazí pole každého protokolu. Je to mikroskop, nikoli rentgen na lidské úmysly: ukáže komunikaci, ale sám neví, zda je legitimní.

Když prohlížeč potřebuje `example.com`, obvykle nejprve zjistí IP adresu pomocí DNS. Potom může navázat TCP spojení trojcestným handshake `SYN → SYN/ACK → ACK`. Nad ním TLS dohodne kryptografické parametry a ověří certifikát serveru. Teprve poté putují HTTP požadavky a odpovědi chráněné šifrováním.

Moderní web může používat také HTTP/3 nad QUIC/UDP, takže konkrétní záznam se může lišit. Cílem není mechanicky najít přesně stejný počet paketů, ale vysvětlit pozorovanou variantu.

**HTTPS neschová existenci komunikace**

TLS chrání obsah a integritu aplikačních dat mezi koncovými body. Pozorovatel obvykle stále vidí zdrojovou a cílovou IP adresu, port, čas, směr, velikost a četnost paketů. DNS může odhalit doménu, pokud není použita šifrovaná varianta. Některé údaje handshake mohou být viditelné podle verze protokolu a použitých rozšíření.

To neznamená, že lze z velikosti paketu spolehlivě přečíst zprávu. Metadata mohou podporovat hypotézu, ale potřebují kontext. Stejná IP může hostovat mnoho domén a jedno zařízení komunikuje na pozadí i bez kliknutí uživatele.

**Capture filter a display filter nejsou totéž**

Capture filter rozhoduje už při záznamu, které pakety se uloží. Co nezachytí, nelze později zobrazit. Display filter pouze vybírá z již uložených dat a lze jej měnit bez ztráty. Pro začátečníka je bezpečnější krátce zachytit vlastní provoz a potom pracovat s display filtry jako `dns`, `tcp` nebo `tls`.

**Síťový záznam může obsahovat citlivá data**

Pcap soubor může zachytit adresy, názvy služeb a u nešifrovaných protokolů i obsah. Proto před měřením zavřeme ostatní aplikace, záznam rychle zastavíme a celý soubor neodevzdáváme. Ve skutečné organizaci je zachytávání síťového provozu řízená činnost s oprávněním a pravidly uchování.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup ve Wiresharku**</summary>

**Příprava a ochrana soukromí**

1. Wireshark instalujte pouze z oficiálního webu a podle pokynu učitele. Na Windows může instalace zahrnout ovladač Npcap; bez oprávnění použijte učitelskou stanici.
2. Zavřete e-mail, chat, cloudové dokumenty, herní klienty a jiné aplikace. V prohlížeči otevřete nové anonymní okno bez osobních účtů.
3. Otevřete protokol a napište předpověď: uvidíte text stránky, doménu, IP adresu, nebo jen část z těchto údajů?

**Záznam**

1. Ve Wiresharku vyberte aktivní rozhraní podle pohybujícího se grafu, například Wi-Fi. Nevybírejte všechna rozhraní.
2. Spusťte zachytávání. V příkazovém řádku proveďte `nslookup example.com` a potom v prohlížeči otevřete `https://example.com`.
3. Ihned se vraťte do Wiresharku a stiskněte Stop. Cílem je desítky až stovky paketů, nikoli dlouhý záznam celé hodiny.

**Filtry a analýza**

1. Do řádku display filter napište `dns`. Najděte dotaz obsahující `example.com` a odpověď s adresou. Pokud dotaz nevidíte kvůli cache či šifrovanému DNS, použijte výsledek `nslookup` a tuto odchylku popište.
2. Použijte `tcp.flags.syn == 1 && tcp.flags.ack == 0`. Najděte počáteční SYN k cílovému serveru a v dalších paketech odpovídající SYN/ACK a ACK.
3. Použijte `tls`. Vyberte handshake nebo aplikační data. Porovnejte strom protokolu: které hlavičky lze číst a kde začínají šifrovaná data?
4. Pravým tlačítkem na paket lze použít `Conversation Filter`, ale pouze pro tuto relaci. Nezkoušejte exportovat objekty ani dešifrovat cizí provoz.
5. Nahraďte adresy v protokolu označením `KLIENT`, `DNS` a `SERVER`. Celý pcap neodevzdávejte.

**Ověření a odevzdání**

Sekvenční diagram musí obsahovat alespoň DNS dotaz/odpověď, navázání transportu a chráněnou komunikaci. Uveďte, zda pozorovaný transport byl TCP/TLS nebo jiná moderní varianta. Závěr zakončete omezením: záznam jednoho zařízení v krátkém intervalu není obraz celé sítě a šifrování obsahu neukrývá všechna metadata.

</details>

## Experiment 3.4: Záchranný člun – záloha 3-2-1 a skutečná obnova

**Cíl:** Navrhnout malou zálohovací strategii, úmyslně poškodit pouze cvičnou pracovní kopii, provést měřenou obnovu a ověřit její integritu.

**Nástroj:** [Testovací balíček obnovy](./materialy/3-4-test-obnovy.md), dvě učitelem určená úložiště, PowerShell `Get-FileHash` nebo CyberChef a stopky.

**Úkoly:**

1. Vytvořte tři pracovní soubory, jejich manifest a dvě oddělené záložní kopie; přesně zakreslete, co model z pravidla 3-2-1 skutečně splňuje.
2. Změňte a smažte pouze cvičnou pracovní kopii a obnovte ji do nové složky při měření času.
3. Ověřte hash i čitelnost a stanovte modelové RPO a naměřené RTO.

**Výstupy:** Schéma tří kopií, manifest hashů před a po obnově, měřený protokol, výpočet RPO/RTO a návrh ochrany jedné zálohy před ransomwarem.

<details>

<summary>**🧠 Rozbalit článek k tématu: Záloha se prokáže návratem, ne zelenou ikonou**</summary>

**Tři kopie neznamenají tři složky na jednom disku**

Pravidlo 3-2-1 doporučuje tři kopie dat, dva různé druhy úložiště a jednu kopii mimo hlavní místo. Smyslem je oddělit příčiny selhání. Porucha jednoho disku zničí všechny složky na něm. Požár může zasáhnout notebook i disk ve stejné zásuvce. Ransomware může zašifrovat připojené i synchronizované kopie.

Synchronizace je užitečná, ale není automaticky záloha. Když uživatel smaže soubor nebo malware uloží zašifrovanou verzi, změna se může rychle synchronizovat. Záloha potřebuje historii, oddělení a řízenou obnovu.

**RPO se dívá dozadu, RTO dopředu**

Recovery Point Objective – RPO – popisuje přijatelnou ztrátu posledních změn. Denní záloha může při incidentu těsně před dalším během znamenat ztrátu téměř jednoho dne. Recovery Time Objective – RTO – říká, za jak dlouho má být služba obnovena. Hodnoty nejsou technické dekorace; vycházejí z dopadu na činnost.

V laboratoři změříme skutečný čas obnovy tří malých souborů. Nelze jej bezmyšlenkovitě přepočítat na celý počítač – velký objem, instalace systému, oprávnění a závislosti mohou dobu násobit. Právě tato mezera mezi malým testem a produkční obnovou je důležitým výsledkem.

**Integrita i použitelnost**

Shodný SHA-256 potvrzuje, že obnovené bajty odpovídají referenci. U dokumentu je ještě vhodné ověřit, že jej lze otevřít a obsah dává smysl. U databáze by bylo nutné zkontrolovat konzistenci a aplikaci. Hash neřeší dostupnost klíče k šifrované záloze ani správnost staršího, ale již chybného obsahu.

Moderní obrana používá offline nebo immutable kopie, oddělené účty pro zálohování a upozornění na neobvyklé mazání. Útočník často hledá zálohy dříve, než spustí ransomware. Záchranný člun proto nemá být připoután ke stejné lodi jediným snadno přeříznutelným lanem.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup obnovy**</summary>

**Příprava**

1. Podle balíčku vytvořte složku `FOTOKROUZEK-PRACE` a tři textové soubory. Nepoužívejte skutečné dokumenty.
2. Vypočítejte jejich SHA-256 příkazem `Get-FileHash -Algorithm SHA256 -LiteralPath ".\soubor.txt"` nebo operací SHA2 v CyberChef. Vyplňte manifest.
3. Vytvořte `ZALOHA-A` na učitelem určeném úložišti a `ZALOHA-B` na jiném dostupném médiu či odděleném místě. Pokud jde pouze o dvě složky stejného disku, poctivě označte, že model nesplňuje dvě média.
4. Jednu kopii po vytvoření odpojte nebo nastavte jako učitelskou „neměnnou“ kopii, se kterou studenti dále nemanipulují.

**Řízený incident**

1. Pouze v `FOTOKROUZEK-PRACE` změňte verzi a datum v jednom souboru, druhý smažte a třetí ponechte.
2. Nesahejte do Koše ani záloh. Napište předpověď, z které kopie budete obnovovat a jak dlouho to potrvá.
3. Spusťte stopky. Obnovte všechny tři správné verze do nové složky `OBNOVENO`; nepřepisujte poškozenou složku, aby zůstala k porovnání.
4. Stopky zastavte až po otevření souborů, kontrole počtu a opětovném výpočtu hashů.

| Soubor | Původní hash | Hash poškozené kopie | Hash po obnově | Otevřen a zkontrolován |
|---|---|---|---|---|
| | | | | |

**Vyhodnocení**

1. RTO laboratoře je naměřený čas. RPO stanovte podle modelové frekvence: při záloze každé čtyři hodiny lze přijít až o téměř čtyři hodiny změn.
2. Navrhněte, jak chránit zálohu před smazáním stejným účtem, jak ověřovat obnovu a kdo má být vlastníkem postupu.

**Ověření a odevzdání**

Odevzdejte manifest, schéma a protokol. Uveďte, kterou část 3-2-1 jste ve škole pouze modelovali. Potvrďte, že jste mazali výhradně cvičné soubory a že všechny testovací složky lze po kontrole učitele odstranit.

</details>

## Experiment 3.5: Radar služeb – bezpečný průzkum Nmapem

**Cíl:** Zmapovat porty a služby výhradně na vlastním počítači nebo učitelem schváleném cíli, interpretovat stavy `open`, `closed` a `filtered` a odlišit expozici od zranitelnosti.

**Nástroj:** Bezplatný [Nmap](https://nmap.org/download.html) nebo jeho grafické rozhraní [Zenmap](https://nmap.org/zenmap/) a [inventář schválených cílů](./materialy/3-5-nmap-inventar.csv).

**Úkoly:**

1. Proveďte základní TCP connect scan cíle `127.0.0.1` a zapište nalezené stavy portů.
2. Na stejném cíli proveďte omezenou identifikaci služby a porovnejte, jak se změnilo množství informací a provozu.
3. U jedné nalezené nebo modelové služby navrhněte ověření oprávněným správcem; nepokoušejte se službu zneužít.

**Výstupy:** Přesný použitý příkaz/profil, anonymizovaný výpis, tabulka portů a služeb, vysvětlení tří stavů a odstavec o oprávnění a omezeních Nmapu.

<details>

<summary>**🧠 Rozbalit článek k tématu: Zaklepat na dveře není totéž jako vloupat se – ale i klepání potřebuje svolení**</summary>

**Port je číslovaný vchod ke službě**

Operační systém rozlišuje síťové aplikace pomocí portů. Webový server často naslouchá na TCP 443, vzdálená správa na jiném portu a mnoho klientských programů na žádném příchozím portu. Nmap posílá přesně zvolené síťové podněty a podle odpovědí odhaduje stav.

`open` znamená, že aplikace přijímá spojení. `closed` obvykle znamená, že host odpověděl, ale na portu nic neposlouchá. `filtered` naznačuje, že filtr či jiná překážka neumožnila stav určit. Stav se týká konkrétního protokolu, adresy, času a místa měření.

Otevřený port není automaticky zranitelnost. Veřejný web musí být dosažitelný; riziko závisí na službě, verzi, konfiguraci, autentizaci a hodnotě aktiva. Naopak zavřený port neříká, že celý počítač je bezpečný.

**Sken má intenzitu**

Základní TCP connect scan využije běžné systémové spojení. Detekce verze `-sV` posílá další sondy a analyzuje odpovědi. OS detection, skripty a rozsáhlé rozsahy mohou být výrazně aktivnější. V laboratoři používáme jen omezené příkazy a žádné NSE skripty, hrubou sílu ani zranitelnostní testy.

`127.0.0.1` je loopback – vlastní zařízení mluví samo se sebou. Výsledek nemusí odpovídat tomu, co vidí jiný počítač přes síť a firewall, ale je bezpečným prvním cílem. Učitelský laboratorní server lze přidat jen tehdy, když je výslovně uveden v rozsahu.

**Oprávnění není technický detail**

Sken vytváří provoz a může spustit detekční systémy nebo zatížit staré zařízení. To, že znáte IP adresu, neznamená souhlas. Profesionální test má vlastníka, přesný rozsah, časové okno, povolené techniky a kontakt pro zastavení. Mimo tento rámec se z obranného měření může stát nepovolená činnost.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v Nmapu nebo Zenmapu**</summary>

**Kontrola rozsahu**

1. Otevřete inventář. Bez dalšího souhlasu je jediným cílem `127.0.0.1`. Nikdy nezadávejte náhodnou veřejnou IP, školní podsíť ani `192.168.x.0/24`.
2. Nmap instalujte z oficiálního webu podle pokynu učitele. Instalátor Windows může nabídnout Npcap a Zenmap; změnu smí provést jen oprávněná osoba.
3. Do protokolu napište cíl, vlastníka, účel, čas a povolené příkazy.

**První měření**

1. V příkazovém řádku spusťte:

   `nmap -sT 127.0.0.1`

2. V Zenmapu lze do Target zadat `127.0.0.1` a do Command přesně stejný příkaz. Nepoužívejte profil Intense scan.
3. Zapište, kolik portů bylo označeno jako open, closed nebo filtered. Nulový počet otevřených portů je platný výsledek.

**Omezená identifikace služby**

1. Na stejném cíli spusťte:

   `nmap -sT -sV --version-light 127.0.0.1`

2. Porovnejte dobu, počet sond a sloupce Service/Version. Výsledek je odhad podle odpovědí, nikoli kryptograficky ověřená identita programu.
3. Pokud učitel poskytl adresu laboratorního serveru, nahraďte cíl pouze touto adresou. Rozsah nesmíte rozšiřovat.

| Port/protokol | Stav | Odhad služby | Očekával jsem ji? | Bezpečný další krok správce |
|---|---|---|---|---|
| | | | | |

**Interpretace bez zneužití**

U otevřené služby lze doporučit ověřit vlastníka procesu, potřebnost, verzi a omezení firewallu. Nespouštějte exploit, nepokoušejte se přihlásit a nepoužívejte zranitelnostní skripty.

**Ověření a odevzdání**

Odevzdejte anonymizovaný výpis a přesný příkaz. Připojte větu: „Nmap zjišťuje dosažitelnost a odhaduje službu; samotný otevřený port není důkaz zranitelnosti.“ Uveďte také, že localhost scan neukazuje pohled jiného zařízení.

</details>

## Experiment 3.6: Síťový vyhazovač – vratné pravidlo Windows Defender Firewall

**Cíl:** Vytvořit přesně omezené odchozí pravidlo pro jednu testovací aplikaci, experimentálně ověřit blokování a bezpečně obnovit původní stav.

**Nástroj:** **Windows Defender Firewall s pokročilým zabezpečením**, vestavěný `curl.exe` nebo jiná učitelem určená testovací aplikace, [oficiální dokumentace Microsoftu](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/configure) a [vratný protokol](./materialy/3-6-firewall-protokol.md).

**Úkoly:**

1. Změřte výchozí komunikaci testovací aplikace k `https://example.com`.
2. Vytvořte dočasné odchozí pravidlo pouze pro daný program, ověřte rozdíl mezi aktivním a vypnutým pravidlem.
3. Pravidlo odstraňte, znovu ověřte komunikaci a vysvětlete rozdíl mezi příchozím/odchozím a stavovým filtrováním.

**Výstupy:** Úplný protokol čtyř fází, snímek konfigurace bez citlivých údajů, důkaz obnovení a diagram rozhodnutí firewallu.

<details>

<summary>**🧠 Rozbalit článek k tématu: Firewall není zeď, ale velmi rychlý rozhodčí**</summary>

**Každý paket předkládá průkaz**

Firewall porovnává síťovou komunikaci s pravidly. Může zvažovat směr, protokol, port, adresu, aplikaci, síťový profil a stav spojení. Výsledkem je povolení nebo blokování. Nečte lidský záměr a sám nerozezná legitimní program od malwaru, pokud oba splňují stejné podmínky.

Příchozí pravidla řídí komunikaci směřující k místním službám. Odchozí pravidla řeší spojení zahájená aplikacemi zařízení. Windows běžně blokuje mnoho nevyžádaných příchozích spojení a povoluje odchozí provoz, pokud jej nezakazuje pravidlo.

**Stavový firewall si pamatuje rozhovor**

Když zařízení zahájí povolené spojení, firewall si uchovává stav a dovolí odpovědi patřící do stejné komunikace. Nemusíme ručně otevřít náhodný příchozí port pro každou webovou odpověď. Stav však není obsahová analýza; povolené HTTPS může přenášet užitečná i škodlivá data.

**Pravidlo pro program je přesnější než otevřený port**

Povolování konkrétní aplikace obvykle omezuje plochu více než trvale otevřený port pro všechny procesy. Stále záleží na správné cestě, podpisu a možnosti, že aplikaci někdo zneužije. Pořadí a precedence pravidel mohou být složité, zejména v doménově spravovaném počítači.

V laboratoři blokujeme pouze odchozí komunikaci `curl.exe`. Prohlížeč a práce třídy zůstávají nedotčené. Název pravidla je jednoznačný a postup zahrnuje jeho vypnutí, odstranění i závěrečný test. Právě návrat je součást experimentu, ne úklid navíc.

**Firewall je jedna vrstva**

Pokud povolená aplikace odešle data, firewall ji nemusí zastavit. Pokud malware používá důvěryhodný proces nebo cloudovou službu, jednoduché pravidlo může být nedostatečné. Ochranu doplňují aktualizace, omezení oprávnění, DNS/web filtering, EDR, segmentace, logy a reakce na incident.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup firewallu a návratu**</summary>

**Podmínky před zahájením**

1. Experiment provádějte pouze na zařízení výslovně určeném učitelem. Vyžaduje oprávnění správce. Na spravovaném školním počítači může pravidla řídit politika a místní změna nemusí být povolena.
2. Otevřete PowerShell nebo Terminál a ověřte dostupnost příkazem `curl.exe --version`. Není-li dostupný, učitel určí neprodukční aplikaci; neblokujte bez domluvy hlavní prohlížeč.
3. Do protokolu zapište výchozí stav a jedinečný název `PV-LAB-3-6-DOCASNE-BLOKOVANI`.

**Výchozí test**

1. Spusťte `curl.exe -I https://example.com`.
2. Zapište, zda jste obdrželi HTTP hlavičky a jak dlouho test trval. Prohlížeč není měřicím nástrojem tohoto pravidla.

**Vytvoření pravidla**

1. Otevřete Windows Security → Firewall a ochrana sítě → Upřesnit nastavení. Potvrzení správce provede učitel.
2. Vyberte `Odchozí pravidla` → `Nové pravidlo`. Zvolte typ `Program` a přesnou cestu k `curl.exe`, obvykle `C:\Windows\System32\curl.exe`; cestu nejprve ověřte.
3. Zvolte `Blokovat připojení`, ponechte učitelem určené profily a použijte přesný laboratorní název. Do popisu napište čas vytvoření a „ODSTRANIT PO TESTU“.
4. Pravidlo otevřete a zkontrolujte směr, akci, program a stav Enabled. Nevytvářejte obecné pravidlo pro všechny programy.

**Měření a návrat**

1. Opakujte `curl.exe -I https://example.com`. Zaznamenejte chybové hlášení a čas. Neúspěch může mít i jinou příčinu; porovnávejte s výchozím stavem.
2. Pravidlo nejprve zakažte volbou Disable Rule a test zopakujte. Komunikace by se měla vrátit.
3. Pravidlo odstraňte volbou Delete. Ověřte, že v seznamu již není, a proveďte poslední test.
4. Pokud komunikace nefunguje, nepřidávejte další pravidla. Zastavte práci a předejte zařízení učiteli.

**Ověření a odevzdání**

Odevzdejte protokol se čtyřmi stavy a anonymizovaný snímek jediného pravidla. Učitel potvrdí jeho odstranění. Vysvětlete, proč blokace jedné aplikace neznamená odpojení počítače od sítě a proč firewall nenahrazuje ochranu proti malwaru.

</details>

## Závěrečná reflexe

**Který postup nejlépe odpovídá práci při podezření na incident?**

<!-- data-randomize="true" -->
[( )] Odstranit všechny neznámé položky a potom zjišťovat, co se stalo.
[( )] Považovat každý otevřený port a každý červený log za potvrzený útok.
[(X)] Zachovat stopy, porovnat více zdrojů, omezit dopad přiměřeným krokem a uvést nejistotu závěru.
[( )] Pokud antivirus nic nehlásí, další vrstvy nejsou potřeba.

Vyberte jeden experiment a doplňte konkrétní řetězec:

`událost → zachycená stopa → interpretace → další ověření → bezpečné rozhodnutí → možnost návratu`
