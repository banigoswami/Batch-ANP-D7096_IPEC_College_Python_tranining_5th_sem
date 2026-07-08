''' Wap to input a string from user and count the number of vowels in the given string.'''

string = input("Enter a string: ")
vowels = 0
for char in string:
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
       char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        vowels += 1
print("Number of vowels in the given string = ", vowels)