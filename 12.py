try:
    bh,sp=map(int,input().split())
    bhav=list(map(int,input().split()))
    bhav1=sorted(bhav)
    print(bhav1[bh-sp])
except ValueError:
    print("invalid")
