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
    print("La connexion a la base de donner est etablie")

    cursor = connexion.cursor()

    cursor.execute("select nom, capacite from salle")

    resultat = cursor.fetchall()

    for row in resultat :
        print(f"{row[0]}, {row[1]}")

cursor.close()
connexion.close()
