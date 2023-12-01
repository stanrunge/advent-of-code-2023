lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

def getFirstNumber(line):
    for char in line:
        if char.isdigit():
            return char
        

def getLastNumber(line):
    for char in line[::-1]:
        if char.isdigit():
            return char


sum = 0
for line in lines:
    firstNumber = getFirstNumber(line)
    lastNumber = getLastNumber(line)

    sum = sum + int(firstNumber + lastNumber)

print(sum)