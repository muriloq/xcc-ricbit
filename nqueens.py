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
    print(q)


def nqueens(row,q):
    global count
    
    if row == n:
        # Found
        
        s = tuple(q)
        r = tuple(q[::-1])
        f = tuple([n-q[i]+1 for i in range(n)])
        fr = tuple(f[::-1])
        z = [0]*n
        for i in range(n):
            z[q[i]-1]=i+1
        t = tuple(z)
        tr = tuple(z[::-1])
        fzr = tuple([n-t[i]+1 for i in range(n)])

        fzrr = tuple(fzr[::-1])
        u = [0]*n
        for i in range(n):
            u[n-1-i]=n-s[i]+1
        ur = tuple(u[::-1])
        u = tuple(u)

        

        sym = set([s,r,t,f,tr,fzr,u,ur,fzrr])
        if not solutions.isdisjoint(sym):
            return
        
        solutions.add(s)
        count = count + 1

        if args.show:
            print_board(q)
#        for q in [s,r,t,f,tr,fzr,u,ur,fzrr]:
#            print_board(q)
        
        print
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

