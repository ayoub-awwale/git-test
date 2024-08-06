import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print(" ".join(ligne))
    print()

def creer_plateau(n, m):
    return [["*" for _ in range(m)] for _ in range(n)]

def positionner_tresor(n, m):
    while True:
        try:
            ligne = int(input(f"Entrez le numéro de ligne (0 à {n-1}) pour cacher le trésor: "))
            colonne = int(input(f"Entrez le numéro de colonne (0 à {m-1}) pour cacher le trésor: "))
            if 0 <= ligne < n and 0 <= colonne < m:
                return ligne, colonne
            else:
                print("Position invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée non valide. Veuillez entrer des numéros valides.")

def positionner_piege(n, m, ligne_tresor, colonne_tresor):
    while True:
        ligne_piege = random.randint(0, n-1)
        colonne_piege = random.randint(0, m-1)
        if (ligne_piege != ligne_tresor) or (colonne_piege != colonne_tresor):
            return ligne_piege, colonne_piege

def deviner_tresor(n, m):
    while True:
        try:
            ligne = int(input(f"Devinez le numéro de ligne (0 à {n-1}) du trésor: "))
            colonne = int(input(f"Devinez le numéro de colonne (0 à {m-1}) du trésor: "))
            if 0 <= ligne < n and 0 <= colonne < m:
                return ligne, colonne
            else:
                print("Position invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée non valide. Veuillez entrer des numéros valides.")

def jeu_chasse_tresor():
    print("Bienvenue dans le jeu de chasse au trésor!")
    n = int(input("Entrez le nombre de lignes du plateau: "))
    m = int(input("Entrez le nombre de colonnes du plateau: "))

    plateau = creer_plateau(n, m)
    afficher_plateau(plateau)

    ligne_tresor, colonne_tresor = positionner_tresor(n, m)
    ligne_piege, colonne_piege = positionner_piege(n, m, ligne_tresor, colonne_tresor)
    
    plateau[ligne_tresor][colonne_tresor] = "T"
    plateau[ligne_piege][colonne_piege] = "X"
    
    print("Le trésor et le piège ont été placés.")
    afficher_plateau(plateau)
    
    while True:
        ligne_devinee, colonne_devinee = deviner_tresor(n, m)
        
        if ligne_devinee == ligne_tresor and colonne_devinee == colonne_tresor:
            print("Félicitations! Vous avez trouvé le trésor!")
            break
        elif ligne_devinee == ligne_piege and colonne_devinee == colonne_piege:
            print("Oh non! Vous êtes tombé dans le piège!")
            break
        else:
            print("Pas de trésor ici. Essayez encore!")