# Webové aplikace

## Modernizovaný výukový text

> Webová aplikace začíná být zajímavá ve chvíli, kdy stránka není jen dokumentem, ale součástí systému: uživatel se přihlásí, odešle data, server rozhodne, zda má právo danou operaci provést, databáze uloží změnu a výsledné rozhraní se znovu sestaví. Kvalita aplikace proto nestojí na jednom frameworku, ale na dobře rozdělených odpovědnostech, bezpečných hranicích a spolehlivém provozu.

# 1. Architektura webové aplikace

## 1.1 Od statické stránky k systému se stavem

Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny. Webová aplikace naproti tomu často vytváří odpověď podle uživatele, dat a aktuálního stavu systému. Stejná adresa `/profil` může po přihlášení zobrazit údaje konkrétního člověka, zatímco nepřihlášeného uživatele přesměruje na přihlašovací stránku.

Jednoduchá webová aplikace se dá rozdělit na tři logické vrstvy. **Prezentační vrstva** vytváří uživatelské rozhraní. **Aplikační vrstva** rozhoduje, co se má při požadavku stát. **Datová vrstva** ukládá a zpřístupňuje data. V reálném systému mohou být vrstvy rozděleny mezi více procesů nebo služeb, ale jejich oddělení je užitečné i v malém projektu.

Představme si redakční systém. Uživatel otevře formulář pro nový článek. HTML formulář patří do prezentační vrstvy. Po odeslání backend zkontroluje, zda je uživatel přihlášen, zda má právo publikovat, zda nechybí titulek a zda je zvolená kategorie platná. Datová vrstva pak uloží článek a vztahy k autorovi a kategorii. Samotné tlačítko „Publikovat“ tedy nepublikuje nic; pouze vyvolá požadavek, který musí bezpečně projít celým systémem.

Tento příklad ukazuje důležitou hranici: **frontend může požádat, backend rozhoduje**. Uživatel si může HTML a JavaScript ve svém prohlížeči změnit. Nelze proto spoléhat na to, že skryté tlačítko zabrání neoprávněné operaci. Server musí oprávnění ověřit při každém citlivém požadavku.

## 1.2 MVC a příbuzné návrhové vzory

Mnoho frameworků používá architektonické myšlenky odvozené od **MVC — Model–View–Controller**. Model reprezentuje data a pravidla kolem nich, view prezentuje výsledek a controller zpracuje vstup a koordinuje další části.

Webové frameworky však používají názvy různě. Django tradičně mluví o **Model–Template–View (MTV/MVT)**. Django `Model` popisuje datovou strukturu a práci s databází, `Template` generuje prezentační výstup a Django `View` přijme požadavek a vrátí odpověď. Funkce či třída označená v Django jako view tedy vykonává část role, kterou by v klasickém popisu MVC lidé často spojili s controllerem.

Není proto užitečné vést spor, zda je Django „opravdu MVC“ nebo „opravdu MVT“. Podstatný je princip **separation of concerns**: databázová logika nemá být bezdůvodně rozeseta v HTML šablonách, routování nemá obsahovat celý obchodní proces a jeden obří soubor nemá řešit vše od přihlášení po generování PDF.

Dobré rozdělení zjednodušuje testování. Model lze ověřit bez prohlížeče, view bez skutečné šablony a šablonu s připravenými daty. Když se změní databáze nebo vzhled stránky, nemusí se automaticky přepisovat celý systém.

## 1.3 Server-side rendering, client-side rendering a hybridní web

Klasická serverová aplikace vytvoří HTML na serveru. Prohlížeč požádá například o `/clanky/42`, backend načte data, vybere šablonu a vrátí hotový dokument. Tento přístup se označuje jako **server-side rendering — SSR**.

U **client-side rendering — CSR** server může poslat základ aplikace a JavaScript následně přes API načte data a sestaví rozhraní v prohlížeči. Tak funguje mnoho Single Page Applications. Výhodou může být velmi interaktivní prostředí, nevýhodou větší množství klientského kódu, složitější počáteční načítání a nutnost dobře řešit navigaci, chyby a přístupnost.

Současné frameworky často kombinují více přístupů. Některé stránky lze vygenerovat předem jako **SSG — Static Site Generation**, jiné renderovat na serveru při požadavku a po načtení „hydratovat“ klientským JavaScriptem. Další architektury posílají do prohlížeče jen JavaScript pro skutečně interaktivní části. Není proto správné chápat SPA jako automaticky modernější než serverové šablony. Vhodná architektura závisí na typu aplikace.

