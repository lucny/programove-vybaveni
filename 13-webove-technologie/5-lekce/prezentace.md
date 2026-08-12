## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Webová API**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**API — Application Programming Interface** je rozhraní, přes které jeden program využívá funkce nebo data jiného programu. **Webové API** zpřístupňuje takové rozhraní přes síť, nejčastěji pomocí HTTP.

Je užitečné si představit API jako smlouvu. Klient musí vědět:

- na jakou adresu má požadavek poslat,
- jakou HTTP metodu použít,
- jaká data má přiložit,
- jakou odpověď může očekávat,
- jak jsou hlášeny chyby,
- zda je nutná autentizace.

Webové API je užitečné proto, že odděluje **způsob zobrazení** od **způsobu zpracování dat**. Stejný backend pak může používat webový frontend, mobilní aplikace nebo jiný server.

API může být **interní**, určené pro části jednoho systému, nebo **veřejné**, určené pro cizí vývojáře. Může používat různé styly a protokoly. Běžně se setkáme s REST API, GraphQL, RPC rozhraními nebo s dlouhodobou komunikací pomocí WebSocketu.

Samotná existence API neříká, kdo má právo jej používat. Přístup může být veřejný, omezený přihlášením, tokenem, API klíčem nebo jiným způsobem autentizace.

***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**AJAX a Fetch API**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Původní web fungoval převážně tak, že každá důležitá akce načetla nový HTML dokument. **AJAX — Asynchronous JavaScript and XML** přinesl možnost, aby JavaScript poslal požadavek na pozadí, získal data a změnil jen potřebnou část stránky.

Historický název obsahuje XML, ale dnešní aplikace velmi často používají JSON. Starší API `XMLHttpRequest` je stále dostupné, pro nový kód se však běžně používá **Fetch API**.

Jednoduché načtení:

```js
const response = await fetch("/api/articles");

if (!response.ok) {
  throw new Error(`HTTP ${response.status}`);
}

const articles = await response.json();
```

Objekt `response` nejprve reprezentuje HTTP odpověď. Teprve volání `response.json()` přečte její tělo a převede JSON na JavaScriptové hodnoty.

Odeslání JSON dat může vypadat:

```js
const response = await fetch("/api/articles", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    title: "Nový článek"
  })
});
```

Fetch se používá například pro živé vyhledávání, průběžné filtrování, ukládání formuláře bez reloadu, načítání další stránky výsledků nebo aktualizaci dashboardu.

Důležitá zvláštnost: `fetch()` obvykle neodmítne Promise jen proto, že server odpověděl stavem 404 nebo 500. Síťové spojení proběhlo a server odpověděl; klient proto musí stav zkontrolovat přes `response.ok` nebo `response.status`.

Při komunikaci s jiným originem může prohlížeč uplatnit **CORS**. Jde o pravidla určující, zda smí skript z jedné webové origin číst odpověď jiné služby. CORS není náhradou autentizace backendu.

***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**REST API**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**REST — Representational State Transfer** je architektonický styl pro síťové aplikace. V praxi se tím často myslí HTTP API, které pracuje se **zdroji — resources**. Zdrojem může být článek, uživatel, produkt nebo objednávka.

Zdroj je dostupný přes endpoint. Například:

```text
/api/articles
/api/articles/42
```

První cesta označuje kolekci článků, druhá konkrétní článek. Identifikátor `42` je součástí cesty a často se označuje jako **path parameter**.

Akci nad zdrojem vyjadřuje HTTP metoda:

```text
GET     /api/articles       načtení seznamu
GET     /api/articles/42    načtení jednoho článku
POST    /api/articles       vytvoření nového článku
PATCH   /api/articles/42    částečná změna článku
DELETE  /api/articles/42    odstranění článku
```

Pro filtrování nebo doplňující volby se často používají **query parameters**:

```text
GET /api/articles?published=true&page=2
```

REST API běžně přenáší reprezentaci zdroje jako JSON:

```json
{
  "id": 42,
  "title": "Webové technologie",
  "published": true
}
```

HTTP stavový kód oznamuje základní výsledek požadavku:

```text
200 OK             úspěch
201 Created        zdroj byl vytvořen
400 Bad Request    neplatný požadavek
401 Unauthorized   chybí platné přihlášení / autentizace
403 Forbidden      identita je známa, ale nemá oprávnění
404 Not Found      zdroj nebyl nalezen
500 Internal Server Error  chyba na straně serveru
```

Dobře navržené API používá metody, cesty a stavy konzistentně. Klient pak nemusí znát vnitřní strukturu backendu; spoléhá na veřejný kontrakt API.

