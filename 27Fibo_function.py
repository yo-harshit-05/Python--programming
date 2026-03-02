# Function to print fibonacci to a given number 
def fibo(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()
fibo(100)
