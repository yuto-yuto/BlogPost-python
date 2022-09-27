import pytest


TEST_DATASET = [
    [[1, 2, 3]],
    [["1", "2", "3"]],
    [["1", 2, 3]],
    [[[1, 2, 3], [4, 5, 6]]],
    [[["1", 2, 3], [4, "5", 6]]],
    [[[[11, 12, 13], [21, 22]], [[31, 32], [41, 42]]]],
]


@pytest.mark.parametrize(
    argnames=["values"],
    argvalues=TEST_DATASET
)
def test_pass_list(values):
    print(f"Solution 1: {values}")
