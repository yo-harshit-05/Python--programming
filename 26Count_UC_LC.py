# Count total number of upper case and lower case
sent=input("Enter Sentence\n")
strupper,strlower=0,0
for i in sent:
    if i>='A'and i<'Z' :
        strupper+=1
    if i>='a'and i<'z' :
        strlower+=1
print(f"The total number of uppercase are {strupper}\nThe total number of lowercase are {strlower}")