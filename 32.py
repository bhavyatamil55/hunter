bhav=int(input())
las=list(map(int,input().split()))
ate=las
cak=[]
while(len(ate)!=1):
	for i1 in range(len(ate)):
		if i1%2!=0:
			cak.append(ate[i1])
	ate=cak
	cak=[]
print(las.index(ate[0]))
