import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#A B C D E F G H I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
a={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25,"@":26}

l = int(input())
h = int(input())
t = input()

t=re.sub('\W','@',t).upper()

base=[]
for i in range(h):
    row = input()
    base.append(row)
#print(base)

lis=[]
for i in range(len(t)):
    lis.append(a[t[i]])
    #print(lis)

letter=""  
for j in range(h):
    for k in range(len(t)):
        letter+=base[j][lis[k]*l:lis[k]*l+l]
    letter+="\n"
print(letter)