Pro školní redakční systém s formuláři a běžnými články může být serverové renderování velmi efektivní a jednoduché. Pro grafický editor v prohlížeči bude naopak významná část logiky přirozeně na klientovi.

# 2. Django jako konkrétní příklad backendového frameworku

## 2.1 Projekt, aplikace a cesta požadavku

**Django** je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů. Je vhodným výukovým příkladem proto, že ukazuje většinu vrstev webové aplikace v jednom konzistentním systému.

Django rozlišuje **project** a **app**. Projekt představuje konfiguraci celého webu. App je logicky související část, například články, uživatelské profily nebo katalog. Jeden projekt může obsahovat více apps a jedna app může být znovupoužitelná ve více projektech.

Typická struktura obsahuje konfigurační modul se `settings.py`, hlavní routování v `urls.py` a vstupní body `wsgi.py` a `asgi.py`. Jednotlivá app mívá například `models.py`, `views.py`, vlastní `urls.py`, šablony a testy. Příkaz `manage.py` poskytuje rozhraní pro správní úlohy.

Při požadavku se zjednodušeně děje toto:

**HTTP request → middleware → URL resolver → view → model/služby → template nebo JSON → HTTP response**

Middleware může řešit bezpečnost, sessions, autentizaci nebo jiné společné operace. URL resolver vybere view podle cesty. View zpracuje požadavek, případně použije ORM a nakonec vytvoří odpověď.

## 2.2 Model a ORM: objektový pohled na relační databázi

Django **ORM — Object–Relational Mapping** umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
```

Instance `Article` odpovídá záznamu, pole objektu sloupcům a metody ORM vytvářejí databázové dotazy. ORM neznamená, že SQL přestalo existovat. Framework generuje SQL podle konkrétní databáze a vývojář musí stále rozumět indexům, vztahům, transakcím a nákladnosti dotazů. Špatně navržený ORM kód může spustit stovky dotazů tam, kde by stačily dva.

Vztahy mezi tabulkami se zapisují například přes `ForeignKey`, `OneToOneField` nebo `ManyToManyField`. U článku může `ForeignKey` odkazovat na autora a kategorii. Framework díky tomu zná nejen typ sloupce, ale i význam vztahu a dokáže nad ním stavět formuláře či administraci.

Model může obsahovat validační pravidla a metody související s datovou doménou. Není však vhodné z modelu udělat nekonečný soubor celé aplikace. Rozsáhlejší obchodní logika může patřit do servisní vrstvy nebo samostatných modulů.

## 2.3 Migrace: databázové schéma má historii

Když do modelu přidáme pole `summary`, databáze se sama bezpečně nezmění jen proto, že Pythonová třída vypadá jinak. Django používá **migrace** — verzované popisy změn schématu.

Příkaz `makemigrations` vytvoří návrh migrace a `migrate` ji aplikuje na databázi. Migrace mohou vytvářet tabulky, přidávat sloupce, měnit indexy nebo provádět definované datové transformace.

Je užitečné chápat migraci jako podobu verzovacího systému pro strukturu databáze. Kód aplikace a schéma musí postupovat společně. Když tým stáhne novou verzi projektu, nestačí jen aktualizovat `.py` soubory; často musí aplikovat také příslušné migrace.

V produkci je změna schématu citlivá operace. Přidat povinný sloupec do tabulky se stovkami milionů řádků může mít zcela jiný dopad než totéž ve školní SQLite databázi. Framework migraci popíše, ale provozní riziko musí posoudit člověk.

## 2.4 Routing a views

Routing přiřazuje URL konkrétní logice. Dobře navržená URL popisuje zdroj nebo význam stránky, ne fyzický soubor na disku.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("articles/<int:article_id>/", views.article_detail, name="article-detail"),
]
```

View přijme objekt `HttpRequest` a vrátí `HttpResponse` nebo jeho specializovanou variantu. Může renderovat HTML, vrátit JSON, přesměrovat uživatele nebo oznámit chybu.

```python
from django.shortcuts import get_object_or_404, render
from .models import Article

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/detail.html", {"article": article})
```

