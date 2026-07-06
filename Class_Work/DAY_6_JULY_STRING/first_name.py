''' WAP to ask the user to input the name and deisplay the first name from it without using the libraray methods'''
name = input("Enter your name: ")
name = name.strip()
first_name = ""
for char in name:
    if char == " ":
        break
    first_name += char
    print("First name is:", first_name)
