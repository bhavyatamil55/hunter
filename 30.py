bhav=int(input())
las=[int(x) for x in input().split()[:bhav]]
net=[]
for i in range(0,int(len(las))):
    if(i==las[i]):
        net.append(i)
if(int(len(net)))!=0:
    for u in net:
        print(u,end=" ")
else:
    print(-1)
