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
    print("La connexion a la base de données est établie")

    cursor = connexion.cursor()

    cursor.execute("select * from etudiant")

    resultat = cursor.fetchall()
    for row in resultat:
        print(row)

else : 
    print("La connexion a la base de données a échoué")

cursor.close()
connexion.close()

