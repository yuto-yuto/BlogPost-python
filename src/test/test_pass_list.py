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
    print(f"values: {values}")


@pytest.mark.parametrize(
    argnames=["x", "y", "z"],
    argvalues=[
        (1, 2, 3)
    ]
)
def test_pass_multi_args(x, y, z):
    print(f"(x, y ,z): ({x}, {y}, {z})")


# @pytest.mark.parametrize(
#     argnames=["x"],
#     argvalues=[
#         ([1, 2, 3])
#     ]
# )
# def test_pass_list_fail(x):
#     print(f"List: {x}")


@pytest.mark.parametrize(
    argnames=["x", "y", "z"],
    argvalues=[
        ([1, 2, 3])
    ]
)
def test_pass_multi_args2(x, y, z):
    print(f"(x, y ,z): ({x}, {y}, {z})")
