import math
a=int(input("Enter a\n"))
b=int(input("Enter b\n"))
c=int(input("Enter c\n"))

if a==0:
    while a==0:
        print("Please give a suitable value")
        a=int(input("Enter a"))

D=(b*b)-(4*a*c)

if D>0:
    print(-b+math.sqrt(D)/2*a)
    print(-b-math.sqrt(D)/2*a)
elif D==0:

    print((-b/2*a))

else:
    print("Imaginary number")


