import day9

file = open("input.txt", 'r')
# file = open("input_test.txt", 'r')
# file = open("input_test_2.txt", 'r')
# file = open("input_test_3.txt", 'r')

lines = day9.prep_data(file)

# result = day8.find_zzz(nodes, commands, starting_node, left_right)
result = day9.find_all_next_values(lines)
print(result)

result = day9.find_all_previous_values(lines)
print(result)