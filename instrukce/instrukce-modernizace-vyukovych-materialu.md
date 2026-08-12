# Instrukce pro revizi a modernizaci výukových materiálů

## Účel

Tento instrukční soubor slouží jako dlouhodobé zadání pro převod starších nebo původních výukových materiálů do podoby moderního, odborně přesného a čtivého výukového textu.

Vstupem bývá jeden nebo více PDF/MD dokumentů s původním výukovým obsahem a případně návrh nového rozdělení tematického okruhu do lekcí. Výstupem má být nový **master text v Markdownu**, který může později sloužit jako zdroj pro LiaScript, prezentace, infografiky, podcastové minipořady, testy a další výukové materiály.

Nejde o mechanické přepisování zdroje. Úkolem je původní materiál **odborně zrevidovat, didakticky přestavět, aktualizovat a stylisticky sjednotit**, přičemž se nesmí ztratit užitečné a zajímavé informace, které mohou čtenáři pomoci látku pochopit nebo si ji zapamatovat.

---

# 1. Základní pracovní postup

Nejprve důkladně prostuduj všechny přiložené zdroje. Urči, které části jsou stále platné, které jsou zastaralé, které jsou příliš stručné nebo nepřesné a které naopak zachycují užitečné podrobnosti, které stojí za zachování.

Poté navrhni nebo ověř logické rozdělení tématu do přibližně **5–7 lekcí**. Každá lekce má představovat smysluplný tematický celek a měla by mít přirozenou vnitřní gradaci. Lekce nemají vznikat podle mechanického pravidla „stejný počet podkapitol“, ale podle skutečné logiky tématu.

Pokud uživatel navrhne názvy nebo pořadí lekcí, považuj je za výchozí koncepci. Měň je jen tehdy, pokud existuje jasný didaktický nebo odborný důvod.

Teprve poté vytvoř nový souvislý výukový text v Markdownu.

---

# 2. Co znamená „modernizovat“

Modernizace nesmí znamenat pouhé doplnění několika současných názvů technologií. Je nutné přehodnotit také způsob vysvětlení.

Při revizi:

- oprav zastaralé nebo nepřesné formulace;
- nahraď překonané technické zkratky přesnějším současným výkladem;
- doplň moderní technologie tam, kde přirozeně navazují na základní princip;
- odstraň informace, které už nemají rozumnou výukovou hodnotu;
- zachovej historické informace tehdy, když pomáhají pochopit současný stav;
- rozlišuj základní znalost od specializovaného detailu.

Pokud je nějaké tradiční tvrzení didakticky pohodlné, ale technicky nepřesné, nevypouštěj celý princip. Vysvětli jej přesněji a lidsky.

Například místo prostého tvrzení „ISO je citlivost snímače“ lze vysvětlit, že jde o praktickou fotografickou zkratku, zatímco množství světla zachyceného snímačem určují především clona a čas.

Smyslem revize je vytvořit **správný mentální model**, nikoli encyklopedii výjimek.

---

# 3. Požadovaná odborná hloubka

Text je určen pro všeobecně pojatou výuku informatiky a pro širšího technicky zvídavého čtenáře. Nemá se měnit ve vysokoškolská skripta ani ve specializovaný oborový kurz.

U každého tématu rozlišuj tři úrovně:

**Základní princip** musí být vysvětlen vždy.

**Zajímavý a užitečný detail** zachovej, pokud pomáhá princip pochopit, ukazuje reálné využití nebo vytváří zapamatovatelnou souvislost.

**Specializovaný technický detail** vynech, pokud je potřebný především pro profesionála daného oboru a nepomáhá vytvořit lepší základní představu.

Nezjednodušuj však látku tak silně, aby zůstaly jen vágní obecnosti. Čtenář má po přečtení získat konkrétní znalosti, nikoli pouze pocit, že se „něco nějak používá“.

Dobrým vodítkem je otázka:

> Pomůže tato podrobnost člověku lépe pochopit princip, rozpoznat technologii v praxi nebo se vyhnout běžnému omylu?

Pokud ano, pravděpodobně stojí za zachování.

---

# 4. Styl výkladu

Piš jako kvalitní moderní populárně-naučnou učebnici informatiky.

Text má být:

- odborně přesný;
- čtivý a plynulý;
- informačně hutný, ale nikoli přeplněný;
- civilní, nikoli školometský;
- vhodný i pro hlasité čtení a následnou adaptaci do podcastu.

Preferuj souvislé odstavce před heslovitými seznamy.

Nepoužívej odrážky automaticky pokaždé, když lze vyjmenovat tři vlastnosti. Pokud lze několik atributů, příkladů nebo variant přirozeně vložit do jedné dobře vystavěné věty nebo odstavce, udělej to.

