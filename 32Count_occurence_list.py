# WAP to count occurence of each element in a list
l1 = [12, 23, 23, 56, 67, 24]

for x in set(l1):
    print(x, ":", l1.count(x))