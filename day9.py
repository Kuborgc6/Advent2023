def prep_data(file):
    lines = [line.split() for line in file]
    for line in lines:
        for i in range(len(line)):
            line[i] = int(line[i])
    return lines

def find_next_value(line):
    result_dif = list()
    for i in range(1, len(line)):
        result_dif.append(line[i] - line[i - 1])
    if len(set(result_dif)) == 1:
        return line[-1] + result_dif[0]
    else:
        result = find_next_value(result_dif)
        return line[-1] + result

def find_all_next_values(lines):
    result = 0
    for line in lines:
        result += find_next_value(line)
    return result

def find_previous_value(line):
    result_dif = list()
    for i in range(1, len(line)):
        result_dif.append(line[i] - line[i - 1])
    if len(set(result_dif)) == 1:
        return line[0] - result_dif[0]
    else:
        result = find_previous_value(result_dif)
        return line[0] - result
    
def find_all_previous_values(lines):
    result = 0
    for line in lines:
        result += find_previous_value(line)
    return result