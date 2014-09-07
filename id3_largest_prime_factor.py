__author__ = 'James W. Kimani'

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def largestprimeFactor(number):
    primes = []
    for num in range(2,number):
        if number%num == 0:
            if isPrime(num) == 'true':
                primes.append(num)
                print(num)

def isPrime(n):
    prime = 'true'
    for a in range(2,n):
        if n%a == 0:
            prime = 'false'
    return prime

largestprimeFactor(600851475143)




