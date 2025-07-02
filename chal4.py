n1=int(input("enter a number"))
n2=int(input("enter another number"))
n=n1*n2
try :
    if n>0 :
        print("the result is positive")
    elif n<0 :
        print("the result is negative")
    else:
        print("the result is zero")
except ValueError:
    print("Please enter valid numeric values.")