file = open("input.txt", 'r')
# file = open("input_test.txt", 'r')

lines = [line.split() for line in file]

left_right = {"L": 0, 'R': 1}

nodes = dict()

commands = list(lines[0][0])

lines = lines[2:]

for line in lines:
    nodes[line[0]] = [line[2][1:-1],line[-1][:-1]]

def find_zzz(nodes, commands):
    current_node = 'AAA'
    i = 0
    result = 0
    while (current_node != 'ZZZ'):
        if i == len(commands):
            i = 0
        direction = left_right[commands[i]]
        current_node = nodes[current_node][direction]
        i += 1
        result += 1
    return result

print(find_zzz(nodes, commands))