'''WAP to create a tuple with 15 numbers given by the user  and print the  odd numbers in the present  tuple.'''
numbers = []
for i in range(15):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers = tuple(numbers)  # Convert list to tuple
print("----------------------------------------------")
#display odd nmbers in the tuple
print("Odd numbers in the tuple:")
for n in numbers:
    if n % 2 != 0:
        print(n)