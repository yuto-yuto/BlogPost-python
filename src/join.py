# import logging

# logging.basicConfig()
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.info("ABC")
# logger.warning(["aaa", "bbb"])
# logger.warning(["aaa", "bbb"])
# exit()


def join(data):
    print("--- ".join(data))


print("--- ".join("a"))
print("--- ".join("abc"))
print("--- ".join(["a", "b", "c"]))
print("--- ".join(["ab", "cd", "ef"]))
try:
    print("--- ".join([["a", "b"], ["c", "d"]]))
except BaseException as e:
    print(e)

try:
    print("--- ".join([["first"], ["second"]]))
except BaseException as e:
    print(e)


def solution1(list):
    inside = ["".join(element) for element in list]
    print(f"inside: {inside}")
    print("--- ".join(inside))


print()
list = [["first"], ["second"]]
solution1([["first"], ["second"]])

try:
    solution1([[1], [2]])
except BaseException as e:
    print(e)

print()


def solution2(list):
    inside = ["".join(str(element)) for element in list]
    print(f"inside: {inside}")
    print("--- ".join(inside))


solution2([["1", 2, 3, 4], [9, 8, 7, 6]])

print()


def solution3(list):
    inside = ["".join(map(str, element)) for element in list]
    print(f"inside: {inside}")
    print("--- ".join(inside))


solution3([["1", 2, 3, 4], [9, 8, 7, 6]])

mapData = map(str, ["1", 2, 3, 4])
[print(x) for x in mapData]

lines = [
    "first line\n",
    "second line\n",
    "third line\n",
]

print("\n".join(lines))
