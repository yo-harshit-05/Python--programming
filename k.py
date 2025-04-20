# Program 2 : Calculate sum and division of numbers

a=int(input("Enter Value for a\n"))
b=int(input("Enter Value for b\n"))
sum=a+b
print("The sum of a and b is\n",sum)
div=b/a
if b==0:
    print("Denominator can't be zero")
else:
    print("The division of a and b is\n",div)
