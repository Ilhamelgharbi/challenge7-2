import string
chaine = str(input("Enter a string: "))
s=""
i= len(chaine)-1
while i>=0 :
    s+=chaine[i]
    i-=1
print(f"l inverse est {s}")


 
