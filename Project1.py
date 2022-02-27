# File: Project1.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
#
# Date: 02/21/2022
# Description of Program: Converts from metric to english and english to metric

def intro():
    print("Welcome to the English/Metric conversion utility.\n")
    print("This utility allows you to convert between English units")
    print("(miles, feet, inches) and metric units (kilometers, meters,")
    print("centimeters).")

footToMeter = 0.3048
miletoFeet = 5280
inchToFeet = 1/12
kmToM = 1000
cmtoM = 1/100
value = 0
loop = True

def barrier():
    print()
    print("-"*60)
    print()
    
def ErrorMessage():
    print("\nERORR: Answer must be 1, 2, or 3. Try again.\n")

def q1():
    while(True):
        print("Which direction would you like to convert: ")
        print("\tFor English to Metric type: 1")
        print("\tFor Metric to English type: 2")
        print("\tTo Quit type:\t\t    3\n")
        direction = eval(input("Input your answer (1, 2, or 3): "))
        print()
        if type(direction) != int:
            ErrorMessage()
        else:
            if direction == 3:
                print("Thanks for using our converter. Goodbye!")
                return direction
            elif direction <= 2 and direction > 0:
                return direction
            else:
                ErrorMessage()

def q2(direction):
    unitName1 = ""
    if direction == 1:
        while(True):
            print("Select English units to convert to metric equivalent: ")
            print("\tFor miles type:    1")
            print("\tFor feet type:     2")
            print("\tFor inches type:   3\n")
            unitConvert = eval(input("Choose English units to convert (1, 2, or 3): "))
            print()
            print(type(unitConvert))
            if type(unitConvert) != int:
                ErrorMessage()
            else:
                if unitConvert == 1:
                    unitName1 == "miles"
                elif unitConvert == 2:
                    unitName1 == "feet"
                elif unitConvert == 3:
                    unitName1 == "inches"
                print(unitName1)
                if unitName1 != "":
                    return direction, unitConvert, unitName1
                else:
                    ErrorMessage()
    elif direction == 2:
        while(True):
            print("Select metric units to convert to English equivalent: ")
            print("\tFor kilometers type:    1")
            print("\tFor meters type:        2") 
            print("\tFor centimeters type:   3\n")
            unitConvert = eval(input("Choose metric units to convert (1, 2, or 3): "))
            print()
            if type(unitConvert) != int:
                ErrorMessage()
            else:
                if unitConvert == 1:
                    unitName1 == "kilometers"
                elif unitConvert == 2:
                    unitName1 == "meters"
                elif unitConvert == 3:
                    unitName1 == "centimeters"
                if unitName1 != "":
                    return direction, unitConvert, unitName1
                else:
                    ErrorMessage()
    else:
        return 0, 0, 0

def q3(direction, unitConvert, unitName1):
    unitName2 = ""
    if direction == 2:
        while(True):
            print("Convert to which English units: ")
            print("\tFor miles type:    1")
            print("\tFor feet type:     2")
            print("\tFor inches type:   3\n")
            unitTarget = eval(input("Choose target metric units (1, 2, or 3): "))
            print()
            if type(unitTarget) != int:
                ErrorMessage()
            else:
                if unitTarget == 1:
                    unitName2 == "miles"
                elif unitTarget == 2:
                    unitName2 == "feet"
                elif unitTarget == 3:
                    unitName2 == "inches"
                if unitName2 != "":
                    return direction, unitConvert, unitTarget, unitName1, unitName2
                else:
                    ErrorMessage()
    elif direction == 1:
        while(True):
            print("Convert to which metric units: ")
            print("\tFor kilometers type:    1")
            print("\tFor meters type:        2")
            print("\tFor centimeters type:   3\n")
            unitTarget = input("Choose target English units (1, 2, or 3): ")
            print()
            if type(unitTarget) != int:
                ErrorMessage()
            else:
                if unitTarget == 1:
                    unitName2 == "kilometers"
                elif unitTarget == 2:
                    unitName2 == "meters"
                elif unitTarget == 3:
                    unitName2 == "centimeters"
                if unitName2 != "":
                    return direction, unitConvert, unitTarget, unitName1, unitName2
                else:
                    ErrorMessage()

def Conversion(direction, unitConvert, unitTarget, unitName1, unitName2):
    value = eval(input("Enter the number of " + unitName1 + " to convert to " + unitName2 + ": "))
    if direction == 2:
        #intialUnit = "meters"
        #finalUnit = "feet"
        if unitConvert == 1:
            finalValue = (value*1000)*3.28084
            #initialUnit = "kilometers"
            if unitTarget == 1:
                finalValue = finalValue/5280
            #    finalUnit = "miles"
            elif unitTarget == 3:
                finalValue = finalValue/12
             #   finalUnit = "inches"
        elif unitConvert == 3:
            finalValue = (value/1000)*3.28084
            #initialUnit = "centimeters"
            if unitTarget == 1:
                finalValue = finalValue/5280
                #final_unit = "miles"
            elif unitTarget == 3:
                finalValue = finalValue*12
                #finalUnit = "inches"
    elif direction == 1:
        #initialUnits = "feet"
        #finalUnits = "meters"
        if unitConvert == 1:
            finalValue = (value*5280)*0.3048
            #intialUnit = "miles"
            if unitTarget == 1:
                finalValue = finalValue/1000
                #finalUnits = "kilometers"
            elif unitTarget == 3:
                finalValue = finalValue*1000
                #finalUnit = "centimeters"
        elif unitConvert == 3:
            finalValue = (value/12)*0.3048
            #initialUnit = "inches"
            if unitTarget == 1:
                finalValue = finalValue/1000
                #final_unit = "kilometers"
            elif unitTarget == 3:
                finalValue = finalValue*1000
                #finalUnit = "centimeters"
                
    print("RESULT: " + str(value) + " " +unitName1 + " = " + format(finalValue, "1.3f") + " " + unitName2)
        
intro()
while loop:
    barrier()
    a1, a2, a3 = q2(q1())
    if a1 == 0 and a2 == 0:
        loop = False
    else:
        b1, b2, b3, b4 = q3(a1, a2, a3)
        Conversion(b1, b2, b3, b4)
