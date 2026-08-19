<!--
title: Relační model – data jako tvrzení a vztahy – kvíz
language: cs
-->

# 1. Testovací část

**1. Jaký problém může nastat, když je kapacita učebny uložena v každé její rezervaci?**

<!-- data-randomize="true" -->
[(X)] Změna kapacity vyžaduje opravit více řádků a může vzniknout rozpor.
[( )] Databáze přestane umět řadit rezervace podle času.
[( )] Sloupec kapacita se automaticky změní na textový.
[( )] Rezervaci už nelze propojit s organizátorem.

---

**2. Co je relace v matematickém základu relačního modelu?**

<!-- data-randomize="true" -->
[(X)] Množina uspořádaných n-tic.
[( )] Jeden soubor s databázovým zálohováním.
[( )] Postup pro propojení dvou serverů.
[( )] Jediná hodnota uložená v buňce.

---

**3. Čemu v běžné databázové tabulce odpovídá atribut?**

<!-- data-randomize="true" -->
[(X)] Sloupci.
[( )] Celé databázi.
[( )] Jednomu řádku.
[( )] Připojenému klientovi.

---

**4. Co určuje datový typ sloupce?**

<!-- data-randomize="true" -->
[(X)] Které hodnoty lze uložit a jaké operace nad nimi dávají smysl.
[( )] Který uživatel smí řádek zobrazit.
[( )] V jakém pořadí budou řádky vráceny.
[( )] Kolik tabulek může databáze obsahovat.

---

**5. Proč je pro peněžní částku obvykle vhodné přesné desetinné číslo?**

<!-- data-randomize="true" -->
[(X)] Nezavádí nepřesnost binárního čísla s plovoucí čárkou.
[( )] Umožní uložit do částky celé datum rezervace.
[( )] Automaticky zajistí jedinečnost částky.
[( )] Odstraní potřebu definovat sloupec.

---

**6. Co vyjadřuje hodnota `NULL`?**

<!-- data-randomize="true" -->
[(X)] Chybějící, neznámou nebo nepoužitelnou hodnotu.
[( )] Číselnou hodnotu nula.
[( )] Prázdný text uložený ve sloupci.
[( )] Řádek, který databáze vždy odmítne.

---

**7. Jak se v SQL testuje, zda je hodnota `NULL`?**

<!-- data-randomize="true" -->
[(X)] `IS NULL`
[( )] `= NULL`
[( )] `== NULL`
[( )] `LIKE NULL`

---

**8. Která tvrzení o klíčích jsou správná?**

<!-- data-randomize="true" -->
[[X]] Kandidátský klíč je minimální kombinace atributů určující záznam.
[[X]] Primární klíč může tvořit více sloupců.
[[X]] Další kandidátský klíč lze chránit omezením `UNIQUE`.
[[ ]] Primární klíč musí vždy tvořit umělé číselné ID.

---

**9. Jaký účel má cizí klíč `rezervace.ucebna_id`?**

<!-- data-randomize="true" -->
[(X)] Vynucuje odkaz na existující učebnu a chrání referenční integritu.
[( )] Nahrazuje datový typ sloupce `ucebna_id`.
[( )] Ukládá heslo pro přístup k učebně.
[( )] Zajišťuje řazení rezervací podle času.

---

**10. Jak se obvykle převede vztah N:M mezi rezervacemi a uživateli?**

<!-- data-randomize="true" -->
[(X)] Vznikne vazební tabulka, jejíž řádek představuje jedno přihlášení.
[( )] ID všech uživatelů se zapíší do jednoho textového pole.
[( )] Jeden cizí klíč se vloží na obě strany vztahu.
[( )] Rezervace se duplikuje pro každého uživatele.

# 2. Interaktivní shrnutí kapitoly

## Fakta na správném místě

Rezervační systém potřebuje údaje o učebnách, lidech, rezervacích a účasti. Jeden velký seznam by stejné vlastnosti učebny nebo člověka opakoval v mnoha řádcích. Při změně kapacity by pak bylo nutné opravit všechny kopie; přehlédnutý řádek by vytvořil nekonzistentní údaj. Smazání poslední rezervace by dokonce mohlo odstranit jedinou informaci o existenci učebny. Relační návrh proto ukládá každý fakt pokud možno na jednom místě a ostatní tabulky na něj odkazují.

