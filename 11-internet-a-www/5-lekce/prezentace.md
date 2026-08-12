## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Vyhledávače: od katalogů k odpovědním systémům**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Vyhledávač už nezobrazuje jen seznam modrých odkazů. Kombinuje webové stránky, mapy, videa, databáze, reklamy a někdy generované souhrny. Čím pohodlnější je odpověď přímo ve výsledcích, tím důležitější je poznat její původ, ověřit zdroje a rozlišit vyhledání dokumentu od odpovědi vytvořené modelem.

První webové katalogy třídily odkazy ručně podle kategorií. Moderní vyhledávače automaticky procházejí web, vytvářejí index a řadí výsledky. Výsledková stránka může obsahovat organické odkazy, reklamy, mapy, obrázky, rychlé odpovědi i AI souhrny.

Vyhledávač není neutrální zrcadlo webu; vybírá a řadí pomocí pravidel, modelů a dostupných dat. Výsledek mohou ovlivnit dotaz, jazyk, region, zařízení, aktuálnost, nastavení a někdy historie či účet. Personalizace není u všech služeb stejná a „stejný výsledek pro všechny“ nelze obecně slíbit.

Generovaný souhrn může kombinovat více zdrojů, ale může také chybovat nebo špatně citovat. U zdraví, práva, financí a dalších závažných témat je nutné otevřít původní důvěryhodné zdroje. Reklamní výsledek má být označen a jeho umístění není důkaz odbornosti.

Google, Bing, Seznam.cz, DuckDuckGo a Ecosia se liší zdroji výsledků, funkcemi, obchodním modelem i ochranou soukromí. Tržní podíly se mění podle země, zařízení a metodiky; procento bez zdroje a data není spolehlivý údaj.

***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Procházení webu: crawling**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Vyhledávač nemůže zařadit stránku, o které neví. Automatizovaný crawler proto navštěvuje známé adresy, načítá obsah, sleduje odkazy a plánuje další návštěvy. Neprochází však celý web nepřetržitě a stránka bez odkazů není nutně neviditelná — lze ji objevit také ze sitemap, ručního odeslání či jiných signálů.

**Crawler**, robot nebo spider je automatický klient, který stahuje webové zdroje. Začíná seznamem známých URL a frontou adres určených k návštěvě. Nové URL objevuje z odkazů, sitemap a dalších zdrojů.

Crawler rozhoduje, co a jak často navštíví; kapacita a ohleduplnost k serveru jsou omezené. HTTP kódy, přesměrování, DNS chyby a rychlost serveru ovlivňují procházení. `robots.txt` dává crawlerům pokyny, které cesty smějí požadovat; není bezpečnostní bariéra.

Zákaz crawlování automaticky nezaručuje odstranění URL z výsledků. Pro zákaz indexace se používá například `noindex`, který ale crawler musí moci načíst. XML sitemap usnadňuje oznámení důležitých nebo změněných URL, nezaručuje indexaci.

Odkazy by měly být technicky dostupné crawlerům a mít smysluplný text. JavaScriptový web může vyžadovat vykreslení; složitost může objevování a analýzu zpomalit. Googlebot, Bingbot, SeznamBot a DuckDuckBot jsou příklady crawlerů různých služeb.

***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Indexace: vyhledatelný rejstřík webu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Při každém dotazu vyhledávač neprochází miliardy webů znovu. Pracuje s předem vytvořeným indexem, podobně jako čtenář s rejstříkem knihy. Do něj ukládá zpracované informace o dokumentech, jejich obsahu, jazyku, odkazech a dalších znacích. Nalezení crawlerem však ještě neznamená indexaci ani zobrazení ve výsledcích.

**Crawling** získává zdroje; **indexace** analyzuje a organizuje informace pro vyhledávání. Vyhledávač obvykle neukládá jen „kopii celého webu“, ale různé reprezentace, signály a někdy cache. Při analýze rozpoznává text, titulky, jazyk, odkazy, obrázky, strukturovaná data a další prvky.

