# Instrukce pro tvorbu interaktivních kvízů v LiaScriptu

## 1. Účel

Pro každou kapitolu výukového dokumentu vytvoř samostatný soubor kvízu ve formátu Markdown pro LiaScript.

Název souboru má tvar:

`[číslo-okruhu]-[číslo-kapitoly]-QUIZ.md`

Například:

`2-1-QUIZ.md`

Kvíz musí vycházet pouze z obsahu příslušné kapitoly zdrojového výukového dokumentu. Nezaváděj pojmy, fakta ani formulace, které zdrojová kapitola nepodporuje.

---

## 2. Povinná struktura souboru

Každý kvíz má dvě hlavní části:

```markdown
# 1. Testovací část

...

# 2. Interaktivní shrnutí kapitoly

...
```

Na začátku lze použít metadata:

```markdown
<!--
title: [název kapitoly] – kvíz
language: cs
-->
```

---

# 3. První část: deset testovacích úloh

První část musí obsahovat přesně **10 otázek**.

Používej pouze:

- single-choice otázky s radiobuttony,
- multiple-choice otázky s checkboxy.

Nepoužívej v této části textové vstupy, dropdowny, přiřazování ani jiné typy úloh.

## 3.1 Single-choice

Syntaxe:

```markdown
**1. Co je...?**

<!-- data-randomize="true" -->
[( )] nesprávná možnost
[(X)] správná možnost
[( )] nesprávná možnost
[( )] nesprávná možnost
```

Každá single-choice otázka má právě jednu správnou odpověď.

## 3.2 Multiple-choice

Syntaxe:

```markdown
**2. Která tvrzení jsou správná?**

<!-- data-randomize="true" -->
[[X]] správná možnost
[[X]] správná možnost
[[ ]] nesprávná možnost
[[ ]] nesprávná možnost
```

Multiple-choice otázka má obvykle 2–5 správných odpovědí a nejméně jeden věrohodný distraktor.

## 3.3 Náhodné pořadí odpovědí

Před každou otázku vlož:

```html
<!-- data-randomize="true" -->
```

LiaScript pak při novém načtení promíchá pořadí možností.

Tím se omezuje zapamatování polohy správné odpovědi.

---

# 4. Zásady konstrukce testových úloh

## 4.1 Pokrytí kapitoly

Deset otázek má společně pokrýt hlavní části celé kapitoly.

Nevytvářej deset variant stejné definice. Kombinuj:

- základní pojmy,
- vztahy mezi pojmy,
- princip fungování,
- rozlišení podobných pojmů,
- praktické použití,
- důsledky určitého nastavení nebo volby,
- jednoduchý výpočet, pokud je v kapitole podstatný,
- bezpečnostní nebo provozní souvislost, pokud ji kapitola obsahuje.

## 4.2 Vyvážené distraktory

Správná odpověď nesmí být snadno odhalitelná podle formy.

Zejména:

- správná odpověď nemá být systematicky nejdelší,
- nesprávné možnosti nemají být očividně absurdní,
- všechny možnosti mají mít podobnou gramatickou strukturu,
- vyhýbej se nápovědě typu „vždy“, „nikdy“, „pouze“ tam, kde z ní lze správnost snadno odhadnout,
- nepoužívej jednu velmi přesnou dlouhou správnou větu vedle tří krátkých vágních distraktorů.

Příklad nevhodný:

```markdown
[( )] hardware
[( )] internet
[(X)] operační systém, který spravuje procesy, paměť, zařízení, soubory a poskytuje aplikacím systémové služby
[( )] aplikace
```

Lepší:

```markdown
[( )] Spravuje pouze uživatelské dokumenty.
[(X)] Spravuje zdroje a poskytuje služby aplikacím.
[( )] Nahrazuje ovladače všech zařízení.
[( )] Slouží hlavně jako kancelářská aplikace.
```

## 4.3 Přesnost formulací

Nevytvářej odborně nepřesné zkratky jen kvůli jednoduchosti otázky.

Pokud zdroj výslovně opravuje běžný mýtus nebo zjednodušení, kvíz má tuto přesnost zachovat.

Například:

- samotná přípona neurčuje skutečný obsah souboru,
- synchronizace není automaticky záloha,
- kontejnery nejsou totéž co virtuální stroje,
- Unicode není totéž co UTF-8,
- PPI není totéž co DPI,
- ISO u digitální fotografie samo nepřidává fotony,
- NoSQL neznamená „bez pravidel“,
- vektorový obraz se při zobrazení na monitoru rasterizuje.

---

# 5. Druhá část: interaktivní shrnutí kapitoly

Druhá část je **souvislý studijní text**, který shrnuje podstatné znalosti dané kapitoly.

Nemá působit jako další seznam izolovaných otázek.

Text rozděl do přibližně **3–6 krátkých tematických oddílů** pomocí podnadpisů:

```markdown
## Základní princip

...

## Praktické použití

...
```

Odrážky používej jen tam, kde přirozeně zpřehledňují skupinu prvků. Většinu výkladu ponech v souvislých větách.

---

# 6. Interaktivní prvky ve shrnutí

Používej tři typy interakce.

## 6.1 Dropdown pro významovou volbu

Delší formulace a vztahy mezi pojmy řeš výběrovým seznamem:

```markdown
Operační systém [[ pouze ukládá dokumenty | (spravuje zdroje a poskytuje služby aplikacím) | nahrazuje veškerý aplikační software ]].
```

Správná možnost je v kulatých závorkách.

Dropdown je vhodný pro:

- definici v kontextu věty,
- příčinu a důsledek,
- porovnání dvou technologií,
- správnou interpretaci jevu,
- výběr správného postupu.

