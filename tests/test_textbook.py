import sys
import subprocess
import shutil
from pathlib import Path

import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.textbook import Book, ROOT, Topic


def test_all_topics_have_one_master():
    book = Book(ROOT)
    topics = book.discover()
    assert len(topics) == 20
    assert all(topic.master for topic in topics)


def test_pilot_parser_keeps_six_lessons_and_czech_text():
    book = Book(ROOT)
    topics = book.discover({"01", "02"})
    assert [len(topic.lessons) for topic in topics] == [6, 6]
    assert any(
        "informatika" in subchapter.title.lower()
        for subchapter in topics[0].lessons[0].subchapters
    )


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
            images / f"01-testovaci-okruh-{lesson}-1.webp", "WEBP"
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
        / "01-testovaci-okruh-2-1.webp"
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


def test_parser_preserves_four_real_subchapter_numbers_and_image_names(tmp_path):
    topic_dir = tmp_path / "topic"
    topic_dir.mkdir()
    master = topic_dir / "master.md"
    master.write_text(
        """# Téma

# 3. Lekce

## 3.1 První
Text.

## 3.2 Druhá
Text.

## 3.3 Třetí
Text.

## 3.4 Čtvrtá
Text.
""",
        encoding="utf-8",
    )
    topic = Topic(1, "topic", topic_dir, master=master)
    book = Book(tmp_path)
    book.parse_master(topic)
    subchapters = topic.lessons[0].subchapters
    topic.images = [
        topic_dir / "3-lekce" / "media" / "images" / f"topic-3-{number}.webp"
        for number in range(1, 5)
    ]

    assert [sub.full_number for sub in subchapters] == ["3.1", "3.2", "3.3", "3.4"]
    assert [sub.source_heading for sub in subchapters] == [
        "3.1 První",
        "3.2 Druhá",
        "3.3 Třetí",
        "3.4 Čtvrtá",
    ]
    matches = [
        book.image_matches(topic, sub.lesson_number, sub.number)[0].name
        for sub in subchapters
    ]
    assert matches == [
        "topic-3-1.webp",
        "topic-3-2.webp",
        "topic-3-3.webp",
        "topic-3-4.webp",
    ]
    assert len(matches) == len(set(matches))


def test_subchapter_numbering_is_independent_of_lesson_number(tmp_path):
    topic_dir = tmp_path / "topic"
    topic_dir.mkdir()
    master = topic_dir / "master.md"
    master.write_text(
        """# Téma

# 1. První lekce
## 1.1 První
## 1.2 Druhá

# 2. Druhá lekce
## 2.1 První
## 2.2 Druhá

# 6. Šestá lekce
## 6.1 První
## 6.2 Druhá
## 6.3 Třetí
""",
        encoding="utf-8",
    )
    topic = Topic(1, "topic", topic_dir, master=master)
    book = Book(tmp_path)
    book.parse_master(topic)

    assert [[sub.full_number for sub in lesson.subchapters] for lesson in topic.lessons] == [
        ["1.1", "1.2"],
        ["2.1", "2.2"],
        ["6.1", "6.2", "6.3"],
    ]


def test_subchapter_from_another_lesson_is_validation_error(tmp_path):
    topic_dir = tmp_path / "topic"
    topic_dir.mkdir()
    master = topic_dir / "master.md"
    master.write_text(
        "# Téma\n\n# 3. Lekce\n\n## 2.4 Chybně zařazená\n",
        encoding="utf-8",
    )
    topic = Topic(1, "topic", topic_dir, master=master)
    book = Book(tmp_path)
    book.parse_master(topic)

    assert any("podkapitola 2.4 nepatří do lekce 3" in error for error in book.errors)


def test_all_current_subchapter_numbers_and_image_names_are_unambiguous():
    book = Book(ROOT)
    topics = book.discover()
    total = 0
    used_images = set()

    for topic in topics:
        for lesson in topic.lessons:
            full_numbers = [sub.full_number for sub in lesson.subchapters]
            assert len(full_numbers) == len(set(full_numbers))
            for sub in lesson.subchapters:
                total += 1
                assert sub.lesson_number == lesson.number
                assert sub.full_number == f"{lesson.number}.{sub.number}"
                matches = book.image_matches(topic, sub.lesson_number, sub.number)
                assert all(
                    image.name
                    in {
                        f"{topic.slug}-{sub.lesson_number}-{sub.number}.webp",
                        f"{sub.lesson_number}-{sub.number}.webp",
                    }
                    for image in matches
                )
                if len(matches) == 1:
                    assert matches[0].resolve() not in used_images
                    used_images.add(matches[0].resolve())

    assert total == 607
