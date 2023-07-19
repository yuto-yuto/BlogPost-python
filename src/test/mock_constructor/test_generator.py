import pytest

from mockito import mock, when
from .generator import ItemGenerator, FileType
from . import generator as GE


def test_execute_raise():
    instance = ItemGenerator()
    with pytest.raises(ValueError):
        instance.execute(FileType.folder, "ab")


def test_execute_mock_constructor():
    mock_instance = mock()
    when(GE).FolderGenerator(...).thenReturn(mock_instance)
    when(mock_instance).generate(...).thenReturn("fake value")

    instance = ItemGenerator()
    result = instance.execute(FileType.folder, "ab")
    assert result == "fake value"

def test_execute_mock_constructor2():
    mock_instance = mock()
    when(GE).FolderGenerator(...).thenReturn(mock_instance)
    when(mock_instance).generate(...).thenReturn("copied")

    instance = ItemGenerator()
    result = instance.execute(FileType.folder, "ab")
    assert result == "copied"
