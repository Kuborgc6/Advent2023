import re

file = open('input.txt', 'r')
# file = open('input_test.txt', 'r')

lines = [line.split()[0] for line in file]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_letter = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = list()
for line in lines:
    temp = ''
    temp_dic = dict()
    for number in numbers_letter:
        indices = [i.start() for i in re.finditer(number, line)]
        if indices:
            for id in indices:
                temp_dic[id] = number        

    first_number = temp_dic[min(temp_dic)]
    if first_number not in numbers:
        first_number = str(numbers_letter.index(first_number)+1)
    
    second_number = temp_dic[max(temp_dic)]
    if second_number not in numbers:
        second_number = str(numbers_letter.index(second_number)+1)
    
    result.append(int(first_number + second_number))

print(sum(result))