__author__ = 'James W. Kimani'
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
            1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.
'''
def FibonacciSequence(number):
    if number <= 1:
        return number
    return FibonacciSequence(number - 1) + FibonacciSequence(number - 2)

def printFibonacciSequence(number):
    for a in range(1, number + 1):
        myNum = FibonacciSequence(a)
        print (myNum, end = ', ')

def findEvenFibonacci(number):
    for a in range(1, number + 1):
        myNum = FibonacciSequence(a)
        if myNum % 2 == 0:
            print(myNum, end = ", ")
findEvenFibonacci(10)