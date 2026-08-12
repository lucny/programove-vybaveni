<!--
title: Relační model – data jako tvrzení a vztahy – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč relační návrh obvykle nerozumně nesoustředí vše do jedné velké tabulky?**

<!-- data-randomize="true" -->
[(X)] Opakování faktů vede k anomáliím a nekonzistenci.
[( )] Databáze nesmí mít mnoho sloupců.
[( )] SQL neumí číst velké tabulky.
[( )] Tabulky nemohou obsahovat text.

---

**2. Co je relace v matematickém základu relačního modelu?**

<!-- data-randomize="true" -->
[(X)] Množina uspořádaných n-tic.
[( )] Grafová hrana.
[( )] Soubor na disku.
[( )] Jedna hodnota v buňce.

---

**3. Co v běžné databázové tabulce odpovídá atributu?**

<!-- data-randomize="true" -->
[(X)] Sloupec.
[( )] Řádek.
[( )] Index.
[( )] Databázový server.

---

**4. Co určuje datový typ sloupce?**

<!-- data-randomize="true" -->
[(X)] Povolené hodnoty a smysluplné operace.
[( )] Pouze barvu v klientovi.
[( )] Pořadí řádků.
[( )] Název tabulky.

---

**5. Co znamená NULL?**

<!-- data-randomize="true" -->
[(X)] Chybějící, neznámou nebo nepoužitelnou hodnotu.
[( )] Nulu.
[( )] Prázdný text.
[( )] Automaticky chybný řádek.

---

**6. Jak se správně testuje NULL v SQL?**

<!-- data-randomize="true" -->
[(X)] IS NULL
[( )] = NULL
[( )] == NULL
[( )] LIKE NULL

---

**7. Co je kandidátský klíč?**

<!-- data-randomize="true" -->
[(X)] Minimální kombinace atributů jednoznačně určující záznam.
[( )] Libovolný index.
[( )] Každý cizí klíč.
[( )] Pouze automatické ID.

---

**8. Co je cizí klíč?**

<!-- data-randomize="true" -->
[(X)] Omezení propojující hodnotu s existujícím řádkem jiné nebo stejné tabulky.
[( )] Alternativní název primárního klíče.
[( )] Klíč pro šifrování.
[( )] Povinný textový sloupec.

---

**9. Kam se u vztahu 1:N typicky umísťuje cizí klíč?**

<!-- data-randomize="true" -->
[(X)] Na stranu N.
[( )] Vždy na stranu 1.
[( )] Do samostatného souboru.
[( )] Do každé tabulky dvakrát.

---

**10. Jak se v relačním modelu obvykle realizuje vztah N:M?**

<!-- data-randomize="true" -->
[(X)] Vazební tabulkou.
[( )] Jedním cizím klíčem v libovolné tabulce.
[( )] Seznamem ID v jednom textovém poli.
[( )] Pomocí NULL.


# 2. Interaktivní shrnutí kapitoly

## Fakta ukládáme podle významu

Jedna obří tabulka vede k opakování stejných faktů a k anomáliím při vložení, změně a odstranění. Relační návrh proto rozděluje fakta do tabulek podle jejich [[významu]].

Relace je matematicky množina n-tic; prakticky ji vidíme jako tabulku. Sloupce jsou [[atributy]], řádky záznamy a doména určuje povolené hodnoty.

## Datové typy a NULL

Datový typ není dekorace. Určuje, jaké hodnoty lze uložit a jaké operace dávají smysl. Datum je vhodné ukládat jako datumový typ, ne jen jako libovolný [[text]].

`NULL` neznamená nulu ani prázdný text. Testuje se pomocí [[IS NULL]] a SQL kvůli neznámým hodnotám používá tříhodnotovou logiku.

## Klíče

Kandidátský klíč jednoznačně identifikuje záznam; z něj se volí [[primární]] klíč. Další kandidátské klíče lze chránit pomocí `UNIQUE`.

Cizí klíč zajišťuje [[referenční integritu]].

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] primární klíč může být složený
[[X]] umělé ID není povinné v každé tabulce
[[X]] cizí klíč může odkazovat i do stejné tabulky
[[ ]] e-mail je vždy neměnný a ideální primární klíč

## Kardinalita

U 1:N je cizí klíč na straně [[N]]. Vztah N:M se převádí na vazební tabulku, která může obsahovat také vlastní údaje, například roli nebo čas přihlášení.
