# setup_uv.py
import os

# Read packages from requirements.txt
with open("requirements.txt") as f:
    packages = f.read().splitlines()

for pkg in packages:
    os.system(f"uv add {pkg}")