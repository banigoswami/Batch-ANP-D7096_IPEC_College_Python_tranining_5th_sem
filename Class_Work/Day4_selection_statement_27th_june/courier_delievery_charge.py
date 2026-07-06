'''Courier Delivery Charge
Problem Statement
A courier company calculates delivery charges based on the package weight.
• Weight up to 2 kg → ₹50
• Weight greater than 2 kg and up to 5 kg → ₹100
• Weight greater than 5 kg → ₹180
Write a Python program to display the delivery charge.
Sample Input
4
Sample Output
Delivery Charge = ₹100'''
package_weight = float(input("Enter the package weight in kg: "))
#-------------Validating the inputs----------------
if package_weight < 0:
    exit("Enter valid values.")
    
if package_weight <= 2:
    delivery_charge = 50
elif package_weight <= 5:
    delivery_charge = 100
else:
    delivery_charge = 180

print(f"Delivery Charge = ₹{delivery_charge}")