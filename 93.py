bhav=input()
temp=""
fak=0
for i in range(len(bhav)):
  if bhav[i]==" ":
    temp+=bhav[i]
  elif fak==0:
    temp+=bhav[i].upper()
    fak=1
  elif fak==1:
    temp+=bhav[i]
    fak=0
print(temp)
