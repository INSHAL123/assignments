
def armstrong (no):
    x=no
    s=0
    while(x!=0):
        x,d=divmod(x,10)
        s=s+d**3
    return s
        
no=int(input("ENTER A NUMBER"))
r=armstrong(no)
if(r==no):
    print("number is armstrong")
else:
    print("number is not armstrong")
