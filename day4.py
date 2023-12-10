file = open('input.txt', 'r')
# file = open('input_test.txt', 'r')

lines = [line.split() for line in file]

print('test')
result = 0
how_many_scratchcards = dict()
for i in range(len(lines)):
    how_many_scratchcards[i] = 1

for i in range(len(lines)):
    for j in range(how_many_scratchcards[i]):
        line = lines[i]
        game = int(line[1][:-1])
        separator = line.index('|')
        winning_numbers = line[2:separator]
        my_numbers = line[separator+1:]
        winning_numbers_set = set(winning_numbers) 
        my_numbers_set = set(my_numbers) 
        my_winning = winning_numbers_set.intersection(my_numbers_set)
        if my_winning:
            for k in range(len(my_winning)):
                how_many_scratchcards[game + k] += 1

print(sum(how_many_scratchcards.values()))
