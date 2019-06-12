"""
The following is useful as part of a program to play Minesweeper. Suppose you have a 5 × 5
list that consists of zeros and M’s. Write a program that creates a new 5×5 list that has M’s in
the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells
(adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint:
short-circuiting may be helpful for avoiding index-out-of-range errors.]

0 M 0 M 0           1 M 3 M 1
0 0 M 0 0           1 2 M 2 1
0 0 0 0 0           2 3 2 1 0
M M 0 0 0           M M 2 1 1
0 0 0 M 0           2 2 2 M 1
"""

matrix[1][1]