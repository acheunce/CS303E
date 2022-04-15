# File: RecursiveFunctions.py
# Student: Aaron Cheung 
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 04/14/2022
# Description of Program: Recursive functinos for lists, strings, etc.

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    # Add up the non-negative integers to n.
    # E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5.
    if n == 0:
        return 0
    else:
        return n + addToN(n - 1)


def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n % 10 == 0:
      return 0
   else:
       return n % 10 + findSumOfDigits(n // 10)


def integerToBinary( n ):
   """ Given a nonnegative decimal integer n, return the 
   binary representation as a string. """
   if n <= 1:
       return str(n % 2)
   else: 
       return integerToBinary(n // 2) + str(n % 2)


def integerToList( n ):
   """ Given a nonnegative decimal integer, return a list of the 
   digits (as strings). """
   digits = []
   if n % 10 == 0:
       return []
   else:
       return integerToList(n // 10) + [str(n % 10)] 


def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if s == "" or len(s) == 1:
       return True
   elif s[0] != s[len(s) - 1]:
       return False
   else:
       return isPalindrome(s[1:len(s)-1])

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any.  Return None if there
   is none. """
   if s == "":
       return None
   elif s[0].isupper():
       return s[0]
   else:
       return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the index of the first uppercase letter, 
   beginning at index.  Return -1 if there is none."""
   if s == "":
       return -1
   elif s[0].isupper():
       return index
   else:
       return findFirstUppercaseIndexHelper(s[1:], index + 1)


# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any.  Return -1 if there is none.  This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )

# print(addToN(10))
# print(addToN(100))
# print(addToN(0))

# print(findSumOfDigits(0))
# print(findSumOfDigits(12345))

# print(integerToBinary( 25 ))
# print(integerToBinary( 100 ))
# print(integerToBinary( 0 ))


# print(integerToList(123))
# print(integerToList(348961))
# print(integerToList(0))

# print(isPalindrome( "abcDcba" ))
# print(isPalindrome( "abcDcbaF" ))
# print(isPalindrome(""))
# print(isPalindrome("X"))

# print(findFirstUppercase( "ab c  dEFg hi" ))
# print(findFirstUppercase( "ab c  dffg hi" ))

# print(findFirstUppercaseIndex( "ab c  dEFg hi" ))
# print(findFirstUppercaseIndex( "ab c  defg hi" ))
# print(findFirstUppercaseIndex( "" ))