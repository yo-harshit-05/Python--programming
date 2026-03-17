bnum = int(input("Enter Number in binary you want to convert to decimal\n"))
result = 0
i = 0
while bnum > 0:
    rem = bnum % 10
    if rem == 1:
        result += rem * (2 ** i)
    bnum //= 10
    i += 1
print(result)