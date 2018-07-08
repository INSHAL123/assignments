n=int(input("enter how many numbers are there\t"))
x=int(input("enter a number"))
gr=sm=total=x
avg=0
for i in range(n-1):
    x=int(input("enter   number"))
    if(x>gr):
        gr=x
    if(x<sm):
        sm=x

    total+=x
avg=total/n
print("greatest number is ",gr)
print("smallest number is",sm)
print("total is ",total)
print("average is",avg)
        
    
