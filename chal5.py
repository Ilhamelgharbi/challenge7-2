N=int(input("enter an integer:"))
try :
    S=0
    while N>0 :
        S+=N
        N-=1
    print(f"the sum  is {S}")
except ValueError:
    print("Please enter a valid integer.")
