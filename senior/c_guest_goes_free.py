'''
The Developers Social Club (DSC) holds a monthly meeting at a restaurant where a guest is always invited.
The DSC consists of 10 members but they do not always attend the monthly meal.
The guest is never asked to pay so the cost of the meal is shared by the DSC members attending like this:

1. The total bill from all the diners is calculated.
2. A tip of 5% is added (no rounding).
3. The individual bill for the DSC members is calculated by dividing the total including the tip by the number of diners - 1. (The guest never pays.)
4. The result of the calculation above is rounded down to the nearest whole pence.

Obviously the DSC would like a computer to do this. They have invited you to join the DSC as long as you will write them a program to sort out their monthly restaurant payments.

Task:
Write a program that takes, as input, the total number of diners and their individual bills and outputs how much each of the DSC members attending the meal should pay.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

Maximum number of diners = 10 DSC members + 1 guest.
The individual bills never come to more than £100.

Input format:
Row 1: The number of diners, n, including the guest as an integer.
n rows of data: Each row of data consists of a float to 2 decimal places. (The individual bills.)

Output format:
The cost each DSC has to pay to cover the bill and tip in UK money format. (e.g. 5.60)

Example:
Input:
5
5.60
7.42
3.16
6.94
9.20
Output:
8.48

'''
import math


def round_down(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier) / multiplier


bill_total = 0
guest = 1
tip = 1.05
diners = int(input())

for i in range(diners):
    bill = float(input())
    bill_total = bill_total + bill

bill_total = bill_total * tip

individual_bill = round_down((bill_total / (diners - guest)), 2)

print(individual_bill)
