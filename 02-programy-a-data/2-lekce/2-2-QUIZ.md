<!--
title: Systémové a aplikační programy – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Které pořadí nejlépe vystihuje základní softwarové vrstvy?**

<!-- data-randomize="true" -->
[(X)] uživatel → aplikace → operační systém → ovladače → hardware
[( )] hardware → uživatel → aplikace → data → síť
[( )] aplikace → hardware → uživatel → firmware → GUI
[( )] uživatel → firmware → dokument → proces → hardware

---

**2. Co patří mezi úlohy jádra operačního systému?**

<!-- data-randomize="true" -->
[[X]] plánování procesů
[[X]] správa paměti
[[X]] komunikace se zařízeními
[[X]] práce se souborovými systémy
[[ ]] tvorba prezentací

---

**3. Co obecně označuje API?**

<!-- data-randomize="true" -->
[(X)] Definované rozhraní mezi softwarovými částmi.
[( )] Typ fyzického konektoru.
[( )] Formát pevného disku.
[( )] Pouze grafické uživatelské rozhraní.

---

**4. Co je podstatou RTOS?**

<!-- data-randomize="true" -->
[(X)] Časová předvídatelnost reakcí.
[( )] Vždy nejvyšší průměrný výkon.
[( )] Pouze grafické ovládání.
[( )] Spuštění bez operační paměti.

---

**5. Která tvrzení správně rozlišují firmware a ovladač?**

<!-- data-randomize="true" -->
[[X]] Firmware běží v zařízení nebo jeho nevolatilní paměti.
[[X]] Ovladač propojuje zařízení s operačním systémem.
[[X]] Firmware může být aktualizovatelný.
[[ ]] Ovladač je vždy uložen uvnitř tiskárny.
[[ ]] Firmware je synonymum GUI.

---

**6. Co na moderních PC převzalo většinu rolí tradičního BIOSu?**

<!-- data-randomize="true" -->
[(X)] UEFI
[( )] CLI
[( )] DLL
[( )] API

---

**7. Které nástroje mohou být utility?**

<!-- data-randomize="true" -->
[[X]] monitor výkonu
[[X]] správce procesů
[[X]] síťová diagnostika
[[X]] zálohovací nástroj
[[ ]] textový procesor jako hlavní kancelářská aplikace

---

**8. Proč se tradiční defragmentace běžně nepoužívá na SSD stejně jako na HDD?**

<!-- data-randomize="true" -->
[(X)] Flash úložiště má jiné vlastnosti a používá jiné optimalizační mechanismy.
[( )] SSD neobsahuje souborový systém.
[( )] SSD neumí přesouvat data.
[( )] Defragmentace je pouze síťový nástroj.

---

**9. Co může znamenat platforma při posuzování kompatibility programu?**

<!-- data-randomize="true" -->
[[X]] operační systém
[[X]] procesorová architektura
[[X]] runtime nebo knihovny
[[X]] grafické API
[[ ]] pouze název výrobce monitoru

---

**10. Co v Semantic Versioning typicky znamená část PATCH?**

<!-- data-randomize="true" -->
[(X)] Kompatibilní opravy.
[( )] Změnu procesorové architektury.
[( )] Vždy placený upgrade.
[( )] Úplné ukončení podpory.


# 2. Interaktivní shrnutí kapitoly

## Software jako vrstvy

Aplikace obvykle neovládá hardware přímo. Typický řetězec je **uživatel → aplikace → operační systém → [[ovladače]] → hardware**. Vrstvení umožňuje aplikaci používat služby nižších vrstev bez znalosti detailů konkrétního zařízení.

Systémový software vytváří prostředí pro provoz počítače; aplikační software řeší konkrétní [[úlohy]] uživatele.

## Operační systém

Nejdůležitější část OS je [[kernel]]. Spravuje procesy, paměť, zařízení, souborové systémy, ochranu a část síťových funkcí. Aplikace využívají systémové služby přes definovaná rozhraní, tedy [[API]].

GUI využívá grafické prvky, zatímco [[CLI]] pracuje s textovými příkazy. CLI není zastaralé; je důležité pro automatizaci, správu serverů a vývoj.

RTOS se od běžného systému liší hlavně důrazem na [[ maximální takt procesoru | (časovou předvídatelnost) | grafickou kvalitu ]].

## Firmware a ovladače

Ovladač umožňuje operačnímu systému komunikovat s konkrétním hardwarem. [[firmware]] je software uložený přímo v zařízení a řídí jeho základní chování. Moderní PC při startu většinou používají [[UEFI]].

**Vyber správné role:**

<!-- data-randomize="true" -->
[[X]] firmware — zná základní chování zařízení
[[X]] ovladač — propojuje hardware s OS
[[X]] OS — poskytuje služby aplikacím
[[ ]] GUI — nahrazuje firmware
[[ ]] aplikace — řídí vždy přímo elektrické signály zařízení

## Utility, aplikace a kompatibilita

Utility slouží ke správě, diagnostice a údržbě. Jejich použití musí odpovídat skutečnému problému; například neověřené „čističe“ systému mohou více škodit než pomoci.

Aplikační software zahrnuje kancelářské, grafické, multimediální, komunikační i podnikové nástroje. Dnešní aplikace mohou mít webového, desktopového i mobilního klienta a serverový [[backend]].

Kompatibilita závisí na platformě. Program pro x86-64 nemusí přímo běžet na [[ARM64]]. Verze software mohou používat schémata jako Semantic Versioning `MAJOR.MINOR.PATCH`, ale jen pokud se projekt k tomuto pravidlu skutečně hlásí.
