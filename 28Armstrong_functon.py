# Program for armstrong number by making function
def armst(n):
    test=n
    size=0
    while test>0:
        test//=10
        size+=1
    sum=0
    while n>0:
        rem=n%10
        sum+=rem**size
        n//=10
    return sum
num=int(input("Enter number to check weather a number is armstrong or not \n"))
answer=armst(num)
if answer==num:
    print("The given number is armstrong")
else:
    print("Faaaaaaaaahhhhh!!!!!!!")