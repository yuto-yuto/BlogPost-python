print("--- ".join("a"))     # a
print("--- ".join("abc"))   # a--- b--- c
print("--- ".join(["a", "b", "c"]))     # a--- b--- c
print("--- ".join(["ab", "cd", "ef"]))  # ab--- cd--- ef
print(",".join(["one", "two", "three"]))  # one,two,three


try:
    print("--- ".join([["a", "b"], ["c", "d"]]))
except BaseException as e:
    # sequence item 0: expected str instance, list found
    print(e)

try:
    print("--- ".join([["first"], ["second"]]))
except BaseException as e:
    # sequence item 0: expected str instance, list found
    print(e)


def solution1(values):
    inside = ["".join(element) for element in values]
    result = "".join(inside)
    return inside, result
    # print(f"inside: {inside}")  # inside: ['first', 'second']
    # print("--- ".join(inside))  # first--- second


# print()
# solution1([["first"], ["second"]])
# solution1([["1", "2", "3"], ["4", "5", "6"]])
# solution1([1, 2, 3])
# solution1([[1, 2, 3], [4, 5, 6]])
# solution1([["1", 2, 3], [4, 5, 6]])
# solution1([[[11, 12, 13], [21, 22]], [[31, 32], [41, 42]]])

# try:
#     solution1([[1], [2]])
# except BaseException as e:
#     # sequence item 0: expected str instance, int found
#     print(e)

# print()


def solution2(values):
    inside = ["".join(str(element)) for element in values]
    result = "".join(inside)
    return inside, result
    # inside = ["".join(str(element)) for element in values]
    # print(f"inside: {inside}")  # inside: ["['1', 2, 3, 4]", '[9, 8, 7, 6]']
    # print("--- ".join(inside))  # ['1', 2, 3, 4]--- [9, 8, 7, 6]


# solution2([1, 2, 3])
# solution2([1, 2, 3])
# solution2([["1", 2, 3, 4], [9, 8, 7, 6]])

# print()


def solution3(values):
    inside = ["".join(map(str, element)) for element in values]
    print(f"inside: {inside}")  # inside: ['1234', '9876']
    print("--- ".join(inside))  # 1234--- 9876


# solution3([["1", 2, 3, 4], [9, 8, 7, 6]])

# mapData = map(str, ["1", 2, 3, 4])
# [print(x) for x in mapData]
# 1
# 2
# 3
# 4

lines = [
    "first line\n",
    "second line\n",
    "third line\n",
]

# print("\n".join(lines))
# first line
#
# second line
#
# third line
#

TEST_DATASET = [
    [1, 2, 3],
    ["1", "2", "3"],
    ["1", 2, 3],
    [[1, 2, 3], [4, 5, 6]],
    [["1", 2, 3], [4, "5", 6]],
    [[[11], [21, 22]], [[31, 32], [41, 42]]],
]


def run_test(callback, values):
    try:
        callback(values)
    except Exception as err:
        print(f"ERROR: {values}, {format(err)}")


print("=== solution1 ===")
[run_test(solution1,values) for values in TEST_DATASET]

print()
print("=== solution2 ===")
[run_test(solution2,values) for values in TEST_DATASET]

print()
print("=== solution3 ===")
[run_test(solution3,values) for values in TEST_DATASET]
