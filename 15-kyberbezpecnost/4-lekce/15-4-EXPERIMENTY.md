<!--
author: Marek Lučný
title: Digitální identita, autentizace a hesla – praktická laboratoř
language: cs
mode: Textbook
comment: Šest praktických experimentů s hesly, Bitwardenem, TOTP, passkeys a kontrolou kompromitovaných údajů.
-->

# Praktická laboratoř: Digitální identita, autentizace a hesla

Heslo je tajná věta, kterou musíme sdílet se službou. TOTP přidává tikající kód. Passkey místo sdíleného tajemství používá dvojici klíčů. Která ochrana odolá úniku databáze? Kterou lze vylákat na falešné stránce? A co se stane, když ztratíme telefon? V této laboratoři si jednotlivé metody opravdu vyzkoušíte a nebudete je hodnotit podle jednoho reklamního čísla.

> **🔐 Neporušitelné pravidlo laboratoře**
>
> Do webových testů nikdy nezadávejte skutečné ani dříve používané heslo. Nesdílejte hlavní heslo správce, TOTP QR/klíč, jednorázový kód, obnovovací kód ani seznam osobních účtů. Používejte veřejné tréninkové hodnoty a fiktivní služby `.example`. Práce s osobním trezorem nebo kontrolou uložených hesel je dobrovolná a výsledek se odevzdává pouze jako anonymní počty.

## Mise a vybavení

| Experiment | Mise | Nástroj | Orientační čas |
|---|---|---|---:|
| 4.1 Laboratoř odhadu hesel | rozebrat skóre kalkulátoru | How Secure Is My Password | 35 min |
| 4.2 Trezor místo paměti | vytvořit tři jedinečné přístupy | Bitwarden | 45 min |
| 4.3 Kód, který tiká | zprovoznit veřejný TOTP účet | Google Authenticator / 2FAS | 40 min |
| 4.4 Přihlášení bez sdíleného tajemství | vytvořit a použít passkey | Passkeys.io | 40 min |
| 4.5 Archeolog hesel | ověřit veřejné testovací řetězce | HIBP Pwned Passwords | 35 min |
| 4.6 Audit vlastního trezoru | najít opakování a kompromitace | Chrome / Edge Password Checkup | 40 min |

## Experiment 4.1: Laboratoř odhadu odolnosti hesel

**Cíl:** Provedením řízeného experimentu zjistit, jak délka, předvídatelné vzory a náhodnost ovlivňují odhad odolnosti, a kriticky vyhodnotit omezení webového kalkulátoru.

