# File: WordleAssistant.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date:04/10/2022
# Description of Program: Functions for a future wordle game

def createWordlist(filename): 
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


def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.  
    """
    newWordlist = []
    for word in wordlist:
        if include in word:
            newWordlist.append(word)
    return set(newWordlist)


def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.  
    """
    newWordlist = []
    for word in wordlist:
        contain = False
        for char in exclude:
            if char in word:
                contain = True
        if not contain:
            newWordlist.append(word)
    return set(newWordlist)

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    newWordlist = []
    keys = posInfo.keys()
    for i in range(len(wordlist)):
        print(keys[i])
        if (wordlist[i], i) == (posInfo[i],posInfo[posInfo[i]]):
            newWordlist.append(word)
    return set(newWordlist)

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    s1 = containsAtPositions(wordlist, posInfo)
    s2 = containsAll(wordlist, include)
    s3 = containsNone(wordlist, exclue)

    s12 = s1.intersection(s2)
    return s12.intersection(s3)


wordlist, count = createWordlist( 'wordlist.txt' )
for i in range(10):
    print(wordlist[i], end = " ")
print()

setABC = containsAll(wordlist, 'abc')
print(setABC)

someWords = containsNone( wordlist, 'abcdefghijklmn' ) 
print(someWords)

someMoreWords = containsNone( wordlist, 'abcdefghijklmnopqrstuvw' )
print(someMoreWords)

posDict = {'a':0, 'y':4}
posWords = containsAtPositions( wordlist, posDict )
print(posWords)