<!--
title: Cloudové služby – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co nejlépe vystihuje cloud computing?**

<!-- data-randomize="true" -->
[(X)] Poskytování výpočetních zdrojů jako síťové služby.
[( )] Data bez fyzického hardwaru.
[( )] Jiný název pro internet.
[( )] Výhradně synchronizaci dokumentů.

---

**2. Které vlastnosti jsou pro cloud typické?**

<!-- data-randomize="true" -->
[[X]] samoobslužné poskytování zdrojů
[[X]] síťový přístup
[[X]] sdílení infrastruktury
[[X]] pružné škálování
[[X]] měření využití
[[ ]] nutnost znát fyzický rack serveru

---

**3. Co charakterizuje private cloud?**

<!-- data-randomize="true" -->
[(X)] Je určen jedné organizaci.
[( )] Musí být zdarma.
[( )] Musí běžet pouze doma.
[( )] Je vždy bez virtualizace.

---

**4. Co znamená hybrid cloud?**

<!-- data-randomize="true" -->
[(X)] Propojení privátního a veřejného prostředí.
[( )] Použití dvou webových prohlížečů.
[( )] Pouze veřejný cloud více zákazníků.
[( )] Lokální disk synchronizovaný přes USB.

---

**5. Co zákazník typicky spravuje u IaaS?**

<!-- data-randomize="true" -->
[(X)] Operační systém, aplikace a data.
[( )] Pouze heslo do hotové aplikace.
[( )] Fyzické datové centrum poskytovatele.
[( )] Výrobu procesorů.

---

**6. Co je SaaS?**

<!-- data-randomize="true" -->
[(X)] Hotová aplikace poskytovaná jako služba.
[( )] Pronájem pouze virtuálních disků.
[( )] Výhradně síťová kabeláž.
[( )] Lokální instalace bez poskytovatele.

---

**7. Za co zůstává uživatel odpovědný i u SaaS?**

<!-- data-randomize="true" -->
[[X]] správu účtů
[[X]] oprávnění
[[X]] citlivost ukládaných dat
[[X]] konfiguraci služby
[[ ]] fyzickou klimatizaci datacentra

---

**8. Co je hlavní rozdíl mezi synchronizací a zálohou?**

<!-- data-randomize="true" -->
[(X)] Synchronizace šíří aktuální stav, záloha umožňuje obnovit starší stav.
[( )] Synchronizace vždy uchovává všechny historické verze.
[( )] Záloha musí být vždy v cloudu.
[( )] Jde o totožné mechanismy.

---

**9. Která rizika jsou spojena s cloudem?**

<!-- data-randomize="true" -->
[[X]] vendor lock-in
[[X]] výpadek poskytovatele
[[X]] chybné nastavení oprávnění
[[X]] právní a geografické požadavky na data
[[ ]] automatická ztráta veškeré odpovědnosti zákazníka

---

**10. Co označuje shared responsibility?**

<!-- data-randomize="true" -->
[(X)] Odpovědnost za bezpečnost je rozdělena mezi poskytovatele a zákazníka.
[( )] Poskytovatel přebírá vždy veškerou odpovědnost.
[( )] Každý uživatel spravuje fyzický server.
[( )] Cloud je společně vlastněn zákazníky.


# 2. Interaktivní shrnutí kapitoly

## Cloud jako provozní model

Cloud neznamená, že data přestala být fyzická. Výpočty stále provádějí procesory a data leží na discích v [[datacentrech]]. Cloud odděluje uživatele od konkrétního fyzického serveru a poskytuje zdroje jako síťovou službu.

Typické jsou samoobslužnost, síťový přístup, sdílená infrastruktura, pružné [[škálování]] a měření využití.

## Modely nasazení

Public cloud poskytuje zdroje více zákazníkům. [[private]] cloud je určen jedné organizaci a hybrid cloud propojuje privátní a veřejné prostředí. Multi-cloud znamená používání více poskytovatelů.

Hybridní řešení může například citlivá data držet v privátním prostředí a jinou zátěž dočasně přesunout do [[veřejného]] cloudu.

## IaaS, PaaS a SaaS

U IaaS poskytovatel dodává infrastrukturu, zatímco zákazník spravuje OS, aplikace a data. U PaaS poskytovatel spravuje větší část platformy. U [[SaaS]] uživatel používá hotovou aplikaci.

**Vyber činnosti, za které zůstává zákazník odpovědný i u SaaS:**

<!-- data-randomize="true" -->
[[X]] uživatelské účty
[[X]] oprávnění
[[X]] správné zacházení s daty
[[X]] konfigurace funkcí
[[ ]] fyzická ostraha datacentra

Rozdělení odpovědnosti mezi poskytovatele a zákazníka se označuje jako shared [[responsibility]].

## Úložiště, synchronizace a záloha

Cloudové úložiště, synchronizace a záloha nejsou synonyma. Synchronizace udržuje stejný aktuální stav na více místech, takže chyba nebo smazání se může [[ zůstat vždy jen na jednom zařízení | (rozšířit i na další zařízení) | automaticky změnit na archiv ]].

Záloha má umožnit návrat ke staršímu bezpečnému [[stavu]]. Verzování cloudové služby může pomoci, ale musí být skutečně nastaveno a ověřeno.

## Přínosy a rizika

Cloud umožňuje rychlé škálování, automatizaci a dostupnost bez nákupu vlastního hardwaru. Současně vytváří závislost na poskytovateli, připojení, cenách a jeho pravidlech. Rizikem je vendor [[lock-in]].

Proto je důležitý export dat, záložní plán, správná oprávnění a znalost právního a geografického umístění citlivých dat.
