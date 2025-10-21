# Create a folder called reports and automatically generate 3 text files inside it:
# report_1.txt, report_2.txt, report_3.txt
# Each should contain the text: This is report 1 (or 2, or 3)
# Finally, list all files in the reports folder and print the total number of files.
import os
from pathlib import Path

reports_dir = Path("reports")

# Create folder if not exists
reports_dir.mkdir(exist_ok=True)

# Create report files
for i in range(1, 4):
    (reports_dir / f"report_{i}.txt").write_text(f"This is report {i}")

# List files in reports directory
files = list(reports_dir.iterdir())
print("Files in 'reports' directory:")
for f in files:
    print(" -", f.name)
print("Total number of files in 'reports' directory:", len(files))