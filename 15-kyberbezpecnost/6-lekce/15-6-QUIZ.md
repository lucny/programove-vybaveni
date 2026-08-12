<!--
title: Bezpečnost jako proces: od jednotlivce k organizaci – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč samotná instalace bezpečnostních nástrojů nestačí?**

<!-- data-randomize="true" -->
[(X)] Bezpečnost vyžaduje průběžné řízení rizik, konfigurace, přístupů a reakce.
[( )] Každý nástroj funguje pouze jednou po instalaci.
[( )] Antivirus a firewall nelze používat současně.
[( )] Produkty neobsahují žádný software.

---

**2. Proč je důležitá inventarizace aktiv?**

<!-- data-randomize="true" -->
[(X)] Organizace nemůže chránit a aktualizovat systém, o jehož existenci neví.
[( )] Automaticky odstraní všechny zranitelnosti.
[( )] Nahrazuje monitoring a zálohy.
[( )] Určuje hesla všech uživatelů.

---

**3. Jaké riziko představuje software po konci podpory?**

<!-- data-randomize="true" -->
[(X)] Nedostává bezpečnostní opravy, i když stále technicky funguje.
[( )] Automaticky smaže všechna data v den ukončení podpory.
[( )] Stává se bezpečnější, protože se už nemění.
[( )] Nemůže být připojen k žádné síti.

---

**4. Co vyjadřuje model sdílené odpovědnosti v cloudu?**

<!-- data-randomize="true" -->
[(X)] Poskytovatel a zákazník chrání různé části podle konkrétní služby.
[( )] Poskytovatel vždy odpovídá za účty, data i konfiguraci zákazníka.
[( )] Zákazník musí spravovat fyzické datové centrum poskytovatele.
[( )] Přesun do cloudu odstraňuje bezpečnostní povinnosti.

---

**5. Které chyby zákazníka mohou ohrozit cloudovou službu?**

<!-- data-randomize="true" -->
[[X]] veřejné úložiště
[[X]] příliš široká oprávnění
[[X]] kompromitovaný správce
[[X]] uniklý API klíč
[[X]] chybná konfigurace databáze
[[ ]] správně omezený přístup
[[ ]] ověřená konfigurace

---

**6. Co je hlavní myšlenkou Zero Trust?**

<!-- data-randomize="true" -->
[(X)] Přístup se průběžně ověřuje podle identity, zařízení, kontextu a oprávnění.
[( )] Všem uvnitř firemní sítě se automaticky důvěřuje.
[( )] Nikdo nesmí získat přístup k žádné službě.
[( )] Stačí jednorázově ověřit umístění počítače.

---

**7. Jak Zero Trust mění tradiční představu vnitřní sítě?**

<!-- data-randomize="true" -->
[(X)] Vnitřní umístění samo o sobě není důvodem k důvěře.
[( )] Ruší potřebu autentizace uživatelů.
[( )] Považuje internet za automaticky bezpečný.
[( )] Přiděluje každému administrátorská práva.

---

**8. Proč nelze lidskou chybu řešit pouze výtkou uživateli?**

<!-- data-randomize="true" -->
[(X)] Systém má chybu očekávat a dalšími vrstvami omezit její dopad.
[( )] Uživatel nemá na bezpečnost žádný vliv.
[( )] Technická opatření nikdy nepomáhají.
[( )] Každou chybu lze předem úplně zakázat.

---

**9. Které prvky pomáhají omezit dopad lidské chyby?**

<!-- data-randomize="true" -->
[[X]] MFA
[[X]] nejmenší oprávnění
[[X]] segmentace
[[X]] monitoring
[[X]] snadné hlášení incidentu
[[ ]] strach z oznámení chyby
[[ ]] jeden správce pro všechny účty

---

**10. Která otázka patří k bezpečnostnímu myšlení při instalaci programu?**

<!-- data-randomize="true" -->
[(X)] Odkud pochází, je podepsaný, podporovaný a jaká práva žádá?
[( )] Má jeho ikona důvěryhodnou barvu?
[( )] Používá stejnou velikost okna jako jiné aplikace?
[( )] Je soubor kratší než jeden megabajt?


# 2. Interaktivní shrnutí kapitoly

## Bezpečnost je opakovaný cyklus

Antivirus, firewall, VPN nebo správce hesel jsou nástroje, nikoli hotová bezpečnost. Organizace musí znát aktiva, sledovat hrozby, opravovat software, řídit oprávnění, kontrolovat konfiguraci, monitorovat incidenty a zkoušet obnovu.

[[Inventarizace]] je základ: server, o němž správce neví, nelze spolehlivě aktualizovat. Software po konci podpory zvyšuje riziko, protože [[ (přestává dostávat bezpečnostní opravy) | automaticky se odpojí od internetu | zůstává bezpečný, pokud stále funguje ]].

## Cloud rozděluje, nikoli ruší odpovědnost

Poskytovatel může chránit infrastrukturu, zákazník však stále nastavuje identity, oprávnění, data a služby podle konkrétního modelu. Veřejné úložiště, uniklý API klíč nebo kompromitovaný správce nejsou prolomením kryptografie cloudu.

Model [[shared responsibility]] proto vyžaduje přesně určit hranici. Otázka není pouze „je cloud bezpečný“, ale [[ (kterou část chrání poskytovatel a kterou zákazník) | zda poskytovatel převezme každou chybu konfigurace | zda data po přesunu nepotřebují přístupová práva ]].

## Důvěra se průběžně ověřuje

Zero Trust odmítá předpoklad, že požadavek zevnitř sítě je automaticky bezpečný. Posuzuje identitu, zařízení, oprávnění, kontext a riziko a přiděluje jen potřebný přístup. Neznamená „nikdo nic nesmí“, ale [[ (ověřený uživatel smí konkrétní povolenou činnost) | každý interní uživatel smí vše | poloha zařízení nahrazuje autentizaci ]].

**Vyber projevy principu Zero Trust a omezené důvěry:**

<!-- data-randomize="true" -->
[[X]] ověřování identity a stavu zařízení
[[X]] nejmenší potřebná oprávnění
[[X]] posouzení kontextu požadavku
[[X]] průběžná kontrola důvěryhodnosti
[[ ]] automatický plný přístup z firemní Wi-Fi

## Chyba člověka nesmí zničit celý systém

Uživatel může kliknout na škodlivou přílohu. Pokud tím získá útočník správce celé sítě a smaže zálohy, selhaly i další vrstvy. Školení se proto kombinuje s MFA, segmentací, monitoringem a principem [[least privilege]].

Hlášení podezřelé události musí být jednoduché a bezpečné. Strach z přiznání chyby prodlužuje dobu, kdy se incident šíří bez povšimnutí.

## Bezpečnostní otázky v každodenní praxi

U služby zjišťujeme, jaká data sbírá, kdo je čte, jak funguje přihlášení a obnova. U programu kontrolujeme původ, podpis, podporu a oprávnění. U neobvyklé zprávy hledáme tlak, doménu a možnost [[ověření]] jiným kanálem.

Bezpečnostní myšlení nepředvídá každý útok. Staví systém tak, aby kompromitace jedné části [[ (neznamenala automatickou ztrátu všeho) | zůstala bez detekce a reakce | poskytla všem službám stejná oprávnění ]].
