'''
Susan runs a company that supplies ground source heat pumps to people looking to replace their gas boilers. There are two ways of installing ground source heat pumps:

Horizontally: This needs a large garden as shallow trenches are dug and lengths of pipes that extract heat out of the ground are layed in the trenches.
Vertically: This can be done in a much smaller space as 100m holes are drilled vertically and 100m lengths of pipe are inserted to extract the heat from the ground. 
The horizontal system is cheaper to install than the vertical system but requires that the garden area is at least 2.5 times as large as the floor area in the house.
The vertical system needs a new 100m bore hole and pipe to be installed for every 100m2 of house floor space. (e.g. 100m2 floor space requires 1 vertical pipe and 101m2 requires 2 pipes.)

Task:
Write a program that inputs a house's floor area, and its garden area. The program should then output "Horizontal" if this system is viable or "Vertical" and the number of 100m bores that will need to be drilled for this particular house.

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

The house floor area will not exceed 300m2.
The garden area will not exceed 2000m2.

Input format:
Row 1: A house floor area in m2 as an integer.
Row 2: The garden area in m2 as an integer.

Output format:
Row 1: Either the string "Horizontal" or "Vertical".
Row2: If "Vertical" the number of vertical pipes required as an integer.

Example 1:
Input:
150
750

Output:
Horizontal
Example 2:

Input:
150
300

Output:
Vertical
2

'''
import math


def check(a, b):
    if a/b >= 2.5:
        print("Horizontal")

    else:
        print("Vertical")
        print(math.ceil(b/100))


house_floor_area = int(input())
garden_area = int(input())

check(house_floor_area, garden_area)
