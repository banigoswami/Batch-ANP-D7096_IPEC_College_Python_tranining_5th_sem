'''Pizza Distribution
Scenario:
A party organizer wants to distribute pizza slices equally among children.
Problem Statement:
Write a Python program to find how many slices remain after equal distribution.
Input:
• Total Pizza Slices
• Number of Children
Output:
• Remaining Slices'''
total_slices = int(input("Enter Total Pizza Slices: "))
number_of_children = int(input("Enter Number of Children: "))
#-------------Validating the inputs----------------
if total_slices < 0 or number_of_children <= 0:
    exit("Enter valid values.")
remaining_slices = total_slices % number_of_children
print("Remaining Slices:", remaining_slices)
