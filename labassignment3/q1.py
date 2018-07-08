s=input("ENTER YOUR NAME\t")

for x in s:
    if not(x.isalpha() or x==' '):
        print("invalid name")
        s=input( " enter the name again\t")
        x=0
n=input("ENTER YOUR NUMBER\t")

while (not(n.isdigit()) or len(n)!=10):
      print("enter valid 10 digit number")
      n=(input("ENTER YOUR NUMBER\t"))

a=input("ENTER YOUR ADDRESS\t")

for x in a:
    if not(x.isalnum() or x==' '):
        print("ERROR")
        s=input( " enter the addressagain\t")
        x=0
        
