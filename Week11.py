# Week 11 Notes

print("abc\ndef")
print(r"abc\ndef") # raw, prints string without backslash. Useful for directories in windows where :C\users\etc..


# fileVariable = open(filename, mode)
# Modes:
# r: open for reading
# w: open for writing-overwrite old contents
# a: oepn for appending data to end of file
# rb: open for reading binary data
# wb: open for writing binary data

# fileVariable.close()

# import os.path
# os.path.isfile("") returns boolean


# Tuples are immutable, faster access than lists
tuple() # tuples
t1 = ()
print(t1)

t2 = tuple([1, 2, 3]) # 3-tuple from list
print(t2)
t3 = tuple([1]) # 1-tuples are not useful and have weird syntax
print(t3)

# Functions for sets, lists, tuples
# x in t1
# t1 + t2
# min(t)
# max(t)
# sum(t)

# Lists and tuple functions only
# t * n
# t[i]
# t[i:j]
# <=, >=, ==, != (for sets, these measure subsets and supersets)

# tuple to list to tuple
t3 = (0, 1, 2, 3, 4)
lst = list( t3)
import random
lst2 = random.shuffle(lst) # common error, shuffle does not return a list, but shuffles in place
print(lst2)

random.shuffle(lst)
print(tuple(lst))

# Sets are not ordered, and no duplicate elements
s1 = set()
print(s1)
print(s1 is {}) # sets and dictionaries are distinct
s2 = set([1, 2, 2, 4, 3])
print(s2)

print({'d', 'a', 'c', 'b'} == {'a', 'b', 'c', 'd'}) #  order doesnt matter

s1 = {1, 2, 3}
s2 = {1, 3, 5, 7}
s1.union(s2) # or s1 | s2, creates new set
s1.intersection(s2) # s1 & s2
s1.difference(s2) # not in both
s1.symmetric_difference(s2) # 1 and the other but not both

# Dictionaries: key/value pairs
squares = {2 : 4, 3 : 9, 4 : 16, 5 : 25}
# dictionaryName[key] = value (add)
# dictionaryName[key] (retrieve)
# del dictionaryName[key] (delete)

# Methods of class dict
# d.keys()    returns tuple of keys
# d.values()  returns tuple of values
# d.items()   returns tuple of key/value
# d.get(key)  same as d[key]
# d.clear()   deletes all items in d
# d.pop(key)  removes itme with the key and returns the value
# d.popitem   removes random item and returns pair

print(0<=None)