import conf

from ModuleNotFoundError.folder1.my_funcs import show_message
from folder1.my_funcs import sleep
from folder2.hello import hello

if __name__ == "__main__":
    count = 0
    while True:
        count += 1
        show_message(f"{hello()} {str(count)}")
        sleep(1)
