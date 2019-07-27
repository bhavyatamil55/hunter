net=int(input())
xin=[]
cak=0
for i in range(net):
  xin.append(list(map(int,input().split())))
rest=[]
for i in range(net+1):
  if i==0:
    rest.append(list("0"*(net+2)))
  else:
    sek="0"
    for j in range(net):
      sek=sek+str(x[i-1][j])
    rest.append(list(sek+"0"))
rest.append(list("0"*(net+2)))
for i in range(len(rest)):
  for j in range(len(rest)):
    if rest[i][j]=="1" and rest[i-1][j]==rest[i+1][j]==rest[i][j-1]==rest[i][j+1]==rest[i+1][j+1]==rest[i+1][j-1]==rest[i-1][j+1]==rest[i-1][j-1]=="0":
      cak+=1
print(cak)
