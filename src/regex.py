import re

regex_str = r"([0-9a-zA-Z_\.]+) ([0-9a-zA-Z_]+) * = *(\d+);"
str = "my.data.type data_1 = 1;"

match = re.search(regex_str,str)
if match:
    print(match)    # <re.Match object; span=(0, 24), match='my.data.type data_1 = 1;'>
    print(match.group(0))   # my.data.type data_1 = 1;
    print(match.group(1))   # my.data.type
    print(match.group(2))   # data_1
    print(match.group(3))   # 1
