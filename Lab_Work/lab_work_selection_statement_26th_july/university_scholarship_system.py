''' 
------------------------------------------------University Scholarship System------------------------------------------------
Problem Statement 
Scholarship is awarded based on percentage: 
Percentage Scholarship 
95+ 100% 
90-94 75% 
85-89 50% 
80-84 25% 
Below 80 No Scholarship 
Conditions: 
• Family income must be below ₹8,00,000.  
• Students with disciplinary actions receive no scholarship.  
----------------------------------------------------------------
Sample Input 
Percentage: 92 
Family Income: 500000 
Disciplinary Action (Y/N): N 
----------------------------------------------------------------
Sample Output 
Scholarship Awarded: 75%
----------------------------------------------------------------
--------------------------------Coding--------------------------------
'''
percentage = float(input("Percentage: "))
family_income = float(input("Family Income (in rupees): "))
disciplinary_action = input("Disciplinary Action (Y/N): ")
#-------------Validating the inputs----------------
if percentage < 0 or percentage > 100 or family_income < 0:
    exit("Enter valid values for percentage or family income.")
#--------------------------------------------------
if family_income >= 800000:
    print("------------------------------------------------")
    print("Scholarship Awarded: No Scholarship")
    print("Reason: Family income exceeds ₹8,00,000.")
    print("------------------------------------------------")
elif disciplinary_action == "Y":
    print("------------------------------------------------")
    print("Scholarship Awarded: No Scholarship")
    print("Reason: Student has disciplinary actions.")
    print("------------------------------------------------")
else:
    if percentage >= 95:
        scholarship = 100
    elif percentage >= 90:
        scholarship = 75
    elif percentage >= 85:
        scholarship = 50
    elif percentage >= 80:
        scholarship = 25
    else:
        scholarship = 0

    print("------------------------------------------------")
    print(f"Scholarship Awarded: {scholarship}%")
    print("------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------+++