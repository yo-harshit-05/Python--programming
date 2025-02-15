#length Function
str="ram is a good Boy."
length=len(str)
print(length)
#Concatenation
str2="He likes to play cricket"
str3=str+str2
print(str3)
#How to access string 
for i in range(0,len(str),2):
    print(str[i])
#slicing of string
print(str[0:4])
#string function
print(str.endswith("oy")) #returns true if string ends with substr 
print(str.capitalize( )) #capitalizes 1st char 
str=str.replace( "Boy", "Man" ) #replaces all occurrences of old 
print(str.find("a")) #returns 1st index of 1st occurrer 
print(str.count("to")) #counts the occurrence of substr 

