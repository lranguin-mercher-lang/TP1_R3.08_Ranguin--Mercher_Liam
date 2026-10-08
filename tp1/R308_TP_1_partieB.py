# ==============================================================================
# TP1 - R3.08 : POO Python
# Partie B : Mini-jeu « Devine le nombre »
# Auteur : Liam Ranguin--Mercher
# ==============================================================================

import random

def devine_le_nombre():
    """Jeu de devinette d'un nombre secret entre 1 et 100 en 10 essais max."""
    nombre_secret = random.randint(1, 100)
    essais_max = 10
    
    print("=== Jeu : Devine le nombre secret (entre 1 et 100) ===")
    print(f"Vous avez {essais_max} essais pour trouver le nombre.\n")

    for essai in range(1, essais_max + 1):
        # Saisie sécurisée d'un entier
        try:
            proposition = int(input(f"Essai {essai}/{essais_max} - Votre proposition : "))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
            continue

        # Vérification de la proposition
        if proposition < nombre_secret:
            print("Trop petit !")
        elif proposition > nombre_secret:
            print("Trop grand !")
        else:
            print(f"\nGagné ! Vous avez trouvé le nombre secret ({nombre_secret}) en {essai} essai(s).")
            return

    print(f"\nPerdu ! Le nombre secret était {nombre_secret}.")

if __name__ == "__main__":
    devine_le_nombre()