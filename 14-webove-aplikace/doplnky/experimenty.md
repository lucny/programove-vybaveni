<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Praktická a bezpečně vedená laboratoř k tématu webové aplikace.
-->

# Laboratoř: webové aplikace v praxi

> **Upozornění ke zdrojům:** Následující praktické úlohy, zvolené nástroje a podrobné postupy rozšiřují teoretický základ kurzu o externí znalosti. Nejsou doslovným přepisem zdrojových textů. Pokud se rozhraní některého nástroje mezitím změní, ověřte si jeho aktuální dokumentaci a popište, co jste museli upravit.

## Jak budeme pracovat

Tato laboratoř není návodem k testování cizích webů. Pozorujeme pouze **vlastní prohlížeč**, veřejná testovací API a vlastní lokální soubory. Nikdy neměňte URL, identifikátory, cookies ani formulářová data cizí služby za účelem získání přístupu k datům nebo účtu, které vám nepatří.

Každý experiment odevzdejte stručným zápisem v tomto formátu:

```text
Experiment:
Co jsem udělal/a:
Co jsem pozoroval/a:
Vysvětlení principu:
Jedno bezpečnostní nebo provozní poučení:
```

### Výchozí pojmy

- **Klient** je prohlížeč či mobilní aplikace uživatele.
- **Server** přijímá požadavky a vrací odpovědi.
- **HTTP** je protokol, kterým si klient a server vyměňují zprávy.
- **API** je rozhraní, přes které program žádá jiný program o data nebo akci.
- **Nedůvěryhodný vstup** je vše, co aplikace dostane zvenčí: formulář, URL, soubor, cookie, odpověď API i text vytvořený AI.

[[ Které tvrzení nejlépe vystihuje bezpečnou práci v této laboratoři? ]]

[( )] Je v pořádku zkoušet libovolné identifikátory objednávek, pokud jen čtu data.
[(X)] Používám testovací služby, vlastní data a pozorování vlastního prohlížeče.
[( )] DevTools dovolují obcházet oprávnění backendu.

---

## 1. Architektura webové aplikace

### Cíl kapitoly

Rozlišíte HTML dokument, běh JavaScriptu v prohlížeči a serverovou část aplikace. Naučíte se číst základní HTTP požadavek a odpověď.

### 1.1 HTTP vrstvy a hlavičky v DevTools

**Nástroj:** Chrome, Edge nebo Firefox; vývojářské nástroje (`F12`).

1. Otevřete `https://example.com`.
2. Stiskněte `F12`, otevřete panel **Network / Síť** a stránku obnovte (`Ctrl+R`).
3. Vyberte první požadavek typu **document** (obvykle `example.com`).
4. V části **Headers / Hlavičky** najděte:
   - request URL a HTTP metodu (nejspíš `GET`),
   - stavový kód (`200` znamená úspěch),
   - hlavičku `Content-Type`,
   - v panelu **Response / Odpověď** samotný text vrácený serverem.
5. Do zápisu opište jednu request a jednu response hlavičku a vlastními slovy vysvětlete jejich roli.

> **Pozorování:** Prohlížeč neobdrží „hotovou aplikaci“ jako abstraktní objekt. Dostává konkrétní HTTP odpovědi: HTML, CSS, skripty, obrázky a případně data z API.

[[ Co obvykle určuje hlavička `Content-Type`? ]]

[( )] Kdo smí odpověď číst.
[(X)] Jaký typ obsahu server posílá, například `text/html` nebo `application/json`.
[( )] Jak dlouhé bude heslo uživatele.

### 1.2 Požadavek na API bez HTML

