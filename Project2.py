# File: Project2.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 03/30/2022
# Description of Program: Given input integer N, the program generates a list of N Fibonnaci numbers

def ErrorMessage():
    print("ERROR: Answer must be 1, 2 or 3. Try again.\n")

def intro():
    print("Welcome to the Fibonnaci Number laboratory!\n")
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: List the first N Fibonnaci numbers.")
    print("  2: Display the ith Fibonnaci number (0-based).")
    print("  3: List the Fibonnaci numbers less or equal to N.")
    print("  4: How many Fibonnaci numbers are less or equal to N?")
    print("  5: Find a list of the largest Fibonnaci numbers that add up to N.")
    print("  6: Display this help message. \n")
    
    while()
    num = (input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): "))
    if type(num) != int:
        ErrorMessage()
    return