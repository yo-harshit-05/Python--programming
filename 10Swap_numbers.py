#Program 4 : To swap 2 numbers

a=int(input("Enter values for a\n"))
b=int(input("Enter values for b\n"))
print(f"The values of a and b before swapping is\na={a},b={b}")
a=a+b
b=a-b
a=a-b
print(f"The values of a and b after swapping is\na={a},b={b}")
