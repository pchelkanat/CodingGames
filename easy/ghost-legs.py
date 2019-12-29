import sys
import math
import numpy as np
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
mas=np.array([[input()]for i in range(h)])

mas1=[]
for line in mas:
    s=re.sub(r"--", r"- -", line[0]).split()
    mas1.append(s)
mas1=np.array(mas1)

for i in range(w//2):
    index=i
    let=mas1[0,index]
    for k in range(1,h):
        if mas1[k,index]=="|":
            index+=0
        elif mas1[k,index]=="|-":
            index+=1
        elif mas1[k,index]=="-|":
            index-=1
    print(str(let)+str(mas1[-1,index]))