Duplicity a velmi podobné URL může seskupit a vybrat **kanonickou** verzi. `rel="canonical"` je doporučení, nikoli absolutní příkaz. Direktiva `noindex` žádá, aby stránka nebyla ve výsledcích.

`robots.txt` řídí crawling; není správným nástrojem pro spolehlivé `noindex`. K indexaci nemusí dojít kvůli nízké kvalitě, duplicitě, chybě, blokování či nedostupnosti. Dynamický obsah musí být pro crawler technicky získatelný a srozumitelný.

Strukturovaná data pomáhají popsat význam, ale nezaručují rozšířený výsledek ani lepší pozici. Index se průběžně aktualizuje; starý výsledek může přetrvat do dalšího zpracování.

***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Ranking: jak vyhledávač řadí výsledky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Index může obsahovat mnoho dokumentů odpovídajících stejnému dotazu. Ranking z nich vytvoří pořadí, které se snaží nabídnout užitečnou odpověď. Přesné algoritmy nejsou veřejným jednoduchým vzorcem a mění se. Klíčová slova ani odkazy proto samy o sobě nestačí; důležité jsou záměr, kvalita, kontext a použitelnost.

**Ranking** řadí kandidátní výsledky pro konkrétní dotaz. Relevance vyjadřuje, jak dobře dokument odpovídá významu a záměru dotazu. Systémy mohou hodnotit jazyk, lokalitu, aktuálnost, typ obsahu a mnoho dalších signálů.

Odkazy mohou fungovat jako signál důležitosti, ale hodnotí se kontext a kvalita, ne jen počet. **PageRank** je historicky významný odkazový algoritmus, nikoli úplný popis dnešního rankingu. E‑E‑A‑T je koncept pro hodnocení kvality a důvěryhodnosti, nikoli jeden veřejný číselný „ranking faktor“.

U citlivých YMYL témat je důvěryhodnost zdroje zvlášť důležitá. Výsledek může ovlivnit zařízení, jazyk, přibližná poloha a nastavení. Vysoká pozice nedokazuje pravdivost a nízká pozice nedokazuje nepravdivost.

Manipulativní odkazy, skrytý text a obsah vytvořený jen pro algoritmy mohou porušovat pravidla spamu. Kvalitní obsah má uspokojit potřebu člověka, uvést zdroje a umožnit posoudit autora či provozovatele.

***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**SEO a placené vyhledávání**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Výsledková stránka kombinuje algoritmicky řazené odkazy s placenými reklamami. SEO pomáhá vyhledávačům i lidem pochopit a najít web; placené kampaně kupují reklamní prostor podle aukčních a kvalitativních pravidel. Ani jedno není záruka důvěryhodnosti a „SEO je zdarma“ je zjednodušení — neplatí se za organický klik, ale kvalitní obsah i technická správa stojí čas a peníze.

**SEO** je optimalizace viditelnosti webu v neplacených výsledcích. SEO pomáhá crawlerům objevit obsah, vyhledávači jej pochopit a uživateli vybrat výsledek. Organická pozice se nekupuje přímo od vyhledávače.

SEO není zdarma: vyžaduje výzkum, tvorbu obsahu, vývoj, měření a údržbu. **SEM** se používá různě; v praxi často označuje placený search marketing, širší význam může zahrnovat i SEO. Placené výsledky mají být označeny jako reklama nebo sponzorovaný obsah.

U PPC inzerent obvykle platí za kliknutí, ale existují i jiné modely účtování. Pořadí reklamy nemusí určovat jen nejvyšší nabídka; roli hraje kvalita a relevance. Organické výsledky mohou přinášet dlouhodobou návštěvnost, ale pozice nejsou trvalé ani garantované.

Kvalitní SEO staví na užitečném originálním obsahu, přístupnosti, rychlosti, mobilní použitelnosti a technické správnosti. **Keyword stuffing**, kupování manipulativních odkazů a klamavé stránky jsou rizikové spamové techniky. Konverze a přínos pro uživatele jsou důležitější než samotná návštěvnost či první pozice.

