import pytest


@pytest.fixture(autouse=True)
def before_after():
    # Process before a test execution
    print("\nBEFORE ---")

    yield  # Actual test is executed here

    # Process after a test execution
    print("\nAFTER ---")


@pytest.fixture()
def func1():
    return "This is func1"


def test_1_1():
    print("fixture is not used")
    pass


def test_1_2(func1):
    print(func1)
    pass


@pytest.fixture(name="func2_name")
def func2():
    print("func2 --- inner")
    return "This is func2"


@pytest.mark.skip("Test fails")
def test_2_1(func2):
    pass


def test_2_2(func2_name):
    print(func2_name)
    pass


@pytest.mark.usefixtures("func2_name")
def test_2_3():
    pass
