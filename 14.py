from itertools import permutations
bh=input()
bh=list(bh)
perm=permutations(bh)
ant=[]
for j in list(perm):
    ant.append(''.join(list(j)))
bhav=list(set(ant))
cak=[]
for i in range(len(bhav)):
    cak.append(bhav[i])
cak.sort()
for i in range(len(cak)):
    print(cak[i])
