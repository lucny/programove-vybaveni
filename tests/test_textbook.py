import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.textbook import Book, ROOT


def test_all_topics_have_one_master():
    book = Book(ROOT)
    topics = book.discover()
    assert len(topics) == 20
    assert all(topic.master for topic in topics)


def test_pilot_parser_keeps_six_lessons_and_czech_text():
    book = Book(ROOT)
    topics = book.discover({"01", "02"})
    assert [len(topic.lessons) for topic in topics] == [6, 6]
    assert any("informatika" in sub[1].lower() for sub in topics[0].lessons[0].subchapters)


def test_generated_files_have_guard_header():
    generated = ROOT / "docs" / "01-zaklady-informatiky" / "1-lekce" / "index.md"
    if generated.exists():
        assert generated.read_text(encoding="utf-8").startswith("<!--\nGENERATED FILE.")


def test_current_validation_has_nonzero_exit_for_critical_errors():
    result = subprocess.run([sys.executable, "tools/textbook.py", "validate"], cwd=ROOT)
    assert result.returncode != 0
