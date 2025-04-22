# Program 9 : quadratic equation roots

import math
print("The given equation is in the form of \nax²+bx+c=0\nSo enter the values of a,b and c ")
a=int(input("Enter values for a\n"))
b=int(input("Enter values for b\n"))
c=int(input("Enter values for c\n"))
print(f"Hence the equation formed is\n{a}x²+{b}x+{c}")
discriminant=b**2-4*a*c
if discriminant>0:
    print("Roots are real and distinct")
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print(f"Root1={root1},Root2={root2}")
elif discriminant==0:
    print("Roots are real and same")
    root=(-b/(2*a))
    print("root 1 and 2 =",root)
else:
    print("Roots are imaginary")
    real_part=(-b/(2*a))
    imaginary_part=(math.sqrt(abs(discriminant))/(2*a))
    print(f"Root1={real_part}+i{imaginary_part}")
    print(f"Root2={real_part}-i{imaginary_part}")
