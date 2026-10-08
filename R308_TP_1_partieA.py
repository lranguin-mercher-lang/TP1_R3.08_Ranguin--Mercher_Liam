def ajouter_etudiant(d, nom, note):
    d[nom] = note

def moyenne_classe(d):
    return sum(d.values()) / len(d)

etudiants = {}
ajouter_etudiant(etudiants, "Djo", 14.5)
ajouter_etudiant(etudiants, "Xav", 12.0)
ajouter_etudiant(etudiants, "Emma", 16.5)
ajouter_etudiant(etudiants, "Djo", 18.0)
print(etudiants)
print("La moyenne est de : ", moyenne_classe(etudiants))

def meilleur_etudiant(d):
   meilleure_note = max(d.values())
   for nom, note in d.items():
            if note == meilleure_note :
                return(nom, note)
            
print("Le meilleur étudiant est : " , meilleur_etudiant(etudiants))

with open("exemple.txt", "w") as f:
    f.write("bonjour\n")
      
   
