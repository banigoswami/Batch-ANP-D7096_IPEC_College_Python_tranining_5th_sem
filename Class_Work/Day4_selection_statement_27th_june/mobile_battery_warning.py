'''Mobile Battery Warning
Problem Statement
A smartphone displays a low battery warning only when the battery percentage falls below 15%.
Write a Python program to accept the battery percentage.
If the battery is below 15, display:
Connect Charger Immediately
Otherwise, display nothing.
Sample Input
10
Sample Output
Connect Charger Immediately'''
battery_percentage = int(input("Enter the battery percentage: "))
#-------------Validating the inputs----------------
if battery_percentage < 0 or battery_percentage > 100:
    exit("Enter valid values.")
    
if battery_percentage < 15:
    print("Connect Charger Immediately")
    