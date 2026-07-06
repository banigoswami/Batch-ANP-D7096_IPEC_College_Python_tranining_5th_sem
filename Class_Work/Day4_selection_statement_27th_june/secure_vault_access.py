'''Secure Vault Access
Problem Statement
A digital vault can only be opened if the user enters the correct security code.
Write a Python program that accepts the entered security code. If the entered code is 7890, display:
"Access Granted to the Vault."
Otherwise, do nothing.
Sample Input
7890
Sample Output
Access Granted to the Vault'''
security_code = int(input("Enter the security code: "))
#-------------Validating the inputs----------------
if security_code < 0:
    exit("Enter valid values.")
    
if security_code == 7890:
    print("Access Granted to the Vault.")
    