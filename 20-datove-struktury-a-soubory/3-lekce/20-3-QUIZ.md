<!--
title: Regulární výrazy – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je regulární výraz?**

<!-- data-randomize="true" -->
[(X)] Vzor popisující množinu řetězců.
[( )] Konkrétní textový soubor s jedním řádkem.
[( )] Programovací jazyk pro databáze.
[( )] Dynamické pole znaků.

---

**2. K čemu lze regex použít?**

<!-- data-randomize="true" -->
[[X]] vyhledávání podle vzoru
[[X]] validace formátu
[[X]] extrakce částí textu
[[X]] nahrazování textu
[[ ]] dokazování významové správnosti všech dat
[[ ]] kompilace zdrojového kódu

---

**3. Co v regulárním výrazu obvykle znamená tečka?**

<!-- data-randomize="true" -->
[(X)] Libovolný znak.
[( )] Konec řetězce.
[( )] Přesně jednu číslici.
[( )] Doslovnou tečku za všech okolností.

---

**4. Co označují ^ a $?**

<!-- data-randomize="true" -->
[(X)] Začátek a konec řetězce.
[( )] Jednu nebo více číslic.
[( )] Alternativu dvou vzorů.
[( )] Skupinu bílých znaků.

---

**5. Jaký význam má kvantifikátor +?**

<!-- data-randomize="true" -->
[(X)] Jeden nebo více výskytů.
[( )] Nula nebo více výskytů.
[( )] Nula nebo jeden výskyt.
[( )] Přesně dva výskyty.

---

**6. Co odpovídá zápisu \d?**

<!-- data-randomize="true" -->
[(X)] Číslice.
[( )] Bílý znak.
[( )] Písmeno bez číslic.
[( )] Konec řádku.

---

**7. Co vyjadřuje {3,5}?**

<!-- data-randomize="true" -->
[(X)] Tři až pět opakování předchozího prvku.
[( )] Třetí nebo pátý znak řetězce.
[( )] Rozsah číslic od 3 do 5.
[( )] Pět skupin po třech znacích.

---

**8. Která funkce modulu re hledá první výskyt kdekoliv v textu?**

<!-- data-randomize="true" -->
[(X)] re.search.
[( )] re.findall.
[( )] re.sub.
[( )] re.match.

---

**9. K čemu slouží re.findall?**

<!-- data-randomize="true" -->
[(X)] Vrátí všechny nalezené shody.
[( )] Nahradí každou shodu.
[( )] Ověří pouze začátek a nic nevrátí.
[( )] Zkompiluje celý Python program.

---

**10. Proč používat složité regulární výrazy uvážlivě?**

<!-- data-randomize="true" -->
[(X)] Mohou zhoršit čitelnost a údržbu kódu.
[( )] Neumějí pracovat s textem.
[( )] Vždy jsou pomalejší než ruční kontrola.
[( )] Nelze je dokumentovat komentářem.


# 2. Interaktivní shrnutí kapitoly

## Vzor místo konkrétního textu

Regulární výraz nepopisuje jen jeden řetězec, ale množinu textů odpovídajících pravidlu. Lze jím hledat, ověřovat formát, extrahovat části nebo nahrazovat shody. Zkráceně se používá označení [[regex]].

Validace regexem kontroluje strukturu, například rozmístění číslic a pomlček. Sama však nemusí ověřit význam údaje; formálně správné datum může stále obsahovat [[ (nesmyslnou kalendářní hodnotu) | vždy platný den | automaticky správné časové pásmo ]].

## Stavební znaky vzoru

Literál odpovídá sám sobě, tečka běžně libovolnému znaku. `^` kotví [[začátek]] a `$` konec řetězce. Třída `[0-9]` nebo zkratka [[\d]] označuje číslici, `\w` alfanumerický znak a `\s` bílý znak.

Kvantifikátory řídí opakování: `*` nula a více, `+` jeden a více, `?` nula nebo jeden. `{n}` žádá přesný počet a `{n,m}` interval.

**Vyber správné významy konstrukcí:**

<!-- data-randomize="true" -->
[[X]] [abc] — jeden ze znaků a, b, c
[[X]] a|b — alternativa a nebo b
[[X]] \d{3} — právě tři číslice
[[X]] ^text — text na začátku řetězce
[[ ]] + — žádný nebo jeden výskyt

## Operace modulu re

Pythonový modul [[re]] nabízí `search` pro první shodu kdekoliv, `findall` pro všechny shody, `match` pro kontrolu od začátku a `sub` pro nahrazení podle vzoru. Objekt shody zpřístupňuje nalezený text metodou `group()`.

Rozdíl mezi `search` a `match` je podstatný: `match` začíná na počátku řetězce, `search` může shodu najít [[ (kdekoli v textu) | pouze na posledním znaku | jen v seznamu čísel ]]. Kotvy dovolují požadavek ještě zpřesnit.

## Síla a čitelnost

Regex je vhodný pro logy, čištění dat, editory, anonymizaci či kontrolu formátu. Příliš složitý vzor však může být hůře pochopitelný než několik běžných operací. Složitější výrazy je proto vhodné [[ (dokumentovat a testovat na hraničních případech) | přijmout bez vysvětlení | používat pro každý textový problém ]].
