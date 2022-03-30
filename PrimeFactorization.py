# File: FindPrimeFactors.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 03/14/2022
# Description of Program: Takes in an integer from user and returns list
# of all prime factors

import math

def isPrime(num):
    if (num < 2 or num % 2 == 0):
        return (num == 2)
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findNextPrime(num):
    if num < 2:
        return 2
    else:
        guess = num + 1
        while not isPrime(guess):
            guess += 1
        return guess

def primeFactors(num):
    if isPrime(num):
        return [num]
    else:
        factors = []
        d = 2
        num1 = num
        while num1 > 1:
            while num1 % d == 0:
                factors += [d]
                num1 /= d
            d = findNextPrime(d)
        return factors


print("Find Prime Factors:")

num = -1

while num != 0:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 1:
        print("  1 has no prime factorization.\n")
    elif num < 0:
        print("  Negative integer entered.  Try again.\n")
    elif num == 0:
        print("Goodbye!")
    else:
        print("  The prime factorization of " + str(num) + " is:", primeFactors(num))
        print()