### API klíče a přístupové tokeny

Některé služby vyžadují **API klíč**. Ten identifikuje aplikaci nebo odběratele služby a může sloužit například k měření spotřeby nebo omezení přístupu.

Jiné systémy používají **access token**, který může reprezentovat konkrétního přihlášeného uživatele a jeho oprávnění. Pojmy nejsou totožné, i když se oba v požadavku často posílají v HTTP hlavičce.

Například:

```text
Authorization: Bearer <token>
```

Citlivý tajný klíč nelze bezpečně schovat do veřejného JavaScriptu v prohlížeči. Uživatel má kód frontendu pod kontrolou. Tajemství proto obvykle uchovává backend a klient komunikuje přes něj.

REST není jediný správný návrh API. Jeho hlavní síla spočívá v jednoduchém modelu zdrojů a v dobrém využití vlastností HTTP.

***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**REST API v praxi**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


REST API umožňuje oddělit zdroj dat od aplikace, která je zobrazuje.

### Počasí

Frontend může požádat meteorologickou službu:

```text
GET /api/weather?city=Opava
```

a získat:

```json
{
  "temperature": 22.4,
  "condition": "cloudy"
}
```

### E-shop

```text
GET  /api/products
GET  /api/products/125
POST /api/orders
```

Webový frontend i mobilní aplikace mohou používat stejné produktové a objednávkové API.

### Školní systém

```text
GET  /api/classes/3A/students
GET  /api/students/125
POST /api/grades
```

Backend přitom musí kontrolovat oprávnění. To, že frontend zná endpoint pro známky, neznamená, že každý uživatel smí známku vytvořit.

### Služby třetích stran

REST API se používá také pro mapy, překlady, platební služby, cloudová úložiště nebo informační systémy. Při použití cizího API je třeba číst dokumentaci: popisuje endpointy, parametry, metody, formát dat, autentizaci, limity počtu požadavků a chybové odpovědi.

Důležitou dovedností proto není naučit se konkrétní URL zpaměti, ale umět z dokumentace pochopit kontrakt služby a sestavit správný požadavek.

***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**GraphQL**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**GraphQL** je jiný způsob zpřístupnění dat přes API. Zatímco REST často nabízí více endpointů pro různé zdroje, GraphQL obvykle poskytuje jednotné rozhraní se **schématem**, které popisuje dostupné typy a vztahy.

Klient v dotazu přesně uvede, která pole potřebuje:

```graphql
{
  article(id: 42) {
    title
    author {
      name
    }
  }
}
```

Server může vrátit například jen požadovaná data:

```json
{
  "data": {
    "article": {
      "title": "Webové technologie",
      "author": {
        "name": "Eva Nováková"
      }
    }
  }
}
```

Výhodou je flexibilita klienta. Mobilní aplikace může chtít menší množství polí než desktopové rozhraní a nemusí kvůli tomu vznikat nový REST endpoint.

Tato pružnost má cenu. Server musí řídit schéma, validovat dotazy, řešit autorizaci a hlídat, aby klient nevytvořil nepřiměřeně náročný dotaz. GraphQL proto není „lepší REST“, ale jiný návrhový přístup vhodný zejména pro systémy s bohatě propojenými daty a různými klienty.

***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**WebSocket a Socket.IO**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Běžná komunikace přes HTTP je založena na modelu **požadavek → odpověď**. Klient se zeptá a server odpoví. U chatu, multiplayerové hry nebo společné editace ale server často potřebuje poslat zprávu okamžitě, aniž by klient pokaždé předem vytvořil nový požadavek.

**WebSocket** umožňuje po úvodním navázání vytvořit dlouhodobý obousměrný komunikační kanál:

```text
klient ⇄ server
```

Klient může spojení vytvořit:

```js
const socket = new WebSocket("wss://example.com/socket");
```

Poté může reagovat na příchozí zprávy:

```js
socket.addEventListener("message", event => {
  console.log(event.data);
});
```

A může také zprávy posílat:

```js
socket.send("Ahoj");
```

WebSocket je vhodný například pro:

- chat,
- online hry,
- živé sledování stavu,
- společnou editaci,
- okamžité notifikace.

Nad touto oblastí existují knihovny s vyšší úrovní abstrakce. Známým příkladem je **Socket.IO**. Nabízí pohodlný událostní model, opětovné připojení, místnosti a další funkce užitečné pro aplikace v reálném čase.

Socket.IO není totéž jako samotný standard WebSocket. Je to knihovna a vlastní komunikační vrstva, která může WebSocket využívat. Toto rozlišení je důležité při propojování klientů a serverů různých technologií.

***
