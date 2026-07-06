'''Compound Growth of Savings
Scenario:
A person invests money and wants to see how the amount grows over years.
Problem Statement:
Write a Python program to calculate the value of money after a certain number of years assuming it
doubles every year.
Input:
• Initial Amount
• Number of Years
Output:
• Final Amount'''
initial_amount = float(input("Enter Initial Amount: "))
number_of_years = int(input("Enter Number of Years: "))
#-------------Validating the inputs----------------
if initial_amount < 0 or number_of_years < 0:
    exit("Enter valid values.")
final_amount = initial_amount * (2 ** number_of_years)
print("Final Amount after", number_of_years, "years:", final_amount)
