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
    intermediate = ["".join(element) for element in values]
    result = "".join(intermediate)
    return intermediate, result


def solution2(values):
    intermediate = ["".join(str(element)) for element in values]
    result = "".join(intermediate)
    return intermediate, result


def solution3(values):
    intermediate = ["".join(map(str, element)) for element in values]
    result = "".join(intermediate)
    return intermediate, result


def flat(element) -> list:
    has_list = any([isinstance(x, list) for x in element])
    if not has_list:
        return element

    flatten_list = []
    for x in element:
        if isinstance(x, list):
            val = flat(x)
            flatten_list.extend(val)
        else:
            flatten_list.append(x)

    return flatten_list


def solution4(values):
    flatten_list = flat(values)

    intermediate = ["".join(str(element)) for element in flatten_list]
    result = "".join(intermediate)
    return intermediate, result


TEST_DATASET = [
    [1, 2, 3],
    ["1", "2", "3"],
    ["1", 2, 3],
    [["first"], ["second"]],
    [["1", "2"], ["3"]],
    [[1, 2, 3], [4, 5, 6]],
    [["1", 2, 3], [4, "5", 6]],
    [[["fir"], ["st"]], [["se", "co"], ["nd"]]],
    [[[11], [21, 22]], [[31, 32], [41, 42]]],
]


def run_test(callback, values):
    try:
        intermediate, result = callback(values)
        print(f"intermediate: {intermediate}")
        print(f"RESULT: {values} -> {result}")
    except Exception as err:
        print(f"ERROR: {values}, {format(err)}")
    finally:
        print()


print("=== solution1 ===")
[run_test(solution1, values) for values in TEST_DATASET]

print()
print("=== solution2 ===")
[run_test(solution2, values) for values in TEST_DATASET]

print()
print("=== solution3 ===")
[run_test(solution3, values) for values in TEST_DATASET]

print()
print("=== solution4 ===")
[run_test(solution4, values) for values in TEST_DATASET]

[print(flat(values)) for values in TEST_DATASET]
