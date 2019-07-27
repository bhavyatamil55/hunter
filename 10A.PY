bhav,bhav1=map(int,input().split())
vSB={int(vSB) for vSB in input().split()}
sp={int(sp) for sp in input().split()} 
if(sp.issubset(vSB)):
  print("YES")
else:
  print("NO")
