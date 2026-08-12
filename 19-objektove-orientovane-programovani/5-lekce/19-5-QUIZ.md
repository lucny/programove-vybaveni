<!--
title: Abstraktní třídy a rozhraní – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je abstraktní třída?**

<!-- data-randomize="true" -->
[(X)] Neinstancovatelný základ definující společné rozhraní potomků.
[( )] Každá třída bez atributů.
[( )] Konkrétní objekt na stacku.
[( )] Soubor obsahující jen komentáře.

---

**2. Co je abstraktní metoda?**

<!-- data-randomize="true" -->
[(X)] Metoda bez konkrétní implementace, kterou musí doplnit odvozená třída.
[( )] Privátní metoda dostupná jen rodiči.
[( )] Metoda volaná při zániku objektu.
[( )] Libovolná přetížená metoda.

---

**3. Proč nelze vytvořit objekt abstraktní třídy?**

<!-- data-randomize="true" -->
[(X)] Nemá úplné konkrétní chování požadované kontraktem.
[( )] Nemůže obsahovat žádný atribut.
[( )] Musí být vždy uložena v jiném souboru.
[( )] Je určena pouze pro jazyk C.

---

**4. Jak se v C++ označuje čistě virtuální metoda?**

<!-- data-randomize="true" -->
[(X)] Zápisem = 0.
[( )] Klíčovým slovem abstractmethod.
[( )] Dekorátorem @property.
[( )] Příkazem delete.

---

**5. Který modul Python používá pro abstraktní třídy v příkladu?**

<!-- data-randomize="true" -->
[(X)] abc.
[( )] re.
[( )] json.
[( )] math.

---

**6. Který dekorátor v Pythonu označuje abstraktní metodu?**

<!-- data-randomize="true" -->
[(X)] @abstractmethod.
[( )] @classmethod.
[( )] @property.
[( )] @interface.

---

**7. Co definuje rozhraní?**

<!-- data-randomize="true" -->
[(X)] Sadu operací, které implementující třída musí poskytovat.
[( )] Vnitřní reprezentaci všech atributů.
[( )] Konkrétní životnost objektu na heapu.
[( )] Přesnou podobu uživatelského okna.

---

**8. Jak se v C++ obvykle simuluje interface?**

<!-- data-randomize="true" -->
[(X)] Abstraktní třídou obsahující čistě virtuální metody.
[( )] Strukturou bez metod.
[( )] Globální funkcí s ukazatelem.
[( )] Hlavičkovým souborem bez deklarací.

---

**9. Které třídy mohou sdílet rozhraní Pohyblivý bez společné konkrétní hierarchie?**

<!-- data-randomize="true" -->
[[X]] Auto
[[X]] Pes
[[X]] Robot
[[ ]] pouze potomci jedné konkrétní třídy Motor
[[ ]] jen objekty vytvořené na stacku

---

**10. Jaký přínos mají rozhraní?**

<!-- data-randomize="true" -->
[(X)] Umožňují různým typům poskytovat jednotně použitelné chování.
[( )] Zaručují stejnou vnitřní implementaci všech tříd.
[( )] Zakazují polymorfismus.
[( )] Nahrazují potřebu metod v třídách.


# 2. Interaktivní shrnutí kapitoly

## Společný základ bez konkrétní instance

Abstraktní třída popisuje společné vlastnosti a chování, ale není určena k přímému vytvoření objektu. `Zvire` může být obecný základ, zatímco konkrétní `Pes` doplní skutečné chování. Abstraktní metoda nemá implementaci a vytváří [[povinnost]] pro potomky.

V C++ se čistě virtuální metoda zapisuje `= 0`. Python používá modul [[abc]], třídu `ABC` a dekorátor [[@abstractmethod]]. Potomek bez povinné implementace zůstává také abstraktní.

## Kontrakt pro různé implementace

Rozhraní určuje, jaké operace objekt nabízí, nikoli jak je uvnitř provádí. Například `Vozidlo` může požadovat `urychlit()` a `zastavit()`. Auto implementuje obě metody vlastním způsobem, ale uživatel rozhraní se může opřít o jejich existenci.

**Vyber správná tvrzení o abstrakci:**

<!-- data-randomize="true" -->
[[X]] abstraktní třídu nelze přímo instancovat
[[X]] abstraktní metoda definuje požadované chování
[[X]] konkrétní potomek musí povinné metody implementovat
[[X]] rozhraní umožňuje jednotně pracovat s různými typy
[[ ]] rozhraní předepisuje stejný interní algoritmus každé třídě

## Abstraktní třída a interface

Abstraktní třída může nést společný stav i částečnou implementaci. Čisté rozhraní se soustředí na kontrakt metod. C++ interface obvykle vyjadřuje abstraktní třídou s čistě virtuálními metodami; Python používá obdobný mechanismus přes `ABC`.

Rozhraní se hodí i pro typy, které nejsou ve vztahu jedné konkrétní rodiny. Auto, Pes a Robot mohou být [[Pohyblivý]], přestože jeden z druhého nedědí jako specializace.

## Polymorfismus přes společný kontrakt

Kód může přijmout objekt určitého rozhraní a volat jeho operace bez znalosti konkrétní třídy. Tím vzniká volnější vazba: implementaci lze vyměnit, pokud zachová [[kontrakt]]. Abstrakce tedy neskrývá neexistující chování; přesně říká, co musí konkrétní typ dodat.

Smyslem není vytvořit abstraktní třídu pro každý objekt, ale oddělit [[ (požadované chování od konkrétního provedení) | všechny atributy od každé metody | správu paměti od konstruktoru ]].
