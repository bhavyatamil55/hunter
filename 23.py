bhav,mak=map(eval,input().split())
ant=[]
for i in range(bhav):
  ant.append(list(map(eval,input().split())))
post=[]
oooh=[]
temp_out=[]
tak=[]
i=0
j=0
oooh.append(ant[i][j])
post.append([i,j])
while [bhav-1,mak-1] not in post:
  i=0
  for x in post:
    if x[0]+1<bhav and x[1]+1<mak:
      temp_out.append(ant[x[0]+1][x[1]]+oooh[i])
      temp_out.append(ant[x[0]][x[1]+1]+oooh[i])
      tak.append([x[0]+1,x[1]])
      tak.append([x[0],x[1]+1])
    elif x[0]+1<bhav:
      temp_out.append(ant[x[0]+1][x[1]]+oooh[i])
      tak.append([x[0]+1,x[1]])
    elif x[1]+1<mak:
      temp_out.append(ant[x[0]][x[1]+1]+oooh[i])
      tak.append([x[0],x[1]+1])
    i+=1
  post=tak
  tak=[]
  oooh=temp_out
  temp_out=[]
print(max(oooh))
