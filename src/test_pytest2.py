import pytest

def sum(a, b):
    return a + b

@pytest.fixture(autouse=True)
def before_after():
    # Process before a test execution
    print("BEFORE")
    yield # Actual test is executed here
    print("AFTER")
    # Process after a test execution

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



class TestMyTest():
    def test_sum(self):
        result = sum(1, 2)
        assert result == 3

