bhav=input()
app=0
for i in range(len(bhav)):
    if bhav[:i]==bhav[i+1:]:
        app=0
        break
    else:
        app=1
if app==0:
    print("YES")
else:
    print("NO")
