'''
-------------------------------------------------Smart Electricity Billing System-------------------------------------------------
Problem Statement 
Calculate electricity bill using: 
Units Rate 
0-100 ₹5/unit 
101-300 ₹7/unit 
Above 300 ₹10/unit 
Additional Rules: 
• Commercial consumers pay 20% extra.  
• Bills above ₹5000 attract 5% surcharge.  
• Senior citizens receive 10% discount.  
----------------------------------------------------------------------
Sample Input 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y 
----------------------------------------------------------------------
Sample Output 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103 
----------------------------------------------------------------------
---------------------------------------------Coding--------------------------------------------
'''
units = int(input("Units Consumed: "))
consumer_type = input("Consumer Type (Residential/Commercial): ")
senior_citizen = input("Senior Citizen (Y/N): ")
#-------------Validating the inputs----------------
if units < 0:
    exit("Enter a positive value for units consumed.")
if consumer_type not in ["Residential", "Commercial"]:
    exit("Enter a valid consumer type (Residential/Commercial).")
if senior_citizen not in ["Y", "N"]:
    exit("Enter a valid response for senior citizen status (Y/N).")
#--------------------------------------------------
# Calculate base bill
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + ((units - 100) * 7)
else:
    base_bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
# Apply commercial charge
commercial_charge = 0
if consumer_type == "Commercial":
    commercial_charge = base_bill * 0.20

# Apply surcharge (on bill after commercial charge)
bill_after_commercial = base_bill + commercial_charge
surcharge = 0
if bill_after_commercial > 5000:
    surcharge = bill_after_commercial * 0.05

# Apply senior citizen discount (on bill after surcharge)
bill_after_surcharge = bill_after_commercial + surcharge
discount = 0
if senior_citizen == "Y":
    discount = bill_after_surcharge * 0.10

# Calculate final bill amount
final_bill = bill_after_surcharge - discount
print("------------------------------------------------------")
print(f"Base Bill: ₹{base_bill:.2f}")
print(f"Commercial Charge: ₹{commercial_charge:.2f}")
print(f"Surcharge: ₹{surcharge:.2f}")
print(f"Senior Citizen Discount: ₹{discount:.2f}")      
print(f"Final Bill Amount: ₹{final_bill:.2f}")
print("------------------------------------------------------")