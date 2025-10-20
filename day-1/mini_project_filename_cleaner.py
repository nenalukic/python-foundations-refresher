# Goal: take a list of messy filenames and clean them up.

import os

def normalize_paths(paths):
    """Return unique normalized paths (clean and consistent)."""
    cleaned = set()
    for p in paths:
        p = p.strip().lower()            # trim & lowercase
        p = os.path.normpath(p)          # normalize slashes
        parts = [part.strip().replace(" ", "") for part in p.split(os.sep)]  # Removes inner spaces inside each part
        clean_path = os.sep.join(parts)
        cleaned.add(clean_path)
    return sorted(cleaned)

paths = [
    "data / January.csv ",
    "Data/ february .csv",
    "data/March.csv"
]

print(normalize_paths(paths))
# Expected Output: ['data/february.csv', 'data/january.csv', 'data/march.csv']
