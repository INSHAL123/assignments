class reverse:
    
    def rev(self,given):
        l=len(given)
        for i in range (l//2):
            t=given[i]
            given[i]=given[l-1-i]
            given[l-1-i]=t
        print("reverse string is ",given)

        
        

obj=reverse()
y=[]
n=(int (input("enter no of elemnts in list")))
for j in range (n):
    x=(int(input("enter element no ")))
    y.append(x)
obj.rev(y)
