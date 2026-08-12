<!--
title: Efektivita algoritmů a volba řešení – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč správný algoritmus nemusí být vhodným řešením?**

<!-- data-randomize="true" -->
[(X)] Může být na velkých datech příliš pomalý nebo paměťově náročný.
[( )] Správný algoritmus nikdy nevytváří výstup.
[( )] Každý správný algoritmus musí být rekurzivní.
[( )] Správnost platí pouze pro malé programy.

---

**2. Co sleduje časová náročnost?**

<!-- data-randomize="true" -->
[(X)] Jak roste množství práce s velikostí vstupu.
[( )] Přesný čas na každém možném počítači.
[( )] Pouze počet řádků zdrojového kódu.
[( )] Velikost spustitelného souboru.

---

**3. Co vyjadřuje O(1)?**

<!-- data-randomize="true" -->
[(X)] Náročnost se zásadně nezvětšuje s počtem prvků.
[( )] Algoritmus musí provést právě jednu instrukci.
[( )] Práce roste stejně rychle jako vstup.
[( )] Počet operací roste kvadraticky.

---

**4. Která operace je v kapitole příkladem O(n)?**

<!-- data-randomize="true" -->
[(X)] Hledání v neuspořádaném seznamu postupným průchodem.
[( )] Přístup k prvku pole na známém indexu.
[( )] Dvojice vnořených průchodů všemi prvky.
[( )] Binární půlení seřazeného seznamu.

---

**5. Co často vede k chování O(n²)?**

<!-- data-randomize="true" -->
[(X)] Dva vnořené průchody stejnými daty.
[( )] Přímý přístup podle indexu.
[( )] Jedno porovnání dvou hodnot.
[( )] Odstranění nepoužitého komentáře.

---

**6. Jaká podmínka je nutná pro binární vyhledávání?**

<!-- data-randomize="true" -->
[(X)] Data musí být seřazená.
[( )] Data musí obsahovat právě milion položek.
[( )] Každá hodnota se musí opakovat.
[( )] Seznam nesmí mít indexy.

---

**7. Proč je bubble sort nevhodný pro velké seznamy?**

<!-- data-randomize="true" -->
[(X)] Jeho typická časová náročnost je přibližně O(n²).
[( )] Nelze s ním seřadit číselné hodnoty.
[( )] Vyžaduje vždy binární strom.
[( )] Pracuje jen se dvěma prvky.

---

**8. Která kritéria mohou ovlivnit volbu řešení?**

<!-- data-randomize="true" -->
[[X]] rychlost
[[X]] spotřeba paměti
[[X]] čitelnost
[[X]] snadnost údržby
[[ ]] barva editoru
[[ ]] počet komentářů bez ohledu na obsah

---

**9. Co je profilování?**

<!-- data-randomize="true" -->
[(X)] Měření, které hledá části programu spotřebovávající nejvíce času.
[( )] Přepis kódu do jiného přirozeného jazyka.
[( )] Seřazení všech proměnných podle názvu.
[( )] Automatické odstranění každé bezpečnostní chyby.

---

**10. Jaká zásada je doporučena před optimalizací?**

<!-- data-randomize="true" -->
[(X)] Nejprve vytvořit správné a srozumitelné řešení a změřit problém.
[( )] Optimalizovat každou funkci ještě před jejím napsáním.
[( )] Vždy nahradit knihovní algoritmus vlastní verzí.
[( )] Ignorovat velikost skutečných vstupních dat.


# 2. Interaktivní shrnutí kapitoly

## Správnost je začátek, ne konec

Dva algoritmy mohou dávat stejný výsledek, ale při milionu položek se chovat zcela jinak. Hodnotíme proto nejen správnost, ale také čas, paměť, čitelnost a údržbu. U malého školního vstupu může být nejlepší jednoduché řešení; u vytížené služby může rozhodovat každá opakovaná operace.

Zjištění maxima nevyžaduje seřazení celého seznamu. Stačí jediný [[průchod]], při němž si program pamatuje největší dosavadní hodnotu.

## Jak práce roste se vstupem

Asymptotická složitost neudává přesný počet sekund. Popisuje, jak se množství práce mění s velikostí vstupu. Přístup na známý index je přibližně [[O(1)]], lineární průchod [[O(n)]] a dva vnořené průchody často O(n²).

Pokud se vstup u O(n²) zvětší desetkrát, množství práce se přibližně [[ zvětší desetkrát | (zvětší stokrát) | nezmění ]]. Právě proto malé testovací pole nemusí odhalit budoucí problém.

## Hledání a třídění

Lineární vyhledávání ubírá možnosti po jedné. Binární vyhledávání zahazuje přibližně polovinu zbývajících možností, ale vyžaduje [[seřazená]] data a má chování O(log n). Příprava se může vyplatit, pokud budeme v témže seznamu hledat opakovaně.

Bubble sort je názorný, ale jeho opakované porovnávání sousedů vede typicky k O(n²). V praxi je proto rozumné použít [[ (dobře otestovanou vestavěnou nebo knihovní implementaci) | vždy vlastní nejjednodušší třídění | náhodné prohazování prvků ]].

**Které jevy jsou varovným signálem neefektivního programu?**

<!-- data-randomize="true" -->
[[X]] vnořené cykly nad velkými daty
[[X]] opakování stejného neměnného výpočtu
[[X]] datová struktura nevhodná pro časté hledání
[[ ]] přímý přístup k prvku na známém indexu
[[ ]] jednorázové zpracování několika položek

## Teorie, měření a kompromisy

Stejnou složitost mohou v praxi ovlivnit jazyk, procesor, paměť, disk, síť i knihovny. [[Profilování]] ukáže, kde program skutečně tráví čas. Optimalizace má následovat až po měření; předčasné změny mohou zhoršit srozumitelnost bez reálného přínosu.

Někdy vyměníme paměť za rychlost, například vytvořením indexu. Jindy investujeme do přípravy dat pro mnoho budoucích dotazů. Dobrá volba je vždy [[ univerzálně nejrychlejší algoritmus | (kompromis odpovídající skutečnému použití) | řešení s největším počtem řádků ]].
