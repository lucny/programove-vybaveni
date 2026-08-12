<!--
title: Práce se soubory – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč programy používají soubory?**

<!-- data-randomize="true" -->
[(X)] Uchovávají data trvale i po ukončení procesu.
[( )] Nahrazují vždy operační paměť.
[( )] Slouží pouze ke zdrojovému kódu.
[( )] Lze je číst jen jedním programem.

---

**2. Které možnosti soubory poskytují?**

<!-- data-randomize="true" -->
[[X]] trvalé uchování dat
[[X]] výměnu mezi programy
[[X]] zpracování dat větších než RAM
[[X]] tvorbu logů
[[ ]] automatickou validaci obsahu
[[ ]] záruku správného formátu podle přípony

---

**3. Jaký je základní rozdíl textového a binárního souboru?**

<!-- data-randomize="true" -->
[(X)] Textový interpretuje data jako znaky, binární jako obecné bajty podle formátu.
[( )] Binární soubor neobsahuje žádné bajty.
[( )] Textový soubor je vždy menší.
[( )] Binární soubor lze vždy číst jako srozumitelný text.

---

**4. Jaké čtyři kroky tvoří běžnou práci se souborem?**

<!-- data-randomize="true" -->
[(X)] Otevřít, číst nebo zapisovat, zpracovat, uzavřít.
[( )] Přejmenovat, zkompilovat, odeslat, smazat.
[( )] Alokovat, indexovat, třídit, přeložit.
[( )] Importovat, větvit, sloučit, publikovat.

---

**5. Co znamená režim r?**

<!-- data-randomize="true" -->
[(X)] Otevření existujícího souboru pro čtení.
[( )] Zápis s přepsáním obsahu.
[( )] Připojení na konec.
[( )] Binární zápis nového souboru.

---

**6. Co znamená režim w?**

<!-- data-randomize="true" -->
[(X)] Zápis, který vytvoří soubor nebo přepíše existující.
[( )] Čtení bez možnosti změny.
[( )] Připojení za poslední bajt bez přepsání.
[( )] Současné čtení i zápis bez změny délky.

---

**7. Co znamená režim a?**

<!-- data-randomize="true" -->
[(X)] Připojování nového obsahu na konec.
[( )] Automatické čtení všech řádků.
[( )] Otevření pouze binárního souboru.
[( )] Přepsání souboru od začátku.

---

**8. Jak C reprezentuje otevřený soubor?**

<!-- data-randomize="true" -->
[(X)] Ukazatelem typu FILE*.
[( )] Objektem typu str.
[( )] Pole znaků bez ukazatele.
[( )] Slovníkem klíč-hodnota.

---

**9. Proč je v C důležité fclose?**

<!-- data-randomize="true" -->
[(X)] Uvolní prostředky spojené s otevřeným souborem.
[( )] Vymaže obsah souboru.
[( )] Změní textový soubor na binární.
[( )] Ověří správnost každého záznamu.

---

**10. Jaký přínos má v Pythonu with open?**

<!-- data-randomize="true" -->
[(X)] Soubor se po opuštění bloku automaticky uzavře.
[( )] Soubor se vždy načte celý do RAM.
[( )] Chyby při čtení se automaticky opraví.
[( )] Režim zápisu nikdy nepřepíše data.


# 2. Interaktivní shrnutí kapitoly

## Trvalá data mimo proces

Proměnné běžícího programu po jeho ukončení zanikají, soubor uchovává data na [[trvalém úložišti]]. Umožňuje výměnu mezi programy, tvorbu logů i postupné zpracování objemu, který nelze celý držet v RAM.

Textový soubor interpretuje data jako znaky čitelné člověkem. Binární soubor ukládá data v podobě, která není přímo čitelná v běžném textovém editoru. Pro textové formáty jako HTML, XML nebo JSON je důležité správné [[kódování]].

## Životní cyklus otevřeného souboru

Program vytvoří spojení se souborem, čte nebo zapisuje, data zpracuje a nakonec prostředek uzavře. Režim [[r]] čte existující soubor, `w` vytváří či přepisuje a [[a]] připojuje na konec. `r+` dovoluje čtení i zápis, `b` přidává binární režim.

**Vyber důsledky režimů otevření:**

<!-- data-randomize="true" -->
[[X]] r vyžaduje existující soubor
[[X]] w může odstranit předchozí obsah
[[X]] a zachová obsah a zapisuje za něj
[[X]] rb čte v binárním režimu
[[ ]] a vždy přepíše soubor od začátku

Před zápisem je proto nutné vědomě zvolit režim; záměna `a` a `w` může znamenat ztrátu dat.

## Souborové ukazatele v C

C pracuje s typem [[FILE*]] z `stdio.h`. `fopen` může selhat a vrátit `NULL`, což je nutné zkontrolovat. `fgets` čte řádky, `fgetc` znaky a `fprintf` formátovaně zapisuje. [[fclose]] uzavře proud a uvolní prostředky.

Ruční správa dává kontrolu, ale každý úspěšně otevřený soubor musí mít odpovídající uzavření i při chybových cestách.

## Kontextový manažer v Pythonu

Pythonový zápis `with open(...) as soubor` uzavře soubor automaticky po opuštění bloku. `read` načte celý obsah, iterace přes objekt čte po řádcích a `readlines` vytvoří seznam řádků. Pro text se výslovně uvádí například [[UTF-8]].

Kontextový manažer zjednodušuje správu prostředku, ale [[ (neodstraňuje potřebu řešit chyby a správný režim) | vždy obnoví přepsaný obsah | zaručuje validitu dat uvnitř souboru ]].
