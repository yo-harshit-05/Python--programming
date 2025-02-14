#use of ternary operator type one
#find the greatest number
a=int(input("Enter value for a\n"))
b=int(input("Enter value for b\n"))
greater=a if a>b else b
print("The greater number among the given value is\n",greater)
#ternary operator type 2
# clever if ternary operator
age=int(input("Enter age\n"))
vote=("Yes","No") [age<=18]
print(vote)