***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Efektivní vyhledávání**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Dobré hledání není soutěž v počtu operátorů. Začíná formulací informační potřeby, pokračuje zpřesněním dotazu a končí ověřením zdroje. Operátory mohou omezit šum, ale jejich podpora se mezi vyhledávači mění a výsledky nejsou úplné. Profesionál proto umí dotaz několikrát přeformulovat a zdroj číst kriticky.

Nejprve určete, zda hledáte definici, návod, aktuální zprávu, odbornou studii, data nebo konkrétní dokument. Krátký výstižný dotaz bývá lepší než celá vágní otázka; moderní vyhledávače však rozumějí i přirozenému jazyku. Uvozovky často hledají přesnou frázi: `"přepojování paketů"`.

Znaménko minus může vyloučit význam: `jaguar -auto`. `site:cvut.cz` omezuje výsledky na doménu nebo web. `filetype:pdf` hledá určitý typ souboru, ale neprokazuje jeho odbornost ani bezpečnost.

Operátory lze kombinovat, jejich dostupnost a přesné chování se mohou měnit. Pro aktuální témata přidejte časové období a zkontrolujte datum události i datum publikace. Pro odborné informace preferujte primární zdroj: standard, zákon, dokumentaci, datovou sadu či původní studii.

Výsledek posuzujte podle autora, provozovatele, důkazů, data, účelu a nezávislého potvrzení. AI odpověď nebo úryvek výsledku není náhradou za přečtení zdroje. Když nic nenajdete, použijte synonyma, širší pojem, anglický termín nebo jiný vyhledávač/databázi.

***

## Snímek 5.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Personalizace a soukromí při vyhledávání**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Vyhledávač může využít polohu, jazyk, zařízení, účet a předchozí aktivitu, aby nabídl relevantnější výsledky. To je užitečné při hledání dopravy či restaurace, ale vytváří otázky soukromí a možné omezení pohledu. Soukromější vyhledávač snižuje množství spojovaných dat, nezaručuje však objektivní či stejné výsledky pro celý svět.

Personalizace může využívat účet, historii, přibližnou polohu, jazyk, zařízení a nastavení. Lokalizace výsledků není totéž co dlouhodobý osobní profil; může vycházet jen z aktuálního regionu. **Filtrační bublina** je hypotéza, že výběr obsahu může omezovat setkání s odlišnými informacemi; její síla závisí na službě a situaci.

Žádný vyhledávač neposkytuje dokonale neutrální pořadí — vždy vybírá zdroje a používá ranking. DuckDuckGo uvádí, že nevytváří osobní historii vyhledávání a reklamy cílí podle aktuálního dotazu. Soukromější vyhledávání neanonymizuje automaticky následnou návštěvu cílového webu.

Vyhledávač může využívat výsledky či infrastrukturu partnerů, aniž by jim musel předat osobní identifikátory. Soukromé okno omezuje místní historii, ale samo nezabrání vyhledávači či síti vidět požadavek. HTTPS brání poskytovateli sítě číst obsah dotazu, ale může zůstat vidět, ke které službě se připojujete.

Odhlášení, vypnutí historie a správa aktivity mohou omezit personalizaci, ne nutně veškeré zpracování. Pro citlivé dotazy používejte důvěryhodnou službu, kontrolujte nastavení a po přechodu na výsledek myslete na zásady cílového webu. Soukromí je kompromis mezi množstvím dat, pohodlím, lokalizací a obchodním modelem služby.


# 6. Vývoj internetu, nové technologie a digitální rizika

> Internet se neustále mění, ale jeho další vývoj není jen otázkou vyšší rychlosti. Současně řešíme nové modely webu, miliardy zařízení, nedostatek adres, generativní AI, kybernetické útoky i důvěryhodnost informací.

Tato lekce propojuje historii internetu se současnými technologickými a společenskými změnami. Ukazuje, jak vznikaly jednotlivé vrstvy internetu, co přinesly Web 2.0, Web3, IoT a IPv6, jak pracovat s generativní AI a jak chránit systémy, data, soukromí i informační prostředí.

***
