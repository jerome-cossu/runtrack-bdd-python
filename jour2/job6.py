import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mot_de_passe = os.getenv("MOT_DE_PASSE")

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=mot_de_passe,
    database="LaPlateforme"
)

if conn.is_connected():
    print("Connecté à la base de données")

cursor = conn.cursor()

cursor.execute("select sum(capacite) from salle")

capacite_totale = cursor.fetchone()

capacite_totale = capacite_totale[0]

print(f"La capacité totale des salles est de {capacite_totale}")

cursor.close()
conn.close