**Nástroj:** [Hoppscotch](https://hoppscotch.io/) nebo přímo prohlížeč.

1. Otevřete Hoppscotch.
2. Zvolte metodu **GET** a vložte `https://jsonplaceholder.typicode.com/posts/1`.
3. Klikněte na **Send**.
4. Určete stavový kód, typ odpovědi a alespoň tři klíče JSON objektu.
5. Porovnejte výsledek s běžnou webovou stránkou: kde jsou barvy, rozložení a tlačítka? Proč je API neposílá?

> **Závěr:** API typicky vrací data. O podobě rozhraní rozhoduje klientská aplikace. Backend však stále rozhoduje, jaká data a které operace v odpovědi povolí.

### 1.3 Rozdělení odpovědností MVC

**Nástroj:** [Excalidraw](https://excalidraw.com/).

1. Vytvořte tři boxy: **Model / databáze**, **Controller nebo aplikační view / logika**, **View / šablona či UI**.
2. Přidejte uživatele a šipky pro situaci „uživatel upraví článek“.
3. Ke každé šipce dopište sloveso: například *odešle*, *ověří oprávnění*, *uloží*, *načte*, *vykreslí*.
4. Pod diagram napište dvě věty: co by se pokazilo, kdyby HTML šablona přímo prováděla databázový zápis bez kontrolní vrstvy?

> Model–View–Controller je myšlenkový nástroj. Konkrétní frameworky mohou názvy a rozdělení rolí používat trochu jinak (např. Django mluví o MTV), ale oddělení zodpovědností zůstává důležité.

### 1.4 Client-side rendering (CSR)

**Nástroj:** [CodeSandbox](https://codesandbox.io/) nebo lokální soubor `index.html`.

1. V CodeSandbox vytvořte šablonu **Vanilla**.
2. Do `index.js` vložte:

```js
fetch('https://dummyjson.com/products/1')
  .then((response) => response.json())
  .then((product) => {
    document.body.innerHTML = `<h1>${product.title}</h1>`;
  });
```

3. Otevřete náhled a zjistěte název produktu.
4. V DevTools otevřete Síť, náhled obnovte a najděte požadavek na `products/1`.
5. Popište pořadí: načtení výchozího HTML → spuštění JavaScriptu → požadavek na API → úprava DOM.

> **Důležité:** Ukázka používá `innerHTML` jen pro zcela důvěryhodný testovací řetězec. Data od uživatele se takto nevkládají; bezpečnější je `textContent` nebo frameworkové automatické escapování.

### 1.5 Stav SPA bez úplného obnovení

**Nástroj:** [TodoMVC](https://todomvc.com/).

1. Vyberte jednu ukázkovou implementaci ToDo aplikace.
2. S otevřeným panelem Síť přidejte položku, označte ji jako hotovou a přefiltrujte seznam.
3. Sledujte, zda se načítá nový HTML dokument. Pokud ne, zjistěte, zda aplikace ukládá stav například do `localStorage` (DevTools → Application/Storage).
4. Vysvětlete rozdíl mezi „změnou DOM“ a „obnovením celé HTML stránky“.

### 1.6 Princip statického generování (SSG)

**Nástroj:** textový editor.

1. Vytvořte `template.html`:

```html
<!doctype html>
<html lang="cs">
  <meta charset="utf-8">
  <title>{{ titulek }}</title>
  <body><article>{{ obsah }}</article></body>
</html>
```

2. Zkopírujte jej jako `clanek-1.html`, `clanek-2.html` a `clanek-3.html`.
3. V každé kopii nahraďte značky jiným titulkem a obsahem.
4. Otevřete soubory v prohlížeči. Co musí při požadavku udělat server, pokud jsou tyto soubory hotové předem?

> SSG tento opakovaný proces automatizuje při sestavení webu. Výhodou je rychlé doručení hotového HTML; nevýhodou je nutnost znovu sestavit obsah po změně dat.

[[ Doplňte: CSR vytváří část obsahu až v ___, SSG vytváří hotové HTML při ___. ]]

[[prohlížeči|klientovi]]

[[sestavení|buildu]]

---

## 2. Django jako příklad backendového frameworku

### Cíl kapitoly

Propojíte modely, relační databázi, URL routování, migrace a aplikační logiku. Nejde o ovládnutí celého Djanga, ale o porozumění tomu, co framework organizuje.

### 2.1 Model a cizí klíč

**Nástroj:** [dbdiagram.io](https://dbdiagram.io/).

1. Vytvořte nový diagram a vložte tento DBML zápis:

```dbml
Table Autor {
  id int [pk]
  jmeno varchar
}

Table Clanek {
  id int [pk]
  titulek varchar
  autor_id int
}

Ref: Clanek.autor_id > Autor.id
```

2. Zkontrolujte, že šipka vede od `Clanek.autor_id` k `Autor.id`.
3. Doplňte tabulku `Komentar` s `text`, `clanek_id` a `autor_id`.
4. Určete kardinality: kolik článků může mít autor a kolik autorů má jeden článek v tomto modelu?

### 2.2 ORM a SQL „pod kapotou"

**Nástroj:** [SQLiteOnline](https://sqliteonline.com/) nebo lokální SQLite. (Služba SQL Fiddle nemusí být pro SQLite vždy dostupná.)

1. Vložte a spusťte:

```sql
CREATE TABLE clanek (id INTEGER PRIMARY KEY, titulek TEXT);
INSERT INTO clanek (id, titulek) VALUES (1, 'Test');
SELECT * FROM clanek WHERE id = 1;
```

2. Zapište výsledek dotazu.
3. Porovnejte jej s významem Django zápisu `Clanek.objects.get(id=1)`.
4. Vysvětlete, proč ORM není „databáze“, ale vrstva, která sestavuje dotazy a mapuje řádky na objekty.

### 2.3 N+1 dotazů jako myšlenkový experiment

**Nástroj:** [Mockaroo](https://www.mockaroo.com/) nebo tabulkový procesor.

1. Navrhněte 1 000 článků s `id`, `titulek` a `autor_id`.
2. Představte si kód: nejdřív načte seznam 1 000 článků a pak pro každý článek samostatně načte autora.
3. Spočítejte, kolik databázových dotazů vznikne: jeden dotaz na články + jeden na každého autora.
4. Navrhněte lepší řešení: relační spojení `JOIN`, přednačtení relace nebo hromadný dotaz.

[[ Kolik dotazů odpovídá vzoru „1 dotaz na 1 000 článků + 1 na autora každého článku“? ]]

[( )] 2
[( )] 1 000
[(X)] 1 001

### 2.4 Cesta URL a odpověď 404

1. Otevřete `https://www.wikipedia.org/wiki/Neexistuje123` nebo jinou zjevně neexistující stránku na veřejném webu.
2. V Síti vyhledejte požadavek typu document a ověřte stavový kód.
3. Rozlište dvě možnosti: URL nemá v aplikaci vůbec cestu (routing nenajde pattern), nebo cesta existuje, ale požadovaný objekt neexistuje.
4. Vysvětlete, proč web nemá při chybě odhalovat interní výpis databáze nebo trasování aplikace.

### 2.5 Migrace jako historie schématu

1. V prázdném sešitu vytvořte sloupce `id` a `jmeno` a tři záznamy.
2. Rozhodněte se přidat povinný sloupec `vek`.
3. Zapište pravidlo pro existující záznamy: výchozí hodnota, dočasné povolení prázdné hodnoty, nebo ruční doplnění.
4. Vysvětlete, proč nestačí pouze upravit definici modelu v kódu.

> Migrace jsou verzované instrukce, které mění databázové schéma a případně i data. U produkční databáze je důležité znát pořadí a vratnost změn.

### 2.6 CRUD není celá aplikace

Vyberte si funkci „smazat účet“ na **vlastním testovacím účtu** nebo ji jen modelujte na papíře.

1. Vypište kroky, které jsou víc než databázové `DELETE`: ověření aktuální identity, kontrola oprávnění, potvrzení akce, zrušení relací, audit, případná retenční lhůta.
2. Označte, které kroky patří do UI, které do aplikační logiky a které do databáze.
3. Vysvětlete, proč administrace generovaná frameworkem může být užitečná pro správce, ale nemá sama o sobě nahradit veřejný proces aplikace.

---

## 3. Šablony, formuláře a vstupní data

### Cíl kapitoly

Zjistíte, proč musí server každé vstupní datum ověřovat, jak šablony bezpečně zobrazují text a proč přípona souboru není důkaz jeho typu.

### 3.1 Escapování HTML

**Nástroj:** [CodePen](https://codepen.io/) nebo lokální HTML soubor.

1. Do HTML vložte přesně tento bezpečně escapovaný text:

```html
&lt;script&gt;alert('xss')&lt;/script&gt;
```

2. Sledujte, že prohlížeč vypíše znaky tagu jako text a žádný skript nespustí.
3. Vysvětlete rozdíl mezi textem, který *vypadá* jako HTML, a skutečným HTML elementem.
4. Zapište, proč šablona má neznámý uživatelský obsah standardně escapovat.

### 3.2 Klientská validace není serverová ochrana

**Nástroj:** vlastní lokální soubor. Neodesílejte osobní údaje.

1. Vytvořte `form.html`:

```html
<form action="https://httpbin.org/post" method="post">
  <label>Věk: <input type="number" min="10" name="vek" required></label>
  <button>Odeslat test</button>
</form>
```

2. Otevřete soubor v prohlížeči a zkuste hodnotu `5`; prohlížeč ji běžně odmítne.
3. V DevTools v části Elements dočasně smažte atributy `min` a `required`, zadejte `-5` a odešlete pouze toto fiktivní číslo na testovací službu.
4. Odpověď dokazuje, že uživatel může změnit klientské UI. Backend proto musí věk ověřit znovu, nezávisle na HTML.

### 3.3 Regulární výrazy

**Nástroj:** [Regex101](https://regex101.com/), jazyk Python.

1. Vložte regulární výraz `^[A-Z]{3}-\d{4}$`.
2. Otestujte `ABC-1234`, `AB-12345`, `abc-1234` a `ABC-12A4`.
3. U každého rozhodněte, zda projde, a vysvětlete roli `^`, `$`, `{3}`, `{4}` a `\d`.
4. Diskutujte omezení: regulární výraz může ověřit formát, ne pravdivost údaje (např. zda existuje daný e-mail).

### 3.4 Static files a media files

1. Na veřejném zpravodajském webu otevřete Síť.
2. Filtrujte nejprve **CSS**, potom **Img**.
3. Porovnejte cesty a domény dvou souborů. Který soubor je pravděpodobně součástí nasazené aplikace a který může pocházet z redakčního uploadu/CDN?
4. Napište, proč se v produkci často jinak řeší nasazování společných CSS souborů a ukládání uživatelských fotografií.

### 3.5 Šablona a data

**Nástroj:** [JinjaFx](https://jinjafx.io/) nebo jiný Jinja playground.

1. Do šablony vložte:

```jinja2
Vítej {% if uzivatel %}{{ uzivatel }}{% else %}hoste{% endif %}!
```

2. Jako data použijte YAML:

```yaml
uzivatel: Petr
```

3. Pozorujte výstup, pak položku `uzivatel` odstraňte a výstup porovnejte.
4. Pojmenujte, co je v ukázce struktura šablony a co jsou vstupní data.

### 3.6 Přípona souboru není ověření obsahu

1. Vytvořte `falesny-obrazek.txt` s větou „Tohle není obrázek“.
2. Přejmenujte jej na `falesny-obrazek.jpg`.
3. Pokuste se jej otevřít jako obrázek. Poznamenejte si reakci programu.
4. Vysvětlete, proč backend při uploadu kontroluje povolený typ, skutečný obsah („magic bytes“), velikost, název, oprávnění a bezpečné umístění souboru.

[[ Co musí být poslední autoritou pro validaci formuláře? ]]

[( )] Atribut `required` v HTML.
[( )] JavaScript odeslaný prohlížeči.
[(X)] Serverová aplikační logika.

---

## 4. Stav, autentizace a autorizace

### Cíl kapitoly

Odlišíte identitu uživatele od jeho oprávnění a vysvětlíte účel sessions, tokenů, passkeys, hashování a delegovaného přístupu.

### 4.1 Cookies a session

1. Na vlastním účtu nebo na testovací službě otevřete DevTools → **Application/Storage → Cookies**.
2. Najděte cookie, která pravděpodobně souvisí s relací. Neopisujte a nikomu neposílejte její hodnotu.
3. Pozorujte atributy `HttpOnly`, `Secure`, `SameSite`, doménu a dobu platnosti.
4. Vysvětlete účel atributů. Cookie nemažte na pracovním či školním účtu; chcete-li důsledek ověřit, použijte anonymní/testovací relaci.

> Smazání session cookie často vede k odhlášení, ale chování se liší podle služby a dalších mechanismů přihlášení. Podstatné je, že cookie bývá odkazem na relaci, nikoli „heslem uloženým v prohlížeči“.

### 4.2 Autentizace × autorizace

**Nástroj:** [httpbin Basic Auth](https://httpbin.org/basic-auth/user/passwd).

1. Otevřete odkaz a zadejte testovací údaje `user` / `passwd`.
2. Vysvětlete, co služba nyní ví: identitu nebo oprávnění ke všem akcím?
3. Vytvořte tabulku se třemi akcemi `zobrazit profil`, `upravit vlastní profil`, `smazat cizí účet` a doplňte, zda by je role běžného uživatele měla smět provést.

| Otázka | Správný pojem |
|---|---|
| Kdo se právě přihlásil? | autentizace |
| Smí tato osoba provést konkrétní akci nad konkrétním objektem? | autorizace |

### 4.3 JWT: čitelný obsah, ověřitelný podpis

**Nástroj:** [JWT.io](https://jwt.io/). Pracujte jen s výchozím demonstračním tokenem.

1. Prohlédněte si části `header.payload.signature`.
2. Změňte v payloadu zobrazené jméno na `Administrátor`.
3. Sledujte, že se serializovaný token mění a existující podpis už neodpovídá.
4. Zapište dvě pravidla: payload JWT se obvykle **nešifruje**; server musí ověřit podpis, platnost, vydavatele a zamýšlené publikum.

### 4.4 Passkeys / WebAuthn

**Nástroj:** [webauthn.io](https://webauthn.io/).

1. Použijte pouze testovací název účtu a zařízení, které umožňuje biometrické nebo systémové ověření.
2. Zaregistrujte passkey a poté proveďte autentizaci.
3. Popište, co uživatel prokazuje zařízení a co server ověřuje kryptograficky.
4. Vysvětlete, proč passkey není totéž jako „otisk prstu odeslaný serveru“.

### 4.5 Hashování hesel

**Nástroj:** [CyberChef](https://gchq.github.io/CyberChef/).

1. Do vstupu napište výhradně fiktivní heslo, například `mojeheslo123`.
2. Vyzkoušejte SHA-256 a změňte jeden znak vstupu.
3. Porovnejte dva výrazně odlišné výsledky.
4. Doplňte: v reálné aplikaci se pro hesla používají specializované pomalé adaptivní algoritmy, jako Argon2, bcrypt nebo scrypt, a pro každý záznam jedinečná sůl. Rychlý SHA-256 sám o sobě není doporučené ukládání hesel.

### 4.6 OAuth 2.0 jako delegace

**Nástroj:** [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/).

1. Prostudujte si obrazovku žádosti o oprávnění; nepovolujte citlivé rozsahy a nepřipojujte školní účet, pokud to není výslovně domluveno.
2. V diagramu zachyťte čtyři role: vlastník zdroje, klientská aplikace, autorizační server, resource server/API.
3. Vysvětlete, proč aplikace při správném OAuth toku nemusí získat hlavní heslo uživatele.

[[ Vyberte pravdivé tvrzení o JWT. ]]

[( )] Každý JWT je tajný, protože je zakódovaný.
[(X)] Zakódování není šifrování; důvěryhodnost se ověřuje podpisem a dalšími kontrolami.
[( )] JWT zbavuje backend nutnosti autorizovat akce.

---

## 5. Bezpečnost webové aplikace

### Cíl kapitoly

Poznáte hlavní rizika na izolovaných ukázkách. Cílem není hledat chyby na živých službách, ale pochopit obranné mechanismy.

### 5.1 XSS v izolované výukové hře

**Nástroj:** [Google XSS Game](https://xss-game.appspot.com/) – pouze pokud je v době výuky stále dostupná.

1. Otevřete první úroveň hry.
2. Postupujte podle jejích vlastních instrukcí v jejím izolovaném prostředí.
3. Poznamenejte si, jak se uživatelský vstup dostal do stránky a proč se z textu stal kód.
4. Jako obranu zapište: kontextové escapování výstupu, bezpečné API pro práci s DOM, sanitizace pouze tam, kde je nutné povolit omezené HTML, a vhodná CSP.

> Nikdy nevkládejte XSS payloady do vyhledávání, komentářů nebo formulářů skutečných webů. I „pouhý alert“ je neautorizované bezpečnostní testování.

### 5.2 CSP jako druhá obranná vrstva

**Nástroj:** [CSP Evaluator](https://csp-evaluator.withgoogle.com/).

1. Vložte **vlastní ukázkovou politiku**, nikoli URL cizího webu:

```text
default-src 'self'; script-src 'self'; img-src 'self' https:; object-src 'none'; base-uri 'self'
```

2. Spusťte vyhodnocení a přečtěte si doporučení.
3. Změňte `script-src 'self'` na `script-src *` a vysvětlete, proč je druhá varianta slabší.
4. Uveďte, proč CSP sama nenahrazuje escapování výstupu.

### 5.3 SQL injection pouze jako textový model

1. Do poznámek napište hypotetický nebezpečný princip:

```text
SELECT * FROM uzivatele WHERE jmeno = 'ZADANY_TEXT'
```

2. Diskutujte, proč by skládání struktury SQL z textu uživatele mohlo změnit význam dotazu.
3. Nenapadejte žádnou databázi a nespouštějte útočné řetězce proti službám.
4. Napište bezpečnou zásadu: používat parametrizované dotazy / prepared statements nebo ORM, které data předávají odděleně od struktury dotazu.

### 5.4 IDOR a kontrola přístupu: bezpečná analýza

1. Vymodelujte URL na papíře: `/objednavky/15000`.
2. Vytvořte dva scénáře odpovědi backendu pro uživatele, který objednávku nevlastní: `403 Forbidden` a `404 Not Found`.
3. Vysvětlete, že pouhá přítomnost identifikátoru v URL nezakládá oprávnění k objektu.
4. Na reálných e-shopech, fórech ani školních systémech identifikátory neměňte. Bezpečnostní testování patří jen do vlastního labu nebo do výslovně povoleného programu.

### 5.5 CSRF token ve formuláři

1. Vytvořte lokální ukázkový formulář s fiktivním tokenem:

```html
<form method="post">
  <input type="hidden" name="csrf_token" value="demo-nepouzitelny-token">
  <button>Změnit testovací údaj</button>
</form>
```

2. Označte, které pole uživatel nevidí a proč jeho existence ještě sama nezajišťuje bezpečnost.
3. Vysvětlete princip: server vytvoří nepředvídatelný token, sváže jej s relací nebo jiným ověřitelným kontextem a při změnovém požadavku jej kontroluje.
4. Doplňte související obrany: `SameSite` cookies, kontrola Origin/Referer a opětovné ověření citlivých akcí.

### 5.6 Závislosti a známé zranitelnosti

**Nástroj:** [CVE Details](https://www.cvedetails.com/) nebo databáze [NVD](https://nvd.nist.gov/).

1. Vyhledejte známou technologii, například Django, Node.js nebo OpenSSL.
2. U jedné položky zaznamenejte identifikátor CVE, rok a stručný popis dopadu; nic nezkoušejte zneužívat.
3. Navrhněte provozní reakci: ověřit, zda se týká naší verze, přečíst doporučení dodavatele, aktualizovat/testovat, nasadit opravu a evidovat změnu.
4. Vysvětlete pojem **supply chain** v souvislosti s balíčky a jejich závislostmi.

[[ Jaká je správná obrana proti SQL injection? ]]

[( )] Zakázat uživatelům apostrofy.
[( )] Skrýt databázové chyby, ale dál slepovat SQL text.
[(X)] Používat parametrizované dotazy nebo bezpečně použitý ORM mechanismus.

---

## 6. CMS, nasazení a provoz

### Cíl kapitoly

Uvidíte, že aplikace nekončí posledním řádkem kódu: musí se bezpečně nasadit, rychle doručovat, sledovat a průběžně aktualizovat.

### 6.1 Headless CMS a obsahové API

**Nástroj:** [DummyJSON – posts](https://dummyjson.com/posts).

1. Otevřete URL a prohlédněte si strukturu odpovědi.
2. Najděte pole, které by frontend mohl použít pro titulek, text a autora příspěvku.
3. Navrhněte dvě různé prezentace téhož obsahu: článek na webu a kartu v mobilní aplikaci.
4. Vysvětlete, proč headless CMS dodává především obsah a API, nikoli nutně finální HTML design.

### 6.2 Audit pomocí Lighthouse

**Nástroj:** panel **Lighthouse** v Chrome DevTools.

1. Na vlastním nebo veřejném nekritickém webu otevřete `F12` → Lighthouse.
2. Vyberte **Navigation**, zařízení **Mobile** a spusťte analýzu.
3. Poznamenejte si jedno zjištění z každé oblasti: Performance, Accessibility, Best Practices a SEO.
4. Nezaměňujte skóre za absolutní pravdu: vysvětlete, proč laboratorní měření závisí na síti, zařízení, cache a obsahu stránky.

> Lighthouse dnes neposuzuje instalovatelnost PWA vždy stejným samostatným skóre jako dříve. PWA ověřujte také přes manifest, HTTPS, service worker a skutečný test instalace/offline chování.

### 6.3 Publikování statického webu

**Nástroj:** [Netlify Drop](https://app.netlify.com/drop) nebo školní hosting.

1. Ve složce `muj-web` vytvořte `index.html` s nadpisem a vlastním jménem pouze v podobě křestního jména či přezdívky.
2. Otevřete jej lokálně a ověřte, že funguje.
3. Pokud máte souhlas učitele a účet, přetáhněte složku do Netlify Drop; jinak pouze popište, jak by krok vypadal.
4. Zapište rozdíl mezi souborem na vašem disku, vývojovým serverem a veřejně dostupným produkčním URL s HTTPS.

### 6.4 CI/CD v GitHub Actions

1. Otevřete stránku **Actions** ve veřejném repozitáři, například [Vue](https://github.com/vuejs/core/actions).
2. Vyberte jeden dokončený workflow run a vypište jeho kroky (např. checkout, instalace závislostí, lint, testy, build).
3. Rozlište CI (automatické ověřování změny) a CD (automatizované doručení/nasazení schválené změny).
4. Napište jednu výhodu a jedno riziko plně automatického nasazování.

### 6.5 Cache a CDN v odpovědních hlavičkách

1. V Síti vyberte obrázek nebo CSS z veřejného webu.
2. Najděte `Cache-Control`, případně `Age`, `ETag`, `Last-Modified`, `Via` nebo jinou hlavičku ukazující na cache/CDN.
3. Pokud se objeví `304 Not Modified`, vysvětlete, že klient může znovu použít lokálně uložený obsah po ověření jeho aktuálnosti.
4. Pokud se objeví `HIT`, ověřte si u konkrétní služby význam hlavičky; názvy nejsou mezi CDN univerzální.

> Cache zrychluje doručení, ale přináší problém invalidace: po změně souboru musí uživatel dostat novou verzi. Proto build nástroje často používají názvy jako `app.a1b2c3.js`.

### 6.6 AI jako externí služba a nedůvěryhodný vstup

1. V chatovacím modelu položte bezpečnou otázku: „Jak by měl vypadat parametrizovaný SQL dotaz pro vyhledání uživatele podle jména v **[uveď jazyk/framework]**?“
2. Porovnejte odpověď s pravidly z kapitoly o SQL injection.
3. Sepište minimálně čtyři kontroly, které musí vývojář provést před použitím návrhu AI: správnost, bezpečnost, oprávnění, ochrana osobních údajů/licencí, testy a soulad s architekturou.
4. Vysvětlete, proč nesmíte do veřejného AI nástroje kopírovat hesla, session tokeny, osobní údaje žáků ani neveřejný zdrojový kód bez příslušného povolení.

[[ Které tvrzení o výstupu AI je správné? ]]

[( )] Pokud vypadá jako kód, je automaticky bezpečný.
[(X)] Je to externí návrh, který vyžaduje stejnou kontrolu jako jiný nedůvěryhodný vstup.
[( )] Lze do promptu bez omezení vložit tajné klíče, aby AI kód opravila.

---

## Závěrečný úkol: mini-architektura školního redakčního systému

Navrhněte systém pro publikování školních článků. Odevzdejte jeden diagram a jednu stránku textu.

1. Nakreslete klienta, frontend, backend, databázi, úložiště obrázků a CDN/cache.
2. Vyznačte dva API endpointy: `GET /api/clanky` a `POST /api/clanky`.
3. Pro `POST` popište validaci, autentizaci, autorizaci role editor, CSRF ochranu (je-li použit cookie-based přístup), audit a odpověď při chybě.
4. Rozhodněte, které stránky byste předgenerovali pomocí SSG a které by vyžadovaly dynamické zpracování.
5. Uveďte jednu migraci databáze, jednu kontrolu CI a jeden mechanismus sledování provozu.
6. Označte nejméně tři místa, kde se do systému dostává nedůvěryhodný vstup, a doplňte obranu.

### Sebehodnocení

| Umím… | Ano | Ještě procvičit |
|---|:---:|:---:|
| vysvětlit cestu HTTP požadavku |  |  |
| odlišit klientskou a serverovou validaci |  |  |
| odlišit autentizaci a autorizaci |  |  |
| vysvětlit parametrizovaný SQL dotaz |  |  |
| popsat smysl migrací, CI/CD a cache |  |  |
| pracovat bezpečně a pouze v povoleném prostředí |  |  |

## Slovníček

**API** – rozhraní pro komunikaci programů.  
**Autentizace** – ověření identity.  
**Autorizace** – rozhodnutí, zda identita smí provést danou akci.  
**CDN** – distribuovaná síť pro doručování obsahu z bodů blíže uživatelům.  
**CSR** – vykreslování obsahu JavaScriptem v klientovi.  
**CSP** – politika prohlížeče omezující povolené zdroje obsahu.  
**CSRF** – podvržení požadavku zneužívajícího přihlášený prohlížeč.  
**Migration** – verzovaná změna databázového schématu.  
**ORM** – vrstva mapující databázová data na programové objekty.  
**SSG** – vytvoření hotových stránek před jejich návštěvou.  
**XSS** – spuštění nechtěného skriptu v prohlížeči oběti.
