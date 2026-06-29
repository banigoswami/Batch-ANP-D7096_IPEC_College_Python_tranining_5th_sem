'''
-------------------------------------------------------Airline Ticket Pricing Engine-------------------------------------------------------
Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
------------------------------------------------------
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
-------------------------------------------------------
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0
-------------------------------------------------------
-------------------------------------------------------Coding-------------------------------------------------------
'''
age = int(input("Enter Passenger age: "))
#----------------------------validating age------------------------------
if age<0:
    exit("Please enter a positive number")
#------------------------------------------------------------------------
business_class = input("Business Class (Y/N): ")
window_seat = input("Window Seat (Y/N): ")
weekend_travel = input("Weekend Travel (Y/N): ")
#-------------------------calculating additional charges--------------------------
fare=5000
print("-------------------------------------------------------")
print("Base Fare: ₹", fare)
additional_fare=0
if (business_class=="Y"):
    additional_fare+=3000
if (window_seat=="Y"):
    additional_fare+=500
if (weekend_travel=="Y"):
    additional_fare+=1000
print("Additional Charges: ₹", additional_fare)
#-------------------------calculating discount--------------------------
total_fare=0
if age<12:
    total_fare=(fare+additional_fare)*(1-0.5)
    print("Kids Discount: 50%")
elif age>60:
    total_fare=(fare+additional_fare)*(1-0.2)
    print("Senior Citizen Discount: 20%")

print("Final Ticket Fare: ₹", total_fare)
print("-------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------