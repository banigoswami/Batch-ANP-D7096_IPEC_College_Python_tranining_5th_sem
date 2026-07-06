'''Bank Account Balance
Scenario:
A customer withdraws money from their bank account.
Problem Statement:
Write a Python program to calculate the remaining balance after withdrawal.
Input:
• Current Balance
• Withdrawal Amount
Output:
• Remaining Balance'''
current_balance = float(input("Enter Current Balance: "))
withdrawal_amount = float(input("Enter Withdrawal Amount: "))
#-------------Validating the inputs----------------
if current_balance < 0 or withdrawal_amount < 0:
    exit("Enter valid values.")
if withdrawal_amount > current_balance:
    exit("Insufficient balance.")
remaining_balance = current_balance - withdrawal_amount
print("Remaining Balance:", remaining_balance)
