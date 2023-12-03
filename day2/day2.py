import re

pattern = r"(?=(\d+:))\d+|(?=(\d+.\w+))\d+"

file = "E:\\repos\AoC\day2\input.txt"

with open(file) as f:
    lines= f.readlines()

result = []
for l in lines:
    match = re.search(pattern,l)
    print(match.group(0))
    print(match.group(1))