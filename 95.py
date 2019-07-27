import math
def isprime(bh):
    if(bh ==2):
        return True
    elif(bh%2 == 0):
        return False
    else:
        for j in range(2,int(math.sqrt(bh)+1)):
            if(bh%j == 0):
                return False
        return True
nad = int(input(""))
prime = []
for i in range(2,nad):
    if(isprime(i)):
        prime.append(i)
if(len(prime)>0):
    if(prime[-1] == 97):
        print(" ".join(map(str,prime)),"")
    else:
        print(" ".join(map(str,prime)))
else:
    print(0)
