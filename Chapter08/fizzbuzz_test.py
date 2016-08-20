import unittest

def fizzbuzz(a):
    if a % 15 == 0:
        return 'FizzBuzz'
    elif a % 3 == 0:
        return 'Fizz'
    elif a % 5 == 0:
        return 'Buzz'
    else:
        return a

class FizzBuzzTest(unittest.TestCase):
    def test_fizbuzz(self):
        self.assertEqual('Fizz',     fizzbuzz(3))
        self.assertEqual('Buzz',     fizzbuzz(5))
        self.assertEqual('FizzBuzz', fizzbuzz(15))
        self.assertEqual(16,         fizzbuzz(16))

if __name__ == '__main__':
    unittest.main()

