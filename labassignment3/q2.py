
no=float(input("enter a number\t"))
if(no-int(no)==0.5):
    no=int(no+1)
else:
    no=round(no)
from math import sqrt
print ("square root of",no ,"is",sqrt(no))
