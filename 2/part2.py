lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

sum = 0

for line in lines:
    game_number = int(line.split()[1].split(':')[0])

    max_red = 0
    max_green = 0
    max_blue = 0

    sets = line.split(':')[1].split(';')
    for set in sets:
        pulls = set.split(',')
        for pull in pulls:
            pull_info = pull.split()

            if (pull_info[1] == 'red' and int(pull_info[0]) > max_red):
                max_red = int(pull_info[0])
            
            if (pull_info[1] == 'green' and int(pull_info[0]) > max_green):
                max_green = int(pull_info[0])

            if (pull_info[1] == 'blue' and int(pull_info[0]) > max_blue):
                max_blue = int(pull_info[0])

    sum = sum + (max_red * max_green * max_blue)
    
print('Sum:', sum)