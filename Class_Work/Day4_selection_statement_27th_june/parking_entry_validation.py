'''Parking Entry Validation
Problem Statement
Only vehicles having a valid parking pass are allowed to enter a private parking area.
Accept either 1 (Valid Pass) or 0 (No Pass).
• If the input is 1, display:
Entry Allowed
• Otherwise display:
Entry Denied
Sample Input
0
Sample Output
Entry Denied'''
parking_pass = int(input("Enter 1 if you have a valid parking pass, else 0: "))
# Validating the input
if parking_pass not in [0, 1]:
    exit("Enter valid values.")
    
if parking_pass == 1:
    print("Entry Allowed")
else:
    print("Entry Denied")
    