## Snímek 5.1

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Data v klidu, při přenosu a při zpracování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 5.2

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Symetrické a asymetrické šifrování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 5.3

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Hash není šifrování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 5.4

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**TLS a end-to-end šifrování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 5.5

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Digitální podpis, certifikát a elektronický podpis**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````
