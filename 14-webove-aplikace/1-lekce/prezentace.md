## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Od statické stránky k systému se stavem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny. Webová aplikace naproti tomu často vytváří odpověď podle uživatele, dat a aktuálního stavu systému. Stejná adresa `/profil` může po přihlášení zobrazit údaje konkrétního člověka, zatímco nepřihlášeného uživatele přesměruje na přihlašovací stránku.

Jednoduchá webová aplikace se dá rozdělit na tři logické vrstvy. **Prezentační vrstva** vytváří uživatelské rozhraní. **Aplikační vrstva** rozhoduje, co se má při požadavku stát. **Datová vrstva** ukládá a zpřístupňuje data. V reálném systému mohou být vrstvy rozděleny mezi více procesů nebo služeb, ale jejich oddělení je užitečné i v malém projektu.

Představme si redakční systém. Uživatel otevře formulář pro nový článek. HTML formulář patří do prezentační vrstvy. Po odeslání backend zkontroluje, zda je uživatel přihlášen, zda má právo publikovat, zda nechybí titulek a zda je zvolená kategorie platná. Datová vrstva pak uloží článek a vztahy k autorovi a kategorii. Samotné tlačítko „Publikovat“ tedy nepublikuje nic; pouze vyvolá požadavek, který musí bezpečně projít celým systémem.

Tento příklad ukazuje důležitou hranici: **frontend může požádat, backend rozhoduje**. Uživatel si může HTML a JavaScript ve svém prohlížeči změnit. Nelze proto spoléhat na to, že skryté tlačítko zabrání neoprávněné operaci. Server musí oprávnění ověřit při každém citlivém požadavku.

***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**MVC a příbuzné návrhové vzory**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Mnoho frameworků používá architektonické myšlenky odvozené od **MVC — Model–View–Controller**. Model reprezentuje data a pravidla kolem nich, view prezentuje výsledek a controller zpracuje vstup a koordinuje další části.

Webové frameworky však používají názvy různě. Django tradičně mluví o **Model–Template–View (MTV/MVT)**. Django `Model` popisuje datovou strukturu a práci s databází, `Template` generuje prezentační výstup a Django `View` přijme požadavek a vrátí odpověď. Funkce či třída označená v Django jako view tedy vykonává část role, kterou by v klasickém popisu MVC lidé často spojili s controllerem.

Není proto užitečné vést spor, zda je Django „opravdu MVC“ nebo „opravdu MVT“. Podstatný je princip **separation of concerns**: databázová logika nemá být bezdůvodně rozeseta v HTML šablonách, routování nemá obsahovat celý obchodní proces a jeden obří soubor nemá řešit vše od přihlášení po generování PDF.

Dobré rozdělení zjednodušuje testování. Model lze ověřit bez prohlížeče, view bez skutečné šablony a šablonu s připravenými daty. Když se změní databáze nebo vzhled stránky, nemusí se automaticky přepisovat celý systém.

***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Server-side rendering, client-side rendering a hybridní web**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Klasická serverová aplikace vytvoří HTML na serveru. Prohlížeč požádá například o `/clanky/42`, backend načte data, vybere šablonu a vrátí hotový dokument. Tento přístup se označuje jako **server-side rendering — SSR**.

U **client-side rendering — CSR** server může poslat základ aplikace a JavaScript následně přes API načte data a sestaví rozhraní v prohlížeči. Tak funguje mnoho Single Page Applications. Výhodou může být velmi interaktivní prostředí, nevýhodou větší množství klientského kódu, složitější počáteční načítání a nutnost dobře řešit navigaci, chyby a přístupnost.

Současné frameworky často kombinují více přístupů. Některé stránky lze vygenerovat předem jako **SSG — Static Site Generation**, jiné renderovat na serveru při požadavku a po načtení „hydratovat“ klientským JavaScriptem. Další architektury posílají do prohlížeče jen JavaScript pro skutečně interaktivní části. Není proto správné chápat SPA jako automaticky modernější než serverové šablony. Vhodná architektura závisí na typu aplikace.

Pro školní redakční systém s formuláři a běžnými články může být serverové renderování velmi efektivní a jednoduché. Pro grafický editor v prohlížeči bude naopak významná část logiky přirozeně na klientovi.

# 2. Django jako konkrétní příklad backendového frameworku

***
