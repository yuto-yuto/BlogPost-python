import os
import sys

print("Add necessary paths")

file_dir = os.path.dirname(__file__)
sys.path.insert(1, f"{file_dir}/..")
sys.path.insert(1, f"{file_dir}/folder1")
sys.path.insert(1, f"{file_dir}/folder2")

print("Added")