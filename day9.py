def prep_data(file):
    lines = [line.split() for line in file]
    for line in lines:
        for i in range(len(line)):
            line[i] = int(line[i])
    return lines

def find_difference(line):
    result_dif = list()
    for i in range(1, len(line)):
        result_dif.append(line[i] - line[i - 1])
    if len(set(result_dif)) == 1:
        return line[-1] + result_dif[0]
    else:
        result = find_difference(result_dif)
        return line[-1] + result

def find_all_values(lines):
    result = 0
    for line in lines:
        result += find_difference(line)
    return result
