# Accept string and return after removing vowels

str1=input("Enter any word\n")
newstr=""
v="aeiouAEIOU"
for i in range(len(str1)):
    if str1[i] in v:
        continue
    newstr+=str1[i]
print(newstr)