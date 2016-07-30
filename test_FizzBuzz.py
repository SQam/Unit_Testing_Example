import FizzBuzz
import unittest

class test_fizzbuzz(unittest.TestCase):
   #tests for multiples of 3 that should return Fizz
   def test_3_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(3), 'Fizz')
   def test_6_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(6), 'Fizz')
   def test_9_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(9), 'Fizz')
  
   #tests for multiples of 5 that should return Buzz
   def test_5_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(5), 'Buzz')
   def test_10_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(10), 'Buzz')
   def test_20_returns_Fizz(self):
      self.assertEqual(FizzBuzz.fizzbuzz(20), 'Buzz')

  #tests for multiples of 3 and 5 that should return FizzBuzz
   def test_15_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(15), 'FizzBuzz')
   def test_30_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(30), 'FizzBuzz')
   def test_45_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(45), 'FizzBuzz')

   """tests for numbers that are not multiples of either and 
    should return as numbers""" 
   def test_1_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(1), 1)
   def test_2_returns_FizzBuzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(2), 2)
   def test_if_1_returns_Buzz(self):
       self.assertEqual(FizzBuzz.fizzbuzz(7), 7)
   

if __name__ == '__main__':
    unittest.main()
    