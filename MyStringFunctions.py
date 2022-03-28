# File: MyStringFunctions.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E

# Date: 03/14/2022
# Description of Program: 

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in str:
        if ch is i:
            count += 1
    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    
    min = 0
    num = 0

    for ch in str:
        num = ord(ch)
        if num <= min:
            min = num
    
    if min == 0:
        print("Empty string: no min value")
        return None
    else:
        return num


def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.

    newStr = ""
    if i >= len(str):
        print("Invalid index")
        return None
    else:
        for j in str:
            if j == str[i]:
                newStr += ch
            newStr += str[j]
        return newStr


def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    
    newStr = ""
    removed = ""
    if i >= len(str):
        print("Invalid index")
        return str, None
    else:
        for j in len(str):
            if j == i:
                removed = str[j]
            else:
                newStr += str[j]
        return newStr, removed


def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.

    for i in str:
        if i == ch:
            return i
        else:
            return -1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(-1,-(len(str) + 1),-1):
        if i == ch:
            return i
        else:
            return -1



def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.

    newStr = ""
    for i in str:
        pass

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.

    newStr = ""
    for i in range(str):
        if str[i] == ch:
            return str[:i] + str[i+1:]
    return str

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.

    newStr = ""
    for i in range(-1,-(len(str) + 1),-1):
        newStr = str[i]
    return newStr
