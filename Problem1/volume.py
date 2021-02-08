import unittest

def volume(x,y,z):
    if type(x) != int and type(x) != float:
        return None
    if type(y) != int and type(y) != float:
        return None
    if type(z) != int and type(z) != float:
        return None
    
    if x < 0 or y < 0 or z < 0: return None
    return x * y * z
    
class TestVolume(unittest.TestCase):
    def test_volume_success(self):
        actual = volume(3,3,5)
        expected = 45
        self.assertEqual(actual, expected)

    def test_negative(self):
        actual = volume(-1,3,3)
        expected = None
        self.assertEqual(actual,expected)
        actual = volume(-1,-1,3)
        expected = None
        self.assertEqual(actual,expected)

    def test_type_error(self):
        actual = volume(3,"String",[])
        expected = None
        self.assertEqual(actual, expected)



