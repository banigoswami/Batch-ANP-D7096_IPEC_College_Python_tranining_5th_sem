''' 
------------------------------------------E-Commerce Premium Membership Eligibility------------------------------------------
Problem Statement 
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
----------------------------------------------------------
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
----------------------------------------------------------
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000.
----------------------------------------------------------
--------------------------------------------Coding--------------------------------------------
'''
total_purchases = float(input("Total Purchases (in rupees): "))
orders_completed = int(input("Orders Completed: "))
customer_rating = float(input("Customer Rating (out of 5): "))
#-------------Validating the inputs----------------
if total_purchases < 0 or orders_completed < 0 or customer_rating < 0 or customer_rating > 5:
    exit("Enter valid values.")
#-----------------------------------------------------------
if total_purchases > 100000:
    print("----------------------------------------------------------")
    print("Premium Membership Status: Eligible")
    print("Reason: Purchase amount exceeded ₹100000.")
    print("----------------------------------------------------------")
elif total_purchases > 50000 and orders_completed >= 20 and customer_rating >= 4.5:
    print("----------------------------------------------------------")
    print("Premium Membership Status: Eligible")
    print("Reason: All criteria met.")
    print("----------------------------------------------------------")
else:
    print("----------------------------------------------------------")
    print("Premium Membership Status: Not Eligible")
    print("Reason: Criteria not met.")
    print("----------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------