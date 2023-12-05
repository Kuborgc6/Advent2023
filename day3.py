file = open('input.txt', 'r')
# file = open('input_test.txt', 'r')

lines = [line.split()[0] for line in file]

layout = list()
for line in lines:
    layout.append(list(line))


def search_adjacent(layout, i, j, max_len_i, max_len_j, len_number):
    result = False

    k = i - 1 
    l = j
    while(k >= 0 and l >= 0 and l < (len_number + j + 1) and l < max_len_j ): # check +1 in len_number + i + 1
        if layout[k][l] != '.':
            result = True
            break
        # k -= 1
        # l -= 1
        l += 1

    l = j - 1
    if(l >= 0):
        if layout[i][l] != '.':
            result = True
        # l -= 1

    k = i + 1 
    l = j
    while(k <= max_len_i - 1 and l >= 0 and l < (len_number + j + 1) and l < max_len_j):
        if layout[k][l] != '.':
            result = True
            break
        # k += 1
        l += 1
    
    l = j + len_number
    if(l <= max_len_j - 1):
        if layout[i][l] != '.':
            result = True
        # l += 1

    k = i - 1 
    l = j - 1
    if(k >= 0 and l >= 0 and l < (len_number + j + 1) and l < max_len_j ): # check +1 in len_number + i + 1
        if layout[k][l] != '.':
            result = True
    
    k = i + 1 
    l = j - 1
    if(k >= 0 and l >= 0 and l < (len_number + j + 1) and l < max_len_j and k < max_len_i): # check +1 in len_number + i + 1
        if layout[k][l] != '.':
            result = True
        # k -= 1
        # l -= 1
        # l += 1


    return result

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

max_len_i = len(layout)
max_len_j = len(layout[0])
result = 0
temp_skip_j = 0
temp_skip_i = 0

for i in range(max_len_i):
    for j in range(max_len_j):
        if j < temp_skip_j and i == temp_skip_i:
            continue
        temp_skip_j = 0
        temp_skip_i = 0
        temp_nubmer = ''
        j_temp = j
        while(j_temp < max_len_j and layout[i][j_temp].isdigit()):
            temp_nubmer += layout[i][j_temp]
            j_temp += 1
        if temp_nubmer != '':
            len_number = len(temp_nubmer)
            if temp_nubmer == '664':
                print()
            result_temp = search_adjacent(layout, i, j, max_len_i, max_len_j, len_number)
            if result_temp:
                result += int(temp_nubmer)
            temp_skip_j = j + len_number
            temp_skip_i = i


print(result)

def search_adjacent_numbers(layout, i, j, max_len_i, max_len_j):
    numbers = list()
    j_start = list()    
    for i_prim in range(i-1,i+2):
        for j_prim in range(j-1, j+2):
            number_temp = ''
            if 0 <= i_prim < max_len_i and 0 <= j_prim < max_len_j and layout[i_prim][j_prim].isdigit():
                j_temp = j_prim
                while(0 <= j_temp < max_len_j and layout[i_prim][j_temp].isdigit()):
                    number_temp = layout[i_prim][j_temp] + number_temp
                    j_temp -= 1
                j_start_temp = j_prim - len(number_temp) + 1
                i_start_temp = i_prim
                j_temp = j_prim + 1
                while(0 <= j_temp < max_len_j and layout[i_prim][j_temp].isdigit()):
                    number_temp += layout[i_prim][j_temp]
                    j_temp += 1
                if [i_start_temp, j_start_temp] not in j_start:
                    j_start.append([i_start_temp, j_start_temp])
                    numbers.append(int(number_temp))
    return numbers

result = 0

for i in range(max_len_i):
    for j in range(max_len_j):
        if layout[i][j] == '*':
            numbers = search_adjacent_numbers(layout, i, j, max_len_i, max_len_j)
            if 910 in numbers:
                print('test') 
            if len(numbers) == 2:
                gear_ratio = numbers[0]*numbers[1]
                result += gear_ratio

print(result)