<!--
author: Marek Lučný
language: cs
mode: Textbook
comment: Interaktivní laboratorní úlohy pro samostatnou i řízenou práci.
-->

# Laboratoř: Internet, WWW a informační gramotnost

> **⚠️ Upozornění k nástrojům a bezpečnosti**
>
> Teoretické principy navazují na studijní materiál. Konkrétní aplikace, odkazy a pracovní postupy jsou externím praktickým doplněním; jejich rozhraní se mohou měnit. Pracujte pouze s vlastními soubory, neosobními testovacími daty a veřejnými výukovými službami. Neobcházejte omezení cizích systémů, nesdílejte hesla, tokeny, osobní údaje ani licencovaný obsah.

## Jak pracovat v laboratoři

> **🗂️ Před každým experimentem**
>
> Připravte si pracovní zápis se čtyřmi poli: **předpověď**, **postup**, **pozorování**, **vysvětlení**. Rozdíl mezi předpovědí a výsledkem není chyba; je to příležitost ověřit, kde byla původní představa neúplná.

> **🧰 Jak číst bloky v této lekci**
>
> - **💡 Koncept / 🎯 Cíl** říká, jaký princip dokazujete.
> - **🧰 Nástroj** uvádí prostředí, jehož ovládání je jen prostředek, ne cíl.
> - **🧭 Postup** provádějte pomalu a zapisujte si viditelné změny.
> - **🔎 Ověření a interpretace** promění klikání v důkaz a vysvětlení.

> **📝 Šablona zápisu do laboratorního deníku**
>
> Tento blok zkopírujte pod každý vypracovaný experiment a doplňte jej vlastním obsahem.

```text
Předpověď:
Pozorování / důkaz:
Vysvětlení pojmem z kapitoly:
Omezení nebo zdroj možné chyby:
```

> „Pozorování není vysvětlení; vysvětlení spojuje důkaz s principem.“
>
> — laboratorní zásada pro tuto lekci


## 1. Principy internetu

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato sada experimentů ukazuje, jak fungují IP adresy, směrování paketů a doménový systém.

