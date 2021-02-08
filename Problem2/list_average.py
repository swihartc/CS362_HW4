import unittest

def list_average(li):
    
    total = 0
    count = 0
    
    if li == []:
        return None

    for i in li:
        if (type(i) != int and type(i) != float):
            return None
        total += i
        count += 1

    try:
       return total / i
    except ZeroDivisionError:
        return None

        

class Test_list_average(unittest.TestCase):
    def test_valid_list(self):
        actual = list_average([1,2,3,4,5,6,7,8])
        expected = 4.5
        self.assertEqual(actual,expected)

    def test_invalid_list(self):
        actual = list_average([1,2,3,4,"WHAT??",6,7,8])
        expected = None
        self.assertEqual(actual,expected)

    def test_empty_list(self):
        actual = list_average([])
        expected = None
        self.assertEqual(actual,expected)
    
    def test_list_full_zero(self):
        actual = list_average([0,0,0,0,0,0])
        expected = None
        self.assertEqual(actual,expected)