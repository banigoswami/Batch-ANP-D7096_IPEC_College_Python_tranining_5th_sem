''' WAP TO COUNT THE NUMBER OF UPPERCASE AND LOWERCASE CHARACTERS IN A GIVEN SENTENCE WITHOUT USING LIBARY FUNCTION. '''
sentence = input("Enter a sentence: ")
uppercase = 0
lowercase = 0
for char in sentence:
    if (char == 'A' or char == 'B' or char == 'C' or char == 'D' or char == 'E' or char == 'F' or char == 'G' or char == 'H' or char == 'I' or char == 'J' or char == 'K' or char == 'L' or char == 'M' or char == 'N' or char == 'O' or char == 'P' or char == 'Q' or char == 'R' or char == 'S' or char == 'T' or char == 'U' or char == 'V' or char == 'W' or char == 'X' or char == 'Y' or char == 'Z'):
        uppercase += 1
    elif (char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e' or char == 'f' or char == 'g' or char == 'h' or char == 'i' or char == 'j' or char == 'k' or char == 'l' or char == 'm' or char == 'n' or char == 'o' or char == 'p' or char == 'q' or char == 'r' or char == 's' or char == 't' or char == 'u' or char == 'v' or char == 'w' or char == 'x' or char == 'y' or char == 'z'):
        lowercase += 1
print("Number of Uppercase characters = ", uppercase)
print("Number of Lowercase characters = ", lowercase)
''' or char <= 'Z' and char >= 'A' or char <= 'z' and char >= 'a' '''
