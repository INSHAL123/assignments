j=0
for i in range(1,101):
 for j in range(2,i//2):
  if(i%j==0):
    break
 if(j==i-1):
   print(i)
