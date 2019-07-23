bh=input()
la=[bh[i] for i in range(len(bh)) if i%2==0]
s=[bh[i] for i in range(len(bh)) if i%2!=0]
for j in range(len(bh)//2):
  print(s[j]+la[j],end="")
