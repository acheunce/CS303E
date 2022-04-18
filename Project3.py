# File: Project3.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 04/16/2022
# Description of Program: Wordle Game

import os.path
from typing import ParamSpecArgs

def Welcome():
    
    print("""Welcome to WORDLE, the popular word game. The goal is to guess a
    five letter word chosen at random from our wordlist.  None of the
    words on the wordlist have any duplicate letters.
    
    You will be allowed 6 guesses.  Guesses must be from the allowed
    wordlist.  We'll tell you if they're not.
    
    Each letter in your guess will be marked as follows:
    
       x means that the letter does not appear in the answer
       ^ means that the letter is correct and in the correct location
       + means that the letter is correct, but in the wrong location
    
    Good luck!""")
    
    input("Enter the name of the file from which to extract the wordlist: ")

def CreateWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """
    file = open(filename, "r")
    wordlist = file.readlines() # returns ['string1', 'string2']
    index = 0
    newWordlist = []
    for word in wordlist:
        word1 = word.strip()
        if len(word1) == 5 and word1[len(word1) - 1] != 's':
            # wordlist.pop(index)
            duplicate = False
            for char in word1:
                if word1.count(char) > 1:
                    duplicate = True
            if not duplicate:
                newWordlist.append(word1)
    return newWordlist, len(newWordlist)

def BinarySearch(lst,key):
   low = 0
   high = len(lst) - 1
   while (high >= low):
      mid = (low + high) // 2
      if key < lst[mid]:
         high = mid - 1
      elif key == lst[mid]:
         return mid
      else:
         low = mid + 1
   return (-low - 1)

def WordSearch(wordlist, word):
    if BinarySearch(wordlist, ) > 0:
        

    pass


def GetFileName():
    while True:
        file = input("Enter the name of the file from which to extract the wordlist: ")
        if os.path.exists(file + ".txt"):
            return file
        else:
            print("File does not exist. Try again!")

def ChooseWord(newWordlist, length):
    pass

def Parse(word):
    feedback = ""
    for i in range(6):
        guess = input("Enter your guess " + "(" + str(i) + "): ")
        for i in range(len(guess)):
            print(guess[i].upper(), end = "  ")
            if guess[i].lower() == word[i].lower():
                feedback += "^  "
            else:
                feedback += "x  "
        print("\n " + feedback)
        if guess.lower() == word.lower():
            print("CONGRAULATIONS! You win!")
            break
    print("Sorry! The word was " + word + ". Better luck next time!")