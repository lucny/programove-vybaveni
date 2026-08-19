# Protokol řízeného testu firewallu

Test smí proběhnout pouze na vyhrazeném zařízení a se souhlasem učitele. Před změnou zaznamenejte výchozí stav pravidel.

| Fáze | Stav pravidla | Testovaná aplikace | Očekávání | Výsledek | Čas |
|---|---|---|---|---|---|
| před testem | neexistuje | | komunikace funguje | | |
| blokování | aktivní | | komunikace selže | | |
| vypnuté pravidlo | neaktivní | | komunikace funguje | | |
| úklid | odstraněno | | výchozí stav obnoven | | |

Název pravidla používaný v laboratoři: `PV-LAB-3-6-DOCASNE-BLOKOVANI`.

Na konci musí učitel nebo správce potvrdit, že pravidlo bylo odstraněno a původní komunikace funguje.

