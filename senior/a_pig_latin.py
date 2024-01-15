'''
Pig Latin is a language game made by modifying English words:

If the letter starts with a consonant:
Step 1: Remove the first letter of the word.
Step 2: Add a “-” to the end of the word.
Step 3: Add the removed letter.
Step 4: Add ”ay”.

If the letter starts with a vowel just add “-yay“ to the end of the word.

Task:
Write a program that will translate a word into Pig Latin.

Constraints:
[Note: Your code does not need to check constraints - they are provided so you know the range of test data values your program will need to handle.]

The provided input word will only consist of uppercase and lowercase letters.
Input format:
A string consisting of a single English word.
Output format:
A string consisting of the translated input.
Example:
Input:
Hello
Output:
ello-Hay

'''
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
word = input().strip()
pig_word = ""

if word[0].lower() in consonants:
    pig_word = word[1:] + "-" + word[0] + "ay"
elif word[0].lower() in vowels:
    pig_word = word + "-yay"

print(pig_word)
