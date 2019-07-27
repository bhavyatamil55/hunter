import sys,string
bhav= int(input())
Las = [ int(x) for x in input().split()]
sak = 0
for i in range(0,bhav) :
    sak = sak + Las[i]

for j in range(bhav-2,-1,-1) :
    for i in range(0,bhav-j) :
        lia, ria = i,j+i
        s1 = sum(Las[lia:ria+1])
        if s1 > sak :
            sak = s1
print(sak)
