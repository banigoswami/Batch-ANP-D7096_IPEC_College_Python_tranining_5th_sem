'''Display a menu for selecting one of the following figures:
o Square
o Circle
o Triangle
o Rectangle
2. Based on the user's choice, ask for the required dimensions of the selected figure.
o Example:
▪ Circle → Radius
▪ Square → Side
▪ Rectangle → Length and Breadth
▪ Triangle → Three sides (for perimeter) and Base & Height (for area)
3. Display a second menu to choose the required operation:
o Area
o Perimeter
4. Call the appropriate function from the twodfigures module based on the user's selections.
5. Display the calculated result in a user-friendly format.
6. Allow the user to perform multiple calculations until they choose to exit the application.'''
import twodfigures as tf
print("Select a figure:")
print("1. Square")
print("2. Circle")
print("3. Triangle")
print("4. Rectangle")
print("5. Exit")
choice = int(input("Enter your choice: "))

#square

if choice == 1:
    side = float(input("Enter the side of the square: "))
    print("Select an operation:")
    print("1. Area")
    print("2. Perimeter")
    operation = int(input("Enter your choice: "))
    if operation == 1:
        print("Area of the square:", tf.square_area(side))
    elif operation == 2:
        print("Perimeter of the square:", tf.square_perimeter(side))

 #circle

elif choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    print("Select an operation:")
    print("1. Area")
    print("2. Circumference")
    operation = int(input("Enter your choice: "))
    if operation == 1:
        print("Area of the circle:", tf.circle_area(radius))
    elif operation == 2:
        print("Circumference of the circle:", tf.circle_circumference(radius))

 #triangle

elif choice == 3:
    print("Enter the three sides of the triangle:")
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))
    base = float(input("Base: "))
    height = float(input("Height: "))
    print("Select an operation:")
    print("1. Area")
    print("2. Perimeter")
    operation = int(input("Enter your choice: "))
    if operation == 1:
        print("Area of the triangle:", tf.triangle_area(base, height))
    elif operation == 2:
        print("Perimeter of the triangle:", tf.triangle_perimeter(side1, side2, side3))

#rectangle

elif choice == 4:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Select an operation:")
    print("1. Area")
    print("2. Perimeter")
    operation = int(input("Enter your choice: "))
    if operation == 1:
        print("Area of the rectangle:", tf.rectangle_area(length, width))
    elif operation == 2:
        print("Perimeter of the rectangle:", tf.rectangle_perimeter(length, width))

        #exit
              
elif choice == 5:
    print("Exiting the application.")
