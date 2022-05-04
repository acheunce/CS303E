# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours
    
    def getName(self):
        """Returns the name of this course"""
        return self.__name
    
    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor
    
    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours
    
    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        # replace pass with your __init__ implementation here
        self.__name = name
        self.__year = year
        self.__major = major
        self.__courses = courses

    def numCourses(self):
        # replace pass with your numCourses implementation here
        return len(self.__courses)

    def isUpperClassman(self):
        # replace pass with your isUpperClassman implementation here
        return self.__year > 2

    def totalHours(self):
        # replace pass with your totalHours implementation here
        hours = 0
        for course in self.__courses:
            hours += course.getHours()
        return hours
        pass

    def __str__(self):
        # replace pass with your __str__ implementation here
        yearName = ""
        if self.__year == 1:
            yearName = "freshman"
        elif self.__year == 2:
            yearName = "sophomore"
        elif self.__year == 3:
            yearName = "junior"
        elif self.__year == 4:
            yearName = "senior"
        return self.__name + " is a " + yearName + " " + self.__major + " major."


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    # replace pass with your solution to problem 2 here
    string = ""
    for num in lst:
        string += chr(num)
    return string

# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    # replace pass with your solution to problem 3 here
    sentence = sentence + " "
    count = 0
    sentence_list = []
    starting_index = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            sentence_list += [sentence[starting_index:i]]
            starting_index = i + 1
        
    for word in sentence_list:
        if word.lower() not in words:
            count += len(word)
    return count


# Problem 4 - Dueling Tanks
def duelingTanks(grid):
    # replace pass with your solution to problem 4 here
    duels = 0
    for col in range(len(grid)):
        tanks = 0
        for space in range(len(grid[0])):
            if grid[col][space] == "T":
                tanks += 1
        if tanks != 0:
            duels += tanks - 1

    for row in range(len(grid[0])):
        tanks = 0
        for space in range(len(grid)):
            if grid[space][row] == "T":
                tanks += 1
        if tanks != 0:
            duels += tanks - 1
    return duels

# Problem 5 - Even Elements Dictionary
def evenElementsDict(tups):
    # replace pass with your solution to problem 5 here
    
    evens = {}
    for tup in tups:
        even = 0
        for num in tup:
            if num % 2 == 0:
                even += 1
        evens[tup] = even
    return evens


# Problem 6 - Set of Common Factors
def setOfCommonFactors(lst):
    # replace pass with your solution to problem 6 here
    top = max(lst)
    factors = set()
    for i in range(1, top + 1):
        isFactor = True
        for num in lst:
            if num % i != 0:
                isFactor = False
        if isFactor:
            factors.add(i)
    return factors
    pass


# Problem 7 - Recursive Character Last Index Dictionary
def characterLastIndexDictionary(string, index):
    # replace pass with your solution to problem 7 here
    if len(string) == index:
        return {}
    else:
        d = characterLastIndexDictionary(string, index + 1)
        ch = string[index]
        if ch in d:
            pass
        else:
            d[ch] = index
        return d
    pass


# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst) :
    # replace pass with your solution to problem 8 here
    if lst == []:
        return (0, 0)
    else:
        count3 = 0
        count5 = 0
        if lst[0] % 5 == 0:
            count5 = 1
        if lst[0] % 3 == 0:
            count3 = 1
        
        return (divBy3And5(lst[1:])[0] + count3, divBy3And5(lst[1:])[1] + count5)



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    
    # print(duelingTanks([['T', '.', '.', 'T', '.', 'T'], ['T', 'T', '.', '.', '.', '.'], \
    #     ['.', '.', 'T', 'T', '.', 'T'], ['.', 'T', '.', '.', '.', '.'], ['T', '.', '.', 'T', '.', '.']]))
    # print(duelingTanks([['T', '.', 'T'], ['.', 'T', '.'], ['T', '.', 'T']]))
    # print(duelingTanks([['.', '.', 'T', '.'], ['T', '.', '.', '.'], ['.', '.', '.', 'T'], ['.', 'T', '.', '.']]))

    # print(evenElementsDict({(1, 2, 3, 4, 5), (2, 222, 2), (17,)}))
    # print(evenElementsDict(set()))
    # print(evenElementsDict({(0,), (1, 3, 5, 7, 9), (3, 1, 4, 1, 5, 9), (98, 76, 54, 32, 10)}))

    # print(setOfCommonFactors([50, 100]))
    # print(setOfCommonFactors([18]))
    # print(setOfCommonFactors([210, 770, 2730, 1015]))

    print(characterLastIndexDictionary('Hello World!', 0))
    print(characterLastIndexDictionary('', 0))
    print(characterLastIndexDictionary('CS303E is fun CS303E is fun CS303E is fun', 0))

    # print(divBy3And5([15, 9, 7, 5, 3]))
    # print(divBy3And5([]))
    # print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass