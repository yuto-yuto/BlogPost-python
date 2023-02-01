text = "   aaaaa bbbb ccc     "
print(f"origin\t [{text}]")          # origin   [   aaaaa bbbb ccc     ]
print(f"rstrip\t [{text.rstrip()}]") # rstrip   [   aaaaa bbbb ccc]
print(f"lstrip\t [{text.lstrip()}]") # lstrip   [aaaaa bbbb ccc     ]
print(f"strip\t [{text.strip()}]")   # strip    [aaaaa bbbb ccc]

print()
text2 = "! *** Hello World!!"
# print(f"rstrip [{text3.rstrip("!")}]") Error due to double quotations
print(f"rstrip('!')\t [{text2.rstrip('!')}]") # rstrip('!')      [! *** Hello World]
print(f"lstrip('!')\t [{text2.lstrip('!')}]") # lstrip('!')      [ *** Hello World!!]
print(f"strip('!')\t [{text2.strip('!')}]")   # strip('!')       [ *** Hello World]

print()
print(f"rstrip('!')\t [{text2.rstrip('* !')}]") # rstrip('!')      [! *** Hello World]
print(f"lstrip('!')\t [{text2.lstrip('* !')}]") # lstrip('!')      [Hello World!!]
print(f"strip('!')\t [{text2.strip('* !')}]")   # strip('!')       [Hello World]

