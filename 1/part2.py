lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def getFirstNumber(line, spelledOutNumbers):
    firstRealNumber = ''
    firstRealNumberIndex = float('inf')
    
    for char in line:
        if char.isdigit():
            firstRealNumber = char
            firstRealNumberIndex = line.find(firstRealNumber)
            break

    for spelledOutNumber in spelledOutNumbers:
        if spelledOutNumber[1] < firstRealNumberIndex:
            firstRealNumber = str(spelledOutNumber[0])
            firstRealNumberIndex = spelledOutNumber[1]

    return firstRealNumber

def getLastNumber(line, spelledOutNumbers):
    lastRealNumber = ''
    lastRealNumberIndex = -1
    
    for char in line[::-1]:
        if char.isdigit():
            lastRealNumber = char
            lastRealNumberIndex = line.rfind(lastRealNumber)
            break

    for spelledOutNumber in spelledOutNumbers:
        if spelledOutNumber[1] > lastRealNumberIndex:
            lastRealNumber = str(spelledOutNumber[0])
            lastRealNumberIndex = spelledOutNumber[1]

    return lastRealNumber
        
def getSpelledOutNumbers(line):
    numbers = []
    for key in dict:
        index = 0
        while True:
            index = line.find(key, index)
            if index == -1:
                break
            numbers.append((dict[key], index))
            index += 1
    return numbers

sum = 0
for line in lines:
    spelledOutNumbers = getSpelledOutNumbers(line)
    spelledOutNumbers.sort(key=lambda x: x[1])
    
    firstNumber = getFirstNumber(line, spelledOutNumbers)
    lastNumber = getLastNumber(line, spelledOutNumbers)

    sum = sum + int(firstNumber + lastNumber)

print(sum)