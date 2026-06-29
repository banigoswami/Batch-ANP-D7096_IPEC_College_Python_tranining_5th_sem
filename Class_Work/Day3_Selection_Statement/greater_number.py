'''
---------------------------------------Find greater number between two numbers---------------------------------------
Compare two numbers and find the greater number.
----------------------------------------------------------
Sample Input:
Enter first number: 10
Enter second number: 20
----------------------------------------------------------
Sample Output:
The greater number is: 20
----------------------------------------------------------
--------------------------------------------Coding----------------------------------------
'''
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print("-------------------------------------------------")
if first_number>second_number:
    print("The greater number is: ", first_number)
elif second_number>first_number:
    print("The greater number is : ", second_number)
else:
    print("The number are equal. No greater number")
print("-------------------------------------------------")