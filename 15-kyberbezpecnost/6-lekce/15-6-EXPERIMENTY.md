<!--
author: Marek Lučný
title: Bezpečná správa zařízení a účtů – praktická laboratoř
language: cs
mode: Textbook
comment: Šest praktických experimentů k šesté lekci okruhu Kyberbezpečnost.
-->

# Praktická laboratoř: Bezpečná správa zařízení a účtů

Největší bezpečnostní problém často nevypadá jako útok z filmu. Je to zapomenutá aplikace s přístupem k účtu, starý tablet bez aktualizací, všudypřítomný administrátor nebo jediná domácí síť pro notebook, televizi i levnou chytrou zásuvku. V šesti experimentech budete bezpečnost **spravovat**: objevíte majetek, omezíte oprávnění, oddělíte rizika, naplánujete konec životnosti a nacvičíte první minuty incidentu.

> **🛡️ Pravidlo bezpečných změn**
>
> Na školních a cizích zařízeních nic neměňte bez výslovného souhlasu vlastníka nebo správce. Každá změna musí mít zaznamenaný původní stav, způsob ověření a plán návratu. Osobní účty jsou vždy dobrovolné; rovnocennou variantou je připravený model. Nikdy nemažte skutečný účet, zařízení ani data jen kvůli cvičení.

| Experiment | Praktický problém | Nástroj | Orientační čas |
|---|---|---|---:|
| 6.1 Co vlastně chráníme? | inventář aktiv a rizik | systémové informace, tabulka | 35 min |
| 6.2 Kdo má klíče od účtu? | přístupy aplikací třetích stran | nastavení Google / Microsoft / Apple | 35 min |
| 6.3 Jeden den bez koruny správce | princip nejmenších oprávnění | účty Windows, UAC | 40 min |
| 6.4 Karanténa pro chytrou žárovku | segmentace a hostovská síť | router / bezpečná simulace | 45 min |
| 6.5 Technologická archeologie | životní cyklus a konec podpory | systémové nástroje, endoflife.date | 40 min |
| 6.6 Telefon zmizel – čas běží | reakce na incident | stolní scénář a playbook | 45 min |

U všech výstupů anonymizujte jména, e-maily, sériová čísla, veřejné IP adresy, identifikátory zařízení a skutečné názvy domácích sítí. Bezpečnostní protokol má ukázat postup a důkazy, ne vytvořit nový únik dat.

## Experiment 6.1: Co vlastně chráníme?

**Cíl:** Vytvořit použitelný inventář digitálních aktiv, přiřadit vlastnictví, důležitost a stav podpory a z inventáře odvodit tři konkrétní bezpečnostní priority.

**Nástroj:** Vestavěné systémové informace Windows/Android/iOS, tabulkový editor a připravený [model inventáře školního fotokroužku](./materialy/6-1-inventar-fotokrouzku.csv). Není nutný žádný skener sítě.

**Úkoly:**

1. Zkontrolujte a opravte modelový inventář: najděte chybějícího vlastníka, nejasnou důležitost, zařízení bez údaje o podpoře a aktivum, které v tabulce úplně chybí.
2. U jednoho vlastního nebo školního zařízení pouze se svolením zjistěte model, verzi systému, datum poslední aktualizace a stav zálohy; údaje zapište anonymizovaně.
3. Seřaďte rizika podle dopadu a naléhavosti a navrhněte vlastníka i termín prvních tří opatření.

**Výstupy:** Opravený anonymizovaný inventář; karta jednoho ověřeného zařízení; žebříček tří priorit s důkazem, odpovědnou rolí a termínem; seznam údajů, které inventář záměrně neukládá.

<details>

<summary>**🧠 Rozbalit článek: Mapa pokladu dříve než vysoká zeď**</summary>

**Neznámé zařízení nelze rozumně chránit**

Organizace může koupit moderní firewall a přesto nechat důležitá data na zapomenutém notebooku ve skříni. Bez inventáře neví, co aktualizovat, zálohovat, vyřadit ani komu zavolat při incidentu. Inventář aktiv je proto mapa: nebrání útočníkovi přímo, ale bez něj obránce neví, kde jsou dveře, poklad ani slepé uličky.

Aktivem není jen hardware. Patří sem operační systém, aplikace, uživatelské a servisní účty, cloudové služby, domény, kryptografické klíče, zálohy i data. Fotokroužek například chrání snímky žáků, souhlasy s publikací, sdílený disk, účet sociální sítě a notebook pro úpravy. Ztráta každého aktiva má jiný dopad.

**Soupis bez vlastníka je seznam nalezených věcí**

Každé aktivum potřebuje vlastníka v organizačním smyslu: roli, která rozhoduje o jeho použití, klasifikaci a vyřazení. Nemusí to být člověk, který zařízení drží v ruce. Správce může systém technicky udržovat, zatímco vedoucí kroužku odpovídá za to, kdo smí vidět fotografie.

Důležitá je také vazba na proces. Notebook může být levný a snadno nahraditelný, ale pokud obsahuje jedinou kopii fotografií před soutěží, jeho dočasná ztráta má velký dopad. Cena zařízení proto není totéž co hodnota aktiva. Ptejte se na důvěrnost, integritu i dostupnost: co se stane, když data někdo přečte, změní nebo na týden znepřístupní?

