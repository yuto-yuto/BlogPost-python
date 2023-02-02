try:
    raise SyntaxError("Fake error")
except Exception as err:
    print(err)
    print(type(err).__name__)
    print(err.args)

try:
    raise ZeroDivisionError("Fake error")
except Exception as err:
    print(err)
    print(type(err).__name__)
    print(err.args)

try:
    1/0
except Exception as err:
    print(err)
    print(type(err).__name__)
    print(err.args)
