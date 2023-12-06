lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

accepted_games = []

for line in lines:
    game_number = int(line.split()[1].split(':')[0])

    valid = True

    sets = line.split(':')[1].split(';')
    for set in sets:
        pulls = set.split(',')
        for pull in pulls:
            pull_info = pull.split()

            if (pull_info[1] == 'red' and int(pull_info[0]) > 12):
                valid = False
            
            if (pull_info[1] == 'green' and int(pull_info[0]) > 13):
                valid = False

            if (pull_info[1] == 'blue' and int(pull_info[0]) > 14):
                valid = False

    if valid:
        accepted_games.append(game_number)
    
print('Sum of accepted game IDs:', sum(accepted_games))