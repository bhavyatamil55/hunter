AB=input().split()
big=[]
for i in AB:
  big.append(i[::-1])
print(*big)
