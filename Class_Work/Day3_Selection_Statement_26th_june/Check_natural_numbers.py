'''
------------------------------------------------Natural Number Check-------------------------------------------------
Check whether a number is a natural number or not. A natural number is a positive integer greater than zero. 
--------------------------------------------------------------------------------------
Sample Input:
Enter a number: 5
--------------------------------------
Sample Output:
The number is a natural number
--------------------------------------
------------------------------Coding--------------------------------
'''
number = int(input("Enter a number: "))
print("--------------------------------------")
if number > 0:
    print("The number is a natural number")
else:
    print("The number is not a natural number")
print("--------------------------------------")
#----------------------------------------------------------------------------------------------------------------------