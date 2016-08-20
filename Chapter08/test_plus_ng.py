import unittest

def plus(a, b):
    return a + b

class PlusTest(unittest.TestCase):
    def test_lus(self):
        self.assertEqual(10, plus(2, 8))
        self.assertEqual(20, plus(2, 8))

if __name__ == '__main__':
    unittest.main()
