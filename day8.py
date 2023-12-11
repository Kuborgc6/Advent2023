import copy
import math

def create_data(file):
    lines = [line.split() for line in file]

    left_right = {"L": 0, 'R': 1}

    nodes = dict()
    # only_nodes = list()
    A_nodes = list()

    commands = list(lines[0][0])

    lines = lines[2:]

    for line in lines:
        nodes[line[0]] = [line[2][1:-1],line[-1][:-1]]
        if(line[0][-1] == 'A'):
            A_nodes.append(line[0])
            
    return left_right, commands , nodes, A_nodes


def find_zzz(nodes, commands, starting_node, left_right):
    current_node = copy.deepcopy(starting_node)
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


# print(find_zzz(nodes, commands, starting_node))

### PART TWO

def find_xxz(nodes, commands, starting_nodes, left_right):
    current_nodes = copy.deepcopy(starting_nodes)
    i = 0
    result = 0
    while (not if_ends_Z(current_nodes)):
        if i == len(commands):
            i = 0
        direction = left_right[commands[i]]
        for j in range(len(current_nodes)):
            current_nodes[j] = nodes[current_nodes[j]][direction]
        i += 1
        result += 1
        if (current_nodes == starting_nodes):
            result = "doesn't work"
            break
    return result

def if_ends_Z(current_nodes):
    result = True
    for node in current_nodes:
        if node[-1] != 'Z':
            result = False
    return result

def find_xxz_one_node(nodes, commands, starting_node, left_right):
    current_node = copy.deepcopy(starting_node)
    i = 0
    result = 0
    while (current_node[-1] != 'Z'):
        if i == len(commands):
            i = 0
        direction = left_right[commands[i]]
        current_node = nodes[current_node][direction]
        i += 1
        result += 1
    return result


def find_xxz_v2(nodes, commands, starting_nodes, left_right):
    results = list()
    for node in starting_nodes:
        results.append(find_xxz_one_node(nodes, commands, node, left_right))
    result = math.lcm(*results) 
    return result