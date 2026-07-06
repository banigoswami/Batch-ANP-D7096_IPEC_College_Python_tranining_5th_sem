'''Restaurant Bill Discount
Problem Statement
A restaurant offers discounts based on the total bill amount.
• Bill below ₹1000 → No Discount
• ₹1000–₹2999 → 10% Discount
• ₹3000 or more → 20% Discount
Write a Python program to determine the applicable discount.
Sample Input
3200
Sample Output
20% Discount Applied'''
bill_amount = int(input("Enter the total bill amount: "))
#-------------Validating the inputs----------------
if bill_amount < 0:
    exit("Enter valid values.")
if bill_amount < 1000:
    discount = 0
elif 1000 <= bill_amount < 3000:
    discount = 10
else:
    discount = 20
print(f"{discount}% Discount Applied")
