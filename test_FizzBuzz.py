import FizzBuzz
import unittest

class test_fizzbuzz(unittest.TestCase):
   def test_3_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(3), 'Fizz')
   def test_5_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(5), 'Buzz')
   def test_15_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(15), 'FizzBuzz')
   def test_1_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(1), 1)
   def test_2_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(2), 2)
   def test_6_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(6), 'Fizz')
   def test_10_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(10), 'Buzz')
   def test_30_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(30), 'FizzBuzz')
   def test_if_1_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(7), 7)
   def test_if_2_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(8), 8)
if __name__ == '__main__':
    unittest.main()