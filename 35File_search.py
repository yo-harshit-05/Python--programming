word="good"
data=True
line=1
flag=0
with open("practice.txt","r") as f:
    while data:
        data=f.readline()
        if word in data:
            print(f"Found at {line} line")
            flag=1
            break
        line+=1
if flag==0:
    print("The word not found")
