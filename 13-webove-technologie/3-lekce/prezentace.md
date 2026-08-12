## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Jak připojit JavaScript k HTML**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


JavaScript lze vložit přímo do HTML:

```html
<script>
  console.log("Ahoj");
</script>
```

Ve větších projektech je ale lepší použít samostatný soubor:

```html
<script src="app.js"></script>
```

Pokud skript pracuje s prvky stránky, je vhodné zajistit, aby HTML bylo nejprve načteno. Jednou z možností je atribut `defer`:

```html
<script src="app.js" defer></script>
```

Moderní moduly lze načíst:

```html
<script type="module" src="app.js"></script>
```

Moduly podporují `import` a `export` a mají vlastní scope.

```js
// math.js
export function add(a, b) {
  return a + b;
}
```

```js
// app.js
import { add } from "./math.js";
console.log(add(2, 3));
```

***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**DOM — Document Object Model**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


HTML soubor je text. Prohlížeč jej ale při načítání **parsuje** a vytváří z něj v paměti objektovou stromovou strukturu nazývanou **DOM — Document Object Model**.

Máme-li například:

```html
<body>
  <h1>Webové technologie</h1>
  <p id="info">Úvodní text</p>
</body>
```

můžeme si část DOM představit:

```text
document
└── html
    └── body
        ├── h1
        └── p#info
```

Každá část dokumentu je reprezentována uzlem. HTML elementy jsou jedním druhem uzlů; dalšími mohou být například textové uzly. Objekt `document` představuje vstupní bod k právě načtenému dokumentu.

JavaScript může element vyhledat:

```js
const paragraph = document.querySelector("#info");
```

`querySelector()` přijímá CSS selektor a vrátí první odpovídající element. Pro více prvků existuje `querySelectorAll()`:

```js
const items = document.querySelectorAll("li.active");
```

Důležité je rozlišovat **zdrojový HTML soubor** a **aktuální DOM**. JavaScript může DOM po načtení změnit, aniž by se tím přepsal původní HTML soubor na serveru. Vývojářské nástroje prohlížeče proto mohou ukazovat jinou strukturu, než jaká byla původně zapsána ve zdrojovém kódu.

DOM není pouze „seznam tagů“. Je to programové rozhraní. Elementy mají vlastnosti a metody:

```js
paragraph.textContent = "Nový text";
paragraph.classList.add("important");
```

Lze také vytvářet nové elementy:

```js
const item = document.createElement("li");
item.textContent = "Nová položka";

document.querySelector("ul").append(item);
```

Užitečné je také rozlišovat **atribut v HTML** a **vlastnost objektu DOM**. Často spolu souvisejí, ale nejsou vždy totožné. Například `<input value="A">` obsahuje atribut s výchozí hodnotou, zatímco vlastnost `input.value` se může během práce uživatele měnit.

DOM tak vytváří most mezi statickou strukturou HTML a programovým chováním JavaScriptu.

***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**BOM — Browser Object Model**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


DOM popisuje dokument, ale webový prohlížeč poskytuje JavaScriptu i další informace a funkce, které se netýkají přímo HTML stránky. Tradičně se pro ně používá označení **BOM — Browser Object Model**.

Na rozdíl od DOM není BOM jedním přesně uzavřeným modelem s jedinou standardní specifikací. Je to spíše historické a didakticky užitečné označení pro objekty prohlížeče mimo samotný dokument.

V běžném skriptu je nejdůležitější globální objekt **`window`**. Reprezentuje okno nebo kontext prohlížeče a zpřístupňuje mnoho dalších API. Například:

```js
window.location
window.history
window.navigator
window.document
```

V prohlížeči lze často `window.` vynechat:

```js
console.log(location.href);
```

**`location`** obsahuje informace o aktuální URL a umožňuje navigaci:

```js
console.log(location.hostname);
```

**`history`** poskytuje práci s historií aktuálního tabu. Moderní aplikace jej mohou využívat například ke změně URL bez úplného načtení nové stránky.

