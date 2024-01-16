'''
You are babysitting your young nephew. You are finding it difficult to keep her amused.
She doesnt like computer games, but does like doing sums. So you devise the following game for her.

I give you a number. Write it down.
Multiply this number by 3 and add 1. Write your number down unless it is more than 99.
If the number is 100 or more, just write down the last two digits.
You keep going, using the last number you have written down, until you reach the number I gave you.
Then you tell me how long your list is.
Example
 17 → 52 → 57 → 72 → 17
You want to keep your nephew amused for a while, so you dont want a list that is too short or too long.

Task:
Write a program that calculates the length of the list of numbers produced, using the rules above, when supplied with an integer from 1 to 100 inclusive.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

The input will be no more than 100.
Input format:
An integer.
Output format:
An integer.
Example:
Input:
17
Output:
5

'''
number_list = []
match = False
number = int(input())

while not (1 < number < 100):
    number = int(input())

number_list.append(number)
new_num = number

while not match:
    new_num = (new_num * 3) + 1
    if new_num <= 99:
        number_list.append(new_num)
    else:
        new_num = new_num % 100
        number_list.append(new_num)
    if new_num == number:
        match = True

print(len(number_list))
