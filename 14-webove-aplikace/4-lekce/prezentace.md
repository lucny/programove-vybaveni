## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**HTTP si uživatele samo nepamatuje**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Každý HTTP požadavek je samostatná zpráva. Přihlášený stav se proto musí propojit pomocí dalšího mechanismu. Klasická webová aplikace často používá **session**: server uchovává stav a prohlížeči dá náhodný identifikátor v cookie. Při dalším požadavku cookie dorazí zpět a server podle identifikátoru najde session.

Cookie má být chráněna vhodnými atributy. `Secure` omezuje přenos na HTTPS, `HttpOnly` brání běžnému JavaScriptu cookie přečíst a `SameSite` omezuje některé cross-site scénáře. Ani správně nastavená cookie však neřeší všechna rizika; například XSS může jménem uživatele provádět akce, i když session cookie kvůli `HttpOnly` přímo nepřečte.

Django má session framework zabudovaný a na něm může stavět autentizaci. Konkrétní backend session se dá měnit; pro mentální model stačí rozlišit **serverový stav relace** a **identifikátor, který prohlížeč posílá**.

***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Autentizace odpovídá „kdo jsi?“, autorizace „co smíš?“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Autentizace** ověřuje identitu. **Autorizace** rozhoduje o oprávnění k operaci nebo zdroji. Přihlášení úspěšně ověřeného studenta neznamená, že může upravovat účty učitelů.

Django poskytuje model uživatele, hashování hesel, přihlášení, skupiny a permissions. Vlastní aplikace může navíc definovat pravidla na úrovni objektu: editor může upravit článek své rubriky, ale ne cizí uzamčený článek.

Častou chybou je kontrola pouze v rozhraní. Tlačítko „Smazat“ se administrátorovi zobrazí a běžnému uživateli skryje, ale endpoint `/article/42/delete` neověří oprávnění. Útočník nepotřebuje tlačítko; požadavek může sestavit ručně. Správné pravidlo proto zní: **UI může funkci skrýt pro pohodlí, backend ji musí zakázat pro bezpečnost**.

***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Hesla, vícefaktorové ověřování a passkeys**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Heslo se na serveru nemá ukládat v čitelné podobě. Ukládá se jeho výsledek z vhodné pomalé funkce pro odvozování hesel se solí. Frameworky jako Django tuto práci řeší za vývojáře a umožňují aktualizovat používaný algoritmus bez změny uživatelského rozhraní.

Vícefaktorové ověřování přidává další faktor, například jednorázový kód nebo hardwarový autentizátor. Moderní **passkeys** založené na WebAuthn používají kryptografický pár klíčů a mohou omezit riziko phishingu, protože přihlašovací údaj je vázán na konkrétní původ služby.

Není správné tvrdit, že **OAuth 2.0** je sám o sobě standard pro „přihlášení Googlem“. OAuth je primárně autorizační rámec pro delegovaný přístup. Pro autentizační identitu se nad ním typicky používá **OpenID Connect — OIDC**. Uživatel tento rozdíl ve formuláři nevidí, pro návrh systému je však zásadní.

Také **JWT** není automaticky „lepší session“. Je to formát podepsaného tokenu s tvrzeními. Může být vhodný v některých distribuovaných API, ale přináší vlastní otázky expirace, odvolání, uložení a velikosti. Pro klasickou serverovou aplikaci je session cookie často jednodušší a bezpečnější výchozí řešení.

# 5. Bezpečnost webové aplikace

***
