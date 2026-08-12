## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Základní pravidlo: klientský vstup není důvěryhodný**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Bezpečnost nezačíná seznamem názvů útoků. Začíná otázkou, kde systém přechází mezi různě důvěryhodnými částmi. HTTP požadavek, uploadovaný soubor, data z externího API i parametr v URL mohou být chybné nebo úmyslně škodlivé.

Aplikace proto kombinuje validaci vstupu, bezpečné zpracování, kontrolu oprávnění a správné kódování výstupu. Jedna univerzální funkce „sanitize všechno“ neexistuje. Řetězec, který je bezpečný jako prostý text v HTML, nemusí být bezpečný uvnitř JavaScriptu, URL nebo SQL dotazu. Obrana závisí na kontextu.

OWASP Top 10 se průběžně aktualizuje podle bezpečnostní praxe. Pro výuku je užitečnější rozumět mechanismům než memorovat pořadí kategorií. Zvlášť důležité jsou chyby v řízení přístupu, injection, bezpečnostní konfigurace, práce s kryptografií, autentizací a závislostmi.

***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**XSS: když se data stanou kódem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Cross-Site Scripting — XSS** vzniká, když aplikace vloží nedůvěryhodná data do stránky tak, že je prohlížeč interpretuje jako aktivní obsah. Představme si komentář, jehož text backend bez escapování vloží do HTML. Pokud vstup obsahuje skript nebo nebezpečný atribut, prohlížeč jej může spustit v kontextu legitimního webu.

Základní obranou je **output encoding** podle kontextu a bezpečné templatingové API. Django Templates běžný text automaticky escapují. Na klientu je vhodné při vkládání textu používat `textContent` místo `innerHTML`, pokud HTML skutečně nepotřebujeme.

**Content Security Policy — CSP** může omezit zdroje skriptů a ztížit využití některých XSS chyb. Je to důležitá další vrstva, ne omluva pro nebezpečné generování HTML.

***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**SQL injection: dotaz není řetězec ke slepování**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


SQL injection vzniká, když se nedůvěryhodný vstup stane součástí syntaxe databázového dotazu. Obrana není „zakázat apostrof“, ale používat **parametrizované dotazy** nebo ORM, které hodnoty oddělí od struktury příkazu.

Django ORM při běžném použití parametry bezpečně předává databázovému ovladači. Riziko se vrací, když vývojář začne skládat raw SQL řetězce ručně. ORM tedy pomáhá, ale není magický štít proti libovolnému nebezpečnému kódu.

Stejný obecný princip platí i jinde: nedůvěryhodná data se nemají měnit v příkazy shellu, šablonu, URL redirectu nebo jiný interpretovaný kód bez správné hranice a validace.

***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**CSRF: zneužití přihlášeného prohlížeče**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Cross-Site Request Forgery — CSRF** využívá skutečnosti, že prohlížeč může k požadavku automaticky připojit přihlašovací cookie. Útočný web se pokusí vyvolat změnový požadavek na jinou službu a využít tak už existující identitu oběti.

Django má CSRF ochranu vestavěnou. Formuláře s metodou POST používají CSRF token a middleware kontroluje, zda požadavek odpovídá očekávanému původu a tokenu. Atribut `SameSite` u cookie přidává další ochrannou vrstvu.

CSRF se liší od XSS. U XSS běží škodlivý obsah uvnitř důvěryhodné stránky. U CSRF se zvenčí zneužije skutečnost, že prohlížeč už má vztah s cílovou službou. Jedna chyba proto není „jiný název“ pro druhou.

***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Broken access control: nejde jen o přihlášení**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednou z nejzávažnějších skupin chyb je špatné řízení přístupu. Uživatel může změnit ID v URL z `/invoice/100` na `/invoice/101` a server mu cizí fakturu vydá, protože ověřil pouze to, že je přihlášen. Tomu se někdy říká IDOR — Insecure Direct Object Reference — a spadá do širšího problému přístupových kontrol.

Správná kontrola se ptá nejen „je uživatel přihlášen?“, ale „má tento konkrétní uživatel právo provést tuto konkrétní operaci nad tímto konkrétním objektem?“.

Role-based přístup je jednoduchý model: administrátor, editor, čtenář. Jemnější systémy mohou pracovat s permissions nebo politikami založenými na vlastnostech uživatele, objektu a kontextu. Čím složitější pravidlo, tím důležitější jsou automatizované testy autorizace.

***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Bezpečnost konfigurace a závislostí**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Aplikace může mít správný kód a přesto být nebezpečná kvůli provozu. Typickým příkladem je produkční server se zapnutým debug režimem, veřejným administrátorským rozhraním bez ochrany, uniklým `SECRET_KEY` nebo nepodporovanou knihovnou.

Tajné údaje nepatří do veřejného Git repozitáře. Produkční konfigurace používá bezpečné proměnné prostředí nebo secret manager. HTTPS má být standardem, nikoli volitelným „šifrovaným režimem“. Framework i databáze potřebují bezpečnostní aktualizace a tým musí vědět, jaké balíčky nasazuje.

Supply-chain bezpečnost získala na významu právě proto, že moderní aplikace používají stovky závislostí. Lockfile zlepšuje reprodukovatelnost, ale sám nezaručuje bezpečnost. Je potřeba sledovat aktualizace, původ balíčků a minimalizovat zbytečné závislosti.

# 6. CMS, nasazení a provoz

***