Odrážky použij jen tehdy, když skutečně zvyšují orientaci: například u krátkého algoritmu, kontrolního seznamu, přehledu několika jasně paralelních voleb nebo tam, kde by souvislá věta byla nepřehledná.

Text nesmí působit jako prezentace převedená do Markdownu.

---

# 5. Konkrétní příklady místo katalogů pojmů

Kdykoli je to možné, vysvětli několik vlastností prostřednictvím jednoho dobře zvoleného příkladu nebo krátkého příběhu z praxe.

Místo katalogu:

> mikrofon má typ, směrovost, citlivost, proximity effect, gain…

je lepší popsat situaci člověka nahrávajícího rozhovor v prázdné učebně a ukázat na ní, proč záleží na směrové charakteristice, vzdálenosti od mikrofonu, akustice místnosti a nastavení zisku.

Místo výčtu deseti kompresních formátů je často lepší podrobněji představit tři reprezentativní přístupy a ostatní zasadit do kontextu.

Preferovaný vzorec je:

**konkrétní situace → problém → vysvětlení principu → obecnější závěr**

Příklady mají být realistické a přístupné: školní síť, telefon, web, fotografie, podcast, e-shop, senzor, tabulka, domácí počítač, běžná mobilní aplikace, jednoduchý programovací projekt.

---

# 6. Reprezentativní technologie místo encyklopedických seznamů

Pokud existuje mnoho podobných formátů, knihoven, kodeků, protokolů nebo nástrojů, není nutné všechny probírat stejně podrobně.

Vyber jeden až tři dobře známé reprezentanty a vysvětli na nich princip.

Například u audia lze použít WAV, FLAC a MP3 jako tři odlišné strategie práce s daty. AAC nebo Opus je možné uvést jako současné alternativy, ale není nutné z nich vytvářet další samostatné podkapitoly.

U nástrojů může být jeden konkrétní program použit jako hlavní příklad a ostatní stručně zmíněny jako alternativy.

Cílem je, aby si čtenář odnesl **přenosný princip**, nikoli seznam názvů.

---

# 7. Struktura lekcí a podkapitol

Jedna lekce má mít obvykle několik skutečně smysluplných podkapitol. Nevytvářej podkapitolu pro každou jednotlivou drobnou myšlenku.

Je lepší jedna kvalitní podkapitola o rozsahu několika souvislých odstavců než tři velmi krátké podkapitoly o několika větách.

Každá podkapitola by měla mít vlastní myšlenkový oblouk:

1. uvést problém nebo situaci;
2. vysvětlit princip;
3. doplnit konkrétní příklad nebo zajímavou souvislost;
4. případně upozornit na typický omyl;
5. přirozeně přejít k dalšímu tématu.

Názvy podkapitol mají být informační, ale mohou být mírně popularizační. Nemají působit ani příliš akademicky, ani reklamně.

---

# 8. Zachovávej zajímavá fakta

Při zkracování nikdy automaticky neodstraňuj podrobnost jen proto, že není úplným základem tématu.

Některá fakta mají vysokou didaktickou hodnotu právě proto, že jsou překvapivá nebo pomáhají vytvořit mentální obraz.

Typickými příklady jsou:

- frekvenční a časové maskování v psychoakustice;
- proximity effect u směrových mikrofonů;
- dither jako případ, kdy záměrně přidaný šum může zlepšit digitální výsledek;
- fakt, že JPEG neukládá fotografii prostým zmenšením počtu pixelů;
- skutečnost, že DNS se čte hierarchicky zprava doleva;
- rozdíl mezi synchronizací a skutečnou zálohou;
- skutečnost, že korelace neznamená příčinu;
- to, že Git sleduje textové změny podstatně lépe než binární kancelářský dokument.

Takové informace zachovávej, pokud text nezahlcují. Často jsou právě tím, co si čtenář zapamatuje po delší době.

---

# 9. Analogie používej přesně

Analogie jsou vítané, ale musí pomáhat a nesmějí nahrazovat skutečný princip.

Dobrá analogie:

> DNS funguje podobně jako telefonní seznam: člověk zná jméno, systém potřebuje číselnou adresu.

Po analogii vždy vysvětli, v čem spočívá skutečný technický mechanismus.

Nesnaž se analogii natahovat za hranici její použitelnosti. Pokud by vytvářela chybnou představu, raději ji nepoužívej.

---

# 10. Terminologie

Při prvním výskytu důležitého pojmu uveď český název a podle potřeby i běžný anglický termín nebo zkratku:

**vzorkovací frekvence — sample rate**

