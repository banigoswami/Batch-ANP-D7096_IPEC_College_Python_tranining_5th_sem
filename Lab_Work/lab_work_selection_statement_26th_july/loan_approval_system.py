'''
--------------------------------------------Loan Approval System--------------------------------------------
Problem Statement 
A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  
---------------------------------------------------------------
Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 
---------------------------------------------------------------
Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied. 
--------------------------------------------------------------------------------------------------------------
--------------------------------Coding--------------------------------
'''
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income in rupees: "))
existing_loan = float(input("Enter your existing loan amount: "))
#-------------Validating the inputs----------------
if credit_score < 0 or annual_income < 0 or existing_loan < 0:
    exit("Enter positive values for all inputs.")
#--------------------------------------------------
if credit_score >= 750 and annual_income >= 800000 and existing_loan <= 200000:
    print("---------------------------------------------------------------")
    print("Loan Status: Approved")
    print("---------------------------------------------------------------")
elif (credit_score < 750 and annual_income >= 800000 and existing_loan <= 200000):
    print("---------------------------------------------------------------")
    print("Loan Status: Manual Review")
    print("Reason: Credit score criteria not satisfied.")
    print("---------------------------------------------------------------")
elif (credit_score >= 750 and annual_income < 800000 and existing_loan <= 200000):
    print("---------------------------------------------------------------")
    print("Loan Status: Manual Review")
    print("Reason: Income criteria not satisfied.")
    print("---------------------------------------------------------------")
elif (credit_score >= 750 and annual_income >= 800000 and existing_loan > 200000):
    print("---------------------------------------------------------------")
    print("Loan Status: Rejected")
    print("Reason: Existing loan amount exceeds the limit.")
    print("---------------------------------------------------------------")
else:
    print("---------------------------------------------------------------")
    print("Loan Status: Rejected")
    print("Reason: Multiple criteria not satisfied.")
    print("---------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------