'''
In a Fibonacci sequence of numbers, the first two numbers are given and the next number in the sequence is the sum of the preceding two numbers.

The original Fibonacci sequence starts with 0, 1 and the Lucas sequence starts with 2, 1. But the same rule “the next number in the sequence is the sum of the preceding two numbers” can be used to generate sequences with any two starting numbers.

Example Fibonacci Series
0, 1, 1, 2, 3, 5, 8, ...
2, 1, 3, 4, 7, 11, 18, ...
7, 12, 19, 31, 50, 81, ...
You and your friend are fascinated with Fibonacci sequences.
Your friend has made the extraordinary claim that any given positive starting pair of numbers will generate a sequence that contains, within the first 25 numbers, a number that is the reverse of the previous number. For instance 36, 81 → 117, 198, 315, 513.

You are sceptical about this claim, and decide to write a program to test it out.

Task:
Write a program that tests out your friend's claim.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

All input integers will be between 0 and 5000 inclusive.
Input format:
The first two integers of the sequence are provided on two rows of input data.
Output format:
The first number that is the reverse of the preceeding number OR -1 if no such number is found in the first 25 numbers of the sequence.
Example:
Input:
36
81
Output:
513


'''
seq = []
i = 0
result = -1
first_num = seq.append(int(input()))
second_num = seq.append(int(input()))


def reverse(number):
    reversed_num = 0
    while number != 0:
        digit = number % 10  # Get the last digit
        reversed_num = (reversed_num * 10) + digit
        number = number // 10  # Remove the last digit using floor division
    return reversed_num


for i in range(23):
    seq.append(seq[i] + seq[i+1])
    if reverse(seq[i+1]) == seq[i]:
        result = seq[i+1]
        break

print(result)
