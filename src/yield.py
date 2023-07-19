from typing import Iterator

def DoYield():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3


def NonYield():
    print("Hello World")


NonYield()

print("Call DoYield")
DoYield()
print("End DoYield\n")

print("Call DoYield 2")
print(DoYield())
result = DoYield()
[print(v) for v in result]
[print(v) for v in result]
print("End DoYield 2\n")

print("Call DoYield 3-1")
generator = DoYield()
print(next(generator))
print(next(generator))
print("End DoYield 3-1\n")

print("Call DoYield 3-2")
try:
    generator = DoYield()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except BaseException as err:
    # print("Error occurred: " + err)
    print(f"Error occurred: {err=}")
print("End DoYield 3-2\n")

print("Call DoYield 4")
for next_value in DoYield():
    print(next_value)
print("End DoYield 4\n")


def DoYield2(isInterrupted):
    print("first")
    yield 1

    print("second")
    yield 2

    if isInterrupted:
        return 99

    print("third")
    yield 3


print("Call DoYield2")
print("When False====")
[print(v) for v in DoYield2(False)]
print("When True====")
[print(v) for v in DoYield2(True)]
value = DoYield2(True)
print("End DoYield2\n")


def DoYield3(isInterrupted):
  print("Start")
  if isInterrupted:
    return 1
  yield 1
  yield 2
  yield 3

print("Call DoYield3")
result = DoYield3(True)
[print(v) for v in result]
print("End DoYield3")

def DoYield4():
    count = 0
    while count < 2:
        count += 1
        yield count
    
    try:
        raise StopIteration
    except:
        print("end yield")

print()
print("Call DoYield4")
result = DoYield4()
# [print(v) for v in result]
print(next(result))
print(next(result))
print(next(result))