Django podporuje funkční i třídní views. Třídní generické views umějí zkrátit opakující se vzory seznamu, detailu nebo formuláře. Kratší kód ale není automaticky srozumitelnější; při výuce je často vhodné nejprve pochopit explicitní cestu požadavku a teprve potom používat abstrakce.

## 2.5 Administrace a CRUD: rychlý nástroj, ne náhrada veřejného rozhraní

Jednou z praktických předností Djanga je automaticky generované **administrační rozhraní**. Jakmile jsou vytvořeny modely a správně nastavena oprávnění, lze v administraci relativně rychle prohlížet, přidávat, upravovat a mazat záznamy. Typické operace se shrnují zkratkou **CRUD — Create, Read, Update, Delete**. Pro redakční systém tak lze bez psaní celého vlastního editoru vytvořit pracovní prostředí, v němž správce založí autora, upraví článek nebo změní kategorii.

Tato pohodlnost ale snadno svádí k chybnému mentálnímu modelu. Django admin není automaticky hotové veřejné uživatelské rozhraní aplikace a už vůbec ne bezpečnostní vrstva, která by vyřešila všechna oprávnění za vývojáře. Je navržen hlavně jako interní nástroj pro důvěryhodné pracovníky. Veřejný e-shop, školní portál nebo redakční web obvykle potřebuje vlastní views, formuláře, API a především pravidla, která přesně určují, kdo smí kterou operaci provést.

Stejně důležité je oddělit CRUD od skutečné aplikační logiky. Operace „smazat článek“ může ve skutečném systému znamenat kontrolu role uživatele, vytvoření auditního záznamu, odebrání stránky z veřejného webu a případně zachování verze pro obnovu. Jednoduché tlačítko tedy může spustit více pravidel než jediný SQL příkaz `DELETE`. Framework urychluje rutinní práci, ale význam operace musí stále navrhnout člověk.

# 3. Šablony, formuláře a vstupní data

## 3.1 Šablona kombinuje strukturu a data, ne celou aplikační logiku

Django Templates umožňují vložit data do HTML a používat jednoduché řídicí konstrukce.

```html
<h1>{{ article.title }}</h1>

{% if article.published_at %}
  <p>Publikováno: {{ article.published_at }}</p>
{% endif %}
```

Šablona může používat filtry, podmínky, cykly, dědičnost a vkládání dalších šablon. Dědičnost je praktická pro společný layout: `base.html` obsahuje hlavičku a hlavní kostru a konkrétní stránky vyplní pojmenované bloky.

Django ve výchozím nastavení **automaticky escapuje** běžné proměnné v HTML kontextu. To je důležitá obrana proti XSS. Pokud autor bezdůvodně označí uživatelský obsah jako bezpečný HTML řetězec, tuto ochranu vypíná. „Framework mě chrání“ proto platí jen tehdy, když se jeho bezpečné výchozí mechanismy nepřepisují bez porozumění.

Šablona by neměla obsahovat složitý databázový algoritmus. Jejím úkolem je prezentovat připravená data. Čím více obchodních rozhodnutí je ukryto v HTML, tím obtížněji se aplikace testuje a znovu používá například pro API.

## 3.2 Formulář: pohodlí pro uživatele, nedůvěra pro server

