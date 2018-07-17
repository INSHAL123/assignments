#wap to print armstrong no between 1 to 1000
for i in range(1,1001):
    x,s=i,0
    while(x!=0):
        x,d=divmod(x,10)
        s=s+d**3
    if(s==i):
        print(i)
