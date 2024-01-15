'''
A student wants to be able to find all the square numbers from 2 to n, where n is a positive integer.

Task
Write a program that outputs a list of all the square numbers from 2 to n.

Constraints
1 < n < 1000.

Example
Input:
10
Output:
4 9 16 25 36 49 64 81 100

'''
n = 0
squared_list = []

while n < 2 or n > 999:
    n = int(input())

for i in range(2, n+1):
    squared_list.append(i**2)

print(*squared_list)
