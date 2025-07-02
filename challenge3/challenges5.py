L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
def occ(l: list, a: int) -> int:
    occ = 0
    for i in l:
        if i == a:
            occ += 1
    return occ
a=int(input("enter a int "))
occurrence = occ(L, a)
print(f"5 appeared {occurrence} times")