def ajouter_etudiant(d, nom, note):
    """Ajoute ou met à jour la note d'un étudiant dans le dictionnaire."""
    d[nom] = note


def moyenne_classe(d):
    """Calcule et renvoie la moyenne des notes de la classe."""
    if not d:
        return 0.0
    return sum(d.values()) / len(d)


def meilleur_etudiant(d):
    """Cherche et renvoie le nom et la note du meilleur étudiant."""
    if not d:
        return None
    meilleure_note = max(d.values())
    for nom, note in d.items():
        if note == meilleure_note:
            return (nom, note)


# --- 1. Saisie et test des fonctions ---
etudiants = {}

ajouter_etudiant(etudiants, "Djo", 14.5)
ajouter_etudiant(etudiants, "Xav", 12.0)
ajouter_etudiant(etudiants, "Emma", 16.5)
ajouter_etudiant(etudiants, "Djo", 18.0)  # Remplace 14.5 par 18.0 pour Djo

print("Dictionnaire initial :", etudiants)
print("La moyenne est de :", moyenne_classe(etudiants))
print("Le meilleur étudiant est :", meilleur_etudiant(etudiants))


# --- 2. Sauvegarde dans un fichier texte ---
with open("etudiants.txt", "w", encoding="utf-8") as f:
    for nom, note in etudiants.items():
        f.write(f"{nom}:{note}\n")


# --- 3. Rechargement depuis le fichier texte ---
etudiants_recharges = {}

with open("etudiants.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()  # Supprime les espaces et sauts de ligne
        if ligne:
            nom, note_str = ligne.split(":")
            etudiants_recharges[nom] = float(note_str)

print("Dictionnaire rechargé depuis le fichier :", etudiants_recharges)