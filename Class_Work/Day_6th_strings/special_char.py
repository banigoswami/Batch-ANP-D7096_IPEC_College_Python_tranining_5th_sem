'''WAP to count number of special characters in a given string.'''
string = input("Enter a string: ")
special_characters = 0
for char in string:
    if not (char.isalnum() or char.isspace()):
        special_characters += 1
print("Number of special characters in the given string = ", special_characters)



