#!/usr/bin/python
# coding: utf-8
# A000170 		Number of ways of placing n nonattacking queens on an n X n board. 
# 1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044, 234907967154122528"
#
# Example for n=4 (note the symmetry)
# ☐ ♕ ☐ ☐
# ☐ ☐ ☐ ♕
# ♕ ☐ ☐ ☐
# ☐ ☐ ♕ ☐

# ☐ ☐ ♕ ☐
# ♕ ☐ ☐ ☐
# ☐ ☐ ☐ ♕
# ☐ ♕ ☐ ☐


import argparse, sys 

parser = argparse.ArgumentParser(description='Returns the number of ways of placing n nonattacking queens on an n X n board.')
parser.add_argument('n', type=int, help='The size of the n x n board')
parser.add_argument('-s','--show', action="store_true", help='Display found solutions')
args = parser.parse_args()
n = args.n
count=0

def valid (j, row, p):
    for i in range(row):
        # There's a previous queen in the same column
        if p[i]==j:
            return False
        # There's a previous queen in a diagonal to the left
        if p[i]+row-i == j:
            return False
        # There's a previous queen in a diagonal to the right
        if p[i]-row+i == j:
            return False
    return True

def print_board(p):
    for i in range(n):
        for j in range(1,n+1):
            if (p[i] == j):
                print("♕"),
            else:
                print("☐"),
        print
    print

def nqueens(row,queens):
    global count
    
    if row == n:
        # Found
        count = count + 1
        if args.show:
            print_board(queens)
        return
    for i in range(1,n+1):
        queens[row] = i
        if valid(i, row,queens):
            nqueens(row+1, queens)
    queens[row]=0
if n < 2:
    count = 1
else:
    nqueens(row=0,queens=[0]*n)
print (count)

