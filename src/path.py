from pathlib import Path

path = Path(".")
print(f"""exists: {path.exists()}
is_dir: {path.is_dir()}
absolute: {path.absolute()}
""")
