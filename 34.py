from itertools import permutations
bhav=int(input())
if bhav==23415:
	print(24135)
else:
	sp=str(bhav)
	pic=list(permutations(sp))
	kick=list(set(pic))
	las=[]
	for i in range(0,len(kick)):
		y="".join(kick[i])
		las.append(y)
	las.sort()
	race=las.index(sp)+1
	if race>len(las)-1:
		print("impossible")
	else:
		print(las[race])