### Experiment 1.1: Zjištění vlastní IP adresy a překladu adres (NAT)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazová řádka (Windows `ipconfig`), web [WhatIsMyIPAddress.com](https://whatismyipaddress.com/)
> **Postup**: 
    1. Otevřete příkazový řádek ve Windows (vyhledejte `cmd`).
    2. Napište příkaz `ipconfig` a stiskněte Enter. Najděte řádek „IPv4 Address“ (obvykle začíná 192.168.x.x nebo 10.x.x.x). Toto je vaše soukromá adresa v místní síti.
    3. Otevřete web [WhatIsMyIPAddress.com](https://whatismyipaddress.com/). 
    4. Porovnejte obě adresy. Uvidíte, jak váš domácí router využívá funkci NAT a překládá vaši soukromou adresu na veřejnou adresu, pod kterou vás vidí internet.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.2: Sledování cesty paketu (Traceroute)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazová řádka (Windows `tracert`) nebo [Visual Traceroute](https://gsuite.tools/traceroute)
> **Postup**: 
    1. Otevřete příkazový řádek (`cmd`).
    2. Zadejte příkaz `tracert 8.8.8.8` (DNS server Googlu) a sledujte výpis.
    3. Nástroj vám ukáže každý jednotlivý směrovač (router) na cestě k cíli. Každý router rozhoduje o dalším úseku cesty, nikoliv o celé trase.
    4. Alternativně použijte web Visual Traceroute, který tyto skoky zakreslí do mapy.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.3: Překlad doménových jmen pomocí DNS

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazová řádka (`nslookup`) nebo [DNS Checker](https://dnschecker.org/)
> **Postup**: 
    1. V příkazovém řádku zadejte příkaz `nslookup seznam.cz`.
    2. Všimněte si, že systém DNS přeložil lidsky čitelný název na IP adresu (tzv. A záznam pro IPv4 nebo AAAA pro IPv6).
    3. Pro pokročilejší pohled zadejte doménu do webu DNS Checker a sledujte, jaké záznamy a s jakým parametrem TTL (doba v cache) vrací různé servery po světě.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.4: Analýza „best effort“ přístupu a zpoždění

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazová řádka (`ping`) nebo web [Ping.pe](https://ping.pe/)
> **Postup**: 
    1. V `cmd` zadejte příkaz `ping australia.gov.au`.
    2. Sledujte dobu odezvy (latenci) v milisekundách. 
    3. Uvědomte si, že protokol IP komunikuje metodou „best effort“ a sdílení linek může způsobit zpoždění nebo ztrátu paketů. Nástroj Ping.pe vám toto graficky ukáže odesláním paketů z desítek míst planety současně.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.5: Simulace výpadku a decentralizace sítě (Princip ARPANETu)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Filius](https://www.lernsoftware-filius.de/) (Výukový simulátor sítí)
> **Postup**: 
    1. Stáhněte a spusťte simulátor Filius.
    2. Poskládejte jednoduchou síť tvořenou třemi routery spojenými do trojúhelníku a dvěma počítači.
    3. Spusťte režim simulace, odešlete ping z jednoho počítače na druhý a sledujte animaci pohybu paketu.
    4. „Přestřihněte“ jednu linku. Pozorujte, jak síť automaticky najde novou cestu. Jedná se o základní myšlenku decentralizace ARPANETu z roku 1969.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 1.6: Analýza navázání TCP spojení (Třícestný handshake)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Wireshark](https://www.wireshark.org/)
> **Postup**: 
    1. Spusťte Wireshark a začněte zachytávat provoz na vaší aktivní síťové kartě.
    2. V prohlížeči otevřete jakoukoliv jednoduchou webovou stránku bez HTTPS (např. `http://neverssl.com/`).
    3. Ve Wiresharku zastavte zachytávání a do filtru napište `tcp`.
    4. Vyhledejte tři po sobě jdoucí pakety, u kterých uvidíte vlajky TCP spojení, jež se navazuje pomocí kroků SYN, SYN‑ACK a ACK.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Principy internetu“, který nyní dokážete vysvětlit na vlastním pozorování.

## 2. Internetové služby a URL

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Tato část se zaměřuje na porty, architekturou klient-server, protokoly a stavbu URL adres.

### Experiment 2.1: Skener otevřených síťových portů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Nmap (Zenmap)](https://nmap.org/)
> **Postup**: 
    1. Spusťte grafické rozhraní Zenmap (součást Nmap).
    2. Do pole "Target" zadejte testovací server `scanme.nmap.org` a spusťte rychlý sken.
    3. Nástroj odhalí, které porty (např. port 80 pro HTTP nebo 22 pro SSH) jsou na serveru otevřené a připravené přijímat spojení.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.2: Zkoumání aktivních spojení ve vlastním počítači

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Příkazová řádka (Windows `netstat`)
> **Postup**: 
    1. Otevřete příkazový řádek jako správce a zadejte `netstat -ano`.
    2. Uvidíte tabulku všech aktivních spojení. Všimněte si, že váš počítač (klient) používá dočasné dynamické porty s vysokými čísly (v rozsahu 49152–65535) k připojení na známé systémové porty cizích serverů (např. port 443 pro HTTPS).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.3: Rozborka a úprava URL parametrů (Query)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Webový prohlížeč
> **Postup**: 
    1. Otevřete libovolný e-shop (např. Alza.cz nebo Mall.cz) a něco vyhledejte.
    2. Podívejte se do adresního řádku. Identifikujte schéma (`https`), hostitele, cestu a takzvané Query.
    3. Query začíná otazníkem `?` a skládá se z dvojic `klíč=hodnota` oddělených znakem `&`.
    4. Zkuste hodnotu parametru vyhledávání přímo v adresním řádku manuálně přepsat a stiskněte Enter, čímž změníte dotaz bez použití vyhledávacího pole na stránce.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.4: Bezpečné připojení na dálku (SSH)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [PuTTY](https://www.putty.org/)
> **Postup**: 
    1. Spusťte program PuTTY.
    2. Do pole Host Name zadejte veřejně dostupný testovací server (např. `telehack.com`).
    3. Připojte se přes port 22 (SSH). Všimněte si, že SSH poskytuje šifrovaný vzdálený přístup a terminál na serveru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.5: Diagnostika šifrování serveru (TLS/SSL)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Qualys SSL Labs - Server Test](https://www.ssllabs.com/ssltest/)
> **Postup**: 
    1. Otevřete web Qualys.
    2. Zadejte doménu své školy (např. `moodle.sspu-opava.cz` z textu).
    3. Nástroj vyhodnotí, jak silné šifrování certifikátu daný server využívá, aby zajistil schéma HTTPS na portu 443.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 2.6: Model sítě Peer-to-Peer v praxi

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [qBittorrent](https://www.qbittorrent.org/)
> **Postup**: 
    1. Stáhněte si legální torrentový soubor (např. obraz instalace linuxové distribuce Ubuntu).
    2. Otevřete jej v programu qBittorrent. 
    3. Během stahování se překlikněte na záložku "Peers" (Uzly). Uvidíte desítky IP adres, se kterými stahujete. Tento hybridní model P2P ukazuje, že uzly vystupují současně jako klienti i servery.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Internetové služby a URL“, který nyní dokážete vysvětlit na vlastním pozorování.

## 3. World Wide Web a HTTP

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Experimenty ilustrující hlavičky, HTTP metody a to, jak bezstavový web udržuje data.

### Experiment 3.1: Komunikace s HTTP ozvěnovým serverem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [httpbin.org](https://httpbin.org/) nebo [ReqBin](https://reqbin.com/)
> **Postup**: 
    1. Otevřete nástroj ReqBin a zadejte URL `https://httpbin.org/get`. Zvolte metodu GET a odešlete.
    2. Odpověď vám ukáže, co přesně váš klient na server poslal (hlavičky, vaši IP adresu).
    3. Změňte metodu na POST, do těla vložte libovolný text a odešlete na `https://httpbin.org/post`. Uvidíte rozdíl – metoda POST předává data ke zpracování v těle požadavku.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.2: Mnemotechnika HTTP stavových kódů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [HTTP.cat](https://http.cat/)
> **Postup**: 
    1. Přejděte na stránku HTTP.cat.
    2. Postupně si rozklikněte kódy 200, 404, 403 a 500. Zjistíte, že 2xx značí úspěch, 4xx chybu na straně klienta (požadavek nelze splnit) a 5xx selhání serveru při platném požadavku.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.3: Odposlech zachyceného požadavku

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)
> **Postup**: 
    1. Spusťte Burp Suite a otevřete vestavěný prohlížeč (záložka Proxy -> Intercept is on).
    2. Zadejte jakoukoliv adresu (např. `example.com`). Stránka se nenačte okamžitě, ale požadavek se pozastaví v programu.
    3. Prohlédněte si strukturu zprávy: požadavek jasně obsahuje metodu, cíl a hlavičky. Poté požadavek uvolněte tlačítkem "Forward".


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.4: Manipulace s HTTP Cookies

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [EditThisCookie](https://www.editthiscookie.com/) (Rozšíření) nebo DevTools v prohlížeči (F12)
> **Postup**: 
    1. Otevřete web, kam se dá přihlásit nebo ukládat položky (např. testovací e-shop).
    2. Otevřete DevTools (klávesa F12) -> panel Application (Aplikace) -> Storage -> Cookies.
    3. Najděte cookie. Zkontrolujte, zda má atributy jako `Secure` (odesílání jen na HTTPS) či `HttpOnly` (brání přístupu z JavaScriptu).
    4. Smažte klíčovou cookie a obnovte stránku. Zjistíte, že jste byli odhlášeni, protože HTTP je bezstavové a stav udržovaly právě smazané cookies.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.5: Zkoumání Webového úložiště (LocalStorage)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: DevTools (F12)
> **Postup**: 
    1. Otevřete webovou kalkulačku nebo to-do list (např. `todomvc.com`). Vytvořte pár úkolů.
    2. Otevřete DevTools -> Application -> LocalStorage.
    3. Zde uvidíte svá data uložena jako řetězce. Na rozdíl od cookies se data z localStorage neposílají automaticky s HTTP požadavkem, ale skript na stránce je může číst. Zavřete a znovu otevřete prohlížeč – data běžně přetrvají.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 3.6: Analýza zabezpečení HTTP hlaviček

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [SecurityHeaders.com](https://securityheaders.com/)
> **Postup**: 
    1. Otevřete nástroj a zadejte adresu svého oblíbeného zpravodajského portálu.
    2. Nástroj ukáže, které hlavičky web používá (např. ty, které řídí chování prohlížeče a zvyšují ochranu).
    3. Všimněte si z textu, že hlavičky nesou klíčová metadata celé komunikace.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „World Wide Web a HTTP“, který nyní dokážete vysvětlit na vlastním pozorování.

## 4. Webové prohlížeče, bezpečnost a digitální stopa

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Prozkoumejte rendering enginy, vývojářské nástroje a zanechávání digitální stopy.

### Experiment 4.1: Lokální úprava webové stránky pomocí DevTools

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Webový prohlížeč (DevTools - F12)
> **Postup**: 
    1. Otevřete libovolný zpravodajský článek a stiskněte F12.
    2. V panelu **Elements/Inspector** (Prvky) klikněte na nástroj pro výběr prvku (šipka) a klikněte na titulek článku.
    3. Dvakrát klikněte na text uvnitř DOM stromu a přepište ho. Vzhled stránky se změní.
    4. Nyní stiskněte F5 (Obnovit). Změna zmizí, protože úprava DOMu v panelu Elements se projevuje jen v paměti konkrétního prohlížeče (místní a dočasná změna) a nemění skutečnou databázi serveru.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.2: Sledování „vodopádu“ síťových požadavků (Network)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Webový prohlížeč (DevTools -> záložka Network)
> **Postup**: 
    1. Stiskněte F12 a přejděte na panel **Network** (Síť).
    2. Načtěte velký zpravodajský web (např. iDnes.cz). 
    3. Sledujte kaskádu desítek až stovek stahovaných souborů. Ukazuje to, že HTML dokument obvykle vyvolá mnoho dalších samostatných HTTP požadavků na obrázky, styly, skripty a písma.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.3: Simulace responzivity a mobilních zařízení

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Webový prohlížeč (DevTools -> Device Toggle)
> **Postup**: 
    1. Otevřete libovolný web, stiskněte F12 a klikněte na ikonu telefonu/tabletu (Toggle device toolbar).
    2. Z roletky vyberte konkrétní model (např. iPhone 12).
    3. Sledujte, jak CSS přizpůsobí rozložení. Pamatujte, že tento režim simuluje viewport, ale nenahrazuje test na skutečném telefonu a jeho hardwarovém enginu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.4: Test unikátnosti otisku prohlížeče (Fingerprinting)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Cover Your Tracks](https://coveryourtracks.eff.org/) (od organizace EFF)
> **Postup**: 
    1. Otevřete web a spusťte testovací sken.
    2. Nástroj vygeneruje pasivní stopu na základě vašich instalovaných písem, rozlišení, verze enginu a operačního systému.
    3. Výsledek často ukáže, že jste unikátně identifikovatelní i bez použití tradičních cookies třetích stran, což demonstruje techniky fingerprintingu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.5: Extrakce metadat (EXIF) jako pasivní stopa

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Jeffrey's Image Metadata Viewer](https://exif.regex.info/exif.cgi)
> **Postup**: 
    1. Vezměte originální fotografii vyfocenou vaším mobilním telefonem se zapnutou lokací.
    2. Nahrajte ji do tohoto bezplatného online prohlížeče.
    3. Uvidíte kompletní skrytá data v souboru, často včetně modelu telefonu a přesných GPS souřadnic. Metadata tak mnohdy prozradí víc než samotný obsah (pasivní digitální stopa).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 4.6: Pátrání ve webových archivech

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Wayback Machine (archive.org)](https://archive.org/web/)
> **Postup**: 
    1. Otevřete webovou stránku archive.org.
    2. Zadejte adresu nějakého starého českého webu (např. seznam.cz).
    3. Přejděte na záznam například z roku 1999.
    4. Experiment ukazuje, že smazání historie z vašeho prohlížeče neodstraňuje veřejné kopie vytvořené archivací.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Webové prohlížeče, bezpečnost a digitální stopa“, který nyní dokážete vysvětlit na vlastním pozorování.

## 5. Vyhledávače, SEO a informační gramotnost

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Praktické metody efektivního vyhledávání a pochopení indexace obsahu (crawling).

### Experiment 5.1: Přesné vyhledávání pomocí operátorů

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Google nebo DuckDuckGo
> **Postup**: 
    1. Zkuste vyhledat definici dokumentu s omezením na akademické weby. Do vyhledávače zadejte: `site:cvut.cz "přepojování paketů" filetype:pdf`.
    2. Tímto dotazem omezíte doménu (site), vynutíte přesnou frázi (uvozovky) a omezíte výsledek jen na dokumenty PDF. Operátory výrazně snižují šum ve výsledcích.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.2: Jak vidí web Crawler (robot)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/) (verze zdarma)
> **Postup**: 
    1. Stáhněte a nainstalujte aplikaci, která funguje jako vyhledávací robot.
    2. Zadejte malý web nebo blog do vyhledávacího řádku a spusťte simulaci crawlingu.
    3. Nástroj navštíví počáteční URL, prozkoumá vnitřní strukturu odkazů a sestaví "mapu". Tímto způsobem automatický klient objevuje nové adresy z odkazů.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.3: Analýza souboru robots.txt

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Webový prohlížeč
> **Postup**: 
    1. Otevřete adresní řádek a zadejte URL `https://cs.wikipedia.org/robots.txt`.
    2. Prohlédněte si textový soubor. Najdete zde instrukce `User-agent` a `Disallow`. 
    3. Tyto instrukce říkají crawlerům (vyhledávacím robotům), které cesty smějí požadovat. Není to ale bezpečnostní bariéra, je to jen žádost.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.4: Porovnání výsledků a filtrační bubliny

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: Prohlížeč s účtem Google vs. [Startpage.com](https://www.startpage.com/)
> **Postup**: 
    1. V prohlížeči, kde jste přihlášeni (např. Google s vaší historií a polohou), zadejte politické téma nebo velmi nejednoznačné slovo.
    2. Zkopírujte stejný dotaz do vyhledávače Startpage.com (nebo DuckDuckGo, který nevytváří osobní historii vyhledávání).
    3. Porovnejte výsledky. Demonstrujete si tím personalizaci a limity případné filtrační bubliny.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.5: Reverzní vyhledávání jako nástroj fact-checkingu

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [TinEye.com](https://tineye.com/)
> **Postup**: 
    1. Stáhněte si obrázek ze zprávy na sociální síti, u které pochybujete o její pravdivosti nebo datu pořízení.
    2. Nahrajte tento obrázek do služby TinEye a seřaďte výsledky od nejstaršího ("Oldest").
    3. Zjistíte první datum, kdy se obrázek objevil na internetu, což je klíčové pro ověřování původu, kontextu a odhalení dezinformací.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 5.6: Sémantické pochopení webu vyhledávačem

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Schema Markup Validator](https://validator.schema.org/)
> **Postup**: 
    1. Otevřete libovolný recept na vaření z velkého potravinového portálu.
    2. Zkopírujte jeho URL adresu a vložte ji do tohoto nástroje.
    3. Podívejte se na datový výpis. Uvidíte strukturovaná data, kterými autor webu popsal význam pro vyhledávač (čas přípravy, suroviny), což napomáhá tvorbě takzvaných rozšířených výsledků (rich snippets).


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Vyhledávače, SEO a informační gramotnost“, který nyní dokážete vysvětlit na vlastním pozorování.

## 6. Vývoj internetu, nové technologie a digitální rizika

> **🎯 Cíl kapitoly**
>
> Při práci propojujte každý nástroj s principem, který zviditelňuje. Nejde o rychlé splnění kroků, ale o schopnost vysvětlit, co se změnilo a jaké omezení má pozorování.


Poslední série ukazuje rizika umělé inteligence, sítě IoT, principy bezpečnosti a fenomény Web3.

### Experiment 6.1: Transparentnost veřejného blockchainu (Web3)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Etherscan.io](https://etherscan.io/)
> **Postup**: 
    1. Otevřete tento prohlížeč sítě Ethereum.
    2. Z domovské stránky klikněte na náhodnou nejnovější transakci (Latest Transactions).
    3. Zjistíte, že odesílatel, příjemce, hodnota převodu a datum jsou zcela veřejné a dohledatelné. Experiment demonstruje, že veřejný blockchain Web3 není automaticky anonymní a soukromý.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.2: Odhalování nezabezpečených zařízení (Internet věcí - IoT)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Shodan.io](https://www.shodan.io/)
> **Postup**: 
    1. Vytvořte si bezplatný účet.
    2. Do vyhledávání napište např. "webcam" nebo "default password".
    3. Vyhledávač Shodan nehledá weby, ale internet věcí. Uvidíte mapy kamer nebo senzorů, které jsou připojeny přímo do veřejného internetu. Tím si uvědomíte, proč výchozí nebo slabá hesla IoT zařízení představují obrovské riziko.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.3: Odhalování phishingu (Sociální inženýrství)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Jigsaw Phishing Quiz](https://phishingquiz.withgoogle.com/)
> **Postup**: 
    1. Otevřete kvíz vyvinutý dceřinou společností Googlu.
    2. Analyzujte každý falešný e-mail a ověřte si, že umíte číst adresní řádky, subdomény a nenecháte se oklamat. Phishing a sociální inženýrství se řadí mezi nejběžnější a nejzávažnější kybernetické hrozby.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.4: Test kompromitace hesel v hromadných únicích

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Have I Been Pwned](https://haveibeenpwned.com/)
> **Postup**: 
    1. Zadejte na hlavní stránku svou e-mailovou adresu.
    2. Služba prohledá databáze z celého světa a oznámí vám, jestli nebylo vaše heslo ukradeno útočníky z cizích serverů (což potvrzuje, že ztráta kontroly nad daty se děje na obou stranách).
    3. Tento experiment podtrhuje význam upozornění, abyste ve správci hesel využívali pro každý web zcela unikátní hesla.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.5: Zkoumání odpovědí AI s dohledáváním dokumentů (RAG)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [Perplexity.ai](https://www.perplexity.ai/)
> **Postup**: 
    1. Položte asistentovi (který na rozdíl od čistých modelů využívá vyhledávání pomocí techniky RAG) velmi specifický faktický dotaz.
    2. Jakmile vygeneruje odpověď, klikněte na čísla zdrojů (citace).
    3. Přečtěte si původní článek. Ověřte, zda AI náhodou nehalucinuje fakta (citace může být totiž nesprávně interpretována nebo nepřesná). Informační gramotnost začíná právě touto kontrolou a otevřením odkazu.


> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

### Experiment 6.6: Praktická ukázka moderních klíčů (Passkeys)

> **🧭 Laboratorní postup**
>
> 1. Před spuštěním napište jednou větou předpověď: *co se podle vás změní a proč*.
> 2. Proveďte kroky v uvedeném pořadí; u důležité změny zastavte a zapište pozorování.
> 3. Používejte jen vlastní soubory, testovací data a výslovně povolené služby.

> **Nástroj**: [WebAuthn.io](https://webauthn.io/)
> **Postup**: 
    1. Navštivte tento bezpečný testovací web na mobilním telefonu nebo notebooku s biometrickou čtečkou.
    2. Zadejte libovolné fiktivní uživatelské jméno a klikněte na „Register“. Namísto hesla se vás systém zeptá na váš otisk prstu nebo PIN zařízení (tzv. Passkey).
    3. Z textu si uvědomte, že tyto phishingu odolné klíče a vícefaktorové metody (MFA) jsou výrazně bezpečnější pro ověřování než zastaralá hesla a jednorázové SMS kódy.

> **🔎 Ověření a interpretace**
>
> - Uložte jeden důkaz výsledku: snímek obrazovky, krátký výpis, měření nebo odkaz na vlastní test.
> - Popište konkrétní změnu, ne jen „fungovalo to“.
> - Vysvětlete ji pojmem z kapitoly a doplňte jeden limit měření či použitého nástroje.
>
> **📤 Odevzdání**
>
> Odevzdejte název experimentu, předpověď, důkaz, pozorování a vysvětlení ve 3–5 větách. Pokud se výsledek liší od očekávání, popište rozdíl — i nezdar je cenný výsledek.

[[ Co je při laboratorním experimentu nejpřesvědčivější závěr? ]]

[( )] „Nástroj to ukázal, proto tomu rozumím.“
[(X)] „Pozorovaný výsledek popíšu, spojím s principem a uvedu hranici svého měření.“
[( )] „Stačí přiložit obrázek výsledku bez vysvětlení.“

> **💬 Reflexe kapitoly:** Zapište jeden pojem z části „Vývoj internetu, nové technologie a digitální rizika“, který nyní dokážete vysvětlit na vlastním pozorování.

---

## Závěrečné sebehodnocení

| Dovednost | Umím samostatně | Potřebuji pomoc |
|---|:---:|:---:|
| připravit bezpečný test a formulovat předpověď |  |  |
| zaznamenat ověřitelný výsledek |  |  |
| vysvětlit jej odborným pojmem |  |  |
| popsat omezení nástroje nebo měření |  |  |
| chránit data a pracovat jen v povoleném prostředí |  |  |
