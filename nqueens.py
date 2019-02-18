#!/usr/bin/python
# A000170 		Number of ways of placing n nonattacking queens on an n X n board. 
# 1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044, 234907967154122528"
#
# Example for n=4 (note the symmetry)
# ..Q.  .Q..
# Q...  ...Q
# ...Q  Q...
# .Q..  ..Q.

import argparse
parser = argparse.ArgumentParser(description='Returns the number of ways of placing n nonattacking queens on an n X n board.')
parser.add_argument('n', type=int, help='The size of the n x n board')
parser.add_argument('-s','--show', action="store_true", help='Display found solutions')
args = parser.parse_args()
n = args.n
count=0
steps=0


def valid (q, positions):
    for p in positions:
        # There's a previous queen in the same column
        if p[1]==q[1]:
            return False

    # There's a previous queen in a diagonal to the left
    nw = q
    while True:
        nw = (nw[0]-1,nw[1]-1)
        if nw in positions:
            return False
        if nw[0] < 0 or nw[1] < 0:
            break

    # There's a previous queen in a diagonal to the right
    ne = q
    while True:
        ne = (ne[0]-1,ne[1]+1)
        if ne in positions:
            return False
        if ne[0] < 0 or ne[1] >= n:
            break

    return True

def nqueens(level,positions):
    global count,steps
    steps += 1
    
    if level == n:
        # Found
        count = count + 1
        if args.show:
            print (str(positions))
        return
    for i in range(n):
        q = (level,i)
        if valid(q,positions):
            new_positions = positions.copy()
            new_positions.add(q)
            nqueens(level+1, new_positions)

if n < 2:
    count = 1
else:
    nqueens(level=0,positions=set())
print (count)
print ("Total recursive steps:"+str(steps))

