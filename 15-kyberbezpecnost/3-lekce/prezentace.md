## Snímek 3.1

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Příznak není důkaz**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 3.2

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Obrana do hloubky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

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

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 3.3

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Antivirus, antimalware a EDR**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Klasický antivirus porovnával soubory především s databází známých **signatur**. Tento princip stále existuje, ale moderní ochrana používá více technik.

**Signaturní detekce** hledá známé vzory. Je rychlá a přesná u již známých hrozeb, ale sama nestačí na nový nebo pozměněný malware.

**Heuristika** hledá podezřelé vlastnosti programu.

**Behaviorální analýza** sleduje chování. Podezřelý může být například proces, který začne hromadně měnit dokumenty, vypne bezpečnostní nástroj nebo se snaží spouštět kód neobvyklým způsobem.

**Reputační služby** porovnávají soubor, adresu nebo certifikát s informacemi získanými z velkého množství zařízení.

**Sandbox** spustí podezřelý obsah v izolovaném prostředí a sleduje, jak se chová.

V organizacích se používá také **EDR — Endpoint Detection and Response**. EDR neslouží pouze k blokování známého malwaru; shromažďuje informace o aktivitě koncových zařízení a pomáhá analyzovat a omezovat incident.

Antivirus proto není „magický filtr“. Je jednou z vrstev ochrany a může mít falešně pozitivní i falešně negativní výsledky.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 3.4

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Zálohy jako bezpečnostní opatření**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Záloha není pouze ochrana před poruchou disku. Je zásadní také při ransomwaru, chybě správce nebo nechtěném smazání.

Známé pravidlo **3–2–1** doporučuje mít alespoň:

- tři kopie dat,
- na dvou různých typech úložiště,
- jednu kopii oddělenou od hlavního systému.

Dnes je důležitá také otázka, zda útočník může zálohu smazat. Organizace proto používají **offline**, oddělené nebo **immutable** zálohy, které nelze běžným účtem jednoduše přepsat.

Nejdůležitější kontrolní otázka není „Máme zálohu?“, ale:

> Dokážeme z ní skutečně obnovit systém a víme, jak dlouho obnova potrvá?

Záloha, kterou nikdo nikdy nezkusil obnovit, je pouze předpoklad.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````

## Snímek 3.5

````text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Co dělat při podezření na incident**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

U domácího zařízení i v organizaci je důležité nejednat zbrkle.

Pokud zařízení začne například hromadně šifrovat soubory nebo existuje silné podezření na aktivní útok, je vhodné **omezit jeho síťové spojení**, aby se útok dále nešířil. V organizaci je současně nutné co nejrychleji kontaktovat správce nebo bezpečnostní tým.

Není vhodné bez rozmyslu mazat soubory a „uklízet stopy“. Logy a další informace mohou být důležité pro zjištění, co se stalo.

Pokud byly kompromitovány přihlašovací údaje, heslo se mění z **důvěryhodného čistého zařízení**, přičemž se ukončí aktivní relace a zkontrolují další způsoby obnovy účtu.

Obecný postup má několik fází:

**detekce → omezení dopadu → analýza → odstranění příčiny → obnova → poučení**

Cílem není pouze „zprovoznit počítač“, ale také pochopit, jak útočník získal přístup a zda v systému nezůstal další.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
````
