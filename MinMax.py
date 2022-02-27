# File: MinMax.py
# Student: Aaron Cheung
# UT EID: ac77373
# COurse Name: CS303E
#
# Date: 02/14/2022
# Description of Program: Continuous code that takes in user input integers
#   and returns the minumum and the maximum out of the given integers

run = input("Enter an integer or 'stop' to end: ")
min1 = 0
max1 = 0
num = 0

while(run != "stop"):
    num = int(run)
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num
    run = input("Enter an integer or 'stop' to end: ")
    
print("The maximum is " + str(max1))
print("The minimum is " + str(min1))
