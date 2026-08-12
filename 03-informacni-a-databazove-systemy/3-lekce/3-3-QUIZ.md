<!--
title: Životní cyklus informačního systému – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Čím má začínat životní cyklus IS?**

<!-- data-randomize="true" -->
[(X)] Vymezením skutečného problému a cílů.
[( )] Nákupem serveru bez analýzy.
[( )] Volbou programovacího jazyka.
[( )] Tvorbou grafického loga.

---

**2. Co je funkční požadavek?**

<!-- data-randomize="true" -->
[(X)] Popis toho, co má systém dělat.
[( )] Požadavek na rychlost nebo dostupnost.
[( )] Seznam názvů serverů.
[( )] Pouze grafický návrh obrazovky.

---

**3. Co může patřit mezi nefunkční požadavky?**

<!-- data-randomize="true" -->
[[X]] výkon
[[X]] dostupnost
[[X]] bezpečnost
[[X]] přístupnost
[[X]] obnovitelnost
[[ ]] název konkrétního tlačítka jako jediná funkce

---

**4. Které typy testování jsou v kapitole uvedeny?**

<!-- data-randomize="true" -->
[[X]] jednotkové
[[X]] integrační
[[X]] systémové
[[X]] uživatelské akceptační
[[ ]] pouze vizuální kontrola

---

**5. Co je kritickým bodem při nasazení nového IS?**

<!-- data-randomize="true" -->
[(X)] Migrace a kvalita starých dat.
[( )] Pouze barva přihlašovací stránky.
[( )] Výhradně typ monitoru.
[( )] Odstranění všech kontrol.

---

**6. Které strategie přechodu na nový systém kapitola rozlišuje?**

<!-- data-randomize="true" -->
[[X]] přímý přechod
[[X]] paralelní provoz
[[X]] pilotní nasazení
[[X]] postupné nasazení
[[ ]] náhodný přechod bez plánu

---

**7. Co znamená rollback?**

<!-- data-randomize="true" -->
[(X)] Postup návratu k bezpečnému předchozímu stavu.
[( )] Trvalé smazání starých dat.
[( )] Automatickou kompresi databáze.
[( )] Výhradně odhlášení uživatele.

---

**8. Jaký je rozdíl mezi incidentem a problémem?**

<!-- data-randomize="true" -->
[(X)] Incident je konkrétní narušení služby, problém jeho hlubší příčina.
[( )] Incident je příčina a problém jen uživatelská chyba.
[( )] Jde o synonyma.
[( )] Problém je vždy bezpečnostní útok.

---

**9. Co musí zahrnovat provoz a údržba IS?**

<!-- data-randomize="true" -->
[[X]] monitoring dostupnosti
[[X]] aktualizace
[[X]] správu oprávnění
[[X]] zálohy a obnovu
[[X]] evidenci změn
[[ ]] ignorování dokumentace

---

**10. Co je exit strategie u cloudové služby?**

<!-- data-randomize="true" -->
[(X)] Plán, jak získat data a pokračovat při změně nebo ukončení služby.
[( )] Automatický restart aplikace.
[( )] Způsob přihlášení administrátora.
[( )] Pouze smlouva o nákupu hardware.


# 2. Interaktivní shrnutí kapitoly

## Od potřeby k požadavkům

Životní cyklus IS začíná definicí [[problému]], nikoli technologií. Funkční požadavky říkají, co má systém dělat, zatímco nefunkční určují například výkon, dostupnost, bezpečnost nebo přístupnost.

Požadavek má být pokud možno [[ co nejstručnější bez kritérií | (měřitelný a ověřitelný) | pouze obecně pozitivní ]]. Součástí analýzy je také proveditelnost, náklady, rizika a právní omezení.

## Návrh a testování

Při návrhu se modelují procesy, data, role a architektura. Realizace může být sekvenční nebo [[iterativní]]. Iterace neznamená práci bez plánu.

**Vyber oblasti testování:**

<!-- data-randomize="true" -->
[[X]] jednotkové testy
[[X]] integrační testy
[[X]] systémové testy
[[X]] uživatelské akceptační testy
[[X]] výkon a oprávnění
[[ ]] jen kontrola, zda se aplikace spustí

## Nasazení

Při nasazení je kritická migrace [[dat]]. Staré záznamy mohou obsahovat duplicity a nekonzistence; bez čištění bychom chyby jen přenesli.

Strategie přechodu zahrnují přímý, paralelní, pilotní a postupný přechod. [[rollback]] je plán návratu k bezpečnému stavu, pokud nasazení selže.

## Provoz a konec života

Incident je konkrétní výpadek nebo narušení, zatímco [[problém]] je hlubší příčina. Údržba zahrnuje opravy, bezpečnostní aktualizace, změny funkcí i dokumentace.

Záloha musí být testována obnovou; replikace není sama o sobě [[záloha]].

Při outsourcingu či SaaS zůstává odpovědnost organizace. [[exit]] strategie určuje, jak získat data v použitelném formátu a přejít jinam. Životní cyklus končí řízeným vyřazením systému, účtů a integrací.
