# File: Student.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 03/02/2022
# Description of Program: A student class with functions that can set the two exam grades, and retrieve the name and the grades.

class Student():
    def __init__(self, name, grade1 = None, grade2 = None):
        self.__name = name
        self.__grade1 = grade1
        self.__grade2 = grade2
    
    def __str__(self):
        return "Student: " + str(self.__name) + "\n   Exam 1: " + str(self.__grade1) + "\n   Exam 2: " + str(self.__grade2)

    def getName(self):
        print(self.__name)

    def getExam1Grade(self):
        print(str(self.__grade1))

    def getExam1Grade(self):
        print(str(self.__grade2))
    
    def setExam1Grade(self, grade1):
        self.__grade1 = grade1
    
    def setExam2Grade(self, grade2):
        self.__grade2 = grade2

    def getAverage(self):
        if self.__grade1 == None or self.grade2 == None:
            print("Some exam grades are not available")
        else:
            print(str((self.__grade1+self.__dict____grade2)/2))


from Student import *
susie = Student("Susie Q.")
#print(susie)
#susie.getName()
#susie.getExam1Grade()
susie.setExam1Grade(100)
#print(susie)
susie.getExam1Grade()