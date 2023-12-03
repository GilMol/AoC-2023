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

def Handle_Red(value):
    global r
    if value > r:
        r = value

def Handle_Green(value):
    global g
    if value > g:
        g = value

def Handle_Blue(value):
    global b
    if value > b:
        b = value

def switch(color, value):
    switcher = {
        'red' : Handle_Red,
        'green' : Handle_Green,
        'blue' : Handle_Blue
    }

    func = switcher.get(color,lambda x:"wrong color")
    return func(value)

def CalculatePower(match):
    for m in match:
        if m.group(2) is not None:
            colorMatch = re.findall(r"\D+",m.group(2))[0]
            numberOfCubes = int(m.group(0))
            switch(colorMatch.strip(),numberOfCubes)


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

pow = 0

for l in lines:
    r=0
    g=0
    b=0
    match = re.finditer(pattern,l)
    # CheckSum(match)
    CalculatePower(match)
    pow+=(r*g*b)

print(pow)