def rev(n):
    r=0
    while(n!=0):
        n,d=divmod(n,10)
        r=r*10+d
    return r
n=int(input("ENTER A NUMBER:"))
s=rev(n)
if(s==n):
    print("NO IS PALINDROME ")
else:
    print("NO IS NOT PALINDROME")
