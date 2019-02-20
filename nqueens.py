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


import argparse, sys, sets 

parser = argparse.ArgumentParser(description='Returns the number of ways of placing n nonattacking queens on an n X n board.')
parser.add_argument('n', type=int, help='The size of the n x n board')
parser.add_argument('-u','--unique', action="store_true", help='Symmetric solutions count only once')
parser.add_argument('-s','--show', action="store_true", help='Display found solutions')
args = parser.parse_args()
n = args.n
count=0
solutions = set()


def valid (j, row, q):
    for i in range(row):
        # There's a previous queen in the same column
        if q[i]==j:
            return False
        # There's a previous queen in a diagonal to the left
        if q[i]+row-i == j:
            return False
        # There's a previous queen in a diagonal to the right
        if q[i]-row+i == j:
            return False
    return True

def print_board(q):
    for i in range(n):
        for j in range(1,n+1):
            if (q[i] == j):
                print("♕"),
            else:
                print("☐"),
        print
    print

def symmetries(q):
    # Original
    s = tuple(q)

    # Horizontal Mirror
    hmirror = tuple(q[::-1])
    
    # V. Mirror  
    vmirror = tuple([n-q[i]+1 for i in range(n)])

    # Transpose
    transpose = [0]*n
    for i in range(n):
        transpose[q[i]-1]=i+1
    transpose = tuple(transpose)
    
    # Transpose + Horizontal Mirror
    transpose_hmirror = tuple(transpose[::-1])
    
    # Transpose + Vertical Mirror
    transpose_vmirror = tuple([n-transpose[i]+1 for i in range(n)])
    
    # Transpose + Vertical Mirror + Horizontal Mirror
    transpose_vmirror_hmirror = tuple(transpose_vmirror[::-1])
    
    # Rotate 180
    r180 = [0]*n
    for i in range(n):
        r180[n-1-i]=n-s[i]+1
    r180 = tuple(r180)
    
    # Rotate 180 + Horizontal Mirror
    r180_hmirror = tuple(r180[::-1])
    
    sym = set([s,hmirror,transpose,vmirror,transpose_hmirror,transpose_vmirror,r180,r180_hmirror,transpose_vmirror_hmirror])
    return sym

def nqueens(row,q):
    global count
    
    if row == n:
        # Found
        
        if args.unique:
            sym = symmetries(q)
            if not solutions.isdisjoint(sym):
                return
            solutions.add(tuple(q))

        count = count + 1

        if args.show:
            print_board(q)

        return
    for i in range(1,n+1):
        q[row] = i
        if valid(i, row,q):
            nqueens(row+1, q)
    q[row]=0
if n < 2:
    count = 1
else:
    nqueens(row=0,q=[0]*n)
print (count)

