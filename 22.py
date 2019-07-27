bhav=int(input())
bh=list(map(int,input().split()))
race=1
liss=[]
for i in bh:
  race=race*i
for i in bh:
  liss.append(race//i)
print(*liss)
