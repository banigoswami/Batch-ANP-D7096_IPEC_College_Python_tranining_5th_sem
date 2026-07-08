'''Word Frequency Counter
Problem Statement:
Accept a sentence from the user and create a dictionary that stores the frequency of each word.
Example:
Input:
python is easy and python is powerful
Output:
{
'python': 2,
'is': 2,
'easy': 1,
'and': 1,
'powerful': 1
}
Additionally:
• Display the most frequently occurring word.
• Display all words in alphabetical order'''
dict = {}
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
# Display the most frequently occurring word
if dict:
    most_frequent_word = max(dict, key=dict.get)
    print(f"\nMost frequently occurring word: {most_frequent_word} (appears {dict[most_frequent_word]} times)")
# Display all words in alphabetical order
print("\nWords in alphabetical order:")
for word in sorted(dict.keys()):
    print(f"{word}: {dict[word]}")
    