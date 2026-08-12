# Instrukce pro Codex: prompty pro grafickou prezentaci

## Úkol

Pracuj s výukovým dokumentem Markdown, který je uložen v základní složce daného tematického okruhu. Příklad vstupu:

`02-programy-a-data/programy-a-data.md`

Nevytvářej scénáře, metafory, obrazová semínka, shrnutí ani žádné další obsahové analýzy. Pouze rozděl existující text podle lekcí a podkapitol a mechanicky jej dosaď do níže uvedené kostry promptu.

## Struktura složek

1. Za každou lekci vytvoř v základní složce okruhu adresář podle jejího čísla ve tvaru `N-lekce`, například `1-lekce`, `2-lekce`.
2. V každém adresáři lekce vytvoř prázdné podadresáře:

   ```text
   media/
   media/images/
   ```

3. Do základního adresáře každé lekce vytvoř soubor `prezentace.md`.

Výsledná struktura například vypadá takto:

```text
02-programy-a-data/
├── programy-a-data.md
├── 1-lekce/
│   ├── media/
│   │   └── images/
│   └── prezentace.md
├── 2-lekce/
│   ├── media/
│   │   └── images/
│   └── prezentace.md
└── …
```

## Rozpoznání obsahu

- Lekce jsou hlavní nadpisy ve tvaru `# N. Název lekce`.
- Podkapitoly jsou nadpisy druhé úrovně ve tvaru `## N.M Název podkapitoly`.
- Do `prezentace.md` dané lekce vlož jeden prompt pro každou její podkapitolu v původním pořadí.
- Název promptu vytvoř z názvu podkapitoly bez číslování. Například z `## 1.2 Adresáře, cesty a strom souborového systému` použij `Adresáře, cesty a strom souborového systému`.
- Textem podkapitoly je veškerý původní obsah od jejího nadpisu až po následující podkapitolu nebo následující lekci. Zachovej jej beze změny včetně odstavců, seznamů, ukázek cest, kódu a zvýraznění.
- Úvod dokumentu před první číslovanou lekcí ignoruj.

## Obsah souboru `prezentace.md`

Každý prompt vlož do samostatného kódu Markdown s označením `text`, aby jej bylo možné snadno celý zkopírovat. Mimo kódový blok přidej pouze stručný nadpis `## Snímek N.M` pro orientaci. Uvnitř kódu zachovej přesně tuto kostru; nahraď pouze položky v hranatých závorkách:

````markdown
```text
***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**[název podkapitoly bez číslování]**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**[úplný původní text podkapitoly]**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
```
````

Nezasahuj do formulace této kostry. Nezkracuj text podkapitol, nepřidávej k nim žádné vlastní pokyny a nevytvářej obrázky.

## Kontrola před dokončením

- Každá číslovaná lekce má vlastní složku `N-lekce`.
- V každé složce existuje `media/images/` a `prezentace.md`.
- Každá podkapitola má právě jeden prompt.
- Titulek a text promptu jsou převzaty z odpovídající podkapitoly bez věcných úprav.
