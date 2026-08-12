## Snímek 4.1

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Identita, autentizace a autorizace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 4.2

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Autentizační faktory a MFA**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 4.3

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Heslo: délka, jedinečnost a správce hesel**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Starší bezpečnostní poučky často požadovaly například „osm znaků, velké písmeno, malé písmeno, číslici, symbol a změnu každých 30 dní“. Takové pravidlo může vést k předvídatelným heslům typu `Heslo2026!`.

Moderní doporučení klade větší důraz na:

**délku** — dlouhé heslo nebo heslová fráze má větší prostor možných kombinací;

**jedinečnost** — každá služba má mít jiné heslo;

**nepředvídatelnost** — nepoužívat běžné fráze a známá uniklá hesla;

**správce hesel** — umožňuje generovat a ukládat dlouhá náhodná hesla.

Uživatel by si proto neměl pamatovat desítky variant jednoho hesla. Mnohem bezpečnější je chránit kvalitně správce hesel a pro jednotlivé služby používat unikátní generovaná hesla.

Automatická pravidelná změna hesla bez důvodu už není obecně považována za nejlepší postup. Heslo je nutné změnit zejména tehdy, když existuje podezření nebo důkaz, že bylo kompromitováno.

Důležitá je také **obnova účtu**. Pokud služba umožní obejít silné přihlášení jednoduchou otázkou „Jak se jmenoval váš první pes?“, může být právě obnova nejslabším článkem systému.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 4.4

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak se na hesla útočí**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Brute force** zkouší velké množství možných hesel.

**Slovníkový útok** používá seznamy častých hesel, slov a typických variant.

**Password spraying** zkouší malé množství velmi častých hesel proti mnoha účtům, aby se vyhnul rychlému zablokování jednoho konkrétního účtu.

**Credential stuffing** používá dvojice e-mail–heslo uniklé z jedné služby a automaticky je zkouší na jiných službách. Právě proto je opakované použití hesla tak nebezpečné.

**Phishing** heslo neuhodne — uživatel jej útočníkovi sám zadá.

**Keylogger** zachycuje stisky kláves nebo jiným způsobem sbírá zadávané informace.

Na straně služby se proti hádání hesel používá například **rate limiting**, tedy omezení rychlosti neúspěšných pokusů, a blokování známých kompromitovaných hesel.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 4.5

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Passkeys: přihlášení bez sdíleného hesla**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Passkey** používá asymetrickou kryptografii. Zařízení vytvoří dvojici klíčů. Veřejný klíč dostane služba, soukromý klíč zůstává v autentizačním prostředí uživatele.

Při přihlášení server pošle výzvu a zařízení ji podepíše soukromým klíčem. Server podpis ověří veřejným klíčem.

Důležitá výhoda spočívá v tom, že server neuchovává tajemství, které by se dalo stejně jako databáze hesel použít k přihlášení. Passkey je navíc vázán na konkrétní doménu, což výrazně omezuje klasický phishing.

Uživatel může passkey odemknout například biometrikou nebo PINem zařízení. Biometrický údaj se přitom typicky neposílá webové službě; slouží místně k povolení použití uloženého klíče.

Passkeys nejsou řešením všech problémů. Stále je nutné chránit zařízení, účet pro synchronizaci klíčů a proces obnovy. Dobře navržená veřejnoklíčová autentizace ale odstraňuje několik slabin klasických hesel najednou.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````
