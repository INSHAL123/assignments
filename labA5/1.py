d={}


d.setdefault('MATHS',int(input("enter marks of maths:")))
max=min=d.get('MATHS')
d.setdefault('PHY',int(input("enter marks of physics:")))
d.setdefault('MECH',int(input("enter marks of mech:")))
d.setdefault('CHEM',int(input("enter marks of chem:")))
d.setdefault('JAVA',int(input("enter marks of java:")))
for each in d.values():
    if(each>max):
        max=each
    if(min>each):
        min=each
print("max value is :",max)
print("minimum value is :",min)