Relační model formuloval Edgar F. [[Codd]] na začátku sedmdesátých let. Jeho relace je množina uspořádaných n-tic; v databázové praxi ji chápeme jako tabulku. SQL tabulka není úplně totéž jako matematická relace, protože například může obsahovat duplicitní řádky a hodnoty `NULL`. Základní myšlenka však zůstává: nad celými množinami souvisejících údajů pracujeme podle jejich významu.

## Tabulka a datové hodnoty

Dobrá tabulka zastupuje jeden druh objektu nebo události. `ucebna` popisuje učebny, `uzivatel` lidi a `rezervace` konkrétní obsazení učebny v čase. Sloupce jsou [[atributy]], řádky jsou n-tice neboli záznamy a doména určuje povolené hodnoty atributu.

Datový typ neurčuje jen způsob zobrazení. Rozhoduje, které hodnoty smí být uloženy a které operace mají význam. Datumový typ lze chronologicky řadit nebo odčítat, zatímco řetězec s datem je pouze text závislý na zvoleném zápisu. Částky je vhodné ukládat jako [[desetinné]] číslo, pokud požadujeme přesný výsledek.

`NULL` není nula ani prázdný text. Označuje hodnotu, která chybí, není známá nebo není použitelná. SQL proto používá tříhodnotovou logiku: pravda, nepravda a neznámo. Zda je hodnota neznámá, zjišťuje podmínka `[[IS NULL]]`, nikoli porovnání `= NULL`; porovnání s neznámou hodnotou nemá obyčejný pravdivostní výsledek.

## Identita záznamu

Kandidátský klíč je nejmenší kombinace atributů, která řádek jednoznačně určí. Z kandidátů návrhář vybere [[primární]] klíč. Často je to stabilní číselný identifikátor nebo UUID, protože jméno i e-mail se mohou v čase změnit. Jiné kandidátské klíče lze dále chránit přes `UNIQUE`.

Vazební tabulka účasti může mít složený primární klíč `(rezervace_id, uzivatel_id)`. Dvojice tak určí přihlášení a současně zabrání tomu, aby se stejný člověk přihlásil na jednu rezervaci dvakrát. Umělý identifikátor není povinný; důležitá je stabilní a jednoznačná identita.

## Vztahy a jejich pravidla

Cizí klíč propojí řádek s řádkem jiné, případně stejné tabulky. `rezervace.ucebna_id` musí odkazovat na existující učebnu, takže databáze umí odmítnout rezervaci neexistující místnosti. Jde o ochranu [[referenční integrity]], ne jen o pomůcku pro dotazování.

U vztahu 1:N patří cizí klíč na stranu „mnoho“: každá rezervace má jednu učebnu, ale učebna může mít rezervací více. Vztah N:M potřebuje vazební tabulku; ta může nést i čas přihlášení nebo roli účastníka. Návrh dále určuje povinnost vztahu: rezervace musí mít organizátora, ale uživatel nemusí mít žádnou rezervaci.

## Model zachycuje i povinnost vztahu

Kardinalita 1:N nebo N:M sama nestačí. Je nutné určit, zda je vazba povinná, nebo volitelná. U rezervace je organizátor povinný, proto jeho odkaz nemá být neznámý. Naproti tomu uživatel může existovat bez jediné rezervace. Tato rozhodnutí se v pozdějším schématu projeví v povolení `NULL`, v cizích klíčích a také v tom, jak budou tabulky spojovány. Dobře navržené tabulky tak neukládají jen hodnoty, ale i důležitá pravidla světa, který databáze popisuje.

Zvolený primární klíč má být [[ stabilní v čase | (jednoznačný a stabilní v čase) | shodný s názvem tabulky ]].

**Vyber správná tvrzení o vztazích:**

<!-- data-randomize="true" -->
[[X]] Vazební tabulka může obsahovat vlastní údaje o vztahu.
[[X]] Cizí klíč může odkazovat i do stejné tabulky.
[[ ]] Vztah N:M se ukládá jako seznam ID v textovém sloupci.
