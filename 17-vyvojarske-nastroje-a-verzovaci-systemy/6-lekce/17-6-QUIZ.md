<!--
title: Umělá inteligence při programování – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jak se AI asistent liší od klasického autocomplete?**

<!-- data-randomize="true" -->
[(X)] Může pracovat s přirozeným jazykem a širším kontextem projektu.
[( )] Navrhuje vždy jen jeden znak podle syntaxe.
[( )] Nemůže vysvětlovat existující kód.
[( )] Zaručuje správnost každého návrhu.

---

**2. Která posloupnost vystihuje rostoucí rozsah AI podpory?**

<!-- data-randomize="true" -->
[(X)] Autocomplete, generování kódu, konverzační asistent, agent.
[( )] Agent, překladač, textový editor, procesor.
[( )] Debugger, dokumentace, disk, síť.
[( )] Test, commit, image, monitor.

---

**3. S čím může AI podle kapitoly pomoci?**

<!-- data-randomize="true" -->
[[X]] generování kódu
[[X]] vysvětlení kódu
[[X]] refaktorování
[[X]] tvorba testů
[[X]] dokumentace
[[ ]] zaručení bezchybnosti
[[ ]] převzetí odpovědnosti za přijetí změny

---

**4. Co má obsahovat kvalitní zadání pro AI?**

<!-- data-randomize="true" -->
[(X)] Cíl, vstup, očekávaný výstup, omezení a kontext.
[( )] Pouze obecnou větu bez požadavků.
[( )] Jen název programovacího jazyka.
[( )] Výhradně seznam názvů souborů.

---

**5. Proč je při ladění důležitá reprodukce chyby?**

<!-- data-randomize="true" -->
[(X)] Dává konkrétní situaci pro ověření hypotézy a opravy.
[( )] Zajišťuje, že AI nebude potřebovat kód.
[( )] Nahrazuje spuštění testů.
[( )] Automaticky odstraní příčinu problému.

---

**6. Jakou roli má AI návrh příčiny chyby?**

<!-- data-randomize="true" -->
[(X)] Je hypotézou, kterou je nutné ověřit.
[( )] Je závazným důkazem správnosti.
[( )] Je náhradou skutečného stavu proměnných.
[( )] Je automaticky hotovým produkčním řešením.

---

**7. Co odlišuje programovacího agenta od běžného chatu?**

<!-- data-randomize="true" -->
[(X)] Může používat nástroje, měnit více souborů a spouštět příkazy či testy.
[( )] Nemůže číst žádný kontext projektu.
[( )] Pracuje pouze s jedním řádkem kódu.
[( )] Nepotřebuje lidské zadání ani oprávnění.

---

**8. Které informace tvoří užitečný kontext projektu?**

<!-- data-randomize="true" -->
[[X]] architektura a účel
[[X]] verze jazyka a frameworku
[[X]] struktura adresářů
[[X]] způsob testování
[[X]] části, které se nemají měnit
[[ ]] náhodné osobní údaje
[[ ]] barva plochy vývojáře

---

**9. Proč nelze AI kód slepě přijmout?**

<!-- data-randomize="true" -->
[(X)] Může obsahovat neexistující API, chyby, zastaralé postupy nebo bezpečnostní rizika.
[( )] AI nikdy neumí vytvořit syntakticky platný kód.
[( )] AI návrh nelze uložit do souboru.
[( )] Každý AI výstup je vždy totožný.

---

**10. Kdo nese odpovědnost za přijetí AI změny?**

<!-- data-randomize="true" -->
[(X)] Vývojář, který změnu chápe, ověří a schválí.
[( )] Samotný jazykový model.
[( )] Editor zdrojového kódu.
[( )] Vzdálený registr balíčků.


# 2. Interaktivní shrnutí kapitoly

## Od doplňování k agentovi

Klasické autocomplete vychází hlavně ze syntaxe, typů a symbolů projektu. AI asistent navíc rozumí zadání v přirozeném jazyce a může navrhovat delší změny. Rozsah roste po ose automatické doplňování → generování → konverzační asistent → programovací [[agent]].

Agent může podle oprávnění prohledat projekt, upravit soubory a spustit testy. Samostatnost však [[ (zvyšuje potřebu kontroly rozsahu a výsledku) | ruší odpovědnost vývojáře | zaručuje správnou architekturu změny ]].

## Výsledek závisí na zadání a kontextu

Užitečný požadavek popisuje cíl, vstupy, očekávaný výstup, omezení a relevantní kontext. AI potřebuje znát například verze knihoven, strukturu projektu a pravidla testování. Bez těchto údajů může vytvořit obecně rozumný kód, který do konkrétní aplikace [[ nezapadne]].

README, technická dokumentace, testy a instrukční soubory proto pomáhají lidem i nástrojům. Dobře pojmenované moduly a jasné odpovědnosti zmenšují prostor pro chybný předpoklad.

## Ladění je cyklus ověřování

Při chybě má následovat reprodukce, hypotéza, test a oprava. Návrh AI je [[ důkazem správnosti | (hypotézou k ověření) | náhradou spuštěného programu ]]. Model může doporučit hraniční případy, jednotkové testy nebo vysvětlit hlášení, ale debugger a skutečné testy ukazují reálné chování.

**Co je nutné po významnější AI změně udělat?**

<!-- data-randomize="true" -->
[[X]] přečíst a pochopit změněný kód
[[X]] zkontrolovat diff
[[X]] spustit relevantní kontroly a testy
[[X]] posoudit bezpečnostní a výkonové dopady
[[ ]] přijmout změnu jen podle přesvědčivého stylu odpovědi

## Rychlá pomoc, stejná odpovědnost

AI může navrhnout neexistující API, zastaralý postup, chybnou interpretaci požadavku nebo zranitelnost. Přesvědčivý vzhled kódu není důkaz. [[Git]] umožňuje práci na samostatné větvi a přesnou kontrolu diffu, testy ověřují chování a vývojář rozhoduje o přijetí.

Nejbezpečnější pracovní řetězec proto propojuje IDE, testy, verzování a lidské schválení. Odpovědnost [[ (zůstává na vývojáři) | přechází na model po prvním spuštění | nese výhradně platforma s repozitářem ]].
