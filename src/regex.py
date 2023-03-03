import re

def run_regex(text):
    regex_str = r"([0-9a-zA-Z_\.]+) ([0-9a-zA-Z_]+) * = *(\d+);"
    result = re.search(regex_str, text)
    if result:
        print(result)
        print(result.group(0))
        print(result.group(1))
        print(result.group(2))
        print(result.group(3))

run_regex("my.data.type data_1 = 1;")
# <re.Match object; span=(0, 24), match='my.data.type data_1 = 1;'>
# my.data.type data_1 = 1;
# my.data.type
# data_1
# 1
run_regex("product.count count = 26;")
# <re.Match object; span=(0, 25), match='product.count count = 26;'>
# product.count count = 26;
# product.count
# count
# 26

def run_nested_regex(text):
    regex_str = r"(product_name: (.+), price: (\d+))|(name<(.+)>, price<(\d+)>)"
    result = re.search(regex_str, text)
    if result is not None:
        for index, group in enumerate(result.groups()):
            print(f"{index}: {group}")

format1_text = "product_name: super-pc, price: 100"
format2_text = "name<super-pc>, price<100>"

print("--- run_nested_regex")
run_nested_regex(format1_text)
# 0: product_name: super-pc, price: 100
# 1: super-pc
# 2: 100
# 3: None
# 4: None
# 5: None
run_nested_regex(format2_text)
# 0: None
# 1: None
# 2: None
# 3: name<super-pc>, price<100>
# 4: super-pc
# 5: 100


def run_nested_regex2(text):
    regex_str = r"(product_name: (.+), price: (\d+))|(name<(.+)>, price<(\d+)>)"
    result = re.search(regex_str, text)
    if result is not None:
        print(result.lastindex)
        print(f"0: {result.group(0)}")
        print(f"1: {result.group(1)}")
        print(f"2: {result.group(2)}")
        print(f"3: {result.group(3)}")
        print(f"4: {result.group(4)}")
        print(f"5: {result.group(5)}")
        print(f"6: {result.group(6)}")

print("--- run_nested_regex2")
run_nested_regex2(format1_text)
# 1
# 0: product_name: super-pc, price: 100
# 1: product_name: super-pc, price: 100
# 2: super-pc
# 3: 100
# 4: None
# 5: None
# 6: None
run_nested_regex2(format2_text)
# 4
# 0: name<super-pc>, price<100>
# 1: None
# 2: None
# 3: None
# 4: name<super-pc>, price<100>
# 5: super-pc
# 6: 100
