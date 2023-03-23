import sys

def main():
    print(f"Hello World! ({sys.argv})--- from main")


def sub():
    print(f"Hello World! ({sys.argv}) --- from sub")


if __name__ == "__main__":
    main()


sub()
