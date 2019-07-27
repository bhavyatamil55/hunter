bhav=[int(s) for s in input().split()]
sp=[int(s) for s in input().split()]
fak=1
for i in range(bhav[0]):
    for j in range(bhav[0]):
        if i!=j:
            if bhav[1]==sp[i]+sp[j]:
                fak=0
                break
if fak==0:
    print('YES')
else:
    print('NO')
