with open("practice.txt","w") as f:
    f.write("Hi Everyone\nToday I am going to learn java.\n")
    f.write("The java is a very good language.\n")
    f.close()
with open("practice.txt","r") as f:
    data=f.read()
    newdata=data.replace("java","python")
with open("practice.txt","w") as f:
    f.write(newdata)

