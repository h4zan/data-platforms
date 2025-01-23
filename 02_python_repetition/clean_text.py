import re
from pathlib import Path

print(Path(__file__).parent)

with open("data/ml_text_raw.txt", "r") as file:
    raw_text = file.read()

text_fixed_spacing = re.sub(r"\s+", " ", raw_text)

print(text_fixed_spacing)
