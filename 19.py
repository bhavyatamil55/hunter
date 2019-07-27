bhav=list(map(int,input().split()))
net=int(bhav[0])
ken=int(bhav[1])
any=[]
for i in range(0,net):
    any.append(input().split())
cet=set(any[0])
for i in any:
    cet=cet & set(i)
dek=list(cet)
dek.sort()
print(*dek)