**`navigator`** poskytuje informace a vybrané možnosti prostředí prohlížeče. Přes související Web APIs lze například zjišťovat stav připojení nebo po svolení uživatele využít některé schopnosti zařízení.

Objekt **`screen`** popisuje vlastnosti obrazovky, i když pro responzivní návrh stránky se obvykle neřídíme přímo fyzickým rozlišením monitoru, ale velikostí dostupného viewportu a CSS media queries.

Rozdíl mezi DOM a BOM lze zjednodušit takto:

```text
DOM → dokument a jeho elementy
BOM → prostředí prohlížeče kolem dokumentu
```

V současné dokumentaci se častěji mluví konkrétně o jednotlivých **Web APIs** než o BOM jako jednom celku. Pojem BOM je přesto užitečný pro pochopení, proč například `document` pracuje se stránkou, zatímco `location` nebo `history` pracují s prohlížečem a navigací.

***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Dynamický web — změna elementů**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Za **dynamický** označujeme web, jehož obsah nebo stav se může měnit podle dat, času nebo činnosti uživatele. JavaScript k tomu na klientské straně používá především DOM.

Může změnit text:

```js
const heading = document.querySelector("h1");
heading.textContent = "Nový nadpis";
```

může upravit CSS třídy:

```js
heading.classList.add("highlight");
heading.classList.remove("hidden");
```

může změnit atribut:

```js
const image = document.querySelector("img");
image.alt = "Schéma klient–server";
```

a může vytvořit nebo odstranit celý element:

```js
const item = document.createElement("li");
item.textContent = "Nová položka";

document.querySelector("ul").append(item);
```

Změna DOM se projeví při dalším vykreslení stránky, aniž by prohlížeč musel načíst nový HTML dokument ze serveru.

Při vkládání obsahu je důležité rozlišovat `textContent` a `innerHTML`. `textContent` vloží obyčejný text:

```js
message.textContent = userInput;
```

`innerHTML` naopak řetězec interpretuje jako HTML:

```js
message.innerHTML = "<strong>Důležité</strong>";
```

Pokud do `innerHTML` vložíme neověřený text od uživatele nebo z nedůvěryhodného zdroje, může se stát součástí stránky i škodlivý kód. Proto se pro běžný text preferuje `textContent` nebo bezpečné vytváření elementů přes DOM API.

***

## Snímek 3.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Interaktivní web — události**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Dynamická změna stránky sama o sobě nestačí. Aby web reagoval na člověka, potřebuje **události — events**. Událost oznamuje, že se něco stalo: uživatel klikl, stiskl klávesu, změnil hodnotu formuláře, odeslal formulář nebo se dokončilo načtení určitého zdroje.

Na událost lze připojit **event listener**, tedy funkci, která se má při dané události vykonat:

```js
const button = document.querySelector("#send");

button.addEventListener("click", () => {
  console.log("Uživatel klikl.");
});
```

Listener může získat **objekt události** s podrobnostmi:

```js
button.addEventListener("click", event => {
  console.log(event.target);
});
```

`event.target` ukazuje prvek, na němž událost vznikla.

U formuláře může JavaScript zachytit odeslání:

```js
form.addEventListener("submit", event => {
  event.preventDefault();
  console.log("Odeslání převzal JavaScript.");
});
```

`preventDefault()` zabrání výchozí akci prohlížeče. U formuláře to typicky znamená, že se neprovede klasická navigace podle atributů `action` a `method`. Skript pak může například data zkontrolovat a odeslat přes Fetch API.

Události se mohou ve stromu DOM **šířit**. Často vzniknou na konkrétním elementu a následně „probublávají“ k jeho předkům. Díky tomu lze například jeden listener na seznamu použít pro mnoho položek uvnitř. Tomuto přístupu se říká **event delegation**.

Interaktivní frontend lze proto chápat jako opakující se cyklus:

```text
událost → obslužná funkce → změna stavu nebo dat → změna DOM → nový obraz stránky
```

***
