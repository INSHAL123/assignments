x=["is","am","are","of","as","on","a"]
print(x)
y=[]
s=input("ENTER A SENTENCE:")
s=s.lower()
l=s.split()
for i in l:
    if not(i in x):
        y.append(i)
        


print (" ".join(y))        
