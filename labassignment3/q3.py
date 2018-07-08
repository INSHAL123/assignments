from random import randint
no1=randint(1,6)
no2=randint(1,6)

x,y=int(input(" guess 1 no\t")),int(input(" guess 2 no\t"))
for i in range(6):
    
    if(no1==x and no2==y):
        print("congats! you won")
        break
    elif(i==5):
        print("sorry out of chances numbers are",no1," ",no2)
    else:
        print(" Chance\t", i+2)
        s,t=x,y
        x,y=int(input(" guess 1 no\t")),int(input(" guess 2 no\t"))
        if(s==x and t==y):
            print("you hv entered same values ")
        
        
