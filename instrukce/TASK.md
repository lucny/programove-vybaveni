# TASK — autonomní hromadné generování infografických snímků

## Cíl

Vygeneruj **všechny snímky uvedené v `slides-manifest.json`** jako jednu souvislou autonomní úlohu.

Nezastavuj se po jednotlivých snímcích kvůli kontrole, kopírování souboru, volbě cílové složky ani kvůli drobné estetické odchylce. Kontrola, případná regenerace, uložení a aktualizace manifestu jsou součástí jedné iterace.

Zdrojové scénáře jsou v souborech `prezentace.md`.

Cílové obrázky patří do `N-lekce/media/images/N-X.png`. Například snímek `3.4` musí skončit jako `3-lekce/media/images/3-4.png`.

## Základní pravidlo autonomie

Pracuj až do okamžiku, kdy jsou všechny položky manifestu ve stavu `done`, `needs_review` nebo `failed`. Stav `pending` nebo `generating` na konci běžné dávky není dokončení úlohy.

**Nežádej uživatele o schválení mezi snímky.** Pokud je výsledek použitelný, přijmi jej, ulož a pokračuj. Pokud je chybný, oprav prompt a zkus další generaci. Po vyčerpání povolených pokusů označ nejlepší použitelnou variantu `needs_review`; pokud není použitelná žádná varianta, označ položku `failed`. V obou případech pokračuj dalším snímkem.

## Zahájení nebo obnovení dávky

1. Načti `slides-manifest.json`.
2. Spusť `python slide_batch.py prepare`.
3. Spusť `python slide_batch.py reset-stale` pro obnovení po přerušeném běhu.
4. Spusť `python slide_batch.py reconcile`, aby se existující validní PNG znovu negenerovaly.
5. Zkontroluj `python slide_batch.py summary`.
6. Další položku vždy zjisti pomocí `python slide_batch.py next`.

Položky `done` nepřegenerovávej.

## Iterace pro jeden snímek

### 1. Rezervace položky

Spusť `python slide_batch.py start N.X`. Tím se zvýší počet pokusů a stav se změní na `generating`.

### 2. Načtení scénáře

V odpovídajícím souboru najdi přesně sekci `## Snímek N.X — ...`. Použij zejména výukový záměr, odborně citlivý bod, tvůrčí premisu, přesné texty, produkční prompt a kontrolní body.

Nevytvářej generický layout místo scénáře. Každý snímek má mít vlastní obrazový princip.

### 3. Generování

Vygeneruj jeden snímek podle scénáře. Preferovaný formát je 16:9, ideálně 1600 × 900 px.

Pokud generátor uloží PNG pod automatickým názvem, ponech jej ve stagingu `_generated/`. Konečný název a cílovou cestu neurčuj ručně; použij `slide_batch.py`.

### 4. Automatická QA kontrola

Za **kritickou chybu** považuj zejména odborně chybný mechanismus, záměnu pojmů výslovně zakázanou scénářem, chybějící hlavní pointu, chybný přesný údaj či odborný termín, nesrozumitelný hlavní diagram, oříznutý titulek, zásadně chybnou češtinu, pseudo-text místo povinného popisku nebo úplné ignorování vizuální koncepce.

Za **nekritickou odchylku** považuj menší odchylku v rozmístění, jiný úhel kamery při zachování principu, mírnou estetickou nedokonalost, drobný nepovinný detail nebo alternativní, ale věcně správný způsob zobrazení. Nekritická odchylka není důvod k zastavení dávky.

### 5. Přijetí nebo regenerace

Přijatelný výsledek:

`python slide_batch.py complete N.X "CESTA/K/VYGENEROVANEMU.png"`

Skript ověří PNG, zkontroluje poměr stran, vytvoří cílovou složku, přesune soubor na deterministickou cestu, nastaví `done` a atomicky uloží manifest.

Chyba opravitelná dalším pokusem:

`python slide_batch.py retry N.X "stručný důvod regenerace"`

Potom uprav prompt pouze v místě, které chybu způsobilo, a pokračuj novou generací.

Nejlepší varianta je použitelná, ale potřebuje pozdější kontrolu:

`python slide_batch.py review N.X "CESTA/K/NEJLEPSI.png" "stručný důvod"`

Žádná varianta není použitelná:

`python slide_batch.py fail N.X "stručný důvod"`

**Po `review` ani `fail` dávku nezastavuj.**

## Maximální počet pokusů

Výchozí limit v manifestu je `max_generation_attempts = 3`: jedna původní a maximálně dvě opravné generace. Neplýtvej pokusy na kosmetické změny.

## Kdy se NESMÍŠ zastavit

Nezastavuj se jen proto, že byl dokončen jeden snímek, je třeba výsledek vizuálně zkontrolovat, PNG přejmenovat, vytvořit cílovou podsložku, přesunout soubor, existuje drobná estetická odchylka, jeden snímek skončil jako `needs_review` nebo `failed`, nebo je třeba přejít do další lekce.

## Kdy je dovoleno dávku zastavit

Zastav pouze tehdy, když stav objektivně znemožňuje bezpečné pokračování celé dávky: chybí zásadní vstup pro všechny další položky, obrazový nástroj opakovaně selhává pro celou dávku, projekt není zapisovatelný, manifest je poškozen a nelze jej bezpečně rekonstruovat, další krok by vyžadoval nejasné přepsání hotové práce, nebo nástroj narazí na nepřekonatelné bezpečnostní či oprávňovací omezení.

V takovém případě zachovej již hotové výstupy a manifest a až potom informuj uživatele.

## Ochrana hotové práce

Nikdy automaticky nepřepisuj soubor položky ve stavu `done`. Pokud cílový PNG existuje, ale manifest tvrdí `pending`, použij `python slide_batch.py reconcile`.

## Stavové hodnoty

- `pending` — čeká na zpracování,
- `generating` — právě probíhá pokus,
- `done` — výsledek prošel automatickou kontrolou,
- `needs_review` — nejlepší varianta je uložena, ale má známou vadu,
- `failed` — po povolených pokusech není uložen použitelný výsledek.

## Dokončení celé úlohy

Po posledním snímku spusť `python slide_batch.py summary`. Úloha je dokončena, pokud není žádná položka `pending` ani `generating`.

Teprve potom vrať souhrnnou zprávu s počty `done`, `needs_review`, `failed` a seznamem pouze těch snímků, které vyžadují kontrolu nebo selhaly.

## Důležitá zásada

Správný pracovní cyklus je:

**scénář → generování → vizuální QA → případná regenerace → uložení → manifest → další snímek**

nikoli:

**scénář → generování → zastavení → čekání na uživatele**.
