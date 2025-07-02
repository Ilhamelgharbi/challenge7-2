notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
moy = sum(notes) / len(notes)
print("La moyenne des notes est :", moy)
max_note = 0
print("Les notes maximales sont de la moyenne :")
for i in notes :
    if i>moy:
        max_note = i
        print(max_note)




