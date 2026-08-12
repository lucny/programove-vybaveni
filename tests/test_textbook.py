import sys
import subprocess
import shutil
from pathlib import Path

import pytest
from PIL import Image

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


@pytest.fixture
def validation_repository(tmp_path):
    tools = tmp_path / "tools"
    tools.mkdir()
    shutil.copy2(ROOT / "tools" / "textbook.py", tools / "textbook.py")

    config = tmp_path / "textbook" / "config.yml"
    config.parent.mkdir()
    config.write_text(
        """liascript:
  reader_base: "https://liascript.github.io/course/?"
  raw_base: "https://raw.githubusercontent.com/example/test/main/"
  branch: "main"
build:
  strict_quizzes: true
  missing_images_are_errors: false
""",
        encoding="utf-8",
    )

    topic = tmp_path / "01-testovaci-okruh"
    topic.mkdir()
    master = ["# Testovací okruh", "", "Úvod.", ""]
    for lesson in range(1, 7):
        master.extend(
            [
                f"# {lesson}. Lekce {lesson}",
                "",
                f"## {lesson}.1 Podkapitola {lesson}",
                "",
                f"Text {lesson}.",
                "",
            ]
        )
        lesson_dir = topic / f"{lesson}-lekce"
        images = lesson_dir / "media" / "images"
        images.mkdir(parents=True)
        (lesson_dir / f"1-{lesson}-QUIZ.md").write_text(
            f"# Kvíz {lesson}\n", encoding="utf-8"
        )
        Image.new("RGB", (8, 6), "white").save(
            images / f"01-testovaci-okruh-{lesson}-{lesson}.webp", "WEBP"
        )
    (topic / "testovaci-okruh.md").write_text("\n".join(master), encoding="utf-8")
    return tmp_path


def test_current_repository_validation_succeeds():
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "errors=0" in result.stdout


def test_valid_fixture_succeeds(validation_repository):
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=validation_repository,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "errors=0" in result.stdout


def test_missing_quiz_is_critical_error(validation_repository):
    (validation_repository / "01-testovaci-okruh" / "3-lekce" / "1-3-QUIZ.md").unlink()
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=validation_repository,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "errors=0" not in result.stdout


def test_missing_lesson_is_critical_error(validation_repository):
    master = validation_repository / "01-testovaci-okruh" / "testovaci-okruh.md"
    text = master.read_text(encoding="utf-8")
    text = text.replace(
        "# 6. Lekce 6\n\n## 6.1 Podkapitola 6\n\nText 6.\n", ""
    )
    master.write_text(text, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=validation_repository,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "errors=0" not in result.stdout


def test_duplicate_image_is_critical_error(validation_repository):
    images = validation_repository / "01-testovaci-okruh" / "1-lekce" / "media" / "images"
    shutil.copy2(images / "01-testovaci-okruh-1-1.webp", images / "1-1.webp")
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=validation_repository,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "errors=0" not in result.stdout


def test_missing_webp_is_warning_only(validation_repository):
    image = (
        validation_repository
        / "01-testovaci-okruh"
        / "2-lekce"
        / "media"
        / "images"
        / "01-testovaci-okruh-2-2.webp"
    )
    image.unlink()
    result = subprocess.run(
        [sys.executable, "tools/textbook.py", "validate"],
        cwd=validation_repository,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "errors=0" in result.stdout
    assert "warnings=1" in result.stdout
