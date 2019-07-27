bh,sp,cc=map(int,input().split())
cnt=0
for i in range(bh,sp+1):
   if str(cc)in str(i):
       cnt+=1
print(cnt)
