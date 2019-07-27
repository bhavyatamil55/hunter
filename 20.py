sp,bh=map(int,input().split())
lac=[]
cak=0
ken=[]
for i in range(sp,bh+1):
        lac.append(bin(i)[2::])
for i in range(0,len(lac*/)):
        ken.append(lac[i].count("1"))
 
for i in range(0,len(ken)):
        if ken[i]!=1 and ken[i]!=2:
                for p in range(2,ken[i]):
                        if ken[i]%p==0:
                                break
                if p==ken[i]-1:
                        cak=cak+1
        elif ken[i]==2:
                cak=cak+1
print(cak)
