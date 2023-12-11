import unittest   # The test framework
import day8

starting_node = 'AAA'

file_1 = open("input_test.txt", 'r')
left_right, commands_1, nodes_1, A_nodes_1 = day8.create_data(file_1)

file_2 = open("input_test_2.txt", 'r')
left_right, commands_2, nodes_2, A_nodes_2 = day8.create_data(file_2)

file_3 = open("input_test_3.txt", 'r')
left_right, commands_3, nodes_3, A_nodes_3 = day8.create_data(file_3)

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_first(self):
        self.assertEqual(day8.find_zzz(nodes_1, commands_1, starting_node, left_right), 2)

    def test_second(self):
        self.assertEqual(day8.find_zzz(nodes_2, commands_2, starting_node, left_right), 6)
    
    def test_third(self):
        self.assertEqual(day8.find_xxz(nodes_3, commands_3, A_nodes_3, left_right), 6)
    
    def test_third_v2(self):
        self.assertEqual(day8.find_xxz_v2(nodes_3, commands_3, A_nodes_3, left_right), 6)

if __name__ == '__main__':
    unittest.main()