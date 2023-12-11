import unittest   # The test framework
import day9


file_1 = open("input_test.txt", 'r')
lines = day9.prep_data(file_1)


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_first(self):
        self.assertEqual(day9.find_next_value(lines[0]), 18)

    def test_second(self):
        self.assertEqual(day9.find_next_value(lines[1]), 28)
    
    def test_third(self):
        self.assertEqual(day9.find_next_value(lines[2]), 68)
    
    def test_4(self):
        self.assertEqual(day9.find_previous_value(lines[0]), -3)

    def test_5(self):
        self.assertEqual(day9.find_previous_value(lines[1]), 0)
    
    def test_6(self):
        self.assertEqual(day9.find_previous_value(lines[2]), 5)
    # def test_third_v2(self):
    #     self.assertEqual(, 6)

if __name__ == '__main__':
    unittest.main()