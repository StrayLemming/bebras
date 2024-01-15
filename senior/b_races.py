'''
Four friends: A, B, C, and D, are racing multiple times to see who wins the most. Each race winner is awarded 1 point. If a player wins two times in a row they are awarded their winning point and an extra point.

Task:
Write a program that outputs the score of the overall winner (or winners if there is a draw).

Constraints:
[Note: you do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

Provided data will consist of no more than 100 race results.
Input format:
A string of uppercase letters separated by spaces. Each letter represents the player that won that race.
Output format:
An integer.
Example:
Input:
A A B C D C B C D D
Output:
4
'''
data = list(input().split())
players = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}
last = ""

for i in data:
    if i == last:
        players[i] = players[i]+2
    else:
        players[i] = players[i]+1
    last = i

winner = max(players.values())
print(winner)
