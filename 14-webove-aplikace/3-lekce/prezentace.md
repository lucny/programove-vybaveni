## Snímek 3.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Šablona kombinuje strukturu a data, ne celou aplikační logiku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Formulář: pohodlí pro uživatele, nedůvěra pro server**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 3.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Regulární výraz je nástroj, ne univerzální validátor**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Regulární výrazy — regular expressions, regex** popisují vzory v textu. Hodí se pro vyhledání identifikátoru, kontrolu jednoduchého formátu nebo rozdělení logu. Základní konstrukce zahrnují množiny znaků, skupiny, alternativy a kvantifikátory.

```text
^[A-Z]{3}-\d{4}$
```

Tento vzor může například odpovídat školnímu inventárnímu kódu `ABC-1234`. Pro takto přesně definované lokální pravidlo je regex vhodný.

Není však dobrý nápad psát obrovský vlastní regulární výraz, který má „dokonale ověřit každou platnou e-mailovou adresu podle všech standardů“. Pro běžné účely je často lepší použít frameworkovou validaci a skutečné potvrzení adresy zasláním odkazu. Podobně složité parsování HTML nebo programovacího jazyka patří parseru, ne jediné řádce regexu.

***

## Snímek 3.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Soubory, statická data a uživatelská média**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Webová aplikace pracuje se dvěma odlišnými skupinami souborů. **Static files** jsou součástí aplikace: CSS, JavaScript, ikony nebo vlastní fonty. **Media files** vznikají od uživatelů nebo editorů: fotografie článků, přílohy či avatary.

Rozlišení je důležité pro bezpečnost i deployment. Statické soubory lze při nasazení sesbírat, verzovat a doručovat přes CDN. Uživatelská média musí mít vlastní úložiště, zálohy, kontrolu oprávnění a někdy bezpečnostní skenování.

Uploadovaný soubor není důvěryhodný jen proto, že má příponu `.jpg`. Server může kontrolovat velikost, očekávaný typ a způsob dalšího zpracování. Citlivé soubory by neměly být automaticky veřejné jen proto, že leží v adresáři dostupném webovým serverem.

# 4. Stav, autentizace a autorizace

***
