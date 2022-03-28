# File: FindPrimeFactors.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 03/14/2022
# Description of Program: 

def isPrime():
    pass

def prime():
#     if num is prime:
#    return a list containing only num

# otherwise num is composite:
#    set the list of factors to the empty list
#    set d to 2
#    as long as num is greater than 1 do the following:
#       check if d divides num
#          if it does, add d to the end of the list of factors
#             and divide num by d
#          keep checking d until it doesn't divide num
#       set d to the next biggest prime
#    at this point num is 1 and the list of factors is the prime factorization
#    return the list of factors
def findNextPrime():
    pass


print("Find Prime Factors:")

num = -1

while num != 0:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 1:
        print("  1 has not prime factorization\n")
    elif num < 0:
        print("  Negative integer entered. Try again. \n")
    else:
        print("  The prime factorization of " + str(num) + " is " + )
print("Goodbye!")

