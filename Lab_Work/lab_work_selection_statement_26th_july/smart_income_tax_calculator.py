'''
----------------------------------------------Smart Income Tax Calculator---------------------------------------------- 
Problem Statement 
A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable. 
-----------------------------------------------------------------------------------------------------------------------
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
----------------------------------------------------------------------
Sample Output 
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0 
--------------------------------Coding--------------------------------
'''
income = float(input("Enter Annual Income: "))
#-------------Validating the income----------------
if income < 0:
    exit("Enter a positive value.")
#--------------------------------------------------
age = int(input("Enter Age: "))
#------------Validating the age----------------
if age < 0:
    exit("Enter a positive value.")
gender = input("Enter Gender (M/F): ")

# Calculate tax before rebate
if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = (income) * 0.1
elif income <= 2000000:
    tax = (income) * 0.2
else:
    tax = (income) * 0.3

Final_tax= tax

# Calculate rebates
if age >= 60:
    senior_citizen_rebate = tax * 0.05
    Final_tax -= senior_citizen_rebate
else:
    senior_citizen_rebate = 0

if gender == "F":
    women_rebate = tax * 0.02
    Final_tax -= women_rebate
else:
    women_rebate = 0

print("-----------------------------------------------------------")
print("Tax before rebate: ₹", tax)
print("Senior Citizen Rebate: ₹", senior_citizen_rebate)
print("Women Rebate: ₹", women_rebate)
print("Final Tax Payable: ₹", Final_tax)
print("-----------------------------------------------------------")
#------------------------------------------------------------------------