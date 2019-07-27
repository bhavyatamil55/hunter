sp=input()
bh=len(sp)

def check_palindrome(sp,bh):
    if sp==sp[-1:-bh-1:-1]:
        bh-=1
        sp=sp[0:bh]
        check_palindrome(sp,bh)
    else:
        print(sp)


check_palindrome(sp,bh)  