Možnosti mají být významově věrohodné a pokud možno podobně dlouhé.

## 6.2 Krátký textový vstup

Pro opravdu důležité pojmy, zkratky nebo krátké hodnoty používej:

```markdown
Nejdůležitější část operačního systému se nazývá [[kernel]].
```

Do textového pole vybírej především:

- jednoslovné pojmy,
- zkratky,
- jednoduchá čísla,
- velmi krátké jednoznačné termíny.

Vhodné příklady:

`[[kernel]]`  
`[[UEFI]]`  
`[[metadata]]`  
`[[snapshot]]`  
`[[PPI]]`  
`[[RGB]]`  
`[[SLAM]]`  
`[[OLAP]]`

Nevhodné jsou dlouhé věty nebo několikaslovné formulace. Dlouhá odpověď se do nativního textového pole LiaScriptu nevejde pohodlně a zhoršuje čitelnost.

## 6.3 Samostatná multiple-choice vložka

Checkboxy lze použít i uvnitř shrnutí, ale pouze jako **skutečnou samostatnou otázku**.

Například:

```markdown
**Vyber všechny součásti informačního systému:**

<!-- data-randomize="true" -->
[[X]] lidé
[[X]] procesy
[[X]] data
[[X]] software
[[X]] infrastruktura
[[ ]] pouze databáze
```

Nikdy nezapisuj pouhý seznam takto:

```markdown
- [[hardware]]
- [[software]]
- [[data]]
```

LiaScript by tyto položky interpretoval jako jednu checkboxovou otázku, i když nejsou označeny správné odpovědi.

Pokud chceš pouze textový vstup v odrážce, raději formuluj větu mimo souvislý blok checkboxů nebo použij jinou konstrukci.

---

# 7. Rozsah shrnutí

Shrnutí má být kratší než původní kapitola, ale musí zachovat její hlavní výukovou osu.

Doporučený rozsah:

- přibližně 500–900 slov podle složitosti kapitoly,
- 3–6 podnadpisů,
- přibližně 8–15 interaktivních míst,
- z toho většina dropdownů a krátkých textových vstupů,
- nejvýše 1–2 samostatné checkboxové vložky.

Nevytvářej interakci v každé větě. Text musí zůstat čitelný i jako výklad.

---

# 8. Co má být v textových polích

Textová pole vybírej jen pro pojmy, které si má student aktivně vybavit.

Upřednostňuj:

- názvy principů,
- odborné termíny,
- zkratky,
- standardní názvy technologií,
- jednoduché hodnoty.

Nevkládej do textového pole obecná slova typu „systém“, „program“, „správně“, pokud nejsou v dané kapitole skutečně klíčovým termínem.

Textové pole nemá zkoušet pravopis celé věty, ale aktivní vybavení podstatného pojmu.

---

# 9. Styl a jazyk

- Piš česky.
- Zachovej odbornou terminologii zdrojového dokumentu.
- Používej přirozené, čitelné věty.
- Nevkládej metakomunikaci typu „jak jsme se učili“.
- Nevysvětluj v souboru syntaxi LiaScriptu.
- Nepoužívej zbytečně mnoho odrážek.
- Neopakuj stejnou otázku v testu a shrnutí doslova.
- Odpovědi nemají být triviální podle délky nebo stylistického tónu.
- Pokud může mít termín více významů, formuluj kontext tak, aby byla odpověď jednoznačná.

---

# 10. Kontrola před uložením

Před dokončením každého souboru ověř:

1. Soubor obsahuje přesně 10 otázek v první části.
2. V první části jsou jen single-choice a multiple-choice úlohy.
3. Před každou otázkou je `data-randomize="true"`.
4. Každá single-choice otázka má právě jednu správnou odpověď.
5. Každá multiple-choice otázka má nejméně jednu správnou a jednu nesprávnou odpověď.
6. Správné odpovědi nejsou nápadně delší než distraktory.
7. Druhá část je skutečné shrnutí kapitoly, nikoli jen seznam otázek.
8. Textové vstupy obsahují krátké, nejlépe jednoslovné odpovědi.
9. Delší odpovědi jsou řešeny dropdownem.
10. Checkboxy uvnitř shrnutí tvoří samostatnou platnou otázku s `[[X]]` a `[[ ]]`.
11. Kvíz nepoužívá fakta, která nejsou ve zdrojové kapitole.
12. Název souboru odpovídá schématu `[okruh]-[kapitola]-QUIZ.md`.

---

# 11. Vzor výsledné struktury

```markdown
<!--
title: Název kapitoly – kvíz
language: cs
-->

# 1. Testovací část

**1. Otázka...**

<!-- data-randomize="true" -->
[( )] možnost A
[(X)] možnost B
[( )] možnost C
[( )] možnost D

---

**2. Otázka s více správnými odpověďmi...**

<!-- data-randomize="true" -->
[[X]] správná možnost
[[X]] správná možnost
[[ ]] distraktor
[[ ]] distraktor

---

... celkem 10 úloh ...


# 2. Interaktivní shrnutí kapitoly

## První tematický blok

Souvislý výklad s [[krátkým]] textovým vstupem a s dropdownem
[[ chybná možnost | (správná významová formulace) | jiná chybná možnost ]].

## Druhý tematický blok

Další souvislý výklad.

**Vyber správné prvky:**

<!-- data-randomize="true" -->
[[X]] správný prvek
[[X]] správný prvek
[[ ]] distraktor

## Třetí tematický blok

Závěrečné propojení klíčových pojmů.
```

Tuto strukturu zachovávej konzistentně ve všech kapitolách a tematických okruzích.