**Nástroj:** [How Secure Is My Password](https://www.security.org/how-secure-is-my-password/) a připravené [veřejné testovací řetězce](./materialy/4-1-testovaci-hesla.md). Všechny testované hodnoty jsou úmyslně zveřejněné.

**Úkoly:**

1. Změřte pět připravených řetězců a zapište odhad, hodnocení a zachycené slabiny.
2. Vytvořte tři dvojice, ve kterých měníte jen jednu vlastnost – délku, vzor nebo náhodnost – a porovnejte výsledek.
3. Vysvětlete, proč odhad není zárukou a jak se liší online, offline, slovníkový a credential-stuffing útok.

**Výstupy:** Tabulka nejméně osmi měření, tři formulované hypotézy a jejich vyhodnocení, graf nebo pořadí variant a seznam pěti omezení kalkulátoru.

<details>

<summary>**🧠 Rozbalit článek k tématu: Kolik let trvá „prolomit heslo“? Nesprávná otázka bez scénáře**</summary>

**Obrovské číslo svádí k falešnému klidu**

Kalkulátor může napsat „miliony let“, ale útočník nemusí zkoušet všechny možné kombinace. Lidé volí jména, data, klávesové vzory, citáty a oblíbené náhrady jako `a → @`. Slovníkový útok zkouší pravděpodobné kandidáty dříve než náhodné. Řetězec `Heslo2026!` je delší než `pes7`, ale jeho stavba je útočníkovi velmi dobře známá.

U náhodného hesla z abecedy o `N` znacích a délce `L` existuje teoreticky `N^L` kombinací. Délka je mimořádně účinná, pokud jsou volby skutečně nepředvídatelné. Dlouhá heslová fráze z náhodně vybraných slov může být současně silná a lépe zapamatovatelná. Známá věta z filmu však není náhodná fráze, i kdyby měla třicet znaků.

**Online a offline jsou dva různé závody**

Při online útoku posílá útočník pokusy přihlašovací službě. Ta může omezit rychlost, vyžádat MFA, použít CAPTCHA, upozornit na anomálii nebo účet dočasně zablokovat. Deset pokusů za sekundu může být nereálně vysoký předpoklad.

Při offline útoku získal útočník databázi heslových hashů a zkouší kandidáty na vlastním hardwaru. Služba už rychlost neomezuje. Proto se hesla nemají ukládat jako rychlý prostý SHA-256. Používají se soli a pomalé paměťově náročné funkce, například Argon2id, scrypt nebo přiměřeně nastavený bcrypt.

**Síla nepomůže proti každému útoku**

Phishing heslo nehádá – uživatel je zadá. Keylogger je může zachytit. Credential stuffing zkouší již uniklou dvojici na dalších službách. Nejdelší heslo proto selže, pokud je znovu použito nebo předáno podvodníkovi. Obranu tvoří jedinečnost, správce hesel, MFA odolná phishingu a schopnost rychle odvolat relace.

**Co vlastně kalkulátor ví**

Nástroj vidí pouze zadaný testovací řetězec a svůj model. Nezná způsob uložení služby, rychlost útočníka, rate limiting, MFA ani to, zda bylo heslo v úniku. Různé kalkulátory proto stejné hodnotě přiřadí jiné časy. Číslo je demonstrace citlivosti modelu, ne datum v kalendáři.

Do veřejného webu se navíc skutečné heslo nevkládá ani při tvrzení provozovatele, že je neukládáno. Bezpečný experiment pracuje s hodnotou vytvořenou výhradně pro tuto hodinu a zveřejněnou v pracovním listu.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup měření**</summary>

**Příprava experimentu**

1. Otevřete pracovní list. Nahlas potvrďte, že všechny řetězce jsou veřejné a nikdy se nestanou skutečnými hesly.
2. Připravte tabulku `řetězec – délka – odhad – rozpoznaný vzor – moje vysvětlení – omezení`.
3. Před otevřením nástroje seřaďte pět hodnot od nejslabší po nejsilnější a napište důvod.

**Měření**

1. Otevřete kalkulátor a postupně vložte připravené hodnoty. Po každé zapište výsledek; nepoužívejte automatické vyplňování ani schránku se skutečnými hesly.
2. Sledujte, zda nástroj reaguje na běžné heslo, rok, délku, frázi a náhodný řetězec. Výsledek formulujte jako „nástroj odhaduje“, nikoli „heslo vydrží“.
3. Vytvořte dvojici `ModryVlak` a `ModryVlakModryVlak`. Změnila se délka, ale vzor se opakuje. Porovnejte ji s dlouhou frází z různých náhodných slov.
4. Vytvořte dvojici stejně dlouhých testovacích hodnot: předvídatelnou a generovanou. Nepoužívejte osobní údaje.
5. Vytvořte třetí dvojici, kde k heslu přidáte typické `2026!`. Posuďte, zda změna skóre odpovídá skutečné nepředvídatelnosti.

| Test | Měněná vlastnost | Předpověď | Výsledek nástroje | Co výsledek neříká |
|---|---|---|---|---|
| | | | | |

**Ověření a odevzdání**

Do omezení zahrňte alespoň: neznámou rychlost útoku, neznámý způsob hashování, slovníky, únik hesla, online omezení a phishing. Závěr musí vysvětlit, proč je dlouhé unikátní generované heslo uložené ve správci praktičtější než lidská pravidla typu „velké písmeno, rok a vykřičník“.

</details>

## Experiment 4.2: Trezor místo paměti – Bitwarden v praxi

**Cíl:** Zprovoznit správce hesel pro výhradně fiktivní účty, vygenerovat jedinečná hesla, vyzkoušet uzamčení a automatické přiřazení k doméně a navrhnout bezpečnou obnovu trezoru.

**Nástroj:** Bezplatná verze [Bitwarden](https://bitwarden.com/download/) nebo učitelská demonstrace jeho rozšíření a připravené [fiktivní účty](./materialy/4-2-fiktivni-ucty.csv). Pokud škola nepovoluje registraci, praktická práce proběhne na předem připraveném demonstračním trezoru promítaném učitelem.

**Úkoly:**

1. Vytvořte tři položky fiktivních služeb s různými generovanými hesly o délce alespoň 20 znaků.
2. Nastavte přesné URI, uzamkněte a odemkněte trezor a ověřte, že správce nenabízí údaje na podobné, ale jiné doméně.
3. Nakreslete model trezoru a sestavte plán pro ztrátu zařízení, zapomenuté hlavní heslo a kompromitaci trezoru.

**Výstupy:** Anonymizovaný přehled parametrů tří položek bez hesel, snímek generátoru bez tajemství, diagram trezoru a jednostránkový plán obnovy.

<details>

<summary>**🧠 Rozbalit článek k tématu: Jeden dobře hlídaný trezor místo stejného klíče pod každou rohožkou**</summary>

**Problém není počet hesel, ale lidská paměť**

Každá služba potřebuje jiné heslo, protože únik jedné databáze nesmí otevřít e-mail, cloud a školní systém. Desítky dlouhých náhodných řetězců si člověk nezapamatuje. Bez správce začne hesla opakovat, zkracovat nebo tvořit předvídatelné varianty.

Správce hesel generuje a ukládá jedinečné hodnoty v šifrovaném trezoru. Uživatel si pamatuje hlavní heslo a chrání účet dalším faktorem. Trezor může být synchronizovaný mezi zařízeními; data jsou před odesláním chráněna klíčem odvozeným z hlavního hesla. Konkrétní architekturu je vždy nutné ověřit v dokumentaci daného produktu.

**Hlavní heslo je zvláštní**

Musí být dlouhé, jedinečné a nikde jinde nepoužité. Správce jej neumí běžně „poslat zpět“, protože tím by vznikla cesta také pro útočníka. Proces obnovy je proto kompromisem mezi dostupností a bezpečností. Organizace může používat řízenou obnovu, osobní uživatel bezpečně uložený recovery kód nebo nouzový přístup – podle možností služby.

V této laboratoři se skutečné hlavní heslo nevytváří ani neodevzdává. Pokud vznikne cvičný účet, jeho heslo je jen pro daný trezor a student je nesmí ukázat učiteli. Hodnotí se proces, ne znalost tajemství.

**Automatické vyplnění může kontrolovat doménu**

Uživatel může přehlédnout rozdíl mezi `fotocloud.example` a `fotoc1oud.example`. Správce porovnává uložené URI s aktuálním webem a na cizí doméně položku běžně nenabídne. Tím pomáhá proti phishingu. Ochrana závisí na režimu porovnávání URI a správném uložení položky; bezmyšlenkovité kopírování hesla ji obchází.

**Centralizace je výhoda i riziko**

Kompromitovaný odemčený trezor má vysoký dopad. Proto se používá automatické zamykání, aktualizace, MFA, důvěryhodná zařízení a kontrola aktivních relací. Export trezoru může vytvořit nechráněnou kopii, a proto se v laboratoři neprovádí.

Správce hesel neřeší všechno: malware může číst obsah na odemčeném zařízení, podvodník může vylákat obnovovací kód a chybně zadaná doména může vést k nesprávnému vyplnění. Přesto dramaticky zlepšuje jedinečnost, délku a odolnost proti credential stuffingu.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v Bitwardenu**</summary>

**Varianta školy**

1. Učitel předem určí, zda studenti mohou vytvořit bezplatný cvičný účet se školní adresou. Registrace není povinná; při zákazu pracuje jeden demonstrační účet na učitelském zařízení a studenti vyplňují protokol.
2. Rozšíření instalujte pouze přes oficiální stránku Bitwarden, která odkazuje do obchodu konkrétního prohlížeče. Ověřte vydavatele; neinstalujte podobně pojmenované doplňky.
3. Do trezoru nikdy nevkládejte skutečné školní ani osobní údaje. Použijte jen tři služby `.example` z CSV.

**Vytvoření položek**

1. Otevřete generátor. Pro FotoCloud nastavte alespoň 20 náhodných znaků se všemi běžnými skupinami. Pro druhou službu vytvořte jiný 24znakový řetězec a pro třetí náhodnou frázi s nejméně pěti slovy.
2. Hesla nezapisujte do protokolu ani nesnímejte. Zaznamenejte pouze délku, typ a zapnuté skupiny.
3. Vytvořte položku Login, doplňte fiktivní jméno a přesnou URI. Zkontrolujte režim shody URI, aby jiná doména nebyla považována za stejný web.
4. Zopakujte pro všechny tři účty a ověřte, že žádné dvě hodnoty nejsou stejné.

**Pozorování chování**

1. Ručně otevřete fiktivní doménu z textu – nebude existovat, ale rozšíření může ukázat počet odpovídajících položek. Nezkoušejte web vytvářet ani obcházet `.example`.
2. Změňte v testovací položce URI na podobný tvar a sledujte, jak nastavení shody ovlivní nabídku. Potom vraťte správnou hodnotu.
3. Zamkněte trezor a zkuste otevřít položku. Zaznamenejte rozdíl mezi uzamčeným trezorem a odhlášeným účtem.
4. Najděte nastavení automatického zamykání a navrhněte přiměřený čas pro školní notebook a osobní telefon. Bez pokynu neměňte globální nastavení učitelského účtu.

**Plán incidentu a úklid**

1. Pro ztrátu zařízení zahrňte odvolání relace, kontrolu přístupů a vzdálené zabezpečení zařízení.
2. Pro kompromitaci hlavního hesla zahrňte změnu z čistého zařízení, odhlášení relací, kontrolu trezoru a prioritní rotaci citlivých účtů.
3. Fiktivní položky po kontrole smažte. Cvičný účet může student ponechat jen podle pravidel školy; skutečná hesla se do něj v rámci hodiny nepřenášejí.

**Ověření a odevzdání**

Odevzdejte tabulku parametrů, nikoli tajemství. Diagram musí ukázat zařízení, odemčený trezor, šifrovaná data, synchronizační službu, cílovou doménu, MFA a obnovu. Vysvětlete, jak jedinečná hesla omezují dopad úniku jedné služby.

</details>

## Experiment 4.3: Kód, který tiká – TOTP bez osobního účtu

**Cíl:** Přidat do autentizační aplikace veřejný tréninkový TOTP klíč, pozorovat změnu kódu v čase a pochopit roli sdíleného tajemství, hodin a phishingu v reálném čase.

**Nástroj:** Bezplatný **Google Authenticator**, **2FAS** nebo jiná učitelem schválená TOTP aplikace, [návod Google Authenticator](https://support.google.com/accounts/answer/1066447) a [veřejný tréninkový účet](./materialy/4-3-totp-trenink.md). Aplikaci lze použít bez propojení s osobním účtem.

**Úkoly:**

1. Zadejte veřejný Base32 klíč ručně do dvou zařízení a porovnejte tři po sobě jdoucí kódy.
2. Pozorujte přechod časového okna a vysvětlete, proč malý rozdíl hodin může ovlivnit přijetí.
3. Modelujte odcizení jednoho kódu a únik celého aktivačního klíče; porovnejte dobu a rozsah rizika.

**Výstupy:** Tabulka tří časových oken bez použití osobního tajemství, diagram TOTP, srovnání tří typů úniku a pravidla pro QR, záložní kódy a obnovu.

<details>

<summary>**🧠 Rozbalit článek k tématu: Dvě zařízení, stejné tajemství a společný rytmus hodin**</summary>

**Kód nepřichází ze serveru**

TOTP – Time-based One-Time Password – vytváří krátký kód ze sdíleného tajemství a času. Server i aplikace mají stejný základ a nezávisle počítají výsledek pro obvykle třicetisekundové okno. Telefon proto dokáže kód generovat bez internetu a mobilního signálu.

Zjednodušeně jde o `tajemství + časový čítač → HMAC → zkrácený kód`. Krátký šestimístný výstup má omezený počet možností, ale server současně vyžaduje heslo, omezuje pokusy a kód rychle expiruje. Aby toleroval mírně rozdílné hodiny a dobu opisování, může přijmout sousední okno.

**QR kód je kopie budoucí továrny na kódy**

Při aktivaci služby zobrazí QR kód nebo textový setup key. Obsahuje sdílené tajemství. Kdo si jej vyfotografuje, nevlastní jen aktuálních šest číslic – může vytvářet budoucí kódy, dokud služba tajemství nezmění. Proto QR nepatří do snímku obrazovky, prezentace ani protokolu.

Tréninkový klíč v této úloze je záměrně veřejný a k žádnému účtu nevede. Právě proto je bezpečné, když všem vytváří stejný kód. V reálném světě by taková shoda dokazovala kompromitaci.

**Jednorázový neznamená nepřenosný**

Falešná stránka může vylákat heslo i aktuální TOTP a okamžitě je předat pravé službě. Kód ještě několik sekund platí. TOTP tedy výborně omezuje dopad samotného úniku hesla, ale není plně odolný proti phishing proxy v reálném čase.

Bezpečnostní klíče a passkeys kryptograficky vážou operaci na správnou doménu a této třídě útoku odolávají lépe. TOTP je přesto významná a dostupná vrstva, zejména pokud alternativa je pouze heslo.

**Obnova je druhý vchod**

Ztracený telefon nesmí znamenat trvalou ztrátu účtu. Služba nabízí záložní kódy, druhý autentizátor nebo proces podpory. Záložní kódy jsou tajemství, každý se používá jednou a mají být uloženy odděleně. Slabá obnova může obejít jinak silnou autentizaci.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup TOTP experimentu**</summary>

**Příprava**

1. Pracujte ve dvojici. Každý použije učitelem schválenou aplikaci, případně dvě demonstrační zařízení poskytne škola.
2. Google Authenticator lze podle oficiálního návodu použít i bez přihlášení k účtu. Neměňte ani nemažte své existující kódy; nový záznam musí být jasně označen `PV-TRENING`.
3. Otevřete materiál a ověřte, že klíč je označen jako veřejný a nepoužitelný pro skutečnou službu.

**Přidání klíče**

1. V aplikaci zvolte přidání pomocí setup key / ručního zadání, nikoli skenování náhodného QR.
2. Zadejte název `PV-TRENING`, Base32 klíč `JBSWY3DPEHPK3PXP` a časový typ TOTP.
3. Stejný postup provede druhé zařízení. Kód nikam neposílejte; porovnejte jej pouze osobně.

**Měření tří oken**

1. Počkejte na začátek nového časového okna. Zapište čas odečtu, zbývající sekundy a pouze pro tuto veřejnou ukázku oba kódy.
2. Pozorujte okamžik přechodu. Jedno zařízení odečte kód těsně před a druhé těsně po změně. Vysvětlete dočasnou neshodu.
3. Zopakujte pro tři celá okna. Pokud se kódy při stejném okně neshodují, zkontrolujte přesný klíč a automatický čas systému; nevynucujte změnu hodin školního zařízení.

**Model tří kompromitací**

1. Útočník viděl jeden kód po jeho expiraci – jak dlouho je užitečný?
2. Útočník zachytil kód a heslo deset sekund před expirací – může je okamžitě přeposlat?
3. Útočník získal aktivační klíč – kolik budoucích kódů vytvoří a jak se incident napraví?

**Úklid a odevzdání**

Odstraňte pouze záznam `PV-TRENING` a ukažte spolužákovi, že ostatní položky zůstaly. Odevzdejte tabulku a diagram bez osobních QR či kódů. Závěr musí rozlišit TOTP tajemství, aktuální kód a jednorázový záložní kód.

</details>

## Experiment 4.4: Passkey – přihlášení bez sdíleného hesla

**Cíl:** Vytvořit demonstrační passkey, použít jej při opakovaném a případně mezizařízení přihlášení a vysvětlit, proč vazba na doménu omezuje phishing.

**Nástroj:** Bezplatná demonstrační stránka [Passkeys.io](https://www.passkeys.io/) a moderní zařízení s Windows Hello, PINem, biometrikou nebo telefonem. Stránka výslovně dovoluje fiktivní e-mail; alternativou je společná učitelská ukázka.

**Úkoly:**

1. Vytvořte passkey pro fiktivní demonstrační identitu a přihlaste se po odhlášení bez hesla.
2. Pozorujte, co dělá web, prohlížeč, operační systém a místní autentizátor; nakreslete výměnu výzvy a podpisu.
3. Porovnejte passkey s heslem a TOTP při úniku serverové databáze, phishingu, ztrátě zařízení a obnově.

**Výstupy:** Dva časové záznamy registrace/přihlášení, sekvenční diagram, srovnávací matice a bezpečný postup odstranění demonstračního účtu nebo credentialu.

<details>

<summary>**🧠 Rozbalit článek k tématu: Server dostane veřejný zámek, soukromý klíč zůstává u vás**</summary>

**Registrace vytváří dvojici, ne nové heslo**

Při registraci passkey autentizátor vytvoří veřejný a soukromý klíč. Služba uloží veřejný klíč a identifikátor credentialu. Soukromá část zůstává chráněna zařízením nebo správcem passkeys a může být podle ekosystému synchronizována v šifrované podobě.

Při přihlášení server pošle čerstvou náhodnou výzvu. Autentizátor ji po souhlasu uživatele podepíše a server podpis ověří. Zachycený podpis nelze jednoduše znovu použít pro jinou výzvu.

**Biometrika se neposílá webu**

Otisk, obličej nebo PIN zpravidla místně odemkne použití klíče. Web dostane výsledek kryptografické operace, ne fotografii otisku. PIN zařízení není „heslo k webu“ a služba jej neukládá.

**Doména je součást bezpečnostního obřadu**

WebAuthn pracuje s relying party a originem. Credential vytvořený pro `passkeys.io` nelze nabídnout podvodné doméně `passkeys-login.example` jako přihlašovací tajemství pro původní službu. Uživatel nemá co opsat do formuláře. To výrazně omezuje klasický phishing a proxy útoky, které přeposílají heslo a TOTP.

Výhoda neznamená nesmrtelnost. Malware na odemčeném zařízení může zneužít relaci, útočník může ovládnout proces obnovy a ztráta všech autentizátorů ohrozí dostupnost. Synchronizační účet se stává významnou částí bezpečnostního modelu.

**Co unikne ze serveru**

Databáze veřejných klíčů sama neobsahuje tajemství použitelné k vytvoření podpisu. To odstraňuje velkou třídu hromadných útoků na heslové hashe. Server však stále chrání účty, autorizaci, relace a osobní data.

Passkey je tedy lepší stavební prvek autentizace, nikoli náhrada celého bezpečnostního procesu. Uživatel potřebuje vidět, pro jakou službu credential vytváří, a mít bezpečnou cestu pro přidání nového zařízení a zrušení ztraceného.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup na Passkeys.io**</summary>

**Příprava a souhlas**

1. Experiment provádějte na vlastním zařízení nebo na učitelském profilu určeném pro demonstraci. Na sdíleném veřejném počítači nevytvářejte osobní passkey.
2. Připravte fiktivní adresu ve tvaru `student-trenink@example.com`. Doména `.example` nepřijímá poštu; ztracený demonstrační účet tedy nepůjde obnovit e-mailem.
3. Změřte, kolik kroků podle vás registrace zabere, a napište, jaké tajemství očekáváte na serveru.

**Registrace a přihlášení**

1. Na Passkeys.io otevřete demo a zvolte vytvoření účtu. Zadejte fiktivní adresu.
2. Systémová výzva nabídne uložení passkey. Přečtěte doménu a vybraný autentizátor; nepotvrzujte výzvu, pokud ukazuje jinou službu.
3. Operaci odemkněte PINem zařízení nebo povolenou místní metodou. PIN nezapisujte ani neukazujte.
4. Odhlaste se a přihlaste pomocí passkey. Změřte počet kroků a čas od zahájení po dokončení.
5. Pokud učitel povolí mezizařízení scénář, na druhém zařízení vyberte passkey z nearby device a použijte QR tok. Obě zařízení mohou vyžadovat Bluetooth; QR kód nefotografujte.

**Analytický diagram**

Nakreslete dvě sekvence:

```text
registrace: zařízení vytvoří klíče → server dostane veřejný klíč
přihlášení: serverová výzva → místní souhlas → podpis → ověření
```

Ke každé části doplňte: veřejné, soukromé, dočasné a vázané na doménu.

**Úklid**

Použijte možnost demo účtu pro odstranění, pokud je dostupná, a podle pokynu učitele odstraňte credential ze správce passkeys zařízení. Nemažte jiné uložené passkeys. Pokud si nejste jistí, zastavte se a požádejte správce.

**Ověření a odevzdání**

Odevzdejte časy, počet kroků a diagram; nikoli snímek PINu nebo seznam osobních passkeys. V matici porovnejte `serverový únik`, `falešná doména`, `ztráta zařízení`, `obnova` a `odcizená relace` pro heslo, heslo+TOTP a passkey.

</details>

## Experiment 4.5: Archeolog hesel v Pwned Passwords

**Cíl:** Ověřit pouze veřejné testovací řetězce v databázi známých kompromitovaných hesel, interpretovat počet výskytů a pochopit k-anonymní vyhledávání bez odhalení celého hashe.

**Nástroj:** [Have I Been Pwned – Pwned Passwords](https://haveibeenpwned.com/Passwords) a veřejné hodnoty z pracovního listu. Skutečná hesla jsou zakázána.

**Úkoly:**

1. Ověřte tři připravené řetězce a porovnejte počet zaznamenaných výskytů.
2. Pro jeden řetězec vypočítejte SHA-1 a modelově ukažte rozdělení na prvních pět znaků a zbytek používané k-anonymním API.
3. Navrhněte reakci na kompromitované heslo podle toho, zda bylo unikátní, znovu použité nebo chránilo e-mail.

**Výstupy:** Tabulka tří bezpečných dotazů, schéma k-anonymity, vysvětlení významu i omezení počtu výskytů a prioritizovaný reakční plán.

<details>

<summary>**🧠 Rozbalit článek k tématu: Heslo může být prozrazené, i když je matematicky dlouhé**</summary>

**Únik mění pravidla hry**

Pokud se heslo objevilo v uniklých datech, útočník je nemusí hádat. Zařadí je na začátek slovníku a automaticky zkouší u dalších účtů. Síla odhadovaná kombinatorikou přestává být hlavní otázkou. Rozhoduje, zda je hodnota stále používána a zda byla opakována.

Pwned Passwords obsahuje hashe hesel nalezených v datových únicích a počet jejich výskytů. Výsledek „nalezeno“ neříká, u kterého vašeho účtu se heslo objevilo ani kdo je použil. Výsledek „nenalezeno“ zase nedokazuje, že je tajné nebo silné – databáze neobsahuje každý únik a slabou dosud nezaznamenanou variantu lze uhádnout.

**Jak hledat bez poslání celého hashe**

API používá model k-anonymity. Klient vypočítá SHA-1 hesla a odešle pouze prvních pět hexadecimálních znaků. Server vrátí mnoho koncovek hashů se stejným prefixem a klient porovná zbytek lokálně. Server tedy neobdrží celý hash ani původní heslo z tohoto dotazu.

SHA-1 zde není doporučení pro ukládání hesel. Slouží jako index nad již známými hodnotami. Databáze služby má jiný účel než autentizační databáze, která musí použít sůl a pomalou KDF.

**Frekvence je signál, ne skóre člověka**

Miliony výskytů ukazují extrémně běžné heslo. Jeden výskyt stále znamená, že řetězec je v útočnických slovnících. Správná reakce není přidat na konec vykřičník, ale vytvořit zcela nové jedinečné heslo správcem, změnit je na každé službě, kde bylo opakováno, zapnout MFA a zkontrolovat relace.

Nejvyšší prioritu má e-mail a účty umožňující obnovu dalších služeb. Pokud existuje podezření na malware, hesla se mění z důvěryhodného čistého zařízení až po omezení příčiny.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup Pwned Passwords**</summary>

**Bezpečné dotazy**

1. Vyberte tři hodnoty z veřejného pracovního listu, například `123456`, `Heslo2026!` a náhodný laboratorní řetězec. Žádnou z nich nikdy nepoužijte jako heslo.
2. Otevřete Pwned Passwords a postupně je zadejte. Zapište pouze stav nalezeno/nenalezeno a počet výskytů, pokud jej služba zobrazí.
3. Předpovězte výsledek před každým dotazem a vysvětlete případné překvapení.

**Model k-anonymity**

1. V CyberChef nebo PowerShellu vypočítejte SHA-1 pouze pro veřejný `123456`.
2. Rozdělte hash na prefix prvních pěti hex znaků a zbývající suffix. Do diagramu napište, že klient odesílá prefix a lokálně hledá suffix ve vrácené množině.
3. Nevytvářejte vlastní API skript a neposílejte skutečné hodnoty. Cílem je princip.

| Testovací hodnota | Předpověď | Výsledek | Co lze vyvodit | Co nelze vyvodit |
|---|---|---|---|---|
| | | | | |

**Reakční scénáře**

1. Heslo bylo jen u zrušeného fóra a nikde jinde: zdokumentovat, nepoužívat znovu.
2. Stejná hodnota je u e-shopu a e-mailu: nejdříve zabezpečit e-mail, změnit všechny opakované varianty, odvolat relace a zapnout MFA.
3. Počítač může obsahovat infostealer: nejprve incident řešit a hesla měnit z čistého zařízení.

**Ověření a odevzdání**

Odevzdejte tabulku a diagram. Připojte omezení: počet výskytů není počet napadených účtů konkrétního studenta a nenalezení v databázi není certifikát bezpečnosti.

</details>

## Experiment 4.6: Audit znovupoužitých a kompromitovaných hesel v prohlížeči

**Cíl:** Bezpečně spustit vestavěnou kontrolu uložených přístupů, anonymně vyhodnotit kompromitované, opakované a slabé položky a vytvořit plán jejich nápravy.

**Nástroj:** **Google Password Manager – Checkup** v Chrome nebo **Password Monitor / Password security check** v Microsoft Edge. Použít lze pouze vlastní profil; pro ostatní je připravena učitelská demonstrace.

**Úkoly:**

1. Spusťte kontrolu vlastního trezoru nebo analyzujte anonymizovanou učitelskou ukázku.
2. Zapište pouze počty kompromitovaných, znovupoužitých a slabých hesel a vytvořte prioritní pořadí bez odhalení služeb.
3. Pro první tři priority sestavte přesný bezpečný postup změny, aktualizace trezoru, MFA a odvolání relací.

**Výstupy:** Anonymní souhrn kategorií, matice priority a dopadu, plán nápravy a vysvětlení, co kontrola dokládá a co ne.

<details>

<summary>**🧠 Rozbalit článek k tématu: Jedna kopie klíče může otevřít celé digitální město**</summary>

**Credential stuffing využívá naše opakování**

Útočník získá dvojici e-mail–heslo z jedné služby a automaticky ji zkouší na dalších. Nemusí prolomit kryptografii banky; spoléhá na to, že uživatel použil stejný klíč. Prohlížeč nebo správce proto dokáže označit položky se stejnou hodnotou.

Kompromitované heslo odpovídá známým uniklým údajům. Slabé heslo je podle modelu snadno odhadnutelné. Kategorie se mohou překrývat, ale vyžadují jinou pozornost. I silné heslo nalezené v úniku se musí změnit. Slabé unikátní heslo se má zlepšit, i když zatím v žádné databázi není.

**Priorita není jen počet červených položek**

E-mail umožňuje obnovovat další účty, cloud obsahuje data a finanční služba může mít okamžitý dopad. Prioritu zvyšuje opakované heslo, chybějící MFA, podezřelá relace a význam účtu. Mrtvý účet na zrušeném fóru není stejně naléhavý jako aktivní e-mail.

Správný postup pro aktivní kompromitovaný účet zahrnuje otevření služby z vlastní záložky, vytvoření jedinečného hesla, aktualizaci trezoru, zapnutí vhodné MFA, kontrolu obnovovacích údajů a ukončení neznámých relací. Změna jen jedné kopie opakovaného hesla problém neuzavírá.

**Kontrola chrání soukromí jen při správném použití**

Chrome a Edge popisují postupy, které porovnávají uložené údaje s databázemi známých úniků, aniž by službě posílaly běžně čitelný seznam hesel. Přesný mechanismus a nastavení se vyvíjejí, proto je vhodné číst aktuální oficiální dokumentaci.

Obrazovka výsledků je vysoce citlivá: může odhalit účty, domény a bezpečnostní problémy. Ve třídě se nepromítá, nefotografuje a neodevzdává. Student hlásí pouze agregované počty nebo pracuje s modelovou ukázkou.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup auditu**</summary>

**Volba soukromé varianty**

1. Student se sám rozhodne, zda použije vlastní profil. Učitel nesmí požadovat otevření seznamu účtů ani ověření identity před třídou.
2. V Chrome otevřete nabídku → Hesla a automatické vyplňování → Google Password Manager → Checkup. V Edge použijte Nastavení → Hesla a automatické vyplňování → Microsoft Password Manager → Password security check. Názvy se mohou změnit; pomůže oficiální dokumentace pro [Chrome](https://support.google.com/chrome/answer/10311524) nebo [Edge](https://support.microsoft.com/edge/protect-your-online-accounts-using-password-monitor).
3. Pokud zařízení vyžádá místní ověření, proveďte je tak, aby nikdo neviděl PIN ani biometrický údaj.

**Anonymní záznam**

1. Zapište pouze počty ve třech kategoriích. Názvy služeb nahraďte `ÚČET-A`, `ÚČET-B` a podobně.
2. Jestliže žádná hesla uložena nejsou, je výsledek platný; proveďte prioritizaci na učitelském modelu.
3. Pro každou anonymní položku ohodnoťte význam účtu, opakování, MFA, možnost obnovy a známky neznámé aktivity.

| Anonymní účet | Kategorie | Význam 1–3 | Opakování | MFA | Priorita a první krok |
|---|---|---:|---|---|---|
| | | | | | |

**Náprava**

1. Během hodiny nemusíte měnit skutečná hesla. Sepište bezpečný plán a změny proveďte soukromě z důvěryhodného zařízení.
2. Začněte e-mailem a účty obnovujícími další služby. Použijte generátor správce a nikdy jen nepřidávejte rok.
3. U opakované hodnoty vyhledejte všechny kopie. Každá dostane jinou hodnotu.
4. Zkontrolujte aktivní relace, obnovovací adresy a MFA. Při podezření na malware nejdříve řešte zařízení.

**Ověření a odevzdání**

Odevzdejte pouze anonymní počty a plán. Nikdy snímek seznamu. Vysvětlete rozdíl mezi zprávou „tato uložená dvojice odpovídá známému úniku“ a tvrzením „prohlížeč způsobil únik“.

</details>

## Závěrečná reflexe

**Která strategie nejlépe omezuje dopad úniku jedné služby i phishingu?**

<!-- data-randomize="true" -->
[( )] Jedno mimořádně složité heslo použité všude.
[( )] Heslo s každoroční změnou posledního čísla.
[(X)] Jedinečné generované údaje ve správci a tam, kde je to možné, passkey nebo phishingu odolná MFA.
[( )] Uložení TOTP QR kódu do stejného veřejného dokumentu jako heslo.

Vyberte jednu technologii a dokončete větu: „Chrání dobře proti…, ale sama neřeší…“
