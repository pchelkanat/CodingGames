import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
else:
    lis = []
    lik = []
    k = 0
    for i in input().split():
        t = int(i)
        if t > 0:
            k = 1
        lis.append(t)
        lik.append(abs(t))

    if k == 0:
        closet = min(lik)
        t1 = lik.index(closet)
        print(lis[t1])
    elif k == 1:
        closet = min(lik)
        t1 = lis.index(closet)
        print(lis[t1])
