# Program 15 : To print all prime number between 1 to 10
lower=1
upper=10
print(f"The prime numbers between {lower} and {upper} are:\n ")
for num in range(lower,upper+1):
    if num>1:
        for i in range (2,num):
            if num%i==0:
                break
        else:
            print(num)
