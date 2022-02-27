# File: Payroll.py
# Student: Aaron Cheung
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 2/1/2022
# Description of Program: Program takes in several inputs including name,
#   hours worked, hourly pay, and federal and state tax rates and prints
#   the necessary deductions and Net Pay.


name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
pay_rate = eval(input("Enter hourly pay rate: "))
fed_tax = eval(input("Enter federal tax withholding rate: "))
state_tax = eval(input("Enter state tax withholding rate: "))
gross_pay = hours*pay_rate
fed_ded = fed_tax*gross_pay
state_ded = state_tax*gross_pay

print()
print("Employee Name: " + name)
print("Hours Worked: " + format(hours, "3.1f"))
print("Pay Rate: $" + format(pay_rate, "3.2f"))
print("Gross Pay $" + format(gross_pay, "3.2f"))
print("Deductions: ")
print("    Federal Withholding ("+format(100*fed_tax, "3.1f")+"%): $" + format(fed_ded, "3.2f"))
print("    State Witholding ("+format(100*state_tax,"3.1f")+"%): $" + format(state_ded, "3.2f"))
print("    Total Deduction: $" + format(state_ded+fed_ded, "3.2f"))
print("Net Pay: $" + format(gross_pay-(fed_ded+state_ded), "3.2f"))
