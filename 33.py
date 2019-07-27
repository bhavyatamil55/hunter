sp=input()
las=[0]
if "ab" not in sp:
	print("0")
else:
	for i in range(len(sp)):
		cak=1
		for j in range(i,len(sp)-1):
			if sp[j]=="a" and sp[j+1]=="b":
				cak=cak+1
			elif sp[j]=="b" and sp[j+1]=="a":
				cak=cak+1
			else:
				las.append(cak)
				cak=1
				break
		if sp[i]=="a":
			las.append(cak)
		else:
			las.append(cak-1)
	print(max(las))
