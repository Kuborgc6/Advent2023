import re

file = open('input.txt', 'r')
# file = open('input_test.txt', 'r')

lines = [line.split() for line in file]
result = 0

condition_dict = {'red': 12, 'green': 13, 'blue': 14}
max_balls = 12+13+14

for line in lines:
    condition_match = True
    game_id = int(line[1][:-1])
    taken = list()
    temp = list()
    for balls in line[2:]:
        if ',' in balls:
            temp.append(balls[:-1])
        elif ';' in balls:
            temp.append(balls[:-1])
            taken.append(temp)
            temp = list()
        else:
            temp.append(balls)
    taken.append(temp)

    for take in taken:
        value = 0
        for i in range(int(len(take)/2)):
            value += int(take[2*i])
            if (condition_dict[take[2*i+1]] < int(take[2*i])) or value > max_balls:
                condition_match = False
                break
        if condition_match == False:
            break
    
    if condition_match:
        result += game_id

print(result)