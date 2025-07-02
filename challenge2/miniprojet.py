def factorielle (n: int)-> int:
    if n<0 :
        return None
    elif n==0 or n==1 :
        return 1
    else :
        factor= 1
        for i in range(2 , n+1):
            factor*=i
        return factor
def table_multiplication (m: int) -> None:
        for i in range (1 , 11):
             print (f" {m}*{i} = {m*i}")
def is_carre_parfait (c : int)-> bool:
    if c<0 :
        return False
    racine = int(c ** 0.5)
    return racine * racine == c 
def afficher_caracteres (chaine: str) -> None:
    for caractere in chaine:
        print(caractere)

def mot_le_plus_long (phrase: str) -> str:
    mots = phrase.split()
    mot_long = ""
    for mot in mots:
        if len(mot) > len(mot_long):
            mot_long = mot
    return mot_long

def compter_occurrences (ch: str) -> None:
    for caractere in set(ch):
        nombre = ch.count(caractere)
        print(f"'{caractere}': {nombre}")



def menu():
    while True:
        print("\n" + "="*40)
        print("MINI-PROJET PYTHON")
        print("="*40)
        print("1. Calculer la factorielle d'un nombre")
        print("2. Afficher la table de multiplication")
        print("3. Vérifier si un nombre est un carré parfait")
        print("4. Afficher les caractères d'une chaîne")
        print("5. Trouver le mot le plus long")
        print("6. Compter les occurrences des caractères")
        print("0. Quitter")

        choix = input("Choisissez une option: ")
        
        if choix == '0':
            break
        elif choix == '1':
            n = int(input("Entrez un nombre pour la factorielle: "))
            print(f"Factorielle de {n}: {factorielle(n)}")
        elif choix == '2':
            m = int(input("Entrez un nombre pour la table: "))
            table_multiplication(m)
        elif choix == '3':
            c = int(input("Entrez un nombre pour tester carré parfait: "))
            print(f"{c} est carré parfait: {is_carre_parfait(c)}")
        elif choix == '4':
            chaine = input("Entrez une chaîne: ")
            afficher_caracteres(chaine)
        elif choix == '5':
            phrase = input("Entrez une phrase: ")
            print(f"Mot le plus long: {mot_le_plus_long(phrase)}")
        elif choix == '6':
            ch = input("Entrez une chaîne pour compter: ")
            compter_occurrences(ch)
        else:
            print("Option invalide, veuillez réessayer.")      
