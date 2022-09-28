import pytest


class TestScope1:
    @pytest.mark.usefixtures(
        "fixture_function",
        "fixture_class",
        "fixture_module",
        "fixture_session")
    def test_one(self):
        pass

    @pytest.mark.usefixtures(
        "fixture_function",
        "fixture_class",
        "fixture_module",
        "fixture_session")
    def test_two(self):
        pass
