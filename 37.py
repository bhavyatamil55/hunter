from itertools import combinations
sp=input()
tak=0
las=list(combinations(sp,len(sp)-1))
for i in range(len(las)):
    if las[i]==las[i][::-1]:
        print("YES")
        tak=1
        break
if tak==0:
    print("NO")
