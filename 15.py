bh=int(input())
liss=list(map(int,input().split()))
for i in liss:
    if liss.count(i)>1:
        print(i)
        break
else:
    print("unique")
