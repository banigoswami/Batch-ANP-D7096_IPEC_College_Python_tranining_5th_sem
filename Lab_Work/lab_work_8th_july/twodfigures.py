'''Develop a menu-driven Python application that demonstrates the use of User-Defined
Modules and Functions.
Requirements
You are required to create a Python module named twodfigures.py that contains functions to perform
the following calculations for different two-dimensional shapes:
• Triangle
o Calculate Area
o Calculate Perimeter
• Circle
o Calculate Area
o Calculate Circumference (Perimeter)
• Square
o Calculate Area
o Calculate Perimeter
• Rectangle
o Calculate Area
o Calculate Perimeter'''
def triangle_area(base, height):
    return 0.5 * base * height
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
def circle_area(radius):
    return 3.14 * radius * radius
def circle_circumference(radius):
    return 2 * 3.14 * radius
def square_area(side):
    return side * side
def square_perimeter(side):
    return 4 * side
def rectangle_area(length, width):
    return length * width
def rectangle_perimeter(length, width):
    return 2 * (length + width)

    