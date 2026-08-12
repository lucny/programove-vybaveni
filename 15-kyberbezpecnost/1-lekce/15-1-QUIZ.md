<!--
title: Kyberprostor, hrozby a řízení bezpečnosti – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co zahrnuje pojem kyberprostor?**

<!-- data-randomize="true" -->
[(X)] Propojené informační a komunikační technologie včetně fyzické infrastruktury.
[( )] Pouze webové stránky dostupné veřejnosti.
[( )] Nehmotný svět bez vazby na zařízení a sítě.
[( )] Výhradně sociální sítě a cloudová úložiště.

---

**2. Co je v řízení bezpečnosti aktivum?**

<!-- data-randomize="true" -->
[(X)] Něco hodnotného, co potřebujeme chránit.
[( )] Slabé místo umožňující zneužití.
[( )] Událost, která již narušila systém.
[( )] Osoba provádějící každý bezpečnostní test.

---

**3. Jaký je rozdíl mezi hrozbou a zranitelností?**

<!-- data-randomize="true" -->
[(X)] Hrozba může škodit, zranitelnost je slabina, kterou může využít.
[( )] Hrozba je slabina a zranitelnost vzniklá škoda.
[( )] Hrozba je vždy útočník, zranitelnost vždy malware.
[( )] Jde o dva názvy stejného incidentu.

---

**4. Co vyjadřuje riziko?**

<!-- data-randomize="true" -->
[(X)] Pravděpodobnost využití slabiny spolu se závažností následků.
[( )] Pouze cenu bezpečnostního produktu.
[( )] Jistotu, že každý útok bude úspěšný.
[( )] Seznam všech zařízení v organizaci.

---

**5. Které vlastnosti tvoří CIA triádu?**

<!-- data-randomize="true" -->
[[X]] důvěrnost
[[X]] integrita
[[X]] dostupnost
[[ ]] anonymita
[[ ]] komprese

---

**6. Která situace narušuje integritu?**

<!-- data-randomize="true" -->
[(X)] Útočník změní číslo účtu na faktuře.
[( )] DDoS vyřadí server z provozu.
[( )] Neoprávněná osoba přečte zdravotní dokumentaci.
[( )] Uživatel si vytvoří dlouhé heslo.

---

**7. Jaký je rozdíl mezi DoS a DDoS?**

<!-- data-randomize="true" -->
[(X)] DDoS přichází distribuovaně z velkého množství zařízení.
[( )] DoS krade data, DDoS je pouze fyzická porucha.
[( )] DoS používá botnet, DDoS vždy jeden počítač.
[( )] DDoS chrání dostupnost, DoS důvěrnost.

---

**8. Co charakterizuje APT?**

<!-- data-randomize="true" -->
[(X)] Schopný protivník dlouhodobě a nenápadně usiluje o přístup ke konkrétnímu cíli.
[( )] Jeden konkrétní druh počítačového viru.
[( )] Krátký náhodný výpadek bez útočníka.
[( )] Automatická bezpečnostní aktualizace systému.

---

**9. Jaký je rozdíl mezi útokem a incidentem?**

<!-- data-randomize="true" -->
[(X)] Útok je pokus o zneužití, incident skutečné narušení nebo významné ohrožení.
[( )] Každý útok je incident ještě před dopadem.
[( )] Incident může vzniknout pouze úmyslným útokem.
[( )] Útok označuje poruchu a incident zranitelnost.

---

**10. Které činnosti patří k reakci na incident?**

<!-- data-randomize="true" -->
[[X]] detekce
[[X]] vyhodnocení
[[X]] omezení dopadu
[[X]] odstranění příčiny
[[X]] obnova provozu
[[ ]] ignorování logů
[[ ]] okamžité smazání všech stop


# 2. Interaktivní shrnutí kapitoly

## Kyberprostor stojí na skutečné infrastruktuře

Kyberprostor tvoří počítače, servery, sítě, cloudové služby, databáze, mobilní a průmyslová zařízení i software. Nejde o svět oddělený od reality. Datová centra, optické kabely, routery a koncová zařízení jsou fyzické, a proto může digitální útok ovlivnit nemocnici, výrobu nebo dopravu.

Představa čistě virtuálního prostoru [[ zcela odděluje digitální dění od fyzických následků | (zakrývá závislost služeb na skutečných zařízeních a lidech) | znamená totéž co cloudová služba ]].

## Od aktiva k opatření

[[Aktivum]] je něco hodnotného: data, účet, server, know-how, provoz nebo reputace. Hrozba může aktivum poškodit a [[zranitelnost]] je slabé místo, například neopravená chyba, slabé heslo nebo chybné oprávnění.

Riziko spojuje možnost využití slabiny se závažností dopadu. Bezpečnostní rozhodnutí proto začíná otázkami co chráníme, před čím a s jakými následky, nikoli [[ (automatickým nákupem stejného produktu pro každou situaci) | ignorováním hodnoty aktiva | předpokladem, že každá hrozba způsobí stejnou škodu ]].

**Vyber správná přiřazení základních pojmů:**

<!-- data-randomize="true" -->
[[X]] databáze zákazníků — aktivum
[[X]] neopravená chyba serveru — zranitelnost
[[X]] útočník nebo požár — hrozba
[[X]] šifrování a záloha — možná opatření
[[ ]] reputace organizace — technický útok

## CIA triáda a soukromí

[[Důvěrnost]] omezuje přístup na oprávněné osoby, integrita chrání data před nepozorovanou změnou a [[dostupnost]] zajišťuje použitelnost služby v potřebný čas. DDoS míří hlavně na dostupnost, změna částky na integritu a únik dokumentace na důvěrnost.

Soukromí je širší než důvěrnost. Řeší, proč se osobní údaje sbírají, kdo je používá a jak dlouho se uchovávají. Data mohou být [[ (technicky dobře chráněná, ale používaná problematickým způsobem) | automaticky soukromá jen díky šifrování | bezpečná pouze tehdy, když nejsou dostupná nikomu ]].

## Útoky, incidenty a odpovědnost

DoS vyřazuje službu, distribuovaný [[DDoS]] využívá mnoho zařízení, často botnet. APT popisuje cílený dlouhodobý způsob útoku, supply-chain útok zneužívá důvěryhodného dodavatele nebo aktualizaci.

Útok je pokus slabinu využít; incident znamená skutečné narušení nebo významné ohrožení a může vzniknout i chybou či poruchou. Týmy [[CERT]] nebo CSIRT koordinují reakci. V České republice je ústředním orgánem [[NÚKIB]] a významné regulované služby mají také právní povinnosti v oblasti řízení rizik a hlášení incidentů.
