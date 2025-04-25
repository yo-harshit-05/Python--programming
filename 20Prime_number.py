# Program 14 : To check prime number
num=int(input("Enter any number\n"))
flag=False
if num==1 or num==2:
    print("The given number is not a prime number")
elif num>2:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
    if flag==True:
        print("The given number is not prime number")
    else:
        print("The given number is a prime number")
else:
    print("The given number is invalid")
