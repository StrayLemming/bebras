'''
Toothed caterpillars have a curious life cycle.
They are born with teeth in their upper jaw and a different number of teeth in their lower jaw.
After one day the teeth in their upper jaw fall out and they grow new teeth.
On the second day the teeth in their lower jaw fall out and they grow new teeth.
On day three they again grow new teeth in their upper jaw and so on.

The really curious thing is that the number of new teeth they grow on any day is one more than the difference
between the number of teeth in their upper and lower jaws on the previous days.

Example
A caterpillar was born with 6 teeth in its upper jaw and 3 in its lower jaw.

Age (days)  0	1	2	3	4	5
Upper	    6	4	4	3	3	2
Lower	    3	3	2	2	2	2
Difference	3	1	2	1	1	0

When they have the same number of teeth in their upper and lower jaws, they pupate to become butterflies.

Task:
Write a program that determines the caterpillars age, in days, when it pupates (5 in the example).

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

Toothed caterpillars are never born with more than 100 teeth in either jaw, or less than 1.
Input format:
Line 1: The number (as an integer) of teeth in the upper jaw at birth.
Line 2: The number (as an integer) of teeth in the lower jaw at birth.
Output format:
The age at which the caterpillar pupates (an integer).
Example:
Input:
6
3
Output:
5

'''
day = 0
upper_jaw = int(input())
lower_jaw = int(input())

# The upper or lower jaw could have more teeth, so need to make the difference an absolute value
diff = abs(upper_jaw - lower_jaw)
turn = 'upper'
while diff != 0:
    day += 1
    if turn == 'upper':
        upper_jaw = diff + 1
        turn = 'lower'
    elif turn == 'lower':
        lower_jaw = diff + 1
        turn = 'upper'
    diff = abs(upper_jaw - lower_jaw)

print(day)
