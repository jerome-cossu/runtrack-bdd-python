import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
mot_de_passe = os.getenv("MOT_DE_PASSE")

connexion = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = mot_de_passe,
    database = "LaPlateforme"
)

if connexion.is_connected():
    print("La connexion à la base de données est établie")

    cursor = connexion.cursor()
    requete = "select sum(superficie) from etage"
    cursor.execute(requete)

    resultat = cursor.fetchone()

    if resultat[0]:
        print(f"La superficie de LaPlateforme est de {resultat[0]} m²")

cursor.close()
connexion.close()