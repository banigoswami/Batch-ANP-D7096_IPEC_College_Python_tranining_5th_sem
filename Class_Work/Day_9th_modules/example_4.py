'''Importing module name using alias name'''
import numeric_calculator as nc
a=7
b=3
#calling the add function from numeric_calculator module
print("sum is:", nc.add(a, b))
#calling the subtract function from numeric_calculator module
print("difference is:", nc.subtract(a, b))
#calling the multiply function from numeric_calculator module
print("product is:", nc.multiply(a, b))
#calling the divide function from numeric_calculator module
print("quotient is:", nc.divide(a, b))
#calling the remainder function from numeric_calculator module
print("remainder is:", nc.remainder(a, b))
