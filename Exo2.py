def calculate_bmi(poids, taille):
    """Calcule l'IMC à partir du poids (kg) et de la taille (m), et retourne l'IMC arrondi à deux décimales."""
    imc = poids / (taille ** 2)
    return round(imc, 2)

def obtenir_categorie_sante(imc):
    """Retourne la catégorie de santé basée sur l'IMC."""
    if imc < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= imc < 25:
        return "Poids normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obésité"

def convertir_poids_livres_en_kg(poids_livres):
    """Convertit le poids de livres en kilogrammes."""
    return poids_livres / 2.20462

def convertir_taille_pouces_en_metres(taille_pouces):
    """Convertit la taille de pouces en mètres."""
    return taille_pouces / 39.3701

def main():
    print("Bienvenue dans le calculateur d'IMC!")
    unite_poids = input("Voulez-vous entrer le poids en kilogrammes (kg) ou en livres (lb)? ").strip().lower()
    unite_taille = input("Voulez-vous entrer la taille en mètres (m) ou en pouces (in)? ").strip().lower()

    if unite_poids == "kg":
        poids = float(input("Entrez votre poids en kilogrammes: "))
    elif unite_poids == "lb":
        poids_livres = float(input("Entrez votre poids en livres: "))
        poids = convertir_poids_livres_en_kg(poids_livres)
    else:
        print("Unité de poids non reconnue.")
        return

    if unite_taille == "m":
        taille = float(input("Entrez votre taille en mètres: "))
    elif unite_taille == "in":
        taille_pouces = float(input("Entrez votre taille en pouces: "))
        taille = convertir_taille_pouces_en_metres(taille_pouces)
    else:
        print("Unité de taille non reconnue.")
        return

    imc = calculate_bmi(poids, taille)
    categorie = obtenir_categorie_sante(imc)

    print(f"Votre IMC est de {imc}. Catégorie de santé : {categorie}.")
