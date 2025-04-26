# Program 18 : Fibonacci series
size=int(input("Enter size of the series\n"))
first,second=0,1
print(first,second,end=' ')
for i in range(2,size):
    fibo=first+second
    print(fibo,end=' ')
    first=second
    second=fibo
