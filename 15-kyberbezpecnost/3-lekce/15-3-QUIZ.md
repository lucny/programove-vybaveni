<!--
title: Rozpoznání napadení a vícevrstvá obrana – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč samotné vysoké vytížení CPU nedokazuje malware?**

<!-- data-randomize="true" -->
[(X)] Může je způsobit aktualizace, renderování nebo legitimní program.
[( )] Malware procesor nikdy nezatěžuje.
[( )] Vytížení CPU vždy znamená poruchu disku.
[( )] Útočník se musí vždy projevit novou příponou souborů.

---

**2. Proč jsou při diagnostice důležité logy?**

<!-- data-randomize="true" -->
[(X)] Propojují záznamy o přihlášení, procesech, síti a změnách systému.
[( )] Automaticky odstraní každý škodlivý proces.
[( )] Nahrazují zálohy a obnovu systému.
[( )] Dokazují malware jediným záznamem bez kontextu.

---

**3. Co znamená obrana do hloubky?**

<!-- data-randomize="true" -->
[(X)] Více nezávislých vrstev, které se vzájemně doplňují.
[( )] Jediný dokonale nastavený bezpečnostní produkt.
[( )] Úplné odpojení všech zařízení od sítě.
[( )] Pouze pravidelné školení uživatelů.

---

**4. Co říká princip nejmenších oprávnění?**

<!-- data-randomize="true" -->
[(X)] Účet a program dostanou jen práva nutná pro svou činnost.
[( )] Každý uživatel pracuje jako správce.
[( )] Oprávnění se přidělují podle délky hesla.
[( )] Všechny části sítě mají stejný přístup.

---

**5. Jaký je hlavní účel segmentace sítě?**

<!-- data-randomize="true" -->
[(X)] Oddělit části infrastruktury a omezit šíření kompromitace.
[( )] Nahradit autentizaci síťovým kabelem.
[( )] Uložit všechny zálohy do jedné sítě.
[( )] Zrychlit každý přenos bez bezpečnostních pravidel.

---

**6. Jaký je rozdíl mezi signaturní a behaviorální detekcí?**

<!-- data-randomize="true" -->
[(X)] Signatura hledá známý vzor, behaviorální analýza podezřelé chování.
[( )] Behaviorální analýza pracuje jen se známými hashi.
[( )] Signatura sleduje uživatele, behaviorální analýza aktualizace.
[( )] Jde o dvě označení sandboxu.

---

**7. Co dělá sandbox při analýze podezřelého obsahu?**

<!-- data-randomize="true" -->
[(X)] Spustí jej izolovaně a sleduje jeho chování.
[( )] Okamžitě jej zveřejní v produkční síti.
[( )] Porovná pouze název souboru s příponou.
[( )] Uloží jej jako neměnnou zálohu.

---

**8. Jakou roli má EDR?**

<!-- data-randomize="true" -->
[(X)] Sbírá aktivitu koncových zařízení a podporuje detekci a reakci.
[( )] Slouží jen jako seznam známých virových signatur.
[( )] Nahrazuje všechny síťové i organizační vrstvy.
[( )] Provádí pouze obnovu dat ze zálohy.

---

**9. Co znamená pravidlo záloh 3–2–1?**

<!-- data-randomize="true" -->
[(X)] Tři kopie, dva typy úložiště a jedna oddělená kopie.
[( )] Tři hesla, dvě MFA aplikace a jeden správce.
[( )] Tři servery, dvě sítě a jeden firewall.
[( )] Tři obnovy každý den po dobu dvou týdnů.

---

**10. Které kroky patří do reakce na aktivní incident?**

<!-- data-randomize="true" -->
[[X]] omezit další šíření
[[X]] kontaktovat správce nebo bezpečnostní tým
[[X]] uchovat důležité stopy
[[X]] analyzovat příčinu
[[X]] obnovit a poučit se
[[ ]] bez rozmyslu smazat všechny logy
[[ ]] změnit heslo na napadeném zařízení


# 2. Interaktivní shrnutí kapitoly

## Signál potřebuje kontext

Zpomalení, vysoké vytížení, nečekaná komunikace, nové procesy nebo hromadné změny souborů jsou podezřelé, ale jeden příznak není důkaz. Aktualizace nebo legitimní náročná úloha mohou vypadat podobně. Diagnostika proto hledá [[ (více nezávislých souvisejících signálů) | jediný nápadný proces bez dalšího ověření | pouze změnu přípony souboru ]].

[[Logy]] zachycují přihlášení, procesy, síťovou komunikaci a změny. Bez dostatečných záznamů je těžké určit časovou osu a rozsah incidentu.

## Vrstvy omezují selhání

Obrana do hloubky kombinuje chování uživatele, MFA, aktualizace, omezená oprávnění, ochranu zařízení, firewall, segmentaci, monitoring a zálohy. Když jedna vrstva selže, další může útok zastavit nebo zmenšit dopad.

Princip [[least privilege]] přiděluje jen nutná práva. Firewall filtruje síťovou komunikaci, ale [[ (nenahrazuje aktualizace, autentizaci ani kontrolu souborů) | rozpozná automaticky každý malware | zaručí bezpečnost vnitřní sítě ]]. Segmentace brání tomu, aby kompromitované studentské zařízení automaticky dosáhlo na administrátorský server.

**Vyber vrstvy obrany do hloubky:**

<!-- data-randomize="true" -->
[[X]] bezpečnostní aktualizace
[[X]] omezená oprávnění
[[X]] monitoring a logy
[[X]] oddělené a ověřené zálohy
[[ ]] spoléhání na jediný antivirus

## Detekce známého i neznámého

Signaturní detekce hledá známé vzory, heuristika podezřelé vlastnosti a behaviorální analýza sleduje činnost programu. [[Sandbox]] spustí obsah izolovaně a reputační služba využívá informace z mnoha zařízení.

[[EDR]] shromažďuje telemetrii koncových zařízení a pomáhá incident analyzovat a omezit. Antivirus může udělat falešně pozitivní i falešně negativní závěr, proto je [[ (jednou vrstvou, nikoli magickým filtrem) | úplnou náhradou bezpečnostního procesu | spolehlivý pouze bez aktualizací ]].

## Záloha a reakce

Pravidlo [[3–2–1]] požaduje tři kopie, dva typy úložiště a jednu oddělenou. Offline nebo immutable kopie omezuje možnost, že ji útočník smaže. Skutečnou hodnotu zálohy prokáže až vyzkoušená [[obnova]].

Při aktivním šifrování je vhodné omezit síťové spojení a kontaktovat bezpečnostní tým. Stopy se nemažou bez rozmyslu. Kompromitované heslo se mění z čistého zařízení a ukončí se relace. Postup vede od detekce přes omezení, analýzu a odstranění příčiny k obnově a [[poučení]].
