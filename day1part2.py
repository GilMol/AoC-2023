import re
from day1 import concat

# Test string with overlapping words
test_string = "three28jxdmlqfmc619eightwo"

# Regex pattern to match words that represent numbers (allowing overlaps)
pattern = r'(?=(zero|one|two|three|four|five|six|seven|eight|nine))'

# Function to convert word to digit
def word_to_digit(match):
    word_to_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return word_to_num[match.group(1)]

# Find all matches (including overlapping ones) and replace words with corresponding digits
file = "input.txt"

with open(file) as f:
    content = f.readlines()

numbers = []

for t in content:
    numbers.append(re.findall(r'\d',re.sub(pattern,word_to_digit,t)))

result = []

for number in numbers:
    if(len(number)>1):
        result.append(concat(number[0],number[len(number)-1]))
    else:
        result.append(concat(int(number[0]),int(number[0])))

sum = 0

for i in result:
    sum+=i

print(sum)
