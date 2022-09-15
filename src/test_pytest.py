import pytest


def sum(a, b):
    return a + b


def test_sum_one_plus_two():
    print("start test_sum_one_plus_two")
    result = sum(1, 2)
    assert result == 3
    print("end")


def test_sum_fail():
    print("start test_sum_fail")
    result = sum(1, 2)
    try:
        assert result == 4
    finally:
        print("end")


@pytest.mark.parametrize(
    argnames=["x", "y", "expected"],
    argvalues=[
        (1, 1, 2),
        (-1, 1, 0),
        (0, 0, 0),
    ]
)
def test_parameterized(x, y, expected):
    print(f"(x, y, expected) = ({x}, {y}, {expected})")
    result = sum(x, y)
    assert result == expected


class TestMyTest():
    def test_sum(self):
        result = sum(1, 2)
        assert result == 3