**směrová charakteristika — polar pattern**

**automatické rozpoznávání řeči — ASR, Automatic Speech Recognition**

Později používej přirozeně kratší podobu.

Nevkládej anglický název ke každému banálnímu termínu. Angličtina je vhodná tam, kde se s ní člověk reálně setká v software, dokumentaci nebo odborné praxi.

Pokud česká terminologie není jednoznačná, stručně to vysvětli.

---

# 11. Vzorce a technická čísla

Vzorec použij tehdy, když přináší pochopení, ne proto, aby text působil odborněji.

Například vztah:

`T = 1 / f`

je užitečný, protože přímo propojuje frekvenci a periodu.

Naopak dlouhé odvození nebo specializovaná rovnice, se kterou už čtenář dále nepracuje, obvykle není potřebná.

Číselné příklady mají být krátké a názorné. Pokud číslo nemá jasný didaktický účel, není nutné jím text zatěžovat.

---

# 12. Praktická stránka tématu

Kde je to přirozené, zařaď základní doporučení pro běžnou praxi.

Například u audia nestačí vysvětlit mikrofon a sampling. Je užitečné také popsat, jak v běžné místnosti pořídit použitelný záznam.

U práce s daty nestačí ukázat funkci AVERAGE; je třeba vysvětlit, proč se před analýzou kontrolují duplicity, chybějící hodnoty a jednotky.

U webu nestačí vysvětlit HTML a CSS; je vhodné ukázat, jak se z jednoho zdrojového projektu stane skutečně publikovatelná stránka.

Praktická část ale nemá být detailní návod k jednomu konkrétnímu programu, pokud to není výslovným cílem.

---

# 13. Současné trendy a AI

Moderní technologie zařazuj tam, kde organicky navazují na základní princip.

AI nesmí být přilepena jako povinná závěrečná kapitola ke každému tématu. Pokud je však oblast současnou AI zásadně měněna, vysvětli tuto změnu.

Preferuj lidsky pochopitelné situace:

- ASR jako automatický přepis hodinového rozhovoru;
- TTS jako možnost nechat jednu větu vyslovit několika způsoby;
- generativní obraz jako tvorbu nové vizuální informace, nikoli „obnovení ztracených pixelů“;
- AI čištění audia jako pravděpodobnostní rekonstrukci, nikoli přístup k tajné čisté stopě;
- AI asistenta pro tabulky jako pomocníka, jehož vzorec je stále nutné ověřit.

Není-li tématem samotné strojové učení, nevysvětluj zbytečně architektury neuronových sítí, tokenizaci audia, loss functions apod.

---

# 14. Kritické myšlení a typické omyly

Tam, kde existuje rozšířený mýtus nebo zavádějící zkratka, výslovně jej oprav.

Příklady:

> „72 DPI pro web“ není obecné pravidlo; pro web jsou rozhodující především pixelové rozměry a způsob zobrazení.

> RAID není záloha.

> Open source neznamená automaticky „bez licence“.

> Více megapixelů samo o sobě nezaručuje kvalitnější fotografii.

> Vysoké R² nedokazuje příčinnou souvislost.

> Realisticky znějící syntetický hlas není důkaz identity člověka.

Takové opravy formuluj věcně. Text nemá působit jako série „gotcha“ momentů.

---

# 15. Jazyk a dikce

Preferuj delší, logicky vystavěné odstavce před sledem krátkých vět.

Vyhýbej se manifestačnímu stylu:

> „Data jsou všude. Data rozhodují. Data jsou budoucnost.“

Místo toho používej plynulý populárně-naučný výklad.

Vyhýbej se také školometskému metajazyku typu:

> „student musí vědět“  
> „pro středoškoláka postačí“  
> „v této lekci se student naučí“

Samotný text má být použitelný pro kohokoli, kdo si chce téma osvojit. Úroveň výkladu se má projevit výběrem a hloubkou obsahu, nikoli neustálým připomínáním cílové skupiny.

---

# 16. Podcastová použitelnost

Text má být psán tak, aby bylo možné jednotlivé podkapitoly později poměrně snadno převést do krátkého mluveného pořadu.

Proto:

- používej přirozené přechody mezi myšlenkami;
- nejprve vytvoř otázku nebo obraz, potom vysvětluj;
- používej konkrétní situace;
- nerozbíjej text příliš mnoha odrážkami;
- vyhýbej se tabulkám tam, kde nejsou skutečně potřebné;
- nepřetěžuj odstavce zkratkami a katalogy názvů.

Podcastová čitelnost však nesmí vést k rozvolnění faktografie. Text zůstává učebnicí.

---

