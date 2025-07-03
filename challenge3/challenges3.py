stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]
ch1 =[]
ch2 =[]

for i in stock :
    print(i)
    if str(i)==i:
        ch1.append(i)
    else:
        ch2.append(i)
print( stock)
print("Liste des chaînes de caractères:", ch1)
print("Liste des nombres:", ch2)
def tri_liste(ch1):
    n = len(ch1)-1
    for i in range(n):
        for j in range(0, n - i - 1):
            if ch1[j] > ch1[j + 1]:
                ch1[j], ch1[j + 1] = ch1[j + 1], ch1[j]
    return ch1
       

def tri_num_decroissant(ch2):
    n = len(ch2)-1
    for i in range(n):
        for j in range(0, n - i - 1):
            if ch2[j] < ch2[j + 1]:  
                ch2[j], ch2[j + 1] = ch2[j + 1], ch2[j]
    return ch2

ch1 = tri_liste(ch1)
ch2 = tri_num_decroissant(ch2)
print("Liste des chaînes de caractères triee :", ch1)
print("Liste des nombres triee :", ch2)
