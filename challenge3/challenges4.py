def rechercheElement(ch: str, mot: str) :
    for i in range(len(ch)-1):
        if ch[i] == mot:
            return i
    return False 
ch = input("entrer une chaine :")
mot = input("entrer le mot chercher :") 
rechercheElement(ch, mot) 


        
