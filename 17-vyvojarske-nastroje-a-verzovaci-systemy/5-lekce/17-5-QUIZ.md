<!--
title: Verzovací systémy v praxi – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jaký je základní účel verzovacího systému?**

<!-- data-randomize="true" -->
[(X)] Uchovávat historii změn a podporovat práci s verzemi souborů.
[( )] Automaticky kompilovat každý program.
[( )] Nahrazovat veškerou projektovou dokumentaci.
[( )] Spravovat pouze nainstalované knihovny.

---

**2. Jak funguje centrální verzovací systém?**

<!-- data-randomize="true" -->
[(X)] Vývojáři pracují s jedním centrálním repozitářem.
[( )] Každý má povinně pouze lokální historii bez serveru.
[( )] Neumožňuje sdílení změn.
[( )] Ukládá jen poslední verzi souboru.

---

**3. Jaká vlastnost charakterizuje distribuovaný systém?**

<!-- data-randomize="true" -->
[(X)] Každý vývojář má vlastní úplný repozitář a může pracovat offline.
[( )] Historie existuje pouze na jednom serveru.
[( )] Změny nelze mezi vývojáři synchronizovat.
[( )] Systém nepodporuje větve.

---

**4. Co je commit?**

<!-- data-randomize="true" -->
[(X)] Zaznamenaná sada změn s popisem v historii.
[( )] Automaticky vytvořená kopie celého operačního systému.
[( )] Požadavek na instalaci balíčku.
[( )] Spuštěný kontejner aplikace.

---

**5. K čemu slouží větev?**

<!-- data-randomize="true" -->
[(X)] K oddělené práci na změně bez přímého zásahu do hlavní linie.
[( )] K odstranění celé historie projektu.
[( )] K ukládání pouze binárních souborů.
[( )] K automatickému řešení každého konfliktu.

---

**6. Co znamená merge?**

<!-- data-randomize="true" -->
[(X)] Sloučení změn z různých vývojových linií.
[( )] Stažení balíčku z registru.
[( )] Vytvoření testovacího prostředí.
[( )] Překlad kódu do strojových instrukcí.

---

**7. Co zobrazuje diff?**

<!-- data-randomize="true" -->
[(X)] Přesné rozdíly mezi verzemi nebo stavy souborů.
[( )] Pouze seznam uživatelů repozitáře.
[( )] Výkon programu za běhu.
[( )] Strukturu kontejnerového image.

---

**8. Které činnosti podporují týmovou práci s verzemi?**

<!-- data-randomize="true" -->
[[X]] větvení
[[X]] slučování
[[X]] push změn
[[X]] pull změn
[[ ]] mazání historie po každé změně
[[ ]] sdílení jen pomocí snímků obrazovky

---

**9. Jaký je vztah Gitu a GitHubu?**

<!-- data-randomize="true" -->
[(X)] Git je verzovací systém, GitHub platforma pro sdílení repozitářů a spolupráci.
[( )] GitHub je lokální příkaz a Git programovací jazyk.
[( )] Jde o dva názvy stejného souboru.
[( )] Git funguje pouze uvnitř GitHubu.

---

**10. K čemu slouží pull request na platformě typu GitHub?**

<!-- data-randomize="true" -->
[(X)] K návrhu, diskusi a kontrole změn před sloučením.
[( )] K instalaci virtuálního prostředí.
[( )] K překladu aplikace na serveru uživatele.
[( )] K nahrazení všech commitů jedním souborem.


# 2. Interaktivní shrnutí kapitoly

## Historie, ne jen záložní kopie

Verzovací systém zaznamenává, kdo a proč změnil konkrétní soubory. Jednotlivý ucelený záznam se nazývá [[commit]]. Díky historii lze porovnat stavy, dohledat vznik problému nebo se vrátit k dřívější verzi.

Příkaz či zobrazení [[diff]] ukazuje přesné rozdíly. Užitečný commit proto nemá být jen bezejmennou kopií, ale srozumitelnou změnou s odpovídajícím popisem.

## Centrální a distribuovaný model

U centrálního systému, například SVN, je hlavním bodem společný repozitář. Distribuovaný Git dává každému vývojáři [[ (vlastní úplný repozitář s historií) | pouze pracovní soubory bez historie | přístup jen při trvalém připojení ]]. Lokální práce je možná offline a změny se později synchronizují.

## Větve oddělují rozpracované změny

[[Větev]] vytváří samostatnou linii vývoje pro funkci či opravu. Po kontrole lze změny sloučit operací [[merge]]. Pokud různé větve upravily stejné místo neslučitelně, vzniká konflikt a člověk musí určit správný výsledek.

**Vyber funkce verzovacího systému:**

<!-- data-randomize="true" -->
[[X]] historie commitů
[[X]] větvení a slučování
[[X]] porovnávání změn
[[X]] návrat k dřívějšímu stavu
[[ ]] automatické dokazování správnosti programu

Příkazy push a pull přenášejí změny mezi repozitáři. Neznamenají totéž co commit: commit nejprve zaznamená změnu v historii, synchronizace ji [[ (přenáší mezi lokálním a vzdáleným repozitářem) | převádí na test | automaticky schvaluje ]].

## Git a platforma pro spolupráci

Git je samotný distribuovaný verzovací systém. GitHub nebo GitLab nad repozitáři přidávají účty, issues, pull requesty a code review. Pull request umožňuje změnu představit, diskutovat a zkontrolovat před začleněním.

Stejný princip pomáhá jednotlivci, týmu i open-source projektu. Smyslem není jen uchovat soubory, ale vytvořit [[ (dohledatelný a kontrolovatelný vývoj) | jedinou poslední verzi bez kontextu | náhradu testování a dokumentace ]].
