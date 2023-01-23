import pytest

from pathlib import Path


# def unstub_after_test(unstub):
#     yield
#     unstub()


def test_1():
    filepath = Path.joinpath(Path(__file__).parent, "test_file.txt")
    result = Path.read_text(filepath)
    assert result == "data123"


def test_2(when):
    when(Path).read_text().thenReturn("dummy data1")
    filepath = Path.joinpath(Path(__file__).parent, "test_file.txt")
    result = Path.read_text(filepath)
    assert result == "dummy data1"


def test_3(when):
    when(Path).read_text().thenReturn("dummy data2")
    filepath = Path.joinpath(Path(__file__).parent, "test_file.txt")
    result = Path.read_text(filepath)
    assert result == "dummy data2"


def test_4():
    filepath = Path.joinpath(Path(__file__).parent, "test_file.txt")
    result = Path.read_text(filepath)
    assert result == "data123"
