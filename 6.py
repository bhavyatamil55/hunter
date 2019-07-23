import sys, string, math
nick = int(input())
Liss = list(map(int,input().split()))
flags = 1
for i in range(len(Liss)) :
    if Liss.count(Liss[i]) > 1 :
        print(Liss[i])
        flags = 0
        break
if flags == 1 : print('unique')
