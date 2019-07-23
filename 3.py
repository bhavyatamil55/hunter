import sys, string, math
nin = int(input())
Len = list(map(int,input().split()))
List = []
for i in range(nin) :
    if Len[i] == i :
        List.append(i)
Laa = sorted(List)
if len(Laa) == 0 : 
  print(-1)
else :    
  print(*Laa)
