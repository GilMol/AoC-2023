import re

teststring ="Card   1: 73 92 13 35 18 96 37 72 76 39 | 82 73 66 57 25 98 49 28  3 95 81 85 31 30 35 79  7 12 55 76 97 45  9 92  2"

file = "E:\\repos\AoC\day4\input.txt"

globalval = 0

def handleline(line):
    global globalval
    splitted = line.split('|')
    split1 = splitted[0]
    split2 = splitted[1]
    value = 0
    numbersStr1 =re.findall(r'(\d+)',split1)
    numbersStr2 =re.findall(r'(\d+)',split2)
    numbersStr1.remove(numbersStr1[0])
    for number in numbersStr2:
        if numbersStr1.__contains__(number):
            if value == 0:
                value =1
            else:
                value *=2
    globalval += value
    # print(globalval)

with open(file) as f:
    lines = f.readlines()

for line in lines :
    handleline(line)


print(globalval)