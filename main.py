"""Print the one-line entry from entry.txt (cwd-independent)."""
import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), encoding="utf-8") as f:
    print(f.read().strip())
