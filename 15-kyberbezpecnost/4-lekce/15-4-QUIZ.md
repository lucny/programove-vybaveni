<!--
title: Digitální identita, autentizace a hesla – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Na jakou otázku odpovídá identifikace?**

<!-- data-randomize="true" -->
[(X)] Za koho se uživatel vydává?
[( )] Jak uživatel prokáže svou identitu?
[( )] Co smí uživatel po přihlášení dělat?
[( )] Jak se uloží jeho heslo?

---

**2. Co je autentizace?**

<!-- data-randomize="true" -->
[(X)] Ověření, že uživatel je držitelem tvrzené identity.
[( )] Přidělení oprávnění po přihlášení.
[( )] Zadání uživatelského jména bez důkazu.
[( )] Obnova smazaného účtu ze zálohy.

---

**3. Co je autorizace?**

<!-- data-randomize="true" -->
[(X)] Rozhodnutí, které operace smí ověřený uživatel provádět.
[( )] Kontrola hesla nebo bezpečnostního klíče.
[( )] Vytvoření nové identity ve službě.
[( )] Zašifrování přihlašovacího formuláře.

---

**4. Která přiřazení autentizačních faktorů jsou správná?**

<!-- data-randomize="true" -->
[[X]] heslo — něco, co vím
[[X]] telefon — něco, co mám
[[X]] bezpečnostní klíč — něco, co mám
[[X]] otisk prstu — něco, čím jsem
[[ ]] dvě hesla — dva nezávislé faktory
[[ ]] uživatelské jméno — biometrický faktor

---

**5. Proč dvě různá hesla nejsou MFA?**

<!-- data-randomize="true" -->
[(X)] Obě jsou důkazem stejného typu „něco, co vím“. 
[( )] Jedno z hesel musí být vždy biometrické.
[( )] MFA připouští pouze hardwarové klíče.
[( )] Druhé heslo automaticky patří službě.

---

**6. Co je MFA fatigue?**

<!-- data-randomize="true" -->
[(X)] Útočník opakuje potvrzovací výzvy a spoléhá na unavené schválení.
[( )] Uživatel zapomene druhé heslo po pravidelné změně.
[( )] TOTP aplikace přestane generovat kódy.
[( )] Biometrický senzor vybije baterii zařízení.

---

**7. Jaký je důležitý přínos správce hesel?**

<!-- data-randomize="true" -->
[(X)] Generuje a ukládá dlouhá jedinečná hesla pro různé služby.
[( )] Umožňuje bezpečně používat jedno heslo všude.
[( )] Nahrazuje ochranu hlavního účtu.
[( )] Automaticky opraví kompromitovanou službu.

---

**8. Co je credential stuffing?**

<!-- data-randomize="true" -->
[(X)] Zkoušení uniklých dvojic e-mail–heslo na dalších službách.
[( )] Hádání všech možných kombinací znaků.
[( )] Malý počet častých hesel proti mnoha účtům.
[( )] Zachytávání stisků kláves škodlivým programem.

---

**9. Co je password spraying?**

<!-- data-randomize="true" -->
[(X)] Zkoušení několika častých hesel proti mnoha účtům.
[( )] Použití uniklých dvojic z jiné služby.
[( )] Systematické zkoušení všech znakových kombinací u jednoho účtu.
[( )] Odesílání phishingu pomocí QR kódu.

---

**10. Proč je passkey odolnější proti klasickému phishingu?**

<!-- data-randomize="true" -->
[(X)] Je veřejnoklíčový a vázaný na konkrétní službu či doménu.
[( )] Server uchovává soukromý klíč i heslo uživatele.
[( )] Biometrický údaj se posílá webové službě.
[( )] Stejný tajný klíč se zadává na každém webu.


# 2. Interaktivní shrnutí kapitoly

## Kdo jste, jak to prokážete a co smíte

Identifikace je tvrzení identity, například uživatelské jméno. [[Autentizace]] ověřuje důkaz, například heslo nebo bezpečnostní klíč. [[Autorizace]] až potom rozhoduje o oprávněních.

Úspěšné přihlášení [[ (neznamená právo provést libovolnou operaci) | automaticky uděluje roli správce | nahrazuje kontrolu oprávnění u dat ]]. Student může číst vlastní známky, učitel je zapisovat a správce spravovat účty, přestože se všichni autentizovali.

## Nezávislé autentizační faktory

Heslo a PIN představují „něco, co vím“, telefon či bezpečnostní klíč „něco, co mám“ a biometrie „něco, čím jsem“. [[MFA]] kombinuje alespoň dva nezávislé typy. Dvě hesla zůstávají jedním faktorem.

SMS je zpravidla lepší než samotné heslo, TOTP omezuje některé telefonní útoky, ale kód lze stále zadat podvodníkovi. Push výzvy mohou vést k [[MFA fatigue]]. FIDO2/WebAuthn, hardwarové klíče a passkeys používají veřejnoklíčové mechanismy vázané na službu.

**Vyber skutečné kombinace dvou faktorů:**

<!-- data-randomize="true" -->
[[X]] heslo a bezpečnostní klíč
[[X]] PIN a otisk prstu
[[X]] heslo a telefon s TOTP aplikací
[[ ]] heslo a druhé heslo
[[ ]] PIN a bezpečnostní otázka

## Heslo má být dlouhé a jedinečné

Mechanická pravidla mohou vést k předvídatelným heslům typu `Heslo2026!`. Důležitější je délka, jedinečnost a nepředvídatelnost. [[Správce hesel]] vytváří náhodná hesla, takže není nutné recyklovat varianty jednoho vzoru.

Pravidelná změna bez důvodu není sama o sobě cílem. Heslo se musí změnit při podezření na kompromitaci. Slabým článkem může být také [[obnova]] účtu, pokud obejde silné přihlášení jednoduchou otázkou.

## Útoky na hesla a passkeys

Brute force zkouší mnoho kombinací, slovníkový útok častá hesla, [[spraying]] několik hesel proti mnoha účtům a credential stuffing uniklé dvojice na dalších službách. Phishing heslo nehádá a keylogger zachycuje zadávání. Služba může hádání brzdit pomocí [[rate limiting]].

Passkey používá dvojici klíčů. Veřejný klíč má služba, soukromý zůstává u uživatele a podepisuje výzvu. Biometrie nebo PIN jej odemykají místně. Passkey [[ (omezuje phishing, ale stále vyžaduje chránit zařízení a obnovu účtu) | odstraňuje veškerá rizika digitální identity | posílá biometrická data každému serveru ]].
