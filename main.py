import day8

file = open("input.txt", 'r')
# file = open("input_test.txt", 'r')
# file = open("input_test_2.txt", 'r')
# file = open("input_test_3.txt", 'r')

starting_node = 'AAA'
left_right, commands, nodes, A_nodes = day8.create_data(file)

# result = day8.find_zzz(nodes, commands, starting_node, left_right)
result = day8.find_xxz_v2(nodes, commands, A_nodes, left_right)

print(result)