<!--
title: 4. Přenos dat – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Které pořadí odpovídá obecnému modelu datové komunikace?**

<!-- data-randomize="true" -->
[( )] kanál → zdroj → vysílač → příjemce
[(X)] zdroj → vysílač → kanál → přijímač
[( )] přijímač → kanál → zdroj → vysílač
[( )] zdroj → databáze → procesor → příjemce

---

**2. Co může způsobit, že přijatý signál není stejný jako odeslaný?**

<!-- data-randomize="true" -->
[( )] metadata
[( )] komprese
[(X)] šum a rušení
[( )] formát souboru

---

**3. Která spojení média a fyzikálního jevu jsou správná?**

<!-- data-randomize="true" -->
[[X]] metalické vedení — elektrické změny
[[X]] optické vlákno — světlo
[[X]] bezdrátový přenos — elektromagnetické vlny
[[ ]] optické vlákno — zvukové vlny
[[ ]] Wi-Fi — mechanické vibrace

---

**4. Co vyjadřuje propustnost?**

<!-- data-randomize="true" -->
[( )] Kolísání zpoždění.
[(X)] Množství skutečně přenesených užitečných dat.
[( )] Počet chyb v paketu.
[( )] Počet symbolů modulace.

---

**5. Co označuje latence?**

<!-- data-randomize="true" -->
[( )] objem souboru
[( )] bitovou hloubku
[(X)] zpoždění
[( )] sílu signálu

---

**6. Pro kterou aplikaci je zvlášť důležitý malý jitter?**

<!-- data-randomize="true" -->
[( )] archivace souborů
[(X)] videohovor
[( )] tisk dokumentu
[( )] komprese obrázku

---

**7. Co udává baud?**

<!-- data-randomize="true" -->
[( )] bajty za sekundu
[( )] bity v jednom souboru
[(X)] symboly za sekundu
[( )] chyby za sekundu

---

**8. Která tvrzení o modulaci jsou správná?**

<!-- data-randomize="true" -->
[[X]] Může měnit amplitudu.
[[X]] Může měnit frekvenci.
[[X]] Může měnit fázi.
[[X]] QAM kombinuje více vlastností signálu.
[[ ]] Modulace je vždy komprese dat.
[[ ]] Jeden symbol vždy nese právě jeden bit.

---

**9. K čemu je určen CRC?**

<!-- data-randomize="true" -->
[( )] Utajení přenášených dat.
[( )] Zmenšení velikosti paketu.
[(X)] Detekce přenosových chyb.
[( )] Převod textu na Unicode.

---

**10. Která tvrzení rozlišují ARQ a FEC?**

<!-- data-randomize="true" -->
[[X]] ARQ používá opakovaný přenos.
[[X]] FEC přidává opravnou redundanci.
[[X]] FEC může opravit některé chyby bez retransmise.
[[ ]] ARQ je druh ztrátové komprese.
[[ ]] FEC odstraňuje veškerou redundanci.


# 2. Interaktivní shrnutí kapitoly

## Model komunikace

Při datové komunikaci předává jeden systém informaci jinému. Zjednodušený model lze popsat:

**zdroj → kódování → vysílač → [[kanál]] → přijímač → dekódování → příjemce**

Přenosový kanál může být ovlivněn šumem a [[rušením]]. Proto se v digitální komunikaci používají mechanismy pro detekci chyb, jejich opravu nebo opakované odeslání.

Zpětná vazba umožňuje například potvrdit, že data dorazila. Pokud potvrzení nepřijde, systém může [[ data zahodit bez kontroly | (vyžádat opakovaný přenos) | změnit jejich význam ]].

## Jak data fyzicky cestují

Logická data mohou během jedné komunikace projít různými fyzickými médii. V metalickém kabelu se informace reprezentuje elektrickými změnami, v optickém vlákně [[světlem]] a při bezdrátovém přenosu elektromagnetickými vlnami.

Stejný síťový protokol přitom může využívat různé fyzické technologie. Například IP lze přenášet pomocí Ethernetu, Wi-Fi i mobilních sítí. Fyzické médium a [[protokol]] tedy nejsou totéž.

**Vyber vlastnosti, které mohou ovlivnit vhodnost přenosového média:**

<!-- data-randomize="true" -->
[[X]] přenosová rychlost
[[X]] útlum
[[X]] citlivost na rušení
[[X]] maximální vzdálenost
[[X]] cena a instalace
[[ ]] barva ikon v operačním systému

## Rychlost není jediné číslo

Bitová rychlost se udává například v Mbit/s. Skutečné množství užitečných dat přenesených za čas se nazývá [[propustnost]]. Bývá nižší než teoretická rychlost linky kvůli režii, čekání nebo rušení.

[[latence]] označuje zpoždění. Spojení může mít vysokou kapacitu, ale zároveň vysokou latenci. [[jitter]] je kolísání zpoždění a je problematické hlavně u komunikace v reálném čase.

Baud udává počet [[symbolů]] za sekundu. Jeden symbol nemusí nést pouze jeden bit. Pokud jeden symbol reprezentuje dva bity a přenášíme 1000 symbolů za sekundu, bitová rychlost je [[2000]] bit/s.

## Kódování signálu a modulace

Při fyzickém přenosu se datové hodnoty převádějí na změny signálu. Není obecně správné chápat digitální síť jako jednoduché pravidlo „0 = bez napětí, 1 = napětí“. Moderní systémy používají složitější linkové [[kódování]].

Při modulaci se mění vlastnost nosného signálu, například amplituda, frekvence nebo [[fáze]]. QAM kombinuje amplitudu a fázi a může jedním symbolem reprezentovat více bitů.

Při horší kvalitě spojení může systém zvolit [[ jemnější a náročnější modulaci | (robustnější, ale méně datově účinnou modulaci) | vždy vyšší počet symbolů ]].

## Jak odhalit a řešit chybu

Jednoduchým kontrolním mechanismem je paritní [[bit]]. Kontrolní součet a CRC vytvářejí hodnotu odvozenou z přenášených dat. [[CRC]] je navržen především pro detekci neúmyslných přenosových chyb, nikoli jako kryptografická ochrana.

Po nalezení chyby existují dvě základní strategie. ARQ využívá [[ opakování výpočtu | (retransmisi) | kompresi ]] a poškozená data se odešlou znovu. FEC naproti tomu předem přidává dostatek [[redundance]], aby příjemce mohl některé chyby opravit bez nového přenosu.

Hlavní myšlenka kapitoly: kvalitu přenosu neurčuje pouze rychlost, ale také fyzické médium, [[latence]], rušení a způsob detekce a řešení chyb.
