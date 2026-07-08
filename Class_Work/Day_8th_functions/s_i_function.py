''' WAP to calculate the simple interest using function.'''
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
print("The simple interest is:", simple_interest(principal, rate, time))
#parameterized function
#arguments are passed to the functions 
#principal, rate , time are functions arguments 
#print accept the arguments and pass it to the function simple_interest 
