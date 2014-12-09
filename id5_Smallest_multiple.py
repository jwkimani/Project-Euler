__author__ = 'James W. Kimani'
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
#print 2520
#print(2**3 * 3**2 * 5 * 7)

result = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

print("The smallest positive number that is evently divisble by all of the numbers from 1 to 20 is %i" % (result))

message = """The smallest number divisible by all numbers from 1 to 20 must be divisible by all prime powers
occuring among these numbers. And, on the other hand, if we have a number divisible by all prime powers in this range,
it will be divisble by all numbers from 1 to 20."""

print("\n   %s \n%s" %("NOTE!!!", message))
