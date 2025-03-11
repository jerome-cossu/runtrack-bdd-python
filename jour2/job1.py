import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mot_de_passe = os.getenv("MOT_DE_PASSE")

connexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=mot_de_passe,
    database="laplateforme"
)

if connexion.is_connected():
    print("Connecté à la base de données")
else:
    print("Erreur de connexion")

curseur = connexion.cursor()

requete = "select * from etudiant"
curseur.execute(requete)

students = curseur.fetchall()

print("Liste des étudiants :")
for student in students:
    print(student)

curseur.close()
connexion.close()