Django Forms propojují HTML formulář se serverovou validací. Vývojář definuje pole a pravidla, framework vytvoří datový objekt, ověří vstup a zpřístupní chyby.

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
```

`ModelForm` může formulář odvodit z modelu, což je praktické pro CRUD aplikace. Není však vhodné automaticky zpřístupnit všechna pole modelu jen proto, že to framework dovoluje. Například interní příznak `is_approved` nesmí uživatel změnit pouhým doplněním položky do HTTP požadavku.

Validace probíhá na více úrovních. HTML může okamžitě upozornit na chybějící povinné pole. JavaScript může ukázat komplexnější zpětnou vazbu. **Server ale musí data ověřit vždy**, protože klientský kód není pod kontrolou serveru.

Kontrola typu nebo délky navíc nestačí. Titulek může mít správných 80 znaků a přesto uživatel nemusí mít oprávnění článek publikovat. Validace formátu a **autorizace akce** jsou dvě různé otázky.

## 3.3 Regulární výraz je nástroj, ne univerzální validátor

**Regulární výrazy — regular expressions, regex** popisují vzory v textu. Hodí se pro vyhledání identifikátoru, kontrolu jednoduchého formátu nebo rozdělení logu. Základní konstrukce zahrnují množiny znaků, skupiny, alternativy a kvantifikátory.

```text
^[A-Z]{3}-\d{4}$
```

Tento vzor může například odpovídat školnímu inventárnímu kódu `ABC-1234`. Pro takto přesně definované lokální pravidlo je regex vhodný.

Není však dobrý nápad psát obrovský vlastní regulární výraz, který má „dokonale ověřit každou platnou e-mailovou adresu podle všech standardů“. Pro běžné účely je často lepší použít frameworkovou validaci a skutečné potvrzení adresy zasláním odkazu. Podobně složité parsování HTML nebo programovacího jazyka patří parseru, ne jediné řádce regexu.

## 3.4 Soubory, statická data a uživatelská média

Webová aplikace pracuje se dvěma odlišnými skupinami souborů. **Static files** jsou součástí aplikace: CSS, JavaScript, ikony nebo vlastní fonty. **Media files** vznikají od uživatelů nebo editorů: fotografie článků, přílohy či avatary.

Rozlišení je důležité pro bezpečnost i deployment. Statické soubory lze při nasazení sesbírat, verzovat a doručovat přes CDN. Uživatelská média musí mít vlastní úložiště, zálohy, kontrolu oprávnění a někdy bezpečnostní skenování.

Uploadovaný soubor není důvěryhodný jen proto, že má příponu `.jpg`. Server může kontrolovat velikost, očekávaný typ a způsob dalšího zpracování. Citlivé soubory by neměly být automaticky veřejné jen proto, že leží v adresáři dostupném webovým serverem.

# 4. Stav, autentizace a autorizace

## 4.1 HTTP si uživatele samo nepamatuje

Každý HTTP požadavek je samostatná zpráva. Přihlášený stav se proto musí propojit pomocí dalšího mechanismu. Klasická webová aplikace často používá **session**: server uchovává stav a prohlížeči dá náhodný identifikátor v cookie. Při dalším požadavku cookie dorazí zpět a server podle identifikátoru najde session.

Cookie má být chráněna vhodnými atributy. `Secure` omezuje přenos na HTTPS, `HttpOnly` brání běžnému JavaScriptu cookie přečíst a `SameSite` omezuje některé cross-site scénáře. Ani správně nastavená cookie však neřeší všechna rizika; například XSS může jménem uživatele provádět akce, i když session cookie kvůli `HttpOnly` přímo nepřečte.

Django má session framework zabudovaný a na něm může stavět autentizaci. Konkrétní backend session se dá měnit; pro mentální model stačí rozlišit **serverový stav relace** a **identifikátor, který prohlížeč posílá**.

## 4.2 Autentizace odpovídá „kdo jsi?“, autorizace „co smíš?“

**Autentizace** ověřuje identitu. **Autorizace** rozhoduje o oprávnění k operaci nebo zdroji. Přihlášení úspěšně ověřeného studenta neznamená, že může upravovat účty učitelů.

Django poskytuje model uživatele, hashování hesel, přihlášení, skupiny a permissions. Vlastní aplikace může navíc definovat pravidla na úrovni objektu: editor může upravit článek své rubriky, ale ne cizí uzamčený článek.

Častou chybou je kontrola pouze v rozhraní. Tlačítko „Smazat“ se administrátorovi zobrazí a běžnému uživateli skryje, ale endpoint `/article/42/delete` neověří oprávnění. Útočník nepotřebuje tlačítko; požadavek může sestavit ručně. Správné pravidlo proto zní: **UI může funkci skrýt pro pohodlí, backend ji musí zakázat pro bezpečnost**.

## 4.3 Hesla, vícefaktorové ověřování a passkeys

Heslo se na serveru nemá ukládat v čitelné podobě. Ukládá se jeho výsledek z vhodné pomalé funkce pro odvozování hesel se solí. Frameworky jako Django tuto práci řeší za vývojáře a umožňují aktualizovat používaný algoritmus bez změny uživatelského rozhraní.

Vícefaktorové ověřování přidává další faktor, například jednorázový kód nebo hardwarový autentizátor. Moderní **passkeys** založené na WebAuthn používají kryptografický pár klíčů a mohou omezit riziko phishingu, protože přihlašovací údaj je vázán na konkrétní původ služby.

Není správné tvrdit, že **OAuth 2.0** je sám o sobě standard pro „přihlášení Googlem“. OAuth je primárně autorizační rámec pro delegovaný přístup. Pro autentizační identitu se nad ním typicky používá **OpenID Connect — OIDC**. Uživatel tento rozdíl ve formuláři nevidí, pro návrh systému je však zásadní.

Také **JWT** není automaticky „lepší session“. Je to formát podepsaného tokenu s tvrzeními. Může být vhodný v některých distribuovaných API, ale přináší vlastní otázky expirace, odvolání, uložení a velikosti. Pro klasickou serverovou aplikaci je session cookie často jednodušší a bezpečnější výchozí řešení.

# 5. Bezpečnost webové aplikace

## 5.1 Základní pravidlo: klientský vstup není důvěryhodný

Bezpečnost nezačíná seznamem názvů útoků. Začíná otázkou, kde systém přechází mezi různě důvěryhodnými částmi. HTTP požadavek, uploadovaný soubor, data z externího API i parametr v URL mohou být chybné nebo úmyslně škodlivé.

Aplikace proto kombinuje validaci vstupu, bezpečné zpracování, kontrolu oprávnění a správné kódování výstupu. Jedna univerzální funkce „sanitize všechno“ neexistuje. Řetězec, který je bezpečný jako prostý text v HTML, nemusí být bezpečný uvnitř JavaScriptu, URL nebo SQL dotazu. Obrana závisí na kontextu.

OWASP Top 10 se průběžně aktualizuje podle bezpečnostní praxe. Pro výuku je užitečnější rozumět mechanismům než memorovat pořadí kategorií. Zvlášť důležité jsou chyby v řízení přístupu, injection, bezpečnostní konfigurace, práce s kryptografií, autentizací a závislostmi.

## 5.2 XSS: když se data stanou kódem

**Cross-Site Scripting — XSS** vzniká, když aplikace vloží nedůvěryhodná data do stránky tak, že je prohlížeč interpretuje jako aktivní obsah. Představme si komentář, jehož text backend bez escapování vloží do HTML. Pokud vstup obsahuje skript nebo nebezpečný atribut, prohlížeč jej může spustit v kontextu legitimního webu.

Základní obranou je **output encoding** podle kontextu a bezpečné templatingové API. Django Templates běžný text automaticky escapují. Na klientu je vhodné při vkládání textu používat `textContent` místo `innerHTML`, pokud HTML skutečně nepotřebujeme.

**Content Security Policy — CSP** může omezit zdroje skriptů a ztížit využití některých XSS chyb. Je to důležitá další vrstva, ne omluva pro nebezpečné generování HTML.

## 5.3 SQL injection: dotaz není řetězec ke slepování

SQL injection vzniká, když se nedůvěryhodný vstup stane součástí syntaxe databázového dotazu. Obrana není „zakázat apostrof“, ale používat **parametrizované dotazy** nebo ORM, které hodnoty oddělí od struktury příkazu.

Django ORM při běžném použití parametry bezpečně předává databázovému ovladači. Riziko se vrací, když vývojář začne skládat raw SQL řetězce ručně. ORM tedy pomáhá, ale není magický štít proti libovolnému nebezpečnému kódu.

Stejný obecný princip platí i jinde: nedůvěryhodná data se nemají měnit v příkazy shellu, šablonu, URL redirectu nebo jiný interpretovaný kód bez správné hranice a validace.

## 5.4 CSRF: zneužití přihlášeného prohlížeče

**Cross-Site Request Forgery — CSRF** využívá skutečnosti, že prohlížeč může k požadavku automaticky připojit přihlašovací cookie. Útočný web se pokusí vyvolat změnový požadavek na jinou službu a využít tak už existující identitu oběti.

Django má CSRF ochranu vestavěnou. Formuláře s metodou POST používají CSRF token a middleware kontroluje, zda požadavek odpovídá očekávanému původu a tokenu. Atribut `SameSite` u cookie přidává další ochrannou vrstvu.

CSRF se liší od XSS. U XSS běží škodlivý obsah uvnitř důvěryhodné stránky. U CSRF se zvenčí zneužije skutečnost, že prohlížeč už má vztah s cílovou službou. Jedna chyba proto není „jiný název“ pro druhou.

## 5.5 Broken access control: nejde jen o přihlášení

Jednou z nejzávažnějších skupin chyb je špatné řízení přístupu. Uživatel může změnit ID v URL z `/invoice/100` na `/invoice/101` a server mu cizí fakturu vydá, protože ověřil pouze to, že je přihlášen. Tomu se někdy říká IDOR — Insecure Direct Object Reference — a spadá do širšího problému přístupových kontrol.

Správná kontrola se ptá nejen „je uživatel přihlášen?“, ale „má tento konkrétní uživatel právo provést tuto konkrétní operaci nad tímto konkrétním objektem?“.

Role-based přístup je jednoduchý model: administrátor, editor, čtenář. Jemnější systémy mohou pracovat s permissions nebo politikami založenými na vlastnostech uživatele, objektu a kontextu. Čím složitější pravidlo, tím důležitější jsou automatizované testy autorizace.

## 5.6 Bezpečnost konfigurace a závislostí

Aplikace může mít správný kód a přesto být nebezpečná kvůli provozu. Typickým příkladem je produkční server se zapnutým debug režimem, veřejným administrátorským rozhraním bez ochrany, uniklým `SECRET_KEY` nebo nepodporovanou knihovnou.

Tajné údaje nepatří do veřejného Git repozitáře. Produkční konfigurace používá bezpečné proměnné prostředí nebo secret manager. HTTPS má být standardem, nikoli volitelným „šifrovaným režimem“. Framework i databáze potřebují bezpečnostní aktualizace a tým musí vědět, jaké balíčky nasazuje.

Supply-chain bezpečnost získala na významu právě proto, že moderní aplikace používají stovky závislostí. Lockfile zlepšuje reprodukovatelnost, ale sám nezaručuje bezpečnost. Je potřeba sledovat aktualizace, původ balíčků a minimalizovat zbytečné závislosti.

# 6. CMS, nasazení a provoz

## 6.1 CMS je specializovaná webová aplikace

**CMS — Content Management System** umožňuje vytvářet, upravovat a publikovat obsah bez ručního editování HTML. WordPress je známý univerzální CMS v PHP, v ekosystému Pythonu existují systémy jako Django CMS nebo Wagtail. Redakční systém obvykle přidává workflow, role, média, šablony, revize a administraci.

Klasický CMS generuje veřejné stránky sám. **Headless CMS** odděluje správu obsahu od prezentační vrstvy a poskytuje obsah přes API. Jeden backend pak může zásobovat web, mobilní aplikaci i informační panel. Cena za flexibilitu je větší integrační složitost: někdo musí vytvořit frontend, řešit náhledy, cache, autentizaci a propojení při publikaci.

Page builder je jiný typ nástroje. Umožňuje vizuálně skládat layout a komponenty. Může urychlit práci editorů, ale při nekontrolovaném použití vytváří nekonzistentní design a složitá data. CMS proto není jen „program, ve kterém se kliká místo kódování“; je to systém pro správu obsahu a jeho životního cyklu.

## 6.2 PWA, SPA, serverless a další architektury

**Progressive Web App — PWA** je webová aplikace využívající schopnosti platformy tak, aby se v podporovaném prostředí chovala více jako instalovatelná aplikace. Service Worker může řídit cache a offline scénáře, manifest popisuje instalaci a Web APIs mohou podle oprávnění nabídnout další integraci.

PWA není jeden framework ani záruka offline funkčnosti. Vývojář musí přesně navrhnout, co se má stát bez sítě a jak se synchronizují změny. Offline formulář, který uživateli dovolí napsat dlouhý text a po obnovení spojení jej ztratí, není dobrá PWA jen proto, že má ikonu na ploše.

**Serverless** znamená, že vývojář nasazuje funkce nebo služby bez přímé správy dlouhodobě běžícího serveru. Servery samozřejmě fyzicky existují; provozuje je platforma. Výhodou je automatické škálování a účtování podle využití, nevýhodou mohou být limity prostředí, cold start, cena při určitých vzorech zátěže a závislost na platformě.

Mikroslužby rozdělují systém do samostatně nasaditelných služeb. Pro globální bankovní platformu mohou být vhodné, pro školní aplikaci se třemi tabulkami však mohou přinést více síťové a provozní složitosti než užitku. **Monolit není synonymum špatné architektury**. Dobře modulární monolit je často nejjednodušší výchozí řešení a službu lze oddělit teprve tehdy, když existuje skutečný provozní důvod.

## 6.3 Vývojový server není produkční server

Příkaz `python manage.py runserver` je určen pro vývoj. Produkční aplikace potřebuje konfiguraci, která počítá s bezpečností, paralelními požadavky, restartem procesu, logováním a statickými soubory.

Django lze provozovat přes **WSGI** nebo modernější **ASGI** rozhraní. WSGI je tradiční synchronní rozhraní Python webových aplikací. ASGI podporuje také asynchronní komunikaci a dlouhodobější spojení. Aktuální Django má asynchronní API v řadě částí, ale neznamená to, že je potřeba každou view automaticky přepsat na `async def`. Asynchronní přístup dává největší smysl u I/O scénářů, které z něj skutečně těží.

Před aplikačním serverem může stát reverzní proxy nebo cloudový load balancer, který ukončuje HTTPS, směruje provoz a obsluhuje cache. Databáze může běžet jako spravovaná služba. Statické soubory lze posílat přes CDN a uživatelská média ukládat do objektového úložiště.

## 6.4 Hosting, VPS, kontejnery a PaaS

Nejjednodušší webhosting bývá vhodný pro tradiční PHP nebo statické stránky, ale nemusí umožnit libovolně spouštět Pythonový proces. **VPS — Virtual Private Server** dává správci virtuální stroj a velkou kontrolu, zároveň však přenáší odpovědnost za aktualizace, firewall, zálohy a monitoring.

**Kontejner** zabalí aplikaci a její runtime závislosti do reprodukovatelného obrazu. Docker tím neřeší databázové zálohy ani bezpečnost automaticky; pomáhá především standardizovat prostředí mezi vývojem a produkcí.

**PaaS — Platform as a Service** umožňuje nasadit aplikaci bez správy většiny serverové infrastruktury. Platforma může zajistit build, HTTPS, restart procesů, logy a propojení s databází. Cloudové služby mohou poskytovat podobné funkce v různě modulární podobě.

Volba mezi VPS, kontejnerovou platformou a PaaS není soutěž o profesionalitu. Rozhoduje rozpočet, zkušenost týmu, požadovaná kontrola, způsob škálování a kritičnost služby.

## 6.5 Konfigurace produkce

Django produkce vyžaduje několik principů, které se nemají odkládat „na později“. `DEBUG` musí být vypnutý, `ALLOWED_HOSTS` omezuje přijímané hostnames a tajné klíče nemají být ve veřejném repozitáři. HTTPS musí být správně vynuceno a cookie mají odpovídat bezpečnostnímu režimu.

Nastavení se často odděluje podle prostředí: vývoj může používat lokální SQLite a debug nástroje, produkce PostgreSQL, externí úložiště a bezpečné secrets. Cílem není mít dva různé programy, ale stejný kód s kontrolovanou konfigurací.

Před nasazením je vhodné spouštět frameworkové systémové kontroly, testy a databázové migrace. Nasazení by mělo být opakovatelné: když server selže, tým má umět z dokumentovaného postupu nebo automatizovaného pipeline vytvořit nový.

## 6.6 Testování a automatizovaný průchod změny

Webovou aplikaci nelze spolehlivě ověřit jediným klikáním v prohlížeči. **Jednotkové testy** kontrolují malé části logiky, například pravidlo pro výpočet ceny nebo oprávnění uživatele. **Integrační testy** sledují spolupráci více částí, třeba view, databáze a autentizace. **End-to-end test** simuluje celý uživatelský scénář: přihlášení, vyplnění formuláře a zobrazení výsledku. Každý typ zachytí jinou třídu chyb a není účelné nahrazovat všechny pouze jedním obřím testem.

Praktický význam testů se ukáže při změně. Vývojář upraví model článku, vytvoří migraci a současně změní formulář. Lokálně vše vypadá správně, ale starší část aplikace stále očekává původní pole. Automatizovaný test může tuto regresi zachytit dříve, než se kód dostane k uživatelům. Stejný princip platí pro bezpečnostní chyby: test může ověřit, že anonymní uživatel nedostane odpověď s cizími daty a že editor nemůže provést administrátorskou operaci.

V týmovém projektu se tyto kontroly často zapojují do **CI/CD — Continuous Integration / Continuous Delivery nebo Deployment**. Po každé změně repozitáře systém sestaví prostředí, spustí testy, statické kontroly a podle pravidel připraví nebo provede nasazení. CI/CD není samo o sobě záruka kvality; automatizuje pouze kroky, které tým správně definoval. Jeho hlavní hodnota spočívá v opakovatelnosti: stejná změna prochází stejným kontrolním řetězcem bez ohledu na to, kdo ji vytvořil.

## 6.7 Provoz začíná po úspěšném deployi

Aplikace, která prošla lokálními testy, může v produkci narazit na reálný provoz. Potřebuje proto **monitoring**, logování, zálohy a plán obnovy. Logy mají pomoci zjistit, co se stalo, ale nemají bezmyšlenkovitě ukládat hesla, session tokeny nebo osobní údaje.

Databázová záloha má hodnotu teprve tehdy, když lze obnovu skutečně provést. Stejně důležité je vědět, kolik dat se při havárii smí ztratit a jak dlouho může služba stát. Malý školní projekt může mít jednoduchý denní backup, kritická aplikace potřebuje propracovanější strategii.

Cache může snížit zátěž databáze a urychlit odpovědi, ale vytváří otázku, kdy se má stará hodnota zneplatnit. CDN přiblíží statická data uživateli, ale dynamickou autorizovanou odpověď nelze bez rozmyslu veřejně cacheovat. Škálování tedy není jen „přidat další server“; musí respektovat stav, databázi a konzistenci.

## 6.8 AI jako další služba v architektuře

Současné webové aplikace stále častěji přidávají funkce založené na generativní AI: shrnutí článku, vyhledávání v přirozeném jazyce, klasifikaci, překlad nebo asistenta. Z architektonického pohledu je užitečné považovat model za další externí nebo interní službu s API, latencí, cenou, limity a chybovostí.

Výstup modelu není důvěryhodný programový příkaz jen proto, že vznikl uvnitř aplikace. Pokud AI vytvoří HTML, SQL, URL nebo argument pro další nástroj, musí projít stejnou kontrolou jako jiné nedůvěryhodné vstupy. Stejně tak citlivá data nemají být automaticky posílána cizí službě bez posouzení ochrany soukromí a smluvních podmínek.

AI tak nepřepisuje základní pravidla webového inženýrství. Naopak zvýrazňuje jejich význam: jasně definované rozhraní, validace, autorizace, audit a odpovědnost za výsledek zůstávají podstatné.

# Závěrečné propojení

Webová aplikace je spolupráce vrstev, které musí mít jasně rozdělenou odpovědnost. Prohlížeč zobrazuje rozhraní a posílá požadavky. Routing určuje, která část backendu je zpracuje. View nebo služba ověří vstup a oprávnění, model a ORM pracují s databází a šablona nebo API sestaví odpověď. Session a autentizace propojí jednotlivé požadavky s uživatelem a bezpečnostní mechanismy chrání hranice mezi nedůvěryhodným vstupem a citlivou operací.

Celý cyklus lze shrnout:

**požadavek → routing → autentizace a autorizace → aplikační logika → ORM/databáze → odpověď → render → další uživatelská akce**

Framework jako Django tento proces výrazně usnadňuje, ale nenahrazuje porozumění principům. ORM neodstraňuje potřebu rozumět databázi, automatické escapování neznamená konec XSS a vestavěné přihlášení neřeší chybně navržená oprávnění. Stejně tak Docker, cloud nebo serverless neodstraňují provozní odpovědnost — pouze ji jinak rozdělují.

Nejdůležitější schopností proto není zapamatovat si soubor `views.py` nebo jeden příkaz pro deploy. Je to schopnost sledovat, **kde se data právě nacházejí, kdo jim může věřit, kdo o jejich použití rozhoduje a co se stane při chybě**. Tento mentální model zůstane platný i tehdy, až konkrétní frameworky a cloudové služby vystřídají nové generace nástrojů.

## Referenční zdroje pro další studium

- Django Documentation — https://docs.djangoproject.com/
- OWASP Top 10 — https://owasp.org/Top10/
- OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/
- MDN Web Security — https://developer.mozilla.org/en-US/docs/Web/Security
- WebAuthn — https://www.w3.org/TR/webauthn-3/
