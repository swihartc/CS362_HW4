import unittest

def full_name(first,last):
    if type(first) != str:
        return None
   
    if type(last) != str:
        return None
    
    if first == "" or last == "":
        return None
    return first + " " + last

class Test_full_name(unittest.TestCase):
    def test_valid_name(self):
        actual = full_name("Cyrus","Swihart")
        expected = "Cyrus Swihart"
        self.assertEqual(actual,expected)

    def test_invalid(self):
        actual = full_name(1,"Hello")
        expected = None
        self.assertEqual(actual,expected)

    def test_list_invalid(self):
        actual = full_name(["John"],["Doe"])
        expected = None
        self.assertEqual(actual,expected)
    
    def test_empty(self):
        actual = full_name("","Hello")
        expected = None
        self.assertEqual(actual,expected)
