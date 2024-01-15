'''
3 x 3 magic squares consist of 9 digits arranged in three rows.
What makes them magical is that all the rows, all the columns, and the two diagonals, add up to the same number. This number is always 15.

Example Magic Square
8 1 6
3 5 7
4 9 2

Task
Write a program that takes, as input, the three rows of a magic square arrangement and checks that it is indeed magic.
Your program should output "magic" if it is and "muggle" if it is not.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

All integers in the input will be: 1, 2, 3, 4, 5, 6, 7, 8, or 9.
Input format:
Three rows of three integers separated by spaces.
Output format:
A string.
Example:
Input:
8 1 6
3 5 7
4 9 2
Output:
magic

'''

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]
dia1 = [row1[0], row2[1], row3[2]]
dia2 = [row1[2], row2[1], row3[0]]

magic_square = [row1, row2, row3, col1, col2, col3, dia1, dia2]

is_magic = ''


def magic_check(data):
    # Check to see if data is magic
    if sum(data) == 15:
        return True
    else:
        return False


for i in magic_square:
    if magic_check(i) == True:
        is_magic = 'magic'
    else:
        is_magic = 'muggle'
        break

print(is_magic)
