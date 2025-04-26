# Program 16 : Factorial number
num=int(input("Enter any number you want to calculate factorial\n"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of given number is ",fact)
