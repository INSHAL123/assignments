def fibo(n):
    a,b=0,1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)


n=int(input("Enter the number of terms"))
fibo(n)
        
