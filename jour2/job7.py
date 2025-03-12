import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
mot_de_passe = os.getenv('MOT_DE_PASSE')

class Employe:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.curseur = self.connexion.cursor()
    
    def ajouter_employe(self, nom, prenom, salaire, id_service):
        requete = "insert into employe (nom, prenom, salaire, id_service) values (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, values)
        self.connexion.commit()
        print(f"Employé {nom} {prenom} ajouté avec succès")

    def afficher_employes(self):
        requete = "select * from employe"
        self.curseur.execute(requete)
        resultat = self.curseur.fetchall()
        for row in resultat:
            print(row)
    
    def afficher_employes_salaire(self, salaire_min):
        requete = "select * from employe where salaire >= %s"
        values = (salaire_min,)
        self.curseur.execute(requete, values)
        resultat = self.curseur.fetchall()
        for row in resultat:
            print(row)
    
    def mettre_a_jour_salaire(self, id_employe, nouveau_salaire):
        requete = "update employe set salaire = %s where id = %s"
        values = (nouveau_salaire, id_employe)
        self.curseur.execute(requete, values)
        self.connexion.commit()
        print(f"Salaire de l'employé {id_employe} est mis à jour avec succès")
    
    def supprimer_employe(self, id_employe):
        requete = "delete from employe where id = %s"
        self.curseur.execute(requete, (id_employe,))
        self.connexion.commit()
        print(f"Employé {id_employe} supprimé avec succès")

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

if __name__ == '__main__':
    db = Employe(host = "127.0.0.1", user = "root", password = mot_de_passe, database="entreprise")
    db.ajouter_employe("Vador", "Dark", 4000, 1)

    print("Affichage des employés") 
    db.afficher_employes()

    print("\nEmployes avec un salaire supérieur à 3000 € :")
    db.afficher_employes_salaire(3000)
    db.mettre_a_jour_salaire(1, 3800.00)
    db.supprimer_employe(2)
    db.fermer_connexion()