import re


file = "input.txt"
with open(file) as f:
    content = f.readlines()

numbers = []

for t in content:
    numbers.append(re.findall("\d{1}",t))

result = []

def concat(a,b):
    return int(f"{a}{b}")

for number in numbers:
    if(len(number)>1):
        result.append(concat(number[0],number[len(number)-1]))
    else:
        result.append(concat(int(number[0]),int(number[0])))

# print(numbers)
print(result)

sum = 0

for i in result:
    print(i)
    sum += i

print(sum)