**Kolik detailů je tak akorát?**

Příliš chudý inventář nepomůže; příliš bohatý se neudržuje a sám se stane citlivou databází. Užitečné bývají kategorie zařízení, vlastník, správce, účel, verze, stav podpory, důležitost, záloha a datum posledního ověření. Hesla, obnovovací kódy a soukromé klíče do běžné tabulky inventáře nepatří. Přesná domácí adresa či veřejná IP také nebývá pro školní úkol potřebná.

Inventář není jednorázová fotografie. Každý záznam by měl mít datum kontroly a proces přidání, změny i vyřazení. Jinak mapa stárne rychleji než skutečný terén. Dobrá priorita pak nevzniká z nejvýraznější barvy v tabulce, ale ze spojení dopadu, pravděpodobnosti a skutečného důkazu.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Audit modelu**

1. Otevřete [inventář fotokroužku](./materialy/6-1-inventar-fotokrouzku.csv) v tabulkovém editoru. Nejdříve zjistěte význam sloupců; prázdné pole neznamená automaticky „ne“.
2. Označte položky, u nichž chybí vlastník, verze, stav podpory, záloha nebo datum kontroly. Rozlište `nezjištěno`, `nevztahuje se` a skutečně zápornou hodnotu.
3. Doplňte alespoň jedno nehardwarové aktivum, které scénář potřebuje: například cloudový účet, souhlas s publikací nebo záložní médium.
4. Každému aktivu přiřaďte důležitost pro důvěrnost, integritu a dostupnost na stupnici 1–3. Číslo doplňte jednou větou zdůvodnění.

**Ověření skutečného zařízení**

1. Použijte vlastní zařízení nebo školní počítač určený učitelem. Ve Windows spusťte `winver`, otevřete `Nastavení → Systém → O systému` a historii Windows Update. V mobilním systému použijte informace o telefonu a stránku aktualizací.
2. Zapište jen obecný model nebo kategorii, verzi systému, datum poslední úspěšné aktualizace a to, zda je zapnutá automatická aktualizace. Nezapisujte produktový klíč, sériové číslo, IMEI ani identifikátor reklam.
3. Stav zálohy neodhadujte podle existence ikony cloudu. Najděte datum posledního úspěšného běhu nebo použijte hodnotu `neověřeno`. Žádnou osobní fotografii neotevírejte.

| Aktivum | Vlastník | Účel | C/I/A | Verze a podpora | Záloha | Ověřeno dne |
|---|---|---|---|---|---|---|
| anonymizované zařízení | | | | | | |

**Prioritizace**

Pro každou mezeru napište scénář následku. Potom vyberte tři priority ve formátu: `důkaz → riziko → opatření → vlastník → termín → ověření`. „Aktualizovat vše“ není dostatečné opatření; lepší je například „správce do pátku ověří podporovanou verzi systému na notebooku pro úpravy; úspěch doloží novou verzí a datem kontroly“. Nakonec uveďte, kdo a kdy inventář aktualizuje.

</details>

## Experiment 6.2: Kdo má klíče od účtu?

**Cíl:** Provést audit aplikací a služeb třetích stran připojených k účtu, rozlišit přihlášení od uděleného přístupu a bezpečně rozhodnout, co ponechat, omezit nebo odpojit.

