data = 12366.12345
print(format(data, ".3g"))  # 1.24e+04
print(format(data, ".3f"))  # 12366.124
print(format(data, ".3e"))  # 1.237e+04
print(format(data, ".3"))   # 1.24e+04

print()

print(format(data, "%03.2f"))
