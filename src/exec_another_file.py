import pathlib as path

if __name__ == "__main__":
    print("--- import ---")
    import main_check

    print("--- exec ---")
    filepath = path.Path(__file__).parent.joinpath("main_check.py")
    # exec(open("/workspaces/blogpost-python/src/main_check.py").read())
    exec(open(filepath).read())

# --- import ---
# Hello World! --- from sub
# --- exec ---
# Hello World! --- from main
# Hello World! --- from sub