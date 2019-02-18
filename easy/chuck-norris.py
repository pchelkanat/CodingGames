import sys
import math

message = input()
s = ''
for i in range(len(message)):
    mes = ord(message[i])
    mes = format(mes, 'b').zfill(7)
    s += mes

s = s.replace("01", "0.1").replace("10", "1.0")
# print(s)
t = s.split(".")
# print(t)
res = ""
for i in t:
    if i[0] == "1":
        res += "0 " + "0" * len(i) + " "
    elif i[0] == "0":
        res += "00 " + "0" * len(i) + " "

print(res[:-1])