import pathlib as path
import sys
import os
import subprocess

if __name__ == "__main__":
    print("--- import ---")
    import main_check

    print("--- exec ---")
    filepath = path.Path(__file__).parent.joinpath("main_check.py")
    # exec(open("/workspaces/blogpost-python/src/main_check.py").read())
    exec(open(filepath).read())

    print("--- exec2 ---")
    print(sys.argv)  # ['src/exec_another_file.py']
    original_argv = sys.argv

    sys.argv = ["arg1", "arg2"]
    exec(open(filepath).read())
    # Hello World! (['arg1', 'arg2'])--- from main
    # Hello World! (['arg1', 'arg2']) --- from sub

    print(sys.argv)  # ['arg1', 'arg2']
    sys.argv = original_argv
    print(sys.argv)  # ['src/exec_another_file.py']

    print("--- subprocess.call ---")
    print(sys.executable)
    res = subprocess.call([sys.executable, filepath, "one", "two"])
    # Hello World! (['/workspaces/blogpost-python/src/main_check.py', 'one', 'two'])--- from main
    # Hello World! (['/workspaces/blogpost-python/src/main_check.py', 'one', 'two']) --- from sub

    print(res)  # 0

    print("--- subprocess.run ---")
    res = subprocess.run([sys.executable, filepath, "one", "two"],
                         capture_output=True, check=False)
    print(res.returncode) # 0
    print(res.stderr) # b''
    print(res.stdout) # b"Hello World! (['/workspaces/blogpost-python/src/main_check.py', 'one', 'two'])--- from main\nHello World! (['/workspaces/blogpost-python/src/main_check.py', 'one', 'two']) --- from sub\n"

# --- import ---
# Hello World! --- from sub
# --- exec ---
# Hello World! --- from main
# Hello World! --- from sub
