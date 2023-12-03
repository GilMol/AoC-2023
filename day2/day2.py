import re

pattern = r"(?=(\d+:))\d+|(?=(\d+.\w+))\d+"
teststring = "Game 14: 4 blue, 2 green; 19 blue; 6 red, 17 blue; 10 blue, 7 red; 1 green, 2 blue, 7 red"

file = "E:\\repos\AoC\day2\input.txt"

testmatch = re.finditer(pattern,teststring)
        
with open(file) as f:
    lines= f.readlines()

def CheckDiceBag(match):
    # map string of input to get the max available dice
    cubes = {
        'red' : '12',
        'green' : '13',
        'blue' : '14'
    }
    onlyColorMatch = re.findall(r"\D+",match.group(2))[0]
    nrOfCubes = cubes[onlyColorMatch.strip()]
    print(f"{onlyColorMatch} with {nrOfCubes} and in the example are {int(match.group(0))}")
    if int(nrOfCubes) < int(match.group(0)):
        return False
    return True

sum = 0

def CheckSum(match):
    global sum
    isValid = True
    for m in match:
        if m.group(2) is not None:
            if isValid is True:
                isValid= CheckDiceBag(m)
        else:
            id = int(m.group(0))
    print(f"{isValid} {sum} {id}")
    if isValid is True:
        sum += id

# CheckSum(testmatch)

for l in lines:
    match = re.finditer(pattern,l)
    CheckSum(match)

print(sum)