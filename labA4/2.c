x=["is","am","are","of","as","on","a"]
s=input("ENTER A SENTENCE")
print(s)
l=s.split()
for each in l:
    if(each in x):
        l.remove(each)
print (" ".join(l))        
