'''
Saving UpReview mode
Kaleisha, a student, works at a coffee shop and is trying to save her earnings to buy an e-bike.
She spends £20 a day on food and bus fares.
She wants to find out if she will be able to buy an e-bike after 10 days of working.
The bike Kaleisha wants to buy is £1000. She looks back at her pay for the last 20 days working at the coffee shop.

Task:
Write a program that totals Kaleisha's daily earnings and outputs how many days it would have taken her, in the provided 20 days, to save £1000.
Your program must also remove the student's £20 daily expenses.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

All integers in the input will be less than or equal to 200.
The data provided will always be enough to save £1000 by the 20th day.
Input format:
A single row of 20 integers separated by spaces.
Output format:
An integer.
Example:
Input:
80 150 200 90 110 150 150 77 59 200 100 190 205 190 115 150 160 97 102 100
Output:
10

'''
total = 0
days = 0
expenses = 20
earnings = input().split()
for n, earning in enumerate(earnings, start=1):
    total += int(earning) - expenses
    if total >= 1000:
        break
print(n)
