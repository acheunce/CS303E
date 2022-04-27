# File: Project3.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 04/16/2022
# Description of Program: Wordle Game

import os.path
import random

def Welcome():
    
    print("""\nWelcome to WORDLE, the popular word game. The goal is to guess a
five letter word chosen at random from our wordlist.  None of the
words on the wordlist have any duplicate letters.

You will be allowed 6 guesses.  Guesses must be from the allowed
wordlist.  We'll tell you if they're not.

Each letter in your guess will be marked as follows:

   x means that the letter does not appear in the answer
   ^ means that the letter is correct and in the correct location
   + means that the letter is correct, but in the wrong location

Good luck!\n""")
    
def wordOK(word):
    return len(word) == 5 and word[len(word) - 1] != 's'


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
    return newWordlist


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


def GetFileName():
    while True:
        file = input("Enter the name of the file from which to extract the wordlist: ")
        file = file + ".txt"
        if os.path.exists(file):
            print()
            return file
        else:
            print("File does not exist. Try again!")

def Parse(word, wordlist):
    if word in wordlist:
        wrong = True
        index = 0
        while index < 6: 
            feedback = ""
            word = word.lower()
            guess = input("Enter your guess " + "(" + str(index + 1) + "): ").lower()
            if BinarySearch(wordlist, guess) < 0:
                print("Guess must be a 5-letter word in the wordlist.  Try again!")
            else:
                for i in range(len(guess)):
                    print(guess[i].upper(), end = "  ")
                    if guess[i] in word:
                        if guess[i] == word[i]:
                            feedback += "^  "
                        else:
                            feedback += "+  "
                    else:
                        feedback += "x  "
                print("\n" + feedback)
                index += 1
            if guess == word:
                print("CONGRATULATIONS! You win!\n")
                wrong = False
                break
        if wrong:
            print("Sorry!  The word was " + word + ". Better luck next time!\n")
    else:
        print("Answer supplied is not legal.\n")

def PlayWordle(word=None):
    Welcome()
    wordlist = CreateWordlist(GetFileName())
    if word == None:
        word = random.choice(wordlist)
    Parse(word, wordlist)

PlayWordle()