# 17. Markdownová podoba master textu

Výsledný dokument ukládej jako `.md`.

Doporučená hierarchie:

```markdown
# Název tematického okruhu

## Modernizovaný výukový text

> Krátký úvodní odstavec nebo motivace.

# 1. Název první lekce

## 1.1 První podkapitola

Souvislý výklad...

## 1.2 Druhá podkapitola

Souvislý výklad...

# 2. Druhá lekce
...
```

Na konci vytvoř **Závěrečné propojení**, které nevypíše pouze obsah, ale ukáže vztah mezi hlavními principy celého okruhu.

Velmi vhodná je krátká sekvence typu:

**vstup → reprezentace → zpracování → výstup**

pokud skutečně odpovídá tématu.

---

# 18. Rozsah

Rozsah neurčuj mechanicky podle počtu slov. Typický master text může mít přibližně 4 000–8 000 slov podle složitosti tématu.

Důležitější je rovnováha:

- základní témata nesmějí být odbyta;
- okrajová témata nesmějí zabrat polovinu dokumentu;
- jedna technologická specialita nesmí převážit nad obecným principem;
- příklady mají vysvětlovat, nikoli nafukovat rozsah.

Pokud některá lekce začne být nápadně větší než ostatní, prověř, zda není příliš specializovaná nebo zda by neměla být struktura přerozdělena.

---

# 19. Práce s původními zdroji

Původní PDF nebo MD dokumenty jsou hlavním obsahovým východiskem. Zachovej jejich relevantní fakta, terminologii a tematické jádro.

Pokud je zadání výslovně revizní a modernizační, je dovoleno:

- opravovat odborné chyby;
- doplňovat chybějící souvislosti;
- přeskupovat témata;
- rozšiřovat o současné technologie;
- vypouštět zastaralé nebo málo užitečné části.

Nevymýšlej však bez opory konkrétní údaje, historická data, technické parametry nebo současné vlastnosti produktů.

Pokud je důležitá aktuálnost konkrétní technologie, standardu, formátu, AI modelu nebo služby, ověř ji z aktuálních zdrojů. Obecné stabilní principy není nutné pokaždé vyhledávat na webu.

Při větších opravách původního textu je vhodné na konci pracovního procesu stručně uvést, co bylo odborně změněno, ale tyto redakční poznámky nevkládej do samotného master textu.

---

# 20. Kontrola před odevzdáním

Před vytvořením výsledného souboru proveď vlastní revizi.

Zkontroluj zejména:

**Obsah:** Nechybí důležitý princip z původních materiálů? Nebyla při zkracování odstraněna zajímavá informace s vysokou didaktickou hodnotou?

**Hloubka:** Není některá část zbytečně specializovaná? Nezůstala jiná naopak příliš obecná?

**Struktura:** Mají podkapitoly skutečný smysl, nebo jsem text rozsekal na příliš malé bloky?

**Styl:** Nezměnil se výklad v katalog odrážek? Lze některé seznamy rozpustit do plynulého odstavce?

**Příklady:** Obsahuje každá složitější oblast alespoň jeden konkrétní, dobře představitelný příklad?

**Přesnost:** Nepoužívám tradiční, ale zavádějící zkratku bez vysvětlení?

**Současnost:** Nechybí moderní technologie, která zásadně změnila danou oblast?

**Dikce:** Lze text plynule číst nahlas? Nejsou odstavce ani příliš úsečné, ani nepřehledně dlouhé?

**Vyváženost:** Odpovídá rozsah jednotlivých lekcí jejich skutečné důležitosti?

---

# 21. Výstup

Výsledkem má být:

1. kompletní nový master text v souboru `.md`;
2. nikoli pouhá osnova;
3. nikoli jen revizní komentář;
4. nikoli mechanická parafráze původního PDF.

Po vytvoření souboru stručně shrň jeho novou strukturu a významné odborné nebo didaktické změny. Hlavním výstupem je ale samotný Markdown dokument.

---

# 22. Stručné zadání pro nový tematický okruh

Při každém dalším použití lze k tomuto instrukčnímu souboru připojit už jen stručný úkol, například:

> Na základě přiložených původních materiálů zpracuj podle přiložených instrukcí modernizovaný master text pro tematický okruh „Digitální video“. Nejprve zvaž vhodné rozdělení do přibližně šesti lekcí, potom vytvoř celý výsledný Markdown dokument. Zachovej hodnotné informace z původního materiálu, oprav zastaralé nebo nepřesné části a vhodně doplň současné technologie. Dbej na vyváženost témat, plynulý populárně-naučný styl, konkrétní příklady a přiměřenou odbornou hloubku.
