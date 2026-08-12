<!--
title: Ochrana dat a kryptografie – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co jsou data at rest?**

<!-- data-randomize="true" -->
[(X)] Data uložená na disku, v databázi nebo záloze.
[( )] Data putující sítí mezi zařízeními.
[( )] Data právě používaná v operační paměti.
[( )] Data zničená po skončení procesu.

---

**2. Co chrání TLS při použití HTTPS?**

<!-- data-randomize="true" -->
[(X)] Přenos, jeho integritu a ověření identity serveru certifikátem.
[( )] Data na odcizeném vypnutém disku.
[( )] Každý soubor před chybou uživatele.
[( )] Úplnou anonymitu všech komunikujících stran.

---

**3. Co je packet sniffing?**

<!-- data-randomize="true" -->
[(X)] Zachytávání síťových paketů, které může být legitimní i zneužité.
[( )] Automatické šifrování každého souboru.
[( )] Hádání hesel pomocí slovníku.
[( )] Podepisování hashe soukromým klíčem.

---

**4. Jak funguje symetrické šifrování?**

<!-- data-randomize="true" -->
[(X)] Stejný tajný klíč šifruje i dešifruje.
[( )] Veřejný klíč šifruje a stejný veřejný klíč dešifruje.
[( )] Nepoužívá žádný klíč.
[( )] Vytváří pouze nevratný hash.

---

**5. Proč se používá hybridní kryptografie?**

<!-- data-randomize="true" -->
[(X)] Kombinuje veřejnoklíčové vytvoření tajemství s rychlým symetrickým přenosem.
[( )] Dvakrát zašifruje data stejným heslem.
[( )] Nahrazuje certifikáty kontrolním součtem.
[( )] Používá hash místo všech šifrovacích klíčů.

---

**6. Proč hash není šifrování?**

<!-- data-randomize="true" -->
[(X)] Není určen k pozdějšímu získání původního vstupu dešifrováním.
[( )] Nemůže mít výstup pevné délky.
[( )] Vždy používá veřejný a soukromý klíč.
[( )] Slouží pouze k utajení síťového provozu.

---

**7. Proč není hash matematicky unikátní pro každý možný vstup?**

<!-- data-randomize="true" -->
[(X)] Vstupů je více než hodnot výstupu pevné délky, takže kolize existují.
[( )] Hash se při každém výpočtu náhodně mění.
[( )] Každý vstup vytváří dva různé hashe.
[( )] Hashovací funkce uchovává celý původní soubor.

---

**8. Které postupy jsou vhodné pro ukládání hesel?**

<!-- data-randomize="true" -->
[[X]] Argon2, scrypt nebo bcrypt
[[X]] náhodný salt pro každé heslo
[[X]] záměrně náročný password hashing
[[ ]] otevřený text
[[ ]] samotný rychlý SHA-256

---

**9. Jaký je rozdíl mezi TLS a E2EE?**

<!-- data-randomize="true" -->
[(X)] TLS chrání spojení k serveru, E2EE obsah až mezi zařízeními odesílatele a příjemce.
[( )] TLS vždy skrývá všechna metadata, E2EE žádná data nešifruje.
[( )] E2EE používá pouze jeden serverový klíč.
[( )] Mezi nimi není rozdíl v tom, kdo může obsah dešifrovat.

---

**10. Co propojuje digitální certifikát?**

<!-- data-randomize="true" -->
[(X)] Veřejný klíč s určitou identitou.
[( )] Soukromý klíč s otevřeným heslem.
[( )] Hash souboru s jeho záložní kopií.
[( )] Symetrický klíč s každým uživatelem internetu.


# 2. Interaktivní shrnutí kapitoly

## Data mění stav i způsob ochrany

Data v klidu leží na disku či v záloze, data při přenosu putují sítí a data při zpracování používá program v paměti. Šifrování disku chrání zejména odcizené úložiště, [[TLS]] síťovou komunikaci a přístupová práva s izolací data při práci.

Packet sniffing je zachytávání paketů; nástroj jako Wireshark může sloužit legitimní diagnostice. MitM se snaží komunikaci číst nebo měnit. Platně ověřené HTTPS [[ (takový zásah výrazně komplikuje) | automaticky skryje všechna metadata | chrání data i po jejich dešifrování aplikací ]].

## Dva modely šifrování

Symetrické šifrování používá stejný tajný klíč a je rychlé pro velká data; příkladem je [[AES]]. Problémem je bezpečné předání klíče. Asymetrická kryptografie používá veřejný a [[soukromý]] klíč a umožňuje autentizaci nebo vytvoření společného tajemství.

Asymetrický přístup není jednoduše „bezpečnější“, má jiné vlastnosti a vyšší výpočetní náklady. Hybridní kryptografie [[ (spojí veřejnoklíčový mechanismus s rychlým symetrickým přenosem) | používá dva totožné tajné klíče | nahrazuje šifrování hashem ]].

**Vyber správná tvrzení o kryptografii:**

<!-- data-randomize="true" -->
[[X]] AES je symetrická šifra
[[X]] veřejný klíč lze zveřejnit
[[X]] soukromý klíč musí zůstat chráněný
[[X]] TLS běžně kombinuje více kryptografických mechanismů
[[ ]] asymetrická kryptografie je vždy rychlejší pro velká data

## Hash, hesla a salt

Hashovací funkce převádí libovolně dlouhý vstup na výstup pevné délky. Není určena k dešifrování. Kolize matematicky existují; bezpečná funkce má jejich cílené nalezení učinit prakticky obtížným. Změna souboru se projeví jiným kontrolním [[hashem]].

Hesla se neukládají otevřeně ani pouhým rychlým SHA-256. Argon2, scrypt a bcrypt zpomalují hromadné zkoušení. Náhodný [[salt]] zajistí, že stejné heslo různých uživatelů nemá stejný uložený výsledek.

## Přenos, podpis a identita klíče

TLS chrání spojení ke konkrétnímu serveru. [[E2EE]] šifruje obsah na zařízení odesílatele a dešifruje až u příjemce, přesto mohou zůstat metadata. Nestačí tedy tvrzení „používáme šifrování“; je nutné zjistit, kde jsou klíče a kdo může obsah číst.

Digitální podpis obvykle podepisuje hash dokumentu soukromým klíčem. Veřejný klíč ověřuje integritu a vazbu na držitele klíče; [[certifikát]] propojuje veřejný klíč s identitou v PKI. Technický digitální podpis není automaticky totéž co právní elektronický podpis a kvalifikovaný [[QES]] má v EU zvláštní právní účinek.
