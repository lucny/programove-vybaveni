<!--
title: Emulace a virtualizace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je hlavním účelem emulace?**

<!-- data-randomize="true" -->
[(X)] Napodobit chování jiné platformy nebo systému.
[( )] Pouze rozdělit disk na oddíly.
[( )] Synchronizovat soubory mezi zařízeními.
[( )] Zmenšit velikost programu.

---

**2. Co může emulátor napodobovat?**

<!-- data-randomize="true" -->
[[X]] CPU
[[X]] grafiku
[[X]] zvukový čip
[[X]] paměťovou mapu
[[ ]] pouze vzhled ikon

---

**3. Co je Wine podle kapitoly?**

<!-- data-randomize="true" -->
[(X)] Kompatibilní vrstva pro Windows API.
[( )] Kompletní emulátor celého PC.
[( )] Hypervisor typu 1.
[( )] Kontejnerový runtime.

---

**4. Co označuje guest ve virtualizaci?**

<!-- data-randomize="true" -->
[(X)] Virtuální počítač nebo jeho OS.
[( )] Fyzický hostitelský procesor.
[( )] Síťový kabel hypervisoru.
[( )] Pouze obraz instalačního média.

---

**5. Jaké zdroje může mít virtuální stroj?**

<!-- data-randomize="true" -->
[[X]] virtuální CPU
[[X]] virtuální RAM
[[X]] virtuální disk
[[X]] virtuální síťový adaptér
[[ ]] povinně vlastní fyzický monitor

---

**6. Co je hypervisor?**

<!-- data-randomize="true" -->
[(X)] Software řídící virtuální stroje.
[( )] Souborový formát kontejneru.
[( )] Ovladač tiskárny.
[( )] Kompresní algoritmus.

---

**7. Proč snapshot není automaticky plnohodnotná záloha?**

<!-- data-randomize="true" -->
[(X)] Může být závislý na původním virtuálním disku.
[( )] Snapshot vždy smaže původní data.
[( )] Nelze se z něj nikdy vrátit.
[( )] Obsahuje pouze síťové nastavení.

---

**8. Co je typické pro kontejner?**

<!-- data-randomize="true" -->
[(X)] Sdílí jádro hostitelského systému.
[( )] Vždy obsahuje vlastní kernel.
[( )] Musí emulovat jinou CPU architekturu.
[( )] Je totéž co Python venv.

---

**9. Kdy je vhodné použít jednotlivé technologie?**

<!-- data-randomize="true" -->
[[X]] stará konzolová hra — emulace
[[X]] jiný celý operační systém — VM
[[X]] izolace aplikace se závislostmi — kontejner
[[X]] Windows API na Linuxu — Wine
[[ ]] záloha dokumentů — hypervisor

---

**10. Co řeší Python `venv`?**

<!-- data-randomize="true" -->
[(X)] Izolaci balíčků a interpreterových závislostí.
[( )] Hardwarovou virtualizaci celého PC.
[( )] Emulaci jiné architektury CPU.
[( )] Oddělené jádro operačního systému.


# 2. Interaktivní shrnutí kapitoly

## Kompatibilita a emulace

Starší program může očekávat jiné CPU, hardware nebo systémové služby. [[emulace]] napodobuje jinou platformu nebo její části. Emulátor může interpretovat či dynamicky překládat instrukce a napodobovat také grafiku, zvuk nebo časovače.

Wine je [[ klasický emulátor celého Windows PC | (kompatibilní vrstva převádějící Windows API) | virtuální stroj s vlastním kernelem ]]. Rosetta 2 je překladová technologie pro běh x86-64 aplikací na ARM64.

## Virtuální stroje

Fyzický počítač je [[hostitel]], virtuální počítač je guest. VM může mít vlastní virtuální CPU, RAM, disk a síťový adaptér a běžně v něm běží samostatný operační systém.

Software řídící virtuální stroje se nazývá [[hypervisor]]. Type 1 běží přímo nad hardwarem nebo tvoří základ virtualizační platformy, Type 2 nad hostitelským OS.

## Snapshot a virtuální síť

Snapshot zachycuje stav virtuálního stroje a je praktický před experimentem. Není však automaticky dlouhodobou zálohou, protože [[ je vždy samostatnou nezávislou kopií | (může záviset na původním virtuálním disku) | obsahuje pouze nastavení sítě ]].

Virtuální stroje lze propojovat virtuálními [[sítěmi]], používat NAT nebo je od fyzické sítě izolovat.

## Kontejnery

Kontejner není malý virtuální stroj. Typicky sdílí [[kernel]] hostitele a izoluje procesy, souborový systém a síťové prostředí. Díky tomu startuje rychle a má menší režii.

**Vyber správné použití:**

<!-- data-randomize="true" -->
[[X]] historická konzole — emulátor
[[X]] samostatný OS — virtuální stroj
[[X]] distribuovatelná aplikace se závislostmi — kontejner
[[X]] některé Windows aplikace na Linuxu — Wine
[[ ]] izolace Python balíčků — plná hardwarová virtualizace

Python `venv` izoluje hlavně knihovny a [[závislosti]], nikoli celý operační systém.
