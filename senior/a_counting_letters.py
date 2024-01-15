'''
A program is required to count how many vowels and consonants are used in a given sentence.

Task:
Write a program that counts the total number of vowels and consonants used in a sentence. Output the number of vowels then the number of consonants, separated by a space.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

Sentences will only contain upper and lowercase letters, spaces and a full-stop.
Input format:
A string.
Output format:
Two integers separated by a space.
Example:
Input:
I love programming.
Output:
6 10
'''
vowels = ('a', 'e', 'i', 'o', 'u')

count_vowels = 0
count_const = 0

sentence = input().strip().lower()
for i in sentence:
    if i.isalpha():
        if i in vowels:
            count_vowels += 1
        else:
            count_const += 1

print(count_vowels, count_const)
