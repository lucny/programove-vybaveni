## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Projekt, aplikace a cesta požadavku**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Django** je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů. Je vhodným výukovým příkladem proto, že ukazuje většinu vrstev webové aplikace v jednom konzistentním systému.

Django rozlišuje **project** a **app**. Projekt představuje konfiguraci celého webu. App je logicky související část, například články, uživatelské profily nebo katalog. Jeden projekt může obsahovat více apps a jedna app může být znovupoužitelná ve více projektech.

Typická struktura obsahuje konfigurační modul se `settings.py`, hlavní routování v `urls.py` a vstupní body `wsgi.py` a `asgi.py`. Jednotlivá app mívá například `models.py`, `views.py`, vlastní `urls.py`, šablony a testy. Příkaz `manage.py` poskytuje rozhraní pro správní úlohy.

Při požadavku se zjednodušeně děje toto:

**HTTP request → middleware → URL resolver → view → model/služby → template nebo JSON → HTTP response**

Middleware může řešit bezpečnost, sessions, autentizaci nebo jiné společné operace. URL resolver vybere view podle cesty. View zpracuje požadavek, případně použije ORM a nakonec vytvoří odpověď.

***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Model a ORM: objektový pohled na relační databázi**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Migrace: databázové schéma má historii**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Když do modelu přidáme pole `summary`, databáze se sama bezpečně nezmění jen proto, že Pythonová třída vypadá jinak. Django používá **migrace** — verzované popisy změn schématu.

Příkaz `makemigrations` vytvoří návrh migrace a `migrate` ji aplikuje na databázi. Migrace mohou vytvářet tabulky, přidávat sloupce, měnit indexy nebo provádět definované datové transformace.

Je užitečné chápat migraci jako podobu verzovacího systému pro strukturu databáze. Kód aplikace a schéma musí postupovat společně. Když tým stáhne novou verzi projektu, nestačí jen aktualizovat `.py` soubory; často musí aplikovat také příslušné migrace.

V produkci je změna schématu citlivá operace. Přidat povinný sloupec do tabulky se stovkami milionů řádků může mít zcela jiný dopad než totéž ve školní SQLite databázi. Framework migraci popíše, ale provozní riziko musí posoudit člověk.

***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Routing a views**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Administrace a CRUD: rychlý nástroj, ne náhrada veřejného rozhraní**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Jednou z praktických předností Djanga je automaticky generované **administrační rozhraní**. Jakmile jsou vytvořeny modely a správně nastavena oprávnění, lze v administraci relativně rychle prohlížet, přidávat, upravovat a mazat záznamy. Typické operace se shrnují zkratkou **CRUD — Create, Read, Update, Delete**. Pro redakční systém tak lze bez psaní celého vlastního editoru vytvořit pracovní prostředí, v němž správce založí autora, upraví článek nebo změní kategorii.

Tato pohodlnost ale snadno svádí k chybnému mentálnímu modelu. Django admin není automaticky hotové veřejné uživatelské rozhraní aplikace a už vůbec ne bezpečnostní vrstva, která by vyřešila všechna oprávnění za vývojáře. Je navržen hlavně jako interní nástroj pro důvěryhodné pracovníky. Veřejný e-shop, školní portál nebo redakční web obvykle potřebuje vlastní views, formuláře, API a především pravidla, která přesně určují, kdo smí kterou operaci provést.

Stejně důležité je oddělit CRUD od skutečné aplikační logiky. Operace „smazat článek“ může ve skutečném systému znamenat kontrolu role uživatele, vytvoření auditního záznamu, odebrání stránky z veřejného webu a případně zachování verze pro obnovu. Jednoduché tlačítko tedy může spustit více pravidel než jediný SQL příkaz `DELETE`. Framework urychluje rutinní práci, ale význam operace musí stále navrhnout člověk.

# 3. Šablony, formuláře a vstupní data

***
