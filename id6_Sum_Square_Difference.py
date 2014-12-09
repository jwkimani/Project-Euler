__author__ = 'James W. Kimani'

import math
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def sum_square_difference():
    sum_of_numbers, sum_of_squares, square_of_sum = 0, 0, 0
    for a in range(1,101):
        sum_of_squares += a*a
        sum_of_numbers += a
        square_of_sum = sum_of_numbers *sum_of_numbers
    difference = square_of_sum - sum_of_squares
    print("The sum of the squares of the first one hundred natural numbers is: %i"%(sum_of_squares))
    print("The square of the sum of the first one hundred natural numbers is: %i*%i = %i"% (sum_of_numbers, sum_of_numbers, square_of_sum))
    print("The difference between the sum of the square of the first one hundred natural numbers and the square of the"
          " sum is: %i - %i = %i"%(square_of_sum, sum_of_squares,difference))

sum_square_difference()
#The difference between the sum of the square of the first one hundred natural numbers and the square of the sum is: 25502500 - 338350 = 25164150

