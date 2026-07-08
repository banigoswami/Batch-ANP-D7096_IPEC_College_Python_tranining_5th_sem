'''by suing the import statement we can use the functions of other modules in our program'''
from numeric_calculator import*
a=7
b=3
#calling the add function from numeric_calculator module
print("sum is:", add(a, b)) 
#calling the subtract function from numeric_calculator module
print("difference is:", subtract(a, b))
#calling the multiply function from numeric_calculator module
print("product is:", multiply(a, b))
#calling the divide function from numeric_calculator module
print("quotient is:", divide(a, b))
#calling the remainder function from numeric_calculator module
print("remainder is:", remainder(a, b))
