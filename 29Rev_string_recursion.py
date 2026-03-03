#Reversing a string using recursion
def rev(s):
    if len(s) == 0:
        return s
    return rev(s[1:]) + s[0]
text = input("Enter a string: ")
print("Reversed string:", rev(text))