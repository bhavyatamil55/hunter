bh,sp=map(int,input().split())
kim=max(bh,sp)
pic=[]
for i in range(1,kim):
    if bh%i==0 and sp%i==0:
        pic.append(i)
if len(pic)==1:
    print("yes")
else:
    print("no")
