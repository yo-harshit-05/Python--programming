# WAP to remove odd and print even from list 

l1=[12,23,23,56,67,24]
print(list(i for i in l1 if i%2==0))


# WAP to replicate the value that number of time 

l2=[2,3,4]
l3=[]
for i in l2:
    for j in range(0,i):
        l3.append(i)
print(l3)