<!--
title: Závislosti, virtuální prostředí a kontejnery – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je softwarová závislost?**

<!-- data-randomize="true" -->
[(X)] Knihovna, balíček nebo modul potřebný pro aplikaci.
[( )] Každý uživatelský dokument projektu.
[( )] Pouze operační paměť počítače.
[( )] Historie změn ve verzovacím systému.

---

**2. Který nástroj spravuje balíčky Pythonu?**

<!-- data-randomize="true" -->
[(X)] pip.
[( )] npm.
[( )] Git.
[( )] Selenium.

---

**3. Který soubor běžně uvádí závislosti Python projektu?**

<!-- data-randomize="true" -->
[(X)] requirements.txt.
[( )] package.json.
[( )] docker-compose.yml.
[( )] README.exe.

---

**4. Který soubor popisuje závislosti a údaje projektu Node.js?**

<!-- data-randomize="true" -->
[(X)] package.json.
[( )] requirements.txt.
[( )] Dockerfile.py.
[( )] index.uml.

---

**5. Proč se používá virtuální prostředí?**

<!-- data-randomize="true" -->
[(X)] Odděluje interpreter a knihovny jednotlivého projektu.
[( )] Sdílí vždy jednu verzi všech knihoven mezi projekty.
[( )] Nahrazuje zdrojový kód aplikace.
[( )] Vytváří fyzický virtuální procesor.

---

**6. Které přínosy má izolace závislostí?**

<!-- data-randomize="true" -->
[[X]] omezení konfliktů verzí
[[X]] snazší reprodukce prostředí
[[X]] bezpečnější práce na více projektech
[[ ]] automatická oprava logických chyb
[[ ]] zrušení potřeby testů

---

**7. Co popisuje Dockerfile?**

<!-- data-randomize="true" -->
[(X)] Postup vytvoření Docker image.
[( )] Seznam commitů v repozitáři.
[( )] Pouze síťové adresy uživatelů.
[( )] Zdrojový kód orchestrace Kubernetes.

---

**8. K čemu slouží Docker Compose?**

<!-- data-randomize="true" -->
[(X)] K definici a spuštění více spolupracujících kontejnerů.
[( )] K překladu Pythonu do JavaScriptu.
[( )] K vytváření UML diagramů.
[( )] K testování jednoho regulárního výrazu.

---

**9. Jakou úlohu má Kubernetes?**

<!-- data-randomize="true" -->
[(X)] Orchestrace, správa a škálování kontejnerů.
[( )] Editace zdrojového kódu v terminálu.
[( )] Správa dokumentace v Markdownu.
[( )] Překlad aplikace do bytecode.

---

**10. Jaký je vztah image a kontejneru?**

<!-- data-randomize="true" -->
[(X)] Image je připravený obraz, z něhož se spouští kontejner.
[( )] Kontejner je zdrojový text pro vytvoření image.
[( )] Jde o dva názvy virtuálního prostředí Pythonu.
[( )] Image je vždy běžící instance databáze.


# 2. Interaktivní shrnutí kapitoly

## Projekt stojí i na cizím kódu

Závislosti jsou knihovny, balíčky a moduly, bez nichž aplikace nefunguje. Správce balíčků je instaluje a eviduje: Python používá [[pip]], Node.js [[npm]]. Seznam požadovaných verzí umožňuje prostředí znovu sestavit na jiném počítači.

V Pythonu se běžně používá `requirements.txt`, v Node.js [[package.json]]. Neuvedená nebo odlišná verze může změnit chování aplikace, i když její vlastní zdrojový kód zůstal stejný.

## Virtuální prostředí odděluje projekty

Dva projekty mohou vyžadovat různé verze stejné knihovny. Virtuální prostředí proto vytváří izolovaný interpreter a adresář balíčků pro konkrétní projekt. Nástroje `venv` či `virtualenv` [[ (izolují závislosti projektu) | balí všechny služby do kontejnerů | nahrazují verzovací systém ]].

**Co pomáhá k reprodukovatelnému vývojovému prostředí?**

<!-- data-randomize="true" -->
[[X]] evidované verze závislostí
[[X]] oddělené virtuální prostředí
[[X]] sdílený popis instalace projektu
[[ ]] ruční instalace náhodných nejnovějších verzí
[[ ]] vynechání údajů o použitém interpreteru

## Kontejner přenáší širší prostředí

Docker image vzniká podle souboru [[Dockerfile]] a obsahuje připravenou aplikaci s potřebným prostředím. Z image se spouští izolovaný [[kontejner]]. Díky stejnému obrazu může aplikace běžet konzistentně ve vývoji i při nasazení.

Image je tedy předloha, kontejner její běžící instance. Izolace kontejneru je širší než běžné virtuální prostředí Pythonu; neslouží jen k oddělení balíčků jednoho jazyka.

## Více služeb jako celek

Webová aplikace může potřebovat aplikační server i databázi. Docker Compose popíše více kontejnerů v `docker-compose.yml` a spustí je společně. [[Kubernetes]] řeší orchestrace ve větším měřítku: rozmísťování, správu a škálování kontejnerů.

Jednotlivé nástroje proto řeší různé vrstvy: správce balíčků instaluje knihovny, virtuální prostředí izoluje projekt, Docker balí běhové prostředí a orchestrátor [[ (spravuje více běžících kontejnerů) | upravuje syntaxi zdrojového jazyka | nahrazuje testy aplikace ]].
