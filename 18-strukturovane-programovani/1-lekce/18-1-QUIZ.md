<!--
title: Principy strukturovaného programování – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jaký problém přinášelo nadměrné používání GOTO?**

<!-- data-randomize="true" -->
[(X)] Vznikal nepřehledný tok řízení obtížný na údržbu a testování.
[( )] Program nemohl obsahovat žádné proměnné.
[( )] Každý příkaz se vykonal právě jednou.
[( )] Kód se automaticky rozdělil do funkcí.

---

**2. Které důsledky měl nestrukturovaný kód?**

<!-- data-randomize="true" -->
[[X]] špatná čitelnost
[[X]] náročná údržba
[[X]] složité testování
[[X]] nízká produktivita
[[ ]] automatická modularita
[[ ]] snadné ověření všech cest

---

**3. S kým je spojen dopis „Go To Statement Considered Harmful“?**

<!-- data-randomize="true" -->
[(X)] S Edsgerem Dijkstrou.
[( )] S tvůrcem Pythonu.
[( )] S autorem HTML.
[( )] S vývojářem GitHubu.

---

**4. Co je sekvence?**

<!-- data-randomize="true" -->
[(X)] Vykonávání příkazů v určeném pořadí.
[( )] Volba jedné z větví podle podmínky.
[( )] Opakování bloku do splnění podmínky.
[( )] Bezpodmínečný skok na libovolné místo.

---

**5. Co je větvení?**

<!-- data-randomize="true" -->
[(X)] Rozhodnutí mezi cestami podle podmínky.
[( )] Pevný průchod všemi příkazy.
[( )] Vytvoření nové zdrojové větve v Gitu.
[( )] Opakování bez možnosti ukončení.

---

**6. Co je iterace?**

<!-- data-randomize="true" -->
[(X)] Opakované vykonávání skupiny příkazů.
[( )] Deklarace lokální proměnné.
[( )] Překlad programu do strojového kódu.
[( )] Jednorázové vyhodnocení konstanty.

---

**7. Které zásady podporuje strukturované programování?**

<!-- data-randomize="true" -->
[[X]] rozklad na procedury a funkce
[[X]] lokální proměnné
[[X]] jasná rozhraní částí
[[X]] systematické názvy
[[ ]] nekontrolované skoky
[[ ]] globální stav pro každou úlohu

---

**8. Proč jsou lokální proměnné výhodné?**

<!-- data-randomize="true" -->
[(X)] Omezují rozsah platnosti a nežádoucí vazby mezi částmi.
[( )] Jsou přístupné odkudkoli v programu.
[( )] Uchovávají hodnotu po vypnutí počítače.
[( )] Nahrazují všechny parametry funkcí.

---

**9. Jak strukturování podporuje testování?**

<!-- data-randomize="true" -->
[(X)] Menší části programu lze ověřovat odděleně.
[( )] Zaručuje správnost bez spuštění testů.
[( )] Zakazuje vytváření různých cest programem.
[( )] Převádí testy na komentáře.

---

**10. Co je základní myšlenkou strukturovaného programování?**

<!-- data-randomize="true" -->
[(X)] Rozdělit složitý problém na přehledné části s řízeným tokem.
[( )] Soustředit celý program do jedné dlouhé funkce.
[( )] Používat co nejvíce globálních proměnných.
[( )] Nahrazovat podmínky libovolnými skoky.


# 2. Interaktivní shrnutí kapitoly

## Proč nestačí, že program běží

Nekontrolované skoky pomocí [[GOTO]] vytvářely programy, jejichž tok bylo těžké sledovat. Změna na jednom místě mohla ovlivnit vzdálenou část a počet možných průchodů komplikoval testování. S rostoucí velikostí proto klesala čitelnost i produktivita.

Strukturované programování vzniklo jako odpověď: tok má být sestaven z omezených, srozumitelných konstrukcí. Dijkstrův text upozornil, že libovolné skoky [[ usnadňují dokazování toku | (ztěžují porozumění stavu a průchodu programu) | nahrazují potřebu funkcí ]].

## Tři stavební konstrukce

[[Sekvence]] vykonává kroky v pořadí. Větvení vybírá cestu podle podmínky a [[iterace]] opakuje blok. Jejich kombinací lze popsat běžnou logiku bez skoků na libovolná místa.

**Vyber správné příklady řídicích konstrukcí:**

<!-- data-randomize="true" -->
[[X]] výpočet a následný výpis — sekvence
[[X]] sleva podle věku — větvení
[[X]] zpracování každé položky — iterace
[[ ]] přeskočení na náhodný řádek — strukturovaná selekce

Omezení GOTO neznamená zákaz každého řízení toku. Naopak se používají jasně ohraničené podmínky a cykly, u nichž lze zjistit vstup, výstup a návaznost.

## Menší části s jasným rozhraním

Velký problém se rozkládá do procedur a funkcí. Každá část má mít srozumitelnou úlohu a komunikovat přes definované [[rozhraní]]. Lokální proměnné omezují místo, odkud lze stav měnit, a smysluplné názvy zpřehledňují záměr.

Výsledkem není automaticky bezchybný program. Struktura však umožňuje části [[ (testovat a měnit s menším rizikem) | libovolně propojovat globálním stavem | skrýt před ostatními vývojáři ]]. Dobře navrženou funkci lze navíc opakovaně použít a tým může rozdělit práci podle přirozených celků.
