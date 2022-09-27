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


def flat2(element) -> list:
    if element == []:
        return element
    if isinstance(element[0], list):
        return flat2(element[0]) + flat2(element[1:])
    return element[:1] + flat2(element[1:])


TEST_DATASET = [
    [[1, 2, 3], [4, 5], [], [6]],
    [
        [1,
            [
                2, 3, [4, 5], [6], 7
            ]
         ],
        [22, 33, [44, 55]]
    ],
    [1, 2, [3, 4], [[5, 6], [7, 8]], [9, 10]],
    [
        [],
        [
            [
                [
                    [[11, 22], [33, 44]], [55, "66", [77]]
                ],
                [
                    ["first", ["BB"], []], [["CC", ["DD", "FF"]]]
                ]
            ],
            [
                ["99", "88"],
            ]
        ],
        [
            ["E", "F"],
            [55, [66, [77]]]
        ]
    ]
]

list_of_list = [range(5), range(3)]

flat_list = []
for x in list_of_list:
    for y in x:
        flat_list.append(y)
print(flat_list)


print([y for x in list_of_list for y in x])

# list_of_list = [range(5), [range(3), range(3)]]
# print([y for x in list_of_list for y in x])


print("---- flat ----")
[print(flat(x)) for x in TEST_DATASET]
print("--- whole ---")
print(flat(TEST_DATASET))

print("---- flat2 ----")
[print(flat2(x)) for x in TEST_DATASET]
print("--- whole ---")
print(flat2(TEST_DATASET))