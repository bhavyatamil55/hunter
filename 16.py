bh,sp=map(int,input().split())
cse=list(map(int,input().split()))
dml=[[abs(i-sp),i] for i in cse]
dml.sort()
dml=dml[1:]
eat=[i[1] for i in dml[:3]]
print(*eat)
