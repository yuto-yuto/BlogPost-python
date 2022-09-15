"""triple_quotes examples. module comment here """

from tokenize import Double


print("Hello\nHow are you?\nI'm Yuto.\n")
print("Hello\n"
      "How are you?\n"
      "I'm Yuto.\n")

print("""Hello
How are you?
I'm Yuto.
""")

print("""
Hello
How are you?
I'm Yuto.
""")

print('''Hello
How are you?
I'm Yuto.
''')

additional = "additional information here"
print(f"""
Hello
How are you?
I'm Yuto.
{additional}
""")

print(type("Hello"))


def doSomething():
    """
    documentation here
    first line

    second line here

    """
    print("Hello")


doSomething()

""" something """


def notWork():
    print("a")
    """something"""
    return 3


notWork()

str_val = "This is a string value"
""" It contains important information"""



print(str_val)


class MyClass():
    """
    This is my class.
    Here it should summarize this class behavior
    """

    x = 1
    """ This is a member"""

    def __init__(self, x):
        """ This is constructor information."""
        self.x = x
        pass

    def doSomething(self):
        """ Print do something to the console """
        print("do something")

    def sayHello(self):
        """ This function writes "Hello" to the console """
        print("Hello")
        self.doSomething()
        
class MyClass2(MyClass):
    pass



instance = MyClass()
instance.doSomething()
instance.sayHello()
print(instance.x)
