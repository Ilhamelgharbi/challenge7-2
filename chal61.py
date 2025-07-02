from math import sqrt
x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))
y1=float(input("Enter y1: "))
y2=float(input("Enter y2: "))
a=pow(x2-x1,2)
b=pow(y2-y1,2)
c=a+b
d=sqrt(c)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is:\n {d}")