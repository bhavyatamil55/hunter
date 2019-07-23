import sys, string, math

def Count_char(Laa, nee) :
    c = [0] * (nee+1)
    c0] = 1
    c[1] = 1
    for i in range(2,nee+1) :
        c[i] = 0
        if (Laa[i-1] > '0') :
            c[i] = c[i-1]
        if (Laa[i-2] == '1'  or ( Laa[i-2] == '2' and Laa[i-1] < '7') ) :
            c[i] += c[i-2]
    return c[nee]

sic = input()
Laa = list(sic)
if sic == '101' :
    print(2)
    sys.exit()
answer = Count_char(Laa,len(Laa))
print(answer)
