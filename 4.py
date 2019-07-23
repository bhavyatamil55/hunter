import sys, string, math
nick = int(input())
Lass = list(map(int,input().split()))
for i in range(len(Lass)) :
    if Lass.count(Lass[i]) == 1 :
        print(Lass[i])
        break
