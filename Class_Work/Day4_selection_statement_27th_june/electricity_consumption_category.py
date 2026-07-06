'''Electricity Consumption Category (if...elif...else Statement)
Problem Statement
An electricity department categorizes households based on monthly electricity consumption.
• Up to 100 units → Low Consumption
• 101–300 units → Moderate Consumption
• Above 300 units → High Consumption
Write a Python program to display the consumption category.
Sample Input
245
Sample Output
Moderate Consumption'''
units_consumed = int(input("Enter the number of units consumed: "))
# Validating the input  
if units_consumed < 0:
    exit("Enter valid values.")
    
if units_consumed <= 100:
    print("Low Consumption")
elif units_consumed <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")
    