'''ATM Cash Withdrawal
Problem Statement
A customer can withdraw money only if the requested amount does not exceed the available balance.
Accept the account balance and withdrawal amount.
• If withdrawal amount is less than or equal to balance, display:
Transaction Successful
• Otherwise display:
Insufficient Balance
Sample Input
5000
4500
Sample Output
Transaction Successful'''
account_balance = int(input("Enter the account balance: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))
#-------------Validating the inputs----------------
if account_balance < 0 or withdrawal_amount < 0:
    exit("Enter valid values.")
    
if withdrawal_amount <= account_balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
    