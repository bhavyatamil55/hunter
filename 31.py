tak=int(input())
sak=[int(i) for i in input().split()]
ate=[]
for i in range(0,tak):
    cak=1
    for j in range(i,tak):
        cak=cak*sak[j]
    ate.append(cak)
for i in range(0,tak):
    cak=1
    for j in range(i+1):
        cak=cak*sak[j]
    ate.append(cak)
print(max(ate))
