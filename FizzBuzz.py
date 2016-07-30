"""A program that prints the numbers from 1 to 100.
For multiples of 3 prints "Fizz", for multiples of 5, prints "Buzz", for
multiples of both 3 and 5, prints "FizzBuzz" else prints the number. """



"""function that generates output for a number and returns it. This function 
is called in the output loop for numbers 1 to 100 as well as the test cases""" 
def fizzbuzz(number):
    if number%3==0 and number%5==0:
         return 'FizzBuzz'
    elif number%3 == 0:
        return 'Fizz'
    elif number%5==0:
         return 'Buzz'
    else:
         return number
       
# prints resulting output for numbers from 1 to 100, on main
if __name__ == '__main__':
    print ('Output:')
    for number in range(1, 101):
        print (fizzbuzz(number))


    