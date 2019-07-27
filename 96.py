import sys,string
def dgtSum(bh) :
    s1 = 0
    while bh :
        s1 += bh%10
        bh //= 10
    return s1

bh= int(input())
if bh <= 9:
    print(bh)
    sys.exit()
add = bh // 9
bad = bh % 9
if bad :
    sis = str(bad) + str('9') * add
else :
    sis = str('9') * add
print(sis)
