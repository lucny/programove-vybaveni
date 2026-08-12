#!/usr/bin/env python3
"""Build the Read the Docs textbook from the repository's source topics."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
GENERATED = "<!--\nGENERATED FILE.\nDo not edit manually.\nGenerator: tools/textbook.py\nSource: {source}\n-->\n\n"
TOPIC_RE = re.compile(r"^(\d{2})-(.+)$")
LESSON_RE = re.compile(r"^(\d+)-lekce$")
QUIZ_RE = re.compile(r"^(?:(\d{1,2})-)?(\d+)-QUIZ\.md$", re.I)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)\s*$")
SUB_RE = re.compile(r"^(\d+)\.(\d+)\.?\s+(.+?)\s*$")
LESSON_HEADING_RE = re.compile(r"^(?:Lekce\s+)?(\d+)\.?\s*[:.-]?\s+(.+?)\s*$", re.I)


@dataclass
class Subchapter:
    lesson_number: int
    number: int
    full_number: str
    source_heading: str
    title: str
    lines: list[str] = field(default_factory=list)


@dataclass
class Section:
    number: int
    title: str
    lines: list[str] = field(default_factory=list)
    subchapters: list[Subchapter] = field(default_factory=list)


@dataclass
class Topic:
    number: int
    slug: str
    path: Path
    master: Path | None = None
    title: str = ""
    intro: list[str] = field(default_factory=list)
    lessons: list[Section] = field(default_factory=list)
    quizzes: dict[int, Path] = field(default_factory=dict)
    images: list[Path] = field(default_factory=list)
    supplements: list[tuple[Path, str]] = field(default_factory=list)


class Book:
    def __init__(self, root: Path = ROOT):
        self.root = root
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.topics: list[Topic] = []
        self.cfg = self._config()

    def _config(self) -> dict:
        p = self.root / "textbook" / "config.yml"
        cfg = {"raw_base": "", "reader_base": "https://liascript.github.io/course/?", "strict_quizzes": True}
        if p.exists():
            section = None
            for line in p.read_text(encoding="utf-8").splitlines():
                if line and not line.startswith(" ") and line.endswith(":"):
                    section = line[:-1]
                m = re.match(r"^\s+(\w+):\s*(.*)$", line)
                if m:
                    value = m.group(2).strip().strip('"\'')
                    if section == "liascript" and m.group(1) in {"raw_base", "reader_base", "branch"}:
                        cfg[m.group(1)] = value
                    if section == "build" and m.group(1) == "strict_quizzes":
                        cfg[m.group(1)] = value.lower() == "true"
        return cfg

    def discover(self, selected: set[str] | None = None) -> list[Topic]:
        self.topics = []
        for path in sorted(self.root.iterdir()):
            if not path.is_dir() or path.name in {"docs", "site", "tools", "textbook", "instrukce", "_generated", "node_modules", ".textbook-build"}:
                continue
            m = TOPIC_RE.match(path.name)
            if not m or (selected and m.group(1) not in selected):
                continue
            topic = Topic(int(m.group(1)), path.name, path)
            masters = [p for p in path.glob("*.md") if not re.search(r"README|QUIZ", p.name, re.I)]
            if len(masters) != 1:
                self.errors.append(f"{path.name}: očekáván právě jeden master Markdown, nalezeno {len(masters)}")
            else:
                topic.master = masters[0]
                self.parse_master(topic)
            self.find_assets(topic)
            self.topics.append(topic)
        return self.topics

    def parse_master(self, topic: Topic) -> None:
        assert topic.master
        lines = topic.master.read_text(encoding="utf-8").splitlines()
        headings: list[tuple[int, str, int]] = []
        fenced = False
        for i, line in enumerate(lines):
            if line.strip().startswith("```") or line.strip().startswith("~~~"):
                fenced = not fenced
            if not fenced:
                m = HEADING_RE.match(line)
                if m:
                    headings.append((len(m.group(1)), m.group(2), i))
        if headings:
            topic.title = re.sub(r"^\d{2}-", "", topic.slug).replace("-", " ").title()
            topic.title = headings[0][1]
        lesson_heads = [(level, title, pos) for level, title, pos in headings if level == 1 and LESSON_HEADING_RE.match(title)]
        if headings and headings[0][0] == 1:
            topic.intro = lines[headings[0][2] + 1 : lesson_heads[0][2] if lesson_heads else len(lines)]
        for idx, (_, raw_title, start) in enumerate(lesson_heads):
            m = LESSON_HEADING_RE.match(raw_title)
            if not m:
                continue
            num, title = int(m.group(1)), m.group(2)
            end = lesson_heads[idx + 1][2] if idx + 1 < len(lesson_heads) else len(lines)
            body = lines[start + 1 : end]
            section = Section(num, title, body)
            subheads = []
            fenced = False
            for j, line in enumerate(body):
                if line.strip().startswith("```") or line.strip().startswith("~~~"):
                    fenced = not fenced
                if not fenced:
                    hm = HEADING_RE.match(line)
                    if hm and len(hm.group(1)) == 2 and SUB_RE.match(hm.group(2)):
                        subheads.append((j, SUB_RE.match(hm.group(2))))
            for sidx, (pos, sm) in enumerate(subheads):
                assert sm
                sub_end = subheads[sidx + 1][0] if sidx + 1 < len(subheads) else len(body)
                sub_lesson = int(sm.group(1))
                sub_number = int(sm.group(2))
                full_number = f"{sub_lesson}.{sub_number}"
                if sub_lesson != num:
                    self.errors.append(
                        f"{topic.slug}: podkapitola {full_number} nepatří do lekce {num}"
                    )
                if any(sub.number == sub_number for sub in section.subchapters):
                    self.errors.append(
                        f"{topic.slug}: duplicitní číslo podkapitoly {full_number} v lekci {num}"
                    )
                section.subchapters.append(
                    Subchapter(
                        lesson_number=sub_lesson,
                        number=sub_number,
                        full_number=full_number,
                        source_heading=sm.group(0),
                        title=sm.group(3),
                        lines=body[pos + 1 : sub_end],
                    )
                )
            topic.lessons.append(section)

    def find_assets(self, topic: Topic) -> None:
        lesson_dirs: set[int] = set()
        for lesson_dir in sorted(topic.path.glob("*-lekce")):
            lm = LESSON_RE.match(lesson_dir.name)
            if not lm:
                continue
            lesson = int(lm.group(1))
            lesson_dirs.add(lesson)
            topic.images.extend(sorted({p.resolve() for p in lesson_dir.glob("media/images/*") if p.suffix.lower() == ".webp"}, key=lambda p: p.name.lower()))
            for q in lesson_dir.glob("*-QUIZ.md"):
                qm = QUIZ_RE.match(q.name)
                if not qm:
                    self.errors.append(f"{topic.slug}/{lesson_dir.name}: neplatný název kvízu {q.name}")
                    continue
                qtopic, qlesson = qm.groups()
                if qtopic and int(qtopic) != topic.number:
                    self.errors.append(f"{topic.slug}/{q.name}: špatné číslo tématu")
                if int(qlesson) != lesson:
                    self.errors.append(f"{topic.slug}/{q.name}: špatné číslo lekce")
                if int(qlesson) in topic.quizzes:
                    self.errors.append(f"{topic.slug}/{lesson_dir.name}: duplicitní kvíz pro lekci {lesson}")
                else:
                    topic.quizzes[int(qlesson)] = q
            supplement_dir = lesson_dir / "doplnky"
            if supplement_dir.exists():
                for p in sorted(supplement_dir.glob("*.md")):
                    h1 = next((HEADING_RE.match(x).group(2) for x in p.read_text(encoding="utf-8").splitlines() if HEADING_RE.match(x) and len(HEADING_RE.match(x).group(1)) == 1), None)
                    if not h1:
                        self.errors.append(f"{p.relative_to(self.root)}: doplněk nemá první H1")
                    else:
                        topic.supplements.append((p, h1))
        found_master = {lesson.number for lesson in topic.lessons}
        found_dirs = lesson_dirs
        missing_master = sorted(set(range(1, 7)) - found_master)
        missing_dirs = sorted(set(range(1, 7)) - found_dirs)
        if missing_master:
            self.errors.append(f"{topic.slug}: v masteru chybí lekce {', '.join(map(str, missing_master))}; nalezené: {', '.join(map(str, sorted(found_master))) or 'žádné'}")
        if missing_dirs:
            self.errors.append(f"{topic.slug}: v adresářích chybí lekce {', '.join(map(str, missing_dirs))}; nalezené: {', '.join(map(str, sorted(found_dirs))) or 'žádné'}")
        for lesson in range(1, 7):
            if lesson not in topic.quizzes:
                message = f"{topic.slug}/{lesson}-lekce: chybí QUIZ"
                (self.errors if self.cfg.get("strict_quizzes", True) else self.warnings).append(message)

    def image_matches(self, topic: Topic, lesson: int, sub: int) -> list[Path]:
        names = [f"{topic.slug}-{lesson}-{sub}.webp", f"{lesson}-{sub}.webp"]
        return [p for p in topic.images if p.name in names]

    def image_for(self, topic: Topic, lesson: int, sub: int) -> Path | None:
        matches = self.image_matches(topic, lesson, sub)
        if len(matches) > 1:
            message = f"{topic.slug}: více obrázků pro {lesson}.{sub}: {', '.join(p.name for p in matches)}"
            if message not in self.errors:
                self.errors.append(message)
            return None
        if matches:
            return matches[0]
        message = f"{topic.slug}: chybí WEBP pro podkapitolu {lesson}.{sub}"
        if message not in self.warnings:
            self.warnings.append(message)
        return None

    def raw_url(self, quiz: Path) -> str:
        base = str(self.cfg.get("raw_base", "")).strip()
        if not base:
            message = "LiaScript raw_base není nastaven; nelze bezpečně vytvořit veřejnou URL"
            if message not in self.errors:
                self.errors.append(message)
            return ""
        return str(self.cfg.get("reader_base", "https://liascript.github.io/course/?")) + base.rstrip("/") + "/" + quiz.relative_to(self.root).as_posix()

    def validate(self) -> bool:
        for topic in self.topics:
            for lesson in topic.lessons:
                for subchapter in lesson.subchapters:
                    self.image_for(
                        topic, subchapter.lesson_number, subchapter.number
                    )
                if lesson.number in topic.quizzes:
                    self.raw_url(topic.quizzes[lesson.number])
        return not self.errors

    def generated_text(self, source: str, body: str) -> str:
        return GENERATED.format(source=source) + body.rstrip() + "\n"

    def build(self) -> None:
        docs = self.root / "docs"
        if docs.exists():
            shutil.rmtree(docs)
        (docs / "assets/images").mkdir(parents=True)
        (docs / "downloads").mkdir()
        (docs / "stylesheets").mkdir()
        shutil.copy2(self.root / "textbook/theme/extra.css", docs / "stylesheets/extra.css")
        index = ["# Informatika", "", "Elektronická učebnice informatiky.", "", "## Tematické okruhy", ""]
        for topic in self.topics:
            td = docs / topic.slug
            td.mkdir()
            lesson_links = []
            intro = "\n".join(topic.intro).strip()
            body = f"# {topic.title}\n\n{intro}\n\n## Lekce\n\n" + "\n".join(f"- [{l.number}. {l.title}]({l.number}-lekce/index.md)" for l in topic.lessons)
            (td / "index.md").write_text(self.generated_text(str(topic.master.relative_to(self.root)) if topic.master else topic.slug, body), encoding="utf-8")
            index.append(f"- [{topic.number:02d} {topic.title}]({topic.slug}/index.md)")
            for lesson in topic.lessons:
                ld = td / f"{lesson.number}-lekce"
                ld.mkdir()
                chunks = [f"# {lesson.number}. {lesson.title}", ""]
                for subchapter in lesson.subchapters:
                    chunks += [f"## {subchapter.source_heading}", ""] + subchapter.lines + [""]
                    image = self.image_for(
                        topic, subchapter.lesson_number, subchapter.number
                    )
                    if image:
                        dest = docs / "assets/images" / topic.slug / f"{lesson.number}-lekce" / image.name
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(image, dest)
                        rel = Path("../../assets/images") / topic.slug / f"{lesson.number}-lekce" / image.name
                        chunks += [f"![Grafické shrnutí podkapitoly {subchapter.full_number} – {subchapter.title}]({rel.as_posix()})", ""]
                if lesson.number == 6:
                    end_marker = next((i for i, x in enumerate(lesson.lines) if x.strip().lower().startswith("# závěrečné propojení")), None)
                    if end_marker is not None:
                        chunks += lesson.lines[end_marker:] + [""]
                if lesson.number in topic.quizzes:
                    url = self.raw_url(topic.quizzes[lesson.number])
                    chunks += ["---", "", "## Procvičení lekce", "", "Ověřte si porozumění v interaktivním kvízu.", "", f"[Spustit interaktivní kvíz v LiaScriptu]({url}){{ .md-button .md-button--primary }}", ""]
                (ld / "index.md").write_text(self.generated_text(str(topic.master.relative_to(self.root)) if topic.master else topic.slug, "\n".join(chunks)), encoding="utf-8")
            for p, title in topic.supplements:
                lesson = next((x for x in topic.path.glob("*-lekce") if p.parent == x / "doplnky"), None)
                if lesson:
                    out = td / lesson.name / (p.stem + ".md")
                    out.write_text(self.generated_text(str(p.relative_to(self.root)), p.read_text(encoding="utf-8")), encoding="utf-8")
        (docs / "index.md").write_text(self.generated_text("repository topics", "\n".join(index) + "\n"), encoding="utf-8")
        self.write_mkdocs_nav()
        self.write_report()

    def write_mkdocs_nav(self) -> None:
        lines = ["site_name: Informatika", 'site_url: ""', "docs_dir: docs", "theme:", "  name: material", "  language: cs", "  features:", "    - navigation.sections", "    - navigation.indexes", "    - navigation.path", "    - navigation.top", "    - search.suggest", "    - search.highlight", "    - content.code.copy", "extra_css:", "  - stylesheets/extra.css", "plugins:", "  - search", "markdown_extensions:", "  - admonition", "  - attr_list", "  - md_in_html", "  - pymdownx.details", "  - pymdownx.superfences", "nav:", "  - Přehled: index.md"]
        for topic in self.topics:
            lines.append(f'  - "{topic.number:02d} {topic.title}":')
            lines.append(f"    - Přehled: {topic.slug}/index.md")
            for lesson in topic.lessons:
                lines.append(f'    - "{lesson.number}. {lesson.title}":')
                lines.append(f"      - Výukový text: {topic.slug}/{lesson.number}-lekce/index.md")
                for p, title in topic.supplements:
                    if p.parent.parent.name == f"{lesson.number}-lekce":
                        lines.append(f"      - {title}: {topic.slug}/{lesson.number}-lekce/{p.stem}.md")
        (self.root / "mkdocs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def write_report(self) -> None:
        counts = {"topics": len(self.topics), "lessons": sum(len(t.lessons) for t in self.topics), "subchapters": sum(len(s.subchapters) for t in self.topics for s in t.lessons), "quizzes": sum(len(t.quizzes) for t in self.topics), "webp": sum(len(t.images) for t in self.topics), "supplements": sum(len(t.supplements) for t in self.topics)}
        report = ["# TEXTBOOK BUILD REPORT", "", f"Datum: {datetime.now(timezone.utc).isoformat()}", "Git commit: NEOVĚŘENO (repozitář není Git pracovní kopie)", ""]
        labels = [("Témata", counts["topics"]), ("Lekce", counts["lessons"]), ("Podkapitoly", counts["subchapters"]), ("Nalezené QUIZ", counts["quizzes"]), ("Nalezené WEBP", counts["webp"]), ("Doplňkové kapitoly", counts["supplements"])]
        downloads = self.root / "docs" / "downloads"
        pdf_count = len(list(downloads.rglob("*.pdf"))) if downloads.exists() else 0
        tex_count = len(list(downloads.rglob("*.tex"))) if downloads.exists() else 0
        report += [f"- {k}: {v}" for k, v in labels] + [f"- PDF: {pdf_count if pdf_count else 'NEOVĚŘENO'}", f"- TEX: {tex_count if tex_count else 'NEOVĚŘENO'}", "", "## Diagnostika podle okruhů", ""]
        expected = set(range(1, 7))
        for topic in self.topics:
            master = str(topic.master.resolve()) if topic.master else "NENALEZEN"
            master_lessons = {lesson.number for lesson in topic.lessons}
            dir_lessons = {int(m.group(1)) for p in topic.path.glob("*-lekce") if (m := LESSON_RE.match(p.name))}
            report += [f"### {topic.slug}", f"- Master: `{master}`", f"- Lekce v masteru: {', '.join(map(str, sorted(master_lessons))) or 'žádné'}", f"- Chybějící lekce v masteru: {', '.join(map(str, sorted(expected - master_lessons))) or 'žádné'}", f"- Lekční adresáře: {', '.join(map(str, sorted(dir_lessons))) or 'žádné'}", f"- Chybějící lekční adresáře: {', '.join(map(str, sorted(expected - dir_lessons))) or 'žádné'}"]
            for lesson in range(1, 7):
                quiz = topic.quizzes.get(lesson)
                report.append(f"- QUIZ {lesson}: {str(quiz.resolve()) if quiz else 'CHYBÍ'}")
            duplicate_lines = []
            for lesson in topic.lessons:
                for subchapter in lesson.subchapters:
                    matches = self.image_matches(
                        topic, subchapter.lesson_number, subchapter.number
                    )
                    if len(matches) > 1:
                        duplicate_lines.append(
                            f"  - Obrázek {subchapter.full_number}:"
                        )
                        for image in matches:
                            try:
                                digest = hashlib.sha256(image.read_bytes()).hexdigest()
                                with Image.open(image) as opened:
                                    dimensions = f"{opened.width}x{opened.height}"
                            except Exception as exc:
                                digest = f"NEOVĚŘENO ({exc})"
                                dimensions = "NEOVĚŘENO"
                            duplicate_lines.append(f"    - cesta: `{image.resolve()}`; SHA-256: `{digest}`; rozměry: `{dimensions}`")
            report += duplicate_lines or ["- Duplicitní kandidáti obrázků: žádní"]
            report.append("")
        report += ["## Chyby", ""]
        report += [f"- {x}" for x in self.errors] or ["- žádné"]
        report += ["", "## Warningy", ""] + ([f"- {x}" for x in self.warnings] or ["- žádné"])
        (self.root / "TEXTBOOK-BUILD-REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
        (self.root / ".textbook-build").mkdir(exist_ok=True)
        (self.root / ".textbook-build/report.json").write_text(json.dumps({"counts": counts, "errors": self.errors, "warnings": self.warnings}, ensure_ascii=False, indent=2), encoding="utf-8")

    def export(self) -> bool:
        if shutil.which("pandoc") is None or shutil.which("xelatex") is None:
            self.errors.append("PDF/LaTeX export vyžaduje pandoc a xelatex")
            return False
        export_root = self.root / ".textbook-build" / "export-assets"
        if export_root.exists():
            shutil.rmtree(export_root)
        export_root.mkdir(parents=True)
        miktex_config = self.root / ".textbook-build" / "miktex-config"
        miktex_config.mkdir(parents=True, exist_ok=True)
        export_env = dict(__import__("os").environ)
        export_env["MIKTEX_USERCONFIG"] = str(miktex_config)
        export_env["MIKTEX_USERDATA"] = str(self.root / ".textbook-build" / "miktex-data")
        for topic in self.topics:
            out = self.root / "docs/downloads" / topic.slug
            out.mkdir(parents=True, exist_ok=True)
            lesson_inputs = []
            for lesson in range(1, 7):
                md = self.root / "docs" / topic.slug / f"{lesson}-lekce/index.md"
                if md.exists():
                    lesson_inputs.append(md)
            combined = []
            for md in lesson_inputs:
                text = md.read_text(encoding="utf-8")
                for image in re.findall(r"\((../../assets/images/[^)]+\.webp)\)", text):
                    src = self.root / "docs" / topic.slug / "1-lekce" / image.replace("../../", "").replace("/", "\\")
                    if not src.exists():
                        src = self.root / "docs" / image.replace("../../", "").replace("/", "\\")
                    png = export_root / Path(image).name.replace(".webp", ".png")
                    if src.exists() and not png.exists():
                        subprocess.run(["magick", str(src), str(png)], check=True, capture_output=True)
                    if png.exists():
                        text = text.replace(image, str(png))
                temp = export_root / (md.parent.name + "-" + md.parent.parent.name + ".md")
                temp.write_text(text, encoding="utf-8")
                combined.append(temp)
            all_text = export_root / f"{topic.slug}.md"
            all_text.write_text("\n\n\\newpage\n\n".join(p.read_text(encoding="utf-8") for p in combined), encoding="utf-8")
            commands = [(all_text, out / f"{topic.slug}.tex", out / f"{topic.slug}.pdf")]
            commands += [(p, out / f"{topic.slug}-{i}.tex", out / f"{topic.slug}-{i}.pdf") for i, p in enumerate(combined, 1)]
            for source, tex, pdf in commands:
                result = subprocess.run(["pandoc", str(source), "-f", "gfm", "-t", "latex", "--pdf-engine=xelatex", "-V", "mainfont=DejaVu Sans", "-o", str(tex)], cwd=self.root, capture_output=True, text=True)
                if result.returncode:
                    self.errors.append(f"Pandoc selhal pro {source.name}: {result.stderr[-500:]}")
                    continue
                result = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname", pdf.stem, str(tex)], cwd=out, env=export_env, capture_output=True, text=True)
                if result.returncode:
                    self.errors.append(f"XeLaTeX selhal pro {source.name}: {result.stdout[-500:]}")
        return not self.errors


def topics_arg(value: str) -> set[str]:
    return {x.strip().zfill(2) for x in value.split(",") if x.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["audit", "validate", "build", "export", "all"])
    parser.add_argument("--topics", type=topics_arg)
    parser.add_argument("--online", action="store_true", help="reserved for online URL checks")
    args = parser.parse_args()
    book = Book()
    book.discover(args.topics)
    if args.command == "audit":
        book.write_report()
    elif args.command == "validate":
        book.validate(); book.write_report()
    elif args.command == "build":
        book.validate(); book.build()
    elif args.command == "export":
        book.validate(); book.build(); book.export(); book.write_report()
    elif args.command == "all":
        book.validate(); book.build(); book.export(); book.write_report()
    print(f"topics={len(book.topics)} errors={len(book.errors)} warnings={len(book.warnings)}")
    return 0 if not book.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
