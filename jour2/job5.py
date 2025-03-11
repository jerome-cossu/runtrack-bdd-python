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

cursor.execute("select sum(superficie) from etage")

superficie = cursor.fetchone()

superficie_totale = superficie[0]

print (f"La superficie de La Plateforme est de {superficie_totale} m²")

cursor.close()
conn.close