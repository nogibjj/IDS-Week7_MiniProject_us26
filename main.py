import sys

sys.path.insert(0, "./mylib")
from read import read  # noqa: E402
from create import create  # noqa: E402
from update import update  # noqa: E402
from delete import delete  # noqa: E402
from delete import create_summary  # noqa: E402


def test_create():
    result = create("ranking.db")
    assert result == "Database with table named universities created"


def test_read():
    result = read("ranking.db")
    assert len(result[0]) == 34
    assert len(result[1]) == 6
    assert len(result[2]) == 2


def test_update():
    result = update("ranking.db")
    assert result[15][2] == "not found"


def test_delete():
    result = delete("ranking.db")
    assert len(result) < 321


create_summary(file_path="./Generated summary report.md")
