file = open('input.txt', 'r')
# file = open('input_test.txt', 'r')

lines = [line.split() for line in file]

print('test')
result = 0
for line in lines:
    separator = line.index('|')
    winning_numbers = line[2:separator]
    my_numbers = line[separator+1:]
    winning_numbers_set = set(winning_numbers) 
    my_numbers_set = set(my_numbers) 
    my_winning = winning_numbers_set.intersection(my_numbers_set)
    if my_winning:
        points = pow(2,len(my_winning)-1)
        result += points

print(result)
