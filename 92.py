from itertools import permutations
Nee=input()
kem=permutations(Nee)
las=[]
mass=(-1)
ate="abcdefghijklmnopqrstuvwxyz"
if ate==Nee:
  print(Nee)
elif Nee==ate[::-1]:
  print("-1")
else:
    Nee=tuple(Nee)
    for i in kem:
        las.append(i)
    for i in las:
        if i>Nee:
            mass=i
            break

    for i in las:
        if i>Nee and i<mass:
            mass=i

    if mass==-1:
        print("-1")
    else:
        for i in mass:
            print(i,end="")
