'''Monthly Salary Calculation
Scenario:
A company pays an employee a fixed monthly salary and additional incentives based on performance.
Problem Statement:
Write a Python program to calculate the total monthly salary of an employee by adding the fixed salary
and incentive amount.
Input:
• Basic Salary
• Incentive
Output:
• Total Salary
'''
monthly_salary = float(input("Enter Basic Salary: "))
incentive = float(input("Enter Incentive: "))
#-------------Validating the inputs----------------
if monthly_salary < 0 or incentive < 0:
    exit("Enter valid values.")

total_salary = monthly_salary + incentive
print("Total Salary:", total_salary)
