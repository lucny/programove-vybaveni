# Správa elektronické učebnice

Editujte pouze zdrojové master Markdown soubory v tematických adresářích, kvízy, WEBP obrázky a případné soubory v `N-lekce/doplnky/`. Adresář `docs/`, reporty a exporty jsou generované.

Kvíz pojmenujte `K-L-QUIZ.md` (pro téma 2 a lekci 1 například `2-1-QUIZ.md`); podporována je také zkrácená varianta `1-QUIZ.md`. Obrázek pojmenujte ideálně `topic-slug-L-S.webp`; starší varianta `L-S.webp` je podporována.

Výukové bloky zapisujte explicitně jako `!!! principle "Princip"`, `!!! example "Příklad"`, `!!! tip "Tip"`, `!!! warning "Upozornění"`, `!!! history "Historie"` nebo `!!! practice "Praktikum"`.

```text
python tools/textbook.py audit
python tools/textbook.py validate
python tools/textbook.py all
mkdocs serve
```

Pro veřejné LiaScript odkazy nastavte `liascript.raw_base` v `textbook/config.yml` na URL typu `https://raw.githubusercontent.com/OWNER/REPOSITORY/main/`. Bez ní validace bezpečně skončí chybou a nevytvoří falešné odkazy.

PDF/LaTeX export vyžaduje Pandoc a XeLaTeX. Generované soubory nikdy needitujte ručně; opravy provádějte v masteru, konfiguraci nebo `tools/textbook.py`.
