# Counting Numbers in file 
with open("Numbers.txt","w")as f:
    f.write("12,34,23,45,34,56,67,78,89")
    
with open("Numbers.txt","r") as f:
    data=f.read()
    numbers = list(map(int, data.split(",")))  # convert to list of ints
    flg=0
    for i in numbers:
        if i%2==0:
            flg+=1
    print("The numbers of even numbers are",flg)
