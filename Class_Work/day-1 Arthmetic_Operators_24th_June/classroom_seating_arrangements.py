'''Classroom Seating Arrangement
Scenario:
A school wants to arrange students into equal rows.
Problem Statement:
Write a Python program to determine how many complete rows can be formed.
Input:
• Total Students
• Students per Row
Output:
• Number of Complete Rows'''
total_students = int(input("Enter Total Students: "))
students_per_row = int(input("Enter Students per Row: "))
#-------------Validating the inputs----------------
if total_students < 0 or students_per_row <= 0:
    exit("Enter valid values.")
complete_rows = total_students // students_per_row
print("Number of Complete Rows:", complete_rows)
