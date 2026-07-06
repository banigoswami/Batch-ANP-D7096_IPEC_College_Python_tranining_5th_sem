'''Exam Hall Entry
Problem Statement
Students are allowed to enter the examination hall only if they are carrying their admit card.
Accept input as:
• 1 → Admit Card Available
• 0 → Admit Card Not Available
If the input is 1, display:
Enter Examination Hall
Otherwise, do not display anything.
Sample Input
1
Sample Output
Enter Examination Hall'''
admit_card = int(input("Enter 1 if admit card is available, else 0: "))
# Validating the input
if admit_card not in [0, 1]:
    exit("Enter valid values.")
    
if admit_card == 1:
    print("Enter Examination Hall")
else:
    pass  # Do not display anything if admit card is not available
