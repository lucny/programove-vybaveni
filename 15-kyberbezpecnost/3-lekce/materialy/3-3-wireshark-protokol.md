# Protokol síťové expedice ve Wiresharku

Zachytávejte pouze provoz vlastního testovacího zařízení. Před začátkem zavřete e-mail, cloudové dokumenty, sociální sítě a další aplikace s osobními daty.

## Měřicí scénář

1. Spusťte záznam na aktivním rozhraní.
2. Otevřete `https://example.com`.
3. V příkazovém řádku spusťte `nslookup example.com`.
4. Záznam ihned zastavte.

## Záznam pozorování

| Filtr | Počet paketů | Vybraný paket | Co je čitelné | Co nelze zjistit |
|---|---:|---|---|---|
| `dns` | | | | |
| `tcp` | | | | |
| `tls` | | | | |
| `ip.addr == DOPLŇ_IP` | | | | |

## Povinná anonymizace

Do odevzdání nevkládejte úplnou IP adresu vlastního zařízení, MAC adresy, cookies, tokeny ani obsah jiné komunikace. Snímek ořízněte na potřebné sloupce a adresy nahraďte označením `KLIENT` a `SERVER`.

