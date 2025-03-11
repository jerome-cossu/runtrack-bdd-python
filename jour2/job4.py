import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mot_de_passe = os.getenv("MOT_DE_PASSE")

conn = mysql.connector.connect(
    host="127.0.0.1",            
    user="root",      
    password=mot_de_passe, 
    database="LapLateforme"      
)

if conn.is_connected():
    print("Connecté à la base de données")
else:
    print("Erreur de connexion")

cursor = conn.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

salles = cursor.fetchall()

for salle in salles:
    nom, capacite = salle
    print(salle, salle)

cursor.close()
conn.close()
