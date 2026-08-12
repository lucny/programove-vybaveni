<!--
title: NoSQL databáze – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co znamená NoSQL v kontextu kapitoly?**

<!-- data-randomize="true" -->
[(X)] Skupinu nerelačních modelů, často chápanou jako Not only SQL.
[( )] Databáze bez jakýchkoli pravidel.
[( )] Zákaz dotazovacích jazyků.
[( )] Vždy rychlejší náhradu relačních DB.

---

**2. Co platí o „bezschémové“ dokumentové databázi?**

<!-- data-randomize="true" -->
[(X)] Schéma nezmizelo, část odpovědnosti se přesouvá do aplikace a validace.
[( )] Data nemají žádnou strukturu.
[( )] Každý dokument musí být binárně stejný.
[( )] Nelze kontrolovat typy polí.

---

**3. Jak se obvykle ukládají data v dokumentové databázi?**

<!-- data-randomize="true" -->
[(X)] Jako dokumenty podobné JSON.
[( )] Pouze jako jednotlivé bajty bez polí.
[( )] Výhradně jako grafové hrany.
[( )] Pouze ve fixních relačních řádcích.

---

**4. Pro co je typický key-value model?**

<!-- data-randomize="true" -->
[(X)] Velmi rychlý přístup podle známého klíče.
[( )] Složité ad hoc dotazy přes libovolná pole.
[( )] Výhradně prostorové dotazy.
[( )] Povinné spojování tabulek.

---

**5. Který produkt je v kapitole příkladem key-value databáze?**

<!-- data-randomize="true" -->
[(X)] Redis
[( )] Neo4j
[( )] Cassandra
[( )] PostgreSQL

---

**6. Pro jaký typ zátěže se hodí wide-column databáze typu Cassandra?**

<!-- data-randomize="true" -->
[(X)] Velký objem zápisů a předem známé dotazovací vzory.
[( )] Především složité JOINy mezi mnoha tabulkami.
[( )] Výhradně lokální osobní dokumenty.
[( )] Jen grafické vztahy.

---

**7. Co je hlavní výhodou grafové databáze?**

<!-- data-randomize="true" -->
[(X)] Efektivní procházení složitých vztahů a cest.
[( )] Ukládání pouze obrázků.
[( )] Nahrazení všech relačních databází.
[( )] Automatická anonymizace dat.

---

**8. K čemu se grafové databáze mohou hodit?**

<!-- data-randomize="true" -->
[[X]] doporučování
[[X]] detekce podvodů
[[X]] sociální sítě
[[X]] správa závislostí
[[ ]] pouze tisk dokumentů

---

**9. Co je replikace?**

<!-- data-randomize="true" -->
[(X)] Vytváření kopií dat pro dostupnost a odolnost.
[( )] Rozdělení dat podle klíče mezi uzly.
[( )] Komprese dokumentu.
[( )] Převod grafu na tabulku.

---

**10. Co znamená eventual consistency?**

<!-- data-randomize="true" -->
[(X)] Kopie mohou být dočasně rozdílné, ale bez dalších změn se sjednotí.
[( )] Každá kopie je v každém okamžiku vždy identická.
[( )] Databáze neřeší správnost.
[( )] Data se nikdy nereplikují.


# 2. Interaktivní shrnutí kapitoly

## NoSQL není jedna technologie

NoSQL označuje skupinu nerelačních modelů a často se vykládá jako „Not only SQL“. Neznamená databázi bez [[pravidel]] ani automaticky vyšší výkon.

Pružné schéma neznamená žádné schéma. Význam polí, typy a povinné údaje stále musí hlídat aplikace, validace a správa [[dat]].

## Dokumenty a key-value

Dokumentová databáze ukládá strukturované dokumenty podobné [[JSON]]. Je vhodná tam, kde se záznamy mohou lišit strukturou a aplikace často čte celý dokument.

Key-value databáze funguje jako velký slovník. Pokud známe [[klíč]], získáme hodnotu velmi rychle. Redis se používá například pro cache, relace nebo čítače.

## Wide-column a grafy

Wide-column systémy jako [[Cassandra]] modelují data podle dotazů a dobře škálují vysoký objem zápisů. Nejsou totéž co sloupcové analytické databáze.

Grafová databáze ukládá uzly a [[vztahy]]. Hodí se tam, kde jsou hlavním problémem cesty a vazby mezi objekty.

**Vyber správná použití grafového modelu:**

<!-- data-randomize="true" -->
[[X]] sociální síť
[[X]] doporučování
[[X]] detekce podvodů
[[X]] správa závislostí
[[ ]] jednoduchá cache podle jednoho klíče

## Distribuce a konzistence

[[replikace]] vytváří kopie dat, zatímco sharding neboli partitioning rozděluje data mezi uzly. Při síťovém rozdělení vzniká kompromis mezi dostupností a konzistencí.

Eventual consistency připouští dočasně rozdílné kopie, které se později [[sjednotí]]. Přijatelná úroveň konzistence závisí na významu operace; počet reakcí u příspěvku má jiné požadavky než převod peněz.
