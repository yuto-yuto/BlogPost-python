from datetime import datetime
import os
from pathlib import Path

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S --- ")
    print(now + msg)
    # print(msg)
    # print(now.join(msg))

def readFile():
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    
    path = Path(f"{current_dir}/resources/data.txt")
    print(path.absolute())
    if not path.exists():
        log("file not found")
        return

    log("Read the file")
    with open(file=path, mode="r") as file:
        lines = file.readlines()
        print("".join(lines))
        # log(lines)

    # with open(file=path, mode="r") as file:
    #     lines = file.readlines()
    #     msg = "".join(lines)
    #     log(msg)

readFile()