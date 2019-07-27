bh=int(input())
sp=list(map(int,input().split()))
cak=[]
for i in range(0,bh):
    dan=sp[i:]
    eat=max(dan)
    if sp[i]==eat:
        cak.append(sp[i])
print(*cak)
print(max(sp))