**Nástroj:** Bezpečnostní nastavení účtu Google, Microsoft nebo Apple, například oficiální [správa připojení třetích stran u Googlu](https://support.google.com/accounts/answer/14012355), a [anonymní auditní list](./materialy/6-2-audit-aplikaci.md). Osobní kontrola je dobrovolná; učitel poskytne modelové snímky nebo fiktivní seznam.

**Úkoly:**

1. Vypište připojené aplikace bez zveřejnění identity účtu a u každé zjistěte poskytovatele, rozsah oprávnění, poslední použití a známý účel.
2. Rozdělte položky na `ponechat`, `ověřit` a `odebrat`; pro každé rozhodnutí uveďte důkaz, nikoli jen pocit nebo neznámý název.
3. U vlastní jednoznačně nepotřebné aplikace lze dobrovolně odebrat přístup, ale až po kontrole dopadu a plánu opětovného připojení. Modelová varianta změnu pouze simuluje.

**Výstupy:** Anonymizovaná tabulka auditu; rozhodnutí pro nejméně pět modelových nebo skutečných položek; popis jedné bezpečně provedené či simulované revokace; plán pravidelné kontroly.

<details>

<summary>**🧠 Rozbalit článek: Digitální náhradní klíče, na které se zapomnělo**</summary>

**„Přihlásit se pomocí…“ je pohodlná brána**

Když aplikace nabídne přihlášení pomocí Google, Microsoftu nebo Applu, uživatel jí obvykle nesděluje heslo k hlavnímu účtu. Poskytovatel identity potvrdí, kdo se přihlašuje, a aplikace obdrží token. Podle uděleného rozsahu může získat jen základní identitu, ale také přístup ke kalendáři, souborům, poště nebo kontaktům.

Token je jako časově a účelově omezený náhradní klíč. Změna hlavního hesla nemusí automaticky zrušit každý dříve udělený přístup. Proto má smysl samostatný seznam připojených aplikací a možnost přístup odvolat. Audit není hon na neznámé názvy; je to ověření, zda každý klíč stále potřebujeme a zda otevírá jen správné dveře.

**Oprávnění mají význam v kontextu**

Kalendářová aplikace může legitimně číst a zapisovat události. Jednoduchý převodník obrázků stejný přístup pravděpodobně nepotřebuje. Přesto nelze rozhodnout jen podle počtu oprávnění. Zajímají nás účel, důvěryhodnost vydavatele, poslední použití, citlivost dat a možnost méně privilegované alternativy.

Princip nejmenších oprávnění říká, že subjekt má mít pouze přístup nezbytný pro úkol a jen po potřebnou dobu. V praxi je těžké jej udržet, protože souhlasy se hromadí. Aplikaci jsme potřebovali pro jediný školní projekt před dvěma lety, ale token mohl zůstat aktivní. Pravidelná revize zmenšuje plochu, kterou může zasáhnout kompromitace dodavatele.

**Odpojení není vymazání dat**

Odebrání přístupu obvykle zabrání dalšímu použití tokenu. Nemusí smazat účet u dané služby ani data, která si aplikace dříve zkopírovala. Chceme-li službu opustit, musíme prostudovat její nastavení a pravidla mazání. Naopak ukvapené odpojení může zastavit zálohování fotografií, školní kalendář nebo domácí automatizaci.

Bezpečný audit proto zaznamenává dopad a vratnost. Neznámá aplikace je důvod k pátrání, nikoli automaticky důkaz napadení. Pokud ale uživatel přístup nikdy neudělil, je na místě revokace, kontrola posledních přihlášení, zabezpečení účtu a oznámení podle pravidel organizace.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Výběr varianty**

1. Chcete-li použít vlastní účet, pracujte sami, nezobrazujte stránku spolužákům a do protokolu nedávejte e-mail, avatar ani skutečné názvy citlivých služeb. Učitel nepožaduje snímek osobního účtu.
2. Jinak použijte fiktivní seznam připravený učitelem. Hodnotí se kvalita rozhodnutí, ne počet skutečných propojení.
3. K nastavení přejděte ručně přes správu zabezpečení účtu. U Googlu hledejte stránku připojení třetích stran, u Microsoftu aplikace a služby s přístupem a u Apple přihlášení přes Apple. Nereagujte na nevyžádaný odkaz v e-mailu.

**Inventura náhradních klíčů**

1. U každé položky zjistěte zobrazovaného vydavatele, typ připojení, oprávnění a poslední použití, pokud je služba ukazuje.
2. Název anonymizujte jako `kalendář A`, `editor B` nebo `neznámá hra C`. Do [auditního listu](./materialy/6-2-audit-aplikaci.md) napište účel a zda službu stále používáte.
3. Rozhodněte:
   - `ponechat`, pokud je účel známý, přístup přiměřený a služba používaná;
   - `ověřit`, pokud chybí informace nebo by odpojení mohlo něco přerušit;
   - `odebrat`, pokud je služba prokazatelně nepotřebná nebo neautorizovaná.

**Bezpečná revokace**

1. U kandidáta k odpojení zjistěte, co přestane fungovat, zda jsou potřebná data uložená a jak lze přístup znovu udělit. U školního účtu změnu schvaluje správce.
2. Teprve potom zvolte odebrání přístupu a přečtěte potvrzovací dialog. Neodstraňujte celý hlavní účet ani data aplikace.
3. Obnovte seznam a ověřte, že položka zmizela nebo je označena jako odpojená. Kdyby šlo o neočekávaný přístup, pokračujte kontrolou relací, MFA a bezpečnostních upozornění.
4. V modelové variantě napište, kam byste klikli a jak byste výsledek ověřili, ale žádnou změnu neprovádějte.

**Závěr**

Sečtěte položky v jednotlivých kategoriích a napište datum další revize, například za tři měsíce. Vysvětlete rozdíl mezi odvoláním tokenu, změnou hesla a smazáním dat u třetí strany. Osobní počty lze odevzdat jako rozsah; konkrétní názvy nejsou nutné.

</details>

## Experiment 6.3: Jeden den bez koruny správce

**Cíl:** Na testovacím počítači vytvořit standardní uživatelský účet, porovnat jeho možnosti s administrátorem a prakticky pozorovat, jak řízení uživatelských účtů omezuje nechtěné systémové změny.

**Nástroj:** Testovací počítač nebo virtuální stroj s Windows, [oficiální postup správy účtů ve Windows](https://support.microsoft.com/en-us/windows/security/identity-signin/manage-user-accounts-in-windows), nastavení uživatelských účtů a mechanismus UAC. Experiment provádí učitel či student s výslovným oprávněním; na běžném školním počítači se změny nesmějí dělat svévolně.

**Úkoly:**

1. Vytvořte lokální cvičný účet `PV-Standard` bez administrátorských oprávnění a ověřte jeho zařazení.
2. Porovnejte tři běžné činnosti standardního účtu a pokus o schválenou systémovou změnu, která vyvolá požadavek na oprávnění správce.
3. Vysvětlete rozdíl mezi přihlášením jako správce, potvrzením UAC a zadáním správcovských údajů; po kontrole proveďte schválený úklid.

**Výstupy:** Tabulka povolených a blokovaných činností; anonymizované pozorování dialogu UAC; vysvětlení principu nejmenších oprávnění; záznam návratu testovacího zařízení do původního stavu.

<details>

<summary>**🧠 Rozbalit článek: Proč pilot neletí celý den s odjištěným katapultem**</summary>

**Oprávnění určují dosah chyby**

Uživatel potřebuje psát dokumenty, prohlížet web a měnit vlastní nastavení. K tomu obvykle nepotřebuje instalovat systémové ovladače, měnit ochranu všech účtů nebo zapisovat do chráněných částí systému. Pokud běžná práce probíhá s nejvyššími oprávněními, každé chybné kliknutí i spuštěný program získává větší možný dopad.

Princip nejmenších oprávnění omezuje účet na schopnosti nezbytné pro jeho roli. Není to nedůvěra k uživateli; je to bezpečnostní pás pro chvíli, kdy se splete člověk nebo aplikace. Standardní účet může utrpět incident, ale některé systémové změny narazí na hranici a vyžádají si rozhodnutí správce.

**UAC není jen otravné okno**

Řízení uživatelských účtů ve Windows upozorní, když operace vyžaduje zvýšená oprávnění. Správce může být vyzván k potvrzení, standardní uživatel zpravidla k zadání přihlašovacích údajů oprávněného správce. Dialog vytváří přechod mezi běžným a zvýšeným kontextem.

UAC není bezpečnostní kouzlo ani náhrada aktualizací. Pokud uživatel bez čtení schválí každý požadavek a zadá heslo neznámému programu, bariéru sám otevře. Smyslem je, aby zvýšení nebylo tiché a automatické. Dobrý dialog čteme: kdo jej vyvolal, jaký vydavatel je uveden a očekávali jsme právě tuto změnu?

**Oddělené role zlepšují i dohledatelnost**

Správce by měl mít zvláštní účet pro správu a běžnou práci dělat standardním účtem. Když administrativní oprávnění používá více lidí přes jeden sdílený účet, obtížně se zjišťuje, kdo změnu provedl, a heslo se šíří. Pojmenované účty a zaznamenané zvýšení pomáhají odpovědnosti.

Ne každé omezení musí být technicky absolutní. Standardní uživatel může instalovat některé aplikace jen do svého profilu a škodlivý program může poškodit jeho dostupná data. Cíl experimentu není dokázat „standardní účet je neprolomitelný“, ale pozorovat zmenšení oprávnění a pochopit jeho místo ve vrstvené obraně.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Předpoklady a návratový plán**

1. Učitel určí testovací zařízení nebo připravený virtuální stroj. Zapište existující účty pouze podle rolí, ne skutečných jmen, a ověřte, že znáte funkční správcovský účet pro návrat.
2. Před změnou vytvořte bod obnovení virtuálního stroje, pokud jej prostředí podporuje. Na produkčním školním počítači se účet vytváří jen podle postupu správce.
3. Cvičný účet nebude připojen k Microsoft účtu a nebude obsahovat osobní data. Použijte jedinečné dočasné heslo určené učitelem.

**Vytvoření účtu**

1. V nastavení Windows otevřete `Účty → Ostatní uživatelé` nebo odpovídající stránku aktuální verze.
2. Přidejte místního uživatele `PV-Standard`. Když průvodce nabízí online účet, použijte schválenou možnost vytvoření uživatele bez účtu Microsoft.
3. Otevřete typ účtu a ověřte `Standardní uživatel`. Pokud je nastaven správce, před přihlášením typ opravte.
4. Odhlaste se a přihlaste jako `PV-Standard`. Nevytvářejte v profilu žádný skutečný dokument.

**Čtyři zkoušky**

1. Vytvořte textový soubor ve vlastní složce Dokumenty. Zapište, že běžná práce je povolena.
2. Změňte pozadí nebo jiné čistě osobní nastavení a výsledek ověřte.
3. Pokuste se otevřít chráněné nastavení určené učitelem, například změnu systémového času nebo instalaci předem schváleného neškodného balíčku. **Nic nestahujte náhodně z internetu.**
4. Když se objeví UAC, změnu zatím nepotvrzujte. Zaznamenejte název programu, vydavatele, požadavek na údaje správce a bezpečnou plochu. Učitel může demonstraci dokončit testovacími údaji nebo ji zrušit.

| Činnost | Standardní účet sám | Vyžádá zvýšení | Pozorovaný dopad |
|---|---|---|---|
| vytvoření vlastního souboru | | | |
| osobní nastavení | | | |
| systémová změna | | | |
| přístup k datům jiného účtu | | | |

**Úklid**

Odhlaste cvičný účet, přihlaste se schváleným správcem a po kontrole výstupů účet `PV-Standard` odstraňte včetně prázdného profilu, pokud to byl domluvený návratový plán. Před potvrzením ověřte přesný název – nemažte žádný jiný účet. Do protokolu napište, kdo úklid schválil a jak bylo ověřeno obnovení původního stavu.

</details>

## Experiment 6.4: Karanténa pro chytrou žárovku

**Cíl:** Navrhnout a v bezpečném prostředí ověřit oddělení nedůvěryhodných IoT/hostovských zařízení od hlavní sítě při zachování potřebného přístupu k internetu.

**Nástroj:** Domácí nebo laboratorní router s hostovskou sítí, pouze se souhlasem vlastníka, případně učitelská simulace. Plán změny se zapisuje do [připravené šablony segmentace](./materialy/6-4-plan-segmentace.md).

**Úkoly:**

1. Nakreslete současnou a cílovou síť pro domácnost se správcovským notebookem, telefony, tiskárnou, televizí a chytrou žárovkou.
2. Vytvořte plán hostovské/IoT sítě včetně názvu, šifrování, izolace klientů, povolených toků, testů a návratu.
3. Na schváleném routeru nebo v simulaci ověřte, že testovací zařízení dosáhne na internet, ale ne na správu routeru či chráněné zařízení hlavní sítě.

**Výstupy:** Dva síťové diagramy; vyplněný plán změny; tabulka alespoň čtyř testů; výsledek skutečné nebo simulované segmentace a popis omezení hostovské sítě.

<details>

<summary>**🧠 Rozbalit článek: Proč žárovka nepotřebuje klíč od pracovny**</summary>

**Jedna Wi‑Fi, mnoho různých úrovní důvěry**

Domácí síť může obsahovat aktualizovaný notebook s pracovními dokumenty i levné zařízení, jehož výrobce už neposílá opravy. Když jsou všechny přístroje ve stejné ploché síti, kompromitovaná žárovka nebo návštěvníkův notebook může zkoušet komunikovat s dalšími místními službami. Internetové připojení samo o sobě nevyžaduje tak široký přístup.

Segmentace rozděluje síť do zón a mezi nimi uplatňuje pravidla. Hostovská Wi‑Fi bývá nejdostupnější domácí variantou: návštěvníkům a IoT poskytne internet, ale brání nebo omezuje komunikaci do hlavní sítě. V podnikových sítích se používají VLAN, firewally a řízení identity, princip je však podobný – každý tok musí mít důvod.

**Izolace může znamenat několik různých věcí**

Volba „guest network“ nemusí na každém routeru dělat totéž. Některý blokuje přístup z hostů do hlavní LAN, jiný navíc izoluje hosty navzájem. To je důležité: dvě zařízení na hostovské síti se jinak mohou stále vidět. Dokumentace a praktický test jsou spolehlivější než název přepínače.

Příliš přísné oddělení může rozbít tisk, odesílání obrazu do televize nebo prvotní nastavení IoT z telefonu. Řešením není bezmyšlenkovitě vše povolit, ale popsat nezbytný tok. Možná telefon při konfiguraci dočasně připojíme do IoT sítě; možná router dovolí konkrétní komunikaci. Bez přesné potřeby se výjimka snadno změní v díru velikosti původní sítě.

**Dostupnost je součást bezpečnosti**

Změna routeru může odpojit domácnost, proto vyžaduje návratový plán. Správce má znát způsob přístupu, původní nastavení a fyzickou možnost obnovy, ale reset do továrního stavu není běžný první krok – mohl by smazat nastavení poskytovatele. Změny se dělají v domluveném čase, po jedné, a každá se testuje.

Hostovská síť také nenahradí aktualizace zařízení, unikátní hesla ani zabezpečení cloudového účtu výrobce. Zmenšuje dopad jednoho problému. Je to protipožární dveřní přepážka: sama požáru nezabrání, ale nedovolí mu tak snadno obsadit celý dům.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Varianta bez zásahu do routeru**

1. Pokud nemáte výslovný souhlas vlastníka a zálohu nastavení, použijte simulaci. Učitel poskytne snímky modelového rozhraní nebo demonstrační router odpojený od produkční sítě.
2. Do [plánu segmentace](./materialy/6-4-plan-segmentace.md) zapište modelové názvy `HLAVNI` a `IOT-HOSTE`, nikdy skutečné SSID, veřejnou IP ani správcovské heslo.
3. Nakreslete výchozí stav, v němž jsou všechna zařízení v jedné zóně. V cíli ponechte správní notebook a citlivé úložiště v hlavní síti, zatímco návštěvy a IoT přesunete do oddělené zóny.

**Plán řízené změny**

1. Určete povolené toky. Typicky `IOT-HOSTE → internet: ano`, `IOT-HOSTE → správa routeru: ne`, `IOT-HOSTE → zařízení hlavní LAN: ne` a podle možností `host → host: ne`.
2. Zvolte WPA2 nebo WPA3 podle podporovaných zařízení a dlouhou jedinečnou laboratorní frázi. WEP ani otevřenou síť nepoužívejte.
3. Zapište původní stav a návrat: vypnout novou hostovskou síť a vrátit změněná testovací zařízení na předchozí schválené připojení. Export konfigurace ukládejte jen bezpečně a podle dokumentace zařízení.

**Provedení na schváleném zařízení**

1. Ke správě se připojte z důvěryhodného zařízení v místní síti, adresu routeru zjistěte z dokumentace nebo nastavení brány. Nepoužívejte vyhledaný cizí „admin portál“.
2. Aktivujte hostovskou síť a zakažte přístup k místní síti či správě routeru. Pokud je dostupná izolace klientů, zapněte ji a zaznamenejte přesný význam z dokumentace výrobce.
3. Připojte pouze testovací zařízení bez citlivých dat. Nejdřív ověřte přidělení adresy a běžnou stránku na internetu.
4. Zkuste otevřít lokální adresu správy routeru a schválený testovací server v hlavní síti. Očekává se blokace; neprovádějte skenování portů ani pokusy o obejití.
5. Druhé testovací zařízení ve stejné hostovské síti použijte k ověření izolace klientů, pokud je to součást plánu.

| Test | Očekávání | Skutečnost | Splněno |
|---|---|---|---|
| získání síťové konfigurace | ano | | |
| přístup na internet | ano | | |
| přístup do hlavní LAN | ne | | |
| otevření správy routeru | ne | | |
| komunikace mezi hosty | podle plánu | | |

Po měření proveďte domluvený návrat nebo ponechání konfigurace schválí vlastník. Závěr musí uvést, zda izolace blokuje jen hlavní LAN, nebo také komunikaci hostů navzájem.

</details>

## Experiment 6.5: Technologická archeologie

**Cíl:** Zjistit přesnou verzi několika produktů, dohledat jejich životní cyklus v primárním zdroji a vytvořit realistický plán pro software, jehož podpora končí nebo již skončila.

**Nástroj:** Vestavěné informace o verzi, veřejný orientační přehled [endoflife.date](https://endoflife.date/) a především oficiální dokumentace výrobců. Výsledky se zapisují do [modelového EOL inventáře](./materialy/6-5-eol-inventar.csv).

**Úkoly:**

1. U modelových nebo schválených skutečných zařízení zjistěte přesný produkt, řadu/verzi a datum kontroly.
2. Na endoflife.date vyhledejte orientační stav a každý důležitý termín ověřte v odkazované oficiální dokumentaci výrobce.
3. Pro jeden podporovaný, jeden brzy končící a jeden nepodporovaný produkt navrhněte akci, termín, vlastníka a dočasná kompenzační opatření.

**Výstupy:** Doplněný EOL inventář s odkazy a datem ověření; tři klasifikované případy; migrační mini-plán; vysvětlení rozdílu mezi vydáním nové verze, koncem běžné podpory a koncem bezpečnostních aktualizací.

<details>

<summary>**🧠 Rozbalit článek: Software není jogurt, ale datum spotřeby má**</summary>

**Funguje neznamená je podporovaný**

Starý systém se může každé ráno spustit a přesto už nedostávat opravy nově objevených zranitelností. Na obrazovce se nerozsvítí velké červené `EOL`; aplikace dál dělá přesně to, co včera. Bezpečnostní dluh je proto tichý. Útočníci přitom mohou veřejně studovat opravené chyby novějších větví a hledat, zda zůstaly ve staré.

Životní cyklus produktu má více milníků. Vydání novější verze nemusí ukončit podporu starší. Konec běžné podpory může znamenat, že výrobce nepřidává funkce, ale stále vydává kritické bezpečnostní opravy. **End of life** či **end of support** se navíc mezi výrobci používá různě. Rozhodující je přesná produktová řada, edice a politika dodavatele.

**Sekundární přehled je radar, primární zdroj je mapa**

Web endoflife.date pohodlně soustřeďuje mnoho produktů a hodí se k rychlému vyhledání kandidátů. Je to komunitní sekundární zdroj, takže důležité rozhodnutí ověřujeme v oficiální dokumentaci výrobce. Zaznamenáváme URL i datum kontroly; výrobce může podporu prodloužit, politiku změnit nebo rozlišit placený program rozšířených aktualizací.

Přesnost verze je kritická. „Windows“, „Android“ nebo „Python“ není dostatečný údaj. Potřebujeme například řadu, edici a někdy build. Stejně tak u telefonu může podporu ovlivnit výrobce konkrétního modelu, ne jen obecná verze Androidu.

**Migrace není tlačítko Aktualizovat**

Nepodporovaný produkt se má nahradit, ale okamžité vypnutí může přerušit výuku, výrobu nebo zdravotnický proces. Plán proto obsahuje závislosti, test, zálohu, termín a vlastníka. Dočasně lze zařízení izolovat, omezit jeho účty, zakázat nedůležité služby a zvýšit dohled. Tato kompenzační opatření nekonečnou podporu nevytvoří; pouze snižují riziko do migrace.

Priorita závisí i na expozici a dopadu. Nepodporovaný offline ovladač laboratorního přístroje je jiný případ než nepodporovaný webový server dostupný z internetu. Dobrá EOL evidence proto není sbírka datumů, ale podklad pro rozhodnutí.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Zjištění přesné verze**

1. Otevřete [EOL inventář](./materialy/6-5-eol-inventar.csv). U modelových položek nejprve označte, který údaj chybí k jednoznačnému určení životního cyklu.
2. Ve Windows použijte `winver` a stránku `Systém → O systému`. Ve webovém prohlížeči otevřete stránku O aplikaci. Pro Python lze použít `python --version`, je-li nainstalován. Na telefonu otevřete informace o zařízení a úroveň bezpečnostní aktualizace.
3. Neinstalujte staré verze jen kvůli experimentu. Pokud zařízení nemáte, pracujte s modelovým záznamem učitele.

**Dvojí ověření termínu**

1. Vyhledejte produkt na endoflife.date a zkontrolujte, zda jste zvolili správnou řadu. Zapište orientační datum konce podpory a datum dnešní kontroly.
2. Otevřete odkaz na dokumentaci výrobce nebo samostatně najděte oficiální lifecycle stránku. Porovnejte termín, edici a případnou rozšířenou podporu.
3. Pokud se zdroje liší, nevytvářejte průměr. Zapište rozpor, použijte primární zdroj pro rozhodnutí a navrhněte, kdo informaci ověří.

| Produkt a přesná řada | Verze | Stav | Oficiální zdroj | Datum kontroly | Akce |
|---|---|---|---|---|---|
| | | podporován / brzy EOL / EOL | | | |

**Migrační mini-plán**

1. Vyberte nejrizikovější nepodporovanou položku podle expozice, citlivosti a důležitosti služby.
2. Napište cílový podporovaný stav a předpoklady: kompatibilita souborů, ovladačů, účtů, záloh a návazných aplikací.
3. Rozdělte plán na testovací migraci, ověření, produkční změnu a návrat. Každý krok dostane vlastníka a termín.
4. Do doby migrace navrhněte dvě přiměřená opatření, například síťovou izolaci a zákaz běžného webového prohlížení. Nevydávejte je za trvalou náhradu aktualizací.

Na závěr napište, jak často by se inventář měl automaticky či ručně kontrolovat a kolik měsíců před EOL musí začít plánování náhrady.

</details>

## Experiment 6.6: Telefon zmizel – čas běží

**Cíl:** V časovaném stolním cvičení vytvořit a prověřit playbook reakce na ztracený odemčený telefon s přístupem ke školnímu e-mailu, cloudu a vícefaktorovému ověřování.

**Nástroj:** [Šablona incidentního playbooku](./materialy/6-6-playbook.md), modelové karty událostí, stopky a oficiální návody výrobců, například [postup Googlu pro nalezení, zabezpečení nebo vymazání zařízení](https://support.google.com/android/answer/6160491). **Žádný skutečný telefon se během cvičení nemaže ani nezamyká.**

**Úkoly:**

1. V týmu rozdělte role a sestavte kroky pro prvních 15 minut, první hodinu a následující den po ztrátě odemčeného telefonu.
2. Reagujte na tři nové informace od učitele, například pohyb zařízení, pokus o přihlášení a zjištění, že záloha MFA není dostupná.
3. Odlište vzdálené nalezení, označení jako ztracené/uzamčení a smazání; určete, kdy chránit účty, SIM, data a důkazy.

**Výstupy:** Vyplněný playbook; časová osa rozhodnutí; matice krok–vlastník–důkaz–riziko; seznam předem připravených opatření, která by incident zkrátila; týmová retrospektiva.

<details>

<summary>**🧠 Rozbalit článek: Když incident závodí s majitelem telefonu**</summary>

**Nejdřív omezit dopad, ale nezničit stopy bez rozmyslu**

Odemčený telefon může zpřístupnit e-mail, obnovení hesel, cloudové soubory, komunikaci i jednorázové ověřovací kódy. Jedno zařízení tak někdy funguje jako svazek klíčů k digitálnímu životu. Rychlost je důležitá, ale chaotické změny mohou člověka odříznout od vlastních účtů nebo znemožnit zjistit, co se stalo.

První reakce začíná potvrzením základních faktů: komu zařízení patří, kdy a kde bylo naposledy viděno, zda je zapnuté, zda bylo odemčené a jaké služby obsahuje. Současně se incident hlásí správné roli. U školního či pracovního zařízení nestačí řešit vše soukromě; správce může zneplatnit relace, odvolat spravovaný profil a vyhodnotit oznamovací povinnosti.

**Najít, uzamknout, smazat – tři různé volby**

Služby výrobců mohou zobrazit polohu, přehrát zvuk, označit zařízení jako ztracené, uzamknout je nebo vzdáleně smazat. Dostupnost závisí na předchozím nastavení, připojení a platformě. Zobrazená poloha není povolením jít sám konfrontovat možného pachatele; fyzickou bezpečnost řeší dospělý a podle okolností policie.

Vzdálené smazání je zásadní krok. Může chránit data, ale také ukončit další sledování, zničit lokální důkazy a selhat, dokud je telefon offline. Rozhodnutí má vycházet z citlivosti dat, pravděpodobnosti návratu, správy zařízení, dostupné zálohy a pravidel organizace. Stolní cvičení dovolí tento konflikt prožít bez skutečného mazání.

**Telefon je jen jedna část incidentu**

Útočník může použít aktivní relace, i když nezná hesla. Proto se kontrolují a podle rizika ukončují přihlášené relace, mění kompromitované přístupové údaje a obnovuje vícefaktorové ověřování. Mobilní operátor může blokovat SIM/eSIM, aby omezil zneužití čísla; u finančních aplikací se kontaktuje banka podle jejího oficiálního kanálu.

Pořadí záleží. Když hlavní e-mail obnovuje ostatní účty, jeho ochrana bývá prioritou. Když byl telefon jediným MFA prostředkem, nepromyšlená změna může zablokovat i majitele. Právě proto se před incidentem připravují obnovovací kódy, druhý bezpečný faktor, aktuální kontakty, šifrovaná záloha a zapnutá služba nalezení zařízení.

**Playbook proměňuje paniku v kontrolní seznam**

Playbook není scénář, který předvídá každou sekundu. Přiděluje role, kontakty, rozhodovací body a důkazy. Musí počítat s nejistotou: co víme, co jen předpokládáme a kdo to ověří. Po incidentu následuje obnova a poučení, nikoli hledání viníka mezi lidmi. Cílem retrospektivy je zjistit, která ochrana chyběla a kdo ji do konkrétního termínu doplní.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Scénář a role**

1. Vytvořte tým rolí: majitel zařízení, školní správce, vedoucí incidentu, zapisovatel a pozorovatel. U malé skupiny lze role spojit, ale každé rozhodnutí má jednoho vlastníka.
2. Do [šablony playbooku](./materialy/6-6-playbook.md) zapište výchozí situaci: „V 15:20 zmizel v autobuse školní telefon. V okamžiku ztráty byl pravděpodobně odemčený, obsahuje školní e-mail, cloud a autentizační aplikaci.“
3. Připravte jen modelové názvy účtů. Nikdo se během hry nepřihlašuje do skutečné služby a nevolá operátorovi, bance ani policii.

**Prvních 15 minut**

1. Spusťte stopky na osm minut plánování. Tým musí určit bezpečný kontakt na majitele, ohlášení správci, ověření posledního místa a použití oficiální služby nalezení z důvěryhodného náhradního zařízení.
2. Rozhodněte, zda zařízení označit jako ztracené/uzamknout, jak zobrazit bezpečný kontaktní údaj a kdo posoudí fyzickou polohu.
3. Sepište nejcitlivější aktivní relace. Určete pořadí jejich kontroly či odvolání a způsob, jak si majitel zachová přístup.
4. Zaznamenejte čas každého rozhodnutí a důkaz, který chcete uchovat: čas ztráty, poslední známou polohu, bezpečnostní upozornění a seznam odvolaných relací. Do školního protokolu nekopírujte citlivé snímky.

**Vložené události**

Učitel postupně přečte tři karty. Po každé má tým tři minuty na úpravu plánu.

- `15:32 – mapa ukazuje pohyb telefonu směrem z města.` Tým nesmí vyslat studenta k fyzické konfrontaci; eskaluje podle bezpečnostních pravidel.
- `15:38 – přišlo upozornění na pokus změnit heslo cloudového účtu.` Tým přehodnotí prioritu e-mailu, relací a MFA a zachová údaje o pokusu.
- `15:45 – majitel zjistil, že obnovovací kódy má jen v telefonu.` Tým použije proces obnovy poskytovatele a zapíše chybějící preventivní opatření; nevymýšlí obcházení ověření.

**Rozhodovací matice**

| Krok | Kdy jej udělat | Kdo rozhodne | Přínos | Riziko / nevratnost | Ověření |
|---|---|---|---|---|---|
| přehrát zvuk / najít | | | | | |
| označit jako ztracené | | | | | |
| odvolat relace | | | | | |
| blokovat SIM/eSIM | | | | | |
| vzdáleně smazat | | | | | |

**Další hodina, další den a retrospektiva**

Doplňte kontakty na správce, mobilního operátora a případně banku pouze jako názvy rolí a odkaz na jejich oficiální kanál. Naplánujte obnovení účtů z čistého zařízení, kontrolu přihlášení, změnu skutečně ohrožených tajemství a ověření záloh. Druhý den se posuzuje rozsah úniku, dokumentace a případné povinnosti organizace.

Pozorovatel nakonec uvede jeden krok, který tým provedl včas, jedno místo s nejasným vlastníkem a tři preventivní změny: například zapnutí funkce nalezení, bezpečně uložené obnovovací kódy a oddělený druhý faktor. Žádná simulovaná akce se neprovádí na reálném telefonu.

</details>

## Závěrečný test spravovatelnosti

Vyberte jedno opatření z každého experimentu a doplňte, **kdo je vlastní, jak často se ověřuje a podle jakého důkazu se pozná jeho funkčnost**. Bez této trojice se i dobré bezpečnostní opatření postupně mění v předpoklad. Bezpečná správa není jednorázové „nastavení na maximum“, ale opakovatelný cyklus: zjistit stav, rozhodnout, změnit, ověřit a včas upravit.
