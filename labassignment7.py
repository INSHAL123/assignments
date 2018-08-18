class Area:
    def area(self,r=0,l=0):
        if(l==0):
            print("Area of circle is :",3.14*r*r)
        else:
            print("Area of rectangle is :",l*r)
obj=Area()

ch=int(input("SELECT WHOSE AREA IS TO BE CALCULATED \n1.CIRCLE\n2.RECTANGLE\n"))
if(ch==1):
    obj.area(float(input("Enter the radius :")))
elif(ch==2):
    obj.area(float(input("Enter the length :")),float(input("Enter the breath :")))
else:
    print("Wrong choice")
