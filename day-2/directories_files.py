import os

files = os.listdir(".")
print("Files in current directory:")
for f in files:
    print(" -", f)
print("Total files:", len(files))

from pathlib import Path

data_dir = Path("data")

# Create folder if not exists
data_dir.mkdir(exist_ok=True)

# Create test files
for i in range(3):
    (data_dir / f"file_{i}.txt").write_text(f"File number {i}")

# List files
for file in data_dir.iterdir():
    print(file.name)
print("Total files in 'data' directory:", len(list(data_dir.iterdir())))