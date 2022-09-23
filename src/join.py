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


print("--- ".join("a"))     # a
print("--- ".join("abc"))   # a--- b--- c
print("--- ".join(["a", "b", "c"]))     # a--- b--- c
print("--- ".join(["ab", "cd", "ef"]))  # ab--- cd--- ef
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


def solution1(list):
    inside = ["".join(element) for element in list]
    print(f"inside: {inside}")  # inside: ['first', 'second']
    print("--- ".join(inside))  # first--- second


print()
list = [["first"], ["second"]]
solution1([["first"], ["second"]])

try:
    solution1([[1], [2]])
except BaseException as e:
    # sequence item 0: expected str instance, int found
    print(e)

print()


def solution2(list):
    inside = ["".join(str(element)) for element in list]
    print(f"inside: {inside}") # inside: ["['1', 2, 3, 4]", '[9, 8, 7, 6]']
    print("--- ".join(inside)) # ['1', 2, 3, 4]--- [9, 8, 7, 6]


solution2([["1", 2, 3, 4], [9, 8, 7, 6]])

print()


def solution3(list):
    inside = ["".join(map(str, element)) for element in list]
    print(f"inside: {inside}") # inside: ['1234', '9876']
    print("--- ".join(inside)) # 1234--- 9876


solution3([["1", 2, 3, 4], [9, 8, 7, 6]])

mapData = map(str, ["1", 2, 3, 4])
[print(x) for x in mapData]
# 1
# 2
# 3
# 4

lines = [
    "first line\n",
    "second line\n",
    "third line\n",
]

print("\n".join(lines))
# first line
# 
# second line
# 
# third line
# 