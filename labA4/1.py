s=input("enter a sentence:")
w=input("enter the word to search:")
print("WORD:",w)
s=s.upper()
w=w.upper()
l=s.split()
if not(w in l):
    print("sorry word does not exist in the sentence")
else:
    print("COUNT:",l.count(w))

