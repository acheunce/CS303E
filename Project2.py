# File: Project2.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 03/30/2022
# Description of Program: Given input integer N, the program generates a list of N Fibonnaci numbers


commands = ["0", "1", "2", "3", "4", "5", "6"]
error0 = ("ERROR: Illegal command. Try again\n")
error1 = ("ERROR: Answer must be 1, 2 or 3. Try again.\n")
error2 = ("ERROR: Illegal value entered\n")


def errorQuestion(val, lowerBound, upperBound, error): # inspired from ControlGameDriver by Sam
    while True: 
        answer = input(val).strip()
        if answer.isdigit():
            command = int(answer)
            if lowerBound == None and upperBound == None:
                break
            elif lowerBound == None:
                if command > upperBound:
                    print(error)
                else:
                    break
            elif upperBound == None:
                if command < lowerBound:
                    print(error)
                else:
                    break
            else:
                if command < lowerBound or command > upperBound:
                    print(error)
                else:
                    break
        else:
            print(error)
    return command





def firstNFibNumbers(n):
    """ Return a list of the first n Fibonnaci numbers.  If 
        n < 0, return the empty list. """
    
    if n == 0:
        return []

    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]

    # Here we know that n is at least 2.
    else:

        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1

        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]

        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):

            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2

            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )

        return fibs

def iFibNumber(i):
    fib1 = 0
    fib2 = 1
    if i < 0:
        errorMessage()
    else:
        for j in range(i):
            fib1, fib2 = fib2, fib1 + fib2
        return fib1

def lessThanFib(N):
    
    fib1, fib2 = 0, 1
    fibs = []
    
    while N >= fib1:
        fibs.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2

    return fibs

def lessThanEqFib(N):
    return len(lessThanFib(N))

def sumToFib(N):
    fibs = []
    sumFibs = []
    subtract = N
    if N < 0:
        errorMessage()
    else:
        fibs = lessThanFib(N)
        sumFibs.append(fibs[len(fibs) - 1])
        subtract -= fibs[len(fibs) - 1]
        for i in range(len(fibs) - 1, 0 , -1):
            print(fibs[i])
            if subtract - fibs[i] >= 0:
                sumFibs.append(fibs[i])
                subtract -= fibs[i]
            elif subtract == 0:
                break
        return sumFibs
            
loop = True
print("Welcome to the Fibonnaci Number laboratory!\n")
print("The following commands are available:")
print("  0: Exit.")
print("  1: List the first N Fibonnaci numbers.")
print("  2: Display the ith Fibonnaci number (0-based).")
print("  3: List the Fibonnaci numbers less or equal to N.")
print("  4: How many Fibonnaci numbers are less or equal to N?")
print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
print("  6: Display this help message. \n")
while loop:    
    num = errorQuestion("Please enter a command (0, 1, 2, 3, 4, 5 or 6): ", 0, 6, error0)

    if num == 0:
        print("\nThanks for using the Fibonnaci Labratory! Goodybe.")
        loop = False
    elif num == 1:
        firstNFibNumbers(errorQuestion("You've asked for the first N Fibonnaci numbers. What is N? ", 0, None, error2))
    elif num == 2:
        n = input("You've asked for the ith Fibonnaci number. What is i? ")
        iFibNumber(errorQuestion(n, 0, None, error2))
    elif num == 3:
        n = input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? ")
        lessThanFib(errorQuestion(n, None, None, error2))
    elif num == 4:
        n = input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? ")
        lessThanEqFib(errorQuestion(n, None, None, error2))
    elif num == 5:
        n = input("You've asked for Fibonnaci numbers that sum to N. What is N? ")
        sumToFib(errorQuestion(n, 0, None, error2))
    elif num == 6:
        userInput(intro())